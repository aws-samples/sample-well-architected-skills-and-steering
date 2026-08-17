# Well-Architected Framework Questions — Evaluation Criteria

Use this reference when evaluating a workload against the 57 WA Framework questions. For each question, look for the listed evidence types in code, IaC, and configuration files.

## Operational Excellence (11 questions)

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

## Security (11 questions)

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

## Reliability (13 questions)

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

## Performance Efficiency (5 questions)

- **PERF 1 — How do you select appropriate cloud resources and architecture patterns?** Look for: resource type justification, service selection rationale, Graviton adoption, trade-off documentation. Evidence: instance types in IaC, architecture docs.
- **PERF 2 — How do you select and use compute resources?** Look for: instance types matching workload, Lambda memory tuning, container right-sizing, Graviton/ARM. Evidence: compute configs, memory/CPU settings.
- **PERF 3 — How do you store, manage, and access data?** Look for: storage types matching access patterns, read replicas, connection pooling (RDS Proxy), caching (ElastiCache, DAX, CloudFront). Evidence: database configs, cache layers.
- **PERF 4 — How do you select and configure networking resources?** Look for: CloudFront distributions, VPC endpoints, placement groups, compression, Global Accelerator. Evidence: CDN configs, endpoint definitions.
- **PERF 5 — What process do you use to support more performance efficiency?** Look for: load testing, performance metrics (p50/p95/p99), performance budgets, continuous optimization. Evidence: load test scripts, latency alarms, performance dashboards.

## Cost Optimization (11 questions)

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

## Sustainability (6 questions)

- **SUS 1 — How do you select Regions for your workload?** Look for: region selection rationale, carbon intensity consideration, data residency alignment. Evidence: region configs in IaC.
- **SUS 2 — How do you align cloud resources to your demand?** Look for: scale-to-zero configs, scheduled scaling, event-driven architecture, unused asset cleanup. Evidence: scaling policies, Lambda/Fargate configs.
- **SUS 3 — How do you take advantage of software and architecture patterns to support your sustainability goals?** Look for: async processing, managed services, efficient algorithms, caching to reduce computation. Evidence: queue usage, managed service adoption, caching layers.
- **SUS 4 — How do you take advantage of data management policies and patterns?** Look for: lifecycle policies, compression, tiering (Intelligent-Tiering, Glacier), TTL, deduplication. Evidence: S3 lifecycle rules, compression configs.
- **SUS 5 — How do you select and use cloud hardware and services to support your sustainability goals?** Look for: Graviton/ARM adoption, latest instance generations, managed services, GPU optimization. Flag x86 where Graviton is available. Evidence: instance type selections.
- **SUS 6 — How do your organizational processes support your sustainability goals?** Look for: multi-stage Docker builds, CI caching, incremental deployments, up-to-date dependencies. Evidence: Dockerfiles, CI configs, dependency versions.

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
