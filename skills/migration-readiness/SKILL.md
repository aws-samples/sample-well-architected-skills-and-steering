---
name: migration-readiness
description: Assess a workload's readiness to migrate to AWS using Well-Architected principles, covering the 7 Rs, dependencies, risks, and a migration plan.
version: 1.1.0
---

# Migration Readiness Assessment

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
| **Repurchase** | Replace with SaaS (e.g., CRM → Salesforce) |
| **Retire** | No longer needed |
| **Retain** | Not ready to move yet |
| **Relocate** | VMware workloads → VMware Cloud on AWS |

Recommend a strategy with justification based on the user's drivers and constraints.

## Step 3: Assess readiness by pillar

For each pillar, classify readiness as:
- 🟢 **Ready** — no blockers, can proceed
- 🟡 **Conditionally Ready** — gaps exist but can be addressed during migration
- 🔴 **Not Ready** — blockers must be resolved before migration

### Operational Excellence
- Is there IaC for the current environment? Can it be adapted?
- Are CI/CD pipelines in place?
- Is monitoring portable or cloud-specific?
- Are operational runbooks documented?

### Security
- Are there compliance requirements that affect region/service choice?
- How are secrets and certificates managed today?
- Are there network security dependencies (firewalls, IDS) that need equivalents?
- Is identity federation in place or needed?

### Reliability
- What is the current availability? What's the target post-migration?
- Are there HA/DR mechanisms that need to be replicated?
- What's the acceptable downtime during migration?
- Are backups and recovery procedures tested?

### Performance Efficiency
- Are there latency-sensitive integrations?
- Are there hardware-specific dependencies (GPUs, FPGAs, specific CPU)?
- What are the current performance baselines?
- Are there performance SLAs that must be maintained during cutover?

### Cost Optimization
- What's the current TCO?
- What's the expected AWS cost? (rough estimate)
- Are there licensing implications? (BYOL, license-included)
- Are there existing commitments (contracts, prepaid licenses)?

### Sustainability
- Can the migration reduce resource footprint?
- Are there opportunities to use Graviton or serverless?
- Can managed services replace self-managed infrastructure?

## Step 4: Identify risks and blockers

Classify each risk by severity:
- 🔴 **High Risk** — can block migration or cause failure
- 🟡 **Medium Risk** — increases effort or timeline but manageable
- 🟢 **Low Risk** — minor impact, address during optimization

Flag:
- Hard dependencies on on-premises systems that can't move yet
- Licensing restrictions (Oracle, Windows, third-party software)
- Data residency or sovereignty requirements
- Large data volumes requiring transfer planning (Snowball, DataSync, DMS)
- Skills gaps in the team
- Compliance re-certification requirements
- Performance-sensitive integrations with on-premises systems

## Step 5: Produce the assessment

Output:

```markdown
# Migration Readiness Assessment: {Workload Name}

## Summary
- **Recommended strategy**: {strategy}
- **Overall readiness**: {Ready / Conditionally Ready / Not Ready}
- **Estimated effort**: {T-shirt size with justification}
- **Key risks**: {top 2-3}
- **Estimated timeline**: {weeks/months}

## Migration Strategy Rationale
{Why this strategy fits the workload and business drivers}

## Readiness Scorecard
| Pillar | Readiness | Score (1-5) | Key Gap |
|--------|-----------|-------------|---------|
| Operational Excellence | 🟢/🟡/🔴 | {score} | {gap} |
| Security | 🟢/🟡/🔴 | {score} | {gap} |
| Reliability | 🟢/🟡/🔴 | {score} | {gap} |
| Performance Efficiency | 🟢/🟡/🔴 | {score} | {gap} |
| Cost Optimization | 🟢/🟡/🔴 | {score} | {gap} |
| Sustainability | 🟢/🟡/🔴 | {score} | {gap} |

## Risks and Blockers
| Risk | Severity | Impact | Mitigation | AWS Service |
|------|----------|--------|------------|-------------|
| {risk} | 🔴/🟡/🟢 | {impact} | {mitigation} | {service} |

## Pre-Migration Checklist
{What must be done before migration starts, ordered by priority}

## Migration Plan

### Phase 1: Assess & Mobilize (Weeks 1-2)
{Discovery, dependency mapping, landing zone setup}

### Phase 2: Migrate (Weeks 3-6)
{Data migration, application migration, testing}

### Phase 3: Optimize (Weeks 7-8)
{Right-sizing, cost optimization, performance tuning}

## AWS Services for Migration
| Category | Service | Purpose |
|----------|---------|---------|
| Server migration | AWS MGN | Rehost EC2 workloads |
| Database migration | AWS DMS | Replicate databases with minimal downtime |
| Data transfer | DataSync / Snowball | Large-scale data movement |
| Schema conversion | AWS SCT | Convert database schemas |
| Network | Direct Connect / VPN | Hybrid connectivity |
| Landing zone | Control Tower | Multi-account governance |

## Cost Comparison
| Category | Current (monthly) | Estimated AWS (monthly) | Savings |
|----------|-------------------|-------------------------|---------|
| Compute | {current} | {estimated} | {delta} |
| Storage | {current} | {estimated} | {delta} |
| Networking | {current} | {estimated} | {delta} |
| Licensing | {current} | {estimated} | {delta} |
| **Total** | {total} | {total} | {delta} |
```

## Step 6: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Design the AWS landing zone architecture?
> - Create a detailed data migration plan?
> - Estimate AWS costs in more detail (instance mapping, storage tiers)?
> - Build a pre-migration testing strategy?
> - Identify quick wins to demonstrate value early?
