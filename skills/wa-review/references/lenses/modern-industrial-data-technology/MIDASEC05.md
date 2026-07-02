# MIDASEC05 — Data protection

**Pillar**: Security  
**Best Practices**: 3

---

# MIDASEC05-BP01 Define access permissions

Establish clear and granular access permissions to control who can access industrial
data, based on job roles and operational responsibilities.

**Desired outcome:** Only authorized personnel can access
specific data resources, reducing the risk of data leakage or misuse.

**Benefits of establishing this best practice:** Supports
principle of least privilege, improves accountability, and reduces insider threats.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use IAM policies and resource tagging strategies to enforce fine-grained permissions
aligned to user roles.

### Implementation steps

- Inventory data assets and define roles for access control.
- Apply IAM roles and permissions based on job functions.
- Use resource tags to apply conditional access policies.
- Review and refine permissions regularly using AWS IAM Access Analyzer.

## Resources

- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Using IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp01.html*

---

# MIDASEC05-BP02 Build user identity solutions

Deploy centralized identity systems that integrate with existing directories and cloud
resources to manage user authentication and authorization efficiently.

**Desired outcome:** Consistent and secure identity management
across all industrial and cloud systems.

**Benefits of establishing this best practice:** Improves user
lifecycle management, simplifies access governance, and enhances login security with MFA and
federation.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement AWS IAM Identity Center or integrate third-party identity providers with AWS.

### Implementation steps

- Deploy IAM Identity Center for central identity control.
- Enable federation with existing AD or SAML-based systems.
- Set up MFA for all privileged roles and access points.
- Log all authentication events using AWS CloudTrail.

## Resources

- [AWS Identity and Access Management Access Analyzer](https://aws.amazon.com/iam/identity-center/)
- [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp02.html*

---

# MIDASEC05-BP03 Implement data authorization models

Design and implement scalable data authorization frameworks using attribute-based or
role-based access control (ABAC or RBAC) models.

**Desired outcome:** Users are granted access to data based on
roles, attributes, or context, supporting scalable and secure access decisions.

**Benefits of establishing this best practice:** Improves
flexibility in data sharing, reduces over-permissions, and enhances compliance controls.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Define authorization attributes based on manufacturing context (like job function,
facility, equipment type, or product line). Implement access controls using AWS Lake Formation for data-level permissions, AWS IAM conditions for resource access, and custom
logic for specialized manufacturing scenarios.

Regularly review access patterns to verify alignment with production needs while
maintaining security boundaries between IT and OT systems.

### Implementation steps

- Define business roles and relevant attributes (for example, plant location or
department).
- Implement policies in Lake Formation or Amazon S3 bucket policies using
conditions.
- Monitor access patterns and refine authorization models over time.
- Log and audit access for compliance reporting.

## Resources

- [What Is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec05-bp03.html*

---
