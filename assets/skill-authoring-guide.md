# DevOps Agent Skill Authoring Guide

## Skill Structure

```
my-skill/
├── SKILL.md              # Required: main instructions (max 6 MB total zip)
├── references/           # Optional: supplementary documentation
│   ├── metrics.md
│   └── runbooks.md
└── assets/               # Optional: images, diagrams, data files
    ├── topology.png
    └── thresholds.csv
```

## Writing Effective Frontmatter

The `name` and `description` fields determine whether DevOps Agent activates your skill.

### Name rules
- Lowercase letters, numbers, and hyphens only
- Maximum 64 characters
- Must not start or end with a hyphen
- Use descriptive names: `rds-connection-exhaustion` not `db-skill`

### Description guidelines

Write from the agent's perspective. Include:
- Specific AWS services covered
- Error types and symptoms that trigger activation
- Investigation scenarios handled

**Effective:**
```yaml
description: Investigation procedures for RDS performance issues including
  connection exhaustion, slow queries, replication lag, and storage capacity.
  Use this skill when investigating database latency, connection errors, or
  read/write performance degradation.
```

**Ineffective:**
```yaml
description: Database investigation skill
```

Minimum 100 characters recommended, maximum 1,024 characters.

## Writing Instructions

### Structure principles

1. **Step-by-step procedures** — Number each phase
2. **Specific and actionable** — Name exact metrics, API calls, thresholds
3. **Decision trees** — Branch on conditions: "If X > Y, then check Z"
4. **Success criteria** — Define what a completed investigation looks like
5. **Severity classification** — Help the agent assess impact consistently

### Instruction template

```markdown
# {Scenario Name}

Use this skill when {specific trigger conditions}.

## Step 1: {First action}

{What to do, what to look for, specific metrics/commands}

Look for:
- {Specific metric} exceeding {threshold}
- {Specific condition} indicating {problem}

## Step 2: {Second action}

{Next step with clear inputs from Step 1}

If {condition from Step 1}:
- {Branch A action}
Otherwise:
- {Branch B action}

## Step 3: {Analysis}

{How to interpret what was found}

## Step 4: {Summary}

Provide a summary with:
1. Current status (healthy / degraded / critical)
2. Root cause hypothesis with supporting evidence
3. Recommended actions ranked by priority
```

## Agent Type Targeting

| Agent Type | Use when skill is for... |
|-----------|--------------------------|
| Generic | All contexts (default) |
| On-demand | User-initiated questions and investigations |
| Incident Triage | Initial assessment, severity classification, skip criteria |
| Incident RCA | Systematic root cause analysis, metric correlation |
| Incident Mitigation | Safe remediation actions, rollback, scaling |
| Evaluation | Proactive health checks, drift detection, recommendations |

**Targeting tips:**
- Use the narrowest type that matches your skill's purpose
- Generic skills consume context in ALL agent types — be specific
- Triage skills should be fast and decisive (skip, investigate, or escalate)
- RCA skills should be thorough and evidence-based
- Mitigation skills must include safety checks and verification steps

## Incident Filtering Skills

Target to **Incident Triage** to automatically skip incidents:

```markdown
---
name: skip-known-flapping-alarm
description: Skip incidents from the order-processing-latency alarm when
  it flaps during the nightly batch job window (02:00-04:00 UTC). This
  alarm is known to trigger during batch processing and resolves without
  intervention.
---

# Skip Nightly Batch Flapping

Skip incidents that meet ALL of the following:
1. Source alarm: `order-processing-latency-high`
2. Time: between 02:00 UTC and 04:00 UTC
3. Severity: MEDIUM or LOW

Do NOT skip if:
- Severity is HIGH or CRITICAL
- The alarm remains in ALARM state for more than 30 minutes
- Multiple alarms fire simultaneously
```

## Common Skill Patterns

### Pattern: Service investigation
Focused on one AWS service's failure modes. Covers 3-5 most common issues.

### Pattern: Cross-service correlation
Traces issues across service boundaries. Starts with customer-facing symptoms and works backward.

### Pattern: Deployment validation
Checks service health after deployments. Compares current metrics to pre-deploy baselines.

### Pattern: Capacity planning
Evaluates current utilization trends and predicts when limits will be hit.

### Pattern: Compliance check
Verifies infrastructure against organizational policies or regulatory requirements.

## Testing Skills

Before deploying:
1. Read the skill as if you had no context — is every step clear?
2. Verify all metric names, API calls, and thresholds are correct
3. Check that decision trees cover all branches (including "none of the above")
4. Ensure the skill doesn't assume access to tools not available in your Agent Space
5. Validate that the description accurately reflects when the skill should activate
