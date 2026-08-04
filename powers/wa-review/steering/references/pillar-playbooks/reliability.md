# Reliability Pillar — Deep-Dive Discovery Playbook

When wa-review is scoped to the Reliability pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

## Fault Tolerance

Examine:
- Compute deployments (AZ distribution, instance count, ASG configs)
- Database configurations (Multi-AZ, read replicas, cluster topology)
- Cache configurations (cluster mode, replica counts, failover)
- Load balancer configurations (cross-zone, health checks, target groups)
- NAT Gateway placement (single vs per-AZ)
- DNS configurations (Route 53 health checks, failover routing)
- Queue and messaging (DLQ, redrive policies)
- Storage redundancy (S3 replication, EBS snapshots, EFS)

Flag HIGH RISK:
- Single-AZ database deployments for production
- Compute without auto-scaling (fixed instance count)
- No health checks on load-balanced targets
- Single NAT Gateway serving multiple AZs
- Stateful services without replication
- Missing DLQ on async invocations (Lambda, SQS, EventBridge)
- No circuit breaker or timeout on external calls

## Recovery Capabilities

Examine:
- AWS Backup plans and rules
- RDS automated backup settings (retention, PITR)
- S3 versioning and replication rules
- DynamoDB PITR and backup settings
- EBS snapshot configurations
- Cross-region replication rules
- Disaster recovery configs (pilot light, warm standby)

Flag HIGH RISK:
- Stateful resources with no backup configuration
- Backup retention < 7 days for production data
- No cross-region backup for critical data
- No evidence of recovery testing (no FIS experiments, no DR runbooks)

## Scaling and Capacity

Examine:
- Auto Scaling Group configs (min, max, desired, scaling policies)
- ECS service scaling (target tracking, step scaling)
- Lambda concurrency settings (reserved, provisioned)
- DynamoDB capacity mode (on-demand vs provisioned, auto-scaling)
- SQS/Kinesis throughput configurations
- API Gateway throttling settings
- Service quota usage and alarms

Flag HIGH RISK:
- Compute without auto-scaling policies
- ASG with min = max (no scaling headroom)
- No service quota alarms
- Lambda without reserved concurrency on critical functions
- No load shedding or throttling for overload

## Resilience Patterns

Examine:
- Retry configurations (SDK clients, custom retry logic)
- Timeout settings (HTTP clients, database connections, Lambda timeout)
- Circuit breaker implementations
- Fallback logic and graceful degradation
- Idempotency handling (idempotency keys, deduplication)
- Health check endpoint implementations
- Connection pooling configurations

Flag HIGH RISK:
- External service calls without timeouts
- No retry logic on SDK clients
- Missing idempotency on event-driven processing
- Health checks that don't verify actual functionality (shallow)
- Lambda timeout >= API Gateway timeout

## Change Management

Examine:
- Deployment strategies (canary, blue/green, rolling, all-at-once)
- Health check gating on deployments
- Automated rollback configurations (alarm-based)
- Database migration strategies (backward-compatible)
- Feature flag usage

Flag HIGH RISK:
- All-at-once deployment to production
- No automated rollback on health check failure
- Database migrations that aren't backward-compatible
- No pre-production environment mirroring production topology

## Reliability-Specific Report Format

When producing a pillar-scoped reliability report, include:
- **Reliability Scorecard** with 6 domains: Fault Tolerance, Recovery & Backup, Scaling & Capacity, Resilience Patterns, Change Management, Testing & Validation
- **Single Points of Failure** table: Component | Evidence | Failure Impact | Current Mitigation | Risk
- **Testing Plan** table: what reliability tests exist vs. what's missing (AZ failover, DB failover, load test, backup restore, rollback)

## Calibration

- Match expectations to availability target: 99.9% doesn't require multi-region, 99.99% does
- For data pipelines: prioritize data durability over compute availability
- "Cannot Determine" is valid for whether DR drills are actually run
