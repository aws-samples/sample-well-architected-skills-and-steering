# Operational Excellence Pillar — Deep-Dive Discovery Playbook

When wa-review is scoped to the Operational Excellence pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

## CI/CD and Deployment

Examine:
- Pipeline definitions (CodePipeline, GitHub Actions, Jenkins, GitLab CI, CDK Pipelines)
- Deployment configurations (CodeDeploy, ECS deployment, Lambda aliases)
- Build configurations (buildspec.yml, Makefile, package.json scripts)
- Testing configurations (unit, integration, e2e test setups)
- Pre-deployment gates (approval stages, quality gates, security scans)

For each pipeline, document:
- Stages and purpose
- Deployment strategy (canary, blue/green, rolling, all-at-once)
- Rollback mechanism (automatic on alarm, manual, none)
- Test coverage gates
- Artifact promotion flow

Flag:
- All-at-once deployments to production without health check gating
- No rollback mechanism configured
- No automated testing in the pipeline
- Manual steps in an otherwise automated pipeline

## Observability

Examine:
- CloudWatch alarm definitions (in IaC or config)
- Dashboard definitions (CloudWatch, Grafana)
- Log configurations (log groups, retention, structured logging)
- Tracing configurations (X-Ray, OpenTelemetry)
- Custom metric publishing (PutMetricData, embedded metrics)
- Synthetic canaries (CloudWatch Synthetics)
- Application-level logging (structured logging, correlation IDs, log levels)

Flag:
- Services or Lambda functions with no CloudWatch alarms
- Missing distributed tracing across service boundaries
- Unstructured logging (no JSON, no correlation IDs)
- No custom metrics for business-critical operations
- Log retention set to "never expire" without justification
- No synthetic canaries for critical user journeys
- Average-only metrics (hides tail latency issues)

## Incident and Event Management

Examine:
- Alert routing (SNS topics, PagerDuty/OpsGenie integrations, EventBridge rules)
- Automated remediation (Lambda triggered by alarms, SSM Automation)
- Runbooks and playbooks (SSM documents, markdown runbooks, Step Functions)
- Escalation configurations
- Health check implementations (ALB, Route 53, custom endpoints)

Flag:
- No alert routing to a notification channel
- No automated remediation for known failure modes
- No runbooks for critical components
- Health checks that only verify HTTP 200 (no deep checks)

## Operational Excellence-Specific Report Format

When producing a pillar-scoped operational excellence report, include:
- **Maturity Scorecard** with 5 domains: CI/CD & Deployment, Observability, Incident Management, Change Management, Continuous Improvement
- Focus on DORA-style metrics where inferable: deployment frequency, lead time, failure rate, MTTR
- Highlight the gap between "what exists" and "Operational Readiness Review" standard

## Calibration

- If something cannot be determined from code (e.g., on-call rotation quality, incident review process), mark "Cannot Determine"
- For workloads transitioning architectures, focus on what the NEW architecture introduces as operational requirements
- Acknowledge existing operational strengths before listing gaps
