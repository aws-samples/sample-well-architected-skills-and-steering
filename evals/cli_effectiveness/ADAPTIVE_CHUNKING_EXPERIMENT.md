<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->

# Experiment Spec: Adaptive Chunk Sizing for the WA-Review Subagent Dispatch

**Status:** Proposed (not yet implemented)
**Surface:** `evals/cli_effectiveness/`
**Motivated by:** Yang et al., *Act More, Decide Less: Skill-Guided Adaptive
Action Chunking for Long-Horizon LLM Agents* (SPACE), EMNLP 2026,
[arXiv:2609.02042](https://arxiv.org/abs/2609.02042).

---

## 1. Background and what transfers from SPACE

SPACE studies **variable-length action chunking**: instead of one action per LLM
round (ReAct), the policy emits chunks of several primitive actions, amortizing
LLM decisions across routine sequences. Its headline results — +7.0–31.3%
success and up to **−78.9% LLM decision rounds** — come from an **RL training**
pipeline (skill induction → skill-to-chunk expansion → chunk-aware GiGPO with
on-policy + off-policy distillation). **None of that training pipeline transfers
here**: this repo runs *frozen* foundation models via the Claude Code CLI /
Bedrock and cannot fine-tune.

Two findings *do* transfer as design signal, without any training:

1. **Chunking beats per-step decisions for long-horizon work.** This
   independently validates the repo's existing design — the
   `aws-well-architected-framework-review` full review pre-loads a whole pillar
   file per subagent and evaluates 30–55 BPs "in one chunk", instead of
   retrieving one BP per LLM round (the README's anti-per-BP-MCP-retrieval
   argument and the observed 20–60/307 plateau).
2. **Chunk granularity has a sweet spot.** SPACE's Figure 3 shows the failure
   modes of *badly sized* chunks: collapse to 1 action/round (Qwen3-4B) or
   over-commit to 5–6 actions/round with **lower** success (Llama-3.1-8B). The
   best policy sat at a **balanced ~3–4 actions/round**. Mapped to our review:
   the current split is a **fixed 6 chunks = 6 pillars**, but pillars are wildly
   uneven (Security ≈ 55 BPs vs Sustainability ≈ 27). A fixed split may be the
   analog of "over-committing" on the heavy pillar and "under-using" the light
   one.

**Hypothesis (H1):** Splitting heavy pillars into multiple subagents and merging
light pillars — i.e. balancing BPs-per-chunk — improves recall/F1 and/or reduces
wall-clock on the heavy pillars, at equal or lower total cost, versus the fixed
6-pillar split.

**Null (H0):** Balanced chunking makes no significant difference to F1, and the
fixed 6-pillar split is already on the flat part of the curve.

This is an **A/B on frozen models**, measured with the existing F1-vs-ground-truth
harness. It is explicitly *not* an attempt to reproduce SPACE's RL method.

---

## 2. Arms

All arms run the same skill, same eval cases, same model, same ground truth. Only
the **chunking policy** (how the review partitions the 307-BP corpus across
parallel `Task` subagents) changes.

| Arm | Chunking policy | # subagents |
|-----|-----------------|-------------|
| **A. Fixed-6 (control)** | Current: one subagent per pillar | 6 |
| **B. Balanced-by-count** | Partition BPs into `N` chunks of ~equal BP count (e.g. split SEC into SEC-a/SEC-b, keep pillars as chunk unit otherwise) | tune to ~35–40 BP/chunk (≈8) |
| **C. Depth-weighted** | Size chunks by `practice_depth` load, not raw BP count — pillars with more `guided`/deep BPs get their own subagent, shallow BPs are merged | variable |
| **D. Coarse (over-commit probe)** | Deliberately merge into 3 chunks (2 pillars each) to confirm the SPACE "over-commit → lower success" failure mode appears | 3 |

Arm D is a **falsification probe**: if coarse chunking does *not* degrade F1,
that weakens the whole premise and we stop.

Chunk boundaries must respect pillar identity for citation attribution (a
subagent still reports canonical `PILLAR##-BP##` IDs). Splitting a pillar means
handing subagent *a* the first half of that pillar's BP list and subagent *b*
the second half, each loading only its slice of the pillar reference file.

---

## 3. Metrics

Per (case, arm), over `--runs` runs (default 3), reuse `measure_wa_review.py`
scoring:

- **Primary:** `subagent_total` F1, recall, precision vs `ground_truth/case_N.json`.
- **Efficiency:** `wall_s`, `duration_ms`, `total_cost_usd`, `input`/`output`/
  `cache_read` tokens, `num_turns`.
- **Chunk-behavior diagnostics:** BPs cited per subagent (distribution), and
  per-subagent wall-clock (does the heavy-pillar subagent dominate latency?).

Report mean ± stdev across runs, and run-to-run variance (SPACE emphasizes
stability; a chunking policy that raises variance is worse even at equal mean).

---

## 4. Decision criteria

Adopt a new chunking policy only if, versus Fixed-6 control across the 6 eval
cases:

- **F1 non-inferior** (mean F1 delta ≥ −0.01, i.e. no meaningful regression), **and**
- at least one of:
  - **F1 improvement** ≥ +0.02 mean (paired, across cases), or
  - **wall-clock reduction** ≥ 20% on the critical-path (slowest) subagent at
    equal F1 and equal-or-lower cost.
- **Variance not worse:** run-to-run F1 stdev does not increase.

Use a paired comparison across cases (same cases both arms). Given only 6 cases,
treat results as directional, not a significance claim — report per-case deltas,
not just the mean. (This mirrors the honesty constraint already used elsewhere
in the harness.)

---

## 5. Harness changes required

1. **Chunk-policy plumbing.** The chunking policy currently lives in `SKILL.md`
   Step 4b ("dispatch 6 parallel pillar subagents"). To A/B it without editing
   the shipped skill, add a preamble override in a new
   `measure_chunking_ab.py` that instructs the review to partition per a supplied
   policy spec (arm B/C/D), analogous to how `AUTONOMOUS_PREAMBLE` already
   overrides the discovery checkpoint.
2. **Per-subagent attribution.** `_parse_session` already reads subagent
   transcripts; extend it to return per-subagent BP sets and per-subagent
   wall-clock (from subagent file mtimes / event timestamps) so we can see the
   chunk-size distribution, not just the merged total.
3. **Policy specs.** Encode arms B/C as a small JSON (`chunk_policies.json`)
   mapping chunk-id → list of pillars/BP-ranges, so arms are reproducible and
   diffable.
4. **Reuse** `build_canonical_bps`, `load_ground_truth`, `score_run`,
   `aggregate` unchanged.

No change to the shipped `SKILL.md`; the experiment overrides dispatch via
preamble only. If an arm wins, *then* propose a `SKILL.md` change in a separate
PR with the A/B evidence attached.

---

## 6. Threats to validity

- **Frozen-model confound.** We are not learning chunk boundaries (SPACE's whole
  contribution); we are hand-specifying them. A negative result means *our
  hand-specified* boundaries did not help — not that learned boundaries wouldn't.
- **Attribution coupling.** Splitting a pillar across two subagents risks
  double-counting or boundary BPs being missed by both. Mitigate with disjoint
  BP-range assignment and a post-hoc check that the union of subagent slices
  equals the pillar's full BP set.
- **Small N.** 6 eval cases → directional only. A win should be confirmed on the
  broader case set before shipping.
- **Cost.** Each arm is a full review (~$7, ~11 min on Opus-tier). Four arms × 6
  cases × 3 runs ≈ 72 full reviews. Budget ~$500 and gate on Arm D first (cheap
  falsification): if coarse chunking doesn't hurt, cancel arms B/C.

---

## 7. Execution order (cost-gated)

1. Run **Arm D** (coarse, 3 chunks) vs **Arm A** (control) on 2 representative
   cases × 3 runs. If D ≈ A (no degradation), **stop** — the premise is refuted.
2. If D degrades, run **Arm B** (balanced-by-count) on all 6 cases × 3 runs.
3. If B wins on the §4 criteria, run **Arm C** (depth-weighted) to see if
   `practice_depth`-aware sizing beats raw count balancing.
4. Report per-case deltas + variance; propose a `SKILL.md` dispatch change only
   with evidence.
