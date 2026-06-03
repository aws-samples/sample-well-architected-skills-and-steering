---
name: sustainability-optimization
description: Assess a workload's environmental sustainability posture by analyzing resource utilization patterns, managed service adoption, data lifecycle configs, and compute efficiency in the codebase against the Well-Architected Sustainability pillar.
version: 2.0.0
---

# Sustainability Optimization Assessment

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for sustainability? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Sustainability goals** (optional — organizational carbon targets, reporting requirements)
> - **Known idle periods** (optional — off-hours, weekends, seasonal patterns)

If context is already provided or you are in a codebase, proceed directly.

## Step 2: Compute Efficiency Discovery

Analyze compute resource configurations for efficiency.

You MUST examine:
- Instance type selections (Graviton vs x86 — Graviton delivers up to 40% better price-performance per watt)
- Auto-scaling configurations (can resources scale to zero?)
- Lambda configurations (memory right-sizing, architecture arm64 vs x86_64)
- Container configurations (base image size, multi-stage builds, runtime efficiency)
- Batch processing configurations (scheduling, instance selection)
- Scheduled scaling (non-production environments, off-hours capacity)
- Serverless vs provisioned choices (Lambda/Fargate vs always-on EC2)

For each compute resource, document:
- File path and line numbers
- Architecture (arm64/x86_64)
- Scaling configuration (min/max, can reach zero)
- Whether always-on or event-driven

You MUST flag:
- x86_64 instances/Lambda where Graviton/arm64 is available and supported
- Always-on compute for variable or event-driven workloads (Lambda/Fargate would scale to zero)
- Non-production environments running 24/7 at production scale
- No scheduled scaling for environments with clear idle periods
- Provisioned concurrency on Lambda that isn't latency-critical
- Large container images that could use multi-stage builds or distroless

## Step 3: Data and Storage Efficiency Discovery

Analyze data management for sustainability.

You MUST examine:
- S3 lifecycle policies (transition to cheaper/more efficient tiers, expiration)
- S3 Intelligent-Tiering adoption
- CloudWatch log retention settings
- Data compression configurations (S3, API responses, database)
- Backup retention policies (excessive retention = wasted storage)
- S3 versioning with lifecycle rules for old versions
- DynamoDB TTL configurations
- Snapshot retention and cleanup automation

For each storage resource, document:
- File path and line numbers
- Lifecycle policy (present or absent)
- Retention settings
- Compression settings
- Access pattern alignment

You MUST flag:
- S3 buckets without lifecycle policies (data accumulates indefinitely)
- CloudWatch logs with "never expire" retention
- No TTL on DynamoDB tables with temporal data
- Uncompressed data storage where compression is feasible
- Backup retention > 90 days without compliance justification
- S3 versioning without version expiration rules
- No Intelligent-Tiering for buckets with unknown access patterns

## Step 4: Architecture Efficiency Discovery

Analyze architectural patterns for sustainability.

You MUST examine:
- Managed service usage vs self-managed (MSK vs self-managed Kafka, ElastiCache vs self-managed Redis)
- Event-driven vs polling patterns
- Batch processing vs real-time (can operations be batched?)
- Caching layers (reducing redundant computation)
- Data transfer patterns (processing close to data, minimizing cross-region/cross-AZ)
- API design efficiency (over-fetching, chatty APIs)
- Async processing for non-time-sensitive operations

You MUST flag:
- Self-managed infrastructure where managed alternatives exist (better utilization at scale)
- Polling patterns where event-driven would reduce idle compute
- Individual API calls where batch operations exist
- Missing caching causing redundant computation
- Chatty APIs causing excessive network round-trips

## Step 5: Development and Deployment Efficiency

Analyze CI/CD and development practices for sustainability.

You MUST examine:
- Container image optimization (multi-stage builds, layer caching, image size)
- CI/CD pipeline efficiency (caching, incremental builds, parallel execution)
- Artifact management (retention, cleanup)
- Test environment lifecycle (auto-teardown, TTL)
- Deployment strategy efficiency (minimal rollout for testing)

You MUST flag:
- Large Docker images without multi-stage builds
- No caching in CI/CD pipelines (rebuilding everything every time)
- Test environments without auto-teardown
- Redundant full deployments where incremental would work

## Step 6: Region and Hardware Efficiency

Analyze region and hardware choices.

You MUST examine:
- Region selection (carbon intensity varies by region)
- Graviton adoption across all resource types
- Instance generation (older generations are less efficient per operation)
- Storage tier selection efficiency

You MUST flag:
- Older generation instances (e.g., m4 instead of m7g, t2 instead of t4g)
- x86 selection where Graviton/ARM is supported by the workload runtime
- Resources in high-carbon regions without latency justification

## Step 7: Evaluate against WA Framework questions

For each question, provide: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

### SUS 1 — How do you select Regions to support your sustainability goals?
- Evidence: region configs, documentation on region selection rationale

### SUS 2 — How do you take advantage of user behavior patterns?
- Evidence: scale-to-zero configs, scheduled scaling, event-driven architecture patterns

### SUS 3 — How do you take advantage of software and architecture patterns?
- Evidence: managed services, async processing, batch operations, caching layers

### SUS 4 — How do you take advantage of data access and usage patterns?
- Evidence: lifecycle policies, compression, tiering, Intelligent-Tiering, TTL configs

### SUS 5 — How do your hardware management and usage patterns support your sustainability goals?
- Evidence: Graviton/arm64 usage, instance generation, right-sizing, managed services

### SUS 6 — How do your development and deployment processes support your sustainability goals?
- Evidence: multi-stage Docker builds, CI caching, incremental deployments, artifact cleanup

## Step 8: Impact Assessment

For each finding, assess:

**Resource Impact**: Low (minor efficiency gain) | Medium (significant resource reduction) | High (major resource elimination or efficiency improvement)

**Implementation Effort**: Low (config change) | Medium (some development needed) | High (architecture change)

Prioritize by: Impact / Effort ratio (highest first)

## Step 9: Produce findings

```markdown
# Sustainability Assessment: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Packages Analyzed**: {list}
- **Findings**: {X} High Impact, {Y} Medium Impact, {Z} Low Impact
- **Overall Sustainability Maturity**: {1-5} — {one-line justification}
- **Key Opportunities**: {top 3 highest-impact changes}

## Sustainability Scorecard
| Domain | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| Compute Efficiency | {score} | {strength} | {gap} |
| Data & Storage | {score} | {strength} | {gap} |
| Architecture Efficiency | {score} | {strength} | {gap} |
| Development & Deployment | {score} | {strength} | {gap} |
| Hardware & Region | {score} | {strength} | {gap} |

## High Impact Findings
{For each: ID, domain, title, description, evidence (file:line), resource impact, recommendation, effort, AWS services}

## Medium Impact Findings
{Same format, condensed}

## Low Impact Findings
{Summary table: ID | Domain | Title | Recommendation}

## Resource Efficiency Opportunities
| Resource | Current Config | Optimized Config | Efficiency Gain | Evidence |
|----------|---------------|-----------------|-----------------|----------|
| {resource} | {current} | {optimized} | {gain description} | {file:line} |

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Resource Impact | Effort |
|---------|--------|----------------|--------|
{Set log retention, add lifecycle policies, enable Intelligent-Tiering, schedule non-prod}

### Foundation (1-4 weeks)
| Finding | Action | Resource Impact | Effort | Dependencies |
|---------|--------|----------------|--------|--------------|
{Graviton migration, right-sizing, scale-to-zero, multi-stage Docker builds}

### Strategic (1-3 months)
| Finding | Action | Resource Impact | Effort | Dependencies |
|---------|--------|----------------|--------|--------------|
{Serverless migration, managed service adoption, event-driven architecture, region optimization}

## AWS Sustainability Tools
- **Customer Carbon Footprint Tool** — Track emissions in the AWS console
- **Compute Optimizer** — Right-size recommendations with Graviton suggestions
- **S3 Storage Lens** — Storage efficiency and access pattern insights
- **Trusted Advisor** — Idle resource detection

## Next Steps
{Top 5 concrete sustainability actions the team should take this week}
```

## Step 10: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Generate Graviton migration IaC for identified resources?
> - Design a scale-to-zero strategy for non-production environments?
> - Implement S3 lifecycle policies for identified buckets?
> - Create multi-stage Docker builds for container images?
> - Design an event-driven architecture to replace polling patterns?
> - Implement scheduled scaling for off-hours capacity reduction?

## Calibration Guidance

- A workload using Graviton, serverless, lifecycle policies, and managed services is MATURE — focus on advanced efficiencies (data locality, batch aggregation, development practices)
- Every finding MUST have code evidence — don't flag "missing lifecycle policy" without checking the IaC
- Sustainability findings should be framed positively (resource efficiency gains) not negatively
- Always note when a sustainability improvement also reduces cost (double benefit)
- "Cannot Determine" is valid for utilization data that requires CloudWatch metrics (recommend Compute Optimizer)
- Don't recommend region changes without considering latency requirements and data residency
- Acknowledge existing sustainability practices before listing gaps
