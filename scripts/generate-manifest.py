#!/usr/bin/env python3
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
"""Generate references/manifest.md — a single lightweight index of all 307 BPs.

Scans references/questions/*.md for canonical BP definitions (H1 headings matching
`# {ID} {title}`) and emits a compact manifest the wa-review skill loads first.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
REFS = REPO_ROOT / "skills" / "wa-review" / "references" / "questions"
OUTPUT = REPO_ROOT / "skills" / "wa-review" / "references" / "manifest.md"

# Match H1 heading of question or BP.
Q_H1 = re.compile(r"^# ((OPS|SEC|REL|PERF|COST|SUS) \d+)\s*[—-]\s*(.+)$", re.MULTILINE)
BP_H1 = re.compile(r"^# ([A-Z]{2,}\d{1,3}-BP\d{1,3})\s+(.+)$", re.MULTILINE)


def main() -> int:
    if not REFS.exists():
        print(f"Missing: {REFS}", file=sys.stderr)
        return 1

    pillar_order = ["OPS", "SEC", "REL", "PERF", "COST", "SUS"]
    pillar_names = {
        "OPS": "Operational Excellence",
        "SEC": "Security",
        "REL": "Reliability",
        "PERF": "Performance Efficiency",
        "COST": "Cost Optimization",
        "SUS": "Sustainability",
    }

    # Collect all questions and BPs
    questions: dict[str, tuple[str, list[tuple[str, str]]]] = {}
    for qfile in sorted(REFS.glob("*.md")):
        content = qfile.read_text()
        qmatch = Q_H1.search(content)
        if not qmatch:
            continue
        qid_readable = qmatch.group(1)
        qid = qid_readable.replace(" ", "")
        qtitle = qmatch.group(3).strip()
        bps = [(m.group(1), m.group(2).strip()) for m in BP_H1.finditer(content)]
        questions[qid] = (qtitle, bps)

    lines = [
        "# Well-Architected Framework — Best Practice Manifest",
        "",
        "This is a lightweight index of every WA Framework question and best practice.",
        "**Load this file first for any full review** — it gives you the complete catalog",
        "of BP IDs (in canonical `PILLAR##-BP##` format) so you know what to cite from.",
        "",
        "For detailed BP guidance (implementation, anti-patterns, resources), load the",
        "corresponding per-pillar file at `references/pillars/{pillar-slug}.md`.",
        "",
        "---",
        "",
    ]

    total_bps = 0
    for prefix in pillar_order:
        pillar_qs = [(q, t, bps) for q, (t, bps) in sorted(questions.items())
                     if q.startswith(prefix)]
        # Sort by numeric suffix
        pillar_qs.sort(key=lambda x: int(re.sub(r"[^\d]", "", x[0])))
        lines.append(f"## {pillar_names[prefix]} ({prefix})")
        lines.append("")
        for qid, qtitle, bps in pillar_qs:
            lines.append(f"### {qid} — {qtitle} ({len(bps)} BPs)")
            for bp_id, bp_title in bps:
                lines.append(f"- `{bp_id}` — {bp_title}")
                total_bps += 1
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"**Total: {sum(len(bps) for _, bps in questions.values())} BPs across "
                 f"{len(questions)} questions in 6 pillars.**")
    lines.append("")

    OUTPUT.write_text("\n".join(lines))
    size_kb = OUTPUT.stat().st_size / 1024
    print(f"Wrote {OUTPUT.relative_to(REPO_ROOT)} — {size_kb:.1f} KB, {total_bps} BPs, {len(questions)} questions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
