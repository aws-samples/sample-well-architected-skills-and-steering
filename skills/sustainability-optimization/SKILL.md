---
name: sustainability-optimization
description: Assess a workload's environmental sustainability posture against the Well-Architected Sustainability pillar, identifying opportunities to reduce carbon footprint through resource efficiency, managed services, and architectural optimization.
version: 1.0.0
---

# Sustainability Optimization Assessment

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for sustainability? Please share:
> - **Architecture overview** (compute, storage, database, networking services)
> - **Utilization patterns** (average CPU/memory utilization, traffic patterns, idle periods)
> - **Region selection rationale** (proximity to users, compliance, or legacy?)
> - **Sustainability goals** (optional — organizational carbon targets, reporting requirements)

If context is already provided, proceed directly.

## Step 2: Assess resource utilization

Evaluate how effectively provisioned resources are used:

- **Compute utilization** — Average CPU and memory usage across instances/containers. Are instances idle during off-hours?
- **Storage efficiency** — Are old/unused objects retained? Are lifecycle policies in place? Is storage class appropriate for access frequency?
- **Database utilization** — Is provisioned capacity matched to actual demand? Are there idle read replicas?
- **Network efficiency** — Are data transfers minimized? Are endpoints co-located where possible?
- **Over-provisioning** — Are resources sized for peak when demand is variable?

## Step 3: Evaluate architecture efficiency

Assess:

- **Serverless adoption** — Could provisioned compute be replaced with Lambda, Fargate, or Aurora Serverless to scale to zero?
- **Managed services** — Are there self-managed workloads (Kafka, Elasticsearch, Redis) that could use managed equivalents with better utilization?
- **Graviton adoption** — Are ARM-based instances used where supported? (better performance per watt)
- **Async patterns** — Are synchronous processes that could be event-driven identified? (reduces idle waiting)
- **Batch optimization** — Are batch jobs scheduled during low-carbon grid periods? Are they right-sized?

## Step 4: Assess data management practices

Evaluate:

- **Data lifecycle** — Are retention policies defined and enforced? Is cold data moved to Glacier/Deep Archive?
- **Data deduplication** — Is redundant data storage eliminated?
- **Compression** — Are stored and transferred payloads compressed?
- **Tiered storage** — Is Intelligent-Tiering used for unpredictable access patterns?
- **Data proximity** — Is data stored close to where it's processed?

## Step 5: Evaluate scaling and scheduling

Assess:

- **Scale-to-zero** — Can non-production environments shut down outside business hours?
- **Scheduled scaling** — Are predictable low-traffic periods handled with reduced capacity?
- **Right-sizing cadence** — How often are instance types and sizes reviewed?
- **Spot Instances** — Are fault-tolerant workloads using Spot for better resource pooling?
- **Region-aware scheduling** — Are flexible workloads routed to regions with lower carbon intensity?

## Step 6: Assess software and code efficiency

Evaluate:

- **Algorithmic efficiency** — Are there known inefficient algorithms or unnecessary computation?
- **Caching** — Does caching reduce redundant computation and data retrieval?
- **Payload optimization** — Are API responses, assets, and transfers minimized?
- **Framework efficiency** — Are lightweight runtimes used where possible? (compiled languages vs interpreted for compute-heavy tasks)
- **Client impact** — Is downstream device energy considered? (page weight, client-side computation)

## Step 7: Produce findings

Output:

```markdown
# Sustainability Assessment: {Workload Name}

## Summary
- **Estimated utilization efficiency**: {percentage}
- **Key waste areas**: {top 2-3}
- **Findings**: {X} High Impact, {Y} Medium Impact, {Z} Improvements

## High-Impact Findings
{Each: what's wasteful, estimated carbon/resource impact, how to fix, effort required}

## Optimization Opportunities

### Resource Utilization
| Resource | Current Utilization | Target | Action |
|----------|-------------------|--------|--------|
| {resource} | {current %} | {target %} | {action to take} |

### Architecture Efficiency
{Each: current approach, sustainable alternative, expected improvement}

### Data Management
{Each: current practice, optimized practice, storage/transfer reduction}

### Scheduling & Scaling
{Each: current behavior, optimized behavior, resource hours saved}

## Sustainability Scorecard
| Domain | Score | Key Gap |
|--------|-------|---------|
| Resource Utilization | {1-5} | {gap} |
| Architecture Efficiency | {1-5} | {gap} |
| Data Management | {1-5} | {gap} |
| Scaling & Scheduling | {1-5} | {gap} |
| Software Efficiency | {1-5} | {gap} |

## Prioritized Remediation Plan
{Ordered by carbon impact and implementation effort}

## AWS Sustainability Tools
- **Customer Carbon Footprint Tool** — Track emissions in the AWS console
- **Compute Optimizer** — Right-size recommendations
- **S3 Storage Lens** — Storage efficiency insights
- **Trusted Advisor** — Idle resource detection

## Next Steps
{Concrete actions: quick wins to implement now, architectural changes to plan}
```

## Step 8: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Quantify the carbon impact of a specific optimization?
> - Design a scale-to-zero strategy for non-production environments?
> - Create a resource right-sizing implementation plan?
> - Evaluate Graviton migration feasibility for your workloads?
