# Well-Architected Framework

## When to Apply

Apply this guidance whenever the user:
- Asks for an architecture review or design feedback
- Requests help designing a new workload or system
- Asks about best practices for reliability, security, cost, performance, or sustainability
- Mentions "Well-Architected" or "WA review"

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

## Trade-off Guidance

Acknowledge trade-offs explicitly:
- Security controls may add latency — quantify the impact
- High availability increases cost — present options at different tiers
- Performance optimization may reduce portability — state the lock-in risk
- Cost optimization may reduce resilience — make the risk visible

## Response Format

When delivering Well-Architected guidance:
- Lead with the most critical finding or recommendation
- Group findings by pillar
- Use severity labels: 🔴 High Risk, 🟡 Medium Risk, 🟢 Best Practice
- Include "Why it matters" for each finding
- Provide a concrete next step for each recommendation

## Skills

Well-Architected skills are available as reusable playbooks in the `skills/` directory. If the user requests a specific audit or plan (e.g. WA review, security assessment, reliability improvement plan), locate and follow the step-by-step instructions in the corresponding skill directory:

**Core skills:**
- [aws-well-architected-framework-review](../../skills/aws-well-architected-framework-review/SKILL.md) — Full or pillar-scoped Well-Architected review (all 6 pillars supported as deep-dives)
- [wa-builder](../../skills/wa-builder/SKILL.md) — Learn Well-Architected for your workload and generate visual artifacts: annotated diagrams, decision trees, roadmaps, ADRs
- [wa-guardrails](../../skills/wa-guardrails/SKILL.md) — Generate preventive guardrails: Config rules, SCPs, CI policy checks, and alarms that keep a workload aligned with Well-Architected best practices over time
- [wafr-facilitator](../../skills/wafr-facilitator/SKILL.md) — Prepare conversational Well-Architected Framework Review facilitation with customers
- [migration-readiness](../../skills/migration-readiness/SKILL.md) — 7 Rs migration readiness assessment

**Pillar-scoped variants** route to `aws-well-architected-framework-review` with a single-pillar focus — security assessment, reliability improvement plan, cost optimization review, performance efficiency review, sustainability optimization, and operational excellence — while an architecture decision record maps to `wa-builder`'s ADR mode.

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
