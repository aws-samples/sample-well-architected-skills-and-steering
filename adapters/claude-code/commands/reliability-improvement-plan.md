Identify single points of failure, assess recovery capabilities, and produce a prioritized remediation plan aligned with the Well-Architected Reliability pillar.

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

Check for:
- Single-AZ deployments (databases, compute, caches)
- Single-region dependencies with no failover
- Undeplicated data stores (no backups, no read replicas)
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

## Current State
- **Availability target**: {target}
- **Estimated current availability**: {estimate}
- **RTO**: {current} → {target}
- **RPO**: {current} → {target}

## Single Points of Failure
| Component | Failure Impact | Current Mitigation | Gap |
|-----------|---------------|-------------------|-----|
| {component} | {impact} | {mitigation or "None"} | {what's missing} |

## Remediation Plan

### Phase 1: Critical (address immediately)
{Each: SPOF to eliminate, how, AWS services to use, expected availability gain}

### Phase 2: Important (next 30 days)
{Each: improvement, implementation approach, benefit}

### Phase 3: Hardening (next 90 days)
{Each: advanced resilience measure, chaos testing, multi-region}

## Architecture Recommendations
{Specific changes: multi-AZ, read replicas, circuit breakers, async patterns, etc.}

## Testing Plan
{How to validate each improvement: failover drills, load tests, game days}
```
