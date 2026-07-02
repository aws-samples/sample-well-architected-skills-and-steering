# EUCREL09 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL09-BP01 Implement and test rollback plan for every change you make in EUC environments

Develop rollback plans for changes in Amazon WorkSpaces and
WorkSpaces Applications to anticipate and address potential failures and
their impacts to system stability or resilience. By establishing
these plans, businesses can proactively address unforeseen
situations that may arise during implementation, creating a
smooth transition back to previous configurations if needed.
Test rollback procedures beforehand to gain insights into their
effectiveness and identify any potential areas of improvement.
This proactive approach minimizes service interruptions and
facilitates prompt recovery from incidents or failures,
supporting continuous service delivery and reducing impact on
users.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Develop rollback plans for changes that could potentially
impact WorkSpaces and WorkSpaces Applications resiliency or stability.
Define procedures for reverting to the previous state if a
change causes unexpected incidents or service disruptions.
Test and validate rollback plansto verify their effectiveness
and minimize the time required to restore service in such
situations in the event of a rollback.

Additionally, consider implementing automated rollback
mechanisms where feasible to streamline the recovery process
and reduce manual intervention. By prioritizing rollback
planning and testing, organizations can enhance their ability
to respond effectively to unexpected challenges and maintain
continuous operations in their EUC environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel09-bp01.html*

---
