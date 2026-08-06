#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Measure wa-review effectiveness via real Codex CLI (codex exec).

Parallel to measure_kiro.py but uses `codex exec` instead of `kiro-cli chat`.
Codex writes session JSONL to ~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl
containing token counts, duration, and the full conversation.

Model: openai.gpt-5.4 via amazon-bedrock (configured in ~/.codex/config.toml)
Output: evals/cli_effectiveness/codex_effectiveness.json
"""
from __future__ import annotations

import json
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
EVALS_DIR = SCRIPT_DIR.parent
REPO_ROOT = EVALS_DIR.parent
GT_DIR = SCRIPT_DIR / "ground_truth"

sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(EVALS_DIR))

from measure_wa_review import (  # noqa: E402
    AUTONOMOUS_PREAMBLE,
    _extract_bps,
    aggregate,
    build_canonical_bps,
    load_eval_cases,
    load_ground_truth,
    score_run,
)

CODEX_SESSIONS = Path.home() / ".codex" / "sessions"
CLI_TIMEOUT_SEC = 3600
CODEX_MODEL = "openai.gpt-5.5"  # latest GPT via Amazon Bedrock mantle
RUNS_PER_CASE = 3
RESULTS_FILE = SCRIPT_DIR / "codex_effectiveness.json"
ANSI_ESCAPE = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def _find_codex_session(started_at: float) -> Path | None:
    """Find the most recent Codex session JSONL file created after started_at."""
    candidates = []
    for p in CODEX_SESSIONS.rglob("rollout-*.jsonl"):
        try:
            mtime = p.stat().st_mtime
        except OSError:
            continue
        if mtime >= started_at:
            candidates.append((mtime, p))
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[0], reverse=True)
    return candidates[0][1]


def _parse_codex_session(session_file: Path) -> tuple[str, dict]:
    """Parse a Codex session JSONL. Returns (assembled_text, metadata)."""
    events = []
    for line in session_file.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    all_text = ""
    token_data: dict = {}
    task_meta: dict = {}

    for e in events:
        payload = e.get("payload", {})
        if not isinstance(payload, dict):
            continue

        # Assistant message text
        if payload.get("role") == "assistant":
            for block in payload.get("content", []):
                if isinstance(block, dict) and block.get("type") == "output_text":
                    all_text += block.get("text", "")

        # Token count event
        if payload.get("type") == "token_count":
            info = payload.get("info", {})
            token_data = info.get("total_token_usage", {})

        # Task complete event
        if payload.get("type") == "task_complete":
            task_meta = payload

    return all_text, {
        "input_tokens": token_data.get("input_tokens"),
        "output_tokens": token_data.get("output_tokens"),
        "reasoning_tokens": token_data.get("reasoning_output_tokens"),
        "cached_tokens": token_data.get("cached_input_tokens"),
        "total_tokens": token_data.get("total_tokens"),
        "duration_ms": task_meta.get("duration_ms"),
        "ttft_ms": task_meta.get("time_to_first_token_ms"),
    }


def run_codex(prompt: str) -> dict:
    """Invoke codex exec with the prompt via stdin."""
    start = time.time()
    wrapped = AUTONOMOUS_PREAMBLE + prompt
    try:
        proc = subprocess.run(
            [
                "codex", "exec",
                "-m", CODEX_MODEL,
                "--dangerously-bypass-approvals-and-sandbox",
            ],
            input=wrapped,
            capture_output=True,
            text=True,
            timeout=CLI_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "wall_s": time.time() - start}

    wall_s = time.time() - start
    stdout_clean = ANSI_ESCAPE.sub("", proc.stdout)

    if proc.returncode != 0 and not stdout_clean.strip():
        return {
            "error": f"exit {proc.returncode}",
            "stderr": proc.stderr[-300:],
            "wall_s": wall_s,
        }

    session_file = _find_codex_session(start)
    if not session_file:
        return {"error": "session not found", "wall_s": wall_s,
                "stdout": stdout_clean[-300:]}

    assembled_text, meta = _parse_codex_session(session_file)
    return {
        "assembled_text": assembled_text,
        "all_text": assembled_text,
        "session_file": str(session_file),
        "wall_s": wall_s,
        "exit_code": proc.returncode,
        "stdout_len": len(assembled_text),
        **meta,
    }


def score(cited: set[str], gt: set[str], canonical: set[str]) -> dict:
    valid = cited & canonical
    tp = valid & gt
    r = len(tp) / len(gt) if gt else 0.0
    p = len(tp) / len(valid) if valid else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {
        "cited_count": len(cited),
        "valid_cited_count": len(valid),
        "true_positives": len(tp),
        "false_positives": len(valid - gt),
        "false_negatives": len(gt - valid),
        "recall": round(r, 4),
        "precision": round(p, 4),
        "f1": round(f1, 4),
        "valid_cited_bps": sorted(valid),
    }


def main() -> int:
    canonical = build_canonical_bps()
    cases = load_eval_cases()
    print(f"Canonical: {len(canonical)} BPs | Cases: {len(cases)} | Runs: {RUNS_PER_CASE}")
    print(f"Model: {CODEX_MODEL} | Timeout: {CLI_TIMEOUT_SEC}s")
    print(f"Total invocations: {len(cases) * RUNS_PER_CASE}\n")

    # Load partial results if they exist
    if RESULTS_FILE.exists():
        results = json.loads(RESULTS_FILE.read_text())
        completed = {c["case_id"]
                     for c in results.get("cases", [])
                     if len([r for r in c.get("runs", []) if "error" not in r]) >= RUNS_PER_CASE}
        if completed:
            print(f"Resuming — skipping completed cases: {sorted(completed)}")
    else:
        results = {
            "runtime": "codex-exec",
            "model": CODEX_MODEL,
            "runs_per_case": RUNS_PER_CASE,
            "cases": [],
        }
        completed = set()

    for case in cases:
        case_id = case["id"]
        if case_id in completed:
            print(f"  Skipping Case {case_id} (already complete)")
            continue

        prompt = case["prompt"]
        gt = load_ground_truth(case_id)
        gt_scoring = ({b for b in gt if b.startswith("SEC") or b.startswith("REL")}
                      if case_id == 4 else gt)
        scope = "SEC+REL only" if case_id == 4 else "full 6 pillars"

        print(f"\n=== Case {case_id} (|GT|={len(gt_scoring)}, {scope}) ===")
        print(f"  {prompt[:80]}...")

        case_runs: list[dict] = []
        for run_idx in range(1, RUNS_PER_CASE + 1):
            print(f"  Run {run_idx}/{RUNS_PER_CASE} started...", flush=True)
            r = run_codex(prompt)
            assembled = r.get("assembled_text", "")
            all_text = r.get("all_text", assembled)

            if "error" in r:
                run_data = {"run_idx": run_idx, "error": r["error"],
                            "wall_s": r.get("wall_s")}
                print(f"  Run {run_idx} ✗ {r['error']}")
            else:
                bps_rep = _extract_bps(assembled) & canonical
                bps_sub = _extract_bps(all_text) & canonical
                s_rep = score(bps_rep, gt_scoring, canonical)
                s_sub = score(bps_sub, gt_scoring, canonical)
                tokens = r.get("total_tokens")
                run_data = {
                    "run_idx": run_idx,
                    "gt_count": len(gt_scoring),
                    "gt_scope": scope,
                    "report": s_rep,
                    "subagent_total": s_sub,
                    "wall_s": r.get("wall_s"),
                    "input_tokens": r.get("input_tokens"),
                    "output_tokens": r.get("output_tokens"),
                    "reasoning_tokens": r.get("reasoning_tokens"),
                    "total_tokens": tokens,
                    "duration_ms": r.get("duration_ms"),
                    "ttft_ms": r.get("ttft_ms"),
                    "session_file": r.get("session_file"),
                    "stdout_len": r.get("stdout_len"),
                    "assembled_text": assembled,
                }
                print(f"  Run {run_idx} ✓ "
                      f"F1={s_rep['f1']:.3f} R={s_rep['recall']:.2f} "
                      f"({s_rep['valid_cited_count']} BPs) "
                      f"tokens={tokens} {r.get('wall_s', 0):.0f}s")
            case_runs.append(run_data)

        agg = aggregate(case_runs)
        existing = [c for c in results["cases"] if c["case_id"] != case_id]
        results["cases"] = existing + [{
            "case_id": case_id,
            "prompt": prompt[:200],
            "gt_scope": scope,
            "runs": case_runs,
            "aggregate": agg,
        }]
        results["cases"].sort(key=lambda c: c["case_id"])

        rf1 = agg.get("report_f1", {})
        print(f"  Case {case_id} mean F1: {rf1.get('mean','n/a')}")
        RESULTS_FILE.write_text(json.dumps(results, indent=2))

    print(f"\nSaved: {RESULTS_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
