---
name: migration-readiness
description: Assess a workload's readiness to migrate to AWS by analyzing existing code, dependencies, configurations, and infrastructure to produce evidence-backed findings covering the 7 Rs, risks, and a migration plan.
version: 2.0.0
---

# Migration Readiness Assessment

## Step 1: Gather context

Ask the user:

> What workload are you planning to migrate? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Current environment** (on-premises, other cloud, colocation)
> - **Business drivers** (cost, agility, compliance, end-of-life hardware, etc.)
> - **Timeline constraints** (optional)

If context is already provided or you are in a codebase, proceed directly.

## Step 2: Application Stack Discovery

Analyze the codebase to understand the current application stack.

You MUST examine:
- Programming languages and runtimes (versions, compatibility with AWS services)
- Frameworks and libraries (web frameworks, ORM, messaging)
- Database technologies (relational, NoSQL, search, caching)
- Middleware and message brokers
- External service dependencies (APIs, SaaS integrations)
- Configuration management (config files, environment variables, secrets)
- Operating system dependencies and system-level requirements
- Build and packaging systems (Maven, npm, pip, Docker)

For each component, document:
- File path and line numbers
- Technology and version
- AWS equivalent or migration path
- Migration complexity (simple lift, requires changes, requires rewrite)
- Dependencies on other components

You MUST flag as BLOCKER:
- OS-specific dependencies without cloud equivalents
- Proprietary software with licensing restrictions (Oracle, specific Windows features)
- Hardware-specific dependencies (FPGA, specific CPU instructions, USB dongles)
- Hardcoded IP addresses or hostnames in application code
- Local filesystem dependencies (shared network drives, local storage)

## Step 3: Infrastructure Discovery

Analyze existing infrastructure configurations.

You MUST examine:
- Server configurations (CPU, memory, storage requirements)
- Network topology (VLANs, firewalls, load balancers, DNS)
- Storage systems (SAN, NAS, local disk, file shares)
- Database configurations (engine, version, size, replication)
- Monitoring and alerting systems
- Backup and DR configurations
- Security controls (firewalls, IDS/IPS, WAF, certificates)
- Existing IaC if any (Terraform, Ansible, Chef, Puppet)

For each infrastructure component, document:
- Current configuration
- AWS equivalent service
- Migration approach (rehost, replatform, refactor)
- Data volume and transfer considerations

## Step 4: Dependency Mapping

Map all internal and external dependencies.

You MUST examine:
- Service-to-service communication (protocols, ports, patterns)
- Database connections (connection strings, pooling, multiple consumers)
- Shared databases or data stores (multiple services writing/reading)
- External API integrations (third-party services, partner APIs)
- Network dependencies (latency-sensitive connections, VPN tunnels)
- Batch job dependencies (scheduling, order of execution)
- Authentication/authorization dependencies (LDAP, AD, SSO)

You MUST create a dependency diagram showing:
- All services and their connections
- Data flows and protocols
- External dependencies
- Migration wave groupings (what must move together)

You MUST flag as HIGH RISK:
- Tight coupling between components that must move together (increases blast radius)
- Shared databases accessed by multiple services (migration ordering constraint)
- Latency-sensitive integrations that will span hybrid during migration
- Hard dependencies on on-premises systems that cannot move (require hybrid connectivity)

## Step 5: Determine migration strategy (7 Rs)

For each component, evaluate which strategy fits based on code evidence:

| Strategy | When to use | Code Indicators |
|----------|-------------|-----------------|
| **Rehost** | Fast migration, minimal changes | Standard OS, containerizable, no OS-specific deps |
| **Replatform** | Small optimizations during move | Self-managed DB → RDS, self-managed cache → ElastiCache |
| **Refactor** | Need cloud-native benefits | Monolith that should be decomposed, stateful → stateless |
| **Repurchase** | Replace with SaaS | Commercial software with AWS/SaaS equivalent |
| **Retire** | No longer needed | Unused code, deprecated services |
| **Retain** | Not ready to move | Hard dependencies, compliance blockers |
| **Relocate** | VMware workloads | VMware-specific configurations |

You MUST justify each recommendation with code evidence.

## Step 6: Assess readiness by pillar

For each pillar, provide: **Readiness** (Ready/Conditionally Ready/Not Ready), **Evidence** (file:line), **Gaps**, **Actions needed**.

### Operational Excellence Readiness
- Is there IaC? (CloudFormation, Terraform, CDK, Ansible)
- Are CI/CD pipelines in place? Can they target AWS?
- Is monitoring portable or tied to specific tools?
- Are operational procedures documented?

### Security Readiness
- Are there compliance requirements affecting region/service choice?
- How are secrets managed? (hardcoded, vault, config files)
- Are there network security dependencies needing equivalents?
- Is identity management compatible with AWS IAM/Identity Center?

### Reliability Readiness
- What is the current availability? What's the target?
- Are there HA mechanisms to replicate?
- What's the acceptable downtime during migration?
- Are backup/recovery procedures tested?

### Performance Efficiency Readiness
- Are there latency-sensitive integrations?
- Are there hardware-specific dependencies?
- What are current performance baselines?
- Are there SLAs to maintain during cutover?

### Cost Optimization Readiness
- What's the current TCO? (hardware, licensing, ops, facilities)
- Are there licensing implications? (BYOL, license-included, re-purchase)
- Are there existing contracts or prepaid commitments?

### Sustainability Readiness
- Can migration reduce resource footprint?
- Are there opportunities for Graviton/serverless?
- Can managed services replace self-managed infrastructure?

## Step 7: Risk Assessment

For each risk, assess using Impact × Likelihood:

**Impact**: Minor (schedule slip, minor rework) | Moderate (significant rework, extended hybrid period) | Severe (migration failure, data loss, extended outage)

**Likelihood**: Low (unlikely with proper planning) | Medium (possible without specific mitigation) | High (likely given current state)

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

## Step 8: Produce the assessment

```markdown
# Migration Readiness Assessment: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Packages Analyzed**: {list}
- **Recommended Strategy**: {primary strategy}
- **Overall Readiness**: {Ready / Conditionally Ready / Not Ready}
- **Estimated Effort**: {T-shirt size with justification}
- **Key Risks**: {top 3}
- **Critical Blockers**: {count and brief description}

## Application Stack Summary
| Component | Technology | Version | AWS Equivalent | Strategy | Complexity |
|-----------|-----------|---------|---------------|----------|------------|
| {name} | {tech} | {ver} | {aws service} | {7R} | {Low/Med/High} |

## Dependency Map
{PlantUML diagram showing service dependencies, data flows, and migration wave groupings}

## Readiness Scorecard
| Pillar | Readiness | Score (1-5) | Key Blocker | Action Needed |
|--------|-----------|-------------|-------------|---------------|
| Operational Excellence | {status} | {score} | {blocker} | {action} |
| Security | {status} | {score} | {blocker} | {action} |
| Reliability | {status} | {score} | {blocker} | {action} |
| Performance Efficiency | {status} | {score} | {blocker} | {action} |
| Cost Optimization | {status} | {score} | {blocker} | {action} |
| Sustainability | {status} | {score} | {blocker} | {action} |

## Critical Blockers
{For each: ID, description, evidence (file:line), impact on migration, resolution approach, effort}

## Risks and Mitigations
| Risk | Evidence | Risk Level | Migration Impact | Mitigation | AWS Service |
|------|----------|------------|-----------------|------------|-------------|
| {risk} | {file:line} | {level} | {impact} | {mitigation} | {service} |

## Pre-Migration Checklist
{Ordered by priority — what must be done before migration starts}
- [ ] {action with evidence of why it's needed}

## Migration Plan

### Phase 1: Mobilize (Weeks 1-2)
| Task | Dependencies | AWS Service | Evidence |
|------|-------------|-------------|----------|
{Landing zone, connectivity, tooling setup}

### Phase 2: Migrate (Weeks 3-6)
| Wave | Components | Strategy | Data Volume | Downtime Window |
|------|-----------|----------|-------------|-----------------|
{Component migration waves based on dependency analysis}

### Phase 3: Optimize (Weeks 7-8)
| Optimization | Component | Expected Benefit | AWS Service |
|-------------|-----------|-----------------|-------------|
{Right-sizing, managed services, serverless, Graviton}

## AWS Services for Migration
| Category | Service | Purpose | Relevant Components |
|----------|---------|---------|-------------------|
| Server | AWS MGN | Rehost EC2 | {components} |
| Database | AWS DMS | Replicate with minimal downtime | {components} |
| Data | DataSync / Snowball | Large-scale transfer | {components} |
| Schema | AWS SCT | Schema conversion | {components} |
| Network | Direct Connect / VPN | Hybrid connectivity | {components} |
| Governance | Control Tower | Multi-account | All |

## Cost Comparison
| Category | Current (monthly est.) | AWS Estimated | Delta | Notes |
|----------|----------------------|---------------|-------|-------|
| Compute | {estimate} | {estimate} | {delta} | {basis} |
| Storage | {estimate} | {estimate} | {delta} | {basis} |
| Networking | {estimate} | {estimate} | {delta} | {basis} |
| Licensing | {estimate} | {estimate} | {delta} | {basis} |
| Operations | {estimate} | {estimate} | {delta} | {basis} |

## Next Steps
{Top 5 concrete actions the team should take this week to prepare}
```

## Step 9: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Design the AWS landing zone architecture?
> - Create a detailed data migration plan for a specific database?
> - Estimate AWS costs in detail for specific components?
> - Build a pre-migration testing strategy?
> - Design the hybrid connectivity architecture?
> - Create IaC for the target AWS architecture?

## Calibration Guidance

- A workload already containerized with CI/CD and IaC is LARGELY READY — focus on AWS-specific optimizations and data migration planning
- Every blocker and risk MUST have code evidence — don't flag "licensing risk" without checking actual dependencies
- Migration strategy recommendations must be justified by code analysis (not assumptions)
- "Cannot Determine" is valid for runtime characteristics not visible in code (e.g., actual data volumes, network latency requirements)
- For shared databases, always flag the migration ordering constraint — this is the #1 cause of migration complexity
- Cost estimates from static analysis are rough — acknowledge uncertainty and recommend AWS Pricing Calculator for precision
- Acknowledge migration-ready aspects prominently (containerized, stateless, IaC already exists)
