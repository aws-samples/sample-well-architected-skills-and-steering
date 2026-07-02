**Saga**: Automated governance
**Capability**: AG.DEP — Dynamic environment provisioning

---

# [AG.DEP.8] Implement a unified developer portal for self-service environment management

**Category:** OPTIONAL

Consider implementing a self-service portal that empowers
developers to create, manage, and decommission their own
isolated development or sandbox environments, within the
established boundaries set by the platform team. While
fostering autonomy for development teams, this approach
accelerates the development process and reduces the
operational load on the supporting platform team. To ensure
adherence to the organization's standards and ensure
consistency, the portal could include predefined environment
templates and resource bundles.

While beneficial, the implementation of a developer portal is optional, particularly
if the organization is leveraging codified environment vending as recommended.
Infrastructure as code (IaC) presents an alternative approach that reduces human
intervention.

The self-service portal, if implemented, can adopt the *X as a
Service* (XaaS) interaction model as outlined in the [Team Topologies](https://teamtopologies.com/) book by Matthew Skelton and
Manuel Pais. The portal can evolve over time into a central resource for common, reusable
tools and capabilities preconfigured to comply with organizational standards, facilitating
streamlined automated governance activities. This might include centralized access to
common tools into a unified developer portal, including observability, security, quality,
cost, and organizational use cases. If adopted by many teams, this platform can become an
excellent method for communicating changes within the organization.

**Related information:**

- [The
Amazon Software Development Process: Self-Service
Tools](https://youtu.be/52SC80SFPOw?t=579)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.8-implement-a-unified-developer-portal-for-self-service-environment-management.html*
