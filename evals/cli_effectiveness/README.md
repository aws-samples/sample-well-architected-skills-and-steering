# CLI Effectiveness — measure skills in a real Task-capable runtime

The `evals/run.py` framework (one directory up) uses raw Amazon Bedrock Converse API. Converse has **no `Task` tool**, so it can't execute skills whose value depends on subagent dispatch. `wa-review` is exactly that kind of skill — since v4.2 it dispatches 6 parallel pillar subagents, and its full-review path can only be measured in a runtime that supports the `Task` tool.

This directory ships the real-measurement harness we used to validate `wa-review` end-to-end. It invokes **Claude Code CLI** (`claude -p`) as the runtime and scores output against a **frozen ground truth of applicable Best Practices** derived from a 2-model × 5-run consensus panel.

> **Note on published results:** The F1 and recall numbers in this repository (wa-review v2.2: F1 = 0.960, recall = 1.00) reflect a controlled evaluation — specific workload prompts, Opus tier, a specific ground truth panel, and a fixed point in time. **Customers are responsible for running their own evaluations** against their workloads, model tiers, and requirements before making data-driven decisions. The harness scripts and ground truth are provided so you can do exactly that.

## What you get

- `measure_wa_review.py` — invokes `claude -p` with the wa-review skill installed and scores against ground truth
- `measure_baseline.py` — paired baseline: `claude -p --safe-mode --disable-slash-commands` from a scratch workdir (no skill, no CLAUDE.md, no plugins). Same prompts, same ground truth. The delta between the two is the honest measure of what the skill adds.
- `generate_ground_truth.py` — regenerates the ground truth. Not needed for the shipped v1 data (already in `ground_truth/`), but useful if you want to re-derive against different consensus rules or additional models.
- `ground_truth/case_N.json` — six frozen consensus datasets, one per eval case. Each JSON contains the consensus applicable-BP list and per-model per-run citation frequencies.
- `review_quality.py` — evaluation-only blind and adversarial review of captured reports. It measures evidence, status, severity, recommendation, and uncertainty quality without changing the skill.

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

### Measuring the sequential variant (`SKILL-sequential.md`, #106)

`SKILL-sequential.md` is the Task-free variant for runtimes without parallel
subagent dispatch. To measure it, install the sequential file as the active
skill and run the harness with `--variant sequential` (which drops `Task` from
the allowed tools and swaps in the sequential preamble, so the model cannot fall
back to subagent dispatch):

```bash
# 1. Install the sequential SKILL as the active wa-review skill
./install.sh --global                     # installs SKILL.md (parallel) first
cp skills/wa-review/SKILL-sequential.md ~/.claude/skills/wa-review/SKILL.md

# 2. Measure with Task disabled (18 invocations: 6 cases × 3 runs)
cd evals
uv run python cli_effectiveness/measure_wa_review.py \
  --variant sequential \
  --output cli_effectiveness/wa_review_sequential.json

# 3. Restore the parallel skill afterwards
cp skills/wa-review/SKILL.md ~/.claude/skills/wa-review/SKILL.md
```

Expected: F1 close to the ~0.96 of the parallel runtimes, with higher wall-clock
(~30–40 min total vs ~11 min) and no `Task` usage. Compare
`wa_review_sequential.json` against `wa_review_effectiveness.json` (parallel).
Smoke-test a single case first with `--cases 1 --runs 1`.

## Blind and adversarial quality review

Citation F1 measures coverage, not whether findings are supported or correctly
calibrated. The quality harness adds two independent, anonymous pillar reviewers
and a third-family adversarial adjudicator. Reviewers receive the workload,
candidate ledger, and public WA reference, but not the candidate model, runtime,
skill/baseline condition, cost, or existing scores.

Generate fresh effectiveness output first; current harnesses retain the full
assembled report in their gitignored result JSON. Then run the two-case pilot:

```bash
cd evals
uv run python cli_effectiveness/measure_wa_review.py
uv run python cli_effectiveness/review_quality.py --pilot
```

The pilot selects one successful run each for cases 2 and 3. To review selected
cases or more runs:

```bash
uv run python cli_effectiveness/review_quality.py --cases 1 2 3 --runs 2
```

Generate a fresh single-case candidate without launching the default 18 calls:

```bash
uv run python cli_effectiveness/measure_wa_review.py \
  --cases 2 --runs 1 --model opus \
  --output cli_effectiveness/review_artifacts/e2e-v221/candidate_results.json
```

Then run its blind and adversarial review with isolated raw artifacts:

```bash
uv run python cli_effectiveness/review_quality.py \
  --results cli_effectiveness/review_artifacts/e2e-v221/candidate_results.json \
  --cases 2 --runs 1 \
  --output cli_effectiveness/review_artifacts/e2e-v221-schema-v3/quality_results.json \
  --artifacts-dir cli_effectiveness/review_artifacts/e2e-v221-schema-v3/responses \
  --chunk-size 5 --concurrency 2 --retries 1
```

The output, `cli_effectiveness/review_quality_results.json`, reports status and
severity agreement, weighted kappa, evidence availability, assertion precision,
uncertainty recall, over-conservatism, Critical/High precision, recommendation
quality, adversarial overturns, tokens, cost, and latency. Candidate reports
remain in the gitignored effectiveness JSON; raw reviewer responses remain
under the gitignored `cli_effectiveness/review_artifacts/` directory. An
incomplete model response is recorded as incomplete and is never averaged into
a quality score.

Schema v3 parses candidate status and severity directly from the captured
ledger. Reviewers cannot override those fields. Every independent conclusion
must include a provenance kind and, for determinate or inconclusive conclusions,
an evidence ID from a deterministic catalog of exact workload spans. The
harness resolves that ID to the source quote, avoiding model paraphrases while
preserving exact provenance. Omitted details require `Cannot Determine`;
`authoritative_absence` is rejected for these verbal-only eval cases. The
adversary can select only a complete status/evidence tuple supplied by one of
the blind reviewers and receives no ground-truth status ledger.

Uncertainty is reported as both a rate and explicit counts
(`uncertainty_aligned_count / uncertainty_items`). The harness separately
reports over-conservatism, determinate and negative assertion precision,
legitimate unknowns, and evidence availability. These rates use global
numerators and denominators rather than unweighted averages of pillar rates.

Reviewer and adversary calls are scoped to 20 BPs by default. Valid rows are
retained and only unresolved rows are retried once; full-pillar completeness is
still required before metrics are included. Adjust with `--chunk-size` and
`--retries` when testing model-specific output limits.

If a model throttles or a chunk remains malformed, rerun against the same output
with a smaller chunk and `--resume`. Completed rows and their cost metadata are
reused:

```bash
uv run python cli_effectiveness/review_quality.py \
  --results cli_effectiveness/review_artifacts/e2e-v221/candidate_results.json \
  --cases 2 --runs 1 \
  --output cli_effectiveness/review_artifacts/e2e-v221-schema-v3/quality_results.json \
  --artifacts-dir cli_effectiveness/review_artifacts/e2e-v221-schema-v3/responses \
  --chunk-size 5 --concurrency 2 --resume
```

Resume files must use the current quality-output schema version. When evaluator
invariants change, start a fresh quality output rather than reusing older rows.

By default the panel uses OpenAI and Amazon models as blind reviewers and a
DeepSeek model as adversary. Candidate-family self-grading and same-family
reviewer panels are rejected. Override model IDs with `--reviewers` and
`--adversary` when evaluating a different candidate family.

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

For each of the 6 eval cases, we ran a workload-only consensus panel:

- **2 top-tier models**: Claude Sonnet 5 and OpenAI GPT OSS 120B, both via Amazon Bedrock
- **5 independent runs per model** with subagent-per-pillar dispatch (`call_model_subagent` from `evals/benchmark.py`) — 60 runs total per case
- **Consensus rule**: a BP is "applicable" only if cited by **both models** in **≥3 of their 5 runs**

This yields 270–306 applicable BPs per case out of the 307-BP canonical corpus — a defensible set of "what a strong review should catch" that neither model alone could have hallucinated into existence.

Newly generated ground truth also includes a structured reference ledger with
consensus applicability, expected status, acceptable severity, evidence basis,
confidence, and model votes. Raw panel responses are written only to the
gitignored review-artifact directory; tracked ground truth contains derived
consensus.

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
- **Model review is not human adjudication.** Blind and adversarial scores expose disagreement and unsupported claims, but shared model bias remains possible. Preserve unresolved outcomes instead of treating the panel as an oracle.
- **Opus tier is expensive.** ~$7 per with-skill run × 18 runs = ~$125 to reproduce the full effectiveness measurement. The baseline is ~$2 total.
