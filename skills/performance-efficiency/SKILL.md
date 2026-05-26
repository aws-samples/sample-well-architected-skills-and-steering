---
name: performance-efficiency
description: Evaluate a workload's performance efficiency against the Well-Architected Performance Efficiency pillar, covering resource selection, scaling, monitoring, and optimization opportunities.
version: 1.1.0
---

# Performance Efficiency Assessment

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for performance efficiency? Please share:
> - **Architecture overview** (compute, storage, database, networking services)
> - **Performance requirements** (latency targets, throughput needs, concurrent users)
> - **Current baselines** (p50/p95/p99 latency, request rates, error rates)
> - **Known bottlenecks** (optional — areas you suspect are underperforming)

If context is already provided, proceed directly.

## Step 2: Evaluate resource selection

Classify findings by severity:
- 🔴 **Critical** — actively causing user-facing performance degradation
- 🟡 **High** — suboptimal performance, noticeable under load
- 🟢 **Medium** — optimization opportunity, not yet impacting users

Assess whether optimal resource types are used:

- **Compute** — Are instance types matched to workload characteristics? (compute-optimized vs memory-optimized vs general purpose, Graviton adoption)
- **Storage** — Are storage tiers matched to access patterns? (gp3 vs io2, S3 classes, EFS vs FSx)
- **Database** — Is the database engine appropriate for the access pattern? (relational vs key-value vs document vs graph vs time-series)
- **Networking** — Are placement groups, enhanced networking, or accelerated transfers used where latency matters?
- **Accelerators** — Are GPUs, Inferentia, or custom hardware used where applicable?

## Step 3: Assess scaling and elasticity

Evaluate:

- Is auto-scaling configured with metrics that reflect actual demand? (not just CPU — consider queue depth, request count, custom metrics)
- Are scaling policies responsive enough? (target tracking vs step scaling, cooldown periods)
- Is there pre-warming or scheduled scaling for predictable traffic patterns?
- Are there scaling bottlenecks? (database connections, DNS propagation, cold starts)
- Is the architecture designed to scale horizontally? (stateless compute, distributed caching)

## Step 4: Evaluate caching strategy

Assess:

- Is data cached at the right layers? (CDN, API Gateway cache, application cache, database cache)
- Are cache hit ratios monitored? What are they?
- Is cache invalidation well-managed? (TTL-based, event-driven, or manual)
- Are hot spots identified and mitigated? (DAX for DynamoDB, ElastiCache for session/query data)
- Is content delivery optimized? (CloudFront with appropriate cache behaviors, edge functions)

## Step 5: Assess data and network optimization

Evaluate:

- Is data transfer minimized? (compression, pagination, field selection, binary protocols)
- Are synchronous calls that could be async identified? (SQS, EventBridge, Step Functions)
- Is connection management optimized? (connection pooling, keep-alive, HTTP/2)
- Are queries optimized? (indexes, query plans, read replicas for read-heavy workloads)
- Is data locality considered? (region selection, multi-region for global users)

## Step 6: Evaluate monitoring and optimization practices

Assess:

- Are performance metrics tracked at meaningful percentiles? (p50, p95, p99, not just averages)
- Are there performance budgets and alerts?
- Is load testing conducted regularly? (peak load, sustained load, spike scenarios)
- Is there a process for reviewing and acting on performance data?
- Are experiments conducted to evaluate new approaches? (A/B testing infrastructure changes)

## Step 7: Produce findings

Output:

```markdown
# Performance Efficiency Assessment: {Workload Name}

## Summary
- **Date**: {date}
- **Latency target**: {target} | **Current**: {p50/p95/p99}
- **Throughput target**: {target} | **Current**: {actual}
- **Findings**: {X} Critical, {Y} High, {Z} Medium

## Performance Scorecard
| Domain | Score (1-5) | Key Gap |
|--------|-------------|---------|
| Resource Selection | {score} | {gap} |
| Scaling & Elasticity | {score} | {gap} |
| Caching | {score} | {gap} |
| Data & Network | {score} | {gap} |
| Monitoring & Optimization | {score} | {gap} |

## Critical Performance Issues
{Each: what's bottlenecked, severity, impact on user experience, recommendation, expected improvement, AWS service}

## Optimization Opportunities

### Resource Selection
| Resource | Current | Recommended | Expected Improvement | AWS Service |
|----------|---------|-------------|---------------------|-------------|
| {resource} | {current config} | {recommended} | {improvement} | {service} |

### Scaling Improvements
{Each: current limitation, recommended change, AWS service, implementation approach}

### Caching Opportunities
{Each: cache layer to add/improve, expected hit ratio, latency reduction, AWS service}

### Data and Network Optimizations
{Each: current pattern, optimized pattern, expected benefit, AWS service}

## Remediation Plan

### Quick Wins (< 1 week)
{Configuration changes, enabling features, easy right-sizing}

### Foundation (1-4 weeks)
{Caching layers, scaling policies, monitoring improvements}

### Strategic (1-3 months)
{Architecture changes, database migrations, global distribution}

## Next Steps
{Concrete actions: load test scenarios to run, metrics to instrument, experiments to try}
```

## Step 8: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Deep-dive into a specific bottleneck?
> - Design a caching strategy for a particular data flow?
> - Create a load testing plan with target scenarios?
> - Evaluate alternative architectures for a specific component?
> - Model the performance impact of a scaling change?
