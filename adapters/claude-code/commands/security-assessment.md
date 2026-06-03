Perform a deep-dive security posture assessment by analyzing IAM policies, encryption configs, network rules, and security controls in the codebase to produce evidence-backed findings aligned with the Well-Architected Security pillar.

## Step 1: Gather context

Ask the user:

> What workload would you like me to assess for security? Please share:
> - **Workload name** and code packages/directories to analyze
> - **Compliance requirements** (SOC2, HIPAA, PCI-DSS, FedRAMP, GDPR, etc.)
> - **Known concerns** (optional)

If already in a codebase with IaC, proceed directly.

## Step 2: Identity and Access Management Discovery

Analyze ALL IAM configurations:

- IAM roles (trust policies, permission policies)
- IAM policy documents (managed and inline)
- Resource-based policies (S3, KMS, SQS)
- API Gateway authorizers, Cognito configs
- Lambda execution roles

Flag as HIGH RISK:
- `"Action": "*"` or `"Action": "service:*"` on mutating actions
- `"Resource": "*"` on write/delete policies
- Overly broad cross-account trust
- Long-lived credentials in code or config

## Step 3: Encryption and Data Protection Discovery

Analyze encryption across ALL resources:

- KMS keys and policies
- Encryption at rest (S3, EBS, RDS, DynamoDB, EFS)
- Encryption in transit (TLS configs, listeners, security policies)
- Secrets management (Secrets Manager vs env vars vs hardcoded)

Flag as HIGH RISK:
- Storage without encryption at rest
- TLS < 1.2
- Weak cipher suites
- Secrets in env vars, hardcoded strings, or config files
- KMS keys without rotation

## Step 4: Network Protection Discovery

Analyze network security:

- Security group rules (ingress/egress)
- VPC design (public vs private subnets)
- WAF rules and web ACLs
- VPC endpoints

Flag as HIGH RISK:
- SG ingress `0.0.0.0/0` on non-443/80 ports
- SSH/RDP open to internet
- Databases in public subnets
- No WAF on internet-facing endpoints

## Step 5: Detection and Compute Protection

Analyze:

- CloudTrail, GuardDuty, Security Hub, Config Rules configs
- VPC Flow Logs, S3 access logs
- Container configs (privileged mode, IMDSv2, image scanning)
- Lambda configs (VPC, execution role scope)

Flag: containers in privileged mode, IMDSv1 enabled, no image scanning.

## Step 6: Evaluate against WA Framework questions

Every assessment MUST include: **Status**, **Evidence** (file:line), **Gaps**, **Risk**.

- **SEC 1 — Secure operations**: security baselines, automated response
- **SEC 2 — Identities**: centralized identity, role separation
- **SEC 3 — Permissions**: least privilege, permission boundaries
- **SEC 4 — Detection**: CloudTrail, GuardDuty, Security Hub, logging
- **SEC 5 — Network**: VPC segmentation, WAF, endpoints
- **SEC 6 — Compute**: patching, scanning, minimal privileges
- **SEC 8 — Data at rest**: encryption on ALL stores
- **SEC 9 — Data in transit**: TLS 1.2+, certificates
- **SEC 10 — Incident response**: automation, forensic capabilities

## Step 7: Risk Assessment

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

## Step 8: Produce the report

Structure:

- Executive Summary (date, compliance scope, packages analyzed, findings count, security posture 1-5)
- Security Scorecard (Identity & Access, Data Protection at-rest/in-transit, Network, Compute, Detection & Response — each scored 1-5)
- Critical and High Risk Findings (ID, domain, title, evidence file:line, impact, recommendation, effort, AWS services)
- Medium/Low Risk Findings
- Compliance Mapping (if requirements specified, map to framework controls)
- Prioritized Remediation Plan (Quick Wins < 1 week, Foundation 1-4 weeks, Strategic 1-3 months)
- Next Steps (top 5 actions)

## Calibration

- Every finding MUST have code evidence
- TLS < 1.2 is always Critical. Weak ciphers always High.
- "Cannot Determine" is valid when static analysis is insufficient
- Acknowledge strong security practices before listing gaps
