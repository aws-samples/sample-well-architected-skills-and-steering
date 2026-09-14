# CLI Effectiveness — measure skills in a real Task-capable runtime

The `evals/run.py` framework (one directory up) uses raw Amazon Bedrock Converse API. Converse has **no `Task` tool**, so it can't execute skills whose value depends on subagent dispatch. `aws-well-architected-framework-review` is exactly that kind of skill — since v4.2 it dispatches 6 parallel pillar subagents, and its full-review path can only be measured in a runtime that supports the `Task` tool.

This directory ships the real-measurement harness we used to validate `aws-well-architected-framework-review` end-to-end. It invokes **Claude Code CLI** (`claude -p`) as the runtime and scores output against a **frozen ground truth of applicable Best Practices** derived from a 2-model × 5-run consensus panel.

> **This directory publishes no results.** It publishes the harness. Any number this harness produces is specific to the workload prompts, the model tier, the ground truth panel, and the moment it ran — which is exactly why the figures are not useful to you second-hand. **Run the harness against your own workloads, model tiers, and requirements** before making a data-driven decision. The scripts and the ground truth are here so you can. Your results are written to gitignored files and stay local; see [CONTRIBUTING.md](../../CONTRIBUTING.md#measurement-results-stay-local).

## What you get

- `measure_wa_review.py` — invokes `claude -p` with the aws-well-architected-framework-review skill installed and scores against ground truth
- `measure_baseline.py` — paired baseline: `claude -p --safe-mode --disable-slash-commands` from a scratch workdir (no skill, no CLAUDE.md, no plugins). Same prompts, same ground truth. The delta between the two is the honest measure of what the skill adds.
- `generate_ground_truth.py` — regenerates the ground truth. Not needed for the shipped data (already in `ground_truth/`), but useful if you want to re-derive against different consensus rules or additional models. It writes the consensus set to `ground_truth/case_N.json` and the full panel record — per-run latency, tokens, per-model citation frequency, reference ledger — to `ground_truth/panel/case_N.json`, which is gitignored. Measurement results stay local; see [CONTRIBUTING.md](../../CONTRIBUTING.md#measurement-results-stay-local).
- `ground_truth/case_N.json` — six frozen consensus sets, one per eval case: the applicable-BP list the scorers compare against, plus the panel protocol (models, runs per model, canonical corpus size) needed to interpret it.
- `review_quality.py` — evaluation-only blind and adversarial review of captured reports. It measures evidence, status, severity, recommendation, and uncertainty quality without changing the skill.

## When to use this vs `evals/run.py`

| You have… | Use |
| --------- | --- |
| A skill that depends on `Task` subagents, MCP tools, or other runtime affordances | `cli_effectiveness/` (this directory) |
| A skill whose value is captured by a well-crafted `SKILL.md` alone (no runtime tool calls) | `evals/run.py` — the LLM-as-judge framework is cheaper and faster |

`evals/run.py` remains the appropriate framework for `wa-builder`, `wa-guardrails`, `wafr-facilitator`, and `migration-readiness` — none of those depend on Task subagents. For `aws-well-architected-framework-review`, only the CLI effectiveness harness produces honest numbers.

## Running the full-review measurement

**Prerequisites:**

- Claude Code CLI installed (`claude --version`)
- AWS credentials with Bedrock access enabled for Anthropic and OpenAI GPT OSS 120B in `us-east-1`
- The `aws-well-architected-framework-review` skill installed globally (`./install.sh --global` from the repo root)
- Python 3.13+ and [uv](https://docs.astral.sh/uv/) for the Bedrock-based ground truth generator (only if regenerating; not needed to score against the shipped ground truth)

**Run both configurations:**

```bash
cd evals

# With skill — measures aws-well-architected-framework-review end-to-end in Claude Code CLI
uv run python cli_effectiveness/measure_wa_review.py

# Without skill — paired baseline (no aws-well-architected-framework-review, no plugins)
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
# 1. Install the sequential SKILL as the active aws-well-architected-framework-review skill
./install.sh --global                     # installs SKILL.md (parallel) first
cp skills/aws-well-architected-framework-review/SKILL-sequential.md ~/.claude/skills/aws-well-architected-framework-review/SKILL.md

# 2. Measure with Task disabled (18 invocations: 6 cases × 3 runs)
cd evals
uv run python cli_effectiveness/measure_wa_review.py \
  --variant sequential \
  --output cli_effectiveness/wa_review_sequential.json

# 3. Restore the parallel skill afterwards
cp skills/aws-well-architected-framework-review/SKILL.md ~/.claude/skills/aws-well-architected-framework-review/SKILL.md
```

The sequential path trades wall-clock for runtime independence: it visits the six
pillars one after another instead of dispatching them concurrently, and makes no
`Task` calls. Compare `wa_review_sequential.json` against
`wa_review_effectiveness.json` (parallel) to see what that costs you on your
models. Smoke-test a single case first with `--cases 1 --runs 1`.

> **Slow runtimes:** the per-invocation `claude` timeout defaults to 900s. A full
> review on a slower model can exceed it, and the sequential path is slower than
> the parallel one — a killed run looks like a harness failure, not a slow model.
> Raise the cap with `--timeout` (e.g. `--timeout 2400`) so legitimate runs
> aren't cut off mid-flight.

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

**Reading your own results.** Each configuration writes a gitignored JSON next to
the harness: per-case report F1, recall, precision, cost, and wall-clock, plus the
means across cases. The number that means something is the *delta* between the
with-skill file and the baseline file on your models and your workloads — a single
absolute score has no reference point. Run both arms before drawing a conclusion,
and keep the files local.

If the with-skill arm scores near or below the baseline arm, check these before
concluding the skill doesn't help:

1. **Older aws-well-architected-framework-review version** — the Full BP Ledger, added in v2.2, is what closes the compression gap. Check `~/.claude/skills/aws-well-architected-framework-review/SKILL.md` for `version: 2.2.0` or later.
2. **Model tier** — tiers differ substantially on this task. Score both arms on the *same* tier, or the delta measures the tier, not the skill.
3. **Skill install location** — Claude Code reads `~/.claude/skills/`. If the skill lives elsewhere (e.g. project-local `.claude/`) the harness may not find it, and the with-skill arm silently becomes a second baseline.

## Ground truth methodology

For each of the 6 eval cases, we ran a workload-only consensus panel:

- **2 models from different provider families**: Claude Sonnet 5 and OpenAI GPT OSS 120B, both via Amazon Bedrock
- **5 independent runs per model** with subagent-per-pillar dispatch (`call_model_subagent` from `evals/benchmark.py`) — 60 runs total per case
- **Consensus rule**: a BP is "applicable" only if cited by **both models** in **≥3 of their 5 runs**

What survives that rule is a defensible set of "what a strong review should catch"
that neither model alone could have hallucinated into existence. Read the size of
each shipped set out of `ground_truth/case_N.json` (`consensus_bp_count`); the
canonical corpus it is drawn from is the 307 BPs in
`skills/aws-well-architected-framework-review/references/pillars/`.

The generator also builds a structured reference ledger — consensus applicability,
expected status, acceptable severity, evidence basis, confidence, and model votes.
That ledger, the per-model citation frequencies, and the raw panel responses are
all measurements of the panel, so they are written only to gitignored paths
(`ground_truth/panel/` and the review-artifact directory). The tracked fixture
carries the consensus set the scorers read and nothing else.

The panel is two models rather than three because a third candidate was throttled
so heavily under this concurrency pattern that it produced no usable runs. Two
independent models from different families are enough for the consensus rule — the
point is that neither one alone can put a BP into the ground truth. Swap in the
models you want to panel with and re-derive.

To regenerate:

```bash
cd evals
uv run python cli_effectiveness/generate_ground_truth.py
```

This makes `2 models × 5 runs × 6 cases` structured-ledger calls over the full
canonical corpus, so it is the most expensive thing in this directory — budget for
it against your own provider's pricing. Not needed unless you're deliberately
re-deriving the ground truth (updated framework, different consensus rule, or new
panel models).

## Scoring details

- **Case 4** is a pillar-scoped test ("Review only Security and Reliability"). It's scored against the SEC + REL subset of its ground truth so pillar-scoped mode is measured fairly — the skill correctly runs only 2 subagents on Case 4 and should not be penalized for the 4 pillars it was told not to review.
- **Precision denominator** is BPs cited by the review that appear in the canonical corpus (drops hallucinations at the extraction layer).
- **Recall denominator** is the case's ground truth — its full consensus set, or the SEC + REL subset for Case 4.
- **BP citation extraction** normalizes Unicode hyphens — models frequently emit `SEC03‑BP02` (non-breaking hyphen U+2011) or `SEC03‐BP02` (hyphen U+2010) instead of ASCII `SEC03-BP02`. The extractor accepts all common variants.

## Limitations

- **Six cases is a small sample.** Repeat runs on the same case measure within-configuration variance; whether a result generalizes to a *different* workload is a separate question this harness does not answer. Add your own cases before you trust it for yours.
- **Consensus ground truth is not oracle truth.** Two models agreeing on a BP doesn't guarantee it's actually applicable; it means two strong models thought so. The cases differ in how cleanly the panel agreed — borderline BPs sit just either side of the ≥3/5 threshold, and they are the ones to look at when a score surprises you.
- **F1 is not the whole story.** A review can maximize F1 by enumerating every BP and still be useless — the *severity* assignment and *recommendation* content matter too. This harness measures citation coverage only.
- **Model review is not human adjudication.** Blind and adversarial scores expose disagreement and unsupported claims, but shared model bias remains possible. Preserve unresolved outcomes instead of treating the panel as an oracle.
- **The with-skill arm is the expensive one.** A full review loads all six pillar files and writes a long report; the baseline arm does neither. Price both arms on your own provider's rates before launching the default 18 invocations, and smoke-test with `--cases 1 --runs 1` first.
