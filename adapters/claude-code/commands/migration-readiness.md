Assess a workload's readiness to migrate to AWS using Well-Architected principles, covering the 7 Rs, dependencies, risks, and a migration plan.

## Step 1: Gather context

Ask the user:

> What workload are you planning to migrate? Please share:
> - **Current environment** (on-premises, other cloud, colocation)
> - **Application stack** (languages, frameworks, databases, middleware)
> - **Dependencies** (other systems it talks to, shared databases, network requirements)
> - **Business drivers** (cost, agility, compliance, end-of-life hardware, etc.)
> - **Timeline constraints** (optional)

If context is already provided, proceed directly.

## Step 2: Determine migration strategy (7 Rs)

For the workload, evaluate which strategy fits:

| Strategy | When to use |
|----------|-------------|
| **Rehost** (lift & shift) | Fast migration, minimal changes, optimize later |
| **Replatform** (lift & reshape) | Small optimizations during move (e.g., managed DB) |
| **Refactor** (re-architect) | Need cloud-native benefits, willing to invest |
| **Repurchase** | Replace with SaaS (e.g., CRM to Salesforce) |
| **Retire** | No longer needed |
| **Retain** | Not ready to move yet |
| **Relocate** | VMware workloads to VMware Cloud on AWS |

Recommend a strategy with justification based on the user's drivers and constraints.

## Step 3: Assess readiness by pillar

### Operational Excellence
- Is there IaC for the current environment? Can it be adapted?
- Are CI/CD pipelines in place?
- Is monitoring portable or cloud-specific?

### Security
- Are there compliance requirements that affect region/service choice?
- How are secrets and certificates managed today?
- Are there network security dependencies (firewalls, IDS) that need equivalents?

### Reliability
- What is the current availability? What's the target post-migration?
- Are there HA/DR mechanisms that need to be replicated?
- What's the acceptable downtime during migration?

### Performance Efficiency
- Are there latency-sensitive integrations?
- Are there hardware-specific dependencies (GPUs, FPGAs, specific CPU)?
- What are the current performance baselines?

### Cost Optimization
- What's the current TCO?
- What's the expected AWS cost? (rough estimate)
- Are there licensing implications? (BYOL, license-included)

### Sustainability
- Can the migration reduce resource footprint?
- Are there opportunities to use Graviton or serverless?

## Step 4: Identify risks and blockers

Flag:
- Hard dependencies on on-premises systems that can't move yet
- Licensing restrictions (Oracle, Windows, third-party software)
- Data residency or sovereignty requirements
- Large data volumes requiring transfer planning (Snowball, DataSync, DMS)
- Skills gaps in the team
- Compliance re-certification requirements

## Step 5: Produce the assessment

Output:

```markdown
# Migration Readiness Assessment: {Workload Name}

## Summary
- **Recommended strategy**: {strategy}
- **Readiness score**: {Ready / Conditionally Ready / Not Ready}
- **Estimated effort**: {T-shirt size}
- **Key risks**: {top 2-3}

## Migration Strategy Rationale
{Why this strategy fits the workload and business drivers}

## Readiness by Pillar
| Pillar | Ready? | Key Gap |
|--------|--------|---------|
| Operational Excellence | pass/warn/fail | {gap} |
| Security | pass/warn/fail | {gap} |
| Reliability | pass/warn/fail | {gap} |
| Performance Efficiency | pass/warn/fail | {gap} |
| Cost Optimization | pass/warn/fail | {gap} |
| Sustainability | pass/warn/fail | {gap} |

## Risks and Blockers
| Risk | Impact | Mitigation |
|------|--------|------------|
| {risk} | {High/Med/Low} | {mitigation} |

## Pre-Migration Checklist
{What must be done before migration starts}

## High-Level Migration Plan
{Phases: Assess, Mobilize, Migrate, Optimize}

## AWS Services for Migration
{Relevant services: MGN, DMS, DataSync, Transfer Family, SCT, etc.}
```
