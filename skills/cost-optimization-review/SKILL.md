---
name: cost-optimization-review
description: Review an AWS architecture for cost waste, right-sizing opportunities, and pricing model improvements by examining IaC configurations, scaling policies, and resource provisioning in the codebase.
version: 2.0.0
---

# Cost Optimization Review

## Step 1: Gather context

Ask the user:

> What workload or AWS environment would you like me to review for cost optimization? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Traffic patterns** (steady, spiky, predictable growth, seasonal)
> - **Monthly spend estimate** (optional — helps calibrate severity)
> - **Budget constraints or targets** (optional)

If context is already provided or you are in a codebase with IaC, proceed directly.

## Step 2: Compute Cost Discovery

Analyze all compute resource configurations.

You MUST examine:
- EC2 instance types and sizes in ASG/launch templates
- ECS task definitions (CPU/memory allocations)
- Lambda memory and timeout configurations
- Fargate task sizes
- EKS node group configurations
- Batch compute environments

For each compute resource, document:
- File path and line numbers
- Instance type/size configured
- Scaling configuration (min/max/desired)
- Whether Graviton is used (or x86 where Graviton is available)
- Pricing model implications (on-demand only vs Spot-eligible vs Reserved-eligible)

You MUST flag as HIGH RISK:
- Fixed-size compute (no auto-scaling) for variable workloads
- Over-provisioned Lambda (>1024MB for simple operations)
- x86 instance types where Graviton equivalents exist (cost + sustainability)
- Large instance types for workloads that could use smaller instances with horizontal scaling
- Dev/test environments with production-sized resources
- No scheduled scaling for environments with clear off-hours

## Step 3: Storage and Data Cost Discovery

Analyze storage configurations.

You MUST examine:
- S3 bucket configurations (storage class, lifecycle policies, versioning)
- EBS volume types and sizes
- RDS storage configurations (type, allocated size, auto-scaling)
- DynamoDB capacity mode and provisioning
- ElastiCache node types and cluster sizes
- EFS configurations (throughput mode, lifecycle)
- Backup retention policies (AWS Backup, RDS snapshots)
- Log retention settings (CloudWatch log groups)

You MUST flag as HIGH RISK:
- S3 buckets without lifecycle policies (accumulating indefinitely)
- CloudWatch log groups with "never expire" retention
- DynamoDB with provisioned capacity that could use on-demand (or vice versa based on pattern)
- Over-provisioned IOPS on EBS/RDS
- EBS volumes not using gp3 (gp2 is more expensive for same performance)
- Backup retention > 35 days without business justification
- S3 versioning enabled without lifecycle rules to expire old versions

## Step 4: Data Transfer Cost Discovery

Analyze network and data transfer patterns.

You MUST examine:
- NAT Gateway usage (could VPC endpoints replace?)
- Cross-region data transfer patterns
- VPC endpoint configurations (or lack thereof for S3/DynamoDB)
- CloudFront distributions (or lack thereof for static content)
- Cross-AZ traffic patterns (multi-AZ services communicating across AZs)
- API Gateway configurations (REST vs HTTP API pricing)

You MUST flag as HIGH RISK:
- S3/DynamoDB access going through NAT Gateway (VPC endpoint would be free)
- No CloudFront for static content delivery
- REST API Gateway where HTTP API would suffice (70% cheaper)
- Cross-region replication without business justification
- Public S3 access through internet where CloudFront would reduce transfer costs

## Step 5: Pricing Model Assessment

Analyze whether pricing models align with usage patterns.

You MUST evaluate:
- Steady-state compute → Savings Plans or Reserved Instances opportunity
- Variable/batch compute → Spot Instance opportunity
- Serverless vs provisioned alignment (Lambda/Fargate for spiky, EC2/ECS for steady)
- DynamoDB on-demand vs provisioned (on-demand for unpredictable, provisioned for steady)
- Aurora Serverless v2 vs provisioned (for variable database load)
- S3 Intelligent-Tiering for unknown access patterns

## Step 6: Environment and Lifecycle Management

Analyze non-production environment configurations.

You MUST examine:
- Dev/test/staging environment sizing vs production
- Scheduled scaling or shutdown for non-production
- Resource lifecycle policies (TTL on test resources)
- Cost allocation tags on resources
- Budget and anomaly detection configurations

You MUST flag as IMPROVEMENT OPPORTUNITY:
- Non-production environments running 24/7 at production scale
- No cost allocation tags on resources
- No AWS Budget or Cost Anomaly Detection configured
- No lifecycle policies on test/temporary resources

## Step 7: Evaluate against WA Framework questions

For each question, provide: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

### COST 1 — How do you implement cloud financial management?
- Evidence: cost allocation tags, budget configs, anomaly detection rules

### COST 2 — How do you govern usage?
- Evidence: SCPs limiting instance types, quotas, resource constraints

### COST 3 — How do you monitor usage and cost?
- Evidence: Budget alarms, Cost Anomaly Detection configs, billing alarms

### COST 4 — How do you decommission resources?
- Evidence: lifecycle policies, TTL configs, cleanup automation, retention rules

### COST 5 — How do you evaluate cost when you select services?
- Evidence: serverless for variable loads, provisioned for steady, Spot for batch

### COST 6 — How do you meet cost targets when you select resource type, size, and number?
- Evidence: instance types, scaling min/max, memory allocations, right-sizing evidence

### COST 7 — How do you use pricing models to reduce cost?
- Evidence: Savings Plan configs, Reserved capacity, Spot fleet configs

### COST 8 — How do you plan for data transfer charges?
- Evidence: VPC endpoints, CloudFront distributions, regional placement

## Step 8: Quantify savings estimates

For each finding, estimate:
- **Current cost indicator**: resource configuration that drives cost (instance type, provisioned capacity, retention)
- **Optimized configuration**: what the resource should be
- **Relative savings**: percentage reduction for that resource category
- **Effort**: Low / Medium / High to implement
- **Risk**: impact on reliability or performance

## Step 9: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor (< 10% savings in category) | Moderate (10-30% savings in category) | Severe (> 30% savings in category or fundamental pricing model misalignment)

**Likelihood** (of waste continuing): Low (planned optimization exists) | Medium (no plan but low growth) | High (growing unchecked, no visibility)

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

## Step 10: Produce the report

```markdown
# Cost Optimization Review: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Packages Analyzed**: {list}
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Cost Efficiency**: {1-5} — {one-line justification}
- **Top 3 Savings Opportunities**: {brief list}

## Cost Optimization Scorecard
| Domain | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| Compute Right-Sizing | {score} | {strength} | {gap} |
| Storage Lifecycle | {score} | {strength} | {gap} |
| Data Transfer | {score} | {strength} | {gap} |
| Pricing Models | {score} | {strength} | {gap} |
| Environment Management | {score} | {strength} | {gap} |
| Cost Visibility | {score} | {strength} | {gap} |

## Critical and High Risk Findings
{For each: ID, domain, title, description, evidence (file:line), cost impact, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Domain | Title | Recommendation}

## Savings Summary
| Category | Finding | Current Config | Optimized Config | Relative Savings | Effort |
|----------|---------|---------------|-----------------|-----------------|--------|
| Compute | {title} | {current} | {recommended} | {%} | {effort} |
| Storage | {title} | {current} | {recommended} | {%} | {effort} |
| Transfer | {title} | {current} | {recommended} | {%} | {effort} |

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Savings Impact | Effort | Risk |
|---------|--------|---------------|--------|------|
{Switch gp2→gp3, add lifecycle policies, set log retention, add VPC endpoints}

### Foundation (1-4 weeks)
| Finding | Action | Savings Impact | Effort | Dependencies |
|---------|--------|---------------|--------|--------------|
{Right-size instances, implement auto-scaling, schedule non-prod, add Graviton}

### Strategic (1-3 months)
| Finding | Action | Savings Impact | Effort | Dependencies |
|---------|--------|---------------|--------|--------------|
{Savings Plans commitment, serverless migration, architecture optimization}

## Next Steps
{Top 5 concrete cost-saving actions the team should take this week}
```

## Step 11: Offer follow-up

After delivering the report, offer:

> Would you like me to:
> - Generate IaC changes for quick-win optimizations?
> - Model Savings Plans vs Reserved Instances for your usage?
> - Design a scheduled scaling policy for non-production?
> - Create a FinOps tagging strategy with cost allocation tags?
> - Estimate cost for an architectural alternative (serverless, containers)?
> - Implement S3 lifecycle policies for identified buckets?

## Calibration Guidance

- A workload with auto-scaling, lifecycle policies, VPC endpoints, and cost allocation tags is MATURE — focus on advanced optimizations (Savings Plans, Spot, architectural alternatives)
- Every finding MUST have code evidence — don't flag "over-provisioned" without checking actual configurations
- Savings estimates should be relative (% reduction) when absolute spend is unknown
- Always assess trade-offs: cost optimization MUST NOT introduce reliability risks without explicit acknowledgment
- Flag when a cost optimization would degrade the reliability or performance posture
- "Cannot Determine" is valid when you can't assess actual utilization from IaC alone (recommend Compute Optimizer, Cost Explorer)
- Acknowledge good cost practices before listing waste
