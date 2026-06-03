---
name: architecture-decision-record
description: Create or revise Architecture Decision Records by analyzing the codebase to understand current state, affected code paths, constraints from existing patterns, and trade-offs grounded in implementation reality.
version: 2.1.0
---

# Architecture Decision Record

## Step 1: Understand the decision

Ask the user:

> What architecture decision do you need to document? Please share:
> - **Decision title** (e.g., "Switch from SQS to EventBridge for event routing")
> - **Context** — What problem are you solving or what change are you making?
> - **Options considered** (at least 2) — or ask me to suggest alternatives

If the user has already described the decision, proceed directly.

**IMPORTANT**: When you are in a codebase, ALWAYS analyze the code first to ground the ADR in implementation reality. When no code is available, proceed with the verbal description but mark implementation sections as "Verify against code."

## Step 2: Current State Discovery

Analyze the codebase to understand what exists today.

You MUST examine:
- Infrastructure-as-code relevant to the decision (CDK, CloudFormation, Terraform)
- Application code that implements or will be affected by the decision
- Configuration files, dependency manifests, environment variables
- Existing patterns and conventions in the codebase
- Tests that validate current behavior

For the decision context, you MUST document:
- **Current implementation**: what exists today with file paths and line numbers
- **Affected code**: every file that would need to change for each option
- **Integration points**: interfaces, APIs, contracts that each option must satisfy
- **Constraints from existing code**: language, framework, patterns that limit options
- **Dependencies**: other services or components that depend on the current implementation

You MUST flag:
- Code that must change for each option (quantify: "Option A touches 3 files, Option B touches 12")
- Compatibility constraints from existing dependencies
- Patterns already established that the decision should follow (or explicitly break from with justification)
- Data migration requirements if the change affects stateful resources

## Step 3: Evaluate options with evidence

For each option, provide a concrete analysis:

**Implementation effort** — not T-shirt sizes, but specifics:
- Files that change (list them)
- New dependencies introduced
- Migration steps required
- Estimated time delta between options (e.g., "Option A is ~2 weeks, Option B is ~6 weeks based on migration complexity")

**WA pillar impact** — only for relevant pillars, with specific reasoning:

| Pillar | Option A | Option B |
|--------|----------|----------|
| {relevant pillar} | {impact + why + evidence from code} | {impact + why} |

Use: ✅ Positive | ➖ Neutral | ⚠️ Trade-off | ❌ Negative

Skip pillars that are genuinely neutral for both options — don't pad the table.

For each non-neutral assessment, you MUST provide:
- Why this option has this impact (grounded in the code's reality)
- Specific AWS service, pattern, or code path that creates the benefit or risk
- Whether it's a temporary trade-off (migration pain) or permanent (architectural constraint)

**Operational impact** — what changes for the team:
- Monitoring/alerting changes needed
- Runbook updates
- On-call implications
- Deployment strategy changes

## Step 4: Identify trade-offs and risks

For the recommended option, you MUST explicitly state:
- **What you gain** — with evidence of why it matters for THIS workload (not generic benefits)
- **What you give up** — with honest assessment of whether it's acceptable given constraints
- **What could go wrong** — specific risks during implementation or after, with mitigations
- **Reversibility** — how hard is it to undo? What's the escape hatch? What data is one-way?

For rejected options, you MUST explain:
- Primary rejection reason (one clear sentence)
- Under what future conditions it becomes the better choice (specific triggers)

## Step 5: Produce the ADR

```markdown
# ADR-{number}: {Decision Title}

## Status
{Proposed | Accepted | Deprecated | Superseded by ADR-X}

## Date
{YYYY-MM-DD}

## Context

### Problem Statement
{What problem? Why now? What triggered this decision?}

### Current State
{What exists today — with file paths and code references}
- `{file:line}` — {what it does and why it's relevant}
- `{file:line}` — {what it does}

### Constraints
{Derived from codebase analysis — not assumptions}
- {constraint} — Evidence: `{file:line}`

### Decision Drivers
{Ordered by priority — what matters most}
1. {driver} — {why, grounded in business or code reality}
2. {driver} — {why}

## Decision
{One clear statement of what we're doing.}

## Options Evaluated

### Option 1: {name} ← Chosen
- **How it works**: {description}
- **Pros**: {benefits grounded in this codebase's reality}
- **Cons**: {drawbacks with honest assessment}
- **Files affected**: {list with paths}
- **Migration**: {what needs to happen to get from current state to this}
- **Effort**: {specific estimate with basis}

### Option 2: {name} — Rejected
- **How it works**: {description}
- **Pros**: {benefits}
- **Cons**: {primary reason for rejection}
- **Files affected**: {list}
- **Effort**: {estimate}
- **Would choose this if**: {specific future condition}

## Well-Architected Impact

| Pillar | Impact | Evidence |
|--------|--------|----------|
| {pillar} | {✅/⚠️/❌} | {specific reasoning tied to code/architecture} |
{Only pillars with non-neutral impact}

## Trade-offs

### What We Gain
- {benefit} — matters because {evidence from this workload}

### What We Accept
- {drawback} — acceptable because {justification}

### Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| {specific risk} | {Low/Med/High} | {what breaks} | {concrete action} |

## Implementation

### Migration Path
1. {step} — affects `{file}`
2. {step} — affects `{file}`
3. {step} — verify with {test/metric}

### Rollback Plan
{How to undo if this goes wrong — specific steps, not "revert the change"}

### Verification
- {How to confirm the decision is working as expected}
- {Metric or test that validates success}

## Review Triggers
{Specific, measurable conditions — not "if things change"}
- {metric} exceeds {threshold} (e.g., "p99 latency > 500ms")
- {event} occurs (e.g., "team grows beyond 8 engineers")
- {time} passes (e.g., "re-evaluate after 6 months of production data")
```

## Step 6: Revising an existing ADR

When the user asks to revise or update an ADR:

You MUST:
- Read the existing ADR file
- Analyze what changed in the codebase since the ADR was written (git log, file diffs)
- Determine if the decision still holds or if review triggers have been hit
- If superseding: create a new ADR that references the old one, explain what changed

## Step 7: Offer next steps

After producing the ADR, offer:

> Would you like me to:
> - Generate the implementation code for the chosen option?
> - Create the migration script or step-by-step PR plan?
> - Write tests that validate the new architecture?
> - Draft a follow-up ADR for a dependent decision?
> - Check if any review triggers from existing ADRs have been hit?

## Calibration Guidance

- An ADR is a decision log, not a sales pitch — document the REAL trade-offs, including uncomfortable ones
- Code evidence grounds the decision — "affects 3 files" is better than "low effort"
- Review triggers with specific thresholds are what makes ADRs useful 6 months later
- If no code is available, the ADR still has value but mark implementation sections for verification
- The migration path IS the ADR's most actionable section — make it specific enough that someone could follow it
- Reversibility is critical to document — irreversible decisions deserve more options analysis
- Don't pad the WA pillar table — only include pillars where there's a real, non-obvious impact
