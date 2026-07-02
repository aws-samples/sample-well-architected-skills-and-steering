**Saga**: Automated governance
**Capability**: AG.ACG — Automated compliance and guardrails

---

# [AG.ACG.2] Implement controlled procedures for introducing new services and features

**Category:** FOUNDATIONAL

To maintain the balance between encouraging innovation and
upholding compliance and governance requirements, platform
teams need a scalable, controlled procedure for introducing
new cloud vendor or third-party services to be used.

DevOps culture encourages continuous learning and exploration
of new technologies, tools, and services. Provide teams with
the ability to explore and experiment with new features and
services while maintaining organizational security and
compliance standards. Structure these exploration
opportunities in a controlled, secure manner, to promote
agility without compromising integrity.

Establish well-defined guardrails that uphold security and
compliance when introducing new features and services. This
includes access restrictions, acceptable use cases, and
alignment with security policies. Create sandbox environments
where teams can safely explore and test these features without
compromising production environments or violating governance
policies. Develop a systematic, scalable onboarding process
which allows platform teams to enable guardrails and policies
for governing usage of the service, which leads to enabling
the feature or service in other environments, including
production.

Follow the principle of least privilege by granting teams access to use only specific
actions or API calls for approved services. As services update and add new features, this
will help ensure that the platform team reserves the ability to perform onboarding
procedures with these new features as well.

**Related information:**

- [Example
service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.acg.2-implement-controlled-procedures-for-introducing-new-services-and-features.html*
