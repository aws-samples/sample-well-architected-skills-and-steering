---
name: performance-efficiency
description: Evaluate a workload's performance efficiency by analyzing resource selection, scaling configs, caching patterns, and data access patterns in the codebase against the Well-Architected Performance Efficiency pillar.
version: 2.0.0
---

# Performance Efficiency Assessment

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for performance efficiency? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Performance requirements** (latency targets, throughput needs, concurrent users)
> - **Known bottlenecks** (optional — areas you suspect are underperforming)

If context is already provided or you are in a codebase, proceed directly.

## Step 2: Compute Selection Discovery

Analyze compute resource selection and configuration.

You MUST examine:
- EC2 instance types and families (general purpose vs compute/memory/storage optimized)
- Lambda memory and timeout configurations
- ECS/Fargate task CPU and memory allocations
- Container base images (Alpine, distroless, full OS)
- Graviton (ARM) vs x86 architecture selection
- Provisioned concurrency configurations (Lambda)
- Batch vs real-time processing selection

For each compute resource, document:
- File path and line numbers
- Instance type/size and why it may or may not fit
- Memory/CPU ratio relative to workload type
- Cold start implications (Lambda, Fargate)

You MUST flag:
- Lambda with default 128MB memory (likely under-provisioned, slower execution)
- Lambda timeout ≥ caller's timeout (will always appear as timeout to caller)
- General-purpose instances for compute-heavy or memory-heavy workloads
- x86 where Graviton provides better price-performance
- Over-provisioned Fargate tasks (large CPU/memory for simple workloads)

## Step 3: Storage and Database Performance Discovery

Analyze storage and database configurations for performance.

You MUST examine:
- Database engine selection vs access patterns
- Read replica configurations
- Connection pooling (RDS Proxy, application-level pooling)
- DynamoDB table design (partition key distribution, GSI configurations)
- Caching layers (ElastiCache, DAX, CloudFront)
- S3 access patterns and request rate considerations
- EBS volume types and IOPS provisioning
- Database query patterns in application code (N+1 queries, missing indexes)

You MUST flag:
- Relational database for key-value access patterns (DynamoDB would be better)
- No connection pooling in serverless → RDS architecture
- DynamoDB with hot partition patterns (poor key design)
- No caching layer for read-heavy, low-change data
- gp2 EBS volumes (gp3 offers better baseline performance at lower cost)
- Missing DAX for DynamoDB read-heavy patterns
- Application code with N+1 query patterns or unbounded queries

## Step 4: Networking and Content Delivery Discovery

Analyze networking configurations for performance.

You MUST examine:
- CloudFront distributions (or absence for static/API content)
- API Gateway caching configurations
- VPC endpoint usage (reduced latency vs internet path)
- Placement groups for latency-sensitive workloads
- Global Accelerator configurations
- Connection settings (keep-alive, HTTP/2, compression)
- DNS resolution (Route 53 latency-based routing)

You MUST flag:
- No CDN for static content delivery
- API responses without compression (gzip/brotli)
- No API Gateway caching for cacheable GET endpoints
- Cross-region calls that could use local endpoints
- Missing VPC endpoints (adds NAT Gateway latency)

## Step 5: Scaling and Elasticity Discovery

Analyze scaling configurations and responsiveness.

You MUST examine:
- Auto Scaling policies (target tracking vs step scaling)
- Scaling metrics used (CPU only vs custom metrics like queue depth, latency)
- Cooldown periods and scaling speed
- Scheduled scaling for predictable patterns
- Provisioned concurrency for latency-sensitive Lambda functions
- Database auto-scaling (Aurora, DynamoDB)
- Scaling bottlenecks (connection limits, DNS propagation, cold starts)

You MUST flag:
- CPU-only scaling metrics (ignores memory, queue depth, latency)
- Long cooldown periods that prevent rapid response
- No provisioned concurrency on latency-sensitive Lambda functions
- Fixed-capacity databases with variable load patterns
- Scaling max too low for expected peak

## Step 6: Application Performance Pattern Discovery

Analyze application code for performance patterns.

You MUST examine:
- Synchronous vs asynchronous processing patterns
- Batch processing opportunities (batch writes, bulk APIs)
- Pagination implementations (cursor vs offset)
- Data serialization formats (JSON vs binary protocols)
- Caching usage in application code (local caches, distributed caches)
- Warm-up and connection reuse patterns (Lambda handler outside handler)
- Parallel vs sequential processing of independent operations

You MUST flag:
- Synchronous processing that could be async (SQS, EventBridge)
- Sequential API calls that could be parallelized
- Offset-based pagination on large datasets (cursor-based is O(1))
- Lambda cold start patterns (initializing in handler instead of module scope)
- Missing batch operations (individual PutItem instead of BatchWriteItem)
- Unbounded data retrieval without pagination

## Step 7: Monitoring and Optimization Practices

Analyze performance monitoring configurations.

You MUST examine:
- CloudWatch metrics and alarms (latency percentiles, errors)
- X-Ray/OpenTelemetry tracing configuration
- Custom metrics for performance-sensitive operations
- Performance budgets and alerts
- Dashboard definitions tracking latency/throughput

You MUST flag:
- No latency monitoring at p95/p99 level
- No distributed tracing across service boundaries
- No performance alarms (only error alarms)
- Average-only metrics (hides tail latency issues)

## Step 8: Evaluate against WA Framework questions

For each question, provide: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

### PERF 1 — How do you select appropriate cloud resources?
- Evidence: instance types, compute families, storage tiers, justification

### PERF 2 — How do you select your compute solution?
- Evidence: Lambda vs ECS vs EC2 selection, memory/CPU configs, cold start handling

### PERF 3 — How do you select your storage solution?
- Evidence: storage types matching access patterns, IOPS configs, tiering

### PERF 4 — How do you select your database solution?
- Evidence: engine selection, read replicas, connection pooling, caching layers

### PERF 5 — How do you configure your networking solution?
- Evidence: CloudFront, VPC endpoints, placement groups, compression

### PERF 6 — How do you evolve your workload to take advantage of new releases?
- Evidence: runtime versions, SDK versions, Graviton adoption, modern features

### PERF 7 — How do you monitor your resources to ensure they are performing?
- Evidence: latency metrics at percentiles, throughput tracking, performance alarms

### PERF 8 — How do you use tradeoffs to improve performance?
- Evidence: caching strategies, async patterns, eventual consistency choices

## Step 9: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor (slightly suboptimal, no user-visible effect) | Moderate (noticeable latency, degraded experience under load) | Severe (user-facing timeouts, dropped requests, SLA breach)

**Likelihood**: Low (only affects edge cases or extreme load) | Medium (affects normal peak load) | High (affects steady-state traffic)

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

## Step 10: Produce findings

```markdown
# Performance Efficiency Assessment: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Packages Analyzed**: {list}
- **Performance Target**: {latency/throughput targets if specified}
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Performance Maturity**: {1-5} — {one-line justification}

## Performance Scorecard
| Domain | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| Compute Selection | {score} | {strength} | {gap} |
| Storage & Database | {score} | {strength} | {gap} |
| Networking & CDN | {score} | {strength} | {gap} |
| Scaling & Elasticity | {score} | {strength} | {gap} |
| Application Patterns | {score} | {strength} | {gap} |
| Monitoring | {score} | {strength} | {gap} |

## Critical and High Risk Findings
{For each: ID, domain, title, description, evidence (file:line), performance impact, recommendation, expected improvement, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Domain | Title | Recommendation}

## Optimization Opportunities
| Resource | Current Config | Recommended | Expected Improvement | Evidence |
|----------|---------------|-------------|---------------------|----------|
| {resource} | {current} | {optimized} | {improvement} | {file:line} |

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Performance Impact | Effort |
|---------|--------|-------------------|--------|
{Increase Lambda memory, enable compression, add gp3, enable keep-alive}

### Foundation (1-4 weeks)
| Finding | Action | Performance Impact | Effort | Dependencies |
|---------|--------|-------------------|--------|--------------|
{Add caching layer, implement connection pooling, CDN, async patterns}

### Strategic (1-3 months)
| Finding | Action | Performance Impact | Effort | Dependencies |
|---------|--------|-------------------|--------|--------------|
{Database migration, architecture rework, global distribution, Graviton migration}

## Next Steps
{Top 5 concrete performance actions the team should take this week}
```

## Step 11: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Design a caching strategy for a specific data flow?
> - Optimize Lambda memory/timeout configurations with power tuning approach?
> - Implement connection pooling for serverless → RDS?
> - Create a load testing plan with target scenarios?
> - Refactor synchronous code paths to async with queues?
> - Implement CloudFront distribution for your API/static content?

## Calibration Guidance

- A workload with appropriate instance types, caching, CDN, auto-scaling, and latency monitoring is MATURE — focus on tail latency, advanced caching, and architectural optimizations
- Every finding MUST have code evidence — don't flag "missing caching" without checking for existing cache layers
- Performance findings should estimate the improvement (e.g., "adding connection pooling typically reduces p99 latency by 30-50%")
- Always assess trade-offs: performance optimizations may increase cost or complexity
- "Cannot Determine" is valid when actual performance data is needed (e.g., whether an instance is CPU-bound requires CloudWatch metrics)
- Acknowledge good performance practices before listing issues
