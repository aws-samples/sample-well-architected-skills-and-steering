Create or revise Architecture Decision Records by analyzing the codebase to understand current state, affected code paths, constraints from existing patterns, and trade-offs grounded in implementation reality.

## Step 1: Understand the decision

Ask the user:

> What architecture decision do you need to document? Please share:
> - **Decision title** (e.g., "Switch from SQS to EventBridge for event routing")
> - **Context** — What problem are you solving or what change are you making?
> - **Options considered** (at least 2) — or ask me to suggest alternatives

If the user has already described the decision, proceed directly.

**IMPORTANT**: When in a codebase, ALWAYS analyze the code first. When no code is available, proceed with the verbal description but mark implementation sections as "Verify against code."

## Step 2: Current State Discovery

Analyze the codebase to understand what exists today.

You MUST examine:
- IaC relevant to the decision (CDK, CloudFormation, Terraform)
- Application code affected by the decision
- Configuration files, dependencies, environment variables
- Existing patterns and conventions
- Tests that validate current behavior

Document:
- **Current implementation**: file paths and line numbers
- **Affected code**: every file that would change for each option (quantify: "Option A: 3 files, Option B: 12")
- **Integration points**: interfaces each option must satisfy
- **Constraints from existing code**: language, framework, patterns
- **Dependencies**: other services/components depending on current implementation

Flag:
- Data migration requirements if stateful resources change
- Compatibility constraints from existing dependencies
- Established patterns the decision should follow or explicitly break from

## Step 3: Evaluate options with evidence

For each option, provide concrete analysis:

**Implementation effort** — specifics, not T-shirt sizes:
- Files that change (list them)
- New dependencies introduced
- Migration steps required
- Time estimate delta between options (e.g., "Option A ~2 weeks, Option B ~6 weeks")

**WA pillar impact** — only relevant pillars, skip neutral ones:

| Pillar | Option A | Option B |
|--------|----------|----------|
| {relevant pillar} | {impact + evidence from code} | {impact + why} |

**Operational impact**: monitoring changes, runbook updates, deployment changes.

## Step 4: Trade-offs and risks

For recommended option:
- **What you gain** — evidence of why it matters for THIS workload
- **What you give up** — honest assessment
- **What could go wrong** — specific risks with mitigations
- **Reversibility** — how hard to undo? escape hatch? one-way data changes?

For rejected options:
- Primary rejection reason (one sentence)
- Future conditions where it becomes the better choice

## Step 5: Produce the ADR

Structure:

```markdown
# ADR-{number}: {Decision Title}

## Status
{Proposed | Accepted | Deprecated | Superseded}

## Date

## Context
### Problem Statement
### Current State
{File paths and code references}
### Constraints
{From codebase — with evidence}
### Decision Drivers
{Ordered by priority}

## Decision
{One clear statement}

## Options Evaluated
### Option 1: {name} ← Chosen
- How it works, pros, cons, files affected, migration steps, effort estimate
### Option 2: {name} — Rejected
- How it works, pros, primary rejection reason, would choose if {condition}

## Well-Architected Impact
{Table — only non-neutral pillars}

## Trade-offs
### What We Gain
### What We Accept
### Risks
{Table: risk, likelihood, impact, mitigation}

## Implementation
### Migration Path
{Numbered steps with affected files}
### Rollback Plan
{Specific steps to undo}
### Verification
{How to confirm it worked — metrics, tests}

## Review Triggers
{Measurable conditions — not vague}
```

## Step 6: Revising an existing ADR

When asked to revise:
- Read the existing ADR
- Analyze what changed since it was written (git log, diffs)
- Determine if review triggers have been hit
- If superseding: create new ADR referencing old one

## Calibration

- ADRs are decision logs, not sales pitches — document REAL trade-offs including uncomfortable ones
- Code evidence grounds the decision — "affects 3 files" beats "low effort"
- Review triggers with thresholds make ADRs useful 6 months later
- Migration path is the most actionable section — make it followable
- Reversibility is critical — irreversible decisions deserve more analysis
- Don't pad the WA pillar table — skip genuinely neutral pillars
