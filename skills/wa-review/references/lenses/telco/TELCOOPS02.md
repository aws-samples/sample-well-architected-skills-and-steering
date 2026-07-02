# TELCOOPS02 — Multi-account strategy

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# TELCOOPS02-BP01 Telecommunication resources, operations and projects have identified owners

Establish clear ownership and accountability frameworks for telecommunications assets,
operations, and projects through formal assignment of responsibilities to specific individuals
or teams. This includes mapping ownership of applications, VNFs, solutions, and infrastructure
components while documenting their business value proposition and justification for ownership
allocation. Clear ownership structures enable efficient decision-making, streamlined problem
resolution, and effective resource management across the telecommunications environment.

**Desired outcome:**

- Clear ownership structure for resources.
- Documented responsibilities and accountabilities.
- Efficient resource allocation.
- Streamlined decision-making process.
- Effective resource management.
- Clear escalation paths.

**Common anti-patterns:**

- Undefined resource ownership.
- Shared responsibilities without clear boundaries.
- Missing accountability frameworks.
- Incomplete resource documentation.
- Unclear decision authority.
- Resource orphaning.
- Ambiguous escalation paths.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Establish a comprehensive resource ownership model that clearly defines responsibilities
for telecommunications assets, operations, and projects. Implement a centralized resource
management system that tracks ownership details, including primary and secondary owners,
escalation paths, and relevant stakeholders. Create detailed RACI (responsible, accountable,
consulted, informed) matrices for each major resource category to verify clear understanding
of roles and decision-making authority. Develop standardized handover procedures and
documentation requirements to maintain continuity during ownership transitions or
organizational changes.

### Implementation steps

- Implement AWS Resource Groups and Tag Editor to define and manage resource ownership tags, and
integrate with AWS Organizations for hierarchical resource management.
- Use AWS Config to maintain resource inventory and relationships and AWS Systems Manager Resource
Groups for logical grouping of resources by ownership.
- Deploy Service Catalog for standardized resource provisioning with predefined ownership tags and
AWS CloudFormation for automated resource creation with ownership metadata.
- Configure AWS Config Rules for ownership monitoring and Amazon CloudWatch for resource utilization
tracking by owner.
- Use AWS Systems Manager OpsCenter for ownership-related operations management and AWS
Resource Access Manager for controlled resource sharing.

## Resources

**Key AWS services:**

- [Resource Groups and
Tagging for AWS](https://aws.amazon.com/blogs/aws/resource-groups-and-tagging/)
- [AWS Organizations](https://aws.amazon.com/organizations/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops02-bp01.html*

---

# TELCOOPS02-BP02 Adopt a multi-account strategy to isolate different telecommunication workload

Implement a strategic multi-account architecture that effectively separates and isolates
telecommunications workloads while maintaining necessary interconnectivity and operational
efficiency. This approach creates logical boundaries between different environments, services,
and data classifications to enhance security and operational stability. The strategy should
balance the benefits of isolation with the need for seamless integration and management across
the telecommunications landscape.

**Desired outcome:**

- Secure workload isolation.
- Optimized resource management.
- Clear account boundaries.
- Efficient cross-account connectivity.
- Standardized account governance.
- Scalable account structure.

**Common anti-patterns:**

- Single account for each workload.
- No account categorization.
- Excessive account fragmentation.
- Missing connectivity strategy.
- Inconsistent security controls.
- Ad-hoc account creation.
- Poor resource sharing controls.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Design a multi-account architecture that addresses telecommunications-specific isolation
requirements.

Categorize workloads based on:

- Regulatory data sovereignty (separate accounts per country where laws mandate subscriber data remain within borders like EU GDPR, cybersecurity laws, and data localization regulations).
- Subscriber data sensitivity (isolated accounts for CPNI and PII processing with enhanced security controls versus anonymized network telemetry).
- Network function security domains (dedicated accounts for control plane functions like AMF or SMF requiring high security, user plane UPF functions optimized for throughput, and signaling functions requiring Diameter or SIP/SS7 firewall protection).

This categorization enables mapping
telecommunications regulatory and operational requirements to appropriate account boundaries
while maintaining cloud infrastructure efficiency.

Implement a hierarchical Organizational Unit (OU) structure reflecting your telecommunications architecture:

- RAN OU for edge-deployed radio functions
- 5G core OU with separated control and user plane accounts
- IMS OU for multimedia subsystem functions
- BSS OU for billing (PCI DSS compliance) and CRM (PII protection)
- OSS OU for network management and assurance
- Regional compliance OUs for per-country data sovereignty

Apply service control
policies enforcing regulatory requirements (deny cross-region replication from EU accounts for
GDPR, mandatory encryption for billing accounts). Establish standardized connectivity using
centralized transit and private connectivity services with separate paths for control plane
signaling versus user plane data traffic. Deploy centralized logging, monitoring, and security
tooling in dedicated Security OU accounts to maintain visibility and unified governance across
telco workloads.

### Implementation steps

- Deploy AWS Control Tower for automated account setup and use AWS Organizations for hierarchical
account structure and policy management.
- Implement AWS IAM Identity Center for centralized access management and AWS Security Hub CSPM for
multi-account security monitoring.
- Configure AWS Transit Gateway for centralized network connectivity and AWS Network Firewall for
consistent security controls.
- Use AWS Resource Access Manager for cross-account resource sharing and AWS Systems Manager
for centralized operations management.
- Deploy AWS CloudFormation StackSets for multi-account resource deployment and AWS Organizations for
policy-based governance.

## Resources

**Key AWS services:**

- [AWS Organizations](https://aws.amazon.com/organizations/)
- [AWS Control Tower](https://aws.amazon.com/controltower/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [AWS Resource Access Manager](https://aws.amazon.com/ram/)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
- [AWS Network Firewall](https://aws.amazon.com/network-firewall/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops02-bp02.html*

---

# TELCOOPS02-BP03 Predict and mitigate deployment risks by adapting least disruptive deployment strategy for telecommunication workloads

Implement risk-aware deployment strategies that minimize service disruption in
telecommunications environments through predictive analysis, parallel testing, and proactive
capacity management. This approach combines advanced analytics, infrastructure redundancy, and
staged deployment methodologies to verify seamless service delivery while implementing necessary
changes and updates to the network infrastructure.

**Desired outcome:**

- Minimized service disruption during deployments.
- Predictable deployment outcomes.
- Risk-aware deployment processes.
- Automated rollback capabilities.
- Efficient change management.
- Service continuity maintenance.

**Common anti-patterns:**

- Big bang deployments.
- No rollback planning.
- Insufficient testing.
- Missing impact analysis.
- Poor deployment timing.
- Inadequate capacity planning.
- No deployment validation.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Design and implement deployment strategies that minimize service disruption while
maintaining successful changes in telecommunication environments. Establish a comprehensive
risk assessment framework that evaluates potential impacts before deployments, including
dependencies, customer impact, and resource requirements. Create deployment patterns that
utilize blue-green deployments, canary releases, or rolling updates to minimize service
interruption while maintaining the ability to quickly rollback changes. Implement automated
validation and testing procedures throughout the deployment pipeline to catch potential issues
early and verify service quality is maintained during and after deployments.

### Implementation steps

- Use AWS Systems Manager Change Manager for change risk evaluation and AWS Config for
pre-deployment checks.
- Implement AWS CodeDeploy for blue-green deployments and AWS CloudFormation for infrastructure
deployment with rollback capabilities.
- Deploy AWS CodePipeline for automated testing workflows and AWS Fault Injection Service for controlled failure
testing.
- Configure Amazon CloudWatch for deployment monitoring and AWS X-Ray for deployment impact
tracing.
- Use AWS Systems Manager Automation for standardized deployment procedures and Service Catalog for
approved deployment patterns.

## Resources

**Key AWS services:**

- [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS App Runner](https://aws.amazon.com/apprunner/)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops02-bp03.html*

---
