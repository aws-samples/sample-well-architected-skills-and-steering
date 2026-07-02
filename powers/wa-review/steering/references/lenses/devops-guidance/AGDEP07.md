**Saga**: Automated governance
**Capability**: AG.DEP — Dynamic environment provisioning

---

# [AG.DEP.7] Utilize metadata for scalable environment management

**Category:** OPTIONAL

Effective environment management at scale requires the
collection and maintenance of key information about each
environment, such as ownership, purpose, criticality,
lifespan, and more. These details can offer visibility and
clarity which reduces potential confusion and misuse of
environments and assists with setting up proper controls based
on specific details associated with the environment.

Adopt techniques like resource tagging to track and maintain this metadata. Not only
does this allow platform teams to track and optimize costs by accurately attributing
resource usage to specific environments, but it also supports the management of access
controls and security measures, aligning governance and compliance needs with individual
environments.

For implementation, use available tagging features and APIs for resource management
and metadata tracking. Where additional metadata capture is required, consider creating or
integrating with a custom tracking system tailored to your specific needs, such as
existing configuration management database (CMDB) or IT service management (ITSM) tools,
providing a holistic view of all environments, thus empowering platform teams to better
govern and manage environments based on their metadata.

Although this practice is marked as optional, it is strongly
recommended for organizations operating in complex and
large-scale environments, where managing resources and
configurations based on metadata can significantly improve
efficiency, governance, and compliance. This indicator focuses
on leveraging metadata for active environment management,
distinguishing it from the broader scope of configuration item
management.

**Related information:**

- [Choosing
tags for your environment](https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/choosing-tags.html)
- [Tag
policies - AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.7-utilize-metadata-for-scalable-environment-management.html*
