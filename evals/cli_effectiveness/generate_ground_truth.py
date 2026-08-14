#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Generate ground-truth applicable-BP sets for aws-well-architected-framework-review eval cases.

Uses the subagent-per-pillar pattern (call_model_subagent from benchmark.py)
against 2 top-tier models × 5 runs × 6 eval cases = 60 total runs. Each model
produces a structured workload-only reference ledger before any candidate
report is revealed.

Ground-truth criteria (both-models consensus):
  - A BP is "applicable" if cited by BOTH models in ≥3 of 5 runs each.

Outputs one JSON file per case at:
  evals/cli_effectiveness/ground_truth/case_{N}.json
"""

from __future__ import annotations

import json
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import boto3
from botocore.config import Config as BotoConfig

SCRIPT_DIR = Path(__file__).resolve().parent
EVALS_DIR = SCRIPT_DIR.parent
REPO_ROOT = EVALS_DIR.parent
GT_DIR = SCRIPT_DIR / "ground_truth"
RAW_ARTIFACTS_DIR = SCRIPT_DIR / "review_artifacts" / "ground_truth"

sys.path.insert(0, str(EVALS_DIR))
from benchmark import call_model_subagent  # noqa: E402
sys.path.insert(0, str(SCRIPT_DIR))
from review_quality import (  # noqa: E402
    normalize_reference_row,
    parse_model_rows,
)

MODELS = [
    "us.anthropic.claude-sonnet-5",
    "openai.gpt-oss-120b",
    # Fable 5 dropped: both bedrock-runtime and bedrock-mantle throttle it heavily
    # under this concurrency pattern. Sonnet 5 + GPT OSS 120B are both 5.0/5 quality
    # in our benchmarks; their intersection is a strong ground-truth signal.
]

RUNS_PER_MODEL = 5

SYSTEM_PROMPT = """You are an AWS Well-Architected expert creating an independent
workload-only reference ledger for evaluation.

Analyze only the workload description and authoritative pillar reference. You
will not receive a candidate report. This is a research protocol: evidence
fidelity and complete coverage matter.

MANDATORY citation format: cite every Best Practice using the canonical WA
identifier `PILLAR##-BP##`, for example:
- `SEC01-BP02`, `REL06-BP04`, `COST05-BP03`, `OPS04-BP01`, `PERF03-BP01`, `SUS02-BP01`

Do NOT use shorthand ("SEC-1", "REL 2") or severity-based numbering ("CRITICAL-01").
Do NOT invent BP IDs. Cite the canonical form only.

Do not treat information omitted from a short workload description as proof that
a control is not implemented. Use Cannot Determine when the evidence is
insufficient."""

STRUCTURED_PILLAR_TASK = """Review the workload ONLY for the {pillar_name} pillar.
Enumerate every canonical BP in the supplied pillar reference, including BPs
that are not applicable or cannot be determined.

Return ONLY one JSON object:
{{"rows":[{{"bp_id":"SEC01-BP01","applicability":"applicable",
"expected_status":"Cannot Determine","expected_severity":null,
"evidence_basis":"The workload description does not provide account governance evidence.",
"confidence":"high"}}]}}

Allowed applicability values: applicable, not_applicable, uncertain.
Allowed status values: Implemented, Partially Implemented, Not Implemented,
Not Applicable, Cannot Determine. Allowed severity values: Critical, High,
Medium, Low, or null. Confidence must be high, medium, or low.
Use null severity for Implemented, Not Applicable, and Cannot Determine. Assign
severity only to an evidenced gap. Keep evidence_basis to one concise sentence.

The rows array must contain exactly one unique row for every BP in this pillar.
Do not include markdown or narrative outside the JSON."""


def load_eval_cases() -> list[dict]:
    """Load the 6 aws-well-architected-framework-review eval prompts."""
    evals_file = REPO_ROOT / "skills" / "aws-well-architected-framework-review" / "evals" / "evals.json"
    data = json.loads(evals_file.read_text())
    return data["evals"]


def build_canonical_bps() -> set[str]:
    """Extract the 307 canonical BPs from the corpus (H1 headings)."""
    refs_dir = REPO_ROOT / "skills" / "aws-well-architected-framework-review" / "references" / "pillars"
    canonical: set[str] = set()
    canonical_re = re.compile(r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\b", re.MULTILINE)
    for f in refs_dir.glob("*.md"):
        for m in canonical_re.finditer(f.read_text()):
            canonical.add(m.group(1))
    return canonical


def run_one(client, model_id: str, prompt: str, canonical: set[str]) -> dict:
    """Run a workload-only panel call and parse its structured BP ledger."""
    start = time.time()
    try:
        result = call_model_subagent(client, model_id, prompt,
                                     system=SYSTEM_PROMPT, max_tokens=16384,
                                     temperature=0, region="us-east-1",
                                     pillar_task=STRUCTURED_PILLAR_TASK,
                                     include_reasoning=False)
    except Exception as e:
        return {"model": model_id, "error": str(e), "latency_s": time.time() - start}

    if "error" in result:
        return {"model": model_id, "error": result["error"],
                "latency_s": result.get("latency_s", 0)}

    output = result.get("output", "")
    assessment = parse_model_rows(output, canonical, normalize_reference_row)
    if not assessment["complete"]:
        return {
            "model": model_id,
            "error": (
                "incomplete structured ledger: "
                f"{len(assessment['missing_ids'])} missing, "
                f"{len(assessment['invalid_rows'])} invalid"
            ),
            "raw_output": output,
            "latency_s": result.get("latency_s", 0),
        }
    rows = assessment["rows"]
    valid = {
        bp_id
        for bp_id, row in rows.items()
        if row["applicability"] == "applicable"
    }
    return {
        "model": model_id,
        "cited_count": len(rows),
        "valid_count": len(valid),
        "valid_bps": sorted(valid),
        "assessments": rows,
        "raw_output": output,
        "output_tokens": result.get("output_tokens", 0),
        "input_tokens": result.get("input_tokens", 0),
        "latency_s": result.get("latency_s", 0),
    }


def _stable_model_value(
    model_runs: list[dict],
    bp_id: str,
    field: str,
) -> tuple[Any | None, int]:
    frequencies: dict[Any, int] = defaultdict(int)
    for run in model_runs:
        row = run.get("assessments", {}).get(bp_id)
        if row is not None:
            frequencies[row.get(field)] += 1
    if not frequencies:
        return None, 0
    value, count = max(frequencies.items(), key=lambda item: (item[1], str(item[0])))
    return (value, count) if count >= 3 else (None, count)


def _reference_ledger(runs: list[dict], canonical: set[str]) -> dict[str, dict]:
    successful = [run for run in runs if "error" not in run]
    by_model = {
        model: [run for run in successful if run["model"] == model]
        for model in sorted({run["model"] for run in successful})
    }
    ledger: dict[str, dict] = {}
    severity_order = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}

    for bp_id in sorted(canonical):
        votes: dict[str, dict[str, Any]] = {}
        evidence_basis: list[str] = []
        for model, model_runs in by_model.items():
            applicability, applicability_count = _stable_model_value(
                model_runs, bp_id, "applicability"
            )
            status, status_count = _stable_model_value(
                model_runs, bp_id, "expected_status"
            )
            severity, severity_count = _stable_model_value(
                model_runs, bp_id, "expected_severity"
            )
            votes[model] = {
                "applicability": applicability,
                "applicability_votes": applicability_count,
                "expected_status": status,
                "status_votes": status_count,
                "expected_severity": severity,
                "severity_votes": severity_count,
            }
            for run in model_runs:
                row = run.get("assessments", {}).get(bp_id)
                if (
                    row
                    and row["applicability"] == applicability
                    and row["expected_status"] == status
                    and row["evidence_basis"] not in evidence_basis
                ):
                    evidence_basis.append(row["evidence_basis"])
                    break

        applicability_values = {
            vote["applicability"] for vote in votes.values()
            if vote["applicability"] is not None
        }
        status_values = {
            vote["expected_status"] for vote in votes.values()
            if vote["expected_status"] is not None
        }
        severity_values = {
            vote["expected_severity"] for vote in votes.values()
            if vote["expected_severity"] is not None
        }
        all_models_stable = len(votes) == len(MODELS)
        applicability_stable = all_models_stable and all(
            vote["applicability"] is not None for vote in votes.values()
        )
        status_stable = all_models_stable and all(
            vote["expected_status"] is not None for vote in votes.values()
        )
        severity_signatures = {
            vote["expected_severity"] for vote in votes.values()
            if vote["severity_votes"] >= 3
        }
        severity_stable = all_models_stable and all(
            vote["severity_votes"] >= 3 for vote in votes.values()
        )
        applicability = (
            next(iter(applicability_values))
            if applicability_stable and len(applicability_values) == 1
            else "disputed"
        )
        expected_status = (
            next(iter(status_values))
            if status_stable and len(status_values) == 1
            else "disputed"
        )
        acceptable_severities = sorted(
            severity_values,
            key=lambda value: severity_order[value],
        )
        severity_span = (
            max(severity_order[value] for value in severity_values)
            - min(severity_order[value] for value in severity_values)
            if severity_values else 0
        )
        if (
            applicability != "disputed"
            and expected_status != "disputed"
            and severity_stable
            and len(severity_signatures) == 1
        ):
            confidence = "high"
        elif (
            applicability != "disputed"
            and expected_status != "disputed"
            and severity_stable
            and severity_span <= 1
        ):
            confidence = "medium"
        else:
            confidence = "low"

        ledger[bp_id] = {
            "applicability": applicability,
            "expected_status": expected_status,
            "acceptable_severities": acceptable_severities,
            "evidence_basis": evidence_basis[:2],
            "confidence": confidence,
            "model_votes": votes,
        }
    return ledger


def compute_ground_truth(runs: list[dict], canonical: set[str]) -> dict:
    """Consensus rule: a BP is applicable when both models vote for it in ≥3/5 runs.

    The structured reference ledger separately records consensus status,
    acceptable severity values, evidence bases, and uncertainty.
    """
    per_model_bp_freq: dict[str, dict[str, int]] = {}
    for r in runs:
        if "error" in r:
            continue
        model = r["model"]
        per_model_bp_freq.setdefault(model, defaultdict(int))
        for bp in r["valid_bps"]:
            per_model_bp_freq[model][bp] += 1

    # For each BP, count how many models cited it in ≥3 of their 5 runs
    bp_model_votes: dict[str, int] = defaultdict(int)
    for model, freqs in per_model_bp_freq.items():
        for bp, count in freqs.items():
            if count >= 3:
                bp_model_votes[bp] += 1

    # Consensus rule: BP must be cited by BOTH models in ≥3/5 of their runs each.
    # bp_model_votes counts how many models cited it 3+ times; require == number of successful models.
    successful_models = len(per_model_bp_freq)
    consensus_bps = sorted(
        bp for bp, votes in bp_model_votes.items()
        if successful_models == len(MODELS) and votes >= successful_models
    )
    all_cited = sorted(set().union(*(r.get("valid_bps", []) for r in runs
                                      if "error" not in r)))
    ledger = _reference_ledger(runs, canonical)
    critical_high = sorted(
        bp_id
        for bp_id, row in ledger.items()
        if set(row["acceptable_severities"]) & {"Critical", "High"}
    )

    return {
        "consensus_bps": consensus_bps,
        "consensus_bp_count": len(consensus_bps),
        "critical_high_bps": critical_high,
        "all_cited_bps": all_cited,
        "all_cited_count": len(all_cited),
        "per_model_bp_frequency": {m: dict(f) for m, f in per_model_bp_freq.items()},
        "reference_ledger": ledger,
    }


def process_case(case: dict, canonical: set[str], client) -> dict:
    """Process one eval case: 2 models × RUNS_PER_MODEL runs, then consensus."""
    case_id = case["id"]
    prompt = case["prompt"]
    print(f"\n=== Case {case_id} ===")
    print(f"  Prompt: {prompt[:80]}...")

    jobs = [(model, run_idx) for model in MODELS for run_idx in range(1, RUNS_PER_MODEL + 1)]
    runs: list[dict] = []

    with ThreadPoolExecutor(max_workers=len(MODELS)) as pool:
        futures = {pool.submit(run_one, client, model, prompt, canonical): (model, run_idx)
                   for model, run_idx in jobs}
        for fut in as_completed(futures):
            model, run_idx = futures[fut]
            try:
                r = fut.result()
                r["run_idx"] = run_idx
                raw_output = r.pop("raw_output", "")
                if raw_output:
                    safe_model = re.sub(r"[^a-zA-Z0-9._-]+", "-", model)
                    artifact = (
                        RAW_ARTIFACTS_DIR
                        / f"case-{case_id}-{safe_model}-run-{run_idx}.txt"
                    )
                    artifact.parent.mkdir(parents=True, exist_ok=True)
                    artifact.write_text(raw_output)
                    r["raw_artifact"] = str(artifact.relative_to(REPO_ROOT))
                runs.append(r)
                if "error" in r:
                    print(f"  ✗ {model} run {run_idx}: {r['error'][:80]}")
                else:
                    print(f"  ✓ {model} run {run_idx}: {r['valid_count']}/307 BPs, "
                          f"{r['latency_s']:.0f}s")
            except Exception as e:
                print(f"  ✗ {model} run {run_idx}: EXCEPTION {e}")
                runs.append({"model": model, "run_idx": run_idx, "error": str(e)})

    gt = compute_ground_truth(runs, canonical)
    stored_runs = []
    for run in runs:
        stored_runs.append({
            key: value
            for key, value in run.items()
            if key not in {"assessment", "assessments", "raw_artifact"}
        })
    return {
        "schema_version": 2,
        "case_id": case_id,
        "prompt": prompt,
        "models": MODELS,
        "runs_per_model": RUNS_PER_MODEL,
        "canonical_corpus_size": len(canonical),
        "ground_truth": gt,
        "panel_runs": stored_runs,
    }


def main() -> int:
    GT_DIR.mkdir(parents=True, exist_ok=True)

    canonical = build_canonical_bps()
    print(f"Canonical corpus: {len(canonical)} BPs")

    cases = load_eval_cases()
    print(f"Eval cases: {len(cases)}")

    client = boto3.client(
        "bedrock-runtime",
        region_name="us-east-1",
        config=BotoConfig(read_timeout=300),
    )

    for case in cases:
        gt_result = process_case(case, canonical, client)
        out_file = GT_DIR / f"case_{gt_result['case_id']}.json"
        out_file.write_text(json.dumps(gt_result, indent=2))
        print(f"  Saved: {out_file.relative_to(REPO_ROOT)}")
        print(f"  Consensus (both models, ≥3/5 runs each): "
              f"{gt_result['ground_truth']['consensus_bp_count']} BPs")

    return 0


if __name__ == "__main__":
    sys.exit(main())
