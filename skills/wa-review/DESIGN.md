# wa-review — Design Notes

This document explains **how the `wa-review` skill achieves comprehensive
coverage** and the empirical work that shaped its design. It's aimed at
maintainers and users who want to understand *why* the skill is structured
the way it is.

## The coverage problem

The AWS Well-Architected Framework has **307 canonical Best Practices** across
57 questions in 6 pillars. A "full" review should evaluate every one of them.

However: when a single AI agent tries to enumerate all 307 BPs in one response,
it consistently produces **20-60 findings and stops**. This isn't a prompt
engineering problem — it's a stable equilibrium of the model's concision priors.
We measured this across multiple approaches and it did not budge:

- Loading all 57 per-question reference files → 30-60 BPs cited
- Loading 6 pillar-merged files → 30-60 BPs cited
- Loading a manifest of every BP ID → 30-60 BPs cited
- Using AWS Knowledge MCP retrieval → 30-60 BPs cited
- Adding explicit "you MUST cite 100+ BPs" instructions → 30-60 BPs cited
- Adding a mandatory "coverage audit" checkpoint → 30-60 BPs cited

None of these single-agent strategies reliably reached 200+ BPs.

## The insight that works: narrow-scope subagents

When one agent reviews **only one pillar**, it naturally enumerates all ~30-55
BPs for that pillar. The concision bias doesn't kick in because the scope is
narrower.

Dispatching **6 parallel subagents** — one per pillar — aggregates to **307 BPs
of coverage** in a single review. This is the pattern encoded in the skill's
`Step 4b — Dispatch 6 parallel pillar subagents` section.

### How it works in practice

The skill's default full-review path:

1. **Main agent** reads `references/manifest.md` (~24 KB) — the catalog of all
   307 BPs by pillar.
2. **Main agent** dispatches 6 `Task` subagent invocations, one per pillar.
   Each subagent gets:
   - The workload description + code context
   - A directive to review ONLY its assigned pillar
   - Access to `references/pillars/{pillar-slug}.md` (the merged
     per-pillar reference file, 143-583 KB each)
3. **Each subagent** reads its pillar file, enumerates every BP, and returns
   findings with status: Implemented / Partially Implemented / Not Implemented /
   Not Applicable.
4. **Main agent** aggregates the 6 pillar reports into a single structured
   review with cross-pillar patterns and prioritization.

Subagents run in parallel because pillars are independent. Wall-clock time
is bounded by the slowest single pillar (~2-3 min), not the sum of all 6.

## Empirical validation

We ran a controlled study (n=1 across variants, pilot phase) comparing:

| Approach | Coverage | Latency | Hallucinations |
|----------|----------|---------|----------------|
| Single agent, local files (57 per-question) | 18% (56/307) | 384s | 1 |
| Single agent, local files (6 pillar-merged) | 12% (37/307) | 235s | 0 |
| Single agent, AWS Knowledge MCP retrieval | 9% (29/307) | 215s | 0 |
| Single agent, hybrid (local + MCP) | 12% (37/307) | 235s | 0 |
| **6 parallel subagents (local pillar files)** | **100% (307/307)** | **136s** | **0** |
| **6 parallel subagents (MCP retrieval)** | **99% (304/307)** | **214s** | **3** |

The subagent-per-pillar pattern is the driver — not the file format or
retrieval source. Both local files and MCP retrieval work; local is faster
and cheaper.

### Quality doesn't degrade

Panel-graded quality (3-judge cross-family panel: Sonnet 4.6 + DeepSeek R1 +
GPT OSS 120B) was **5.0/5 across all approaches, including the shorter
single-agent reviews**. The subagent pattern doesn't produce "better" reviews
in an aesthetic sense — it produces **more comprehensive** reviews. The
customer gets every BP evaluated instead of a curated top 30.

## Trade-offs

| Dimension | Single-agent full review | 6-subagent full review |
|-----------|--------------------------|------------------------|
| BP coverage | 20-60 BPs (7-20%) | 300+ BPs (~100%) |
| Wall-clock latency | 3-5 min | 2-4 min (parallel) |
| Output tokens | ~15 K | ~40 K |
| Cost multiplier | 1x | ~3-4x (workload context is duplicated 6x) |
| Reviews per hour | ~12 | ~15 (parallel dispatch is efficient) |
| Hallucinations | 0-1 | 0-3 (mostly cross-referenced BP IDs) |

The 3-4x cost is real. Users who prioritize cost over completeness can invoke
`quick review` mode or `score` mode instead.

## When NOT to use subagents

The skill uses subagents by **default for full reviews**. It does NOT use them for:

- **Quick review mode** — user asked for a summary; single agent, ~30 BPs, cheap.
- **Score mode** — user wants a scorecard, not exhaustive enumeration.
- **Pillar-scoped review** — user asked for only Security or only Reliability;
  a single agent handles it (which is essentially what one subagent does anyway).
- **Cost-constrained environments** — SKILL.md notes that users can override
  and accept lower coverage in exchange for lower cost.

## Reference corpus layout

The corpus is stored in three layers, each serving a purpose:

- `references/manifest.md` (~24 KB) — Lightweight index of all 307 BP IDs and
  titles. Loaded by the main agent to know what universe of BPs exists.
- `references/pillars/{pillar-slug}.md` (6 files, 143-583 KB) — Pillar-merged
  reference files. Each is complete BP content for one pillar. Passed to
  subagents as their reference.
- `references/questions/{QUESTION_ID}.md` (57 files, ~10-40 KB) — Per-question
  reference files. Retained as the canonical source and for pillar-scoped or
  lens-specific work.

The pillar-merged and manifest files are **derived** from the per-question
files via scripts:

- `scripts/generate-manifest.py`
- `scripts/generate-pillar-merged.py`

Both are re-run whenever the per-question corpus changes (via the
`scripts/crawl-wa-framework.py` crawler).

## History and study methodology

The design above is the result of an internal study run in `evals/study_mcp/`
(kept locally, not committed). The study compared 6 variants against the same
architecture-review prompt with panel-graded output. Progressive iterations
narrowed to the finding that **subagent scoping — not retrieval strategy — is
the decisive factor** in citation depth.

Key artifacts (kept locally):
- `evals/STUDY_MCP_VS_BUNDLED.md` — proposal and methodology
- `evals/study_mcp/run.py` — orchestrator that runs each variant and aggregates
- `evals/study_mcp/setup.py` — prepares workspace variants
- `evals/study_mcp/results/*.json` — raw per-variant citation and grading data

If a user or maintainer wants to reproduce or extend the study, the artifacts
are available in the working tree of this branch's development history.
