# CLI Effectiveness — measure skills in a real Task-capable runtime

The `evals/run.py` framework (one directory up) uses raw Amazon Bedrock Converse API. Converse has **no `Task` tool**, so it can't execute skills whose value depends on subagent dispatch. `wa-review` is exactly that kind of skill — since v4.2 it dispatches 6 parallel pillar subagents, and its full-review path can only be measured in a runtime that supports the `Task` tool.

This directory ships the real-measurement harness we used to validate `wa-review` end-to-end. It invokes **Claude Code CLI** (`claude -p`) as the runtime and scores output against a **frozen ground truth of applicable Best Practices** derived from a 2-model × 5-run consensus panel.

## What you get

- `measure_wa_review.py` — invokes `claude -p` with the wa-review skill installed and scores against ground truth
- `measure_baseline.py` — paired baseline: `claude -p --safe-mode --disable-slash-commands` from a scratch workdir (no skill, no CLAUDE.md, no plugins). Same prompts, same ground truth. The delta between the two is the honest measure of what the skill adds.
- `generate_ground_truth.py` — regenerates the ground truth. Not needed for the shipped v1 data (already in `ground_truth/`), but useful if you want to re-derive against different consensus rules or additional models.
- `ground_truth/case_N.json` — six frozen consensus datasets, one per eval case. Each JSON contains the consensus applicable-BP list and per-model per-run citation frequencies.

## When to use this vs `evals/run.py`

| You have… | Use |
| --------- | --- |
| A skill that depends on `Task` subagents, MCP tools, or other runtime affordances | `cli_effectiveness/` (this directory) |
| A skill whose value is captured by a well-crafted `SKILL.md` alone (no runtime tool calls) | `evals/run.py` — the LLM-as-judge framework is cheaper and faster |

`evals/run.py` remains the appropriate framework for `wa-builder`, `wa-guardrails`, `wafr-facilitator`, and `migration-readiness` — none of those depend on Task subagents. For `wa-review`, only the CLI effectiveness harness produces honest numbers.

## Reproducing our published F1 = 0.96

**Prerequisites:**

- Claude Code CLI installed (`claude --version`)
- AWS credentials with Bedrock access enabled for Anthropic and OpenAI GPT OSS 120B in `us-east-1`
- The `wa-review` skill installed globally (`./install.sh --global` from the repo root)
- Python 3.13+ and [uv](https://docs.astral.sh/uv/) for the Bedrock-based ground truth generator (only if regenerating; not needed to score against the shipped ground truth)

**Run both configurations:**

```bash
cd evals

# With skill — measures wa-review end-to-end in Claude Code CLI
uv run python cli_effectiveness/measure_wa_review.py

# Without skill — paired baseline (no wa-review, no plugins)
uv run python cli_effectiveness/measure_baseline.py
```

Each configuration runs 18 CLI invocations (6 cases × 3 runs). Results are saved to:

- `cli_effectiveness/wa_review_effectiveness.json`
- `cli_effectiveness/wa_review_baseline.json`

Both files are gitignored — they're your local measurements.

**Expected results (v2.2 wa-review, Opus tier):**

| Configuration | Mean report F1 | Mean recall | Cost/run | Wall/run |
| ------------- | -------------- | ----------- | -------- | -------- |
| With skill | **0.960** | **1.00** | ~$7 | ~11 min |
| Baseline | 0.264 | 0.15 | ~$0.10 | ~1 min |
| **Delta** | **+0.70** | **+0.85** | 69× | 11× |

If your numbers land far below this (say, report F1 < 0.85 with skill), likely causes:

1. **Older wa-review version** — v2.2's Full BP Ledger is what closes the compression gap. Check `~/.claude/skills/wa-review/SKILL.md` header for `version: 2.2.0` or later.
2. **Different model tier** — these numbers are Opus. Sonnet or Haiku produce different results.
3. **Skill install location** — Claude Code reads `~/.claude/skills/`. If the skill lives elsewhere (e.g. project-local `.claude/`) the harness may not find it.

## Ground truth methodology

For each of the 6 eval cases, we ran a consensus panel:

- **2 top-tier models**: Claude Sonnet 5 and OpenAI GPT OSS 120B, both via Amazon Bedrock
- **5 independent runs per model** with subagent-per-pillar dispatch (`call_model_subagent` from `evals/benchmark.py`) — 60 runs total per case
- **Consensus rule**: a BP is "applicable" only if cited by **both models** in **≥3 of their 5 runs**

This yields 270–306 applicable BPs per case out of the 307-BP canonical corpus — a defensible set of "what a strong review should catch" that neither model alone could have hallucinated into existence.

The two-model panel was chosen after Claude Fable 5 (originally the third judge) was heavily throttled on both `bedrock-runtime` and `bedrock-mantle` endpoints, producing zero successful runs. Sonnet 5 and GPT OSS 120B both scored 5.0/5 in our earlier per-question quality benchmark, so their intersection is a strong signal.

To regenerate:

```bash
cd evals
uv run python cli_effectiveness/generate_ground_truth.py
```

Cost: ~$40, ~30 min. Not needed unless you're deliberately re-deriving the ground truth (e.g., updated framework, different consensus rule, or new judge models).

## Scoring details

- **Case 4** is a pillar-scoped test ("Review only Security and Reliability"). It's scored against the SEC + REL subset of its ground truth (116 of 280 consensus BPs) so pillar-scoped mode is measured fairly — the skill correctly runs only 2 subagents on Case 4 and should not be penalized for the 4 pillars it was told not to review.
- **Precision denominator** is BPs cited by the review that appear in the 307-BP canonical corpus (drops hallucinations at the extraction layer). Precision at both layers stays ≥ 0.88.
- **Recall denominator** is the case's ground truth (270–306 BPs, or 116 for Case 4).
- **BP citation extraction** normalizes Unicode hyphens — models frequently emit `SEC03‑BP02` (non-breaking hyphen U+2011) or `SEC03‐BP02` (hyphen U+2010) instead of ASCII `SEC03-BP02`. The extractor accepts all common variants.

## Limitations

- **Six cases is a small sample.** The variance we measure (zero in v2.2, moderate in baseline) is within-configuration; between-workload generalization is a separate question.
- **Consensus ground truth is not oracle truth.** Two models agreeing on a BP doesn't guarantee it's actually applicable; it means two strong models thought so. Case 3's slightly weaker consensus (4.2% borderline BPs vs 1.3% for Case 2) hints at this.
- **F1 is not the whole story.** A review that hits F1 = 1.00 by enumerating every BP is not automatically useful — the *severity* assignment and *recommendation* content matter too. This harness measures citation coverage only.
- **Opus tier is expensive.** ~$7 per with-skill run × 18 runs = ~$125 to reproduce the full effectiveness measurement. The baseline is ~$2 total.
