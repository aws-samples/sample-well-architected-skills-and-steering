#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Generate ground-truth applicable-BP sets for wa-review eval cases.

Uses the subagent-per-pillar pattern (call_model_subagent from benchmark.py)
against 2 top-tier models × 5 runs × 6 eval cases = 60 total runs.

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

import boto3
from botocore.config import Config as BotoConfig

SCRIPT_DIR = Path(__file__).resolve().parent
EVALS_DIR = SCRIPT_DIR.parent
REPO_ROOT = EVALS_DIR.parent
GT_DIR = SCRIPT_DIR / "ground_truth"

sys.path.insert(0, str(EVALS_DIR))
from benchmark import call_model_subagent  # noqa: E402

MODELS = [
    "us.anthropic.claude-sonnet-5",
    "openai.gpt-oss-120b",
    # Fable 5 dropped: both bedrock-runtime and bedrock-mantle throttle it heavily
    # under this concurrency pattern. Sonnet 5 + GPT OSS 120B are both 5.0/5 quality
    # in our benchmarks; their intersection is a strong ground-truth signal.
]

RUNS_PER_MODEL = 5
# Accept ASCII hyphen (-, U+002D), non-breaking hyphen (‑, U+2011),
# hyphen-minus (‐, U+2010), and em-dash lookalike (—) — models produce all these.
BP_PATTERN = re.compile(r"\b([A-Z]{2,}\d{1,3})[-‐‑–]BP(\d{1,3})\b")


def _normalize_bp(match: re.Match) -> str:
    """Return a canonical BP ID (ASCII hyphen) from a regex match."""
    return f"{match.group(1)}-BP{match.group(2)}"


def _extract_bps(text: str) -> set[str]:
    """Extract BP IDs from text, normalizing any Unicode-hyphen variants."""
    return {_normalize_bp(m) for m in BP_PATTERN.finditer(text)}

SYSTEM_PROMPT = """You are an AWS Well-Architected expert performing a comprehensive review.

Analyze the workload described and produce findings grouped by pillar (Operational
Excellence, Security, Reliability, Performance Efficiency, Cost Optimization,
Sustainability). This is a research protocol — coverage matters.

MANDATORY citation format: cite every Best Practice using the canonical WA
identifier `PILLAR##-BP##`, for example:
- `SEC01-BP02`, `REL06-BP04`, `COST05-BP03`, `OPS04-BP01`, `PERF03-BP01`, `SUS02-BP01`

Do NOT use shorthand ("SEC-1", "REL 2") or severity-based numbering ("CRITICAL-01").
Do NOT invent BP IDs. Cite the canonical form only.

Enumerate every BP that applies to the workload — target 30-55 BPs per pillar for
a comprehensive review. Include "Not Implemented" findings for absent controls
and "Not Applicable" for genuinely inapplicable BPs (with brief rationale)."""


def load_eval_cases() -> list[dict]:
    """Load the 6 wa-review eval prompts."""
    evals_file = REPO_ROOT / "skills" / "wa-review" / "evals" / "evals.json"
    data = json.loads(evals_file.read_text())
    return data["evals"]


def build_canonical_bps() -> set[str]:
    """Extract the 307 canonical BPs from the corpus (H1 headings)."""
    refs_dir = REPO_ROOT / "skills" / "wa-review" / "references" / "questions"
    canonical: set[str] = set()
    canonical_re = re.compile(r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\b", re.MULTILINE)
    for f in refs_dir.glob("*.md"):
        for m in canonical_re.finditer(f.read_text()):
            canonical.add(m.group(1))
    return canonical


def run_one(client, model_id: str, prompt: str, canonical: set[str]) -> dict:
    """Run a single subagent-mode call and extract valid BP citations."""
    start = time.time()
    try:
        result = call_model_subagent(client, model_id, prompt,
                                     system=SYSTEM_PROMPT, max_tokens=4096,
                                     temperature=0, region="us-east-1")
    except Exception as e:
        return {"model": model_id, "error": str(e), "latency_s": time.time() - start}

    if "error" in result:
        return {"model": model_id, "error": result["error"],
                "latency_s": result.get("latency_s", 0)}

    output = result.get("output", "")
    cited = _extract_bps(output)
    valid = cited & canonical
    return {
        "model": model_id,
        "cited_count": len(cited),
        "valid_count": len(valid),
        "valid_bps": sorted(valid),
        "output_tokens": result.get("output_tokens", 0),
        "input_tokens": result.get("input_tokens", 0),
        "latency_s": result.get("latency_s", 0),
    }


def compute_ground_truth(runs: list[dict]) -> dict:
    """Consensus rule: BP is 'applicable' if ≥2 of 3 models cited it in ≥3 of 5 runs each.

    Also compute weaker signals for the output:
      - critical_high_bps: reserved for future work (needs severity extraction, not just IDs)
      - all_cited: union across all runs (upper bound of "applicable")
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
    consensus_bps = sorted(bp for bp, votes in bp_model_votes.items() if votes >= successful_models)
    all_cited = sorted(set().union(*(r.get("valid_bps", []) for r in runs
                                      if "error" not in r)))

    return {
        "consensus_bps": consensus_bps,
        "consensus_bp_count": len(consensus_bps),
        "all_cited_bps": all_cited,
        "all_cited_count": len(all_cited),
        "per_model_bp_frequency": {m: dict(f) for m, f in per_model_bp_freq.items()},
    }


def process_case(case: dict, canonical: set[str], client) -> dict:
    """Process one eval case: 3 models × RUNS_PER_MODEL runs, then consensus."""
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
                runs.append(r)
                if "error" in r:
                    print(f"  ✗ {model} run {run_idx}: {r['error'][:80]}")
                else:
                    print(f"  ✓ {model} run {run_idx}: {r['valid_count']}/307 BPs, "
                          f"{r['latency_s']:.0f}s")
            except Exception as e:
                print(f"  ✗ {model} run {run_idx}: EXCEPTION {e}")
                runs.append({"model": model, "run_idx": run_idx, "error": str(e)})

    gt = compute_ground_truth(runs)
    return {
        "case_id": case_id,
        "prompt": prompt,
        "models": MODELS,
        "runs_per_model": RUNS_PER_MODEL,
        "canonical_corpus_size": len(canonical),
        "ground_truth": gt,
        "raw_runs": runs,
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
        print(f"  Consensus (≥2/3 models, ≥3/5 runs each): "
              f"{gt_result['ground_truth']['consensus_bp_count']} BPs")

    return 0


if __name__ == "__main__":
    sys.exit(main())
