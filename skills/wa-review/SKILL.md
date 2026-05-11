---
name: wa-review
description: Perform a full AWS Well-Architected Framework review of a workload, evaluating all six pillars and producing a prioritized findings report with actionable recommendations.
version: 1.0.0
---

# Well-Architected Review

## Step 1: Define the workload scope

Ask the user to describe the workload:

> What workload would you like me to review? Please share:
> - **Workload name** and brief description
> - **Architecture diagram or description** (services, data flows, integrations)
> - **Business criticality** (revenue-generating, internal tool, compliance-sensitive, etc.)
> - **Current pain points** (optional — anything you already know is problematic)

If the user has already provided architecture details, skip the prompt and proceed.

## Step 2: Identify applicable lens

Determine if a specialized WA Lens applies:
- SaaS, Serverless, Data Analytics, Machine Learning, IoT, SAP, Games, Financial Services, Healthcare, etc.

If a lens applies, note it and incorporate lens-specific questions in the review.

## Step 3: Evaluate each pillar

For each of the six pillars, assess the workload against key best practices:

### Operational Excellence
- How are changes deployed? (CI/CD, IaC, rollback strategy)
- How is the workload monitored? (metrics, alarms, dashboards)
- How are operational events handled? (runbooks, on-call, post-incident reviews)

### Security
- How are identities and permissions managed? (IAM, least privilege, federation)
- How is data protected? (encryption at rest/transit, key management)
- How are security events detected and responded to? (GuardDuty, Security Hub, incident response)

### Reliability
- How does the workload handle component failures? (multi-AZ, retries, circuit breakers)
- How is capacity managed? (auto-scaling, load testing, quotas)
- How are changes managed to avoid outages? (deployment strategies, health checks)

### Performance Efficiency
- Are the right resource types and sizes selected? (instance types, storage tiers)
- How is performance monitored? (latency percentiles, bottleneck identification)
- Are there opportunities for caching, CDN, or async processing?

### Cost Optimization
- Are resources right-sized? (utilization metrics, Savings Plans, Reserved Instances)
- Are there idle or orphaned resources?
- Is the pricing model appropriate? (on-demand vs spot vs reserved, serverless vs provisioned)

### Sustainability
- Is resource utilization maximized? (right-sizing, scaling to zero)
- Are managed services used where possible?
- Is data lifecycle managed? (tiering, expiration, compression)

## Step 4: Classify findings

For each finding, assign:
- **Severity**: 🔴 High Risk Issue (HRI) | 🟡 Medium Risk Issue (MRI) | 🟢 Improvement opportunity
- **Pillar**: Which pillar it belongs to
- **Impact**: What could go wrong if not addressed
- **Effort**: Low / Medium / High to remediate

## Step 5: Produce the report

Output a structured report:

```markdown
# Well-Architected Review: {Workload Name}

## Summary
- **Date**: {date}
- **Pillars reviewed**: 6/6
- **Lens applied**: {lens or "General"}
- **Findings**: {X} HRI, {Y} MRI, {Z} Improvements

## High Risk Issues
{For each HRI: description, impact, recommendation, effort, AWS services to use}

## Medium Risk Issues
{For each MRI: description, impact, recommendation, effort}

## Improvement Opportunities
{For each improvement: description, benefit, recommendation}

## Prioritized Remediation Plan
{Ordered list of actions by impact and effort}

## Next Steps
{Concrete actions the team should take}
```

## Step 6: Offer follow-up

After delivering the report, offer:

> Would you like me to:
> - Deep-dive into any specific pillar?
> - Create an implementation plan for a specific finding?
> - Generate IaC templates to remediate an issue?
> - Compare alternative approaches for a recommendation?
