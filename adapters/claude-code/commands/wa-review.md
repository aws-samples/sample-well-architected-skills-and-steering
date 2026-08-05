Perform a full AWS Well-Architected Framework review of the user's workload by analyzing code, IaC, and configurations to produce evidence-backed findings with prioritized remediation.

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

## Step 4: Evaluate each pillar with code evidence

For each pillar, assess against the WA Framework questions. Every assessment MUST include:
- **Status**: "Implemented", "Partially Implemented", "Not Implemented", "Cannot Determine"
- **Evidence**: specific file paths and line numbers
- **Gaps**: what's missing or could be improved
- **Risk**: what could go wrong due to the gap

### Operational Excellence
- **OPS 4 — Observability**: Look for structured logging, distributed tracing, custom metrics. Evidence: log statements, X-Ray/OTEL instrumentation.
- **OPS 5 — Reduce defects**: Look for automated testing, linting, staged deployments. Evidence: test files, CI/CD configs.
- **OPS 6 — Deployment risk**: Look for canary/blue-green, feature flags, rollback automation. Evidence: deployment config, CodeDeploy settings.
- **OPS 8 — Workload health**: Look for health dashboards, composite alarms. Evidence: alarm definitions, health checks.
- **OPS 10 — Event management**: Look for event routing, automated remediation. Evidence: EventBridge rules, Lambda remediations.

### Security
- **SEC 3 — Permissions**: Look for least privilege, permission boundaries. Flag any `"Action": "*"` or `"Resource": "*"` on mutating actions.
- **SEC 5 — Network protection**: Look for VPC design, security groups, WAF, VPC endpoints. Flag `0.0.0.0/0` on non-443/80 ports.
- **SEC 8 — Data at rest**: Look for encryption on ALL stores. Flag any storage resource without encryption.
- **SEC 9 — Data in transit**: Look for TLS enforcement. Flag TLS < 1.2.
- **SEC 2/3 — Identity**: Look for IAM roles, trust relationships, credential management. Flag hardcoded secrets.

### Reliability
- **REL 2 — Network topology**: Look for multi-AZ deployment, subnet distribution.
- **REL 3 — Demand adaptation**: Look for auto-scaling, capacity modes. Flag compute without scaling.
- **REL 4 — Distributed system interactions**: Look for retries with backoff, timeouts, idempotency.
- **REL 9 — Data backup**: Look for automated backups, PITR. Flag stateful resources without backups.
- **REL 11 — Component failures**: Look for redundancy, failover, health-based routing.
- **REL 13 — Disaster recovery**: Look for cross-region resources, DR automation.

### Performance Efficiency
- **PERF 1 — Resource selection**: Look for instance type justification, Graviton usage.
- **PERF 2 — Compute solution**: Look for right-sizing, memory/CPU alignment.
- **PERF 4 — Database solution**: Look for read replicas, connection pooling (RDS Proxy, DAX).
- **PERF 5 — Networking**: Look for CloudFront, VPC endpoints, edge caching.
- **PERF 8 — Tradeoffs**: Look for caching, async patterns, eventual consistency.

### Cost Optimization
- **COST 4 — Decommission resources**: Look for lifecycle policies, retention configs. Flag "never expire" logs.
- **COST 5 — Service selection**: Look for pricing model alignment. Flag over-provisioned resources.
- **COST 6 — Right-sizing**: Look for scaling boundaries, capacity allocation.
- **COST 8 — Data transfer**: Look for VPC endpoints vs NAT Gateway, cross-region patterns.

### Sustainability
- **SUS 2 — User behavior patterns**: Look for scale-to-zero, scheduled scaling.
- **SUS 4 — Data patterns**: Look for tiering, lifecycle management, compression.
- **SUS 5 — Hardware patterns**: Flag x86 where Graviton is available. Note managed service usage.

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
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Maturity**: {1-5} — {one-line justification}

## Architecture Overview
{PlantUML diagram}
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
{For each: ID, pillar, title, description, evidence (file:line), impact assessment, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Pillar | Title | Recommendation}

## Cross-Pillar Trade-offs
{Conflicts between pillars and recommended resolution}

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Impact | Effort |
|---------|--------|--------|--------|
{Config changes, enabling features, adding tags/alarms}

### Foundation (1-4 weeks)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Multi-AZ, CI/CD improvements, monitoring, caching}

### Strategic (1-3 months)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{DR, re-architecture, compliance programs, advanced automation}

## Next Steps
{Top 5 concrete actions the team should take this week}
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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
