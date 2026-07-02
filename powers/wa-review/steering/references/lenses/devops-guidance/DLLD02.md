**Saga**: Development lifecycle
**Capability**: DL.LD — Local development

---

# [DL.LD.2] Consistently provision local environments

**Category:** FOUNDATIONAL

Standardize and automate the process for setting up local development environments
using managed services, infrastructure as code (IaC), and scripted automation. This approach
permits environments to be reliably replicated across different systems and teams, ensuring
uniformity. Consistent local environments help to reduce issues that occur only on particular machines.

Create a baseline configuration for your local development environment that mirrors
the production setup as closely as possible. Use IaC tools to define this environment, and
script the provisioning process. All IaC and scripts should be version-controlled, helping
to ensure that any changes are tracked and can be rolled back if necessary. Educate
developers on the importance of using the provisioned environments and provide documentation
on how to set up and troubleshoot these environments. Regularly review and update the
baseline configuration to keep it aligned with changes in the production environment.
Consider allowing developers to request local environments on-demand through a self-service
developer portal.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.2-consistently-provision-local-environments.html*
