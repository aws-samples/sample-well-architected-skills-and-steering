# EUCSEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC01-BP01 Identify discrete groups of users that require access and implement security controls appropriate for their risk profiles

When modelling user access to computing systems, it is important
to consider different risk profiles associated with discrete
groups of users. For example, internal employees and external
contractors will have different risk profiles associated with
them. Because of their risk profile, different security controls
should be applied to the groups of users.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Create a group to manage users associated with each risk
profile. If different discrete sets of users will be
interacting with the AWS EUC services, take a risk-based
approach to determine the risk profile associated with each
group. The groups being considered here are broader than other
AWS services, as you need to consider users across multiple
lines of business each with their own discrete risk profiles
in addition to the standard administrators, developers, and
operators.

Based on the risk profile, implement different security
controls to mitigate residual risks within the groups of
users. A matrix can be used to assess the risks associated
with users. For example, in a scenario where four groups of
internal and external users will be accessing the EUC
services, a 2x2 matrix can be created that captures the type
of users on one axis (for example, internal or external) and
the risk profile of the group of users on the other (for
example, high or low risk). By populating the matrix with the
different groups, you can determine the appropriate risk
posture and apply the appropriate level of security controls
for the user group, such as enforcing multi-factor
authentication. An example matrix is shown in the following
figure for groups of internal and external users that will
access a computing service.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec01-bp01.html*

---
