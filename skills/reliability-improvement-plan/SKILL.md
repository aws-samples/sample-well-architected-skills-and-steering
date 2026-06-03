---
name: reliability-improvement-plan
description: Identify single points of failure, assess recovery capabilities, and produce a prioritized remediation plan by analyzing IaC, scaling configs, and resilience patterns in the codebase.
version: 2.0.0
---

# Reliability Improvement Plan

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for reliability? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Availability target** (99.9%, 99.95%, 99.99%, etc.)
> - **Recovery objectives** (RTO and RPO if defined)
> - **Past incidents** (optional — recent outages or near-misses)

If context is already provided or you are in a codebase with IaC, proceed directly.

## Step 2: Fault Tolerance Discovery

Analyze infrastructure for single points of failure.

You MUST examine:
- Compute deployments (AZ distribution, instance count, ASG configs)
- Database configurations (Multi-AZ, read replicas, cluster topology)
- Cache configurations (cluster mode, replica counts, failover)
- Load balancer configurations (cross-zone, health checks, target groups)
- NAT Gateway placement (single vs per-AZ)
- DNS configurations (Route 53 health checks, failover routing)
- Queue and messaging configs (DLQ, redrive policies)
- Storage redundancy (S3 replication, EBS snapshots, EFS)

For each component, document:
- File path and line numbers
- Current redundancy level (single-AZ, multi-AZ, multi-region)
- Failure blast radius
- Failover mechanism (automatic, manual, none)

You MUST flag as HIGH RISK:
- Single-AZ database deployments for production workloads
- Compute without auto-scaling (fixed instance count)
- No health checks on load-balanced targets
- Single NAT Gateway serving multiple AZs
- Stateful services without replication
- Missing DLQ on async invocations (Lambda, SQS, EventBridge)
- No circuit breaker or timeout on external service calls

## Step 3: Recovery Capability Discovery

Analyze backup and recovery configurations.

You MUST examine:
- AWS Backup plans and rules
- RDS automated backup settings (retention, PITR)
- S3 versioning and replication rules
- DynamoDB PITR and backup settings
- EBS snapshot configurations
- Cross-region replication rules
- Disaster recovery configurations (pilot light, warm standby resources)

For each stateful resource, document:
- Backup frequency and retention
- Recovery point capability (RPO)
- Recovery time estimate (RTO)
- Whether recovery has been tested (look for DR runbooks, FIS experiments)

You MUST flag as HIGH RISK:
- Stateful resources with no backup configuration
- Backup retention < 7 days for production data
- No cross-region backup for critical data
- No evidence of recovery testing (no FIS experiments, no DR runbooks)

## Step 4: Scaling and Capacity Discovery

Analyze scaling and capacity configurations.

You MUST examine:
- Auto Scaling Group configurations (min, max, desired, scaling policies)
- ECS service scaling (target tracking, step scaling)
- Lambda concurrency settings (reserved, provisioned)
- DynamoDB capacity mode (on-demand vs provisioned, auto-scaling)
- SQS/Kinesis throughput configurations
- API Gateway throttling settings
- Service quota usage and alarms

You MUST flag as HIGH RISK:
- Compute without auto-scaling policies
- ASG with min = max (no scaling headroom)
- No service quota alarms
- Lambda without reserved concurrency on critical functions
- No load shedding or throttling for overload scenarios

## Step 5: Resilience Pattern Discovery

Analyze application code for resilience patterns.

You MUST examine:
- Retry configurations (SDK clients, custom retry logic)
- Timeout settings (HTTP clients, database connections, Lambda timeout)
- Circuit breaker implementations
- Fallback logic and graceful degradation patterns
- Idempotency handling (idempotency keys, deduplication)
- Health check endpoint implementations
- Connection pooling configurations

For each external integration, document:
- Timeout configured (or missing)
- Retry policy (exponential backoff, max attempts, jitter)
- Circuit breaker (present or absent)
- Fallback behavior on failure

You MUST flag as HIGH RISK:
- External service calls without timeouts
- No retry logic on SDK clients
- Missing idempotency on event-driven processing
- Health checks that don't verify actual functionality (shallow checks)
- Lambda timeout ≥ API Gateway timeout (will always timeout to caller)

## Step 6: Change Management Discovery

Analyze deployment safety configurations.

You MUST examine:
- Deployment strategies (canary, blue/green, rolling, all-at-once)
- Health check gating on deployments
- Automated rollback configurations (alarm-based)
- Database migration strategies (backward-compatible, blue/green schema)
- Feature flag usage

You MUST flag as HIGH RISK:
- All-at-once deployment to production
- No automated rollback on health check failure
- Database migrations that aren't backward-compatible
- No pre-production environment that mirrors production topology

## Step 7: Evaluate against WA Framework questions

For each question, provide: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

### REL 1 — How do you manage service quotas and constraints?
- Evidence: quota alarms, SDK retry configs, throttling handling code

### REL 2 — How do you plan your network topology?
- Evidence: subnet definitions, AZ distribution, NAT redundancy

### REL 3 — How does your system adapt to changes in demand?
- Evidence: ASG configs, scaling policies, Lambda concurrency, DynamoDB capacity mode

### REL 4 — How do you design interactions in a distributed system to prevent failures?
- Evidence: retry logic, timeout configs, SQS decoupling, idempotency tokens

### REL 5 — How do you design interactions to mitigate or withstand failures?
- Evidence: circuit breaker code, fallback paths, bulkhead patterns, load shedding

### REL 6 — How do you monitor workload resources?
- Evidence: health check endpoints, alarm definitions, composite alarms, dashboard configs

### REL 7 — How do you design your workload to adapt to changes in demand?
- Evidence: scaling policy metrics, scheduled scaling, predictive scaling configs

### REL 8 — How do you implement change?
- Evidence: deployment configs, health check gating, rollback trigger alarms

### REL 9 — How do you back up data?
- Evidence: AWS Backup plans, PITR settings, replication rules, snapshot configs

### REL 10 — How do you use fault isolation to protect your workload?
- Evidence: AZ distribution, cell-based patterns, shuffle sharding, isolation boundaries

### REL 11 — How do you design your workload to withstand component failures?
- Evidence: multi-AZ configs, failover policies, stateless design, health-based routing

### REL 12 — How do you test reliability?
- Evidence: FIS experiments, failure injection code, game day runbooks, DR test scripts

### REL 13 — How do you plan for disaster recovery (DR)?
- Evidence: cross-region resources, DR automation, backup restore procedures, RTO/RPO docs

## Step 8: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor (brief degradation, automatic recovery) | Moderate (extended outage for subset of users, manual intervention needed) | Severe (full outage, data loss, cannot recover within RTO)

**Likelihood**: Low (requires multiple simultaneous failures) | Medium (single component failure could trigger) | High (normal operational event could trigger, no redundancy)

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

## Step 9: Produce the plan

```markdown
# Reliability Improvement Plan: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Availability Target**: {target}
- **Packages Analyzed**: {list}
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Reliability Maturity**: {1-5} — {one-line justification}

## Reliability Scorecard
| Domain | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| Fault Tolerance | {score} | {strength} | {gap} |
| Recovery & Backup | {score} | {strength} | {gap} |
| Scaling & Capacity | {score} | {strength} | {gap} |
| Resilience Patterns | {score} | {strength} | {gap} |
| Change Management | {score} | {strength} | {gap} |
| Testing & Validation | {score} | {strength} | {gap} |

## Single Points of Failure
| Component | Evidence | Failure Impact | Current Mitigation | Risk Level |
|-----------|----------|---------------|-------------------|------------|
| {component} | {file:line} | {impact} | {mitigation or "None"} | {Critical/High/Medium/Low} |

## Critical and High Risk Findings
{For each: ID, domain, title, description, evidence (file:line), impact assessment, recommendation, effort, AWS services}

## Medium and Low Risk Findings
{Condensed format}

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Impact | Effort |
|---------|--------|--------|--------|
{Enable Multi-AZ, add health checks, configure DLQs, add timeouts}

### Foundation (1-4 weeks)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Auto-scaling, circuit breakers, backup configs, deployment safety}

### Strategic (1-3 months)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Multi-region DR, chaos engineering, cell-based architecture}

## Testing Plan
| Test | Validates | Frequency | AWS Service | Evidence Exists |
|------|-----------|-----------|-------------|-----------------|
| AZ failover | Compute survives AZ loss | Monthly | FIS | {Yes/No} |
| Database failover | RDS failover < 60s | Quarterly | FIS | {Yes/No} |
| Load test | Handles 2x peak | Before releases | Load Testing | {Yes/No} |
| Backup restore | RPO met, data recoverable | Monthly | AWS Backup | {Yes/No} |
| Deployment rollback | Bad deploy reverted < 5 min | Every deploy | CodeDeploy | {Yes/No} |

## Next Steps
{Top 5 concrete reliability actions the team should take this week}
```

## Step 10: Offer follow-up

After delivering the plan, offer:

> Would you like me to:
> - Design multi-AZ architecture for a specific component?
> - Generate FIS experiment templates for chaos engineering?
> - Implement circuit breaker patterns for service dependencies?
> - Create backup and DR IaC for stateful resources?
> - Design a deployment safety configuration with automated rollback?

## Calibration Guidance

- A workload with Multi-AZ, auto-scaling, health checks, automated rollback, and backups is MATURE — focus on advanced testing (chaos engineering, DR drills, game days)
- Every finding MUST have code evidence — don't flag "missing Multi-AZ" without checking the IaC
- For data pipelines: prioritize data durability over compute availability — message loss is worse than processing delay
- Match expectations to availability target: 99.9% doesn't require multi-region, 99.99% does
- "Cannot Determine" is valid for operational aspects not visible in code (e.g., whether DR drills are actually run)
- Acknowledge existing reliability patterns prominently before listing gaps
