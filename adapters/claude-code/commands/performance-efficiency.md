Evaluate a workload's performance efficiency by analyzing resource selection, scaling configs, caching patterns, and data access patterns in the codebase against the Well-Architected Performance Efficiency pillar.

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for performance efficiency? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Performance requirements** (latency targets, throughput needs)
> - **Known bottlenecks** (optional)

If already in a codebase, proceed directly.

## Step 2: Compute Selection Discovery

Analyze compute configurations:

- EC2 instance types/families
- Lambda memory and timeout
- ECS/Fargate CPU and memory
- Container base images
- Graviton vs x86 selection

Flag:
- Lambda with default 128MB memory
- Lambda timeout ≥ caller's timeout
- General-purpose instances for compute/memory-heavy workloads
- x86 where Graviton provides better price-performance

## Step 3: Storage and Database Performance Discovery

Analyze database and storage:

- Database engine selection vs access patterns
- Read replicas, connection pooling (RDS Proxy)
- DynamoDB table design (partition keys, GSIs)
- Caching layers (ElastiCache, DAX, CloudFront)
- EBS volume types and IOPS
- Application query patterns (N+1, unbounded queries)

Flag: no connection pooling in serverless→RDS, missing caching for read-heavy data, DynamoDB hot partitions, N+1 queries, gp2 volumes.

## Step 4: Networking and Content Delivery

Analyze:

- CloudFront distributions (or absence)
- API Gateway caching
- VPC endpoints, compression settings
- Connection settings (keep-alive, HTTP/2)

Flag: no CDN for static content, no API caching, no compression, missing VPC endpoints.

## Step 5: Scaling and Application Patterns

Analyze:

- Auto Scaling policies and metrics (CPU-only vs custom)
- Provisioned concurrency for latency-sensitive Lambda
- Synchronous vs async processing
- Batch opportunities, pagination implementations
- Cold start patterns (Lambda initialization)

Flag: CPU-only scaling, no provisioned concurrency on latency-critical functions, sync processing that could be async, offset pagination on large datasets.

## Step 6: Evaluate against WA Framework questions

Every assessment MUST include: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

- **PERF 1 — Resource selection**: instance types, compute families, Graviton
- **PERF 2 — Compute solution**: Lambda vs ECS vs EC2, memory/CPU configs
- **PERF 3 — Storage solution**: storage types, IOPS, tiering
- **PERF 4 — Database solution**: engine selection, replicas, pooling, caching
- **PERF 5 — Networking**: CloudFront, VPC endpoints, compression
- **PERF 7 — Monitoring**: latency percentiles, throughput, performance alarms
- **PERF 8 — Tradeoffs**: caching, async, eventual consistency

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

## Step 8: Produce findings

Structure:

- Executive Summary (date, packages analyzed, performance target, findings count, performance maturity 1-5)
- Performance Scorecard (Compute Selection, Storage & Database, Networking & CDN, Scaling & Elasticity, Application Patterns, Monitoring — each scored 1-5)
- Critical and High Risk Findings (ID, domain, title, evidence file:line, performance impact, recommendation, expected improvement, effort, AWS services)
- Medium/Low Findings
- Optimization Opportunities table (resource, current config, recommended, expected improvement, evidence)
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- Next Steps (top 5 actions)

## Calibration

- Every finding MUST have code evidence
- Estimate improvements where possible ("connection pooling typically reduces p99 by 30-50%")
- Always assess trade-offs: performance optimizations may increase cost/complexity
- "Cannot Determine" is valid when actual metrics are needed
- Acknowledge good performance practices before listing issues
