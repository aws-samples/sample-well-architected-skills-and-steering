#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
Generate a markdown report from your own benchmark results.

The report is a measurement of your models in your account. It prints to stdout
and, with --out, writes under evals/results/, which is gitignored. There is
deliberately no path from this script into a tracked file: this repository ships
the benchmark, not its results. See CONTRIBUTING.md, "Measurement results stay
local".

Usage:
    uv run python benchmark_report.py results/benchmark-20260701-143022.json
    uv run python benchmark_report.py results/benchmark-20260701-143022.json --out report.md
"""

import argparse
import json
import re
from pathlib import Path

EVALS_DIR = Path(__file__).parent
RESULTS_DIR = EVALS_DIR / "results"


def load_results(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def format_model_name(model_id: str) -> str:
    """Shorten model ID for display."""
    name = model_id
    for prefix in ("us.", "anthropic.", "amazon.", "meta.", "mistral.", "deepseek.", "cohere."):
        name = name.replace(prefix, "")
    name = re.sub(r"-v\d+:\d+$", "", name)
    return name


def generate_markdown(benchmark: dict) -> str:
    """Generate markdown table from benchmark results."""
    results = benchmark["results"]
    config = benchmark["config"]
    timestamp = benchmark.get("timestamp", "unknown")

    lines = []
    lines.append(f"### Model Benchmark Results")
    lines.append(f"")
    lines.append(f"**Last run:** {timestamp} | **Region:** {config['region']} | "
                 f"**Prompt:** {config['prompt_chars']:,} chars | "
                 f"**Max tokens:** {config['max_tokens']:,}")
    lines.append(f"")

    has_grades = any("grade" in r and "overall" in r.get("grade", {}) for r in results)
    has_cost = any("cost_usd" in r for r in results)

    # Header
    header = "| Model | Input Tokens | Output Tokens | Latency (s) | Tokens/s |"
    separator = "|-------|-------------:|--------------:|------------:|---------:|"
    if has_cost:
        header += " Cost |"
        separator += "------:|"
    if has_grades:
        header += " Quality |"
        separator += "--------:|"
    lines.append(header)
    lines.append(separator)

    # Sort by quality (if graded) then by latency
    def sort_key(r):
        if "error" in r:
            return (0, 999)
        grade = r.get("grade", {}).get("overall", 0)
        return (-grade, r["latency_s"])

    for r in sorted(results, key=sort_key):
        name = format_model_name(r["model_id"])
        if "error" in r:
            row = f"| {name} | — | — | {r['latency_s']:.1f} | — |"
            if has_cost:
                row += " — |"
            if has_grades:
                row += " — |"
            lines.append(row)
            continue

        row = (f"| {name} | {r['input_tokens']:,} | {r['output_tokens']:,} | "
               f"{r['latency_s']:.1f} | {r['tokens_per_sec']:.0f} |")
        if has_cost:
            cost = r.get("cost_usd")
            row += f" ${cost:.4f} |" if cost is not None else " — |"
        if has_grades:
            grade = r.get("grade", {}).get("overall")
            row += f" {grade:.1f}/5 |" if grade else " — |"
        lines.append(row)

    lines.append("")
    lines.append(f"<details><summary>Benchmark details</summary>")
    lines.append(f"")
    lines.append(f"- Task: Well-Architected review of an e-commerce Terraform architecture")
    lines.append(f"- Temperature: {config['temperature']}")
    lines.append(f"- Models tested: {config['models_tested']}")
    if has_grades:
        grading_model = benchmark.get("config", {}).get("grading_model", "unknown")
        lines.append(f"- Quality graded by: {grading_model}")
        lines.append(f"- Criteria: coverage of 6 pillars, identification of key risks, actionability")
    lines.append(f"- Run with: `cd evals && uv run python benchmark.py --grade`")
    lines.append(f"")
    lines.append(f"</details>")

    return "\n".join(lines)


def resolve_out_path(out: Path) -> Path:
    """Resolve --out under evals/results/, which is gitignored.

    A bare filename lands in evals/results/. An absolute or parent-relative path
    is rejected rather than silently written somewhere tracked.
    """
    candidate = (RESULTS_DIR / out).resolve() if not out.is_absolute() else out.resolve()
    if RESULTS_DIR.resolve() not in candidate.parents:
        raise SystemExit(
            f"--out must stay under {RESULTS_DIR.relative_to(EVALS_DIR.parent)}/ "
            "(gitignored). Benchmark results are not published from this repo."
        )
    return candidate


def main():
    parser = argparse.ArgumentParser(description="Generate benchmark report")
    parser.add_argument("results_file", type=Path, help="Path to benchmark JSON results")
    parser.add_argument("--out", type=Path,
                        help="Also write the report to this file under evals/results/")
    args = parser.parse_args()

    benchmark = load_results(args.results_file)
    markdown = generate_markdown(benchmark)

    print(markdown)

    if args.out:
        out_path = resolve_out_path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(markdown + "\n", encoding="utf-8")
        print(f"\n✓ Report written to {out_path} (local only)")


if __name__ == "__main__":
    main()
