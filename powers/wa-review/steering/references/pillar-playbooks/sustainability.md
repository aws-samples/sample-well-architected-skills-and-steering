# Sustainability Pillar — Deep-Dive Discovery Playbook

When wa-review is scoped to the Sustainability pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

## Compute Efficiency

Examine:
- Instance type selections (Graviton vs x86 — up to 40% better price-performance per watt)
- Auto-scaling configs (can resources scale to zero?)
- Lambda configs (memory right-sizing, arm64 vs x86_64)
- Container configs (base image size, multi-stage builds)
- Scheduled scaling (non-production, off-hours capacity)
- Serverless vs provisioned choices (Lambda/Fargate vs always-on EC2)

Flag:
- x86_64 where Graviton/arm64 is available and supported
- Always-on compute for variable or event-driven workloads
- Non-production environments running 24/7 at production scale
- No scheduled scaling for environments with clear idle periods
- Provisioned concurrency on Lambda that isn't latency-critical
- Large container images without multi-stage builds

## Data and Storage Efficiency

Examine:
- S3 lifecycle policies (transition to efficient tiers, expiration)
- S3 Intelligent-Tiering adoption
- CloudWatch log retention settings
- Data compression configurations
- Backup retention policies (excessive retention = wasted storage)
- S3 versioning with lifecycle rules for old versions
- DynamoDB TTL configurations
- Snapshot retention and cleanup automation

Flag:
- S3 buckets without lifecycle policies (data accumulates indefinitely)
- CloudWatch logs with "never expire" retention
- No TTL on DynamoDB tables with temporal data
- Uncompressed data storage where compression is feasible
- Backup retention > 90 days without compliance justification
- No Intelligent-Tiering for buckets with unknown access patterns

## Architecture Efficiency

Examine:
- Managed service usage vs self-managed (MSK vs Kafka, ElastiCache vs Redis)
- Event-driven vs polling patterns
- Batch processing vs real-time (can operations be batched?)
- Caching layers (reducing redundant computation)
- Data transfer patterns (processing close to data)
- API design efficiency (over-fetching, chatty APIs)
- Async processing for non-time-sensitive operations

Flag:
- Self-managed infrastructure where managed alternatives exist
- Polling patterns where event-driven would reduce idle compute
- Individual API calls where batch operations exist
- Missing caching causing redundant computation
- Chatty APIs causing excessive network round-trips

## Development and Deployment Efficiency

Examine:
- Container image optimization (multi-stage builds, layer caching, image size)
- CI/CD pipeline efficiency (caching, incremental builds, parallel execution)
- Artifact management (retention, cleanup)
- Test environment lifecycle (auto-teardown, TTL)
- Deployment strategy efficiency (minimal rollout for testing)

Flag:
- Large Docker images without multi-stage builds
- No caching in CI/CD pipelines
- Test environments without auto-teardown
- Redundant full deployments where incremental would work

## Region and Hardware

Examine:
- Region selection (carbon intensity varies by region)
- Graviton adoption across all resource types
- Instance generation (older generations less efficient)
- Storage tier selection efficiency

Flag:
- Older generation instances (m4 instead of m7g, t2 instead of t4g)
- Resources in high-carbon regions without latency justification

## Sustainability-Specific Report Format

When producing a pillar-scoped sustainability report, include:
- **Sustainability Scorecard** with 5 domains: Compute Efficiency, Data & Storage, Architecture Efficiency, Development & Deployment, Hardware & Region
- **Resource Efficiency Opportunities** table: Resource | Current | Optimized | Efficiency Gain
- Note when sustainability improvements also reduce cost (double benefit)
- Reference AWS sustainability tools: Customer Carbon Footprint Tool, Compute Optimizer, S3 Storage Lens

## Calibration

- Frame findings positively (resource efficiency gains, not blame)
- Don't recommend region changes without considering latency and data residency
- "Cannot Determine" is valid for actual utilization data (recommend Compute Optimizer)
