**Saga**: Development lifecycle
**Capability**: DL.EAC — Everything as code

---

# [DL.EAC.2] Modernize networks through infrastructure as code

**Category:** FOUNDATIONAL

The practice of managing networking configurations through code, including network
automation, version control, and rigorous testing to ensure quality and stability. Apply
DevOps practices to networking systems to streamline network operations, reduce human
errors, and speed up network deployments. *Networking as code* enables
the predictable and repeatable provisioning of networking components, making
infrastructure more modular and less prone to error.

Managing networking components as code requires cultural, process, and tool changes.
Shift from a centralized, manual model of network management to a more autonomous model
where individual teams can operate independently. Loosely couple networking architectures
to create modular components that can be managed, maintained, and scaled individually. Use
infrastructure as code (IaC) tools to define network infrastructure and configurations and
use development lifecycle capabilities like continuous integration and continuous delivery
(CI/CD) for deploying networking changes. Like other systems, networking changes should
undergo automated testing to provide assurance that they meet functional, non-functional,
and security requirements before deployment.

Often, platform teams manage network components on behalf of
individual teams when possible so that all teams do not need
to become networking experts. However, for cases where this is
not possible, use shared resources or predefined network
configuration templates which have embedded best practices and
secure defaults. This approach encourages predictable and
repeatable provisioning of self-service networking components.
Have guardrails in place within the environment to enforce
compliance of networking requirements.

**Related information:**

- [NetDevOps:
A modern approach to AWS networking deployments](https://aws.amazon.com/blogs/networking-and-content-delivery/netdevops-a-modern-approach-to-aws-networking-deployments/)
- [NetDevSecOps
to modernize AWS networking deployments](https://aws.amazon.com/blogs/networking-and-content-delivery/netdevsecops-to-modernize-aws-networking-deployments/)
- [Field
Notes: Using Infrastructure as Code to Manage Your AWS
Networking Environment](https://aws.amazon.com/blogs/architecture/field-notes-using-infrastructure-as-code-to-manage-your-aws-networking-environment/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.2-modernize-networks-through-infrastructure-as-code.html*
