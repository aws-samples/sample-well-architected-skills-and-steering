Identify single points of failure, assess recovery capabilities, and produce a prioritized remediation plan by analyzing IaC, scaling configs, and resilience patterns in the codebase.

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for reliability? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Availability target** (99.9%, 99.95%, 99.99%, etc.)
> - **Recovery objectives** (RTO and RPO if defined)

If already in a codebase with IaC, proceed directly.

## Step 2: Fault Tolerance Discovery

Analyze infrastructure for single points of failure:

- Compute (AZ distribution, instance count, ASG configs)
- Databases (Multi-AZ, replicas, cluster topology)
- Caches (cluster mode, replica counts)
- Load balancers (cross-zone, health checks)
- NAT Gateways (single vs per-AZ)
- Queues (DLQ, redrive policies)

Flag as HIGH RISK:
- Single-AZ databases in production
- Compute without auto-scaling
- No health checks on load-balanced targets
- Single NAT Gateway for multiple AZs
- Missing DLQ on async invocations

## Step 3: Recovery Capability Discovery

Analyze backup and recovery:

- AWS Backup plans, RDS backup settings, PITR
- S3 versioning and replication
- Cross-region replication
- DR configurations

Flag: stateful resources without backups, retention < 7 days, no cross-region backup for critical data, no DR testing evidence.

## Step 4: Resilience Pattern Discovery

Analyze application code for resilience:

- Retry configurations (SDK clients, custom logic)
- Timeout settings (HTTP clients, DB connections, Lambda)
- Circuit breakers, fallbacks, graceful degradation
- Idempotency handling
- Health check implementations
- Connection pooling

Flag: external calls without timeouts, no retry logic, missing idempotency, shallow health checks, Lambda timeout ≥ API Gateway timeout.

## Step 5: Change Management Discovery

Analyze deployment safety:

- Deployment strategies (canary, blue/green, rolling)
- Health check gating, automated rollback
- Database migration approaches

Flag: all-at-once deployment, no rollback mechanism, non-backward-compatible migrations.

## Step 6: Evaluate against WA Framework questions

Every assessment MUST include: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

- **REL 1 — Quotas**: quota alarms, throttling handling
- **REL 2 — Network topology**: multi-AZ, subnet distribution
- **REL 3 — Demand adaptation**: auto-scaling, capacity modes
- **REL 4 — Prevent failures**: retries, timeouts, idempotency, decoupling
- **REL 5 — Withstand failures**: circuit breakers, fallbacks, load shedding
- **REL 8 — Implement change**: deployment safety, rollback
- **REL 9 — Backup data**: automated backups, PITR, replication
- **REL 11 — Component failures**: redundancy, failover, stateless
- **REL 12 — Test reliability**: FIS experiments, game days
- **REL 13 — DR**: cross-region, RTO/RPO, DR automation

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

## Step 8: Produce the plan

Structure:

- Executive Summary (date, availability target, packages analyzed, findings count, reliability maturity 1-5)
- Reliability Scorecard (Fault Tolerance, Recovery & Backup, Scaling, Resilience Patterns, Change Management, Testing — each scored 1-5)
- Single Points of Failure table (component, evidence, failure impact, current mitigation, risk level)
- Critical and High Risk Findings (ID, domain, title, evidence file:line, impact, recommendation, effort, AWS services)
- Medium/Low Findings
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- Testing Plan (AZ failover, DB failover, load test, backup restore, deployment rollback — with "Evidence Exists: Yes/No")
- Next Steps (top 5 actions)

## Calibration

- Every finding MUST have code evidence
- For data pipelines: data durability > compute availability
- Match expectations to availability target (99.9% ≠ multi-region, 99.99% = multi-region)
- "Cannot Determine" is valid for operational aspects not in code
- Acknowledge existing reliability patterns before gaps
