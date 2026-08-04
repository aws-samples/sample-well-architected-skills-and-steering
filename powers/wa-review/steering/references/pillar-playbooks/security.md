# Security Pillar — Deep-Dive Discovery Playbook

When wa-review is scoped to the Security pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

## Identity and Access Management

Examine:
- IAM role definitions (trust policies and permission policies)
- IAM policy documents (managed and inline)
- Permission boundaries and service-linked roles
- Resource-based policies (S3 bucket, KMS key, SQS policies)
- Cognito/Identity Center configurations
- API Gateway authorizers
- Lambda execution roles

Flag HIGH RISK:
- `"Action": "*"` or `"Action": "service:*"` on mutating actions
- `"Resource": "*"` on write/delete policies
- Cross-account trust with overly broad conditions
- Missing `Condition` blocks on sensitive operations
- IAM policies attached to `*` principals
- Long-lived credentials (access keys in code or config)

## Encryption and Data Protection

Examine:
- KMS key definitions and key policies
- Encryption-at-rest on all storage (S3, EBS, RDS, DynamoDB, EFS, Secrets Manager)
- Encryption-in-transit settings (TLS configs, listener rules, security policies)
- Certificate management (ACM, self-signed)
- Secrets management (Secrets Manager, Parameter Store SecureString, environment variables)

Flag HIGH RISK:
- Storage resources without encryption at rest
- TLS versions below 1.2
- Security policies allowing weak cipher suites (RC4, DES, 3DES)
- Self-signed or expired certificates in production
- Secrets in environment variables or hardcoded strings
- KMS keys without rotation enabled
- S3 buckets without default encryption

## Network Protection

Examine:
- VPC definitions (subnets, route tables, internet gateways)
- Security group rules (ingress and egress)
- Network ACLs
- WAF rules and web ACLs
- VPC endpoints (interface and gateway)
- NAT Gateway placement
- Load balancer security (listeners, security policies)
- API Gateway endpoint types and throttling

Flag HIGH RISK:
- Security group ingress `0.0.0.0/0` on ports other than 443/80
- SSH (22) or RDP (3389) open to `0.0.0.0/0`
- Public subnets hosting databases or internal services
- Missing VPC endpoints for S3/DynamoDB
- No WAF on internet-facing endpoints
- Overly permissive egress rules

## Detection and Response

Examine:
- CloudTrail configurations
- GuardDuty enablement
- Security Hub configurations
- Config Rules
- VPC Flow Log settings
- CloudWatch alarms for security events (root login, unauthorized API calls)
- Automated response (Lambda remediation, Step Functions)
- S3 access logging

## Compute Protection

Examine:
- Lambda function configurations (runtime, layers, VPC attachment)
- ECS/EKS task definitions (privileged mode, user, capabilities, secrets)
- EC2 launch templates (IMDSv2, user data, security groups)
- Container image sources and scanning
- SSM Session Manager vs SSH access

Flag HIGH RISK:
- Containers running in privileged mode without justification
- EC2 instances with IMDSv1 enabled
- No container image scanning
- SSH access where SSM Session Manager would suffice

## Security-Specific Report Format

When producing a pillar-scoped security report, include:
- **Security Scorecard** with 6 domains: Identity & Access, Data Protection (at rest), Data Protection (in transit), Network Protection, Compute Protection, Detection & Response
- **Compliance Mapping** table if compliance requirements specified (map findings to SOC2/HIPAA/PCI-DSS controls)
- **Quick Wins / Foundation / Strategic** remediation tiers

## Calibration

- Flag protocol-level risks explicitly: TLS < 1.2 is always Critical, weak ciphers always High
- "Cannot Determine" is valid for operational aspects (e.g., actual IAM usage requires Access Analyzer data)
