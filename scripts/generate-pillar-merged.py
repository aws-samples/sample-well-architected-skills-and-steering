#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Generate pillar-merged reference files in skills/wa-review/references/pillars/.

Merges all per-question files for a pillar into a single markdown file. This
reduces file count from 57 to 6 while preserving all BP content, and helps AI
agents avoid the "read selectively, skip most files" behavior seen with the
57-file layout.

The per-question files remain as the canonical source; pillars/ are a derived,
consumption-friendly view.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
QUESTIONS = REPO_ROOT / "skills" / "wa-review" / "references" / "questions"
OUTPUT = REPO_ROOT / "skills" / "wa-review" / "references" / "pillars"

PILLARS = {
    "operational-excellence": ("OPS", 11),
    "security": ("SEC", 11),
    "reliability": ("REL", 13),
    "performance-efficiency": ("PERF", 5),
    "cost-optimization": ("COST", 11),
    "sustainability": ("SUS", 6),
}


def merge_pillar(pillar_name: str, prefix: str, count: int) -> str:
    parts = [
        f"# {pillar_name.replace('-', ' ').title()} — All Questions & Best Practices",
        "",
        f"This file contains all {count} WA Framework questions for the {pillar_name} pillar",
        "and their complete best-practice content. Load this ONE file to have the entire",
        f"pillar in context at once — no need for {count} separate Read calls.",
        "",
        "For a lightweight catalog of every BP ID across all 6 pillars, see",
        "`references/manifest.md`.",
        "",
        "---",
        "",
    ]

    for i in range(1, count + 1):
        qid = f"{prefix}{i:02d}"
        qfile = QUESTIONS / f"{qid}.md"
        if not qfile.exists():
            print(f"  warn: missing {qfile.name}", file=sys.stderr)
            continue
        content = qfile.read_text()
        parts.append(f"## Question {qid}")
        parts.append("")
        parts.append(content.strip())
        parts.append("")
        parts.append("---")
        parts.append("")

    return "\n".join(parts)


def main() -> int:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for pillar_name, (prefix, count) in PILLARS.items():
        merged = merge_pillar(pillar_name, prefix, count)
        out_file = OUTPUT / f"{pillar_name}.md"
        out_file.write_text(merged)
        size_kb = len(merged) / 1024
        print(f"  {pillar_name:<25s} → {size_kb:>6.1f} KB ({count} questions merged)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
