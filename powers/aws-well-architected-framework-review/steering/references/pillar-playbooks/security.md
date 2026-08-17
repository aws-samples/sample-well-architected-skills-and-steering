# Security Pillar — Deep-Dive Discovery Playbook

When aws-well-architected-framework-review is scoped to the Security pillar, apply these specialized discovery steps in addition to general infrastructure discovery.

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

## Named Anti-Patterns

High-frequency Well-Architected failures codified as named patterns. Check every detection heuristic explicitly during discovery. When one matches, cite the anti-pattern ID alongside the BP ID in the finding, and base the remediation on the Right example (adapted to the workload's IaC dialect and actual resource names).

### AP-SEC-01: Wildcard IAM action grants
**Detect:** `"Action": "*"` or service-wide wildcards (`"Action": ["s3:*", ...]`) combined with `"Resource": "*"` in any IAM policy document — Terraform `aws_iam_policy` / `aws_iam_role_policy`, CloudFormation `AWS::IAM::Policy` or inline role policies, CDK `iam.PolicyStatement` with `actions: ["*"]`.
**Maps to:** SEC03-BP02
**Wrong:**
```hcl
resource "aws_iam_role_policy" "app" {
  role = aws_iam_role.app.id
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [{ Effect = "Allow", Action = "*", Resource = "*" }]
  })
}
```
**Right:**
```hcl
resource "aws_iam_role_policy" "app" {
  role = aws_iam_role.app.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = ["s3:GetObject", "s3:PutObject"]
      Resource = "${aws_s3_bucket.uploads.arn}/*"
    }]
  })
}
```

### AP-SEC-02: Public S3 bucket / missing Block Public Access
**Detect:** No `aws_s3_bucket_public_access_block` for a bucket (or any of its four flags false); CloudFormation `AWS::S3::Bucket` without `PublicAccessBlockConfiguration`; CDK `Bucket` with `blockPublicAccess` unset or weakened; bucket ACLs `public-read`/`public-read-write`; bucket policies with `"Principal": "*"` and no restricting condition.
**Maps to:** SEC08-BP04 (related: SEC03-BP07)
**Wrong:**
```hcl
resource "aws_s3_bucket" "uploads" {
  bucket = "app-uploads"
}
# no aws_s3_bucket_public_access_block anywhere in the module
```
**Right:**
```hcl
resource "aws_s3_bucket_public_access_block" "uploads" {
  bucket                  = aws_s3_bucket.uploads.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

### AP-SEC-03: Unencrypted data at rest (S3, EBS, RDS)
**Detect:** Terraform `aws_db_instance` without `storage_encrypted = true`; `aws_ebs_volume` or launch-template block devices without `encrypted = true`; no `aws_s3_bucket_server_side_encryption_configuration` for a bucket; CloudFormation `AWS::RDS::DBInstance` without `StorageEncrypted: true` or `AWS::EC2::Volume` without `Encrypted: true`; CDK storage constructs with encryption explicitly disabled or left to an unencrypted default.
**Maps to:** SEC08-BP02
**Wrong:**
```hcl
resource "aws_db_instance" "orders" {
  engine         = "postgres"
  instance_class = "db.t3.medium"
}
```
**Right:**
```hcl
resource "aws_db_instance" "orders" {
  engine            = "postgres"
  instance_class    = "db.t3.medium"
  storage_encrypted = true
  kms_key_id        = aws_kms_key.data.arn
}
```

### AP-SEC-04: Hardcoded credentials or secrets in code
**Detect:** String literals assigned to names matching `password|secret|api[_-]?key|token` in application code or IaC; secrets passed as plaintext Lambda/ECS environment variables; committed `.env` files; connection strings with embedded credentials.
**Maps to:** SEC02-BP03
**Wrong:**
```hcl
resource "aws_lambda_function" "api" {
  # ...
  environment {
    variables = { DB_PASSWORD = "p@ssw0rd123" }
  }
}
```
**Right:**
```hcl
resource "aws_lambda_function" "api" {
  # ...
  environment {
    variables = { DB_SECRET_ARN = aws_secretsmanager_secret.db.arn }
  }
}
# function code resolves the secret at runtime via secretsmanager:GetSecretValue
```

## Security-Specific Report Format

When producing a pillar-scoped security report, include:
- **Security Scorecard** with 6 domains: Identity & Access, Data Protection (at rest), Data Protection (in transit), Network Protection, Compute Protection, Detection & Response
- **Compliance Mapping** table if compliance requirements specified (map findings to SOC2/HIPAA/PCI-DSS controls)
- **Quick Wins / Foundation / Strategic** remediation tiers

## Calibration

- Flag protocol-level risks explicitly: TLS < 1.2 is always Critical, weak ciphers always High
- "Cannot Determine" is valid for operational aspects (e.g., actual IAM usage requires Access Analyzer data)

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
