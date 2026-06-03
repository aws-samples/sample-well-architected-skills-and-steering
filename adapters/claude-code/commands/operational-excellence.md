Assess a workload's operational excellence posture by analyzing CI/CD pipelines, observability instrumentation, deployment configs, and incident management patterns in the codebase to produce evidence-backed findings.

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for operational excellence? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Known operational pain points** (optional — alert fatigue, slow deployments, etc.)

If already in a codebase, skip the prompt and proceed with discovery.

## Step 2: CI/CD and Deployment Discovery

Analyze ALL CI/CD and deployment configurations:

- Pipeline definitions (CodePipeline, GitHub Actions, Jenkins, GitLab CI, CDK Pipelines)
- Deployment strategies (canary, blue/green, rolling, all-at-once)
- Rollback mechanisms (automatic on alarm, manual, none)
- Testing gates (unit, integration, e2e in pipeline)

Flag: all-at-once production deployments, no rollback mechanism, no automated testing, manual steps in pipelines.

## Step 3: Observability Discovery

Analyze monitoring and observability:

- CloudWatch alarms and dashboards
- Logging (structured logging, log levels, retention, correlation IDs)
- Tracing (X-Ray, OpenTelemetry)
- Custom metrics and synthetic canaries

Flag: services without alarms, unstructured logging, missing tracing across boundaries, no custom metrics, "never expire" log retention.

## Step 4: Incident and Event Management

Analyze incident response configs:

- Alert routing (SNS, PagerDuty, EventBridge rules)
- Automated remediation (Lambda/SSM triggered by alarms)
- Health check implementations
- Runbooks (SSM documents, markdown)

## Step 5: Evaluate against WA Framework questions

Every assessment MUST include: **Status** (Implemented/Partially/Not Implemented/Cannot Determine), **Evidence** (file:line), **Gaps**, **Risk**.

- **OPS 4 — Observability**: structured logging, tracing, metrics, dashboards
- **OPS 5 — Reduce defects**: automated testing, linting, staged deployments
- **OPS 6 — Deployment risk**: canary/blue-green, feature flags, rollback
- **OPS 7 — Readiness**: runbooks, load testing, operational readiness
- **OPS 8 — Workload health**: composite alarms, health dashboards, SLI monitoring
- **OPS 9 — Operations health**: DORA metrics, pipeline health, deployment success
- **OPS 10 — Event management**: EventBridge rules, automated remediation, escalation

## Step 6: Risk Assessment

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

## Step 7: Produce the report

Structure:

- Executive Summary (date, packages analyzed, findings count, overall maturity 1-5)
- Maturity Scorecard (CI/CD, Observability, Incident Management, Change Management, Continuous Improvement — each scored 1-5 with strength and gap)
- Critical and High Risk Findings (ID, domain, title, evidence file:line, impact, recommendation, effort, AWS services)
- Medium/Low Risk Findings
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- Next Steps (top 5 concrete actions)

## Calibration

- Workloads with CI/CD, rollback, alarms, and structured logging are MATURE — focus on advanced improvements
- Every finding MUST have code evidence
- "Cannot Determine" is valid for operational aspects not in code (on-call quality, incident review process)
- Acknowledge existing strengths before gaps
