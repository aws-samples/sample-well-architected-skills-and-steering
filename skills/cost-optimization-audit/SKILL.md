---
name: cost-optimization-audit
description: Analyze an AWS architecture for cost waste, right-sizing opportunities, and pricing model improvements aligned with the Well-Architected Cost Optimization pillar.
version: 1.1.0
---

# Cost Optimization Audit

## Step 1: Gather context

Ask the user:

> What workload or AWS environment would you like me to audit for cost optimization? Please share:
> - **Architecture overview** (services used, rough monthly spend if known)
> - **Traffic patterns** (steady, spiky, predictable growth, seasonal)
> - **Commitment status** (Savings Plans, Reserved Instances, existing contracts)
> - **Budget constraints or targets** (optional)

If context is already provided, proceed directly.

## Step 2: Identify waste

Classify each finding by severity:
- 🔴 **High** — significant ongoing waste (>20% of category spend or >$500/month)
- 🟡 **Medium** — moderate waste (5-20% of category spend or $100-500/month)
- 🟢 **Low** — minor waste or optimization opportunity

Look for:
- **Idle resources** — unattached EBS volumes, unused Elastic IPs, idle load balancers, stopped instances with attached storage
- **Over-provisioned resources** — instances with <20% CPU/memory utilization, over-sized RDS instances, over-provisioned DynamoDB capacity
- **Orphaned resources** — old snapshots, unused AMIs, stale log groups, abandoned S3 buckets
- **Redundant data transfer** — cross-AZ traffic that could be avoided, NAT Gateway costs for S3/DynamoDB (use VPC endpoints)

## Step 3: Evaluate pricing models

Assess:
- Are Savings Plans or Reserved Instances used for steady-state workloads?
- Could Spot Instances cover fault-tolerant or batch workloads?
- Would serverless (Lambda, Fargate, Aurora Serverless) reduce cost for variable workloads?
- Are S3 storage classes optimized? (Intelligent-Tiering, Glacier for archives)
- Is there opportunity for Graviton-based instances? (better price-performance)
- Are data transfer costs optimized? (VPC endpoints, CloudFront, regional placement)

## Step 4: Assess architecture efficiency

Evaluate:
- Could caching reduce compute/database load? (ElastiCache, CloudFront, DAX)
- Are there synchronous calls that could be async? (SQS, EventBridge — reduces over-provisioning)
- Is data lifecycle managed? (S3 lifecycle policies, RDS snapshot retention, log expiration)
- Are environments right-sized for their purpose? (dev/test smaller than prod, scheduled scaling)
- Can non-production environments be scheduled off during nights/weekends?

## Step 5: Quantify savings

For each recommendation, estimate:
- **Current cost** (monthly)
- **Projected cost** after change
- **Savings** ($ and %)
- **Effort** to implement (Low / Medium / High)
- **Risk** of the change
- **AWS Service** to use

## Step 6: Produce the report

Output:

```markdown
# Cost Optimization Audit: {Workload Name}

## Summary
- **Date**: {date}
- **Estimated current monthly spend**: ${X}
- **Potential monthly savings**: ${Y} ({Z}%)
- **Findings**: {A} High, {B} Medium, {C} Low

## Cost Optimization Scorecard
| Domain | Score (1-5) | Key Gap |
|--------|-------------|---------|
| Waste Elimination | {score} | {gap} |
| Pricing Model | {score} | {gap} |
| Architecture Efficiency | {score} | {gap} |
| Data Lifecycle | {score} | {gap} |
| Environment Management | {score} | {gap} |

## High-Impact Findings
{Each: what's wasteful, severity, current cost, projected savings, AWS service, effort}

## Quick Wins (< 1 week)
{Each: what to do, savings estimate, how to implement, AWS service}

## Foundation Improvements (1-4 weeks)
{Each: what to change, savings estimate, trade-offs, AWS service}

## Strategic Changes (1-3 months)
{Each: what to redesign, savings estimate, effort, risk, AWS service}

## Savings Summary
| Category | Current $/mo | Optimized $/mo | Savings $/mo | AWS Service |
|----------|-------------|----------------|--------------|-------------|
| Compute | {current} | {optimized} | {savings} | Compute Optimizer, Savings Plans |
| Storage | {current} | {optimized} | {savings} | S3 Intelligent-Tiering, Glacier |
| Data Transfer | {current} | {optimized} | {savings} | VPC Endpoints, CloudFront |
| Database | {current} | {optimized} | {savings} | RDS Reserved, Aurora Serverless |
| Other | {current} | {optimized} | {savings} | {relevant services} |
| **Total** | **{total}** | **{total}** | **{total}** | |

## Implementation Roadmap
| Priority | Action | Savings/mo | Effort | Risk |
|----------|--------|-----------|--------|------|
| 1 | {action} | ${savings} | Low | Low |
| 2 | {action} | ${savings} | Medium | Low |
| ... | ... | ... | ... | ... |

## Next Steps
{Concrete actions to start saving immediately}
```

## Step 7: Offer follow-up

After delivering the report, offer:

> Would you like me to:
> - Create a detailed right-sizing plan for a specific service?
> - Model Savings Plans vs Reserved Instances for your usage pattern?
> - Design a FinOps tagging and cost allocation strategy?
> - Build a scheduled scaling policy for non-production environments?
> - Estimate costs for an architectural alternative (serverless, containers, etc.)?
