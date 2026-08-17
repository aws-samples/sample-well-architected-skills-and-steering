---
name: aws-well-architected-framework-review
description: Perform a full AWS Well-Architected Framework review evaluating all 57 questions across 6 pillars by analyzing code, IaC, and configurations to produce evidence-backed findings with Eisenhower-prioritized remediation.
not_for: single-pillar deep-dives (use the specific pillar skill), learning WA (use wa-builder), ADRs (use architecture-decision-record), migration (use migration-readiness)
version: 2.3.0
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

**IMPORTANT**: When no code or IaC is available to analyze (e.g., the user describes their architecture verbally), proceed with the review based on the information provided. Produce the full report using explicit statements in the architecture description as evidence. Treat omitted details as unknown, not as evidence that a control is absent. Mark unverifiable implementation details `Cannot Determine`, state what evidence would resolve them, and do NOT ask for code if the user has already given you enough context to perform a meaningful review.

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

Record the workload's **primary IaC dialect** (CDK, CloudFormation, Terraform, or SAM) — Step 6 emits a per-finding **Fix:** block in this dialect. When the workload has no IaC, note that fix blocks will fall back to AWS CLI commands.

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

**CRITICAL — DO NOT PRODUCE A SHORT REVIEW.** The single most common failure mode is citing 20-30 BPs and stopping. The reference corpus contains **307 BPs across 57 questions**; a real full review MUST evaluate ALL 307. Every BP receives one of five statuses: Implemented, Partially Implemented, Not Implemented, Not Applicable, or Cannot Determine (with rationale). If you find yourself with fewer than 200 BP citations, you have not finished the review. Iterate until every BP is addressed.

Assess the workload against ALL 57 questions in the Well-Architected Framework. For each question, provide:
- **Status**: "Implemented", "Partially Implemented", "Not Implemented", "Not Applicable", "Cannot Determine"
- **Evidence**: specific file paths and line numbers
- **Gaps**: what's missing or could be improved
- **Risk**: what could go wrong due to the gap

### Evidence sufficiency gate

Assign a status only after applying this gate:

- **Implemented** — explicit evidence demonstrates the complete BP.
- **Partially Implemented** — explicit evidence demonstrates part of the BP and identifies a concrete gap.
- **Not Implemented** — explicit evidence states the control is absent, or an authoritative and sufficiently complete source was examined where the control would have to appear and it is absent.
- **Not Applicable** — the BP is outside the workload scope; provide a workload-specific rationale.
- **Cannot Determine** — available evidence is missing, inconclusive, runtime-only, or outside the inspected scope. State the exact artifact, metric, configuration, or interview answer needed to decide.

Absence of evidence is not evidence of absence. A verbal description omitting a control, or code/IaC that is not authoritative for that control, MUST result in `Cannot Determine`, not `Not Implemented`. For example, "no backups configured" supports `Not Implemented`; no mention of control objectives or TCO analysis supports only `Cannot Determine`.

Leave severity blank for `Implemented`, `Not Applicable`, and `Cannot Determine`. For `Cannot Determine`, provide a verification action rather than a remediation finding. Do not convert uncertainty into a High or Critical finding.

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
- Load `references/pillars/{pillar-slug}.md` per pillar (see Step 4b for parallel subagent dispatch); each pillar file contains every question and every best practice for that pillar
- Cite specific BP IDs in findings (e.g., "SEC03-BP02: No permission boundaries defined")

**Quick review** (when user says "quick review", "high-level", "summary", or time-constrained):
- Evaluate all 57 questions at the QUESTION level only (do not load individual BP reference files)
- Use the pillar summaries above to assess each question based on what you find in the code
- Flag obvious gaps but do not exhaustively check every BP
- Faster, less detailed, still covers all pillars

**Pillar-scoped review** (when user asks for specific pillars, e.g., "review security and reliability only", "assess my security", "identify single points of failure", "optimize our costs"):
- Evaluate ONLY the questions for the requested pillars
- Load `references/pillar-playbooks/{pillar}.md` to apply domain-specific discovery steps (specialized evidence collection beyond generic infrastructure scan)
- Apply full-review depth (load BP reference files) for those pillars
- Skip all other pillars entirely — do not comment on them unless a critical cross-pillar issue is obvious
- Produce a pillar-focused report with domain-specific scorecard (e.g., Security: 6-domain scorecard; Reliability: SPOF table + testing plan)

Trigger phrases that indicate pillar-scoped review:
- Security: "security assessment", "IAM review", "encryption audit", "assess my security posture"
- Reliability: "reliability plan", "identify SPOFs", "assess disaster recovery", "fault tolerance review"
- Cost: "cost optimization", "right-sizing review", "reduce AWS spend", "cost assessment"
- Performance: "performance assessment", "latency analysis", "bottleneck identification"
- Sustainability: "sustainability review", "carbon footprint", "resource efficiency audit"
- Operational Excellence: "operational assessment", "CI/CD review", "observability audit"

**Score mode** (when user asks for "score", "grade", "scorecard", "matrix", or "just give me a number"):
- Analyze the codebase at the provided path
- Run a quick-scan pass across all 57 questions (no BP reference files loaded)
- Produce ONLY a structured scorecard + filtered findings — no full narrative report
- Respect depth parameter:
  - "critical only" → show only Critical findings
  - "critical and high" → show Critical + High
  - "all" (default if unspecified) → show Critical + High + Medium + Low
- Output format:

```markdown
## WA Score: {workload_name}

**Overall: {X.X}/5** | OPS: {}/5 | SEC: {}/5 | REL: {}/5 | PERF: {}/5 | COST: {}/5 | SUS: {}/5

| Pillar | Score | Critical | High | Medium | Low |
|--------|-------|----------|------|--------|-----|
| Operational Excellence | {1-5} | {n} | {n} | {n} | {n} |
| Security | {1-5} | {n} | {n} | {n} | {n} |
| Reliability | {1-5} | {n} | {n} | {n} | {n} |
| Performance Efficiency | {1-5} | {n} | {n} | {n} | {n} |
| Cost Optimization | {1-5} | {n} | {n} | {n} | {n} |
| Sustainability | {1-5} | {n} | {n} | {n} | {n} |

### Findings ({depth} and above)
| # | Pillar | Severity | Finding | Evidence |
|---|--------|----------|---------|----------|
| 1 | {pillar} | {Critical/High/...} | {one-line finding} | {file:line} |
...

### Summary
{1-2 sentence takeaway: overall posture + single most impactful action}
```

Trigger phrases: "score my app", "WA scorecard", "grade this", "give me a score matrix", "how does my architecture score"

If unclear, ask:

> Would you like a **full review** (deep BP-level analysis per question — thorough but longer), a **quick review** (question-level assessment — faster), or a **score** (just the scorecard + top findings)?

### Coverage strategy — MANIFEST-FIRST, THEN PILLAR FILES

**The purpose of a full review is comprehensive BP-level coverage.** To achieve this reliably, the reference corpus is provided in THREE layers:

1. **`references/manifest.md`** (~24 KB) — Lightweight catalog of every BP ID with 1-line titles. **ALWAYS load this file first** for any full review. It shows you the complete universe of 307 BPs to cite from.
2. **`references/pillars/{pillar-slug}.md`** (6 files, ~150-580 KB each) — Merged per-pillar reference containing ALL questions and full BP content for one pillar. Load these to get full BP detail (implementation guidance, anti-patterns, resources).
3. **`references/pillar-playbooks/{pillar}.md`** (6 files, ~3-5 KB each) — Domain-specific evidence-collection guide for one pillar: what resources to examine, what patterns to flag as HIGH RISK, and a pillar-specific report format. Each full-review subagent loads its pillar's playbook (Step 4b) so findings are backed by concrete file:line evidence rather than generic BP restatements.

### Mandatory loading pattern for a full review

**Step 4a — Load the manifest (MANDATORY, 1 Read call):**

```
Read: references/manifest.md
```

This gives you every BP ID and title in ~24 KB.

**Step 4b — Dispatch 6 parallel pillar subagents (MANDATORY for full coverage):**

**Why this pattern:** Empirical measurement shows that when a single agent tries to enumerate all 307 BPs in one response, it produces **20-60 findings and stops** — regardless of prompt strength, retrieval strategy (local files, MCP, or hybrid), or explicit "evaluate all 307" instructions. This is a stable behavioral equilibrium of the model's concision priors.

**The fix:** narrow scope per subagent. When one agent reviews ONE pillar, it naturally enumerates the pillar's 30-55 BPs. Dispatching **6 parallel subagents (one per pillar)** aggregates to **~307 BPs of coverage** — measured empirically at **100% (307/307)** in evals/study_mcp with **zero hallucinations**.

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
- Status: exactly one of `Implemented` / `Partially Implemented` / `Not Implemented` / `Not Applicable` / `Cannot Determine`
- Severity: `Critical` / `High` / `Medium` / `Low` (or blank for Implemented/Not Applicable/Cannot Determine)
- Evidence: specific file:line references when code was analyzed, an explicit quoted fact when reviewing verbally, or `Cannot Determine — need {specific evidence}`
- BP ID in canonical `PILLAR##-BP##` format only

Append this exact calibration rule to every pillar subagent prompt:

> Apply the evidence sufficiency gate: omitted or inconclusive information is Cannot Determine, not Not Implemented. Use Not Implemented only for an explicitly absent control or absence from an authoritative source where the control must appear. Leave severity blank for Cannot Determine and state the specific evidence needed.

**Dispatch template:**

```
Task(subagent_type="general-purpose",
     description="Review Operational Excellence",
     prompt="Read references/pillars/operational-excellence.md and references/pillar-playbooks/operational-excellence.md (domain-specific evidence-collection checklist: what to examine and what to flag as HIGH RISK), then review the following workload ONLY for the OPS pillar. Enumerate EVERY BP in the pillar file (all 30+ BPs) — do not filter to 'top issues'. Return findings as the mandatory markdown table (columns: BP ID | Status | Severity | Evidence | Recommendation) with one row per BP. Do NOT prepend narrative summary text before the table. Workload: {workload description + code}")

Task(subagent_type="general-purpose",
     description="Review Security",
     prompt="Read references/pillars/security.md and references/pillar-playbooks/security.md (domain-specific evidence-collection checklist), then review the workload ONLY for the SEC pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Reliability",
     prompt="Read references/pillars/reliability.md and references/pillar-playbooks/reliability.md (domain-specific evidence-collection checklist), then review the workload ONLY for the REL pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Performance Efficiency",
     prompt="Read references/pillars/performance-efficiency.md and references/pillar-playbooks/performance-efficiency.md (domain-specific evidence-collection checklist), then review the workload ONLY for the PERF pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Cost Optimization",
     prompt="Read references/pillars/cost-optimization.md and references/pillar-playbooks/cost-optimization.md (domain-specific evidence-collection checklist), then review the workload ONLY for the COST pillar. [same table format, every BP as a row] Workload: {workload}")

Task(subagent_type="general-purpose",
     description="Review Sustainability",
     prompt="Read references/pillars/sustainability.md and references/pillar-playbooks/sustainability.md (domain-specific evidence-collection checklist), then review the workload ONLY for the SUS pillar. [same table format, every BP as a row] Workload: {workload}")
```

**Total: 6 Task calls in one turn.** Each subagent runs independently with its own context, so each can be exhaustive without stealing from the others. The uniform table format means aggregation is a mechanical concatenation, not an interpretive summary — this prevents ~30-70% recall loss observed with narrative subagent output.

**Cost/latency:** ~3-4x the tokens of a single-agent review (each subagent duplicates workload context), but wall-clock is bounded by the slowest single pillar (~2-3 min). Users trade cost for coverage.

**When to skip subagent dispatch:**
- User explicitly asked for **quick review** / **score mode** / **pillar-scoped review** — those modes stay single-agent
- **Cost-constrained** environments where 3-4x token usage is unacceptable — do a single-agent review but be honest with the user that coverage will be ~50-60 BPs, not 307

**Step 4c — Aggregate subagent findings (PRESERVE citations verbatim):**

Once all 6 subagents return, merge their findings into a single structured report. **CRITICAL**: preserve every BP citation each subagent produced. The aggregation step is a merge, NOT a summary — do not paraphrase, cluster, or omit BP citations that a subagent surfaced. Empirical measurement shows the assembly step is where recall is typically lost: subagents surface 250-307 BPs but naive aggregation collapses to 60-90 in the final report.

**Aggregation rules — follow all of these:**
1. **Full BP Ledger required.** The report MUST contain a "Full BP Ledger" section (see Step 6) with a row per BP-status pair from every subagent. If subagent A cited `SEC03-BP02` as Not Implemented, that row appears in the ledger — verbatim, no paraphrase.
2. **No compression by pillar.** Do NOT reduce a subagent's 45 BP citations to "top 5 findings per pillar" in the final output. Every cited BP appears in the ledger. High-severity findings ALSO get a full-detail narrative in the "Critical and High Risk Findings" section, but that is IN ADDITION to the ledger, never instead of it.
3. **Verify count before writing.** Count BP IDs in your assembled draft (in `PILLAR##-BP##` format) BEFORE returning. If the count is lower than the sum of subagent citations, you dropped some — go back and add them.
4. **Cross-pillar patterns and prioritization** are additive analyses that reference the ledger; they do NOT replace it.

For each BP citation, the ledger row shows:
- **Implemented** — the workload demonstrates this BP (cite the BP + evidence)
- **Partially Implemented** — some coverage, gaps exist (cite the BP + gap)
- **Not Implemented** — explicit or authoritative evidence demonstrates that the workload lacks this BP
- **Not Applicable** — this BP doesn't apply to the workload's context (explain why briefly)
- **Cannot Determine** — evidence is insufficient to decide (state the specific evidence needed)

**Coverage expectations** — a full review MUST evaluate all **307 BPs**. Every BP receives one of five statuses. `Cannot Determine` counts as evaluated coverage; exhaustive coverage does not require inventing a determinate status. `Not Implemented` for an evidenced absence is a valid, valuable finding.

### Step 4d — MANDATORY coverage audit (do NOT skip)

**Before producing the final report**, you MUST perform a self-audit and iterate if coverage is incomplete:

1. **Count**: How many unique BP IDs have you evaluated so far (in canonical `PILLAR##-BP##` format)? Count all five statuses — Implemented, Partially Implemented, Not Implemented, Not Applicable, AND Cannot Determine.
2. **Compare against the target**: A full review evaluates ALL **307 BPs** in the manifest. Anything less is incomplete.
3. **If your evaluated count is below 307**, you MUST NOT proceed to the final report. Instead, iterate:
   - Compare your evaluated set against the full 307-BP list in `references/manifest.md`
   - For each un-evaluated BP, load the corresponding pillar file if not already loaded, then add an entry (Implemented / Partially Implemented / Not Implemented / N/A / Cannot Determine)
   - Repeat the count check.
4. **Continue iterating** until every one of the 307 BPs has an entry. If a BP is genuinely N/A (e.g., serverless-specific BP for a container workload), mark it N/A with a one-line rationale — do not silently skip.

**Why this matters:** The default agent behavior is to cite the 20-30 most salient findings and stop. That produces a superficial review that misses systemic gaps. The value of the WA corpus is comprehensive coverage — every BP evaluated, every gap surfaced. A customer paying for a WA review expects the full 307-BP assessment, not the model's top-of-mind list.

**Audit output format** (include in your final report before the executive summary):

```
## Coverage audit
- BPs evaluated: {count} / 307
- Iterations performed: {N}
- Status distribution: {implemented} Implemented, {partial} Partial, {not_impl} Not Implemented, {na} N/A, {cannot_determine} Cannot Determine
```

If `BPs evaluated` is less than 307, you have not finished the review — go back to Step 4d.

### When economy matters — quick review mode

If the user explicitly asks for a **quick review**, a **high-level summary**, a **score**, or is time-constrained, load ONLY `references/manifest.md` (24 KB) and cite BPs at question-level or by ID without loading pillar files. This gives you canonical BP IDs but skips the deep implementation content.

### Pillar-scoped review

For a single-pillar review, load `references/manifest.md` + only that pillar's file (e.g., `references/pillars/security.md`).

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
- `references/lenses/mergers-and-acquisitions/` — M&A due diligence, multi-account/multicloud governance, integration, technical debt, post-acquisition cost & security
- `references/lenses/maori-data/` — Māori data governance, data sovereignty, Te Ao Māori principles, indigenous data protection & retention

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

## Full BP Ledger (MANDATORY)

**This section MUST list every BP citation produced by every subagent.** Concatenate all 6 subagent tables here, sorted by pillar then BP ID. Do NOT filter, cluster, or paraphrase. If a subagent surfaced 45 BPs for its pillar, this ledger shows 45 rows for that pillar. Target row count: 250-307 (one row per BP evaluated across all pillars).

Empirical measurement shows this section is where recall reaches the user. Skipping it or truncating it drops final-report recall from ~1.00 (what the subagents surface) to ~0.30 (what the assembler compresses to). **Do not skip this section.**

| BP ID | Pillar | Status | Severity | Evidence | Recommendation |
|-------|--------|--------|----------|----------|-----------------|
| OPS01-BP01 | Operational Excellence | {status} | {severity or blank} | {evidence} | {recommendation} |
| OPS01-BP02 | Operational Excellence | {status} | {severity or blank} | {evidence} | {recommendation} |
| ... | ... | ... | ... | ... | ... |
| SUS06-BP05 | Sustainability | {status} | {severity or blank} | {evidence} | {recommendation} |

{After writing this table, count the rows and confirm the count matches the sum of subagent rows. If not, you dropped citations — go back and add them.}

## Critical and High Risk Findings
{For each: ID, pillar, title, description, evidence (file:line), impact assessment, recommendation, **Fix:** block (see "Fix blocks" below), effort, AWS services. This section EXPANDS on rows in the Full BP Ledger — it does NOT replace them.}

## Medium Risk Findings
{Same format, condensed — each finding still carries its **Fix:** block. Also references ledger rows.}

## Low Risk Findings
{Summary table: ID | Pillar | Title | Recommendation. Also references ledger rows.}

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

### Fix blocks — ready-to-copy remediation snippets

Every 🔴 Critical/High and 🟡 Medium finding in the report MUST include a **Fix:** block — a minimal, ready-to-copy remediation snippet the user can apply themselves:

- **Language-matched.** Emit the snippet in the primary IaC dialect recorded in Step 2 (CDK / CloudFormation / Terraform / SAM). When the workload has no IaC (e.g., a verbal review), fall back to equivalent AWS CLI commands.
- **Evidence-grounded.** Use the actual resource names and identifiers from the finding's evidence — not generic placeholders — whenever the source is available.
- **Minimal.** Only the lines needed to close the gap; elide unchanged surrounding configuration with a comment.
- **Report-only.** The fix appears in the report for the user to review and apply. Do NOT apply it to the user's codebase and do NOT emit it as a diff/patch (repo design principle: review and guidance, not code mutation). The JSON artifact's `recommendation` field (Step 6b) stays prose-only; fix blocks live in the markdown report.
- **Reuse anti-pattern examples.** When a finding matches a named anti-pattern from the pillar playbooks, start from that entry's Right example.
- **Scope.** Applies to full and pillar-scoped reports. Score mode and quick review stay snippet-free, and the Full BP Ledger table stays snippet-free — fixes belong in the findings sections.

Example (finding SEC08-BP02, Terraform workload, evidence `infra/rds.tf:12`):

**Fix:**
```hcl
# infra/rds.tf — aws_db_instance.orders (line 12)
resource "aws_db_instance" "orders" {
  # ...existing configuration...
  storage_encrypted = true
}
```

## Step 6b: Emit structured output (`aws-well-architected-framework-review.json`)

After the markdown report, ALSO emit a machine-readable `aws-well-architected-framework-review.json` so the review can be
diffed over time (CI gate), aggregated across workloads, or imported into the WA Tool. The
markdown is for humans; this artifact is for tools. Conform to the versioned contract in
[`schemas/aws-well-architected-framework-review-v1.schema.json`](../../schemas/aws-well-architected-framework-review-v1.schema.json).

Write it to `aws-well-architected-framework-review.json` in the workload root (or a path the user names). Populate it from the
same findings you just reported — do NOT re-run the analysis, just serialize what the Full BP
Ledger already contains.

**Rules:**
- One `findings` entry per BP you evaluated, including `implemented` and `not_applicable` ones. A
  consumer must be able to tell an evaluated-and-passed BP from one that was never assessed, so do
  not drop the passing rows.
- For a core-framework BP, `bp_id` MUST be canonical `PILLAR##-BP##` — it is the identity key a
  baseline diff pairs on. Most lens BPs also publish a canonical ID (e.g. `IOTCOST01-BP01`); use it.
- Some lenses are organized by topic and expose NO BP ID (serverless-applications, saas,
  government, healthcare-industry, container-build, sap, streaming-media, and a few mixed cases).
  For a finding from one of those, OMIT `bp_id` and give a `title` (plus `lens`). A title is not a
  stable key, so these findings are reported as advisory and are never gated. Do not invent a BP
  ID to satisfy the diff; that produces keys that drift between reviews.
- Set `review_mode` to the depth you actually ran (`full`, `quick`, `pillar-scoped`, `score`). A
  non-full run does not cover all 307 BPs; say so in `recall_note`.
- Set `skill_version` to this skill's frontmatter `version`, and generate a unique `run_id`
  (e.g. `{date}T{time}-{workload-slug}`) so two same-day reviews stay distinguishable.
- Every gap (`not_implemented` / `partially_implemented`) MUST carry a `severity`
  (`critical`/`high`/`medium`/`low`). The CI gate ranks by severity, so an unrated gap fails the
  build closed. Leave `severity` off only for `implemented` / `not_applicable` / `cannot_determine`.
- `recall_note` MUST state that coverage is high-recall but not exhaustive (aws-well-architected-framework-review measures
  F1 ~0.96), so downstream gates never read a missing finding as proof a control exists.
- `recommendation` stays prose guidance — never a code diff (repo design principle).

**Shape** (see the schema for the authoritative, complete definition):

```json
{
  "schema_version": "1.0.0",
  "workload": "{workload name}",
  "date": "{YYYY-MM-DD}",
  "review_mode": "full",
  "skill_version": "2.3.0",
  "run_id": "{date}T{time}-{workload-slug}",
  "lens": ["{lens-name}"],
  "business_criticality": "{critical|high|standard|low}",
  "pillar_scores": {
    "operational_excellence": 3, "security": 2, "reliability": 2,
    "performance_efficiency": 3, "cost_optimization": 4, "sustainability": 3
  },
  "findings": [
    {
      "bp_id": "SEC08-BP01",
      "pillar": "security",
      "status": "not_implemented",
      "severity": "high",
      "evidence": { "file": "infra/s3.tf", "line": 14 },
      "effort": "low",
      "recommendation": "Enable SSE and BlockPublicAccess on the uploads bucket."
    },
    {
      "title": "Use asynchronous invocation for non-critical Lambda work",
      "lens": "serverless-applications",
      "pillar": "performance_efficiency",
      "status": "not_implemented",
      "severity": "medium",
      "recommendation": "Move the notification path to async invocation so the request path is not blocked."
    }
  ],
  "recall_note": "Full review, F1 approx 0.96. High recall but not exhaustive; absence of a finding is not proof of implementation."
}
```

The second finding above shows a topic-organized lens finding: no `bp_id`, a `title` instead. It
is advisory (reported, not gated).

Once written, mention the file and point the user at CI use:

> I have also written `aws-well-architected-framework-review.json` (machine-readable, conforms to `schemas/aws-well-architected-framework-review-v1.schema.json`).
> Commit it as `.well-architected/baseline.json` and wire `tools/wa-ci` into your pipeline to gate
> future PRs on the Well-Architected delta.

## Step 7: Offer follow-up

After delivering the report, offer:

> Would you like me to:
> - Deep-dive into a specific pillar with expanded analysis?
> - Generate IaC templates to remediate a specific finding?
> - Create a migration plan for a specific architectural change?
> - Compare your workload against a specific WA Lens in detail?
> - Generate automated checks (Config rules, custom metrics) for ongoing compliance?
> - Set up a continuous WA gate: commit `aws-well-architected-framework-review.json` as a baseline and run `tools/wa-ci` in CI?
> - Produce a WA Tool import for tracking in the AWS console?
> - File the 🔴/🟡 findings as tracking issues with a summary epic? (Step 7b — offer only when an issue tracker CLI is available)

## Step 7b: File findings as tracking issues (optional — confirmation-gated)

An optional output mode that turns report findings into tracked work so the report does not go stale. **Never run it automatically** — it is gated behind one explicit user confirmation per review, and the default is no (design principle: keep the user in control).

**Tracker detection.** Before offering, check that an issue tracker is actually reachable: `gh` CLI first (`gh auth status` succeeds and the workload repo has a GitHub remote); another tracker only if the runtime exposes an equivalent tool. If none is available, skip silently — do not offer — and add one line to the report footer: `Tracking-issue filing skipped — no issue tracker CLI available.`

**Ask once** (only when a tracker is available), as part of the Step 7 offer:

> Shall I file these findings as tracking issues? I would create one issue per 🔴 Critical/High and 🟡 Medium finding, plus one summary epic with a prioritized checklist. Low and Cannot Determine items stay in the report only. (default: no)

**If — and only if — the user confirms**, create:

1. **One issue per 🔴 Critical/High and 🟡 Medium finding**
   - Title: `[WA][<PILLAR>] <finding title>` (e.g., `[WA][SEC] Uploads bucket lacks Block Public Access`)
   - Body: severity, BP ID in canonical `SEC01-BP02` format (or the lens + finding title when the lens exposes no BP ID), the evidence citation (file:line), and the remediation next step from the report — including its **Fix:** block when present.
2. **One summary epic**
   - Title: `[WA] Well-Architected review — {workload name} ({date})`
   - Body: the pillar scorecard table plus a checklist linking every finding issue (`- [ ] #<n> …`), grouped by Eisenhower quadrant (Do First → Plan → Delegate → Defer).

**Rules:**
- Issues are review artifacts, not code changes — bodies carry guidance and fix snippets to copy, never applied diffs.
- Do not add labels, assignees, or milestones unless the user asks — leave triage to the team.
- Do not file Low or Cannot Determine rows (tracker noise); they remain in the report.
- When done, list the created issue URLs and note the epic as the tracking entry point.

## Calibration Guidance

- A workload with multi-AZ, encryption, CI/CD with rollback, monitoring, and auto-scaling is MATURE — most findings should be improvements, not Critical
- Do NOT manufacture Critical findings for a well-built workload — accuracy over alarm
- When business criticality is "low"/"standard", accept simpler architectures (single-region is fine for internal tools)
- When business criticality is "critical", apply stricter standards (multi-region DR, chaos testing, sub-minute RTO expected)
- Every determinate finding MUST have concrete code, configuration, runtime, or explicit user-provided evidence — no generic recommendations without backing
- If something cannot be determined from the available evidence, say "Cannot Determine", leave severity blank, and explain what runtime/interview data is needed
- Acknowledge strengths prominently — a mature workload should feel validated, not just criticized

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
