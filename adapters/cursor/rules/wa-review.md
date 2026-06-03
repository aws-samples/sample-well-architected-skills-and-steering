---
description: Run a full Well-Architected Framework review when the user asks for an architecture review, WA assessment, or mentions "Well-Architected review". Analyzes code, IaC, and configurations to produce evidence-backed findings.
globs:
alwaysApply: false
---

# Well-Architected Review Skill

When the user requests a WA review, follow these steps:

## Step 1: Define scope

Ask for: workload name, code packages/directories to analyze, business criticality (critical/high/standard/low), and pain points.

If you are already in a codebase with IaC, skip the prompt and proceed with discovery.

Determine if a specialized WA Lens applies (Serverless, SaaS, Data Analytics, ML, IoT, Containers, Games, Financial Services, Healthcare). If obvious from code, note it.

## Step 2: Infrastructure Discovery

Analyze ALL infrastructure-as-code in the codebase:

- CDK, CloudFormation, Terraform, SAM, Serverless Framework
- CI/CD pipeline definitions
- Monitoring configurations (CloudWatch alarms, dashboards)
- Deployment configurations

For each resource, document: type, configuration, file path and line numbers, security/resilience/cost relevance.

Create a PlantUML architecture diagram showing components, data flows, and boundaries.

## Step 3: Application Architecture Discovery

Analyze application code for:

- Entry points (API handlers, event processors, scheduled tasks)
- Service communication patterns (sync/async, retries, timeouts, circuit breakers)
- Data access patterns and error handling
- Authentication/authorization logic
- Observability instrumentation

## Step 4: Evaluate each pillar with code evidence

For each pillar, assess against WA Framework questions. Every finding MUST include:

- **Status**: Implemented / Partially Implemented / Not Implemented / Cannot Determine
- **Evidence**: specific file paths and line numbers
- **Gaps**: what's missing
- **Risk**: what could go wrong

### Operational Excellence

- OPS 4 — Observability: structured logging, tracing, custom metrics
- OPS 5 — Reduce defects: automated testing, linting, staged deployments
- OPS 6 — Deployment risk: canary/blue-green, feature flags, rollback
- OPS 8 — Workload health: dashboards, composite alarms
- OPS 10 — Event management: event routing, automated remediation

### Security

- SEC 3 — Permissions: least privilege. Flag `"Action": "*"` or `"Resource": "*"` on mutating actions
- SEC 5 — Network: VPC design, security groups. Flag `0.0.0.0/0` on non-443/80 ports
- SEC 8 — Data at rest: encryption on ALL stores. Flag unencrypted storage
- SEC 9 — Data in transit: TLS enforcement. Flag TLS < 1.2
- SEC 2/3 — Identity: IAM roles, credential management. Flag hardcoded secrets

### Reliability

- REL 2 — Network topology: multi-AZ, subnet distribution
- REL 3 — Demand: auto-scaling, capacity modes. Flag compute without scaling
- REL 4 — Distributed interactions: retries, timeouts, idempotency
- REL 9 — Backup: automated backups, PITR. Flag stateful resources without backups
- REL 11 — Component failures: redundancy, failover
- REL 13 — DR: cross-region resources, DR automation

### Performance Efficiency

- PERF 1 — Resource selection: instance types, Graviton usage
- PERF 4 — Database: read replicas, connection pooling
- PERF 5 — Networking: CloudFront, VPC endpoints
- PERF 8 — Tradeoffs: caching, async patterns

### Cost Optimization

- COST 4 — Decommission: lifecycle policies. Flag "never expire" logs
- COST 5 — Service selection: pricing alignment. Flag over-provisioned resources
- COST 8 — Data transfer: VPC endpoints vs NAT Gateway

### Sustainability

- SUS 2 — Scale-to-zero, scheduled scaling
- SUS 4 — Data tiering, lifecycle, compression
- SUS 5 — Flag x86 where Graviton available

## Step 5: Risk Assessment

Assess each finding using Impact × Likelihood matrix:

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

Identify cross-pillar conflicts (security vs performance, cost vs reliability).

## Step 6: Output report

Structure:

- Executive Summary (date, workload, criticality, lens, findings count, overall maturity 1-5)
- Architecture Overview (PlantUML diagram)
- Pillar Scorecard (table: pillar, score 1-5, key strength, key gap)
- Critical and High Risk Findings (ID, pillar, title, evidence file:line, impact, recommendation, effort, AWS services)
- Medium Risk Findings (condensed)
- Low Risk Findings (summary table)
- Cross-Pillar Trade-offs
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- Next Steps (top 5 concrete actions)

## Calibration

- Mature workloads (multi-AZ, encryption, CI/CD, monitoring, scaling) should score 4+ — don't over-penalize
- Every finding MUST have code evidence — no generic recommendations
- "Cannot Determine" is valid when code alone is insufficient
- Acknowledge strengths before gaps
- Match expectations to business criticality tier
