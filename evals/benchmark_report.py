#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""
Generate a markdown report from benchmark results and optionally update the README.

Usage:
    python benchmark_report.py results/benchmark-20260701-143022.json
    python benchmark_report.py results/benchmark-20260701-143022.json --update-readme
"""

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
README_PATH = REPO_ROOT / "README.md"

# Markers in README where benchmark table gets inserted
BENCH_START = "<!-- BENCHMARK-START -->"
BENCH_END = "<!-- BENCHMARK-END -->"


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

    # Header
    header = "| Model | Input Tokens | Output Tokens | Latency (s) | Tokens/s |"
    separator = "|-------|-------------:|--------------:|------------:|---------:|"
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
            if has_grades:
                row += " — |"
            lines.append(row)
            continue

        row = (f"| {name} | {r['input_tokens']:,} | {r['output_tokens']:,} | "
               f"{r['latency_s']:.1f} | {r['tokens_per_sec']:.0f} |")
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
    lines.append(f"- Run with: `cd evals && python benchmark.py --grade`")
    lines.append(f"")
    lines.append(f"</details>")

    return "\n".join(lines)


def update_readme(markdown: str):
    """Insert benchmark markdown between markers in README."""
    if not README_PATH.exists():
        print(f"README not found at {README_PATH}", file=sys.stderr)
        sys.exit(1)

    content = README_PATH.read_text(encoding="utf-8")

    if BENCH_START not in content:
        print(f"Marker '{BENCH_START}' not found in README. Add it where you want the table.", file=sys.stderr)
        sys.exit(1)

    pattern = re.compile(
        rf"({re.escape(BENCH_START)})\n.*?\n({re.escape(BENCH_END)})",
        re.DOTALL,
    )
    replacement = f"{BENCH_START}\n{markdown}\n{BENCH_END}"
    new_content = pattern.sub(replacement, content)

    README_PATH.write_text(new_content, encoding="utf-8")
    print(f"✓ README updated with benchmark results")


def main():
    parser = argparse.ArgumentParser(description="Generate benchmark report")
    parser.add_argument("results_file", type=Path, help="Path to benchmark JSON results")
    parser.add_argument("--update-readme", action="store_true", help="Update README.md with results")
    args = parser.parse_args()

    benchmark = load_results(args.results_file)
    markdown = generate_markdown(benchmark)

    print(markdown)

    if args.update_readme:
        update_readme(markdown)


if __name__ == "__main__":
    main()
