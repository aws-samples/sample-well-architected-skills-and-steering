**Saga**: Automated governance
**Capability**: AG.SAD — Secure access and delegation

---

# [AG.SAD.6] Conduct periodic identity and access management reviews

**Category:** FOUNDATIONAL

With the distributed nature of DevOps Identity and Access Management (IAM)
responsibilities, it is important to systematically review IAM roles and permissions
periodically. This helps ensure that changes in roles and permissions align with the rapidly
shifting needs of the organization, and that the guardrails set in place for delegation are
working as intended or perhaps need to be fine-tuned. This activity aids in identifying
unused or overly broad permissions, reinforcing the adherence to the principle of least
privilege and reducing potential security risks.

Optionally, automate the right-sizing of permissions as part
of these reviews. This proactive approach not only keeps IAM
policies up-to-date, but also minimizes potential avenues for
unauthorized access, further strengthening your overall
security posture. Automatically right sizing roles and
permissions based on actual activity allows organizations to
scalably enforce that the right resources are accessible to
the right entities, at the right times.

**Related information:**

- [AWS Well-Architected Security Pillar: SEC03-BP04 Reduce
permissions continuously](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_permissions_continuous_reduction.html)
- [Regularly
review and remove unused users, roles, permissions,
policies, and credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#remove-credentials)
- [Use
IAM Access Analyzer to generate least-privilege policies
based on access activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-gen-least-privilege-policies)
- [Verify
public and cross-account access to resources with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-preview-access)
- [Using
AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [Blog: IAM Access Analyzer makes it easier to implement least
privilege permissions by generating IAM policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
- [Blog: Continuous
permissions rightsizing to ensure least privileges in AWS
using CloudKnox and AWS Config](https://aws.amazon.com/blogs/mt/continuous-permissions-rightsizing-ensure-least-privileges-aws-using-cloudknox-aws-config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.sad.6-conduct-periodic-identity-and-access-management-reviews.html*
