#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Baseline: run each eval case in Claude Code CLI WITHOUT wa-review skill.

For each case × run:
  - Invoke `claude -p --safe-mode --disable-slash-commands ...` from a scratch
    working directory. --safe-mode disables all skills, CLAUDE.md, plugins,
    hooks, MCP. --disable-slash-commands is belt-and-suspenders.
  - Score output against the same ground truth
  - Save to evals/cli_effectiveness/wa_review_baseline.json
    (parallel to wa_review_effectiveness.json)

Enables paired comparison: "with skill" (0.96) vs "without skill" (?).
"""
from __future__ import annotations

import json
import statistics
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from measure_wa_review import (  # noqa: E402
    CLI_TIMEOUT_SEC,
    MODEL,
    _find_session_file,
    _parse_session,
    _score_text,
    aggregate,
    build_canonical_bps,
    load_eval_cases,
    load_ground_truth,
)

# For the baseline we do NOT wrap with the AUTONOMOUS_PREAMBLE — that preamble
# specifically instructs the agent to use the wa-review skill. In the baseline
# the agent has no skill loaded, so we just pass the raw case prompt with a
# minimal cover note asking for a WA review.
BASELINE_COVER = """[NON-INTERACTIVE EVAL MODE — no follow-up questions possible]

Perform a comprehensive AWS Well-Architected Framework review of the workload
described below. Cover all applicable pillars (Operational Excellence, Security,
Reliability, Performance Efficiency, Cost Optimization, Sustainability). Cite
specific Best Practice IDs where relevant in the canonical WA identifier format
`PILLAR##-BP##` (e.g., SEC03-BP02, REL06-BP04). Do not ask for clarification —
proceed with the review based on what is provided.

===== WORKLOAD =====
"""

RUNS_PER_CASE = 3
BASELINE_RESULTS = SCRIPT_DIR / "wa_review_baseline.json"


def run_baseline_cli(prompt: str, workdir: Path) -> dict:
    """Invoke claude -p in --safe-mode from a scratch workdir.

    --safe-mode disables all skills, CLAUDE.md discovery, plugins, hooks, MCP
    servers. --disable-slash-commands adds explicit skill-blocking. This
    guarantees the wa-review skill is not loaded and no auto-trigger fires.
    """
    start = time.time()
    try:
        proc = subprocess.run(
            [
                "claude",
                "-p",
                "--output-format", "json",
                "--model", MODEL,
                "--safe-mode",
                "--disable-slash-commands",
                "--allowedTools", "Task", "Read", "Grep", "Glob", "Bash",
                "--dangerously-skip-permissions",
            ],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=CLI_TIMEOUT_SEC,
            cwd=str(workdir),
        )
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "wall_s": time.time() - start}

    wall_s = time.time() - start
    if proc.returncode != 0:
        return {
            "error": f"exit {proc.returncode}",
            "stderr": proc.stderr[-500:],
            "wall_s": wall_s,
        }

    try:
        final_event = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return {
            "error": f"json parse: {e}",
            "stdout_head": proc.stdout[:500],
            "wall_s": wall_s,
        }

    session_file = _find_session_file(start)
    if session_file is None:
        return {"error": "session file not found", "final": final_event, "wall_s": wall_s}

    assembled_text, all_text = _parse_session(session_file)
    return {
        "final": final_event or {},
        "assembled_text": assembled_text,
        "all_text": all_text,
        "session_file": str(session_file),
        "wall_s": wall_s,
    }


def score_baseline_run(cli_result: dict, gt_bps: set[str], canonical: set[str]) -> dict:
    if "error" in cli_result:
        return {"error": cli_result.get("error"), "wall_s": cli_result.get("wall_s")}

    final = cli_result.get("final", {}) or {}
    assembled_text = cli_result.get("assembled_text", "")
    all_text = cli_result.get("all_text", "")

    report_scores = _score_text(assembled_text, gt_bps, canonical)
    subagent_scores = _score_text(all_text, gt_bps, canonical)
    usage = final.get("usage", {}) or {}

    return {
        "gt_count": len(gt_bps),
        "report": report_scores,
        "subagent_total": subagent_scores,
        "total_cost_usd": final.get("total_cost_usd"),
        "duration_ms": final.get("duration_ms"),
        "duration_api_ms": final.get("duration_api_ms"),
        "ttft_ms": final.get("ttft_ms"),
        "wall_s": cli_result.get("wall_s"),
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
        "num_turns": final.get("num_turns"),
        "permission_denials": final.get("permission_denials", []),
        "stop_reason": final.get("stop_reason"),
        "assembled_text_len": len(assembled_text),
        "all_text_len": len(all_text),
    }


def main() -> int:
    # Create scratch workdir with no .claude/ subdir so nothing auto-loads
    scratch = Path("/tmp/wa-review-baseline-scratch")
    scratch.mkdir(exist_ok=True)
    # Ensure no .claude subdir exists here (defensive)
    if (scratch / ".claude").exists():
        print(f"WARN: {scratch}/.claude exists — remove for clean baseline")
    print(f"Scratch workdir: {scratch}")

    canonical = build_canonical_bps()
    cases = load_eval_cases()
    print(f"Canonical corpus: {len(canonical)} BPs")
    print(f"Eval cases: {len(cases)}")
    print(f"Model: {MODEL}, runs per case: {RUNS_PER_CASE}")
    print(f"Total CLI invocations: {len(cases) * RUNS_PER_CASE}")

    results = {
        "model": MODEL,
        "runs_per_case": RUNS_PER_CASE,
        "mode": "baseline (no wa-review skill, --safe-mode)",
        "cases": [],
    }

    for case in cases:
        case_id = case["id"]
        prompt = case["prompt"]
        gt = load_ground_truth(case_id)
        wrapped = BASELINE_COVER + prompt

        # Case 4 is pillar-scoped; restrict GT to SEC + REL for fair scoring
        gt_for_scoring = gt
        if case_id == 4:
            gt_for_scoring = {b for b in gt if b.startswith("SEC") or b.startswith("REL")}
            print(f"\n=== Case {case_id} (|GT|={len(gt_for_scoring)}, scoped SEC+REL) ===")
        else:
            print(f"\n=== Case {case_id} (|GT|={len(gt_for_scoring)}) ===")

        case_runs: list[dict] = []
        for run_idx in range(1, RUNS_PER_CASE + 1):
            print(f"  Run {run_idx}/{RUNS_PER_CASE}...", end="", flush=True)
            cli_result = run_baseline_cli(wrapped, scratch)
            scored = score_baseline_run(cli_result, gt_for_scoring, canonical)
            scored["run_idx"] = run_idx
            case_runs.append(scored)
            if "error" in scored:
                print(f" ✗ {scored['error']}")
            else:
                rep = scored["report"]
                sub = scored["subagent_total"]
                print(f" ✓ report F1={rep['f1']:.3f} (R={rep['recall']:.2f} P={rep['precision']:.2f}) "
                      f"| subagent F1={sub['f1']:.3f} | "
                      f"${scored['total_cost_usd']:.3f}, {scored['duration_ms']/1000:.0f}s")

        agg = aggregate(case_runs)
        results["cases"].append({
            "case_id": case_id,
            "prompt": prompt[:200],
            "runs": case_runs,
            "aggregate": agg,
            "gt_scope": "SEC+REL only" if case_id == 4 else "full 6 pillars",
        })
        rf1 = agg.get("report_f1", {})
        print(f"  Case {case_id} mean report F1: "
              f"{rf1.get('mean') if rf1 else 'n/a'}")

        BASELINE_RESULTS.write_text(json.dumps(results, indent=2))

    print(f"\nSaved: {BASELINE_RESULTS.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
