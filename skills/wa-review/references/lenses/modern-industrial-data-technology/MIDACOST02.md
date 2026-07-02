# MIDACOST02 — Data lifecycle

**Pillar**: Cost Optimization  
**Best Practices**: 6

---

# MIDACOST02-BP01 Track resources over their lifetime

Implement complete visibility and control over resource lifecycle costs from creation to
deletion, with comprehensive tagging aligned to manufacturing processes. This includes
monitoring resource utilization against production metrics, implementing clear ownership and
purpose documentation, and regularly reviewing resource usage patterns. Essential for
understanding total cost of ownership and identifying optimization opportunities.

**Desired outcome:** Complete visibility and control over
resource lifecycle costs from creation to deletion.

**Common anti-patterns:**

- Creating resources without implementing a consistent tagging strategy from day one
- Failing to assign clear ownership of resources during provisioning
- Using generic tags that do not reflect manufacturing-specific contexts (production
line, cell, product)
- Neglecting to track resource dependencies, leading to orphaned resources after
decommissioning
- Maintaining resources without clear business justification
- Not implementing automated cleanup procedures for temporary resources
- Tracking only active resources while ignoring deprecated or archived industrial data
- Using the same lifecycle management approach for all data types regardless of their
criticality or retention requirements
- Failing to consider data compliance requirements when implementing lifecycle policies
- Not accounting for seasonal production variations when evaluating resource
utilization
- Implementing lifecycle tracking tools without proper team training and documentation
- Allowing multiple teams to create resources without centralized visibility and
governance

**Benefits of establishing this Best Practice:**

- Improved resource utilization
- Reduced waste from unused resources
- Better understanding of resource ROI
- Enhanced cost allocation accuracy

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Inventory of all manufacturing systems (for example, SCADA, MES, and PLM)
- Mapping of data flows between shop floor and enterprise systems
- Compliance requirements for data retention in your industry

Key decisions needed:

- Resource tagging strategy aligned with production lines and processes
- Lifecycle stages specific to manufacturing data and systems
- Thresholds for resource utilization in different production scenarios

Establish a systematic approach to track resources throughout their entire
lifecycle, from provisioning to decommissioning, with appropriate governance controls for
optimal utilization and cost management in your manufacturing environment.

Consider the following:

- Mapping cloud resources to specific production lines or product types
- Tracking resource usage against production output metrics
- Implementing different lifecycle policies for operational versus analytical data
- Aligning resource reviews with production cycles or shift patterns

Regularly review resource utilization in the context of manufacturing KPIs and adjust
your tracking approach based on changes in production processes or compliance requirements.

### Implementation steps

- Implement comprehensive tagging strategy aligned with manufacturing processes.
- Track resource creation, modification, and usage patterns in relation to
production cycles.
- Monitor resource dependencies, especially between OT and IT systems.
- Document resource ownership and purpose, involving both IT and operations teams.
- Conduct regular reviews of resource utilization metrics against production output.
- Implement automated reporting on resource lifecycle stages, integrated with
manufacturing dashboards.

## Key AWS services

- AWS Config
- AWS Systems Manager
- AWS Resource Groups
- AWS Tag Editor
- AWS Cost Explorer
- AWS Application Cost Profiler
- AWS Trusted Advisor

## Resources

**Related documents:**

- [Tagging AWS Resources and Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)
- [Evaluating Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)

- [AWS Resource Groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-resource-groups.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp01.html*

---

# MIDACOST02-BP02 Implement manufacturing-aware resource decommissioning process

Systematically remove unused resources while preserving critical manufacturing data,
maintaining production system integrity, and complying with industrial requirements. This
involves careful consideration of dependencies between manufacturing systems, data retention
requirements, and proper archival procedures before resource removal.

**Desired outcome:** Systematic removal of unused resources
while preserving critical manufacturing data, maintaining production system integrity, and
complying with industrial requirements.

**Common anti-patterns:**

- Decommissioning resources without checking their connection to active production
lines
- Failing to preserve quality control and compliance data before resource removal
- Not considering seasonal manufacturing patterns when identifying unused resources
- Decommissioning without checking impact on OT or IT integrated systems
- Removing resources without validating manufacturing regulatory requirements
- Failing to archive production performance data and custom configuration settings
before decommissioning
- Not considering maintenance and repair history requirements

**Benefits of establishing this Best Practice:**

- Reduced costs from unnecessary resource retention
- Minimized risk of accidental data loss
- Clear process for resource retirement
- Compliance with data governance requirements

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Establish formal processes for identifying and safely decommissioning resources in your
manufacturing setup that are no longer needed, while meeting data preservation requirements
and managing dependencies.

### Implementation steps

- Create decommissioning criteria based on:

Resource utilization thresholds
- Business value assessment
- Data retention requirements

- Establish approval workflows.
- Document dependencies and impact analysis.
- Create backup and archival procedures.
- Implement verification steps post-decommissioning.
- Consider manufacturing-specific decommissioning criteria:

Production line changeovers
- End of product lifecycle
- Equipment replacement cycles
- Historical data retention for quality compliance and machine learning

## Key AWS services

- AWS Backup
- Amazon S3 Lifecycle policies
- AWS Organizations
- Amazon CloudWatch
- AWS Glue Data Catalog

## Resources

**Related documents:**

- [Amazon Simple Storage Service: Examples of S3 Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp02.html*

---

# MIDACOST02-BP03 Automate production-aware resource decommissioning

Implement automated identification and removal of unused resources synchronized with
production schedules, product lifecycles, and manufacturing compliance requirements. This
automation includes safety checks, rollback procedures, and consideration of maintenance
windows to help prevent disruption to manufacturing operations.

**Desired outcome:** Automated identification and removal of
unused resources synchronized with production schedules, product lifecycles, and manufacturing
compliance requirements.

**Common anti-patterns:**

- Implementing automated removal without considering production schedules
- Using the same automation rules for both IT and OT resources
- Not incorporating manufacturing compliance checks in automation
- Failing to account for interdependencies with MES, SCADA, or other manufacturing
systems
- Automated decommissioning during production hours
- Not maintaining audit trails for regulated manufacturing processes
- Bypassing quality management system validations

**Benefits of establishing this best practice:**

- Reduced manual intervention
- Consistent application of decommissioning policies
- Immediate cost savings from unused resource removal
- Reduced human error

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Create automated systems that can safely identify, tag, notify relevant stakeholders,
and finally remove resources that are no longer needed, with appropriate safeguards to help
prevent disruption to manufacturing operations.

### Implementation steps

- Define automation rules for resource identification.
- Create automated workflows for:

Resource tagging
- Notification of stakeholders
- Backup creation
- Resource termination

- Implement safety checks and rollback procedures.
- Monitor automation effectiveness.
- Include manufacturing-specific automation rules:

Production schedule-aware decommissioning
- Product lifecycle milestones
- Equipment maintenance windows
- Shift pattern considerations

## Key AWS services

- AWS Lambda
- Amazon EventBridge
- AWS Config Rules
- AWS Systems Manager Automation
- AWS Step Functions
- Amazon SNS

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/scheduler.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Building Lambda functions with Python](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp03.html*

---

# MIDACOST02-BP04 Implement manufacturing-specific data retention policies

Implement cost-effective industrial data management that balances retention requirements
for production data, quality records, and compliance needs with optimized storage costs. This
includes implementing tiered storage strategies and automated archival processes.

**Desired outcome:** Cost-effective industrial data management
that balances retention requirements for production data, quality records, and compliance
needs with optimized storage costs.

**Common anti-patterns:**

- Applying generic IT data retention policies to manufacturing data
- Failing to differentiate between operational data and long-term quality records
- Overlooking industry-specific regulations (for example, FDA, ISO) in retention
policies
- Storing manufacturing data indefinitely without a defined purpose
- Not considering data dependencies in retention schedules (for example, keeping raw
data but deleting related metadata)
- Implementing retention policies without input from production and quality teams

**Benefits of establishing this best practice:**

- Alignment with regulatory requirements
- Optimized storage costs
- Clear data lifecycle management
- Reduced risk of compliance violations

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement comprehensive data retention policies that store manufacturing data only as
long as necessary for operational, regulatory, and business purposes while optimizing
storage costs.

### Implementation steps

- Document regulatory requirements.
- Define data classification schemes.
- Create retention schedules.
- Implement automated archival processes.
- Set up compliance monitoring.
- Regular policy review and updates.

## Key AWS services

- Amazon S3 Lifecycle policies
- Amazon Glacier
- AWS Backup
- AWS Storage Gateway
- Amazon Macie
- AWS CloudTrail

## Resources

**Related documents:**

- [Amazon Simple Storage Service: Managing the lifecycle of
objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp04.html*

---

# MIDACOST02-BP05 Develop cloud resource policies aligned with manufacturing operations

Create well-defined policies for cloud resource provisioning, usage, and management that
reflect specific manufacturing processes, compliance requirements, and cost optimization
goals. These policies should consider both IT and OT needs while maintaining operational
efficiency.

**Desired outcome:** Well-defined policies for cloud resource
provisioning, usage, and management that reflect specific manufacturing processes, compliance
requirements, and cost optimization goals.

**Common anti-patterns:**

- Creating generic cloud policies without considering manufacturing-specific needs
- Implementing policies that hinder rapid scaling during production spikes
- Overlooking OT or IT integration in policy development
- Failing to involve key stakeholders (for example, production managers and quality
control) in policy creation
- Not accounting for different policy needs across various manufacturing stages
(design, production, and maintenance)
- Implementing strict cost-saving policies that compromise manufacturing system
reliability

**Benefits of establishing this best practice:**

- Standardized resource management
- Clear governance framework
- Aligned business and IT objectives
- Improved cost control

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Develop and implement comprehensive policies that reflect your organization's specific
manufacturing requirements while improving cost optimization.

### Implementation steps

- Document organizational requirements:

Manufacturing process needs
- Compliance requirements
- Cost optimization targets

- Create policy frameworks for:

Resource provisioning
- Access control
- Cost allocation
- Data management

- Establish review and approval processes.
- Implement policy enforcement mechanisms.

## Key AWS services

- AWS Organizations
- AWS Control Tower
- Service Catalog
- AWS IAM
- AWS Config
- AWS CloudFormation

## Resources

**Related documents:**

- [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
- [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html)
- [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp05.html*

---

# MIDACOST02-BP06 Implement manufacturing-aware cost controls

Establish effective guardrails that help prevent unnecessary spending while maintaining
operational efficiency and flexibility for production demands. This includes implementing
approval workflows that don't hinder urgent production needs and differentiating between cost
controls for different environments (production, development, testing).

**Desired outcome:** Effective guardrails that help prevent
unnecessary spending while maintaining operational efficiency and flexibility for production
demands.

**Common anti-patterns:**

- Applying blanket cost controls without considering critical manufacturing systems
- Implementing rigid resource limits that don't account for production variability
- Neglecting to create separate cost control policies for research and development, production, and
quality assurance environments
- Failing to align cost control measures with manufacturing cycles and seasonal demands
- Implementing approval workflows that cause delays in scaling resources for urgent
production needs
- Not differentiating between cost controls for operational data and long-term
compliance data storage
- Implementing strict policies that hinder engineering research and development or applying overly
permissive policies that lead to over provisioning
- Not training employees on best practices of deploying right-sized
infrastructure/services that balance cost and performance

**Benefits of establishing this Best Practice:**

- Avoided cost overruns
- Controlled resource provisioning
- Enhanced budget compliance
- Improved cost predictability

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish mechanisms to monitor, control, and optimize cloud spending for manufacturing
workloads while verifying that critical operational systems maintain necessary resources.

### Implementation steps

- Define cost control mechanisms:

Budget thresholds
- Resource limits
- Approval workflows

- Implement automated enforcement.
- Create exception processes.
- Monitor control effectiveness.
- Regular review and adjustment.

## Key AWS services

- AWS Budgets
- AWS Cost Explorer
- AWS Service Quotas
- AWS Organizations
- AWS CloudFormation
- AWS Control Tower

## Resources

**Related documents:**

- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [AWS Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
- [AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-cost-categories.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost02-bp06.html*

---
