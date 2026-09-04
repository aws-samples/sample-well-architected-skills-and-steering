#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Measure aws-knowledge-mcp-server recall in two CC CLI configurations.

Configuration A (MCP-only baseline):
  claude -p --safe-mode --disable-slash-commands
  + aws-knowledge MCP loaded via --mcp-config
  No skill, no systematic coverage instructions.
  Expected: 2-22% recall (replicates Dec 2025 study conditions in CC CLI).

Configuration B (MCP + aws-well-architected-framework-review skill):
  claude -p (normal mode, aws-well-architected-framework-review skill installed)
  + aws-knowledge MCP loaded via --mcp-config
  The aws-well-architected-framework-review skill instructs systematic per-pillar dispatch.
  Expected: does the skill's coverage strategy lift recall past the plateau?

Scores both against the same ground truth used in measure_wa_review.py.
Output: evals/cli_effectiveness/aws_knowledge_mcp_effectiveness.json
"""
from __future__ import annotations

import json
import statistics
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from measure_wa_review import (  # noqa: E402
    AUTONOMOUS_PREAMBLE,
    CLI_TIMEOUT_SEC,
    MODEL,
    _find_session_file,
    _parse_session,
    _score_text,
    aggregate,
    build_canonical_bps,
    load_eval_cases,
    load_ground_truth,
    score_run,
)
import subprocess

SCRIPT_DIR = Path(__file__).resolve().parent
RESULTS_FILE = SCRIPT_DIR / "aws_knowledge_mcp_effectiveness.json"

RUNS_PER_CASE = 3


def _count_mcp_calls(session_file: str | None) -> int:
    """Count MCP tool_use events across the main + subagent transcripts.

    Claude Code names MCP tools `mcp__<server>__<tool>` (here the server is
    `aws-knowledge`). We count every such tool_use block so RAE can condition
    on cases where retrieval actually fired (rae.py --conditioned-field
    mcp_tool_calls), rather than falling back to all cases.
    """
    if not session_file:
        return 0
    main = Path(session_file)
    if not main.exists():
        return 0
    files = [main]
    sub_dir = main.parent / main.stem / "subagents"
    if sub_dir.exists():
        files.extend(sorted(sub_dir.glob("*.jsonl")))

    count = 0
    for f in files:
        try:
            lines = f.read_text().splitlines()
        except OSError:
            continue
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                ev = json.loads(line)
            except json.JSONDecodeError:
                continue
            if ev.get("type") != "assistant":
                continue
            for block in ev.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    name = block.get("name", "")
                    if name.startswith("mcp__") or "aws-knowledge" in name:
                        count += 1
    return count

# Remote MCP server — no local install needed
MCP_CONFIG = json.dumps({
    "mcpServers": {
        "aws-knowledge": {
            "url": "https://knowledge-mcp.global.api.aws"
        }
    }
})

# Preamble for MCP-only (no skill): ask for systematic WA review using the MCP
MCP_ONLY_PREAMBLE = """[NON-INTERACTIVE EVAL MODE — no follow-up questions possible]

Perform a comprehensive AWS Well-Architected Framework review of the workload below.
Use the aws-knowledge MCP tools to look up AWS Well-Architected best practices.
Cover ALL 6 pillars: Operational Excellence, Security, Reliability, Performance Efficiency,
Cost Optimization, Sustainability.

For each pillar, search for and list relevant best practices. Cite specific Best Practice
IDs in canonical format: PILLAR##-BP## (e.g. SEC03-BP02, REL06-BP04, COST05-BP03).
Be exhaustive — search multiple times per pillar to find all applicable BPs.
Do NOT ask clarifying questions. Proceed directly.

===== WORKLOAD =====
"""


def run_mcp_only(prompt: str) -> dict:
    """claude -p --safe-mode + aws-knowledge MCP, no skill."""
    start = time.time()
    wrapped = MCP_ONLY_PREAMBLE + prompt
    try:
        proc = subprocess.run(
            [
                "claude", "-p",
                "--output-format", "json",
                "--model", MODEL,
                "--safe-mode",
                "--disable-slash-commands",
                "--mcp-config", MCP_CONFIG,
                "--dangerously-skip-permissions",
            ],
            input=wrapped,
            capture_output=True,
            text=True,
            timeout=CLI_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "wall_s": time.time() - start}

    wall_s = time.time() - start
    if proc.returncode != 0:
        return {"error": f"exit {proc.returncode}", "stderr": proc.stderr[-300:], "wall_s": wall_s}

    try:
        final_event = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return {"error": f"json: {e}", "wall_s": wall_s}

    session_file = _find_session_file(start)
    if not session_file:
        return {"error": "session not found", "final": final_event, "wall_s": wall_s}

    assembled, all_text = _parse_session(session_file)
    return {
        "final": final_event,
        "assembled_text": assembled,
        "all_text": all_text,
        "session_file": str(session_file),
        "wall_s": wall_s,
    }


def run_mcp_with_skill(prompt: str) -> dict:
    """claude -p (aws-well-architected-framework-review skill loaded) + aws-knowledge MCP."""
    start = time.time()
    wrapped = AUTONOMOUS_PREAMBLE + prompt
    try:
        proc = subprocess.run(
            [
                "claude", "-p",
                "--output-format", "json",
                "--model", MODEL,
                "--mcp-config", MCP_CONFIG,
                "--dangerously-skip-permissions",
            ],
            input=wrapped,
            capture_output=True,
            text=True,
            timeout=CLI_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "wall_s": time.time() - start}

    wall_s = time.time() - start
    if proc.returncode != 0:
        return {"error": f"exit {proc.returncode}", "stderr": proc.stderr[-300:], "wall_s": wall_s}

    try:
        final_event = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        return {"error": f"json: {e}", "wall_s": wall_s}

    session_file = _find_session_file(start)
    if not session_file:
        return {"error": "session not found", "final": final_event, "wall_s": wall_s}

    assembled, all_text = _parse_session(session_file)
    return {
        "final": final_event,
        "assembled_text": assembled,
        "all_text": all_text,
        "session_file": str(session_file),
        "wall_s": wall_s,
    }


def build_parser() -> "argparse.ArgumentParser":
    import argparse
    p = argparse.ArgumentParser(
        description="Measure aws-knowledge MCP recall (SE arm for RAE) via Claude Code CLI.",
    )
    p.add_argument("--cases", type=int, nargs="+", default=None,
                   help="Evaluate only these case IDs (default: all).")
    p.add_argument("--runs", type=int, default=RUNS_PER_CASE,
                   help=f"Runs per case (default: {RUNS_PER_CASE}).")
    p.add_argument("--model", default=MODEL, help=f"Model (default: {MODEL}).")
    p.add_argument("--output", type=Path, default=RESULTS_FILE, help="Result JSON path.")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.runs < 1:
        raise SystemExit("--runs must be >= 1")

    canonical = build_canonical_bps()
    cases = load_eval_cases()
    available = {int(c["id"]) for c in cases}
    if args.cases:
        unknown = set(args.cases) - available
        if unknown:
            raise SystemExit(f"unknown case IDs: {sorted(unknown)}")
        cases = [c for c in cases if int(c["id"]) in set(args.cases)]

    runs = args.runs
    output_path = args.output.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Canonical: {len(canonical)} BPs | Cases: {[c['id'] for c in cases]} | Runs: {runs}")
    print(f"MCP server: https://knowledge-mcp.global.api.aws")
    print(f"Total CLI invocations: {len(cases) * runs}\n")

    results = {
        "mcp_server": "https://knowledge-mcp.global.api.aws",
        "model": args.model,
        "runs_per_case": runs,
        "configuration": "mcp_only_systematic",
        "cases": [],
    }

    for case in cases:
        case_id = case["id"]
        prompt = case["prompt"]
        gt = load_ground_truth(case_id)
        gt_scoring = ({b for b in gt if b.startswith("SEC") or b.startswith("REL")}
                      if case_id == 4 else gt)
        scope = "SEC+REL only" if case_id == 4 else "full 6 pillars"
        print(f"=== Case {case_id} (|GT|={len(gt_scoring)}, {scope}) ===")
        print(f"  {prompt[:80]}...")

        case_runs: list[dict] = []
        for run_idx in range(1, runs + 1):
            print(f"  Run {run_idx}/{runs}...", end="", flush=True)
            r = run_mcp_only(prompt)
            s = score_run(r, gt_scoring, canonical)
            s["run_idx"] = run_idx
            # Record MCP retrieval activity so RAE can condition on cases where
            # retrieval actually fired (rae.py --conditioned-field mcp_tool_calls).
            s["mcp_tool_calls"] = _count_mcp_calls(r.get("session_file"))
            case_runs.append(s)
            if "error" in s:
                print(f" ✗ {s['error']}")
            else:
                rep = s["report"]
                sub = s["subagent_total"]
                print(f" ✓ report F1={rep['f1']:.3f} R={rep['recall']:.2f} ({rep['valid_cited_count']} BPs) "
                      f"| sub F1={sub['f1']:.3f} "
                      f"${s.get('total_cost_usd', 0):.2f} {s.get('duration_ms', 0)/1000:.0f}s")

        agg = aggregate(case_runs)
        results["cases"].append({
            "case_id": case_id,
            "prompt": prompt[:200],
            "gt_scope": scope,
            "runs": case_runs,
            "aggregate": agg,
        })
        rf1 = agg.get("report_f1", {}).get("mean", "n/a")
        print(f"  Case {case_id} mean report F1: {rf1}")

        output_path.write_text(json.dumps(results, indent=2))

    print(f"\nSaved: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
