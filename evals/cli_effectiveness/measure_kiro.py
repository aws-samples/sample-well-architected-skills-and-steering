#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Measure wa-review effectiveness via real Kiro CLI runs.

Parallel to measure_wa_review.py but uses kiro-cli instead of claude -p.
Kiro loads skills from ~/.kiro/skills/ and steering from ~/.kiro/steering/.

Install the skill first:
    ./install.sh --global --tool kiro   (from the repo root)

For each eval case, invokes:
    kiro-cli chat --no-interactive --trust-all-tools "{prompt}"

Session logs are parsed from ~/.kiro/sessions/cli/*.jsonl — same approach
as measure_wa_review.py but with Kiro's session format:
  {"version":"v1","kind":"AssistantMessage","data":{"content":[{"kind":"text","data":"..."}]}}

Cost is not available in USD from Kiro sessions (Kiro shows credits, not USD).
Token counts are not directly exposed. Wall clock and F1/recall are the primary metrics.

Output: evals/cli_effectiveness/kiro_effectiveness.json
"""
from __future__ import annotations

import ast
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

RUNS_PER_CASE = 3
CLI_TIMEOUT_SEC = 3600  # 60 min — Kiro + Opus subagent dispatch can be slow
# Match the model used in measure_wa_review.py for a fair runtime comparison
KIRO_MODEL = "claude-opus-4.6"   # same as CC CLI global.anthropic.claude-opus-4-6-v1
RESULTS_FILE = SCRIPT_DIR / "kiro_effectiveness.json"
KIRO_SESSIONS = Path.home() / ".kiro" / "sessions" / "cli"

AUTONOMOUS_PREAMBLE = """[NON-INTERACTIVE EVAL MODE — no follow-up questions possible]

Use the /wa-review skill. Skip the discovery checkpoint. Proceed directly to the
full review based ONLY on the workload description below — do NOT ask for code,
scope confirmation, or clarification. If information is missing, mark findings
as "Based on description — verify in code" and continue.

Dispatch the 6 parallel pillar subagents as instructed by SKILL.md Step 4b.
Every Best Practice you cite MUST use the canonical WA identifier format
`PILLAR##-BP##` (e.g., SEC01-BP02, REL06-BP04, COST05-BP03). Target full
307-BP corpus. Produce the full report as specified in SKILL.md.

CRITICAL: Do NOT offer follow-up actions, do NOT ask "Would you like me to...",
do NOT offer to produce the Full BP Ledger as a separate step — produce it
immediately as part of the report. The session ends after your response.
There is no user to respond to follow-up offers.

===== WORKLOAD =====
"""

BP_PATTERN = re.compile(r"\b([A-Z]{2,}\d{1,3})[-‐‑–]BP(\d{1,3})\b")


def _extract_bps(text: str) -> set[str]:
    return {f"{m.group(1)}-BP{m.group(2)}" for m in BP_PATTERN.finditer(text)}


def build_canonical_bps() -> set[str]:
    refs_dir = REPO_ROOT / "skills" / "wa-review" / "references" / "pillars"
    canonical: set[str] = set()
    bp_re = re.compile(r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\b", re.MULTILINE)
    for f in refs_dir.glob("*.md"):
        for m in bp_re.finditer(f.read_text()):
            canonical.add(m.group(1))
    return canonical


def load_eval_cases() -> list[dict]:
    data = json.loads(
        (REPO_ROOT / "skills" / "wa-review" / "evals" / "evals.json").read_text()
    )
    return data["evals"]


def load_ground_truth(case_id: int) -> set[str]:
    return set(json.loads((GT_DIR / f"case_{case_id}.json").read_text())
               ["ground_truth"]["consensus_bps"])


def _find_kiro_session(started_at: float) -> Path | None:
    """Find the most recent Kiro CLI session started after `started_at`."""
    if not KIRO_SESSIONS.exists():
        return None
    candidates = [
        (f.stat().st_mtime, f)
        for f in KIRO_SESSIONS.glob("*.jsonl")
        if f.stat().st_mtime >= started_at
    ]
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[0], reverse=True)
    return candidates[0][1]


def _parse_kiro_session(session_file: Path) -> tuple[str, str]:
    """Parse a Kiro session JSONL and return (assembled_text, all_text).

    Kiro session format:
      {"version":"v1","kind":"AssistantMessage","data":{"content":[{"kind":"text","data":"..."}]}}
      {"version":"v1","kind":"ToolResults","data":{"content":[{"kind":"toolResult","data":{...}}]}}
    """
    all_chunks: list[str] = []
    last_assistant: list[str] = []

    for line in session_file.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue

        kind = ev.get("kind", "")
        # data may be a string (ast.literal_eval) or a dict
        raw_data = ev.get("data", {})
        if isinstance(raw_data, str):
            try:
                data = ast.literal_eval(raw_data)
            except Exception:
                continue
        else:
            data = raw_data

        if kind == "AssistantMessage":
            content = data.get("content", []) if isinstance(data, dict) else []
            for block in content:
                if isinstance(block, dict):
                    if block.get("kind") == "text":
                        txt = block.get("data", "")
                        if isinstance(txt, str) and txt:
                            all_chunks.append(txt)
                            last_assistant.append(txt)
                    elif block.get("kind") in ("toolUse", "tool_use"):
                        last_assistant = []  # reset on tool call

        elif kind == "ToolResults":
            content = data.get("content", []) if isinstance(data, dict) else []
            for block in content:
                if isinstance(block, dict) and block.get("kind") == "toolResult":
                    result = block.get("data", {})
                    if isinstance(result, dict):
                        for rb in result.get("content", []):
                            if isinstance(rb, dict) and rb.get("kind") == "text":
                                txt = rb.get("data", "")
                                if isinstance(txt, str) and txt:
                                    all_chunks.append(txt)

    return "\n".join(last_assistant), "\n".join(all_chunks)


ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')


def _strip_ansi(text: str) -> str:
    return ANSI_ESCAPE.sub("", text)


def run_kiro(prompt: str) -> dict:
    """Invoke kiro-cli chat --no-interactive with the prompt.

    kiro-cli --no-interactive does NOT write a session .jsonl file —
    it streams response to stdout only. We parse stdout directly after
    stripping ANSI escape codes.
    """
    start = time.time()
    wrapped = AUTONOMOUS_PREAMBLE + prompt
    try:
        proc = subprocess.run(
            [
                "kiro-cli", "chat",
                "--no-interactive",
                "--trust-all-tools",
                "--model", KIRO_MODEL,
                wrapped,
            ],
            capture_output=True,
            text=True,
            timeout=CLI_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "wall_s": time.time() - start}

    wall_s = time.time() - start
    stdout_clean = _strip_ansi(proc.stdout)

    if not stdout_clean.strip():
        return {
            "error": f"empty output (exit {proc.returncode})",
            "stderr": proc.stderr[-300:],
            "wall_s": wall_s,
        }

    # Extract credits — Kiro writes "▸ Credits: X.XX • Time: Xs" to stderr
    credits_used = None
    import re as _re
    stderr_clean = ANSI_ESCAPE.sub("", proc.stderr)
    credits_match = _re.search(r'Credits:\s*([\d.]+)', stderr_clean)
    if credits_match:
        try:
            credits_used = float(credits_match.group(1))
        except ValueError:
            pass

    # Strip Kiro UI chrome, keep only the model response
    lines = stdout_clean.splitlines()
    content_lines = [
        l for l in lines
        if not any(marker in l for marker in [
            "Credits:", "Time:", "Checkpoints are enabled",
            "All tools are now trusted", "Learn more at",
            "Agents can sometimes", "took ", "▸ "
        ])
    ]
    assembled_text = "\n".join(content_lines).strip()

    return {
        "assembled_text": assembled_text,
        "all_text": assembled_text,
        "session_file": None,
        "wall_s": wall_s,
        "exit_code": proc.returncode,
        "stdout_len": len(assembled_text),
        "credits_used": credits_used,
    }


def score(cited_set: set[str], gt: set[str], canonical: set[str]) -> dict:
    valid = cited_set & canonical
    tp = valid & gt
    r = len(tp) / len(gt) if gt else 0.0
    p = len(tp) / len(valid) if valid else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return {
        "cited_count": len(cited_set),
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
    # Verify kiro-cli is available
    try:
        v = subprocess.run(["kiro-cli", "--version"], capture_output=True, text=True, timeout=10)
        print(f"kiro-cli version: {v.stdout.strip()}")
    except Exception as e:
        print(f"kiro-cli not found: {e}")
        return 1

    # Verify skill is installed
    skill_path = Path.home() / ".kiro" / "skills" / "wa-review" / "SKILL.md"
    if not skill_path.exists():
        print(f"wa-review skill not found at {skill_path}")
        print("Run: ./install.sh --global --tool kiro  (from repo root)")
        return 1
    skill_version = ""
    for line in skill_path.read_text().splitlines():
        if line.startswith("version:"):
            skill_version = line.split(":", 1)[1].strip()
            break
    print(f"wa-review SKILL.md version: {skill_version}")

    canonical = build_canonical_bps()
    cases = load_eval_cases()
    print(f"Canonical: {len(canonical)} BPs | Cases: {len(cases)} | Runs: {RUNS_PER_CASE}")
    print(f"Total Kiro invocations: {len(cases) * RUNS_PER_CASE}\n")

    # Load partial results if they exist (resume support)
    if RESULTS_FILE.exists():
        results = json.loads(RESULTS_FILE.read_text())
        completed_ids = {c["case_id"] for c in results.get("cases", [])
                         if len([r for r in c.get("runs", []) if "error" not in r]) >= RUNS_PER_CASE}
        if completed_ids:
            print(f"Resuming — skipping already-completed cases: {sorted(completed_ids)}")
    else:
        results = {
            "runtime": "kiro-cli",
            "model": KIRO_MODEL,
            "skill_version": skill_version,
            "runs_per_case": RUNS_PER_CASE,
            "cases": [],
        }
        completed_ids = set()

    for case in cases:
        if case["id"] in completed_ids:
            print(f"  Skipping Case {case['id']} (already complete)")
            continue
        case_id = case["id"]
        prompt = case["prompt"]
        gt = load_ground_truth(case_id)
        gt_scoring = ({b for b in gt if b.startswith("SEC") or b.startswith("REL")}
                      if case_id == 4 else gt)
        scope = "SEC+REL only" if case_id == 4 else "full 6 pillars"
        print(f"=== Case {case_id} (|GT|={len(gt_scoring)}, {scope}) ===")
        print(f"  {prompt[:80]}...")

        case_runs: list[dict] = []
        for run_idx in range(1, RUNS_PER_CASE + 1):
            print(f"  Run {run_idx}/{RUNS_PER_CASE} started...", flush=True)
            result = run_kiro(prompt)
            print(f"  Run {run_idx}/{RUNS_PER_CASE} finished ({result.get('wall_s', 0):.0f}s) — ", end="", flush=True)

            if "error" in result:
                print(f" ✗ {result['error']}")
                case_runs.append({"run_idx": run_idx, "error": result["error"],
                                   "wall_s": result.get("wall_s", 0)})
                continue

            assembled_text = result.get("assembled_text", "")
            all_text = result.get("all_text", "")
            rep = score(_extract_bps(assembled_text), gt_scoring, canonical)
            sub = score(_extract_bps(all_text), gt_scoring, canonical)

            credits = result.get("credits_used")
            run = {
                "run_idx": run_idx,
                "gt_count": len(gt_scoring),
                "gt_scope": scope,
                "report": rep,
                "subagent_total": sub,
                "wall_s": result["wall_s"],
                "session_file": result["session_file"],
                "assembled_text_len": len(assembled_text),
                "all_text_len": len(all_text),
                "credits_used": credits,
            }
            case_runs.append(run)
            credits_str = f" credits={credits:.2f}" if credits is not None else ""
            print(f" ✓ report F1={rep['f1']:.3f} (R={rep['recall']:.2f} P={rep['precision']:.2f}) "
                  f"| sub F1={sub['f1']:.3f} | {result['wall_s']:.0f}s{credits_str}")

        # Aggregate
        ok = [r for r in case_runs if "error" not in r]
        agg: dict = {}
        if ok:
            for layer in ("report", "subagent_total"):
                for metric in ("f1", "recall", "precision", "valid_cited_count"):
                    vals = [r[layer][metric] for r in ok]
                    agg.setdefault(layer, {})[metric] = {
                        "mean": round(statistics.mean(vals), 4),
                        "stdev": round(statistics.stdev(vals), 4) if len(vals) > 1 else 0.0,
                    }
            wall_vals = [r["wall_s"] for r in ok]
            agg["wall_s"] = {"mean": round(statistics.mean(wall_vals), 1),
                             "stdev": round(statistics.stdev(wall_vals), 1) if len(wall_vals) > 1 else 0.0}

        results["cases"].append({
            "case_id": case_id,
            "prompt": prompt[:200],
            "gt_scope": scope,
            "runs": case_runs,
            "aggregate": agg,
        })

        if agg:
            rf1 = agg.get("report", {}).get("f1", {}).get("mean", "n/a")
            sf1 = agg.get("subagent_total", {}).get("f1", {}).get("mean", "n/a")
            print(f"  Case {case_id} mean report F1: {rf1} | subagent F1: {sf1}")

        RESULTS_FILE.write_text(json.dumps(results, indent=2))

    print(f"\nSaved: {RESULTS_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
