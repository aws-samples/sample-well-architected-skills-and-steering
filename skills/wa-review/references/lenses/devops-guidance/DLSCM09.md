**Saga**: Development lifecycle
**Capability**: DL.SCM — Software component management

---

# [DL.SCM.9] Implement plans for deprecating and revoking outdated software components

**Category:** RECOMMENDED

Maintaining an up-to-date and secure code base requires the proactive management of
components, including removing outdated artifacts, libraries, and repositories. Not only
does their removal reduce storage costs, but it also mitigates risks associated with
deploying outdated or potentially vulnerable software. The removal process of outdated
components should comply with the organization's data retention policies.

Develop clear plans for the deprecation and revocation of outdated components. These
plans should include regular audits of the code base to identify deprecated or unused
artifacts, libraries, and repositories. Establish timelines for deprecation and final
removal of identified components. Communicate these plans to your development team and
ensure that they are aware of the timelines.

Consider automating the removal process where feasible, for example, by using scripts
or automated governance tools that support such functionality. By implementing such plans,
you can streamline the code base, making it easier to manage and less prone to errors,
while ensuring security and reducing the risk of system failures.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST04-BP05
Enforce data retention policies](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_data_retention.html)
- [AWS Well-Architected Sustainability Pillar: SUS02-BP03 Stop
the creation and maintenance of unused assets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.scm.9-implement-plans-for-deprecating-and-revoking-outdated-software-components.html*
