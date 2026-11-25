#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Generate lens-on (SE) vs lens-off (SD) paired runs for the lens RAE surface.

The lens surface asks: when a workload matches a lens (e.g. Generative AI), does
LOADING that lens change the review's correctness on the core best practices in
the pillars the lens spans -- does the extra lens context rescue more applicable
BPs than it distracts away? This is the conditional-retrieval question from
Cho & Park 2026 (arXiv:2609.00549), applied to lens packs instead of a search
tool.

DESIGN
------
For each selected eval case we run the aws-well-architected-framework-review
skill TWICE, identical except for one instruction:

  SE (lens on):  "...additionally apply the <lens> lens."
  SD (lens off): "...do NOT apply any lens; evaluate the 6 core pillars only."

Both are scored against the SAME core ground truth (consensus_bps) using the
shared measure_wa_review scoring, so the outputs drop straight into rae.py.

Because the lens BPs themselves are NOT in the core ground truth, RAE here is
scored on the CORE GT BPs, optionally restricted to the pillars the lens spans
(printed as the --pillars filter to pass to rae.py). This measures the lens's
*side effect* on core coverage -- the honest, GT-backed question -- rather than
lens-BP recall, which would need a separate lens ground truth.

USAGE
-----
    python measure_lens_rae.py --lens generative-ai --cases 5 --runs 3
    # then, using the printed pillar filter:
    python rae.py --se lens_generative-ai_se.json --sd lens_generative-ai_sd.json \\
        --pillars <printed> --conditioned-cases 5 --label "GenAI lens on/off"

The lens directory name must match a folder under
skills/aws-well-architected-framework-review/references/lenses/.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from measure_wa_review import (  # noqa: E402
    AUTONOMOUS_PREAMBLE,
    CLI_TIMEOUT_SEC,
    MODEL,
    aggregate,
    build_canonical_bps,
    load_eval_cases,
    load_ground_truth,
    run_claude_cli,
    score_run,
)

REPO_ROOT = SCRIPT_DIR.parent.parent
LENSES_DIR = REPO_ROOT / "skills" / "aws-well-architected-framework-review" / "references" / "lenses"

RUNS_PER_CASE = 3

PILLAR_NAME_TO_PREFIX = {
    "operational excellence": "OPS",
    "security": "SEC",
    "reliability": "REL",
    "performance efficiency": "PERF",
    "cost optimization": "COST",
    "sustainability": "SUS",
}

_PILLAR_HEADER = re.compile(r"\*\*Pillar\*\*:\s*(.+)", re.IGNORECASE)


def lens_dir(name: str) -> Path:
    d = LENSES_DIR / name
    if not d.is_dir():
        available = sorted(p.name for p in LENSES_DIR.iterdir() if p.is_dir())
        raise SystemExit(f"unknown lens '{name}'. Available: {', '.join(available)}")
    return d


def lens_covered_pillars(name: str) -> list[str]:
    """Core pillar prefixes a lens spans, from each file's `**Pillar**:` header.

    Lenses that AWS does not organize by the 6 pillars (e.g. responsible-ai)
    omit the header; those return [] (RAE then scores against all core GT BPs).
    """
    prefixes: set[str] = set()
    for f in lens_dir(name).glob("*.md"):
        for m in _PILLAR_HEADER.finditer(f.read_text(errors="ignore")):
            key = m.group(1).strip().lower()
            if key in PILLAR_NAME_TO_PREFIX:
                prefixes.add(PILLAR_NAME_TO_PREFIX[key])
    return sorted(prefixes)


def lens_bp_universe(name: str) -> list[str]:
    """The lens's own BP IDs (H1 headings), for reporting only."""
    ids: set[str] = set()
    heading = re.compile(r"^#\s+([A-Z][A-Z0-9]*\d{1,3}(?:-BP\d{1,3})?)\b", re.MULTILINE)
    for f in lens_dir(name).glob("*.md"):
        for m in heading.finditer(f.read_text(errors="ignore")):
            ids.add(m.group(1))
    return sorted(ids)


SE_INSTRUCTION = (
    "\n\nADDITIONALLY apply the {lens} lens: load the lens reference pack and "
    "evaluate its lens-specific best practices alongside the 6 core pillars.\n"
)
SD_INSTRUCTION = (
    "\n\nDo NOT apply any lens. Evaluate ONLY the 6 core Well-Architected pillars. "
    "Ignore domain-specific lens packs entirely.\n"
)


def _preamble(lens: str, lens_on: bool) -> str:
    instr = SE_INSTRUCTION.format(lens=lens) if lens_on else SD_INSTRUCTION
    # Insert the lens instruction just before the workload block.
    marker = "===== WORKLOAD ====="
    return AUTONOMOUS_PREAMBLE.replace(marker, instr + marker)


def run_arm(cases, lens, lens_on, runs, model, timeout, canonical, output_path):
    arm = "se_lens_on" if lens_on else "sd_lens_off"
    results = {
        "mode": "lens_rae",
        "lens": lens,
        "arm": arm,
        "covered_pillars": lens_covered_pillars(lens),
        "lens_bp_universe": lens_bp_universe(lens),
        "model": model,
        "runs_per_case": runs,
        "cases": [],
    }
    preamble = _preamble(lens, lens_on)
    for case in cases:
        cid = case["id"]
        gt = load_ground_truth(cid)
        gt_scoring = ({b for b in gt if b.startswith(("SEC", "REL"))} if cid == 4 else gt)
        print(f"  [{arm}] case {cid} (|GT|={len(gt_scoring)})")
        case_runs = []
        wrapped = preamble + case["prompt"]
        for run_idx in range(1, runs + 1):
            print(f"    run {run_idx}/{runs}...", end="", flush=True)
            cli = run_claude_cli(wrapped, model, allow_task=True, timeout=timeout)
            scored = score_run(cli, gt_scoring, canonical)
            scored["run_idx"] = run_idx
            case_runs.append(scored)
            if "error" in scored:
                print(f" x {scored['error']}")
            else:
                print(f" ok sub F1={scored['subagent_total']['f1']:.3f}")
        results["cases"].append({
            "case_id": cid, "prompt": case["prompt"][:200],
            "runs": case_runs, "aggregate": aggregate(case_runs),
        })
        output_path.write_text(json.dumps(results, indent=2))
    return results


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate lens-on/off paired runs for RAE.")
    p.add_argument("--lens", required=True, help="Lens folder name under references/lenses/.")
    p.add_argument("--cases", type=int, nargs="+", required=True,
                   help="Eval case IDs the lens applies to (e.g. 5 for GenAI).")
    p.add_argument("--runs", type=int, default=RUNS_PER_CASE)
    p.add_argument("--model", default=MODEL)
    p.add_argument("--timeout", type=int, default=CLI_TIMEOUT_SEC)
    p.add_argument("--arm", choices=["se", "sd", "both"], default="both",
                   help="Which arm(s) to run (default: both).")
    p.add_argument("--output-se", type=Path, default=None)
    p.add_argument("--output-sd", type=Path, default=None)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    lens = args.lens
    out_se = args.output_se or SCRIPT_DIR / f"lens_{lens}_se.json"
    out_sd = args.output_sd or SCRIPT_DIR / f"lens_{lens}_sd.json"

    canonical = build_canonical_bps()
    all_cases = {int(c["id"]): c for c in load_eval_cases()}
    unknown = set(args.cases) - set(all_cases)
    if unknown:
        raise SystemExit(f"unknown case IDs: {sorted(unknown)}")
    cases = [all_cases[c] for c in args.cases]

    pillars = lens_covered_pillars(lens)
    print(f"Lens: {lens} | covered pillars: {pillars or 'none (scores all core GT)'}")
    print(f"Lens BP universe: {len(lens_bp_universe(lens))} lens BPs (informational)")
    print(f"Cases: {args.cases} | runs: {args.runs} | model: {args.model}\n")

    if args.arm in ("se", "both"):
        run_arm(cases, lens, True, args.runs, args.model, args.timeout, canonical, out_se)
        print(f"Saved SE: {out_se}")
    if args.arm in ("sd", "both"):
        run_arm(cases, lens, False, args.runs, args.model, args.timeout, canonical, out_sd)
        print(f"Saved SD: {out_sd}")

    pillar_flag = f"--pillars {' '.join(pillars)}" if pillars else ""
    cases_flag = " ".join(str(c) for c in args.cases)
    print("\nNext, compute lens RAE:")
    print(f"  python rae.py --se {out_se.name} --sd {out_sd.name} "
          f"{pillar_flag} --conditioned-cases {cases_flag} "
          f"--label '{lens} lens on/off'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
