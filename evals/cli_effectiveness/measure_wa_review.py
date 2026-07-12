#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Measure wa-review effectiveness via real Claude Code CLI runs.

For each eval case, invokes `claude -p --output-format json` with the
wa-review skill available (mounted at ~/.claude/skills). The skill's SKILL.md
instructs Claude Code to dispatch 6 parallel Task subagents (one per pillar).

For each (case, run) we capture:
  - effectiveness: recall / precision / F1 vs ground_truth/case_N.json
  - cost: total_cost_usd
  - latency: duration_ms, duration_api_ms, ttft_ms
  - tokens: input, output, cache_creation, cache_read
  - orchestration: num_turns, permission_denials
  - raw text (for post-hoc inspection)

Output: evals/cli_effectiveness/wa_review_effectiveness.json
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

MODEL = "sonnet"
RUNS_PER_CASE = 3
CLI_TIMEOUT_SEC = 900  # subagent dispatch is 6-way parallel; each pillar ~30-90s

# Autonomous-mode preamble: the skill has a discovery checkpoint that requires user
# confirmation. In non-interactive eval mode we authorize the full review upfront and
# require canonical BP citations so downstream regex extraction works.
AUTONOMOUS_PREAMBLE = """[NON-INTERACTIVE EVAL MODE — no follow-up questions possible]

Use the wa-review skill. Skip the discovery checkpoint. Proceed directly to the
full review based ONLY on the workload description below — do NOT ask for code,
scope confirmation, or clarification. If information is missing, mark those
findings as "Based on description — verify in code" and continue.

Dispatch the 6 parallel pillar subagents as instructed by SKILL.md Step 4b.
Every Best Practice you cite MUST use the canonical WA identifier format
`PILLAR##-BP##` (e.g., SEC01-BP02, REL06-BP04, COST05-BP03). Do NOT use
shorthand, severity numbering, or invent IDs. Target the full 307-BP corpus.

Produce the full report as specified in SKILL.md.

===== WORKLOAD =====
"""

# Accept ASCII hyphen, non-breaking hyphen, hyphen-minus, em-dash
BP_PATTERN = re.compile(r"\b([A-Z]{2,}\d{1,3})[-‐‑–]BP(\d{1,3})\b")


def _extract_bps(text: str) -> set[str]:
    return {f"{m.group(1)}-BP{m.group(2)}" for m in BP_PATTERN.finditer(text)}


def build_canonical_bps() -> set[str]:
    """Extract the 307 canonical BPs from the corpus (H1 headings in pillar files)."""
    refs_dir = REPO_ROOT / "skills" / "wa-review" / "references" / "pillars"
    canonical: set[str] = set()
    canonical_re = re.compile(r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\b", re.MULTILINE)
    for f in refs_dir.glob("*.md"):
        for m in canonical_re.finditer(f.read_text()):
            canonical.add(m.group(1))
    return canonical


def load_eval_cases() -> list[dict]:
    evals_file = REPO_ROOT / "skills" / "wa-review" / "evals" / "evals.json"
    data = json.loads(evals_file.read_text())
    return data["evals"]


def load_ground_truth(case_id: int) -> set[str]:
    gt_file = GT_DIR / f"case_{case_id}.json"
    data = json.loads(gt_file.read_text())
    return set(data["ground_truth"]["consensus_bps"])


SESSIONS_DIR = Path.home() / ".claude" / "projects"


def _find_session_file(started_at: float) -> Path | None:
    """Find the CC session .jsonl file created after `started_at` (unix ts).

    Claude Code writes session logs to ~/.claude/projects/{slug}/{uuid}.jsonl
    when `claude -p` is invoked. We match by mtime > started_at and pick the
    most-recently-modified one.
    """
    candidates: list[tuple[float, Path]] = []
    for p in SESSIONS_DIR.rglob("*.jsonl"):
        try:
            mtime = p.stat().st_mtime
        except OSError:
            continue
        # Skip subagent files — they live under {parent}/subagents/agent-*.jsonl
        if "/subagents/" in str(p):
            continue
        if mtime >= started_at:
            candidates.append((mtime, p))
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[0], reverse=True)
    return candidates[0][1]


def _parse_session(session_file: Path) -> tuple[str, str]:
    """Parse a CC session .jsonl and return (assembled_text, all_text).

    assembled_text = the final main-thread assistant.text block(s) (what the user sees).
    all_text = every text block from main-thread + subagent files (full analysis).
    """
    def load_jsonl(p: Path) -> list[dict]:
        events: list[dict] = []
        for line in p.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
        return events

    main_events = load_jsonl(session_file)
    # Subagent transcripts live under {session_file_stem}/subagents/*.jsonl
    subagent_dir = session_file.parent / session_file.stem / "subagents"
    subagent_events: list[dict] = []
    if subagent_dir.exists():
        for p in sorted(subagent_dir.glob("*.jsonl")):
            subagent_events.extend(load_jsonl(p))

    all_text_chunks: list[str] = []
    last_assistant_text: list[str] = []

    def collect(events: list[dict], is_main: bool) -> None:
        nonlocal last_assistant_text
        for ev in events:
            if ev.get("type") != "assistant":
                continue
            content = ev.get("message", {}).get("content", [])
            for block in content:
                if block.get("type") == "text":
                    txt = block.get("text", "")
                    all_text_chunks.append(txt)
                    if is_main:
                        last_assistant_text.append(txt)
                elif block.get("type") == "tool_use" and is_main:
                    # Reset last_assistant_text — a new tool call means the previous
                    # text was intermediate. We only want the final terminal text.
                    last_assistant_text = []

    collect(main_events, is_main=True)
    collect(subagent_events, is_main=False)

    return "\n".join(last_assistant_text), "\n".join(all_text_chunks)


def run_claude_cli(prompt: str) -> dict:
    """Invoke `claude -p --output-format json` (small stdout for cost/latency
    metrics), then parse the CC session .jsonl file for the full transcript.

    We used to pipe --output-format=stream-json on stdout, but that broke on
    130KB+ assistant messages (pipe buffering / line-split issues silently
    dropped events). The session log is a reliable source of truth: Claude
    Code writes every event there, no truncation.

    Returns a dict with:
      - final: the terminal `type=result` event from --output-format json
               (has cost/tokens/duration)
      - assembled_text: final main-thread assistant text (what the user sees)
      - all_text: every text block from main + subagent transcripts
      - session_file: path to the parsed .jsonl (for debugging)
      - wall_s
    """
    start = time.time()
    try:
        proc = subprocess.run(
            [
                "claude",
                "-p",
                "--output-format", "json",
                "--model", MODEL,
                "--allowedTools", "Task", "Read", "Grep", "Glob", "Bash",
                "--dangerously-skip-permissions",
            ],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=CLI_TIMEOUT_SEC,
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
        return {
            "error": "session file not found",
            "final": final_event,
            "wall_s": wall_s,
        }

    assembled_text, all_text = _parse_session(session_file)

    return {
        "final": final_event or {},
        "assembled_text": assembled_text,
        "all_text": all_text,
        "session_file": str(session_file),
        "wall_s": wall_s,
    }


def _score_text(text: str, gt_bps: set[str], canonical: set[str]) -> dict:
    """Compute recall/precision/F1 for BP citations in a text blob."""
    cited = _extract_bps(text)
    valid = cited & canonical
    tp = valid & gt_bps
    recall = len(tp) / len(gt_bps) if gt_bps else 0.0
    precision = len(tp) / len(valid) if valid else 0.0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0.0
    return {
        "cited_count": len(cited),
        "valid_cited_count": len(valid),
        "true_positives": len(tp),
        "false_positives": len(valid - gt_bps),
        "false_negatives": len(gt_bps - valid),
        "recall": round(recall, 4),
        "precision": round(precision, 4),
        "f1": round(f1, 4),
        "valid_cited_bps": sorted(valid),  # for diagnostics (set diff vs GT)
    }


def score_run(cli_result: dict, gt_bps: set[str], canonical: set[str]) -> dict:
    """Score both the user-facing report and the full subagent-inclusive text."""
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
        # BOTH metrics side-by-side
        "report": report_scores,       # what the user sees in the assembled report
        "subagent_total": subagent_scores,  # what all subagents surfaced combined
        # cost & latency
        "total_cost_usd": final.get("total_cost_usd"),
        "duration_ms": final.get("duration_ms"),
        "duration_api_ms": final.get("duration_api_ms"),
        "ttft_ms": final.get("ttft_ms"),
        "wall_s": cli_result.get("wall_s"),
        # tokens
        "input_tokens": usage.get("input_tokens"),
        "output_tokens": usage.get("output_tokens"),
        "cache_creation_input_tokens": usage.get("cache_creation_input_tokens"),
        "cache_read_input_tokens": usage.get("cache_read_input_tokens"),
        # orchestration
        "num_turns": final.get("num_turns"),
        "permission_denials": final.get("permission_denials", []),
        "stop_reason": final.get("stop_reason"),
        "model_used": final.get("modelUsage") if isinstance(final.get("modelUsage"), dict) else None,
        # raw
        "assembled_text_len": len(assembled_text),
        "all_text_len": len(all_text),
        "assembled_head": assembled_text[:400],
    }


def aggregate(runs: list[dict]) -> dict:
    """Mean ± stdev across successful runs."""
    ok = [r for r in runs if "error" not in r]
    if not ok:
        return {"n_successful": 0}

    def stats(key: str) -> dict | None:
        vals = [r.get(key) for r in ok if r.get(key) is not None]
        if not vals:
            return None
        return {
            "mean": round(statistics.mean(vals), 4),
            "stdev": round(statistics.stdev(vals), 4) if len(vals) > 1 else 0.0,
            "min": min(vals),
            "max": max(vals),
        }

    def nested_stats(sub_key: str, key: str) -> dict | None:
        vals = [r.get(sub_key, {}).get(key) for r in ok
                if isinstance(r.get(sub_key), dict) and r[sub_key].get(key) is not None]
        if not vals:
            return None
        return {
            "mean": round(statistics.mean(vals), 4),
            "stdev": round(statistics.stdev(vals), 4) if len(vals) > 1 else 0.0,
            "min": min(vals),
            "max": max(vals),
        }

    return {
        "n_successful": len(ok),
        "report_f1": nested_stats("report", "f1"),
        "report_recall": nested_stats("report", "recall"),
        "report_precision": nested_stats("report", "precision"),
        "subagent_total_f1": nested_stats("subagent_total", "f1"),
        "subagent_total_recall": nested_stats("subagent_total", "recall"),
        "subagent_total_precision": nested_stats("subagent_total", "precision"),
        "total_cost_usd": stats("total_cost_usd"),
        "duration_ms": stats("duration_ms"),
        "wall_s": stats("wall_s"),
        "input_tokens": stats("input_tokens"),
        "output_tokens": stats("output_tokens"),
        "cache_read_input_tokens": stats("cache_read_input_tokens"),
        "num_turns": stats("num_turns"),
    }


def main() -> int:
    canonical = build_canonical_bps()
    cases = load_eval_cases()
    print(f"Canonical corpus: {len(canonical)} BPs")
    print(f"Eval cases: {len(cases)}")
    print(f"Model: {MODEL}, runs per case: {RUNS_PER_CASE}")
    print(f"Total CLI invocations: {len(cases) * RUNS_PER_CASE}")

    results = {"model": MODEL, "runs_per_case": RUNS_PER_CASE, "cases": []}

    for case in cases:
        case_id = case["id"]
        prompt = case["prompt"]
        gt = load_ground_truth(case_id)
        print(f"\n=== Case {case_id} (|GT|={len(gt)}) ===")

        case_runs: list[dict] = []
        wrapped = AUTONOMOUS_PREAMBLE + prompt
        for run_idx in range(1, RUNS_PER_CASE + 1):
            print(f"  Run {run_idx}/{RUNS_PER_CASE}...", end="", flush=True)
            cli_result = run_claude_cli(wrapped)
            scored = score_run(cli_result, gt, canonical)
            scored["run_idx"] = run_idx
            case_runs.append(scored)
            if "error" in scored:
                print(f" ✗ {scored['error']}")
            else:
                rep = scored["report"]
                sub = scored["subagent_total"]
                print(f" ✓ report F1={rep['f1']:.3f} (R={rep['recall']:.2f} P={rep['precision']:.2f}) | "
                      f"subagent F1={sub['f1']:.3f} (R={sub['recall']:.2f} P={sub['precision']:.2f}) | "
                      f"${scored['total_cost_usd']:.3f}, "
                      f"{scored['duration_ms']/1000:.0f}s")

        agg = aggregate(case_runs)
        results["cases"].append({
            "case_id": case_id,
            "prompt": prompt[:200],
            "runs": case_runs,
            "aggregate": agg,
        })
        rf1 = agg.get('report_f1', {})
        sf1 = agg.get('subagent_total_f1', {})
        print(f"  Case {case_id} mean report F1: {rf1.get('mean') if rf1 else 'n/a'} | "
              f"subagent F1: {sf1.get('mean') if sf1 else 'n/a'}")

        # Save incrementally so partial data survives a crash
        out_file = SCRIPT_DIR / "wa_review_effectiveness.json"
        out_file.write_text(json.dumps(results, indent=2))

    print(f"\nSaved: {out_file.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
