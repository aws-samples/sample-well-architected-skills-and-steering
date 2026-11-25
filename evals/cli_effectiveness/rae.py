#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Retrieval-Invoked Actual-Use Effect (RAE) for the WA-review harness.

Implements the paired, same-task actual-use estimator from Cho & Park,
"Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents"
(Findings of EMNLP 2026, arXiv:2609.00549), adapted to this repo's F1 harness.

WHY
---
The effectiveness harness reports *aggregate* F1 (recall/precision) for a
skill-enabled (SE) configuration and, separately, for a skill-disabled (SD)
baseline. The MCP-vs-static experiment famously found aggregate parity
(F1 delta +/- 0.0024). The RAE paper shows aggregate parity/lift can hide a
mix of rescues and harms that net to zero: a retrieval source can help on some
items and hurt on others while the mean looks flat. RAE isolates the net effect
on exactly the items where the retrieval actually fired.

ADAPTATION TO THIS HARNESS
--------------------------
The paper's unit is a *task* with a binary correct/incorrect outcome. Here the
natural matched unit is a **(case, best-practice)** pair, with the binary
outcome "the review correctly cited this applicable (ground-truth) BP". For each
such unit we compare the SE configuration against the SD baseline:

    helpful flip  (b): SD missed the GT BP, SE cited it     -> +1
    harmful flip  (c): SD cited the GT BP, SE dropped it     -> -1
    concordant       : both cited, or both missed            ->  0

    RAE = 100 * (b - c) / n_cond

`n_cond` is the size of the *conditioned* unit set: all (case, BP) pairs where
BP is in ground truth for the case AND the case is one where the SE retrieval
source actually fired (`--conditioned-cases`, or a per-run signal, else all SE
cases as an explicit fallback).

DEVIATIONS FROM THE PAPER (stated honestly)
-------------------------------------------
* Matching granularity. The paper matches single SE/SD executions by shared
  seed. The Claude Code CLI runs here are not seed-reproducible, so we collapse
  the N runs per side into a per-(case, BP) hit via a voting rule
  (`--vote any|majority|all`, default majority) and match at the case level.
* Outcome axis. Units are restricted to ground-truth BPs, so RAE here is a
  recall-flip measure (did the source rescue more applicable BPs than it
  dropped). A precision-side variant over the canonical-minus-GT universe is
  possible but not computed here.
* Interpretation. As in the paper, RAE is a protocol-conditional paired signal,
  NOT an unbiased causal effect: the conditioned set is self-selected by the SE
  configuration. The paper's own Limitations note the paradox's prevalence and
  magnitude are not established for long-horizon / multi-subagent agents, which
  is exactly what the full WA review is. Treat RAE as most meaningful on the
  genuinely conditional surfaces (MCP sourcing; lens loading), not the always-on
  core review.

OUTPUT
------
Per-case and pooled b / c / n_cond / RAE, an exact McNemar two-sided p-value and
a bootstrap CI over the unit outcomes, and the OAE = (n_cond/n_all)*RAE +
(n_skip/n_all)*delta_skip decomposition (Eq. 4/12 of the paper) as a sanity
check. Cells with n_cond < --min-cond (default 10, the paper's threshold) are
flagged non-reportable.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
from dataclasses import dataclass, field
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
GT_DIR = SCRIPT_DIR / "ground_truth"

# Case 4 is a pillar-scoped (SEC+REL) eval; ground truth is scored against that
# subset, matching measure_aws_knowledge_mcp.py.
PILLAR_SCOPED_CASES = {4: ("SEC", "REL")}

DEFAULT_MIN_COND = 10          # paper's n_cond >= 10 reporting threshold
DEFAULT_BOOTSTRAP = 20_000     # paper uses 20k paired resamples
DEFAULT_SEED = 42


# --------------------------------------------------------------------------- #
# Loading
# --------------------------------------------------------------------------- #
def load_ground_truth(case_id: int) -> set[str]:
    data = json.loads((GT_DIR / f"case_{case_id}.json").read_text())
    gt = set(data["ground_truth"]["consensus_bps"])
    prefixes = PILLAR_SCOPED_CASES.get(case_id)
    if prefixes:
        gt = {b for b in gt if b.startswith(prefixes)}
    return gt


def load_run_bps(result_path: Path, scope: str) -> dict[int, list[set[str]]]:
    """case_id -> list of BP sets, one per SUCCESSFUL run.

    `scope` selects which citation set to read: "report" (user-facing assembled
    report) or "subagent_total" (every subagent's combined citations).
    """
    data = json.loads(result_path.read_text())
    out: dict[int, list[set[str]]] = {}
    for case in data.get("cases", []):
        cid = int(case["case_id"])
        sets: list[set[str]] = []
        for run in case.get("runs", []):
            if "error" in run:
                continue
            block = run.get(scope) or {}
            bps = block.get("valid_cited_bps")
            if bps is None:
                continue
            sets.append(set(bps))
        if sets:
            out[cid] = sets
    return out


# --------------------------------------------------------------------------- #
# Voting: collapse N runs per side into a per-BP hit
# --------------------------------------------------------------------------- #
def vote_hit(bp: str, run_sets: list[set[str]], rule: str) -> bool:
    n = len(run_sets)
    hits = sum(1 for s in run_sets if bp in s)
    if rule == "any":
        return hits > 0
    if rule == "all":
        return hits == n
    # majority (default): strict majority of successful runs
    return hits >= math.ceil(n / 2)


# --------------------------------------------------------------------------- #
# Core estimator
# --------------------------------------------------------------------------- #
@dataclass
class CaseUnits:
    case_id: int
    b: int = 0            # helpful flips (SD miss -> SE hit)
    c: int = 0            # harmful flips (SD hit -> SE miss)
    n: int = 0            # conditioned units (all GT BPs in universe for the case)
    units: list[int] = field(default_factory=list)  # per-unit +1/0/-1

    @property
    def rae(self) -> float | None:
        return None if self.n == 0 else 100.0 * (self.b - self.c) / self.n


def paired_units(
    se: dict[int, list[set[str]]],
    sd: dict[int, list[set[str]]],
    gt_by_case: dict[int, set[str]],
    conditioned_cases: set[int],
    vote: str,
    universe_prefixes: tuple[str, ...] | None,
) -> tuple[list[CaseUnits], list[CaseUnits]]:
    """Return (conditioned_case_units, all_case_units).

    A case contributes only if it has >=1 successful SE run AND >=1 successful
    SD run. `all_case_units` covers every paired case (for OAE); the conditioned
    list is the subset in `conditioned_cases` (for RAE).
    """
    all_units: list[CaseUnits] = []
    for cid in sorted(set(se) & set(sd)):
        gt = gt_by_case.get(cid, set())
        if universe_prefixes:
            gt = {b for b in gt if b.startswith(universe_prefixes)}
        if not gt:
            continue
        cu = CaseUnits(case_id=cid)
        for bp in sorted(gt):
            se_hit = vote_hit(bp, se[cid], vote)
            sd_hit = vote_hit(bp, sd[cid], vote)
            if se_hit and not sd_hit:
                cu.b += 1
                cu.units.append(+1)
            elif sd_hit and not se_hit:
                cu.c += 1
                cu.units.append(-1)
            else:
                cu.units.append(0)
            cu.n += 1
        all_units.append(cu)
    conditioned = [cu for cu in all_units if cu.case_id in conditioned_cases]
    return conditioned, all_units


def mcnemar_exact_p(b: int, c: int) -> float | None:
    """Two-sided exact McNemar p over discordant counts (binomial, p=0.5)."""
    n = b + c
    if n == 0:
        return None
    k = min(b, c)
    tail = sum(math.comb(n, i) for i in range(0, k + 1)) * (0.5 ** n)
    return min(1.0, 2.0 * tail)


def bootstrap_ci(
    units: list[int], resamples: int, seed: int, alpha: float = 0.05
) -> tuple[float, float] | None:
    """Percentile CI for RAE (=100*mean(units)) via paired unit resampling."""
    n = len(units)
    if n == 0:
        return None
    rng = random.Random(seed)
    means: list[float] = []
    for _ in range(resamples):
        s = sum(units[rng.randrange(n)] for _ in range(n))
        means.append(100.0 * s / n)
    means.sort()
    lo = means[int((alpha / 2) * resamples)]
    hi = means[min(resamples - 1, int((1 - alpha / 2) * resamples))]
    return round(lo, 2), round(hi, 2)


def pooled(case_units: list[CaseUnits]) -> tuple[int, int, int, list[int]]:
    b = sum(cu.b for cu in case_units)
    c = sum(cu.c for cu in case_units)
    n = sum(cu.n for cu in case_units)
    units: list[int] = []
    for cu in case_units:
        units.extend(cu.units)
    return b, c, n, units


def compute_rae(
    se: dict[int, list[set[str]]],
    sd: dict[int, list[set[str]]],
    gt_by_case: dict[int, set[str]],
    conditioned_cases: set[int],
    vote: str = "majority",
    universe_prefixes: tuple[str, ...] | None = None,
    min_cond: int = DEFAULT_MIN_COND,
    bootstrap: int = DEFAULT_BOOTSTRAP,
    seed: int = DEFAULT_SEED,
) -> dict:
    conditioned, all_units = paired_units(
        se, sd, gt_by_case, conditioned_cases, vote, universe_prefixes
    )

    # RAE over the conditioned subset
    b, c, n_cond, cond_unit_vals = pooled(conditioned)
    rae = None if n_cond == 0 else round(100.0 * (b - c) / n_cond, 2)

    # OAE over all paired cases + skip decomposition (Eq. 4/12)
    all_b, all_c, n_all, _ = pooled(all_units)
    oae = None if n_all == 0 else round(100.0 * (all_b - all_c) / n_all, 2)
    skip_b, skip_c, n_skip = all_b - b, all_c - c, n_all - n_cond
    delta_skip = None if n_skip == 0 else round(100.0 * (skip_b - skip_c) / n_skip, 2)

    return {
        "vote": vote,
        "scope_note": "unit = (case, ground-truth BP); outcome = correctly cited",
        "universe_prefixes": list(universe_prefixes) if universe_prefixes else None,
        "conditioned_cases": sorted(conditioned_cases),
        "reportable": n_cond >= min_cond,
        "min_cond": min_cond,
        "rae": {
            "value": rae,
            "helpful_b": b,
            "harmful_c": c,
            "n_cond": n_cond,
            "mcnemar_p": (
                round(p, 6) if (p := mcnemar_exact_p(b, c)) is not None else None
            ),
            "ci95": bootstrap_ci(cond_unit_vals, bootstrap, seed),
        },
        "oae": {"value": oae, "helpful_b": all_b, "harmful_c": all_c, "n_all": n_all},
        "delta_skip": {
            "value": delta_skip,
            "helpful_b": skip_b,
            "harmful_c": skip_c,
            "n_skip": n_skip,
        },
        "decomposition_check": _decomposition_check(oae, rae, delta_skip, n_cond, n_skip, n_all),
        "per_case": [
            {
                "case_id": cu.case_id,
                "rae": round(cu.rae, 2) if cu.rae is not None else None,
                "helpful_b": cu.b,
                "harmful_c": cu.c,
                "n": cu.n,
                "conditioned": cu.case_id in conditioned_cases,
            }
            for cu in all_units
        ],
    }


def _decomposition_check(oae, rae, delta_skip, n_cond, n_skip, n_all) -> dict:
    """Verify OAE == (n_cond/n_all)*RAE + (n_skip/n_all)*delta_skip."""
    if oae is None or n_all == 0:
        return {"ok": None}
    recon = 0.0
    if rae is not None:
        recon += (n_cond / n_all) * rae
    if delta_skip is not None:
        recon += (n_skip / n_all) * delta_skip
    return {"ok": abs(recon - oae) < 1e-6, "reconstructed_oae": round(recon, 4)}


# --------------------------------------------------------------------------- #
# Conditioning signal
# --------------------------------------------------------------------------- #
def infer_conditioned_cases(
    se_path: Path, explicit: list[int] | None, field_name: str | None
) -> tuple[set[int], str]:
    """Decide which cases count as 'retrieval actually fired' for RAE.

    Priority:
      1. --conditioned-cases explicit list.
      2. A per-run integer/boolean field (e.g. a recorded MCP tool-call count);
         a case is conditioned if any successful run has field > 0 / True.
      3. Fallback: every case in the SE file, flagged as an explicit fallback so
         the reader knows RAE has collapsed toward case-level OAE.
    """
    data = json.loads(se_path.read_text())
    all_cases = {int(c["case_id"]) for c in data.get("cases", [])}
    if explicit:
        return set(explicit) & all_cases, "explicit"
    if field_name:
        fired: set[int] = set()
        for case in data.get("cases", []):
            for run in case.get("runs", []):
                if "error" in run:
                    continue
                v = run.get(field_name)
                if isinstance(v, bool) and v:
                    fired.add(int(case["case_id"]))
                elif isinstance(v, (int, float)) and v > 0:
                    fired.add(int(case["case_id"]))
        return fired, f"field:{field_name}"
    return all_cases, "all_cases_fallback"


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def _print_report(label: str, res: dict, conditioning: str) -> None:
    r = res["rae"]
    print(f"\n=== RAE: {label} ===")
    print(f"  conditioning: {conditioning} (cases {res['conditioned_cases']})")
    print(f"  vote={res['vote']}  universe={res['universe_prefixes'] or 'GT (all pillars)'}")
    flag = "" if res["reportable"] else f"  [NOT REPORTABLE: n_cond<{res['min_cond']}]"
    print(f"  RAE = {r['value']} pp   (helpful b={r['helpful_b']}, harmful c={r['harmful_c']}, "
          f"n_cond={r['n_cond']}){flag}")
    if r["ci95"]:
        print(f"        95% CI {r['ci95']}   McNemar p={r['mcnemar_p']}")
    o = res["oae"]
    print(f"  OAE = {o['value']} pp   (b={o['helpful_b']}, c={o['harmful_c']}, n_all={o['n_all']})")
    ds = res["delta_skip"]
    print(f"  delta_skip = {ds['value']} pp (n_skip={ds['n_skip']})   "
          f"decomposition_ok={res['decomposition_check'].get('ok')}")
    print("  per-case RAE:")
    for pc in res["per_case"]:
        mark = "*" if pc["conditioned"] else " "
        print(f"   {mark} case {pc['case_id']}: RAE={pc['rae']} "
              f"(b={pc['helpful_b']} c={pc['harmful_c']} n={pc['n']})")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Compute the Retrieval-Invoked Actual-Use Effect (RAE) between a "
        "skill-enabled (SE) result file and a skill-disabled (SD) baseline file.",
    )
    p.add_argument("--se", type=Path, required=True,
                   help="SE (retrieval-enabled) result JSON, e.g. aws_knowledge_mcp_effectiveness.json")
    p.add_argument("--sd", type=Path, required=True,
                   help="SD (baseline) result JSON, e.g. wa_review_effectiveness.json (static) "
                        "or wa_review_baseline.json (no skill)")
    p.add_argument("--scope", choices=["report", "subagent_total"], default="subagent_total",
                   help="Which citation set to read from each run (default: subagent_total).")
    p.add_argument("--vote", choices=["any", "majority", "all"], default="majority",
                   help="How to collapse N runs per side into a per-BP hit (default: majority).")
    p.add_argument("--pillars", nargs="+", default=None,
                   help="Restrict the unit universe to GT BPs with these prefixes "
                        "(e.g. SEC REL). Used for the lens surface.")
    p.add_argument("--conditioned-cases", type=int, nargs="+", default=None,
                   help="Cases where the SE retrieval actually fired (RAE conditioning set). "
                        "Omit to infer from --conditioned-field or fall back to all SE cases.")
    p.add_argument("--conditioned-field", default=None,
                   help="Per-run field name whose >0/True value marks retrieval as fired "
                        "(e.g. mcp_tool_calls). Used only if --conditioned-cases is omitted.")
    p.add_argument("--min-cond", type=int, default=DEFAULT_MIN_COND,
                   help=f"Minimum n_cond to mark a cell reportable (default: {DEFAULT_MIN_COND}).")
    p.add_argument("--bootstrap", type=int, default=DEFAULT_BOOTSTRAP,
                   help=f"Bootstrap resamples for the CI (default: {DEFAULT_BOOTSTRAP}).")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--label", default="SE vs SD")
    p.add_argument("--output", type=Path, default=None, help="Write the full result JSON here.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    for path in (args.se, args.sd):
        if not path.exists():
            print(f"error: result file not found: {path}", file=sys.stderr)
            return 2

    se = load_run_bps(args.se, args.scope)
    sd = load_run_bps(args.sd, args.scope)
    if not (set(se) & set(sd)):
        print("error: SE and SD share no cases with successful runs", file=sys.stderr)
        return 2

    gt_by_case = {cid: load_ground_truth(cid) for cid in set(se) | set(sd)}
    conditioned, conditioning = infer_conditioned_cases(
        args.se, args.conditioned_cases, args.conditioned_field
    )
    universe = tuple(args.pillars) if args.pillars else None

    res = compute_rae(
        se, sd, gt_by_case, conditioned,
        vote=args.vote, universe_prefixes=universe,
        min_cond=args.min_cond, bootstrap=args.bootstrap, seed=args.seed,
    )
    res["label"] = args.label
    res["conditioning_source"] = conditioning
    res["se_file"] = str(args.se)
    res["sd_file"] = str(args.sd)
    res["scope"] = args.scope

    _print_report(args.label, res, conditioning)
    if conditioning == "all_cases_fallback":
        print("\n  NOTE: no retrieval-fired signal supplied; RAE conditioned on ALL SE "
              "cases. Provide --conditioned-cases or --conditioned-field for a true "
              "retrieval-invoked RAE.")

    if args.output:
        args.output.write_text(json.dumps(res, indent=2))
        print(f"\nSaved: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
