"Learn then Build" — help the user understand AWS Well-Architected best practices for their specific workload, then produce actionable visual artifacts (architecture diagrams with WA annotations, decision trees, improvement roadmaps) they can commit and use.

Unlike `/wa-review` (which assesses and scores), wa-builder teaches and enables. Adapt explanations for beginners and generate artifacts faster for experienced builders.

## Step 1: Context and calibration

Ask the user:

> I can help you understand Well-Architected for your project and produce visual artifacts. Let me know:
> - **Workload name** and brief description (or point me at your code)
> - **Your WA familiarity**: New to WA / Familiar / Practitioner
> - **What you want**: Architecture diagram, decision tree, roadmap, or all three
> - **Existing review** (optional): If you have a `/wa-review` output, share it for richer artifacts

If context is already provided or you are in a codebase, proceed directly.

**Detect experience** if not stated:
- Uses "pillar", "HRI", "RTO/RPO", "blast radius" naturally → **Practitioner** (skip learning, go straight to artifacts)
- Asks "what is WA" or "how does this apply" → **Beginner** (full explanations with analogies)
- Default → **Familiar** (concise pillar relevance)

## Step 2: Workload discovery

**Path A — Standalone (no prior review):** lightweight discovery — scan IaC for resource types, identify compute pattern (serverless/containers/VMs/mixed), data stores, network topology, deployment patterns. Produce a workload profile: architecture pattern, AWS services in use, per-pillar health signals, top 3 risk hotspots.

**Path B — Post-review (consumes a `/wa-review` output):** parse the report for pillar scores, findings by severity, evidence locations, remediation items, and any PlantUML diagram. Use directly — skip discovery, do NOT re-assess.

## Step 3: Learning phase

**Skip entirely for Practitioners.** For Beginners and Familiar, personalize WA to their workload, prioritized by gap severity.

- **Beginner**: for each relevant pillar, explain "Why it matters for YOU" (reference their actual services), top 3 concepts with WA Question IDs, and one developer-friendly analogy.
- **Familiar**: terse per-pillar key-gap list with Question/BP IDs.

Select concepts by mapping the workload's gaps to WA questions (OPS 1–11, SEC 1–11, REL 1–13, PERF 1–5, COST 1–11, SUS 1–6), clustering related questions, and ordering by risk severity then relevance.

## Step 4: Artifact generation

Generate ALL requested artifacts. Each MUST include BP ID references, color/severity indicators, and context specific to THEIR workload (never generic).

**Artifact 1 — Architecture diagram with WA annotations:** PlantUML (primary) + Mermaid alternative. Color-coded component borders — 🟢 key BPs implemented, 🟡 partial gaps, 🔴 critical/high gaps — plus risk-hotspot callouts citing BP IDs and a legend.

**Artifact 2 — Decision trees:** 2–3 Mermaid flowcharts for the most impactful architectural choices (e.g. serverless vs containers, single vs multi-region, canary vs blue/green). Start from their workload context, branch on WA-relevant criteria (availability target, cost tolerance, compliance), end with recommendations citing BP IDs and effort/cost indicators. Present OPTIONS, not mandates.

**Artifact 3 — Improvement roadmap:** Mermaid Gantt chart (Quick Wins → Foundation → Strategic) plus an ASCII dependency graph showing what blocks what. Order by prerequisite relationships, then effort phase, then severity. Keep it REALISTIC — do not pack everything into "Quick Wins".

## Step 5: Commit guidance

Suggest where to save the artifacts, e.g.:
- `docs/architecture/wa-annotated.puml` — architecture with pillar health
- `docs/decisions/{topic}-decision.md` — decision tree(s)
- `docs/roadmap/wa-improvement-roadmap.md` — Gantt + dependency graph

Then offer to refine an artifact, deep-dive a decision, generate IaC for a roadmap item, create an ADR (`/architecture-decision-record`), or run a full `/wa-review` for precise per-BP scoring.

## Calibration

- This skill is about ENABLEMENT, not JUDGMENT — tone is encouraging, not critical
- Beginners: analogies, avoid jargon, explain why before what. Practitioners: concise, artifacts fast
- Decision trees present options; the builder decides
- Always tie back to WA Framework Question IDs (OPS 4, SEC 3, REL 9, etc.) so builders can look up details
- When generating from a `/wa-review`, USE its findings — don't re-assess
- PlantUML is primary (broadest support); Mermaid is the alternative (renders in GitHub/VS Code); ASCII fallbacks work everywhere
