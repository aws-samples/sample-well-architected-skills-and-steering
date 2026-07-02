# MIDASEC02 — Identity and access management

**Pillar**: Security  
**Best Practices**: 4

---

# MIDASEC02-BP01 Enforce least privilege and security policies to control system access

Minimize access rights for users and systems by enforcing least privilege principles.
This reduces the risk of lateral movement and privilege escalation in manufacturing
environments.

**Desired outcome:** Users and systems can only access
resources necessary for their roles, reducing exposure to unauthorized activities.

**Benefits of establishing this best practice:** Limits the
scope of security incidents and enhances overall control over sensitive manufacturing
resources.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Map access requirements for different production roles and critical system
interactions. Implement IAM policies and SCPs aligned with manufacturing functions,
enforcing clear boundaries between IT/OT systems. Monitor access patterns using AWS IAM Access Analyzer to continually align with operational needs.

### Implementation steps

- Conduct role analysis across IT/OT to define minimum required privileges.
- Apply IAM permission boundaries and SCPs at account and organizational unit
levels.
- Use IAM Access Analyzer to detect overly permissive roles.
- Implement regular audits to verify adherence to least privilege policies.

## Resources

**Related documents:**

- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp01.html*

---

# MIDASEC02-BP02 Enable multi-factor authentication (MFA) and token authorization (TA)

Strengthen identity verification by enforcing MFA for human users and implementing
token-based authorization for machines and services.

**Desired outcome:** Stronger authentication for both human
users and industrial systems accessing AWS resources.

**Benefits of establishing this best practice:** Reduces risks
associated with credential theft and replay attacks across IT/OT boundaries.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Enable MFA across all accounts, and integrate token services for secure, time-bound
access.

### Implementation steps

- Require MFA for all AWS accounts and IAM users using virtual or hardware devices.
- Implement SSO with MFA enforcement using AWS IAM Identity Center.
- Use temporary credentials and tokens through AWS Security Token Service for
federated and service access.
- Enable and monitor MFA usage compliance with AWS Config rules.

## Resources

- [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)
- [What is AWS Identity and Access Management Access Analyzer?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Welcome to the AWS Security Token Service API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp02.html*

---

# MIDASEC02-BP03 Use centralized access management tools

Consolidate identity and access management using centralized tools to streamline
permission handling and improve visibility across multi-site operations.

**Desired outcome:** Reduced access complexity and improved
governance across distributed industrial environments.

**Benefits of establishing this best practice:** Simplifies
identity lifecycle management, supports consistent policy application, and enables centralized
logging.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Adopt AWS IAM Identity Center or integrate with external identity providers to unify
access controls.

### Implementation steps

- Set up IAM Identity Center or integrate AWS accounts with your identity provider
(for example, Active Directory).
- Configure fine-grained access permissions mapped to business roles.
- Enable centralized access logging and reporting.
- Regularly update identity mappings to reflect org structure changes.

## Resources

- [What is AWS IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp03.html*

---

# MIDASEC02-BP04 Develop a mechanism for regular review of IAM roles and policies

Establish processes to regularly review IAM roles and permissions to help prevent
privilege creep and maintain access integrity over time.

**Desired outcome:** Stale or over-permissive access is
detected and remediated proactively.

**Benefits of establishing this best practice:** Improves
compliance posture, reduces operational risk, and enforces clean access policies aligned to
least privilege.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use tools like IAM Access Analyzer, AWS Config, and custom automation to audit and
report access configuration regularly.

### Implementation steps

- Establish a schedule for IAM access reviews.
- Use AWS IAM Access Analyzer to identify unused or overly broad permissions.
- Log and track review outcomes for auditing purposes.
- Automate revocation or modification of unneeded permissions using AWS Lambda or
AWS Systems Manager.

## Resources

- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)
- [iam-user-policy-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-user-policy-check.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec02-bp04.html*

---
