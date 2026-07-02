---
name: wa-review
description: Perform a full AWS Well-Architected Framework review evaluating all 57 questions across 6 pillars by analyzing code, IaC, and configurations to produce evidence-backed findings with Eisenhower-prioritized remediation.
not_for: single-pillar deep-dives (use the specific pillar skill), learning WA (use wa-builder), ADRs (use architecture-decision-record), migration (use migration-readiness)
version: 2.1.0
---

# Well-Architected Review

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

---STOP---
**Checkpoint**: Discovery complete — present findings before evaluation.

> Here is what I discovered about your workload:
> - **Infrastructure**: {summary of IaC resources found}
> - **Architecture patterns**: {key patterns detected}
> - **Scope**: {number of files/resources analyzed}
>
> **Shall I proceed with the full 57-question evaluation, or would you like to adjust the scope?**

Do NOT proceed past this point until the user explicitly confirms.
---

## Step 4: Evaluate EVERY WA Framework question with code evidence

Assess the workload against ALL 57 questions in the Well-Architected Framework. For each question, provide:
- **Status**: "Implemented", "Partially Implemented", "Not Implemented", "Cannot Determine"
- **Evidence**: specific file paths and line numbers
- **Gaps**: what's missing or could be improved
- **Risk**: what could go wrong due to the gap

The 6 pillars and their questions:
- **Operational Excellence** (OPS 1–11): Organization, observability, deployment risk, operational readiness, event management, evolution
- **Security** (SEC 1–11): Foundations, identity, permissions, detection, network/compute protection, data protection, incident response, app security
- **Reliability** (REL 1–13): Quotas, network topology, service architecture, distributed systems, monitoring, scaling, change management, backups, fault isolation, DR
- **Performance Efficiency** (PERF 1–5): Resource selection, compute, data/storage, networking, optimization process
- **Cost Optimization** (COST 1–11): Financial management, usage governance, monitoring, decommissioning, service selection, right-sizing, pricing models, data transfer, demand management, evolution
- **Sustainability** (SUS 1–6): Region selection, demand alignment, architecture patterns, data management, hardware selection, organizational processes

### Review depth

Before starting the evaluation, determine the review depth based on the user's request:

**Full review** (default when user says "WA review", "full review", "comprehensive"):
- Evaluate ALL 57 questions
- For EACH question, load `references/questions/{QUESTION_ID}.md` and evaluate against every best practice
- Cite specific BP IDs in findings (e.g., "SEC03-BP02: No permission boundaries defined")

**Quick review** (when user says "quick review", "high-level", "summary", or time-constrained):
- Evaluate all 57 questions at the QUESTION level only (do not load individual BP reference files)
- Use the pillar summaries above to assess each question based on what you find in the code
- Flag obvious gaps but do not exhaustively check every BP
- Faster, less detailed, still covers all pillars

**Pillar-scoped review** (when user asks for specific pillars, e.g., "review security and reliability only"):
- Evaluate ONLY the questions for the requested pillars
- Apply full-review depth (load BP reference files) for those pillars
- Skip all other pillars entirely — do not comment on them unless a critical cross-pillar issue is obvious
- Still produce the same report format but only for the scoped pillars

If unclear, ask:

> Would you like a **full review** (deep BP-level analysis per question — thorough but longer) or a **quick review** (question-level assessment — faster, covers all pillars at a high level)?

### Context management strategy

The full reference corpus is ~2.2 MB (57 question files). Do NOT attempt to load all files at once. Use this two-pass, pillar-by-pillar approach:

**Pass 1 — Quick scan (no reference files loaded):**

Work through all 6 pillars sequentially (OPS → SEC → REL → PERF → COST → SUS). For each question, use your knowledge and the code discovered in Steps 2-3 to assign a preliminary status. Mark questions as:
- "Implemented" — clear evidence found, no obvious gaps
- "Gaps found" — missing or weak implementation detected
- "Cannot Determine" — not enough evidence

Produce a summary table after Pass 1 showing which questions have gaps.

**Pass 2 — Deep dive (reference files loaded selectively):**

For ONLY the questions marked "Gaps found" in Pass 1:
1. Load `references/questions/{QUESTION_ID}.md`
2. Evaluate the workload against each BP in that file
3. Record detailed findings with BP IDs, evidence, and risk
4. Move to the next flagged question — the reference file does not need to remain loaded

This typically loads 15–25 reference files instead of 57, reducing token consumption by 50–70%.

**Key rules:**
- Never load more than one question's reference file simultaneously — read, evaluate, record, move on
- Write findings as you go — do not accumulate them in memory
- After completing each pillar in Pass 2, produce that pillar's findings before starting the next
- If the user explicitly asks for a full deep-dive on ALL questions (not just gaps), follow the same sequential pattern but load every question file one at a time

### How to evaluate each question (full review)

For EACH question in a full review:

1. **Load the question file**: Read `references/questions/{QUESTION_ID}.md` (e.g., `references/questions/SEC03.md` for SEC 3). Each file contains all best practices for that question with implementation guidance, anti-patterns, and risk levels.
2. **Evaluate against every BP**: Check whether the workload implements each best practice listed in the file. Use the anti-patterns and implementation guidance to determine gaps.
3. **Record and release**: Write the finding immediately. You do not need to keep the reference file in context for subsequent questions.
4. **Cite BP IDs in findings**: When flagging a gap, reference the specific BP ID (e.g., "SEC03-BP02: No permission boundaries defined").

### When a WA Lens applies

Lenses are **additive** — they expand the core 57-question framework with domain-specific best practices. They do NOT replace the framework questions.

**When to apply a lens:**
- The workload clearly matches a lens domain (e.g., Lambda-heavy → serverless, LLM-based → generative AI)
- The user explicitly asks for a lens-specific review

**How to apply:**
- First complete the core framework evaluation (all 57 questions)
- Then load the relevant lens from `references/lenses/{lens-name}/` and evaluate additional lens-specific best practices
- Report lens findings in a separate section after the core findings

**If the user ONLY asks for a lens review** (e.g., "review my app against the serverless lens") — that is also valid. Load only the lens references and evaluate against those.

Available lenses:
- `references/lenses/serverless-applications/` — Lambda, API Gateway, Step Functions, event-driven
- `references/lenses/generative-ai/` — LLM workloads, RAG, fine-tuning, prompt engineering
- `references/lenses/agentic-ai/` — AI agents, orchestration, tool use, guardrails
- `references/lenses/responsible-ai/` — Fairness, explainability, governance, monitoring
- `references/lenses/hybrid-networking/` — Direct Connect, VPN, Transit Gateway, DNS
- `references/lenses/migration/` — Assess, Mobilize, Migrate phases per pillar
- `references/lenses/devops-guidance/` — CI/CD, automated governance, development lifecycle, observability, security testing
- `references/lenses/machine-learning/` — ML lifecycle (MLOPS), model training/deployment, data engineering, responsible ML
- `references/lenses/data-analytics/` — data pipelines, governance, data catalogs, lineage, analytics performance and cost
- `references/lenses/games-industry/` — game backends, real-time multiplayer, player data, live operations
- `references/lenses/saas/` — multi-tenancy, tenant isolation, onboarding, metering, tiering
- `references/lenses/financial-services/` — regulatory compliance, data residency, resilience, auditability for FSI workloads
- `references/lenses/life-sciences/` — GxP, validated systems, clinical/research data, regulatory compliance
- `references/lenses/end-user-computing/` — virtual desktops/apps, streaming, identity, endpoint delivery
- `references/lenses/supply-chain/` — supply chain data, integration, traceability, resilience
- `references/lenses/video-streaming-advertising/` — video pipelines, streaming delivery, ad tech, monetization
- `references/lenses/telco/` — telecom network workloads, 5G/edge, OSS/BSS, carrier-grade reliability
- `references/lenses/sap/` — SAP on AWS, S/4HANA, HANA databases, SAP landscape resilience
- `references/lenses/modern-industrial-data-technology/` — industrial data platforms, OT/IT convergence, manufacturing analytics
- `references/lenses/microsoft-workloads/` — Windows Server, SQL Server, Active Directory, .NET on AWS
- `references/lenses/connected-mobility/` — connected vehicles, telematics, fleet data, automotive platforms
- `references/lenses/healthcare-industry/` — HIPAA, clinical data, interoperability, patient privacy
- `references/lenses/container-build/` — container image builds, supply chain security, registries, CI/CD
- `references/lenses/high-performance-computing/` — HPC clusters, parallel workloads, scheduling, low-latency networking
- `references/lenses/streaming-media/` — media streaming, live/VOD delivery, encoding, content workflows
- `references/lenses/iot/` — IoT devices, telemetry, edge computing, fleet provisioning, OTA updates
- `references/lenses/government/` — public sector, privacy-by-design, compliance, real-time security

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

---STOP---
**Checkpoint**: Risk assessment complete — confirm findings before generating report.

> I have completed the assessment. Here is the summary:
> - **Critical findings**: {count}
> - **High findings**: {count}
> - **Medium findings**: {count}
> - **Low findings**: {count}
> - **Cross-pillar conflicts**: {count}
>
> **Shall I produce the full report, or would you like to discuss specific findings first?**

Do NOT proceed past this point until the user explicitly confirms.
---

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
- **Questions Assessed**: 57/57
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Maturity**: {1-5} — {one-line justification}

## Architecture Overview
{PlantUML diagram}
{Brief description of architecture, key services, data flows}

## Pillar Scorecard
| Pillar | Score (1-5) | Questions Assessed | Key Strength | Key Gap |
|--------|-------------|-------------------|--------------|---------|
| Operational Excellence | {score} | 11/11 | {strength} | {gap} |
| Security | {score} | 11/11 | {strength} | {gap} |
| Reliability | {score} | 13/13 | {strength} | {gap} |
| Performance Efficiency | {score} | 5/5 | {strength} | {gap} |
| Cost Optimization | {score} | 11/11 | {strength} | {gap} |
| Sustainability | {score} | 6/6 | {strength} | {gap} |

## Per-Question Assessment
| ID | Question | Status | Risk Level | Key Evidence |
|----|----------|--------|------------|--------------|
| OPS 1 | Priorities | {status} | {risk or N/A} | {evidence} |
| OPS 2 | Organization structure | {status} | {risk or N/A} | {evidence} |
| ... | ... | ... | ... | ... |
| SUS 6 | Process and culture | {status} | {risk or N/A} | {evidence} |

{Complete this table for all 57 questions — do not truncate}

## Critical and High Risk Findings
{For each: ID, pillar, title, description, evidence (file:line), impact assessment, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Pillar | Title | Recommendation}

## Cross-Pillar Trade-offs
{Conflicts between pillars and recommended resolution}

## Prioritize Improvements — Eisenhower Matrix

Not all findings should be addressed at once. Focus on a selected number of issues that make the most business impact and are easiest to implement. Then iterate.

Classify each finding by **importance** (business value) and **effort** (time, complexity, headcount):

```
        HIGH IMPORTANCE
             │
   ┌─────────┼─────────┐
   │  DO     │  PLAN   │
   │  FIRST  │         │
   │         │         │
───┼─────────┼─────────┼───
   │         │         │
   │DELEGATE │  DEFER  │
   │         │         │
   └─────────┼─────────┘
             │
        LOW IMPORTANCE
   LOW EFFORT    HIGH EFFORT
```

| Quadrant | Action | Findings |
|----------|--------|----------|
| **Do First** (High Importance, Low Effort) | Implement immediately | {finding IDs} |
| **Plan** (High Importance, High Effort) | Schedule in roadmap, break into phases | {finding IDs} |
| **Delegate** (Low Importance, Low Effort) | Batch together, assign to available team member | {finding IDs} |
| **Defer** (Low Importance, High Effort) | Revisit in next iteration | {finding IDs} |

### Solution Characteristics

For each solution in "Do First" and "Plan":
- **SMART goal**: Specific, Measurable, Achievable, Relevant, Time-bound
- **Owner**: Identify who is responsible
- **Simple over complex**: Choose the simplest solution unless complexity is a non-negotiable requirement
- **Two-way door decisions**: Solutions should be extensible and evolve over time — avoid static solutions that cannot adapt
- **Pattern-based**: Target solutions that can be codified, reused, and re-shared (reference AWS Architecture Center)

## Prioritized Remediation Plan

### Quick Wins (< 1 week) — "Do First" quadrant
| Finding | Action | SMART Goal | Owner Suggestion | Effort |
|---------|--------|-----------|-----------------|--------|
{Config changes, enabling features, adding tags/alarms — simple, high-impact}

### Foundation (1-4 weeks) — "Plan" quadrant
| Finding | Action | Phases | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Multi-AZ, CI/CD improvements, monitoring, caching — phased approach}

### Strategic (1-3 months) — "Plan" quadrant (complex)
| Finding | Action | Phases | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{DR, re-architecture, compliance programs — two-way door design}

### Deferred — Revisit Next Iteration
{Findings in "Delegate" and "Defer" quadrants with brief justification for deferral}

## Next Steps
{Top 5 concrete actions from the "Do First" quadrant — the team should start this week}
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
