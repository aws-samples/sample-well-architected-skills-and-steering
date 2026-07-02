**Saga**: Development lifecycle
**Capability**: DL.LD — Local development

---

# [DL.LD.10] Manage unused development environments

**Category:** OPTIONAL

Properly managing unused environments prevents unnecessary
resource utilization and potential security threats. When
development environments are not in use, the environment and
associated resources should be disabled or deleted.

Managing unused development environments requires tracking,
disabling, or removing development setups that are dormant or
no longer in active use. Regularly audit the active and
inactive development environments. Implement automated tools
or scripts that monitor activity and provide notifications
regarding dormant environments.

Once identified, these environments should be archived,
disabled, or removed, depending on the future needs of the
project. Treat development environments as ephemeral
environments to reduces the risk of incurring unexpected cost
and leaving potentially insecure resources running.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS02-BP03 Stop
the creation and maintenance of unused assets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)
- [AWS Well-Architected Cost Optimization Pillar: COST04-BP03
Decommission resources](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_decomissioning_resources_decommission.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.10-manage-unused-development-environments.html*
