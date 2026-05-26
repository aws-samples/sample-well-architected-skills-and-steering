---
name: reliability-improvement-plan
description: Identify single points of failure, assess recovery capabilities, and produce a prioritized remediation plan aligned with the Well-Architected Reliability pillar.
version: 1.1.0
---

# Reliability Improvement Plan

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for reliability? Please share:
> - **Architecture overview** (services, regions, AZs, dependencies)
> - **Availability target** (99.9%, 99.95%, 99.99%, etc.)
> - **Recovery objectives** (RTO and RPO if defined)
> - **Past incidents** (optional — recent outages or near-misses)

If context is already provided, proceed directly.

## Step 2: Identify single points of failure

For each component, ask: "What happens if this fails?"

Classify each SPOF by severity:
- 🔴 **High Risk** — total outage or data loss if this component fails
- 🟡 **Medium Risk** — degraded experience or partial outage
- 🟢 **Low Risk** — minimal impact, graceful degradation

Check for:
- Single-AZ deployments (databases, compute, caches)
- Single-region dependencies with no failover
- Unreplicated data stores (no backups, no read replicas)
- Hard dependencies on third-party services without fallback
- Single NAT Gateway, single bastion, single load balancer
- Shared-nothing vs shared-everything bottlenecks

## Step 3: Assess recovery capabilities

Evaluate:
- **Backup strategy** — Are backups automated, tested, and cross-region?
- **Failover mechanisms** — Is failover automatic or manual? How long does it take?
- **Health checks** — Are they deep enough to detect real failures?
- **Deployment rollback** — Can a bad deploy be reverted in minutes?
- **Dependency isolation** — Does one service failure cascade?
- **Chaos engineering** — Are failure scenarios tested proactively?

## Step 4: Evaluate scaling and capacity

Assess:
- Is auto-scaling configured with appropriate min/max/cooldown?
- Are service quotas monitored and increased proactively?
- Is there load shedding or throttling for overload scenarios?
- Are queues used to absorb traffic spikes?
- Is capacity tested under peak load?

## Step 5: Assess change management

Evaluate:
- Are deployments canary or blue/green?
- Are database migrations backward-compatible?
- Is there automated rollback on health check failure?
- Are changes tested in a staging environment that mirrors production?

## Step 6: Produce the plan

Output:

```markdown
# Reliability Improvement Plan: {Workload Name}

## Summary
- **Date**: {date}
- **Availability target**: {target}
- **Estimated current availability**: {estimate}
- **RTO**: {current} → {target}
- **RPO**: {current} → {target}
- **Findings**: {X} High Risk, {Y} Medium Risk, {Z} Low Risk

## Reliability Scorecard
| Domain | Score (1-5) | Key Gap |
|--------|-------------|---------|
| Fault Tolerance | {score} | {gap} |
| Recovery & Backup | {score} | {gap} |
| Scaling & Capacity | {score} | {gap} |
| Change Management | {score} | {gap} |
| Testing & Validation | {score} | {gap} |

## Single Points of Failure
| Component | Severity | Failure Impact | Current Mitigation | Gap | AWS Service to Fix |
|-----------|----------|---------------|-------------------|-----|-------------------|
| {component} | 🔴/🟡/🟢 | {impact} | {mitigation or "None"} | {what's missing} | {service} |

## High Risk Findings
{Each: SPOF description, blast radius, recommendation, AWS services, effort}

## Remediation Plan

### Quick Wins (< 1 week)
{Low-effort high-impact: enable backups, turn on Multi-AZ, add health checks}

### Foundation (1-4 weeks)
{Multi-AZ compute, auto-scaling, circuit breakers, deployment safety}

### Advanced (1-3 months)
{Multi-region, chaos engineering, automated failover drills}

## Architecture Recommendations
{Specific changes: multi-AZ, read replicas, circuit breakers, async patterns, etc.}

## Testing Plan
| Test | What it validates | Frequency | AWS Service |
|------|-------------------|-----------|-------------|
| AZ failover drill | Compute continues in remaining AZs | Monthly | FIS |
| Database failover | RDS/Aurora failover < 60s | Quarterly | FIS |
| Load test | Capacity handles 2x peak | Before releases | Distributed Load Testing |
| Backup restore | RPO is met, data is recoverable | Monthly | AWS Backup |
| Deployment rollback | Bad deploy is reverted < 5 min | Every deploy | CodeDeploy |

## Next Steps
{Concrete actions the team should take this week}
```

## Step 7: Offer follow-up

After delivering the plan, offer:

> Would you like me to:
> - Design the multi-AZ architecture in detail?
> - Create a chaos engineering experiment plan using AWS FIS?
> - Build a failover testing runbook?
> - Estimate the cost of the reliability improvements?
> - Design circuit breaker patterns for your service dependencies?
