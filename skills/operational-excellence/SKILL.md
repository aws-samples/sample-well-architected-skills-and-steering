---
name: operational-excellence
description: Assess a workload's operational excellence posture against the Well-Architected Operational Excellence pillar, covering organization, preparation, operation, and evolution. Use this skill when evaluating CI/CD practices, observability, incident management, runbook coverage, or operational maturity.
version: 1.1.0
---

# Operational Excellence Assessment

## Step 1: Gather context

Ask the user:

> What workload or environment would you like me to assess for operational excellence? Please share:
> - **Workload name** and brief description
> - **Team structure** (who owns operations, on-call rotation, team size)
> - **Deployment tooling** (CodePipeline, GitHub Actions, Jenkins, CDK Pipelines, etc.)
> - **Observability stack** (CloudWatch, X-Ray, Prometheus, Datadog, etc.)
> - **Incident management process** (PagerDuty, OpsGenie, manual, DevOps Agent, etc.)
> - **Known operational pain points** (optional)

If context is already provided, proceed directly.

## Step 2: Assess Organization

Evaluate:
- Is there a clear operating model with defined responsibilities?
- Are operational priorities aligned with business objectives?
- Is there an operational improvement feedback loop?
- Are operational risks identified and mitigated?
- Are compliance and governance requirements integrated into operations?

## Step 3: Assess Prepare

### CI/CD pipeline maturity
- Is infrastructure deployed via IaC? (CloudFormation, CDK, Terraform)
- Are deployments automated end-to-end?
- Is there a canary, blue/green, or rolling deployment strategy?
- Are rollback mechanisms automatic on health check failure?
- Are pipeline stages isolated with proper artifact promotion?
- Is deployment frequency tracked?

### Observability readiness
- Are the four golden signals monitored? (latency, traffic, errors, saturation)
- Are distributed traces enabled across service boundaries?
- Are structured logs emitted with correlation IDs?
- Are custom metrics published for business-critical operations?
- Are dashboards available per service with SLI/SLO tracking?
- Are synthetic canaries probing critical user journeys?

### Operational readiness
- Are runbooks documented for known failure modes?
- Are on-call rotations defined with escalation paths?
- Are game days or tabletop exercises conducted?
- Is there a pre-deployment checklist or readiness review?

## Step 4: Assess Operate

### Alerting and event management
- Are alerts actionable with runbooks linked?
- Is alert routing correct with proper escalation?
- Is alert fatigue managed? (deduplication, grouping, suppression)
- Are composite alarms used to reduce noise?
- Are severity levels defined with response SLAs?

### Incident management
- Is there a documented incident response process?
- Are incidents automatically created from alarm thresholds?
- Is there a severity classification with defined response times?
- Are automated mitigation actions configured? (Lambda, SSM, Step Functions)
- Are incident metrics measured? (MTTD, MTTR, frequency, recurrence)

### Change management
- Are all changes tracked and auditable? (CloudTrail, Config)
- Are configuration changes deployed through the same pipeline as code?
- Is there drift detection for production infrastructure?
- Are feature flags used to decouple deployment from release?
- Is there a change freeze policy for high-risk periods?

## Step 5: Assess Evolve

- Is there a blameless post-incident review process?
- Are action items from post-mortems tracked to completion?
- Are operational metrics reviewed regularly? (deployment frequency, MTTR, change failure rate)
- Are lessons learned shared across teams?
- Is there continuous improvement of runbooks and automation?
- Are manual operational tasks being automated over time?
- Is chaos engineering practiced to discover weaknesses proactively?

## Step 6: Produce the assessment

Output:

```markdown
# Operational Excellence Assessment: {Workload Name}

## Summary
- **Date**: {date}
- **Deployment frequency**: {current}
- **MTTR estimate**: {current}
- **Change failure rate**: {current or unknown}
- **Findings**: {X} Critical, {Y} High, {Z} Medium

## Maturity Scorecard
| Domain | Score (1-5) | Key Gap |
|--------|-------------|---------|
| Organization | {score} | {gap} |
| Prepare — CI/CD | {score} | {gap} |
| Prepare — Observability | {score} | {gap} |
| Prepare — Readiness | {score} | {gap} |
| Operate — Alerting | {score} | {gap} |
| Operate — Incident Mgmt | {score} | {gap} |
| Operate — Change Mgmt | {score} | {gap} |
| Evolve | {score} | {gap} |

## Critical Findings
{Each: what's wrong, blast radius, recommendation, AWS services to use, effort}

## High Findings
{Each: gap description, operational risk, remediation approach, AWS services, effort}

## Medium Findings
{Each: improvement opportunity, benefit, implementation guidance, AWS services}

## Remediation Roadmap

### Quick Wins (1-2 weeks)
{Low-effort, high-impact improvements}

### Foundation (30 days)
{Pipeline, observability, and alerting improvements}

### Advanced (90 days)
{Automation, chaos engineering, self-healing}

## Next Steps
{Concrete actions prioritized by impact}
```

## Step 7: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Deep-dive into CI/CD, observability, or incident response?
> - Create runbooks or investigation workflows for specific failure modes?
> - Generate IaC for observability or alerting improvements?
> - Design a self-healing architecture for a recurring issue?
> - Propose DORA metrics tracking for your team?
