---
name: security-assessment
description: Deep-dive security posture assessment by analyzing IAM policies, encryption configs, network rules, and security controls in code to produce evidence-backed findings aligned with the Well-Architected Security pillar.
version: 2.0.0
---

# Security Assessment

## Step 1: Gather context

Ask the user:

> What workload or AWS environment would you like me to assess for security? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Compliance requirements** (SOC2, HIPAA, PCI-DSS, FedRAMP, GDPR, etc.)
> - **Known concerns** (optional)

If context is already provided or you are in a codebase with IaC, proceed directly.

## Step 2: Identity and Access Management Discovery

Analyze all IAM configurations in the codebase.

You MUST examine:
- IAM role definitions (trust policies and permission policies)
- IAM policy documents (managed and inline)
- Service-linked roles and permission boundaries
- Resource-based policies (S3 bucket policies, KMS key policies, SQS policies)
- Cognito/Identity Center configurations
- API Gateway authorizers
- Lambda execution roles

For each IAM resource, document:
- File path and line numbers
- Actions allowed (flag wildcards)
- Resources scoped (flag wildcards)
- Trust relationships (who can assume)
- Whether least privilege is followed

You MUST flag as HIGH RISK:
- Any `"Action": "*"` or `"Action": "service:*"` on mutating actions
- Any `"Resource": "*"` on policies that allow write/delete operations
- Cross-account trust with overly broad conditions
- Missing `Condition` blocks on sensitive operations
- IAM policies attached to `*` principals
- Long-lived credentials (access keys in code or config)

## Step 3: Encryption and Data Protection Discovery

Analyze encryption configurations across all resources.

You MUST examine:
- KMS key definitions and key policies
- Encryption-at-rest settings on all storage (S3, EBS, RDS, DynamoDB, EFS, Secrets Manager)
- Encryption-in-transit settings (TLS configs, listener rules, security policies)
- Certificate management (ACM, self-signed)
- Secrets management (Secrets Manager, Parameter Store SecureString, environment variables)
- Data classification tags

You MUST flag as HIGH RISK:
- Any storage resource without encryption at rest enabled
- TLS versions below 1.2 on any listener or endpoint
- Security policies allowing weak cipher suites (RC4, DES, 3DES, MD5-based MACs)
- Self-signed or expired certificates in production configurations
- Secrets in environment variables, hardcoded strings, or config files (instead of Secrets Manager/Parameter Store)
- KMS keys without rotation enabled
- S3 buckets without default encryption

## Step 4: Network Protection Discovery

Analyze all network security configurations.

You MUST examine:
- VPC definitions (subnets, route tables, internet gateways)
- Security group rules (ingress and egress)
- Network ACLs
- WAF rules and web ACLs
- VPC endpoints (interface and gateway)
- NAT Gateways and their placement
- Load balancer security (listeners, target groups, security policies)
- API Gateway endpoint types and throttling

You MUST flag as HIGH RISK:
- Security group ingress `0.0.0.0/0` on ports other than 443/80
- Security group ingress `0.0.0.0/0` on SSH (22) or RDP (3389)
- Public subnets hosting databases or internal services
- Missing VPC endpoints for S3/DynamoDB (traffic going through NAT/internet)
- No WAF on internet-facing endpoints
- Overly permissive egress rules (all traffic to all destinations)

## Step 5: Detection and Response Discovery

Analyze security monitoring and incident response configurations.

You MUST examine:
- CloudTrail configurations
- GuardDuty enablement
- Security Hub configurations
- Config Rules
- VPC Flow Log settings
- CloudWatch alarms for security events (root login, unauthorized API calls)
- Automated response configurations (Lambda remediation, Step Functions)
- S3 access logging

## Step 6: Compute Protection Discovery

Analyze compute security configurations.

You MUST examine:
- Lambda function configurations (runtime, layers, VPC attachment, reserved concurrency)
- ECS/EKS task definitions (privileged mode, user, capabilities, secrets injection)
- EC2 launch templates (IMDSv2, user data, security groups)
- Container image sources and scanning configurations
- SSM Session Manager configurations (vs SSH access)

You MUST flag as HIGH RISK:
- Containers running in privileged mode without justification
- EC2 instances with IMDSv1 enabled (hop limit > 1 without IMDSv2 required)
- Lambda functions with overly broad VPC access
- No container image scanning configured
- SSH access enabled where SSM Session Manager would suffice

## Step 7: Evaluate against WA Framework questions

For each question, provide: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

### SEC 1 — How do you securely operate your workload?
- Look for: security baselines, account separation, threat detection, automated response
- Evidence: Config rules, GuardDuty configs, security automation

### SEC 2 — How do you manage identities for people and machines?
- Look for: centralized identity, role separation, credential lifecycle, MFA configurations
- Evidence: Identity Center configs, IAM role trust policies, Cognito settings

### SEC 3 — How do you manage permissions for people and machines?
- Look for: least privilege, permission boundaries, access analysis, regular review process
- Evidence: IAM policies, permission boundary ARNs, Access Analyzer configs

### SEC 4 — How do you detect and investigate security events?
- Look for: CloudTrail, GuardDuty, Security Hub, VPC Flow Logs, DNS logging
- Evidence: trail configs, detector settings, log group definitions, alarm rules

### SEC 5 — How do you protect your network resources?
- Look for: VPC segmentation, security groups, WAF, private subnets, VPC endpoints
- Evidence: VPC constructs, SG rules, WAF ACLs, endpoint definitions

### SEC 6 — How do you protect your compute resources?
- Look for: patching, container scanning, runtime protection, minimal privileges
- Evidence: launch templates, task definitions, Lambda configs, scanning configs

### SEC 7 — How do you classify your data?
- Look for: data classification tags, sensitivity labels, data catalog configs
- Evidence: resource tags, Macie configs, Glue catalog settings

### SEC 8 — How do you protect your data at rest?
- Look for: encryption on ALL stores, KMS policies, key rotation
- Evidence: encryption properties on every storage resource in IaC

### SEC 9 — How do you protect your data in transit?
- Look for: TLS 1.2+ enforcement, certificate management, HTTPS-only
- Evidence: listener configs, security policies, redirect rules

### SEC 10 — How do you anticipate, respond to, and recover from incidents?
- Look for: response automation, forensic capabilities, containment procedures
- Evidence: remediation Lambdas, isolation procedures, backup configs

## Step 8: Risk Assessment

For each finding, assess using Impact × Likelihood:

**Impact**: Minor (limited data exposure, no compliance violation) | Moderate (partial data exposure, minor compliance gap) | Severe (full data breach, regulatory violation, privilege escalation)

**Likelihood**: Low (requires chained exploits, strong compensating controls) | Medium (exploitable with moderate effort, partial controls) | High (easily exploitable, no compensating controls)

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

## Step 9: Produce findings

```markdown
# Security Assessment: {Workload Name}

## Executive Summary
- **Date**: {date}
- **Compliance Scope**: {frameworks}
- **Packages Analyzed**: {list}
- **Findings**: {X} Critical, {Y} High, {Z} Medium, {W} Low
- **Overall Security Posture**: {1-5} — {one-line justification}

## Security Scorecard
| Domain | Score (1-5) | Key Strength | Key Gap |
|--------|-------------|--------------|---------|
| Identity & Access | {score} | {strength} | {gap} |
| Data Protection (at rest) | {score} | {strength} | {gap} |
| Data Protection (in transit) | {score} | {strength} | {gap} |
| Network Protection | {score} | {strength} | {gap} |
| Compute Protection | {score} | {strength} | {gap} |
| Detection & Response | {score} | {strength} | {gap} |

## Critical and High Risk Findings
{For each: ID, domain, title, description, evidence (file:line), impact assessment, recommendation, effort, AWS services}

## Medium Risk Findings
{Same format, condensed}

## Low Risk Findings
{Summary table: ID | Domain | Title | Recommendation}

## Compliance Mapping
{If compliance requirements specified, map findings to relevant framework controls}
| Finding ID | SOC2 CC | HIPAA | PCI-DSS | Notes |
|------------|---------|-------|---------|-------|

## Prioritized Remediation Plan

### Quick Wins (< 1 week)
| Finding | Action | Impact | Effort |
|---------|--------|--------|--------|
{Enable encryption, tighten SG rules, rotate keys, fix TLS versions}

### Foundation (1-4 weeks)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Implement least privilege, add WAF, enable GuardDuty, add VPC endpoints}

### Strategic (1-3 months)
| Finding | Action | Impact | Effort | Dependencies |
|---------|--------|--------|--------|--------------|
{Zero-trust network, automated response, forensic capabilities, compliance program}

## Next Steps
{Top 5 concrete security actions the team should take this week}
```

## Step 10: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Design least-privilege IAM policies for specific roles?
> - Generate IaC for security controls (GuardDuty, Security Hub, Config rules)?
> - Create an incident response playbook for a specific threat?
> - Map findings to a specific compliance framework in detail?
> - Design network segmentation architecture?
> - Tighten specific security group rules with minimal disruption?

## Calibration Guidance

- A workload with encryption everywhere, least-privilege IAM, VPC segmentation, GuardDuty, and Security Hub is MATURE — focus on hardening, detection depth, and response automation
- Every finding MUST have code evidence — no "you should enable encryption" without first checking if it's already enabled
- Flag protocol-level risks explicitly: TLS < 1.2 is always Critical, weak ciphers always High
- If compliance is specified, map EVERY Critical/High finding to the relevant compliance control
- "Cannot Determine" is valid when static analysis is insufficient (e.g., actual IAM usage patterns require Access Analyzer data)
- Acknowledge strong security practices prominently before listing gaps
