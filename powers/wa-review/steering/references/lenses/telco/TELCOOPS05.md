# TELCOOPS05 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# TELCOOPS05-BP01 Implement standardized provisioning and management of high-performance network interfaces

telco and high-performance network workloads require specialized networking interfaces (like
SR-IOV, DPDK, and Multus) for separating control, management, and data plane traffic. While
other cloud and container solutions provide native support for these interfaces, AWS currently
requires custom implementation. This creates challenges for standardization and automation in
large-scale deployments. Until AWS support becomes available, organizations need to implement
enterprise-grade solutions that provide consistent, supported, and maintainable approaches to
interface provisioning and management.

**Desired outcome:**

- Automated interface provisioning.
- Consistent configuration.
- Scalable deployment process.
- Efficient resource utilization.
- Standardized networking setup.
- Reliable interface management.

**Common anti-patterns:**

- Manual interface configuration.
- Inconsistent setup procedures.
- Poor documentation.
- No automation framework.
- Missing standardization.
- Inefficient resource allocation.
- Ad-hoc management.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Develop an automated interface provisioning system that maintains consistent
configuration and optimal performance for telecommunication workloads. Create standardized
templates and workflows that handle the entire lifecycle of network interfaces, from initial
provisioning through configuration, monitoring, and decommissioning. Implement comprehensive
validation checks at each stage of the provisioning process to verify proper configuration and
block common issues such as IP conflicts or misconfigurations. Establish monitoring and
alerting mechanisms that track interface health, performance metrics, and utilization patterns
to enable proactive management and optimization.

### Implementation steps

- Solution selection:

Evaluate enterprise-supported container networking solutions
- Verify integration capabilities with AWS infrastructure
- Verify vendor support and maintenance agreements
- Document migration strategy for future native AWS capabilities

- Interface management:

Implement vendor-supported automation tools
- Use solution-provided operators where available
- Integrate with AWS service limits and quotas
- Maintain consistent interface naming and tagging

- Operational integration:

Deploy vendor-recommended monitoring solutions
- Integrate with Amazon CloudWatch for infrastructure monitoring
- Establish clear operational boundaries between systems and AWS
- Implement automated health checks

- Support and maintenance:

Establish clear support channels with both vendor and AWS
- Document operational procedures
- Maintain upgrade and patch procedures
- Regular testing of failover scenarios

- Future readiness:

Monitor AWS feature announcements
- Maintain modularity in automation
- Document transition strategy
- Regular architecture reviews

## Resources

**Key AWS services:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Cloud Development Kit (AWS CDK) (CDK)](https://aws.amazon.com/cdk/)
- [AWS Network Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-network-manager.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops05-bp01.html*

---

# TELCOOPS05-BP02 Implement a structured sequence of interface assignment based on the persistent or ephemeral nature of the interfaces

The order of operations is important as the creation and termination of instances often
creates and destroys interfaces. This is a useful property for ephemeral interfaces. However, it
can lead to problems where other resources are dependent on the persistence of an interface and
IP addressed across network domains. Persistent interfaces should be created prior to the
creation of the EC2 instance with their properties assigned through IaC. Upon EC2 instance
creation ephemeral interfaces and addresses can be created at the initialization of the EC2
instance while persistent interfaces which were previously created can be added to the EC2
instance. Thus, the termination of the instance will remove the ephemeral interfaces while
preserving the persistent interfaces. The persistent interfaces retain their properties and can
be re-assigned to a new EC2 instance without impacting adjacent functions.

**Desired outcome:**

- Clear interface lifecycle management.
- Predictable interface behavior.
- Proper resource dependency handling.
- Efficient interface assignment.
- Minimized service disruption.
- Reliable state management.

**Common anti-patterns:**

- Random interface assignment.
- No lifecycle consideration.
- Missing dependency mapping.
- Improper sequence handling.
- Poor state management.
- Undefined persistence rules.
- Inconsistent cleanup.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Create a structured approach to interface assignment that clearly distinguishes between
persistent and ephemeral interfaces throughout their lifecycle. Develop automated workflows
that handle the creation, attachment, and cleanup of interfaces in the correct sequence,
making sure that persistent interfaces are properly preserved during instance replacements or
updates. Implement state tracking mechanisms that maintain visibility into interface status
and dependencies, enabling proper handling of complex networking scenarios. Establish robust
error handling and rollback procedures to maintain system integrity during interface
operations, while verifying proper cleanup of ephemeral resources.

### Implementation steps

- Use AWS tags for interface type identification and AWS Resource Groups for interface
categorization.
- Deploy AWS Step Functions for orchestrating interface assignment workflow and AWS Lambda for
execution logic.
- Implement AWS CloudFormation for defining interface dependencies and AWS Systems Manager Automation for
sequence execution.
- Use Amazon DynamoDB for interface state tracking and Amazon EventBridge for state change management.
- Configure AWS Systems Manager OpsCenter for interface-related operations and AWS CloudTrail for
interface activity tracking.

## Resources

**Key AWS services:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops05-bp02.html*

---
