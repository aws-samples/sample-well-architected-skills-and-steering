---
description: Run a full Well-Architected Framework review when the user asks for an architecture review, WA assessment, or mentions "Well-Architected review".
globs:
alwaysApply: false
---

# Well-Architected Review Skill

When the user requests a WA review, follow these steps:

## Step 1: Define scope

Ask for: workload name, architecture description, business criticality, and pain points.

## Step 2: Identify lens

Check if SaaS, Serverless, Data Analytics, ML, IoT, or other specialized lens applies.

## Step 3: Evaluate all six pillars

For each pillar, assess against key best practices:

- **Operational Excellence**: CI/CD, IaC, monitoring, runbooks, rollback
- **Security**: IAM least privilege, encryption, detection, incident response
- **Reliability**: Multi-AZ, auto-scaling, failover, health checks, circuit breakers
- **Performance Efficiency**: Right resource types, caching, CDN, async processing
- **Cost Optimization**: Right-sizing, Savings Plans, idle resources, serverless
- **Sustainability**: Utilization, managed services, data lifecycle, scale-to-zero

## Step 4: Classify findings

Assign each: severity (🔴 HRI / 🟡 MRI / 🟢 Improvement), pillar, impact, effort.

## Step 5: Output report

Use this structure:
- Summary (date, pillars reviewed, lens, finding counts)
- High Risk Issues (description, impact, recommendation, effort, AWS services)
- Medium Risk Issues
- Improvement Opportunities
- Prioritized Remediation Plan
- Next Steps
