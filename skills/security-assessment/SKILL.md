---
name: security-assessment
description: Deep-dive security posture assessment against the Well-Architected Security pillar, covering identity, detection, infrastructure protection, data protection, and incident response.
version: 1.1.0
---

# Security Assessment

## Step 1: Gather context

Ask the user:

> What workload or AWS environment would you like me to assess for security? Please share:
> - **Architecture overview** (services, accounts, network topology)
> - **Compliance requirements** (SOC2, HIPAA, PCI-DSS, FedRAMP, GDPR, etc.)
> - **Current security tooling** (GuardDuty, Security Hub, WAF, etc.)
> - **Known concerns** (optional)

If context is already provided, proceed directly.

## Step 2: Assess Identity and Access Management

Evaluate:
- Is there a centralized identity provider? (IAM Identity Center, federation)
- Are IAM policies following least privilege? (wildcards, overly broad permissions)
- Are service roles scoped per function?
- Is MFA enforced for human access?
- Are long-lived credentials eliminated? (access keys vs roles)
- Is cross-account access managed via Organizations and SCPs?

## Step 3: Assess Detection and Monitoring

Evaluate:
- Is CloudTrail enabled in all regions with log file validation?
- Is GuardDuty active with findings routed to a response workflow?
- Is Security Hub aggregating findings across accounts?
- Are VPC Flow Logs, DNS logs, and S3 access logs enabled?
- Are security-relevant CloudWatch alarms configured? (root login, unauthorized API calls)
- Is there automated alerting for configuration drift? (Config Rules)

## Step 4: Assess Infrastructure Protection

Evaluate:
- Are VPCs segmented with private subnets for workloads?
- Are security groups and NACLs following deny-by-default?
- Is traffic inspected? (Network Firewall, WAF, Shield)
- Are public endpoints minimized and protected?
- Are compute resources hardened? (patching, SSM, no SSH)
- Is there protection against DDoS? (Shield Advanced, CloudFront)
- **Protocol-level risks** (always flag explicitly):
  - TLS 1.0 or 1.1 still supported → **Critical** severity (deprecated, exploitable)
  - Weak cipher suites (RC4, DES, 3DES, MD5-based MACs) → **High** severity
  - Self-signed or expired certificates in production → **High** severity
  - HTTP endpoints without redirect-to-HTTPS → **High** severity

## Step 5: Assess Data Protection

Evaluate:
- Is encryption at rest enabled for all data stores? (KMS, default keys vs CMKs)
- Is encryption in transit enforced? (TLS 1.2+, certificate management)
- Is sensitive data classified and tagged?
- Are backup and recovery mechanisms in place?
- Is data access audited?
- Are secrets managed properly? (Secrets Manager or Parameter Store SecureString — not environment variables, not hardcoded credentials, not config files)

## Step 6: Assess Incident Response

Evaluate:
- Is there a documented incident response plan?
- Are forensic capabilities available? (isolated accounts, snapshot automation)
- Are there automated containment actions? (Lambda remediation, Step Functions)
- Is there a process for post-incident review?
- Are game days or tabletop exercises conducted?

## Step 7: Produce findings

**Calibration guidance:**
- If the environment demonstrates strong controls (MFA, SCPs, encryption, Security Hub, incident response plan), acknowledge this explicitly in the summary
- A "Strong" or "Satisfactory" overall posture is a valid assessment — not every review must produce Critical findings
- For compliance-focused assessments, map controls directly to the relevant framework criteria (SOC2 CC, PCI-DSS requirements, HIPAA safeguards)
- Do not invent findings that aren't supported by the provided architecture details
- Focus on gaps and hardening opportunities rather than re-flagging controls already in place

Output:

```markdown
# Security Assessment: {Workload Name}

## Summary
- **Compliance scope**: {frameworks}
- **Findings**: {X} Critical, {Y} High, {Z} Medium

## Critical Findings
{Each: what's wrong, why it matters, how to fix it, AWS service/feature to use}

## High Findings
{Same format}

## Medium Findings
{Same format}

## Security Scorecard
| Domain | Score | Key Gap |
|--------|-------|---------|
| Identity & Access | {1-5} | {gap} |
| Detection | {1-5} | {gap} |
| Infrastructure Protection | {1-5} | {gap} |
| Data Protection | {1-5} | {gap} |
| Incident Response | {1-5} | {gap} |

## Remediation Roadmap

### Quick Wins (< 1 week)
{Low-effort, high-impact security improvements}

### Foundation (1-4 weeks)
{Core security controls and detection capabilities}

### Advanced (1-3 months)
{Automated response, advanced detection, compliance hardening}
```

## Step 8: Offer follow-up

After delivering the assessment, offer:

> Would you like me to:
> - Design IAM policies following least privilege for a specific role?
> - Create an incident response playbook for a specific threat?
> - Generate IaC for security controls (GuardDuty, Security Hub, Config rules)?
> - Map findings to a specific compliance framework (SOC2, HIPAA, PCI)?
> - Design a network segmentation architecture?
