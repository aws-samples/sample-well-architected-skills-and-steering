# Well-Architected Framework

## Purpose

Guide the agent to apply AWS Well-Architected Framework principles when reviewing architectures, writing code, or advising on design decisions. Route user intent to the most specific skill available.

## When to Apply

Apply this steering whenever the user:
- Asks for an architecture review or design feedback
- Requests help designing a new workload or system
- Asks about best practices for reliability, security, cost, performance, or sustainability
- Mentions "Well-Architected" or "WA review"

## Intent Routing

When the user's request involves Well-Architected topics, route to the most specific skill:

| User Intent Pattern | Route To | NOT This |
|-------------------|----------|----------|
| "security review/assessment/audit", "IAM review", "encryption check" | security-assessment | wa-review |
| "reliability/availability/failover", "single point of failure", "DR" | reliability-improvement-plan | wa-review |
| "cost/spend/budget/savings", "right-sizing", "waste" | cost-optimization-review | wa-review |
| "performance/latency/throughput", "scaling", "caching" | performance-efficiency | wa-review |
| "sustainability/carbon/green", "energy efficiency" | sustainability-optimization | wa-review |
| "operational/CI-CD/observability", "deployment strategy", "incidents" | operational-excellence | wa-review |
| "migrate/migration/7Rs", "on-prem to cloud", "lift and shift" | migration-readiness | wa-review |
| "ADR/decision record", "document our choice", "compare options" | architecture-decision-record | wa-review |
| "learn WA/teach me", "diagram", "visual roadmap" | wa-builder | wa-review |
| "full review/all pillars/comprehensive", "WA review" | wa-review | single-pillar skills |
| Ambiguous (mentions 2+ pillars equally) | wa-review | — |

### Routing Rules

1. **Specificity wins**: If the user's request clearly maps to a single pillar, route to that pillar's skill — even if they say "review"
2. **Explicit overrides**: If the user names a skill or slash command directly, use it regardless of routing table
3. **Ambiguity → ask**: If two skills could equally apply, ask one clarifying question rather than guessing
4. **Cross-pillar → wa-review**: If the request spans 3+ pillars or says "comprehensive/full/all", use wa-review

### Fallback Behavior

- If no skill clearly matches, apply the Design Principles below as general guidance
- If a skill completes and identifies gaps in another pillar, suggest the relevant skill as a follow-up
- If the user asks about a specific WA Lens (SaaS, Serverless, etc.), use wa-review with the lens applied

## Lifecycle Stages

Well-Architected work follows a cycle. Recognize which stage the user is in:

```
    ┌──────────┐     ┌──────────┐     ┌──────────┐
    │  ASSESS  │────►│REMEDIATE │────►│ VALIDATE │
    │          │     │          │     │          │
    │wa-review │     │ pillar   │     │wa-review │
    │pillar    │     │ skills   │     │ (re-run) │
    │skills    │     │ ADR      │     │          │
    └──────────┘     └──────────┘     └──────────┘
         ▲                                  │
         └──────────────────────────────────┘
```

- **Assess**: Identify gaps (wa-review, pillar skills)
- **Remediate**: Fix gaps (generate IaC, create ADRs, redesign)
- **Validate**: Re-run assessment to confirm improvements

## Shared Context Protocol

When transitioning between skills within a session, carry these context variables:

| Context Variable | Set By | Used By |
|-----------------|--------|---------|
| workload_name | First skill invoked | All subsequent skills |
| code_paths | Discovery phase of any skill | All evaluation phases |
| business_criticality | User input (Step 1 of most skills) | Risk calibration in all skills |
| pillar_findings | Any pillar skill's output | wa-review (aggregation), follow-up skills |
| risk_level | Assessment skills (risk matrix) | Remediation prioritization |
| compliance_framework | User input | security-assessment, wa-review |
| architecture_diagram | wa-review Step 2, wa-builder | All skills (visual reference) |

### Context Rules

1. **Reference prior findings**: If a pillar skill already ran, reference its findings rather than re-discovering
2. **Don't re-discover**: If infrastructure discovery was done by a previous skill in this session, reuse the inventory
3. **Extract from files**: If the user provides existing docs or previous review outputs, extract context from them to skip redundant questions

## Pillars

Always consider all six pillars when evaluating or proposing architectures:

1. **Operational Excellence** — Automate operations, make frequent small reversible changes, refine procedures, anticipate failure, learn from operational events.
2. **Security** — Implement a strong identity foundation, enable traceability, apply security at all layers, automate security best practices, protect data in transit and at rest, keep people away from data, prepare for security events.
3. **Reliability** — Automatically recover from failure, test recovery procedures, scale horizontally, stop guessing capacity, manage change through automation.
4. **Performance Efficiency** — Democratize advanced technologies, go global in minutes, use serverless architectures, experiment more often, consider mechanical sympathy.
5. **Cost Optimization** — Implement cloud financial management, adopt a consumption model, measure overall efficiency, stop spending money on undifferentiated heavy lifting, analyze and attribute expenditure.
6. **Sustainability** — Understand your impact, establish sustainability goals, maximize utilization, anticipate and adopt new more efficient offerings, use managed services, reduce downstream impact.

## Design Principles

When proposing solutions:
- Favor managed services over self-managed infrastructure
- Design for failure — assume any component can fail at any time
- Decouple components to reduce blast radius
- Use multiple Availability Zones for high availability
- Implement least-privilege access for all identities
- Automate everything that can be automated
- Use infrastructure as code for all environments
- Design for observability from day one

## Review Approach

When performing a Well-Architected review:
1. Identify the workload scope and business context
2. Evaluate each pillar systematically — do not skip pillars
3. Identify high-risk issues (HRIs) and medium-risk issues (MRIs)
4. Prioritize findings by business impact and effort to remediate
5. Provide specific, actionable recommendations with AWS service suggestions
6. Reference the relevant Well-Architected lens if the workload fits one (SaaS, Serverless, Data Analytics, Machine Learning, IoT, SAP, Games, etc.)

## Trade-off Guidance

Acknowledge trade-offs explicitly:
- Security controls may add latency — quantify the impact
- High availability increases cost — present options at different tiers
- Performance optimization may reduce portability — state the lock-in risk
- Cost optimization may reduce resilience — make the risk visible

## Conversation Style

When interacting with the user on WA topics:
- **Group related questions** rather than asking one at a time
- **Route immediately** when intent is clear — don't ask "would you like me to use the security-assessment skill?"
- **Carry context** across skill transitions without asking the user to repeat information
- **Explain routing briefly** ("I'll focus on security since you mentioned IAM and encryption")
- **Resolve ambiguity** by asking which aspect matters most, not which tool to use

## Response Format

When delivering Well-Architected guidance:
- Lead with the most critical finding or recommendation
- Group findings by pillar
- Use severity labels: 🔴 High Risk, 🟡 Medium Risk, 🟢 Best Practice
- Include "Why it matters" for each finding
- Provide a concrete next step for each recommendation

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
