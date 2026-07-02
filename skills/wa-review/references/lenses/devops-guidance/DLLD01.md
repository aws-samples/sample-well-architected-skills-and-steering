**Saga**: Development lifecycle
**Capability**: DL.LD — Local development

---

# [DL.LD.1] Establish development environments for local development

**Category:** FOUNDATIONAL

Create development environments that provide individual developers with a safe space
to test changes and receive immediate feedback without impacting others on the team or
shared environments. Development environments are small scale, production-like environments
that provide a balance between providing developers with accurate feedback and being low
cost and easy to manage. Development environments serve a [different purpose](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/sandbox-ou.html#sandbox-and-development-environments) than sandbox environments and should be used for day-to-day
development and experimentation that requires access to your software components and
services.

Development environments can take the form of dedicated cloud environments, local
emulations of infrastructure, or be hosted on a local workstation. While most cloud
providers, open-source tools, and third parties provide options for emulating infrastructure
locally on development machines, these tools might not have full feature parity, leaving
them to only be suitable for a subset of use cases. Using cloud-based development
environments provides the most reliable, accurate, and complete coverage when working with
cloud workloads. We recommend providing a cloud-based development environment to each
developer, with each environment being in a separate AWS account.

Developers should be encouraged to use their own development environments for testing
and debugging to reduce the chance of problems occurring in environments shared by the
broader team. To keep the development environment as close to the production setup as
possible, deployments to the development environment should be sourced from the main
releasable branch, rather than from long-lived development branches. The development
environment setup should be well-documented in an up-to-date playbook that is readily
available to all members of the team. For this to be effective, the playbook must be updated
as the needs of the team and environment change over time. Ideally, the full lifecycle of
these environments, including provisioning, are managed through automated governance
processes.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS02-BP05
Optimize team member resources for activities performed](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a6.html)
- [Setting
Up Your AWS Environment](https://aws.amazon.com/getting-started/guides/setup-environment/)
- [Dev
Environments in CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment.html)
- [Best
practices for testing serverless applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-application-testing/best-practices.html)
- [Improving
the development cycle - Testing in the cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-dev-cycle.html)
- [Improving
the development cycle - Testing locally](https://docs.aws.amazon.com/prescriptive-guidance/latest/hexagonal-architectures/improve-dev-cycle.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.1-establish-development-environments-for-local-development.html*
