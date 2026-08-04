# Performance Efficiency Pillar — Deep-Dive Discovery Playbook

When wa-review is scoped to the Performance Efficiency pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

## Compute Selection

Examine:
- EC2 instance types and families (general purpose vs compute/memory/storage optimized)
- Lambda memory and timeout configurations
- ECS/Fargate task CPU and memory allocations
- Container base images (Alpine, distroless, full OS)
- Graviton (ARM) vs x86 architecture selection
- Provisioned concurrency configurations (Lambda)
- Batch vs real-time processing selection

Flag:
- Lambda with default 128MB memory (under-provisioned, slower execution)
- Lambda timeout >= caller's timeout (always appears as timeout)
- General-purpose instances for compute-heavy or memory-heavy workloads
- x86 where Graviton provides better price-performance
- Over-provisioned Fargate tasks for simple workloads

## Storage and Database Performance

Examine:
- Database engine selection vs access patterns
- Read replica configurations
- Connection pooling (RDS Proxy, application-level)
- DynamoDB table design (partition key distribution, GSI configs)
- Caching layers (ElastiCache, DAX, CloudFront)
- S3 access patterns and request rate
- EBS volume types and IOPS provisioning
- Application code query patterns (N+1 queries, missing indexes)

Flag:
- Relational database for key-value access patterns
- No connection pooling in serverless → RDS architecture
- DynamoDB with hot partition patterns (poor key design)
- No caching layer for read-heavy, low-change data
- gp2 EBS volumes (gp3 has better baseline performance)
- Application code with N+1 query patterns

## Networking and Content Delivery

Examine:
- CloudFront distributions (or absence)
- API Gateway caching configurations
- VPC endpoint usage (reduced latency vs internet path)
- Placement groups for latency-sensitive workloads
- Connection settings (keep-alive, HTTP/2, compression)
- DNS resolution (Route 53 latency-based routing)

Flag:
- No CDN for static content delivery
- API responses without compression (gzip/brotli)
- No API Gateway caching for cacheable GET endpoints
- Cross-region calls that could use local endpoints
- Missing VPC endpoints (adds NAT Gateway latency)

## Scaling and Elasticity

Examine:
- Auto Scaling policies (target tracking vs step)
- Scaling metrics (CPU only vs custom like queue depth, latency)
- Cooldown periods and scaling speed
- Scheduled scaling for predictable patterns
- Provisioned concurrency for latency-sensitive Lambda
- Database auto-scaling (Aurora, DynamoDB)
- Scaling bottlenecks (connection limits, cold starts)

Flag:
- CPU-only scaling metrics (ignores memory, queue depth, latency)
- Long cooldown periods preventing rapid response
- No provisioned concurrency on latency-sensitive Lambda
- Fixed-capacity databases with variable load
- Scaling max too low for expected peak

## Application Performance Patterns

Examine:
- Synchronous vs asynchronous processing patterns
- Batch processing opportunities (batch writes, bulk APIs)
- Pagination implementations (cursor vs offset)
- Data serialization formats (JSON vs binary protocols)
- Caching in application code (local, distributed)
- Warm-up and connection reuse (Lambda init outside handler)
- Parallel vs sequential processing of independent operations

Flag:
- Synchronous processing that could be async (SQS, EventBridge)
- Sequential API calls that could be parallelized
- Offset-based pagination on large datasets
- Lambda cold start patterns (init in handler instead of module scope)
- Missing batch operations (individual PutItem instead of BatchWriteItem)
- Unbounded data retrieval without pagination

## Performance-Specific Report Format

When producing a pillar-scoped performance report, include:
- **Performance Scorecard** with 6 domains: Compute Selection, Storage & Database, Networking & CDN, Scaling & Elasticity, Application Patterns, Monitoring
- **Optimization Opportunities** table: Resource | Current Config | Recommended | Expected Improvement | Evidence
- Performance findings should estimate improvement where possible

## Calibration

- "Cannot Determine" is valid when actual performance data is needed (e.g., whether an instance is CPU-bound requires CloudWatch metrics)
- Always assess trade-offs: performance optimizations may increase cost or complexity
