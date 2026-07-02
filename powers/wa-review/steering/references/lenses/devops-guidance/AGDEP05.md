**Saga**: Automated governance
**Capability**: AG.DEP — Dynamic environment provisioning

---

# [AG.DEP.5] Standardize and manage shared resources across environments

**Category:** RECOMMENDED

Cross-environment resource sharing is the practice of deploying, managing, and
providing access to common resources across various environments from a centrally managed
account. This approach enables teams to efficiently use and manage shared resources, such
as networking or security services, without the need to replicate their setup in each
environment. By unifying the management of these foundational resources, individual teams
can focus more on the functionality of their workloads, rather than spending time and
effort managing common infrastructure components.

Platform teams should deploy and manage shared resources into
accounts they manage, then provide APIs or libraries that
individual teams can use to consume the shared resources as
needed. This approach reduces redundancy and promotes
standardization across the organization, allowing development
teams to concentrate on their unique workloads rather than
complex infrastructure management.

**Related information:**

- [Infrastructure
OU and accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/infrastructure-ou-and-accounts.html)
- [Sourcing
and distribution](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/sourcinganddistribution.html)
- [Sharing
your AWS resources - AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.5-standardize-and-manage-shared-resources-across-environments.html*
