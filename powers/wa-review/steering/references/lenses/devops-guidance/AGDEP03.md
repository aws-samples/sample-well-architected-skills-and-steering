**Saga**: Automated governance
**Capability**: AG.DEP — Dynamic environment provisioning

---

# [AG.DEP.3] Enable deployment to the landing zone

**Category:** FOUNDATIONAL

Dedicate an environment for each system to host the resources
and tools required to perform controlled and uniform
application deployments to related non-production and
production environments. These deployment environments can
include infrastructure or services such as pipelines and build
agents.

At a minimum, each system should have a set of deployment, test, and production
environments to support the development lifecycle. Having these environments at the system
level, as opposed to sharing environments across multiple systems or at the team level,
provides multiple benefits:

- **Isolation of systems:** Each system's resources are
isolated, reducing the risk of cross-system interference, reaching quotas, and security
breaches.
- **Tailored environments:** The environments can be
customized according to the specific needs of each system, improving efficiency and
reducing unnecessary resource usage.
- **Separation of concerns:** Each environment handles a
specific aspect of the application lifecycle (deployment, testing, production), ensuring
a clean and organized workflow.

The deployment environment should include resources and tools to support building,
validation, promotion, and deployment of the system. A deployment environment may not be
necessary for all organizations and scenarios, such as if your development lifecycle tools
are hosted on-premises or outside of your landing zone. For these use cases, you will need
to verify network connectivity between your external tools and your landing zone
environments.

**Related information:**

- [Spaces
in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces.html)
- [Deployments
OU](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/deployments-ou.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.3-enable-deployment-to-the-landing-zone.html*
