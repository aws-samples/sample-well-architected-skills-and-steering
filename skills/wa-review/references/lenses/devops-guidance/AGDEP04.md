**Saga**: Automated governance
**Capability**: AG.DEP — Dynamic environment provisioning

---

# [AG.DEP.4] Codify environment vending

**Category:** RECOMMENDED

A core benefit of the DevOps model is team autonomy and reducing cross-team
dependencies. Through infrastructure as code (IaC), teams can establish and manage their
environments autonomously in a self-service manner, shifting from traditional methods
where operations teams would oversee these responsibilities.

By provisioning environments, and the accounts operating them,
as IaC or API calls, teams are empowered with the flexibility
to create environments according to their specific
requirements and ways of working. Codifying the environment
provisioning process provides teams with the flexibility to
create both persistent and ephemeral environments based on
their specific needs and workflows. In particular, this
code-based approach enables the easy creation of ephemeral
environments that can be automatically setup and torn down
when not in use, optimizing resource utilization and cost.

Use shared libraries or services that allow teams to request
and manage environments using IaC. These libraries should
encapsulate best practices for environment configuration and
should be designed to be used directly in deployment
pipelines, enabling individual teams to manage their
environments autonomously. This reduces the need for manual
requests or interactions with a developer portal, as well as
reduces the reliance on platform teams for provisioning and
managing environments on their behalf. This approach promotes
consistency and reduces overhead from cross-team
collaboration.

**Related information:**

- [What
is the AWS CDK?](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [Create
an AWS Proton environment](https://docs.aws.amazon.com/proton/latest/userguide/ag-create-env.html)
- [Provision
and manage accounts with Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
- [Provision
Accounts Through Service Catalog](https://docs.aws.amazon.com/controltower/latest/userguide/service-catalog.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.4-codify-environment-vending.html*
