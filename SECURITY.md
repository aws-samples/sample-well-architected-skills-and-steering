# Security Checklist

This checklist applies to all skills, scripts, and reference content in this repository. Contributors MUST verify each item before submitting changes.

## Skills (SKILL.md and references/)

### Credentials and secrets

- [ ] No credentials, passwords, endpoints, or secrets are hardcoded in examples
- [ ] Credential storage examples reference AWS Secrets Manager or Parameter Store
- [ ] Ephemeral credentials are preferred (IAM roles over IAM users, IAM auth over username/password)
- [ ] Example code uses placeholder values (`ACCOUNT_ID`, `example.com`, `CHANGE_ME`) not real identifiers

### IAM and access

- [ ] Examples use least-privilege IAM policies — no `*FullAccess` policies or `service:*` wildcards
- [ ] Resource policies include condition keys (`aws:SourceArn`, `aws:SourceAccount`) where applicable
- [ ] No `0.0.0.0/0` in security group examples without explicit callout that it's an anti-pattern
- [ ] `authorization: NONE` or open access is never used as a default

### Data protection

- [ ] Encryption at rest and in transit is recommended for all storage and transmission
- [ ] Risks of sensitive data in notifications, logs, and responses are noted
- [ ] Notification recipients (email, SNS) use `example.com` not real addresses

### Web and API surfaces

- [ ] Public-facing APIs recommend AWS WAF for defense in depth
- [ ] Security headers are included for web-facing resource examples (CSP, HSTS)
- [ ] Input validation, throttling, and rate limiting are recommended for APIs

### Observability

- [ ] CloudTrail, access logs, and CloudWatch alarms are recommended
- [ ] Log retention periods are set explicitly (not infinite by default)

### Naming and defaults

- [ ] No production-like naming (`PROD`, `production`) as default values in examples
- [ ] Secure defaults are provided rather than simplified insecure settings
- [ ] An explicit "Security Considerations" section is included when the skill touches sensitive operations

## Scripts (scripts/)

### Dependencies

- [ ] Scripts use Python standard library where possible
- [ ] Amazon-owned packages (boto3, aws-cdk-lib) are acceptable without justification
- [ ] Non-Amazon third-party packages require documented justification (why stdlib can't do it, package maintenance status)
- [ ] No `pip install` of unvetted packages from skill instructions

### Execution

- [ ] Scripts do not require elevated privileges (no `sudo`, no root)
- [ ] Scripts do not write outside the project directory without explicit user confirmation
- [ ] Scripts handle errors gracefully (no silent failures that leave partial state)
- [ ] Network requests use HTTPS and validate TLS

### Secrets in scripts

- [ ] Scripts do not hardcode credentials or API keys
- [ ] Environment variables or AWS credential chain are used for authentication
- [ ] No secrets are logged or printed to stdout

## Examples (examples/)

Examples contain intentionally insecure code for demonstration purposes. They MUST:

- [ ] Include a clear README stating the code is deliberately flawed
- [ ] Use `example.com` for all email/domain references
- [ ] Use obvious placeholders for passwords (`CHANGE_ME_insecure_password_123`)
- [ ] Never contain real AWS account IDs, ARNs, or credentials
- [ ] Not be deployable to production without modification (missing required fields, placeholder values)

## Reporting Security Issues

If you discover a security vulnerability in this project, please report it through the [AWS Vulnerability Reporting](https://aws.amazon.com/security/vulnerability-reporting/) page. Do not open a public issue.

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
