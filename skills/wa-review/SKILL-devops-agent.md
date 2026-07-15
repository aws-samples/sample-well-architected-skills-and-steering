---
name: wa-review
description: |
  Perform a Well-Architected Framework review when:
  - A post-incident analysis reveals a structural gap (missing retry, absent
    dead-letter queue, fail-fast consumer, no circuit breaker, schema coupling)
  - A service has had two or more incidents of the same type in 30 days
  - An investigation concludes with a root cause that points to an architectural
    weakness rather than a one-off operational failure
  - A user explicitly requests a WA review, architectural assessment, or asks
    "why does this keep happening"

  Do NOT load this skill for: routine incident triage, single-pillar deep-dives,
  learning WA concepts, or migration readiness assessments.

  Produces evidence-backed findings across all 6 pillars with Eisenhower-prioritized
  remediation. Evidence comes from incident history, observable metrics, application
  logs, and source code — not from user prompts.
not_for: routine incident triage (use standard investigation flow), learning WA (use wa-builder), migration readiness (use migration-readiness), generating guardrails (use wa-guardrails)
version: 2.2.0-devops-agent
---

# Well-Architected Review — DevOps Agent Variant

This skill is optimized for the AWS DevOps Agent context: autonomous execution,
post-incident triggering, and workload evidence derived from the investigation
already in progress. No interactive checkpoints. No user prompts for workload
details.

## Step 1: Establish workload context

Do NOT ask the user for workload details. Derive them from what is already known:

- **From the incident**: ticket title, affected service, severity, recurrence history
- **From investigation findings**: root cause, affected components, timeline, blast radius
- **From observable signals**: metric history, log patterns, error rates already retrieved
- **From source code**: repository already accessed during the investigation

Construct the workload scope from this evidence. If running as part of a
post-incident review, the workload IS the service that caused the incident.

Only ask the user if none of the above is available AND this is an explicit
on-demand review with no prior investigation context.

**Determine business criticality from:**
- Severity of the incident that triggered this review (Disaster/Critical = high)
- Service name (payment, billing, authentication = critical by convention)
- Default to "high" when uncertain — err toward stricter standards

**Determine applicable lens from workload characteristics:**
- Telecom infrastructure, OSS/BSS, carrier systems → apply `telco` lens
- Event-driven messaging, queue consumers → focus on Reliability REL 9–11
- On-premises workloads with cloud observability → note hybrid gap explicitly
- Lambda-heavy, event-driven → apply `serverless-applications` lens
- LLM, RAG, AI inference → apply `generative-ai` lens

## Step 1b: Frame the review as post-incident

If this review was triggered by an incident investigation:

**Connect WA findings to the incident timeline:**
- The root cause IS a WA gap — identify which pillar and which question it falls under
- The incident recurrence rate answers REL 10 (how failure is detected and recovered)
- The MTTR from the incident answers OPS 7 (understanding operational health)

**Weight findings accordingly:**
- Gaps directly related to the root cause → Critical or High by default, regardless
  of theoretical likelihood (likelihood is proven — it already happened)
- Gaps that would have detected the incident earlier → elevate OPS findings one severity
- Gaps that would have limited blast radius → elevate REL findings one severity

**State explicitly in the Executive Summary:**

> This review was triggered by {incident ID / description}. The root cause
> ({root cause summary}) maps to {BP ID} under the {Pillar} pillar. All findings
> are assessed in the context of this proven failure mode.

## Step 2: Infrastructure Discovery

Analyze all infrastructure evidence available from the current investigation context.

When IaC is available, examine:
- CDK code (TypeScript, Python, Java, Go)
- CloudFormation templates (YAML, JSON)
- Terraform configurations (.tf files)
- SAM/Serverless Framework templates
- CI/CD pipeline definitions (CodePipeline, GitHub Actions, etc.)
- Monitoring configurations (CloudWatch alarms, dashboards)
- Deployment configurations (CodeDeploy, ECS deployment settings)

**When no IaC exists (on-premises or legacy workloads):**

Derive infrastructure evidence from:
- **Metric history**: resource utilization patterns indicate sizing and scaling approach
- **Application logs**: connection counts, error rates, timeout patterns reveal
  capacity and resilience configuration
- **Source code**: connection pool settings, retry configuration, timeout values,
  exception handling patterns are the IaC equivalent for application-layer WA

Mark infrastructure findings as "Based on observable evidence — verify in
configuration" rather than "Cannot Determine". The absence of IaC is itself
a finding under OPS 5 (infrastructure as code).

For each infrastructure component, document:
- Resource type, logical name, and configuration
- File path and line numbers where defined (or metric/log source if no IaC)
- Security-relevant configs (IAM, encryption, network)
- Resilience configs (multi-AZ, backups, scaling)
- Cost-relevant configs (instance types, capacity mode)

Create an architecture diagram in PlantUML showing major components, data flows,
and trust boundaries.

## Step 3: Application Architecture Discovery

Analyze application code for architectural patterns:
- Entry points (API handlers, event processors, scheduled tasks)
- Service communication patterns (sync/async, retries, timeouts, circuit breakers)
- Data access patterns (queries, caching, connection management)
- Error handling and resilience patterns
- Authentication/authorization logic
- Observability instrumentation (logging, tracing, metrics)

> **Discovery complete.** Proceeding with full 57-question evaluation based on
> {N files analyzed / incident evidence / {workload name}}.

## Step 4: Evaluate EVERY WA Framework question with code evidence

**CRITICAL — DO NOT PRODUCE A SHORT REVIEW.** The single most common failure mode is citing 20-30 BPs and stopping. The reference corpus contains **307 BPs across 57 questions**; a real full review MUST evaluate ALL 307. Every BP receives a status: Implemented, Partially Implemented, Not Implemented, or Not Applicable (with rationale). If you find yourself with fewer than 200 BP citations, you have not finished the review. Iterate until every BP is addressed.

Assess the workload against ALL 57 questions in the Well-Architected Framework. For each question, provide:
- **Status**: "Implemented", "Partially Implemented", "Not Implemented", "Cannot Determine"
- **Evidence**: specific file paths and line numbers (or metric/log source for non-IaC workloads)
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

**Full review** (default — always use for post-incident reviews):
- Evaluate ALL 57 questions
- Load `references/pillars/{pillar-slug}.md` per pillar (see Step 4b for parallel subagent dispatch)
- Cite specific BP IDs in findings (e.g., "SEC03-BP02: No permission boundaries defined")

**Pillar-scoped review** (when the incident clearly points to one or two pillars):
- Evaluate ONLY the questions for the affected pillars
- Load `references/pillar-playbooks/{pillar}.md` for domain-specific discovery steps
- Apply full-review depth for those pillars

### Coverage strategy — MANIFEST-FIRST, THEN PILLAR FILES

**The purpose of a full review is comprehensive BP-level coverage.** To achieve this reliably, the reference corpus is provided in TWO layers:

1. **`references/manifest.md`** (~24 KB) — Lightweight catalog of every BP ID with 1-line titles. **ALWAYS load this file first** for any full review.
2. **`references/pillars/{pillar-slug}.md`** (6 files, ~150-580 KB each) — Merged per-pillar reference containing ALL questions and full BP content for one pillar.

### Mandatory loading pattern for a full review

**Step 4a — Load the manifest (MANDATORY, 1 Read call):**

```text
Read: references/manifest.md
```

**Step 4b — Dispatch 6 parallel pillar subagents (MANDATORY for full coverage):**

**Why this pattern:** Empirical measurement shows that when a single agent tries to enumerate all 307 BPs in one response, it produces **20-60 findings and stops** — regardless of prompt strength or explicit "evaluate all 307" instructions. Dispatching **6 parallel subagents (one per pillar)** aggregates to **~307 BPs of coverage** — measured empirically at **100% (307/307)** with **zero hallucinations**.

Dispatch all 6 Task calls in a single turn (parallel execution). **Each subagent MUST return a structured markdown table** so the top-level aggregator can merge findings verbatim without paraphrasing.

**Required return format (every subagent):**

```markdown
## {Pillar} Findings

| BP ID | Status | Severity | Evidence | Recommendation |
|-------|--------|----------|----------|-----------------|
| SEC03-BP02 | Not Implemented | High | No permission boundaries found in cdk/iam.ts | Add IAM permission boundaries per role |
| SEC04-BP01 | Partially Implemented | Medium | CloudTrail on, but no S3 access logging | Enable S3 server access logging |
| ...one row per BP evaluated in this pillar... |
```

**Row requirements:**
- One row per BP evaluated (target 30-55 rows per pillar; MUST cover every BP in the pillar file)
- Status: exactly one of `Implemented` / `Partially Implemented` / `Not Implemented` / `Not Applicable`
- Severity: `Critical` / `High` / `Medium` / `Low` (or blank for Implemented/Not Applicable)
- Evidence: specific file:line references when code was analyzed, or metric/log source for non-IaC workloads
- BP ID in canonical `PILLAR##-BP##` format only

**Dispatch template:**

```text
Task(subagent_type="general-purpose",
     description="Review Operational Excellence",
     prompt="Read references/pillars/operational-excellence.md, then review the following workload ONLY for the OPS pillar. Enumerate EVERY BP in the pillar file (all 30+ BPs) — do not filter to 'top issues'. Return findings as the mandatory markdown table (columns: BP ID | Status | Severity | Evidence | Recommendation) with one row per BP. Do NOT prepend narrative summary text before the table. Workload: {workload description + incident context}")

Task(subagent_type="general-purpose",
     description="Review Security",
     prompt="Read references/pillars/security.md, then review the workload ONLY for the SEC pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Reliability",
     prompt="Read references/pillars/reliability.md, then review the workload ONLY for the REL pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Performance Efficiency",
     prompt="Read references/pillars/performance-efficiency.md, then review the workload ONLY for the PERF pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Cost Optimization",
     prompt="Read references/pillars/cost-optimization.md, then review the workload ONLY for the COST pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Sustainability",
     prompt="Read references/pillars/sustainability.md, then review the workload ONLY for the SUS pillar. [same table format, every BP as a row] Workload: {workload}")
```

**Total: 6 Task calls in one turn.** Each subagent runs independently with its own context, so each can be exhaustive without stealing from the others. The uniform table format means aggregation is a mechanical concatenation, not an interpretive summary — this prevents ~30-70% recall loss observed with narrative subagent output.

**Step 4c — Aggregate subagent findings (PRESERVE citations verbatim):**

Once all 6 subagents return, merge their findings into a single structured report. **CRITICAL**: preserve every BP citation each subagent produced. The aggregation step is a merge, NOT a summary.

**Aggregation rules — follow all of these:**
1. **Full BP Ledger required.** The report MUST contain a "Full BP Ledger" section (see Step 6) with a row per BP-status pair from every subagent. Verbatim, no paraphrase.
2. **No compression by pillar.** Do NOT reduce a subagent's 45 BP citations to "top 5 findings per pillar." Every cited BP appears in the ledger.
3. **Verify count before writing.** Count BP IDs in your assembled draft BEFORE returning. If the count is lower than the sum of subagent citations, you dropped some — go back and add them.
4. **Cross-pillar patterns and prioritization** are additive analyses that reference the ledger; they do NOT replace it.

**Coverage expectations** — a full review MUST evaluate all **307 BPs**. Every BP receives one of four statuses.

### Step 4d — MANDATORY coverage audit (do NOT skip)

Before producing the final report, perform a self-audit:

1. Count unique BP IDs evaluated (all four statuses)
2. Compare against the target: 307 BPs
3. If below 307: compare against `references/manifest.md`, add missing entries, repeat
4. Continue until every BP has an entry

**Audit output format:**

```text
## Coverage audit
- BPs evaluated: {count} / 307
- Iterations performed: {N}
- Status distribution: {implemented} Implemented, {partial} Partial, {not_impl} Not Implemented, {na} N/A
```

### When a WA Lens applies

Lenses are **additive**. When the incident or workload matches a domain, load the relevant lens after completing the core 307-BP evaluation:

- `references/lenses/telco/` — telecom workloads, 5G/edge, OSS/BSS
- `references/lenses/serverless-applications/` — Lambda, API Gateway, Step Functions
- `references/lenses/generative-ai/` — LLM workloads, RAG, fine-tuning
- `references/lenses/devops-guidance/` — CI/CD, automated governance, observability

Full lens list available in `references/lenses/`.

## Step 5: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor | Moderate | Severe (full outage, data loss, regulatory violation)

**Likelihood**: Low | Medium | High (common failure mode, weak controls)

**Post-incident adjustment**: For the root-cause finding and directly related gaps,
set Likelihood to High regardless of theoretical assessment — the incident proves it.

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

> **Assessment complete.** Producing report.

## Step 6: Produce the report

Output a structured report. If post-incident, lead the Executive Summary with the
incident connection before the standard fields.

```markdown
# Well-Architected Review: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Triggered by**: {incident ID} — {one-line root cause} → {mapped BP ID}, {Pillar}
- **Workload**: {name}
- **Business Criticality**: {level}
- **Lens Applied**: {lens or "General"}
- **Evidence Sources**: {IaC files / incident ticket / metrics / logs / source code}
- **Questions Assessed**: 57/57
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Maturity**: {1-5} — {one-line justification}

## Architecture Overview
{PlantUML diagram if available, otherwise text description}
{Key services, data flows, trust boundaries}

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
| ... | ... | ... | ... | ... |
| SUS 6 | Process and culture | {status} | {risk or N/A} | {evidence} |

{Complete this table for all 57 questions — do not truncate}

## Full BP Ledger (MANDATORY)

**This section MUST list every BP citation produced by every subagent.** Concatenate
all 6 subagent tables here, sorted by pillar then BP ID. Do NOT filter, cluster, or
paraphrase. Target row count: 250-307.

| BP ID | Pillar | Status | Severity | Evidence | Recommendation |
|-------|--------|--------|----------|----------|-----------------|
| OPS01-BP01 | Operational Excellence | {status} | {severity or blank} | {evidence} | {recommendation} |
| ... | ... | ... | ... | ... | ... |
| SUS06-BP05 | Sustainability | {status} | {severity or blank} | {evidence} | {recommendation} |

{After writing this table, count the rows and confirm the count matches the sum of
subagent rows. If not, you dropped citations — go back and add them.}

## Critical and High Risk Findings
{For each: ID, pillar, title, description, evidence, impact, recommendation, effort, AWS services.
 This section EXPANDS on rows in the Full BP Ledger — it does NOT replace them.}

## Medium Risk Findings
{Same format, condensed.}

## Low Risk Findings
{Summary table: ID | Pillar | Title | Recommendation}

## Cross-Pillar Trade-offs
{Conflicts between pillars and recommended resolution}

## Prioritize Improvements — Eisenhower Matrix

| Quadrant | Action | Findings |
|----------|--------|----------|
| **Do First** (High Importance, Low Effort) | Implement immediately | {finding IDs} |
| **Plan** (High Importance, High Effort) | Schedule in roadmap | {finding IDs} |
| **Delegate** (Low Importance, Low Effort) | Batch, assign | {finding IDs} |
| **Defer** (Low Importance, High Effort) | Revisit next iteration | {finding IDs} |

## Prioritized Remediation Plan

### Quick Wins (< 1 week) — "Do First" quadrant
| Finding | Action | SMART Goal | Owner Suggestion | Effort |
|---------|--------|-----------|-----------------|--------|

### Foundation (1-4 weeks) — "Plan" quadrant
| Finding | Action | Phases | Effort | Dependencies |
|---------|--------|--------|--------|--------------|

### Strategic (1-3 months) — "Plan" quadrant (complex)
| Finding | Action | Phases | Effort | Dependencies |
|---------|--------|--------|--------|--------------|

### Deferred — Revisit Next Iteration
{Findings in "Delegate" and "Defer" quadrants with brief justification}

## Next Steps
{Top 5 concrete actions from the "Do First" quadrant}
```

## Calibration Guidance

- A workload with multi-AZ, encryption, CI/CD with rollback, monitoring, and auto-scaling is MATURE — most findings should be improvements, not Critical
- Do NOT manufacture Critical findings for a well-built workload — accuracy over alarm
- When business criticality is "critical", apply stricter standards (multi-region DR, chaos testing, sub-minute RTO expected)
- Every finding MUST have evidence — no generic recommendations without backing
- If something cannot be determined from available evidence, say "Cannot Determine" and state what data would be needed
- For on-premises workloads, "Cannot Determine" is rarely appropriate — observable signals (metrics, logs, source code) are always available; use them

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
