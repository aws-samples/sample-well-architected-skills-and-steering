---
name: wa-review
description: Perform a full AWS Well-Architected Framework review evaluating all 57 questions across 6 pillars by analyzing code, IaC, and configurations to produce evidence-backed findings with Eisenhower-prioritized remediation.
version: 2.1.0
---

# Well-Architected Review

## Step 1: Define the workload scope

Ask the user to describe the workload:

> What workload would you like me to review? Please share:
> - **Workload name** and brief description
> - **Code packages/directories** to analyze (IaC, application code, CI/CD configs)
> - **Business criticality** (critical, high, standard, low)
> - **Current pain points** (optional — anything you already know is problematic)

If the user has already provided architecture details or you are in a codebase with IaC, skip the prompt and proceed with discovery.

**IMPORTANT**: When no code or IaC is available to analyze (e.g., the user describes their architecture verbally), proceed with the review based on the information provided. Produce the full report using the architecture description as evidence. Mark findings where you cannot verify implementation details as "Based on description — verify in code." Do NOT ask for code if the user has already given you enough context to perform a meaningful review.

Determine if a specialized WA Lens applies:
- SaaS, Serverless, Data Analytics, Machine Learning, IoT, Containers, Games, Financial Services, Healthcare

If a lens is obvious from the code (e.g., Lambda-heavy → serverless), note it and apply lens-specific questions.

## Step 2: Infrastructure Discovery

Analyze all infrastructure-as-code and deployment configurations in the codebase.

You MUST examine:
- CDK code (TypeScript, Python, Java, Go)
- CloudFormation templates (YAML, JSON)
- Terraform configurations (.tf files)
- SAM/Serverless Framework templates
- CI/CD pipeline definitions (CodePipeline, GitHub Actions, etc.)
- Monitoring configurations (CloudWatch alarms, dashboards)
- Deployment configurations (CodeDeploy, ECS deployment settings)

For each infrastructure component, document:
- Resource type, logical name, and configuration
- File path and line numbers where defined
- Security-relevant configs (IAM, encryption, network)
- Resilience configs (multi-AZ, backups, scaling)
- Cost-relevant configs (instance types, capacity mode)

You MUST create an architecture diagram in PlantUML showing:
- All major components and their relationships
- Data flows and external dependencies
- Trust and network boundaries

## Step 3: Application Architecture Discovery

Analyze application code for architectural patterns:
- Entry points (API handlers, event processors, scheduled tasks)
- Service communication patterns (sync/async, retries, timeouts, circuit breakers)
- Data access patterns (queries, caching, connection management)
- Error handling and resilience patterns
- Authentication/authorization logic
- Observability instrumentation (logging, tracing, metrics)

## Step 4: Evaluate EVERY WA Framework question with code evidence

Assess the workload against ALL 57 questions in the Well-Architected Framework. For each question, provide:
- **Status**: "Implemented", "Partially Implemented", "Not Implemented", "Cannot Determine"
- **Evidence**: specific file paths and line numbers
- **Gaps**: what's missing or could be improved
- **Risk**: what could go wrong due to the gap

### Operational Excellence (11 questions)

**Organization:**
- **OPS 1 — How do you determine what your priorities are?** Look for: SLO/SLI definitions, business metrics in dashboards, health check endpoints, documented priorities. Evidence: README, dashboard definitions, alarm thresholds.
- **OPS 2 — How do you structure your organization to support your business outcomes?** Look for: CODEOWNERS files, package boundaries, team ownership docs, clear module separation. Evidence: CODEOWNERS, ownership configs.
- **OPS 3 — How does your organizational culture support your business outcomes?** Look for: test coverage, PR templates, contributing guides, code review configs. Evidence: test directories, CONTRIBUTING.md, PR templates.

**Prepare:**
- **OPS 4 — How do you implement observability in your workload?** Look for: structured logging (JSON, correlation IDs), distributed tracing (X-Ray, OTEL), custom metrics (PutMetricData, EMF), dashboards. Evidence: logger configs, tracing SDK usage, metric publishing code.
- **OPS 5 — How do you reduce defects, ease remediation, and improve flow into production?** Look for: automated testing (unit, integration, e2e), linting, SAST/DAST, staged pipelines, artifact promotion. Evidence: test files, CI/CD configs, quality gates.
- **OPS 6 — How do you mitigate deployment risks?** Look for: canary/blue-green/rolling deployments, feature flags, automated rollback on alarm, deployment health checks. Evidence: CodeDeploy configs, deployment strategies, rollback triggers.
- **OPS 7 — How do you know that you are ready to support a workload?** Look for: runbooks (SSM docs, markdown), load test scripts, operational readiness configs, pre-deploy checklists. Evidence: SSM documents, runbook files, readiness checks.

**Operate:**
- **OPS 8 — How do you utilize workload observability in your organization?** Look for: composite alarms, SLI-based dashboards, dependency health tracking, anomaly detection. Evidence: CompositeAlarm constructs, dashboard JSON, health check endpoints.
- **OPS 9 — How do you understand the health of your operations?** Look for: DORA metrics tracking, deployment success monitoring, pipeline health dashboards. Evidence: pipeline metrics, deployment alarms, operational dashboards.
- **OPS 10 — How do you manage workload and operations events?** Look for: EventBridge rules for operational events, automated remediation (Lambda/SSM), escalation configs, SNS routing. Evidence: EventBridge rules, remediation functions, notification topics.

**Evolve:**
- **OPS 11 — How do you evolve operations?** Look for: post-incident review process, action item tracking, chaos engineering (FIS experiments), automation of manual tasks, feedback loops. Evidence: FIS configs, retrospective docs, automation scripts.

### Security (11 questions)

**Security Foundations:**
- **SEC 1 — How do you securely operate your workload?** Look for: security baselines, account separation, Config rules, automated security response. Evidence: SCPs, Config rule definitions, security automation.

**Identity and Access Management:**
- **SEC 2 — How do you manage identities for people and machines?** Look for: centralized identity (Identity Center, Cognito), role separation, credential lifecycle, MFA configs. Evidence: identity provider configs, role definitions, MFA enforcement.
- **SEC 3 — How do you manage permissions for people and machines?** Look for: least privilege policies, permission boundaries, Access Analyzer. Flag any `"Action": "*"` or `"Resource": "*"` on mutating actions. Evidence: IAM policy documents, permission boundary ARNs.

**Detection:**
- **SEC 4 — How do you detect and investigate security events?** Look for: CloudTrail (all regions, log validation), GuardDuty, Security Hub, VPC Flow Logs, security alarms. Evidence: trail configs, detector settings, log group definitions.

**Infrastructure Protection:**
- **SEC 5 — How do you protect your network resources?** Look for: VPC segmentation, private subnets, security groups (flag `0.0.0.0/0` on non-443/80), WAF, VPC endpoints. Evidence: VPC constructs, SG rules, WAF ACLs.
- **SEC 6 — How do you protect your compute resources?** Look for: IMDSv2 enforcement, container image scanning, no privileged mode, SSM vs SSH, patching. Evidence: launch templates, task definitions, Lambda configs.

**Data Protection:**
- **SEC 7 — How do you classify your data?** Look for: data classification tags, sensitivity labels, Macie configs. Evidence: resource tags, classification policies.
- **SEC 8 — How do you protect your data at rest?** Look for: encryption on ALL storage resources. Flag any without encryption. KMS key rotation, CMK vs default. Evidence: encryption properties in IaC.
- **SEC 9 — How do you protect your data in transit?** Look for: TLS 1.2+ enforcement, HTTPS-only, certificate management. Flag TLS < 1.2 as Critical. Evidence: listener configs, security policies.

**Incident Response:**
- **SEC 10 — How do you anticipate, respond to, and recover from incidents?** Look for: response automation, forensic capabilities, containment procedures, game days. Evidence: remediation Lambdas, isolation procedures.

**Application Security:**
- **SEC 11 — How do you incorporate and validate the security properties of applications throughout the design, development, and deployment lifecycle?** Look for: SAST/DAST in pipeline, dependency scanning, threat modeling, security testing. Evidence: security scan configs, dependency audit tools.

### Reliability (13 questions)

**Foundations:**
- **REL 1 — How do you manage Service Quotas and constraints?** Look for: quota monitoring alarms, SDK retry configs, throttling handling code. Evidence: quota alarms, retry logic.
- **REL 2 — How do you plan your network topology?** Look for: multi-AZ subnets, redundant NAT Gateways, VPC design, IP planning. Evidence: subnet definitions, AZ distribution.

**Workload Architecture:**
- **REL 3 — How do you design your workload service architecture?** Look for: service boundaries, loose coupling, API contracts, async communication. Evidence: module structure, queue-based decoupling.
- **REL 4 — How do you design interactions in a distributed system to prevent failures?** Look for: retries with exponential backoff, timeouts, idempotency tokens, queue-based decoupling. Evidence: SDK client configs, retry logic, SQS/SNS usage.
- **REL 5 — How do you design interactions in a distributed system to mitigate or withstand failures?** Look for: circuit breakers, graceful degradation, fallback logic, bulkhead patterns, load shedding. Evidence: fallback code paths, throttling configs.

**Change Management:**
- **REL 6 — How do you monitor workload resources?** Look for: health check endpoints, alarm definitions, composite alarms, anomaly detection. Evidence: health check implementations, CloudWatch alarms.
- **REL 7 — How do you design your workload to adapt to changes in demand?** Look for: auto-scaling policies (target tracking, step), scaling metrics, scheduled scaling, capacity buffers. Evidence: ASG configs, scaling policies.
- **REL 8 — How do you implement change?** Look for: deployment strategies (canary, blue/green), health check gating, automated rollback, backward-compatible migrations. Evidence: deployment configs, rollback triggers.

**Failure Management:**
- **REL 9 — How do you back up data?** Look for: AWS Backup plans, PITR, cross-region replication, snapshot configs. Flag stateful resources without backups. Evidence: backup rules, retention settings.
- **REL 10 — How do you use fault isolation to protect your workload?** Look for: multi-AZ distribution, cell-based architecture, shuffle sharding, blast radius containment. Evidence: AZ spread in IaC, isolation boundaries.
- **REL 11 — How do you design your workload to withstand component failures?** Look for: redundancy, failover automation, stateless design, health-based routing, DLQs. Evidence: multi-AZ configs, failover policies, DLQ settings.
- **REL 12 — How do you test reliability?** Look for: FIS experiments, failure injection code, game day runbooks, DR test scripts. Evidence: FIS experiment templates, chaos configs.
- **REL 13 — How do you plan for disaster recovery (DR)?** Look for: cross-region resources, RTO/RPO definitions, DR automation, pilot light/warm standby configs. Evidence: cross-region replication, DR runbooks.

### Performance Efficiency (5 questions)

- **PERF 1 — How do you select appropriate cloud resources and architecture patterns?** Look for: resource type justification, service selection rationale, Graviton adoption, trade-off documentation. Evidence: instance types in IaC, architecture docs.
- **PERF 2 — How do you select and use compute resources?** Look for: instance types matching workload, Lambda memory tuning, container right-sizing, Graviton/ARM. Evidence: compute configs, memory/CPU settings.
- **PERF 3 — How do you store, manage, and access data?** Look for: storage types matching access patterns, read replicas, connection pooling (RDS Proxy), caching (ElastiCache, DAX, CloudFront). Evidence: database configs, cache layers.
- **PERF 4 — How do you select and configure networking resources?** Look for: CloudFront distributions, VPC endpoints, placement groups, compression, Global Accelerator. Evidence: CDN configs, endpoint definitions.
- **PERF 5 — What process do you use to support more performance efficiency?** Look for: load testing, performance metrics (p50/p95/p99), performance budgets, continuous optimization. Evidence: load test scripts, latency alarms, performance dashboards.

### Cost Optimization (11 questions)

**Cloud Financial Management:**
- **COST 1 — How do you implement cloud financial management?** Look for: cost allocation tags, FinOps practices, Budget configs, cost-aware culture. Evidence: tag policies, budget definitions.

**Expenditure and Usage Awareness:**
- **COST 2 — How do you govern usage?** Look for: SCPs limiting resource types, quotas, governance policies. Evidence: organizational policies, resource constraints.
- **COST 3 — How do you monitor usage and cost?** Look for: Budget alarms, Cost Anomaly Detection, billing dashboards. Evidence: Budget configs, anomaly rules.
- **COST 4 — How do you decommission resources?** Look for: lifecycle policies, TTL configs, cleanup automation, retention rules. Flag "never expire" logs. Evidence: S3 lifecycle, log retention settings.

**Cost-Effective Resources:**
- **COST 5 — How do you evaluate cost when you select services?** Look for: managed services vs self-managed, serverless for variable loads, provisioned for steady state. Evidence: service selection in IaC.
- **COST 6 — How do you meet cost targets when you select resource type, size and number?** Look for: right-sized instances, scaling boundaries, Compute Optimizer usage. Flag over-provisioned resources. Evidence: instance types, scaling min/max.
- **COST 7 — How do you use pricing models to reduce cost?** Look for: Savings Plans, Reserved capacity, Spot usage for fault-tolerant workloads. Evidence: reservation configs, Spot fleet settings.
- **COST 8 — How do you plan for data transfer charges?** Look for: VPC endpoints (avoid NAT charges), CloudFront, regional placement, cross-region patterns. Evidence: VPC endpoint configs, CDN usage.

**Manage Demand and Supply:**
- **COST 9 — How do you manage demand, and supply resources?** Look for: auto-scaling, throttling (API Gateway), queue-based load leveling, scheduled scaling. Evidence: scaling configs, throttle settings.

**Optimize Over Time:**
- **COST 10 — How do you evaluate new services?** Look for: modern service adoption, latest instance generations, managed service migration. Evidence: instance gen in IaC, service choices.
- **COST 11 — How do you evaluate the cost of effort?** Look for: automation of manual operations, operational efficiency measurement. Evidence: automation scripts, CI/CD reducing manual effort.

### Sustainability (6 questions)

- **SUS 1 — How do you select Regions for your workload?** Look for: region selection rationale, carbon intensity consideration, data residency alignment. Evidence: region configs in IaC.
- **SUS 2 — How do you align cloud resources to your demand?** Look for: scale-to-zero configs, scheduled scaling, event-driven architecture, unused asset cleanup. Evidence: scaling policies, Lambda/Fargate configs.
- **SUS 3 — How do you take advantage of software and architecture patterns to support your sustainability goals?** Look for: async processing, managed services, efficient algorithms, caching to reduce computation. Evidence: queue usage, managed service adoption, caching layers.
- **SUS 4 — How do you take advantage of data management policies and patterns?** Look for: lifecycle policies, compression, tiering (Intelligent-Tiering, Glacier), TTL, deduplication. Evidence: S3 lifecycle rules, compression configs.
- **SUS 5 — How do you select and use cloud hardware and services to support your sustainability goals?** Look for: Graviton/ARM adoption, latest instance generations, managed services, GPU optimization. Flag x86 where Graviton is available. Evidence: instance type selections.
- **SUS 6 — How do your organizational processes support your sustainability goals?** Look for: multi-stage Docker builds, CI caching, incremental deployments, up-to-date dependencies. Evidence: Dockerfiles, CI configs, dependency versions.

## Step 5: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor (limited blast radius) | Moderate (subset of users affected) | Severe (full outage, data loss, regulatory violation)

**Likelihood**: Low (specific conditions required) | Medium (possible under normal operations) | High (common failure mode, weak controls)

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

Identify cross-pillar conflicts:
- Security controls that impact performance
- Cost optimizations that reduce reliability
- Reliability patterns that increase cost

## Step 6: Produce the report

Output a structured report:

```markdown
# Well-Architected Review: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Workload**: {name}
- **Business Criticality**: {level}
- **Lens Applied**: {lens or "General"}
- **Packages Analyzed**: {list}
- **Questions Assessed**: 57/57
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Maturity**: {1-5} — {one-line justification}

## Architecture Overview
{PlantUML diagram}
{Brief description of architecture, key services, data flows}

## Pillar Scorecard
| Pillar | Score (1-5) | Questions Assessed | Key Strength | Key Gap |
|--------|-------------|-------------------|--------------|---------|
| Operational Excellence | {score} | 11/11 | {strength} | {gap} |
| Security | {score} | 11/11 | {strength} | {gap} |
| Reliability | {score} | 13/13 | {strength} | {gap} |
| Performance Efficiency | {score} | 5/5 | {strength} | {gap} |
| Cost Optimization | {score} | 11/11 | {strength} | {gap} |
| Sustainability | {score} | 6/6 | {strength} | {gap} |

## Per-Question Assessment
| ID | Question | Status | Risk Level | Key Evidence |
|----|----------|--------|------------|--------------|
| OPS 1 | Priorities | {status} | {risk or N/A} | {evidence} |
| OPS 2 | Organization structure | {status} | {risk or N/A} | {evidence} |
| ... | ... | ... | ... | ... |
| SUS 6 | Process and culture | {status} | {risk or N/A} | {evidence} |

{Complete this table for all 57 questions — do not truncate}

## Critical and High Risk Findings
{For each: ID, pillar, title, description, evidence (file:line), impact assessment, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Pillar | Title | Recommendation}

## Cross-Pillar Trade-offs
{Conflicts between pillars and recommended resolution}

## Prioritize Improvements — Eisenhower Matrix

Not all findings should be addressed at once. Focus on a selected number of issues that make the most business impact and are easiest to implement. Then iterate.

Classify each finding by **importance** (business value) and **effort** (time, complexity, headcount):

```
        HIGH IMPORTANCE
             │
   ┌─────────┼─────────┐
   │  DO     │  PLAN   │
   │  FIRST  │         │
   │         │         │
───┼─────────┼─────────┼───
   │         │         │
   │DELEGATE │  DEFER  │
   │         │         │
   └─────────┼─────────┘
             │
        LOW IMPORTANCE
   LOW EFFORT    HIGH EFFORT
```

| Quadrant | Action | Findings |
|----------|--------|----------|
| **Do First** (High Importance, Low Effort) | Implement immediately | {finding IDs} |
| **Plan** (High Importance, High Effort) | Schedule in roadmap, break into phases | {finding IDs} |
| **Delegate** (Low Importance, Low Effort) | Batch together, assign to available team member | {finding IDs} |
| **Defer** (Low Importance, High Effort) | Revisit in next iteration | {finding IDs} |

### Solution Characteristics

For each solution in "Do First" and "Plan":
- **SMART goal**: Specific, Measurable, Achievable, Relevant, Time-bound
- **Owner**: Identify who is responsible
- **Simple over complex**: Choose the simplest solution unless complexity is a non-negotiable requirement
- **Two-way door decisions**: Solutions should be extensible and evolve over time — avoid static solutions that cannot adapt
- **Pattern-based**: Target solutions that can be codified, reused, and re-shared (reference AWS Architecture Center)

## Prioritized Remediation Plan

### Quick Wins (< 1 week) — "Do First" quadrant
| Finding | Action | SMART Goal | Owner Suggestion | Effort |
|---------|--------|-----------|-----------------|--------|
{Config changes, enabling features, adding tags/alarms — simple, high-impact}

### Foundation (1-4 weeks) — "Plan" quadrant
| Finding | Action | Phases | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Multi-AZ, CI/CD improvements, monitoring, caching — phased approach}

### Strategic (1-3 months) — "Plan" quadrant (complex)
| Finding | Action | Phases | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{DR, re-architecture, compliance programs — two-way door design}

### Deferred — Revisit Next Iteration
{Findings in "Delegate" and "Defer" quadrants with brief justification for deferral}

## Next Steps
{Top 5 concrete actions from the "Do First" quadrant — the team should start this week}
```

## Step 7: Offer follow-up

After delivering the report, offer:

> Would you like me to:
> - Deep-dive into a specific pillar with expanded analysis?
> - Generate IaC templates to remediate a specific finding?
> - Create a migration plan for a specific architectural change?
> - Compare your workload against a specific WA Lens in detail?
> - Generate automated checks (Config rules, custom metrics) for ongoing compliance?
> - Produce a WA Tool import for tracking in the AWS console?

## Calibration Guidance

- A workload with multi-AZ, encryption, CI/CD with rollback, monitoring, and auto-scaling is MATURE — most findings should be improvements, not Critical
- Do NOT manufacture Critical findings for a well-built workload — accuracy over alarm
- When business criticality is "low"/"standard", accept simpler architectures (single-region is fine for internal tools)
- When business criticality is "critical", apply stricter standards (multi-region DR, chaos testing, sub-minute RTO expected)
- Every finding MUST have code evidence — no generic recommendations without backing
- If something cannot be determined from code, say "Cannot Determine" and explain what runtime/interview data is needed
- Acknowledge strengths prominently — a mature workload should feel validated, not just criticized
