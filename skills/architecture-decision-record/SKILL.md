---
name: architecture-decision-record
description: Generate a Well-Architected-aligned Architecture Decision Record (ADR) that documents a design decision with context, options evaluated, trade-offs, and WA pillar impact.
version: 1.1.0
---

# Architecture Decision Record

## Step 1: Understand the decision

Ask the user:

> What architecture decision do you need to document? Please share:
> - **Decision title** (e.g., "Use Aurora Serverless v2 for the orders database")
> - **Context** — What problem are you solving? What constraints exist?
> - **Options considered** (at least 2) — or ask me to suggest alternatives

If the user has already described the decision, proceed directly.

## Step 2: Evaluate options against WA pillars

For each option, assess impact on all six pillars:

| Pillar | Option A | Option B | Option C |
|--------|----------|----------|----------|
| Operational Excellence | | | |
| Security | | | |
| Reliability | | | |
| Performance Efficiency | | | |
| Cost Optimization | | | |
| Sustainability | | | |

Use: ✅ Positive | ➖ Neutral | ⚠️ Trade-off | ❌ Negative

## Step 3: Identify trade-offs

For the recommended option, explicitly state:
- What you gain
- What you give up
- Under what conditions the decision should be revisited

## Step 4: Produce the ADR

Output using the standard ADR format:

```markdown
# ADR-{number}: {Decision Title}

## Status
{Proposed | Accepted | Deprecated | Superseded by ADR-X}

## Date
{YYYY-MM-DD}

## Context
{What is the problem? What forces are at play? What constraints exist?}

## Decision
{What is the change that we're proposing and/or doing?}

## Options Considered

### Option 1: {name}
- **Description**: {how it works}
- **Pros**: {benefits}
- **Cons**: {drawbacks}
- **WA Impact**: {pillar impacts}

### Option 2: {name}
- **Description**: {how it works}
- **Pros**: {benefits}
- **Cons**: {drawbacks}
- **WA Impact**: {pillar impacts}

{Additional options as needed}

## Well-Architected Impact

| Pillar | Impact | Notes |
|--------|--------|-------|
| Operational Excellence | {+/-/neutral} | {why} |
| Security | {+/-/neutral} | {why} |
| Reliability | {+/-/neutral} | {why} |
| Performance Efficiency | {+/-/neutral} | {why} |
| Cost Optimization | {+/-/neutral} | {why} |
| Sustainability | {+/-/neutral} | {why} |

## Trade-offs
{What are we explicitly accepting as a trade-off?}

## Consequences
{What becomes easier or harder because of this decision?}

## Implementation Notes
- **Effort**: {Low / Medium / High}
- **Timeline**: {estimated}
- **AWS Services**: {key services involved}
- **Reversibility**: {Easy / Hard / Irreversible}

## Review Triggers
{Under what conditions should this decision be revisited?}
- {trigger 1}
- {trigger 2}
```

## Step 5: Offer next steps

After producing the ADR, offer:

> Would you like me to:
> - Add more options to evaluate?
> - Deep-dive into a specific pillar's impact?
> - Create an implementation plan for the chosen option?
> - Generate IaC for the decision?
> - Draft a follow-up ADR for a related decision?
