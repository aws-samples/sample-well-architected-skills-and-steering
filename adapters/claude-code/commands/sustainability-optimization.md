Assess a workload's environmental sustainability posture by analyzing resource utilization patterns, managed service adoption, data lifecycle configs, and compute efficiency in the codebase against the Well-Architected Sustainability pillar.

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for sustainability? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Sustainability goals** (optional — carbon targets, reporting requirements)
> - **Known idle periods** (optional — off-hours, weekends, seasonal)

If already in a codebase, proceed directly.

## Step 2: Compute Efficiency Discovery

Analyze compute for efficiency:

- Instance types (Graviton/arm64 vs x86_64)
- Auto-scaling configs (can scale to zero?)
- Lambda architecture (arm64 vs x86_64)
- Container images (size, multi-stage builds)
- Serverless vs always-on choices
- Scheduled scaling for non-production

Flag:
- x86_64 where Graviton/arm64 is available
- Always-on compute for variable/event-driven workloads
- Non-production running 24/7 at production scale
- No scheduled scaling for clear idle periods
- Large container images without multi-stage builds

## Step 3: Data and Storage Efficiency

Analyze data management:

- S3 lifecycle policies, Intelligent-Tiering
- CloudWatch log retention
- Data compression configs
- DynamoDB TTL configs
- Backup retention policies
- S3 versioning with version expiration

Flag:
- S3 without lifecycle policies
- "Never expire" log retention
- No TTL on temporal DynamoDB data
- Uncompressed storage
- Backup retention > 90 days without compliance justification

## Step 4: Architecture and Development Efficiency

Analyze:

- Managed services vs self-managed
- Event-driven vs polling patterns
- Batch vs real-time processing
- Caching layers
- CI/CD pipeline efficiency (caching, incremental builds)
- Container optimization (multi-stage Docker)
- Instance generation (older less efficient gens)

Flag: self-managed infra where managed exists, polling where event-driven would work, large Docker images, older generation instances.

## Step 5: Evaluate against WA Framework questions

Every assessment MUST include: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

- **SUS 1 — Region selection**: carbon intensity consideration
- **SUS 2 — User behavior patterns**: scale-to-zero, scheduled scaling, event-driven
- **SUS 3 — Software/architecture patterns**: managed services, async, batch, caching
- **SUS 4 — Data patterns**: lifecycle, compression, tiering, TTL
- **SUS 5 — Hardware patterns**: Graviton/arm64, instance generation, right-sizing
- **SUS 6 — Development/deployment**: multi-stage builds, CI caching, incremental deploys

## Step 6: Impact Assessment

Prioritize by Resource Impact / Implementation Effort ratio:

- **High Impact**: major resource elimination or efficiency improvement
- **Medium Impact**: significant resource reduction
- **Low Impact**: minor efficiency gain

## Step 7: Produce findings

Structure:

- Executive Summary (date, packages analyzed, findings count, sustainability maturity 1-5, top 3 opportunities)
- Sustainability Scorecard (Compute Efficiency, Data & Storage, Architecture Efficiency, Development & Deployment, Hardware & Region — each scored 1-5)
- High Impact Findings (ID, domain, title, evidence file:line, resource impact, recommendation, effort, AWS services)
- Medium/Low Impact Findings
- Resource Efficiency Opportunities table (resource, current config, optimized, efficiency gain, evidence)
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- AWS Sustainability Tools reference
- Next Steps (top 5 actions)

## Calibration

- Every finding MUST have code evidence
- Frame findings positively (efficiency gains not criticism)
- Note when sustainability improvements also reduce cost (double benefit)
- Don't recommend region changes without considering latency/data residency
- "Cannot Determine" is valid for utilization data requiring CloudWatch
- Acknowledge existing sustainability practices before gaps
