# LSOPS05 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS05-BP01 Enable a configuration management framework

Use a management framework to record resource configurations,
track changes, identify gaps (like defects and issues) and track
resolution of changes.

**Desired outcome:**

- Automated detection of unauthorized or unplanned configuration
changes.
- Centralized visibility into resource dependencies and
relationships.

**Common anti-patterns:**

- Lacking version control for infrastructure configurations.
- Allowing ad-hoc changes without proper documentation or
approval.

**Benefits of establishing this best
practice:**

- Enhanced compliance-alignment through comprehensive
configuration documentation.
- Improved troubleshooting capabilities with complete change
history.
- Faster recovery from incidents through established baseline
restoration.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Build a configuration management system that automatically
discovers and documents resources supporting GxP workloads.
Infrastructure as code enables version control and consistent
deployment, while continuous monitoring detects unauthorized
changes and configuration drift. These capabilities create a
foundation for demonstrating the control required for GxP
adherence while reducing manual overhead.

When implementing resource management for regulated environments,
balance comprehensive tracking with operational efficiency. Focus
on capturing information relevant to regulatory requirements,
including configuration parameters affecting validated
functionality and dependencies between components, while verifying
that your framework accommodates both cloud and on-premises
resources.

### Implementation steps

- Implement automated discovery and inventory management for
IT resources:

- Deploy AWS Config for continuous resource inventory and
configuration tracking.
- Use AWS Systems Manager Inventory for detailed software and
configuration information.

- Establish version-controlled repositories for infrastructure
configurations:

- Use AWS CloudFormation for templated infrastructure
deployment.

- Define formal change management processes for resource
modifications:

- Implement AWS Systems Manager Change Manager for controlled
change processes.
- Consider Service Catalog for standardized resource
provisioning.

- Implement continuous monitoring for configuration drift:

- Configure AWS Config Rules to detect non-compliant
configurations.
- Consider Amazon EventBridge for automated remediation
workflows.

- Create comprehensive system baselines with restoration
capabilities:

- Use AWS Backup for consistent backup and recovery
capabilities.
- Consider AWS Systems Manager Automation for standardized
restoration procedures.

- Document resource relationships and dependencies in a
centralized system:

- Use AWS Resource Groups for logical organization of related
resources.
- Consider AWS Service Management Connector for integration
with existing CMDB systems.

## Resources

**Related examples:**

- [Synchronize
with CMDB](https://docs.aws.amazon.com/en_us/smc/latest/ag/config-sync.html)

**Related tools:**

- [AWS Config](https://aws.amazon.com/config/)
- [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
- [AWS Service Management Connector](https://aws.amazon.com/service-management-connector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops05-bp01.html*

---
