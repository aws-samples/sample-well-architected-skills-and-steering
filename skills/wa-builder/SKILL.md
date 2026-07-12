---
name: wa-builder
description: "Learn then Build" — help developers understand AWS Well-Architected best practices for their specific workload, then produce actionable visual artifacts (architecture diagrams with WA annotations, decision trees, improvement roadmaps) they can commit and use. Adapts explanations for beginners and generates artifacts faster for experienced builders. Use when the user wants to understand WA for their project, create architecture diagrams with pillar health overlays, get guided decision flows for architectural choices, or generate a visual improvement roadmap.
not_for: assessments or reviews that produce findings (use wa-review), migration planning (use migration-readiness), generating guardrails (use wa-guardrails), facilitating a WAFR (use wafr-facilitator)
version: 1.0.0
---

# Well-Architected Builder

## Overview

This skill helps developers **understand** Well-Architected for their specific workload and **produce visual artifacts** they can commit. Unlike wa-review (which assesses and scores), wa-builder teaches and enables.

**What you'll produce:**
1. Architecture diagram with WA annotations (color-coded pillar health, risk hotspots)
2. Decision trees for architectural choices (contextual trade-off flowcharts)
3. Improvement roadmap (Gantt timeline + dependency graph)

### Knowledge base

This skill uses the AWS Well-Architected Framework (6 pillars, 57 questions) as its knowledge base. It does NOT require external framework files — all guidance is derived from the WA Framework questions and design principles embedded in this skill's instructions.

## Step 1: Context and Calibration

Ask the user:

> I can help you understand Well-Architected for your project and produce visual artifacts. Let me know:
> - **Workload name** and brief description (or point me at your code)
> - **Your WA familiarity**: New to WA / Familiar / Practitioner
> - **What you want**: Architecture diagram, decision tree, roadmap, or all three
> - **Existing review** (optional): If you have a wa-review output, share it for richer artifacts

If context is already provided or you're in a codebase, proceed directly.

### Experience detection

If the user doesn't explicitly state familiarity, detect from language:
- Uses "pillar", "HRI", "RTO/RPO", "blast radius" naturally → **Practitioner**
- Asks "what is WA" or "how does this apply" → **Beginner**
- Default → **Familiar**

### Adaptive behavior

| Phase | Beginner | Familiar | Practitioner |
|-------|----------|----------|--------------|
| Learning | Full pillar explanations with analogies | Concise pillar relevance | Skip → artifacts |
| Discovery | Guided questions with examples | Direct questions | Accept shorthand |
| Artifacts | Explain each annotation | Brief legend | Raw artifacts only |
| Decision trees | Include "what does this mean?" nodes | Standard decision flow | Compact trade-off matrix |

## Step 2: Workload Discovery

### Path A — Standalone (no prior review)

Perform a lightweight discovery:
1. Scan IaC files for resource types and configurations
2. Identify primary compute pattern (serverless, containers, VMs, mixed)
3. Identify data stores and persistence patterns
4. Identify network topology and external integrations
5. Identify deployment and operations patterns

Produce a **workload profile**:
- Architecture pattern (microservices, monolith, event-driven, etc.)
- AWS services in use
- Per-pillar health signals (3-5 strongest indicators per pillar)
- Top 3 risk hotspots

### Path B — Post-review (consumes wa-review output)

Parse the wa-review report to extract:
- Pillar scores (1-5) from the scorecard
- Findings by severity (Critical, High, Medium, Low)
- Evidence locations (file:line)
- Remediation plan items
- Architecture diagram (if PlantUML was generated)

Use this directly — skip lightweight discovery.

---STOP---
**Checkpoint**: Workload discovery complete — ready to generate learning content and artifacts

> Identified architecture pattern ({pattern}), AWS services in use ({services}), per-pillar health signals, and top risk hotspots for {workload name}. User experience level: {Beginner / Familiar / Practitioner}.
>
> **Shall I proceed with generating the WA learning content and visual artifacts (architecture diagram, decision trees, roadmap)?**

Do NOT proceed past this point until the user explicitly confirms.
---

## Step 3: Learning Phase

**Skip entirely for Practitioners.** For Beginners and Familiar, personalize WA to their workload.

For each pillar relevant to the workload (prioritize by gap severity):

### Beginner format:

```markdown
## {Pillar} for Your {Workload Type}

### Why it matters for YOU
{1-2 sentences connecting this pillar to their specific architecture.
Reference their actual services/patterns.}

### Your top 3 concepts to understand:
1. **{Concept}** ({Question ID}) — {One-sentence explanation in their context}
   📖 WA Framework: {Question ID}
   
2. **{Concept}** ({Question ID}) — {Explanation}
   📖 WA Framework: {Question ID}

3. **{Concept}** ({Question ID}) — {Explanation}
   📖 WA Framework: {Question ID}

### Analogy
{One analogy that makes the pillar intuitive for a developer}
```

### Familiar format:

```markdown
## {Pillar} — Key Gaps
- {Question ID}: {Brief gap description} ({BP IDs})
- {Question ID}: {Brief gap description} ({BP IDs})
```

### How to select concepts

Based on the workload's architecture pattern and gaps:
1. Identify which WA questions (OPS 1–11, SEC 1–11, REL 1–13, PERF 1–5, COST 1–11, SUS 1–6) are most relevant
2. Cluster related questions into coherent "concept groups" (e.g., SEC 2 + SEC 3 = "identity and permissions")
3. Prioritize by: risk severity first, then relevance to their workload pattern

## Step 4: Artifact Generation

Generate ALL requested artifacts. Each artifact MUST include:
- BP ID references (so the builder can trace back to specific guidance)
- Color-coding or severity indicators
- Context specific to THEIR workload (not generic)

---

### Artifact 1: Architecture Diagram with WA Annotations

Generate a PlantUML diagram (primary) with optional Mermaid alternative.

The diagram MUST show:
- All major components from their architecture
- Color-coded borders: 🟢 green (all key BPs implemented), 🟡 yellow (partial gaps), 🔴 red (critical/high gaps)
- Risk hotspot callouts with specific BP IDs
- Legend explaining the color coding

**PlantUML format:**

```plantuml
@startuml
!define GOOD #28a745
!define WARN #ffc107
!define RISK #dc3545

skinparam component {
  BackgroundColor White
  BorderColor Black
}

' Components colored by pillar health
rectangle "{Service}\n[{Type}]" as {alias} {GOOD|WARN|RISK}

' Risk hotspot annotations
note right of {alias} #RISK
  **Risk Hotspot**
  {BP_ID}: {brief description}
  {BP_ID}: {brief description}
end note

' Legend
legend right
  | Color | Pillar Health |
  | <GOOD> | Key BPs implemented |
  | <WARN> | Partial gaps exist |
  | <RISK> | Critical/High gaps |
endlegend
@enduml
```

**Also provide Mermaid alternative** (for tools that render Mermaid natively):

```mermaid
graph TD
    classDef good stroke:#28a745,stroke-width:3px
    classDef warn stroke:#ffc107,stroke-width:3px
    classDef risk stroke:#dc3545,stroke-width:3px
    
    {Component}[{Label}]:::{good|warn|risk}
```

---

### Artifact 2: Decision Trees

Generate Mermaid flowcharts for architectural decisions relevant to the workload's gaps.

Each decision tree MUST:
- Start with their specific workload context (not generic)
- Branch on criteria that matter for WA (availability target, cost tolerance, team size, compliance)
- End with concrete recommendations citing BP IDs
- Include effort/cost indicators on leaf nodes

**Identify decisions to generate** by looking at:
- Critical/High findings that require architectural choices
- Areas where multiple valid approaches exist (serverless vs containers, single vs multi-region, etc.)
- Trade-offs between pillars (cost vs reliability, performance vs security)

**Format:**

```mermaid
flowchart TD
    START[Your workload: {name}] --> Q1{"{Decision question}"}
    Q1 -->|{condition}| OPTION_A["{Recommendation}\n• {detail}\n• {BP_ID}\nEffort: {est}\nCost: {impact}"]
    Q1 -->|{condition}| Q2{"{Follow-up question}"}
    Q2 -->|{condition}| OPTION_B["{Recommendation}\n• {detail}"]
    
    style OPTION_A fill:#28a745,color:white
    style OPTION_B fill:#ffc107
```

**Generate 2-3 decision trees** based on the most impactful gaps. Common decision domains:
- Compute: serverless vs containers vs VMs
- Data: SQL vs NoSQL, single vs multi-region
- Resilience: multi-AZ vs multi-region, active-active vs warm standby
- Deployment: canary vs blue/green vs rolling
- Security: WAF rules, encryption approaches, identity providers

---

### Artifact 3: Improvement Roadmap

Generate a Mermaid Gantt chart + ASCII dependency graph.

**Gantt chart** — shows timeline with phases:

```mermaid
gantt
    title WA Improvement Roadmap — {Workload Name}
    dateFormat YYYY-MM-DD
    axisFormat %b %d
    
    section Quick Wins (Week 1-2)
    {action}  :crit, {id}, {start}, {duration}
    {action}  :{id}, {start}, {duration}
    
    section Foundation (Week 3-6)
    {action}  :{id}, after {dependency}, {duration}
    
    section Strategic (Month 2-3)
    {action}  :{id}, after {dependency}, {duration}
```

**Dependency graph** — shows what blocks what:

```
IMPROVEMENT DEPENDENCY GRAPH
============================

[{Action A}] ──────────────┐
     │                      │
     ▼                      ▼
[{Action B}] ────► [{Action C}]
                        │
[{Action D}] ──────────┤
     │                  │
     ▼                  ▼
[{Action E}] ────► [{Action F}]

Legend:
  ───► = "must complete before"
  [{text}] = improvement item (colored by severity)
```

**How to determine ordering:**
1. Identify prerequisite relationships between improvements (e.g., Multi-AZ before chaos testing)
2. Group by effort (Quick Wins → Foundation → Strategic)
3. Critical/High severity items first within each phase
4. Consider pillar dependencies (security foundations before advanced detection)

## Step 5: Commit Guidance

After generating artifacts, suggest where to save them:

```markdown
## Ready to commit

Here are your artifacts:
1. `docs/architecture/wa-annotated.puml` — Architecture with pillar health
2. `docs/decisions/{topic}-decision.md` — Decision tree(s) for key choices
3. `docs/roadmap/wa-improvement-roadmap.md` — Gantt + dependency graph

Would you like me to:
- **Refine** any artifact (more detail, different format)?
- **Deep-dive** into a specific decision with more BP context?
- **Generate IaC** for a specific improvement from the roadmap?
- **Create an ADR** for a decision you've made from the tree?
- **Run a full /wa-review** for precise per-BP scoring?
```

## Mode: Architecture Decision Record

When the user asks to "create an ADR", "document a design decision", "evaluate architectural options", or "trade-off analysis", switch to ADR mode. ADRs are grounded in codebase analysis — they document decisions with implementation evidence.

### ADR Step 1: Understand the decision

> What architecture decision do you need to document?
> - **Decision title** (e.g., "Switch from SQS to EventBridge for event routing")
> - **Context** — What problem are you solving?
> - **Options considered** (at least 2) — or ask me to suggest alternatives

### ADR Step 2: Current state discovery

Analyze the codebase to document:
- **Current implementation**: what exists today with file paths and line numbers
- **Affected code**: every file that changes for each option (quantify)
- **Integration points**: interfaces, APIs, contracts each option must satisfy
- **Constraints**: language, framework, patterns that limit options
- **Dependencies**: other services/components depending on current implementation

### ADR Step 3: Evaluate options with evidence

For each option, provide:
- **Files affected** (list specific paths)
- **New dependencies** introduced
- **Migration steps** required
- **Effort** (specific, with basis — not T-shirt sizes)
- **WA pillar impact** table (only non-neutral pillars, with evidence)
- **Operational impact** (monitoring, runbooks, on-call changes)

---STOP---
Present options analysis. Do NOT proceed to recommendation without confirmation.
---

### ADR Step 4: Trade-offs and risks

For the recommended option:
- **What you gain** — with evidence from THIS workload
- **What you give up** — honest assessment
- **What could go wrong** — specific risks + mitigations
- **Reversibility** — how hard to undo, what's the escape hatch

For rejected options:
- Primary rejection reason (one sentence)
- Under what future condition it becomes better (specific trigger)

### ADR Step 5: Produce the ADR

```markdown
# ADR-{number}: {Decision Title}

## Status
{Proposed | Accepted | Deprecated | Superseded by ADR-X}

## Date
{YYYY-MM-DD}

## Context
### Problem Statement
{What problem? Why now?}
### Current State
{File paths and code references}
### Constraints
{Derived from codebase — not assumptions}
### Decision Drivers
{Ordered by priority}

## Decision
{One clear statement.}

## Options Evaluated
### Option 1: {name} ← Chosen
- **Pros/Cons/Files affected/Migration/Effort**
### Option 2: {name} — Rejected
- **Pros/Cons/Would choose this if**: {trigger}

## Well-Architected Impact
| Pillar | Impact | Evidence |
{Only non-neutral pillars}

## Trade-offs
### What We Gain / What We Accept / Risks

## Implementation
### Migration Path
### Rollback Plan
### Verification

## Review Triggers
{Specific, measurable: metric > threshold, event occurs, time passes}
```

### ADR Calibration
- An ADR is a decision log, not a sales pitch — document REAL trade-offs
- Code evidence grounds the decision ("affects 3 files" > "low effort")
- Review triggers with specific thresholds make ADRs useful 6 months later
- Reversibility is critical — irreversible decisions deserve more analysis
- Don't pad the WA pillar table — only real, non-obvious impact

---

## Calibration Guidance

- This skill is about ENABLEMENT not JUDGMENT — tone should be encouraging, not critical
- For beginners: use analogies, avoid jargon, explain why before what
- For practitioners: be concise, skip explanations, produce artifacts fast
- Decision trees should present OPTIONS not mandates — the builder decides
- Roadmap should be REALISTIC — don't pack 50 items into "Quick Wins"
- Always tie back to WA Framework question IDs (OPS 4, SEC 3, REL 9, etc.) so builders can look up details
- When generating artifacts from a wa-review, USE the review's findings — don't re-assess
- PlantUML is primary (most tools support it), Mermaid is the alternative (renders in GitHub/VS Code)
- ASCII fallbacks for dependency graphs work everywhere including terminals

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
