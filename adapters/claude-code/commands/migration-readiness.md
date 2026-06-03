Assess a workload's readiness to migrate to AWS by analyzing existing code, dependencies, configurations, and infrastructure to produce evidence-backed findings covering the 7 Rs, risks, and a migration plan.

## Step 1: Gather context

Ask the user:

> What workload are you planning to migrate? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Current environment** (on-premises, other cloud, colocation)
> - **Business drivers** (cost, agility, compliance, end-of-life hardware)
> - **Timeline constraints** (optional)

If already in a codebase, proceed directly.

## Step 2: Application Stack Discovery

Analyze the codebase to understand current stack:

- Programming languages and runtime versions
- Frameworks and libraries (web, ORM, messaging)
- Database technologies
- External service dependencies
- Configuration management (config files, env vars, secrets)
- Build and packaging systems (Maven, npm, pip, Docker)
- OS-specific or hardware dependencies

For each component, document:
- File path and line numbers
- Technology and version
- AWS equivalent or migration path
- Migration complexity (simple lift, requires changes, requires rewrite)

Flag as BLOCKER:
- OS-specific deps without cloud equivalents
- Proprietary licensing restrictions (Oracle, specific Windows features)
- Hardware-specific dependencies (FPGA, USB dongles)
- Hardcoded IP addresses/hostnames in application code
- Local filesystem dependencies (shared network drives)

## Step 3: Dependency Mapping

Map all internal and external dependencies:

- Service-to-service communication (protocols, ports)
- Database connections (shared databases, multiple consumers)
- External API integrations
- Network dependencies (latency-sensitive connections)
- Authentication dependencies (LDAP, AD, SSO)

Create a dependency diagram showing services, connections, and migration wave groupings.

Flag as HIGH RISK:
- Tight coupling that must move together
- Shared databases with multiple consumers
- Latency-sensitive integrations spanning hybrid during migration
- Hard dependencies on systems that cannot move

## Step 4: Determine migration strategy (7 Rs)

For each component, recommend based on code evidence:

| Strategy | Code Indicators |
|----------|-----------------|
| **Rehost** | Standard OS, containerizable, no OS-specific deps |
| **Replatform** | Self-managed DB → RDS, self-managed cache → ElastiCache |
| **Refactor** | Monolith to decompose, stateful → stateless |
| **Repurchase** | Commercial software with AWS/SaaS equivalent |
| **Retire** | Unused code, deprecated services |
| **Retain** | Hard dependencies, compliance blockers |
| **Relocate** | VMware-specific configurations |

Every recommendation MUST be justified with code evidence.

## Step 5: Assess readiness by pillar

For each pillar: **Readiness** (Ready/Conditionally Ready/Not Ready), **Evidence** (file:line), **Gaps**, **Actions needed**.

- **Operational Excellence**: IaC existence, CI/CD portability, monitoring portability
- **Security**: compliance constraints, secrets management, network security equivalents, identity compatibility
- **Reliability**: current availability, HA mechanisms to replicate, acceptable migration downtime
- **Performance Efficiency**: latency-sensitive integrations, hardware deps, performance baselines
- **Cost Optimization**: current TCO, licensing implications, existing commitments
- **Sustainability**: resource footprint reduction, Graviton/serverless opportunities

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

## Step 7: Produce the assessment

Structure:

- Executive Summary (date, packages analyzed, recommended strategy, overall readiness, effort estimate, key risks, critical blockers count)
- Application Stack Summary table (component, technology, version, AWS equivalent, strategy, complexity)
- Dependency Map (PlantUML diagram)
- Readiness Scorecard (pillar, readiness status, score 1-5, key blocker, action needed)
- Critical Blockers (ID, description, evidence file:line, impact, resolution approach, effort)
- Risks and Mitigations table (risk, evidence, risk level, impact, mitigation, AWS service)
- Pre-Migration Checklist (ordered by priority)
- Migration Plan (Phase 1: Mobilize, Phase 2: Migrate with waves, Phase 3: Optimize)
- AWS Services for Migration table
- Cost Comparison (category, current est., AWS est., delta)
- Next Steps (top 5 actions)

## Calibration

- Every blocker and risk MUST have code evidence
- Strategy recommendations must be justified by code analysis
- "Cannot Determine" is valid for runtime characteristics not in code (data volumes, latency)
- For shared databases, always flag migration ordering constraint
- Cost estimates from static analysis are rough — acknowledge uncertainty
- Acknowledge migration-ready aspects prominently (containerized, stateless, IaC exists)
