# Well-Architected Framework

## Purpose

Guide the agent to apply AWS Well-Architected Framework principles when reviewing architectures, writing code, or advising on design decisions.

## When to Apply

Apply this steering whenever the user:
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

## Response Format

When delivering Well-Architected guidance:
- Lead with the most critical finding or recommendation
- Group findings by pillar
- Use severity labels: 🔴 High Risk, 🟡 Medium Risk, 🟢 Best Practice
- Include "Why it matters" for each finding
- Provide a concrete next step for each recommendation
