Review an AWS architecture for cost waste, right-sizing opportunities, and pricing model improvements by examining IaC configurations, scaling policies, and resource provisioning in the codebase.

## Step 1: Gather context

Ask the user:

> What workload would you like me to audit for cost optimization? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Traffic patterns** (steady, spiky, predictable growth, seasonal)
> - **Monthly spend estimate** (optional — helps calibrate severity)

If already in a codebase with IaC, proceed directly.

## Step 2: Compute Cost Discovery

Analyze all compute configurations:

- EC2 instance types/sizes in ASG/launch templates
- ECS task definitions (CPU/memory)
- Lambda memory and timeout
- Fargate task sizes, EKS node groups

Flag as HIGH RISK:
- Fixed-size compute (no auto-scaling) for variable workloads
- Over-provisioned Lambda (>1024MB for simple ops)
- x86 where Graviton exists
- Dev/test at production scale
- No scheduled scaling for environments with off-hours

## Step 3: Storage and Data Cost Discovery

Analyze storage configurations:

- S3 lifecycle policies (or absence)
- CloudWatch log retention
- DynamoDB capacity mode
- EBS volume types (gp2 vs gp3)
- Backup retention policies

Flag as HIGH RISK:
- S3 without lifecycle policies
- "Never expire" log retention
- gp2 volumes (gp3 is cheaper for same performance)
- Backup retention > 35 days without justification
- S3 versioning without version expiration

## Step 4: Data Transfer Cost Discovery

Analyze network patterns:

- NAT Gateway usage (VPC endpoints would be free for S3/DynamoDB)
- CloudFront presence (or absence for static content)
- API Gateway type (REST vs HTTP API — 70% cheaper)
- Cross-region replication patterns

Flag: S3/DynamoDB through NAT Gateway, no CDN for static content, REST API where HTTP API suffices.

## Step 5: Pricing Model and Environment Assessment

Evaluate:

- Serverless vs provisioned alignment
- Spot Instance opportunities for batch/fault-tolerant
- Non-production environment sizing and scheduling
- Cost allocation tags (present or absent)
- Budget/anomaly detection configs

## Step 6: Evaluate against WA Framework questions

Every assessment MUST include: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

- **COST 1 — Financial management**: cost allocation tags, budget configs
- **COST 3 — Monitor cost**: Budget alarms, anomaly detection
- **COST 4 — Decommission**: lifecycle policies, retention, cleanup
- **COST 5 — Service selection**: pricing model alignment
- **COST 6 — Right-sizing**: instance types, scaling boundaries
- **COST 7 — Pricing models**: Savings Plans, Reserved, Spot
- **COST 8 — Data transfer**: VPC endpoints, CloudFront, regional placement

## Step 7: Risk Assessment

| Impact   | Likelihood | Risk Level |
|----------|------------|------------|
| Severe   | High       | Critical   |
| Severe   | Medium     | High       |
| Severe   | Low        | High       |
| Moderate | High       | High       |
| Moderate | Medium     | Medium     |
| Moderate | Low        | Medium     |
| Minor    | High       | Medium     |
| Minor    | Medium     | Low        |
| Minor    | Low        | Low        |

## Step 8: Produce the report

Structure:

- Executive Summary (date, packages analyzed, findings count, cost efficiency score 1-5, top 3 savings)
- Cost Optimization Scorecard (Compute Right-Sizing, Storage Lifecycle, Data Transfer, Pricing Models, Environment Management, Cost Visibility — each scored 1-5)
- Critical and High Risk Findings (ID, domain, title, evidence file:line, cost impact, recommendation, effort, AWS services)
- Medium/Low Findings
- Savings Summary table (category, current config, optimized config, relative savings, effort)
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- Next Steps (top 5 actions)

## Calibration

- Every finding MUST have code evidence
- Savings should be relative (%) when absolute spend is unknown
- Always assess trade-offs: cost optimization MUST NOT introduce reliability risks without acknowledgment
- "Cannot Determine" is valid when actual utilization requires CloudWatch metrics
- Acknowledge good cost practices before listing waste
