---
name: operational-excellence
description: Assess a workload's operational excellence posture by analyzing CI/CD pipelines, observability instrumentation, deployment configs, and incident management patterns in the codebase to produce evidence-backed findings.
version: 2.0.0
---

# Operational Excellence Assessment

## Step 1: Gather context

Ask the user:

> What workload or environment would you like me to assess for operational excellence? Please share:
> - **Workload name** and brief description
> - **Code packages/directories** to analyze (CI/CD configs, IaC, application code)
> - **Known operational pain points** (optional — alert fatigue, slow deployments, etc.)

If the user has already provided details or you are in a codebase, skip the prompt and proceed with discovery.

## Step 2: CI/CD and Deployment Discovery

Analyze all CI/CD and deployment configurations in the codebase.

You MUST examine:
- Pipeline definitions (CodePipeline, GitHub Actions, Jenkins, GitLab CI, CDK Pipelines)
- Deployment configurations (CodeDeploy, ECS deployment, Lambda aliases, Apollo)
- Build configurations (buildspec.yml, Makefile, package.json scripts)
- Testing configurations (unit, integration, e2e test setups)
- Pre-deployment gates (approval stages, quality gates, security scans)

For each pipeline/deployment, document:
- File path and line numbers
- Stages and their purpose
- Deployment strategy (canary, blue/green, rolling, all-at-once)
- Rollback mechanism (automatic on alarm, manual, none)
- Test coverage gates
- Artifact promotion flow

You MUST flag:
- All-at-once deployments to production without health check gating
- No rollback mechanism configured
- No automated testing in the pipeline
- Manual steps in an otherwise automated pipeline

## Step 3: Observability Discovery

Analyze all monitoring and observability configurations.

You MUST examine:
- CloudWatch alarm definitions (in IaC or config files)
- Dashboard definitions (CloudWatch dashboard JSON, Grafana configs)
- Log configurations (log groups, retention, structured logging libraries)
- Tracing configurations (X-Ray, OpenTelemetry, Jaeger)
- Custom metric publishing (CloudWatch PutMetricData, StatsD, embedded metrics)
- Synthetic canaries (CloudWatch Synthetics)
- Application-level logging (structured logging, correlation IDs, log levels)

For each observability component, document:
- What it monitors and why
- File path and line numbers
- Gaps in coverage (services without alarms, flows without tracing)

You MUST flag:
- Services or Lambda functions with no CloudWatch alarms
- Missing distributed tracing across service boundaries
- Unstructured logging (no JSON, no correlation IDs)
- No custom metrics for business-critical operations
- Log retention set to "never expire" without justification
- No synthetic canaries for critical user journeys

## Step 4: Incident and Event Management Discovery

Analyze incident response and event management configurations.

You MUST examine:
- Alert routing (SNS topics, PagerDuty/OpsGenie integrations, EventBridge rules)
- Automated remediation (Lambda functions triggered by alarms, SSM Automation)
- Runbooks and playbooks (SSM documents, markdown runbooks, Step Functions)
- Escalation configurations
- Health check implementations (ALB health checks, Route 53, custom endpoints)

## Step 5: Evaluate against WA Framework questions

For each question, provide: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

### OPS 1 — How do you determine what your priorities are?
- Look for: SLO/SLI definitions, business metric dashboards, health check endpoints
- Evidence: alarm thresholds, dashboard panels showing business metrics, README/docs with SLO targets

### OPS 2 — How do you structure your organization to support your business outcomes?
- Look for: CODEOWNERS files, clear package boundaries, ownership documentation
- Evidence: CODEOWNERS, package.json team fields, README ownership sections

### OPS 3 — How does your organizational culture support your business outcomes?
- Look for: test coverage, PR templates, contributing guides, code review configs
- Evidence: test directories, .github/PULL_REQUEST_TEMPLATE, CONTRIBUTING.md

### OPS 4 — How do you implement observability?
- Look for: structured logging with correlation IDs, distributed tracing, custom metrics, dashboards
- Evidence: logger configurations, X-Ray/OTEL SDK usage, PutMetricData calls, dashboard JSON

### OPS 5 — How do you reduce defects, ease remediation, and improve flow into production?
- Look for: automated testing (unit, integration, e2e), linting, security scanning, staged deployments
- Evidence: test files, ESLint/prettier configs, SAST tool configs, pipeline stage definitions

### OPS 6 — How do you mitigate deployment risks?
- Look for: canary/blue-green deployments, feature flags, automated rollback, deployment alarms
- Evidence: CodeDeploy deployment configs, feature flag SDK imports, rollback alarm ARNs

### OPS 7 — How do you know that you are ready to support a workload?
- Look for: runbooks for known failure modes, pre-deployment checklists, load testing, operational readiness reviews
- Evidence: SSM documents, runbook markdown files, load test scripts, readiness configs

### OPS 8 — How do you understand the health of your workload?
- Look for: composite alarms, health dashboards, dependency health tracking, SLI monitoring
- Evidence: CompositeAlarm constructs, dashboard definitions, health check endpoints

### OPS 9 — How do you understand the health of your operations?
- Look for: DORA metrics tracking, deployment success monitoring, pipeline health dashboards
- Evidence: pipeline metrics, deployment monitoring alarms, operational dashboards

### OPS 10 — How do you manage workload and operations events?
- Look for: EventBridge rules for operational events, automated remediation Lambdas, escalation configs
- Evidence: EventBridge rule definitions, remediation Lambda code, SNS topic subscriptions

## Step 6: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor (inconvenience, manual workaround exists) | Moderate (delayed detection, extended recovery time) | Severe (undetected outage, no rollback, data loss)

**Likelihood**: Low (requires unusual conditions) | Medium (possible under normal operations) | High (likely to occur during next incident or deployment)

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

## Step 7: Produce the assessment

```markdown
# Operational Excellence Assessment: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Packages Analyzed**: {list}
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Maturity**: {1-5} — {one-line justification}

## Maturity Scorecard
| Domain | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| CI/CD & Deployment | {score} | {strength} | {gap} |
| Observability | {score} | {strength} | {gap} |
| Incident Management | {score} | {strength} | {gap} |
| Change Management | {score} | {strength} | {gap} |
| Continuous Improvement | {score} | {strength} | {gap} |

## Critical and High Risk Findings
{For each: ID, domain, title, description, evidence (file:line), impact, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Domain | Title | Recommendation}

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Impact | Effort |
|---------|--------|--------|--------|
{Add alarms, fix log retention, enable rollback}

### Foundation (1-4 weeks)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Add tracing, implement canary deployments, create runbooks}

### Strategic (1-3 months)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Chaos engineering, self-healing automation, DORA metrics tracking}

## Next Steps
{Top 5 concrete actions the team should take this week}
```

## Step 8: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Deep-dive into CI/CD, observability, or incident response?
> - Generate CloudWatch alarm and dashboard IaC for gaps identified?
> - Create runbooks for specific failure modes?
> - Design a self-healing architecture for a recurring issue?
> - Implement structured logging with correlation IDs?

## Calibration Guidance

- A workload with CI/CD pipelines, automated rollback, CloudWatch alarms, and structured logging is MATURE — focus on advanced improvements (chaos, SLO-based alerting, operational reviews)
- Every finding MUST have code evidence — no generic "you should have monitoring" without checking what exists
- If something cannot be determined from code (e.g., on-call rotation quality, incident review process), mark "Cannot Determine" and explain what information is needed
- Acknowledge existing operational strengths explicitly before listing gaps
- For workloads transitioning architectures, focus on what the NEW architecture introduces as operational requirements
