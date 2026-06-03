---
inclusion: manual
---

# Well-Architected Review — Deep Analysis

## Overview

This script performs a comprehensive AWS Well-Architected Framework review of a workload by analyzing actual code, infrastructure-as-code, configuration files, and deployment artifacts. Unlike interview-based reviews, this produces evidence-backed findings tied to specific files and configurations. The output is a structured report with prioritized findings, risk assessments, and a remediation plan grounded in code reality.

## Parameters

- **workload_name** (required): Name of the workload being reviewed
- **code_packages** (required): List of code packages/directories to analyze
- **output_directory** (optional, default: "./wa-review-output"): Directory where outputs will be saved
- **business_criticality** (optional, default: "standard"): Business criticality level ("critical", "high", "standard", "low")
- **lens** (optional): Specialized WA Lens to apply ("serverless", "saas", "data-analytics", "machine-learning", "iot", "containers", "games", "financial-services", "healthcare")
- **focus_pillars** (optional): Comma-separated list of pillars to prioritize (all are still evaluated, but these get deeper analysis)

### Constraints for parameter acquisition:
- You MUST ask for all required parameters upfront in a single prompt
- You MUST create the output directory if it doesn't exist
- You MUST NOT overwrite existing output directory without user confirmation
- You SHOULD suggest a lens if the workload type is obvious from the code (e.g., Lambda-heavy → serverless)

## Steps

### 1. Create Project Structure

Set up the output directory structure.

**Constraints:**
- You MUST create the following structure:
```
{output_directory}/
  discovery/
    infrastructure/
    application/
    operations/
    metadata/
  pillars/
    operational-excellence/
    security/
    reliability/
    performance-efficiency/
    cost-optimization/
    sustainability/
  report/
  README.md
```
- You MUST create a README explaining the structure and how to read the outputs
- You MUST notify the user when structure is created

### 2. Infrastructure Discovery

Analyze all infrastructure-as-code and deployment configurations.

**Constraints:**
- You MUST analyze ALL IaC files while respecting .gitignore patterns:
  - CDK code (TypeScript, Python, Java, Go, .NET)
  - CloudFormation templates (YAML, JSON)
  - Terraform configurations (.tf files)
  - SAM templates
  - Serverless Framework configurations
  - Pulumi programs
- You MUST document for each infrastructure component:
  - Resource type and logical name
  - Configuration properties relevant to WA pillars
  - File path and line numbers where defined
  - Dependencies on other resources
  - Security-relevant configurations (IAM, encryption, network)
  - Resilience configurations (multi-AZ, backups, scaling)
  - Cost-relevant configurations (instance types, pricing model, reserved capacity)
- You MUST identify and document:
  - All AWS services used and their configurations
  - Network topology (VPCs, subnets, security groups, NACLs)
  - IAM roles, policies, and trust relationships
  - Encryption configurations (KMS keys, at-rest, in-transit)
  - Scaling configurations (Auto Scaling, Lambda concurrency, DynamoDB capacity)
  - Monitoring configurations (CloudWatch alarms, dashboards, log groups)
  - Backup and recovery configurations (AWS Backup, RDS snapshots, S3 versioning)
  - Deployment configurations (CodeDeploy, ECS deployment, Lambda aliases)
- You MUST save findings to "{output_directory}/discovery/infrastructure/infrastructure-analysis.md"
- You MUST create a JSON inventory at "{output_directory}/discovery/metadata/aws-resources.json" with the structure:
  ```json
  {
    "resources": [
      {
        "type": "AWS::Lambda::Function",
        "logicalId": "IngestionHandler",
        "filePath": "/absolute/path/to/stack.ts",
        "lineNumber": 42,
        "properties": {},
        "pillarRelevance": ["reliability", "security", "cost-optimization"]
      }
    ]
  }
  ```
- You MUST NOT skip any IaC files without examination

### 3. Application Architecture Discovery

Analyze application code for architectural patterns and practices.

**Constraints:**
- You MUST examine:
  - Entry points (API handlers, event processors, scheduled tasks)
  - Service-to-service communication patterns (sync/async, retries, timeouts)
  - Data access patterns (queries, caching, connection management)
  - Error handling and resilience patterns (retries, circuit breakers, fallbacks)
  - Authentication and authorization logic
  - Input validation and sanitization
  - Logging and observability instrumentation
  - Configuration management (environment variables, parameter store, feature flags)
- For each component, you MUST document:
  - Purpose and responsibility
  - File paths with line numbers
  - Architectural patterns used
  - Dependencies (internal and external)
  - Error handling approach
  - Observability instrumentation present
- You MUST create an architecture diagram in PlantUML showing:
  - All major components and their relationships
  - Data flows between components
  - External dependencies
  - Trust boundaries
  - Network boundaries
- You MUST save findings to "{output_directory}/discovery/application/application-analysis.md"
- You MUST save the architecture diagram to "{output_directory}/discovery/application/architecture-diagram.md"
- You MUST create a JSON mapping at "{output_directory}/discovery/metadata/components.json"

### 4. Operations Discovery

Analyze CI/CD, monitoring, and operational configurations.

**Constraints:**
- You MUST examine:
  - CI/CD pipeline definitions (CodePipeline, GitHub Actions, Jenkins, GitLab CI)
  - Deployment strategies configured (canary, blue/green, rolling, all-at-once)
  - Rollback mechanisms
  - CloudWatch alarms and dashboards
  - Log configurations and retention policies
  - Tracing configurations (X-Ray, OpenTelemetry)
  - Runbooks and automation documents (SSM documents, Step Functions)
  - Health check configurations
  - Alerting and notification configurations (SNS, PagerDuty, Slack)
- You MUST document:
  - Deployment frequency and strategy
  - Monitoring coverage (what's monitored vs what should be)
  - Alert routing and escalation
  - Incident response automation
  - Change management process (if evident from code)
- You MUST save findings to "{output_directory}/discovery/operations/operations-analysis.md"
- You MUST create a JSON summary at "{output_directory}/discovery/metadata/operations.json"

### 5. Evaluate Operational Excellence Pillar

Perform deep analysis against the Operational Excellence pillar.

**Constraints:**
- You MUST evaluate against these WA Framework questions with code evidence:

  **OPS 1 — How do you determine what your priorities are?**
  - Look for: business metrics in dashboards, SLO/SLI definitions, health check implementations
  - Evidence: CloudWatch dashboard definitions, alarm configurations, health check endpoints

  **OPS 2 — How do you structure your organization to support your business outcomes?**
  - Look for: separation of concerns in code structure, team ownership boundaries, operational documentation
  - Evidence: package/module boundaries, CODEOWNERS files, documentation

  **OPS 3 — How does your organizational culture support your business outcomes?**
  - Look for: code review processes, testing practices, documentation standards
  - Evidence: test coverage, PR templates, contributing guides

  **OPS 4 — How do you implement observability?**
  - Look for: structured logging, distributed tracing, custom metrics, correlation IDs
  - Evidence: log statements with structured data, X-Ray/OTEL instrumentation, metric publishing code

  **OPS 5 — How do you reduce defects, ease remediation, and improve flow into production?**
  - Look for: automated testing, linting, security scanning, staged deployments
  - Evidence: test files, CI/CD configs, pre-commit hooks, deployment stage definitions

  **OPS 6 — How do you mitigate deployment risks?**
  - Look for: canary/blue-green deployments, feature flags, rollback automation, deployment alarms
  - Evidence: deployment configuration, CodeDeploy settings, feature flag SDK usage

  **OPS 7 — How do you know that you are ready to support a workload?**
  - Look for: runbooks, operational readiness checks, load testing, pre-production validation
  - Evidence: SSM documents, load test scripts, readiness check configurations

  **OPS 8 — How do you understand the health of your workload?**
  - Look for: health dashboards, composite alarms, dependency health tracking
  - Evidence: CloudWatch dashboard JSON, alarm definitions, health check implementations

  **OPS 9 — How do you understand the health of your operations?**
  - Look for: operational metrics, deployment success tracking, change failure rates
  - Evidence: pipeline metrics, deployment monitoring, MTTR tracking

  **OPS 10 — How do you manage workload and operations events?**
  - Look for: event routing, automated remediation, escalation procedures, incident response
  - Evidence: EventBridge rules, Lambda remediations, SNS topics, runbook references

- For each question, you MUST provide:
  - Assessment: "Implemented", "Partially Implemented", "Not Implemented", "Cannot Determine"
  - Evidence: specific file paths and line numbers supporting the assessment
  - Gaps: what's missing or could be improved
  - Risk: what could go wrong due to the gap
- You MUST save the full analysis to "{output_directory}/pillars/operational-excellence/analysis.md"
- You MUST create a summary JSON at "{output_directory}/pillars/operational-excellence/findings.json"

### 6. Evaluate Security Pillar

Perform deep analysis against the Security pillar.

**Constraints:**
- You MUST evaluate against these WA Framework questions with code evidence:

  **SEC 1 — How do you securely operate your workload?**
  - Look for: security controls, account separation, threat detection, security baselines
  - Evidence: SCPs, Config rules, GuardDuty configs, security group rules

  **SEC 2 — How do you manage identities for people and machines?**
  - Look for: identity provider integration, role separation, credential management, MFA
  - Evidence: IAM policies, trust relationships, Cognito/Identity Center configs

  **SEC 3 — How do you manage permissions for people and machines?**
  - Look for: least privilege policies, permission boundaries, resource-based policies, wildcards
  - Evidence: IAM policy documents (flag any `*` in Action or Resource for non-read operations)

  **SEC 4 — How do you detect and investigate security events?**
  - Look for: CloudTrail, GuardDuty, Security Hub, VPC Flow Logs, WAF logs
  - Evidence: trail configurations, detector settings, hub enablement, log group configs

  **SEC 5 — How do you protect your network resources?**
  - Look for: VPC design, security groups, NACLs, WAF rules, private subnets, VPC endpoints
  - Evidence: network constructs in IaC, ingress/egress rules, endpoint definitions

  **SEC 6 — How do you protect your compute resources?**
  - Look for: patching strategy, container image scanning, runtime protection, SSM
  - Evidence: launch templates, ECS task definitions, Lambda configs, AMI pipelines

  **SEC 7 — How do you classify your data?**
  - Look for: data classification tags, sensitivity labels, data catalogs
  - Evidence: resource tags, Macie configs, Glue catalog settings

  **SEC 8 — How do you protect your data at rest?**
  - Look for: encryption enabled on all stores, KMS key policies, key rotation
  - Evidence: encryption properties in IaC (flag any storage resource without encryption)

  **SEC 9 — How do you protect your data in transit?**
  - Look for: TLS enforcement, certificate management, HTTPS-only policies
  - Evidence: listener configs, certificate resources, security policies (flag TLS < 1.2)

  **SEC 10 — How do you anticipate, respond to, and recover from incidents?**
  - Look for: incident response plans, forensic capabilities, automated containment
  - Evidence: response automation, isolation procedures, backup/restore configs

- For each question, you MUST provide:
  - Assessment: "Implemented", "Partially Implemented", "Not Implemented", "Cannot Determine"
  - Evidence: specific file paths and line numbers
  - Gaps: what's missing
  - Risk: what could be exploited or exposed
- You MUST flag as HIGH RISK:
  - Any IAM policy with `"Effect": "Allow", "Action": "*"` or `"Resource": "*"` on mutating actions
  - Any storage resource without encryption at rest
  - Any listener accepting TLS < 1.2
  - Any security group with `0.0.0.0/0` ingress on non-443/80 ports
  - Any hardcoded credentials or secrets in code
  - Any Lambda/container running as root without justification
- You MUST save to "{output_directory}/pillars/security/analysis.md"
- You MUST create "{output_directory}/pillars/security/findings.json"

### 7. Evaluate Reliability Pillar

Perform deep analysis against the Reliability pillar.

**Constraints:**
- You MUST evaluate against these WA Framework questions with code evidence:

  **REL 1 — How do you manage service quotas and constraints?**
  - Look for: quota monitoring, request patterns, throttling handling
  - Evidence: quota alarms, SDK retry configs, rate limiting code

  **REL 2 — How do you plan your network topology?**
  - Look for: multi-AZ deployment, redundant connectivity, IP address planning
  - Evidence: subnet definitions, AZ distribution, NAT gateway redundancy

  **REL 3 — How does your system adapt to changes in demand?**
  - Look for: auto-scaling configurations, scaling policies, capacity planning
  - Evidence: ASG configs, scaling policies, Lambda concurrency, DynamoDB capacity mode

  **REL 4 — How do you design interactions in a distributed system to prevent failures?**
  - Look for: retries with backoff, circuit breakers, timeouts, idempotency, queue-based decoupling
  - Evidence: SDK client configs, retry logic, SQS/SNS usage, idempotency tokens

  **REL 5 — How do you design interactions in a distributed system to mitigate or withstand failures?**
  - Look for: graceful degradation, fallback logic, bulkhead patterns, load shedding
  - Evidence: fallback code paths, throttling configs, priority queue implementations

  **REL 6 — How do you monitor workload resources?**
  - Look for: health checks, dependency monitoring, anomaly detection, composite alarms
  - Evidence: health check endpoints, alarm definitions, dashboard configs

  **REL 7 — How do you design your workload to adapt to changes in demand?**
  - Look for: scaling triggers, predictive scaling, capacity buffers
  - Evidence: scaling policy metrics, scheduled scaling, buffer calculations

  **REL 8 — How do you implement change?**
  - Look for: deployment strategies, health check gating, automated rollback
  - Evidence: deployment configs, health check integration, rollback triggers

  **REL 9 — How do you back up data?**
  - Look for: automated backups, point-in-time recovery, cross-region replication
  - Evidence: backup configs, PITR settings, replication rules

  **REL 10 — How do you use fault isolation to protect your workload?**
  - Look for: multi-AZ, cell-based architecture, shuffle sharding, blast radius containment
  - Evidence: AZ distribution in IaC, isolation boundaries, failure domain design

  **REL 11 — How do you design your workload to withstand component failures?**
  - Look for: redundancy, failover automation, stateless design, health-based routing
  - Evidence: multi-AZ configs, failover policies, session handling

  **REL 12 — How do you test reliability?**
  - Look for: chaos engineering, failure injection, game days, DR testing
  - Evidence: FIS experiments, failure injection code, DR runbooks

  **REL 13 — How do you plan for disaster recovery (DR)?**
  - Look for: DR strategy (pilot light, warm standby, multi-site), RTO/RPO definitions, DR automation
  - Evidence: cross-region resources, DR automation scripts, backup restore procedures

- You MUST flag as HIGH RISK:
  - Single-AZ deployments for critical workloads
  - No auto-scaling on compute resources
  - No backup configuration on stateful resources
  - No health checks on load-balanced targets
  - No retry logic on external service calls
  - No deployment rollback mechanism
- You MUST save to "{output_directory}/pillars/reliability/analysis.md"
- You MUST create "{output_directory}/pillars/reliability/findings.json"

### 8. Evaluate Performance Efficiency Pillar

Perform deep analysis against the Performance Efficiency pillar.

**Constraints:**
- You MUST evaluate against these WA Framework questions with code evidence:

  **PERF 1 — How do you select appropriate cloud resources?**
  - Look for: resource type justification, Graviton usage, instance family selection
  - Evidence: instance types in IaC, compute configurations, storage tier selections

  **PERF 2 — How do you select your compute solution?**
  - Look for: compute type matching workload (Lambda vs ECS vs EC2), right-sizing evidence
  - Evidence: memory/CPU configs, timeout settings, concurrency limits

  **PERF 3 — How do you select your storage solution?**
  - Look for: storage type matching access patterns, IOPS provisioning, tiering
  - Evidence: storage configs, DynamoDB capacity, S3 storage classes, EBS types

  **PERF 4 — How do you select your database solution?**
  - Look for: database type matching query patterns, read replicas, connection pooling
  - Evidence: database configs, RDS Proxy, DAX, replica configurations

  **PERF 5 — How do you configure your networking solution?**
  - Look for: CDN, edge caching, connection reuse, placement groups, enhanced networking
  - Evidence: CloudFront distributions, VPC endpoint usage, placement configs

  **PERF 6 — How do you evolve your workload to take advantage of new releases?**
  - Look for: modern runtime usage, latest SDK versions, new feature adoption
  - Evidence: runtime versions, dependency versions, feature flag for new capabilities

  **PERF 7 — How do you monitor your resources to ensure they are performing?**
  - Look for: latency tracking (p50, p99), throughput metrics, saturation monitoring
  - Evidence: custom metrics, dashboard panels, performance alarms

  **PERF 8 — How do you use tradeoffs to improve performance?**
  - Look for: caching strategies, read replicas, eventual consistency choices, async patterns
  - Evidence: cache configurations, read replica usage, SQS/EventBridge for async

- You MUST flag as HIGH RISK:
  - Over-provisioned resources (e.g., m5.4xlarge for a lightweight API)
  - Missing caching layer for read-heavy workloads
  - Synchronous processing where async would be appropriate
  - Database queries without connection pooling in serverless
  - No CDN for static content delivery
- You MUST save to "{output_directory}/pillars/performance-efficiency/analysis.md"
- You MUST create "{output_directory}/pillars/performance-efficiency/findings.json"

### 9. Evaluate Cost Optimization Pillar

Perform deep analysis against the Cost Optimization pillar.

**Constraints:**
- You MUST evaluate against these WA Framework questions with code evidence:

  **COST 1 — How do you implement cloud financial management?**
  - Look for: cost allocation tags, budget alarms, cost reporting
  - Evidence: tag configurations, Budget/Cost anomaly configs, cost allocation tags in IaC

  **COST 2 — How do you govern usage?**
  - Look for: SCPs, quotas, resource policies, instance type restrictions
  - Evidence: organizational policies, resource constraints, permission boundaries

  **COST 3 — How do you monitor usage and cost?**
  - Look for: cost alarms, anomaly detection, usage metrics
  - Evidence: Budget configs, Cost Anomaly Detection, CloudWatch billing alarms

  **COST 4 — How do you decommission resources?**
  - Look for: lifecycle policies, TTL configurations, cleanup automation
  - Evidence: S3 lifecycle rules, log retention, snapshot cleanup, resource expiration

  **COST 5 — How do you evaluate cost when you select services?**
  - Look for: pricing model alignment, serverless for variable loads, reserved for steady state
  - Evidence: provisioning mode configs, capacity reservations, Spot usage

  **COST 6 — How do you meet cost targets when you select resource type, size, and number?**
  - Look for: right-sizing, instance families matching workload, scaling boundaries
  - Evidence: instance types, scaling min/max, memory/CPU allocations

  **COST 7 — How do you use pricing models to reduce cost?**
  - Look for: Savings Plans, Reserved Instances, Spot Instances, committed throughput
  - Evidence: reservation configs, Spot fleet settings, DynamoDB reserved capacity

  **COST 8 — How do you plan for data transfer charges?**
  - Look for: VPC endpoints (avoid NAT charges), regional deployment, data locality
  - Evidence: VPC endpoint configs, cross-region transfer patterns, S3 access patterns

- You MUST flag as HIGH RISK:
  - Resources provisioned without auto-scaling (paying for idle capacity)
  - Missing S3 lifecycle policies on large buckets
  - NAT Gateway usage where VPC endpoints would suffice
  - Over-provisioned DynamoDB with provisioned capacity
  - No cost allocation tags on resources
  - Log retention set to "never expire" without justification
- You MUST save to "{output_directory}/pillars/cost-optimization/analysis.md"
- You MUST create "{output_directory}/pillars/cost-optimization/findings.json"

### 10. Evaluate Sustainability Pillar

Perform deep analysis against the Sustainability pillar.

**Constraints:**
- You MUST evaluate against these WA Framework questions with code evidence:

  **SUS 1 — How do you select Regions to support your sustainability goals?**
  - Look for: region selection rationale, proximity to users, renewable energy regions
  - Evidence: region configs in IaC, multi-region setup, documentation

  **SUS 2 — How do you take advantage of user behavior patterns to support your sustainability goals?**
  - Look for: scaling to zero, scheduled scaling, demand-based provisioning
  - Evidence: scale-to-zero configs, scheduled actions, event-driven architecture

  **SUS 3 — How do you take advantage of software and architecture patterns to support your sustainability goals?**
  - Look for: async processing, batch operations, efficient algorithms, shared infrastructure
  - Evidence: queue-based processing, batch APIs, Lambda cold start optimization

  **SUS 4 — How do you take advantage of data access and usage patterns to support your sustainability goals?**
  - Look for: data tiering, lifecycle management, compression, deduplication, caching
  - Evidence: S3 Intelligent-Tiering, lifecycle rules, compression configs, cache layers

  **SUS 5 — How do your hardware management and usage patterns support your sustainability goals?**
  - Look for: Graviton processors, right-sizing, managed services, spot instances
  - Evidence: instance type selections (flag x86 where Graviton is available), managed service usage

  **SUS 6 — How do your development and deployment processes support your sustainability goals?**
  - Look for: efficient CI/CD, minimal artifact sizes, incremental deployments, container optimization
  - Evidence: multi-stage Docker builds, layer caching, artifact sizes, deployment efficiency

- You MUST flag as IMPROVEMENT OPPORTUNITY:
  - x86 instances where Graviton equivalents are available
  - Always-on resources that could scale to zero
  - Uncompressed data storage
  - Missing data lifecycle policies
  - Self-managed infrastructure where managed alternatives exist
- You MUST save to "{output_directory}/pillars/sustainability/analysis.md"
- You MUST create "{output_directory}/pillars/sustainability/findings.json"

### 11. Cross-Pillar Risk Assessment

Perform risk assessment across all findings using a standardized framework.

**Constraints:**
- You MUST assess each finding using Impact and Likelihood:
  - **Impact severity:**
    - **Minor**: Limited blast radius, no data loss, minimal user impact, easy to remediate
    - **Moderate**: Service degradation for subset of users, potential data exposure, moderate effort to fix
    - **Severe**: Full service outage, data loss or breach, regulatory violation, significant blast radius
  - **Likelihood:**
    - **Low**: Requires specific conditions, strong existing controls, unlikely to manifest
    - **Medium**: Possible under normal operations, partial controls exist, gaps could be exploited
    - **High**: Likely to occur, weak or missing controls, common failure mode

- You MUST determine Risk Level using this matrix:

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

- You MUST identify cross-pillar conflicts and trade-offs:
  - Security controls that impact performance
  - Cost optimizations that reduce reliability
  - Performance choices that increase cost
  - Reliability patterns that impact sustainability
- You MUST produce a consolidated risk register at "{output_directory}/report/risk-register.json" with structure:
  ```json
  {
    "findings": [
      {
        "id": "SEC-001",
        "pillar": "security",
        "title": "IAM policy with wildcard actions",
        "description": "...",
        "impact": "Severe",
        "likelihood": "Medium",
        "riskLevel": "High",
        "evidence": [{"file": "path", "line": 42, "snippet": "..."}],
        "recommendation": "...",
        "effort": "Low",
        "awsServices": ["IAM", "IAM Access Analyzer"]
      }
    ]
  }
  ```
- You MUST save the cross-pillar analysis to "{output_directory}/report/cross-pillar-analysis.md"

### 12. Generate Pillar Scorecard

Produce scores for each pillar based on evidence.

**Constraints:**
- You MUST score each pillar on a 1-5 scale using this rubric:
  - **1 — No practices implemented**: No evidence of WA best practices; fundamental gaps exist
  - **2 — Basic practices**: Some awareness, but implementation is ad-hoc and incomplete
  - **3 — Developing**: Key practices implemented but gaps remain; reactive approach
  - **4 — Mature**: Most best practices implemented proactively; minor gaps remain
  - **5 — Optimized**: All best practices implemented; continuous improvement evident

- You MUST calibrate scores against evidence:
  - Score 4-5 requires evidence of proactive implementation (monitoring, automation, testing)
  - Score 3 requires basic implementation with identifiable gaps
  - Score 1-2 indicates missing fundamental practices
  - A workload with multi-AZ, encryption, monitoring, and CI/CD should score 4+ on relevant pillars
  - Do NOT over-penalize — acknowledge strengths explicitly before gaps

- You MUST justify each score with:
  - Top 3 strengths (with file paths as evidence)
  - Top 3 gaps (with specific missing configurations)
  - Comparison to WA Framework expectations for the workload's business criticality

- You MUST save the scorecard to "{output_directory}/report/scorecard.md"

### 13. Generate Remediation Plan

Produce a prioritized remediation plan.

**Constraints:**
- You MUST categorize remediation items by timeline:

  **Quick Wins (< 1 week, Low effort)**
  - Configuration changes that don't require architecture changes
  - Enabling features that are available but not turned on
  - Adding tags, alarms, or retention policies
  - Examples: enable encryption, add CloudWatch alarms, enable versioning

  **Foundation (1-4 weeks, Medium effort)**
  - Core architectural improvements requiring some development
  - Adding missing resilience or security patterns
  - Implementing monitoring and observability
  - Examples: add multi-AZ, implement CI/CD, add caching layer

  **Strategic (1-3 months, High effort)**
  - Major architectural changes or re-designs
  - Multi-region deployment, major refactoring
  - Compliance programs or advanced automation
  - Examples: disaster recovery, cell-based architecture, zero-trust network

- For each remediation item, you MUST provide:
  - Finding ID it addresses
  - Specific implementation guidance (not generic advice)
  - IaC snippet or code change suggestion where applicable
  - AWS services involved
  - Expected risk reduction
  - Dependencies on other remediation items

- You MUST order items within each category by: risk reduction (highest first), then effort (lowest first)
- You MUST save to "{output_directory}/report/remediation-plan.md"
- You MUST generate IaC snippets for Quick Wins at "{output_directory}/report/quick-win-snippets/"

### 14. Produce Final Report

Compile all analyses into a comprehensive report.

**Constraints:**
- You MUST produce the report at "{output_directory}/report/well-architected-review.md" with this structure:

```markdown
# Well-Architected Review: {workload_name}

## Executive Summary
- **Date**: {date}
- **Workload**: {workload_name}
- **Business Criticality**: {business_criticality}
- **Lens Applied**: {lens or "General"}
- **Packages Analyzed**: {list of packages}
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Maturity**: {1-5 score with one-line justification}

## Architecture Overview
{PlantUML diagram from discovery}
{Brief description of architecture, key services, data flows}

## Pillar Scorecard
| Pillar | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| Operational Excellence | {score} | {strength} | {gap} |
| Security | {score} | {strength} | {gap} |
| Reliability | {score} | {strength} | {gap} |
| Performance Efficiency | {score} | {strength} | {gap} |
| Cost Optimization | {score} | {strength} | {gap} |
| Sustainability | {score} | {strength} | {gap} |

## Critical and High Risk Findings
{For each finding: ID, pillar, title, description, evidence (file:line), impact, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table only}

## Cross-Pillar Trade-offs
{Identified conflicts between pillars and recommended resolution}

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
{Table: Finding ID | Action | Expected Impact | Effort}

### Foundation (1-4 weeks)
{Table: Finding ID | Action | Expected Impact | Effort | Dependencies}

### Strategic (1-3 months)
{Table: Finding ID | Action | Expected Impact | Effort | Dependencies}

## Lens-Specific Findings
{If a lens was applied, additional findings specific to that lens}

## Next Steps
{Top 5 concrete actions the team should take this week}
```

- You MUST ensure every finding in the report is traceable to specific code evidence
- You MUST NOT include generic recommendations without evidence — if you cannot determine the state from code, mark it "Cannot Determine" and explain what information is needed
- You MUST acknowledge existing strengths prominently — a mature workload should feel validated, not just criticized

### 15. Verification Step

Verify completeness and accuracy of the review.

**Constraints:**
- You MUST verify:
  - All IaC files have been analyzed (cross-reference with file listing)
  - All six pillars have been evaluated
  - Every finding has at least one file:line evidence reference
  - Risk levels are consistent with the assessment matrix
  - Scores are calibrated (no pillar scored without justification)
  - Remediation plan covers all Critical and High findings
  - No duplicate findings across pillars
  - Quick Win IaC snippets are syntactically valid
  - Architecture diagram reflects actual resources found
- You MUST create a verification report at "{output_directory}/report/verification.md"
- You MUST list any areas that could not be assessed from code alone (require runtime data, interviews, or AWS console access)
- You MUST suggest follow-up actions for areas that cannot be determined from static analysis

### 16. Offer Follow-up

Present options for deeper analysis.

**Constraints:**
- You MUST offer these follow-up options:
  > Would you like me to:
  > - Deep-dive into a specific pillar with expanded analysis?
  > - Generate complete IaC templates to remediate a specific finding?
  > - Create a migration plan for a specific architectural change?
  > - Produce a WA Tool import file for tracking in the AWS console?
  > - Compare your workload against a specific WA Lens in more detail?
  > - Generate automated checks (Config rules, custom metrics) for ongoing compliance?

## Calibration Guidance

When assessing workloads:
- A workload with multi-AZ deployments, encryption at rest/transit, CI/CD with automated rollback, CloudWatch monitoring, and auto-scaling is MATURE — most findings should be improvements, not HRIs
- Do NOT manufacture Critical findings for a well-built workload — accuracy over alarm
- When business criticality is "low" or "standard", accept simpler architectures without penalizing (single-region is acceptable for internal tools)
- When business criticality is "critical", apply stricter standards (multi-region DR expected, chaos testing expected, sub-minute RTO expected)
- Always compare against what's appropriate for the workload's tier, not against a theoretical maximum
