# EUCSEC05 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC05-BP01 Evaluate applications and data access requirements and implement entitlements accordingly

Assess the types of users, their associated risk profile, and
the access that each group of users requires to understand the
access permissions each group of users require. Map the
requirements to security groups, such as Active
Directory security groups and the required permissions granted
to these groups. Continually maintain the users associated with
the group to verify ongoing appropriate access to applications
and data.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Automate user
entitlements**: Use a provisioning and
entitlement system that automates the addition and removal
of users from groups that provide role-based permissions
access. Automation creates consistency in the approach for
handling permissions.
- **Use templates for user
creation:** Use templates when creating user
accounts to avoid manual configuration of user groups and
settings that may lead to overly permissive access.
- **Review user entitlements
regularly**: Review user entitlements regularly
to verify that they are aligned with each user's current
role and access requirements to fulfill the role. Consider
a regular cadence, such as a quarterly or monthly review.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec05-bp01.html*

---
