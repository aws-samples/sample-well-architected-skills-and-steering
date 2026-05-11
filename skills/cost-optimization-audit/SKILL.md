---
name: cost-optimization-audit
description: Analyze an AWS architecture for cost waste, right-sizing opportunities, and pricing model improvements aligned with the Well-Architected Cost Optimization pillar.
version: 1.0.0
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

## Step 4: Assess architecture efficiency

Evaluate:
- Could caching reduce compute/database load? (ElastiCache, CloudFront, DAX)
- Are there synchronous calls that could be async? (SQS, EventBridge — reduces over-provisioning)
- Is data lifecycle managed? (S3 lifecycle policies, RDS snapshot retention, log expiration)
- Are environments right-sized for their purpose? (dev/test smaller than prod, scheduled scaling)

## Step 5: Quantify savings

For each recommendation, estimate:
- **Current cost** (monthly)
- **Projected cost** after change
- **Savings** ($ and %)
- **Effort** to implement (Low / Medium / High)
- **Risk** of the change

## Step 6: Produce the report

Output:

```markdown
# Cost Optimization Audit: {Workload Name}

## Summary
- **Estimated current monthly spend**: ${X}
- **Potential monthly savings**: ${Y} ({Z}%)
- **Recommendations**: {N} total

## Quick Wins (< 1 day effort)
{Each: what to do, savings estimate, how to implement}

## Medium-Term Optimizations (1-2 weeks)
{Each: what to change, savings estimate, trade-offs}

## Strategic Changes (requires architecture work)
{Each: what to redesign, savings estimate, effort, risk}

## Savings Summary
| Category | Current | Optimized | Savings |
|----------|---------|-----------|---------|
| Compute | | | |
| Storage | | | |
| Data Transfer | | | |
| Database | | | |
| Other | | | |
| **Total** | | | |

## Next Steps
{Concrete actions to start saving}
```
