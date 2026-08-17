# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 5

---

# MIDACOST01 — Forecast and optimize

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MIDACOST01-BP01 Implement data-driven cost management using AWS cost tools and manufacturing data

Create reliable cost forecasts by combining AWS usage data with manufacturing schedules
to enhance resource provisioning and budget planning accuracy. This involves analyzing
production patterns, seasonal variations, and historical cloud usage to make informed
decisions about resource allocation and cost optimization.

**Desired outcome:** Develop precise monthly and quarterly cost
forecasts by combining AWS usage data with manufacturing schedules to improve forecast
reliability for resource provisioning and budget planning.

**Common anti-patterns:**

- Relying solely on default AWS cost reports without implementing
manufacturing-specific cost allocation tags
- Making resource provisioning decisions based on short-term usage data
- Failing to account for seasonal production variations when forecasting cloud costs
- Using the same forecasting approach for all types of manufacturing workloads without
considering their unique characteristics
- Neglecting to correlate cloud spending with production output metrics
- Setting static budgets without considering manufacturing cycles and production
schedules
- Making Reserved Instance or Savings Plan commitments without analyzing historical
usage patterns
- Ignoring the impact of planned maintenance windows and product launches on resource
requirements

**Benefits of establishing this Best Practice:**

- Improved budget planning and cost predictability
- Better alignment between IT spending and OT production needs
- Reduced risk of over-provisioning or under-provisioning resources
- Enhanced ability to optimize costs during varying production cycles

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

To systematically analyze and optimize costs:

- Configure AWS Cost Explorer to track resource usage by manufacturing workload
- Set up cost allocation tags that map to specific production lines and processes
- Create monthly reports comparing AWS resource utilization with production output
- Use AWS Budgets to set alerts based on predicted usage thresholds
- Integrate production scheduling data from your MES/ERP systems with AWS cost
management tools
- Review and adjust resource allocation quarterly based on collected metrics

### Implementation steps

- Enable detailed cost and usage reporting for all cloud resources.
- Create cost allocation tags aligned with manufacturing processes.
- Establish a system to collect and analyze production schedule data.
- Implement forecasting models that consider:

Seasonal production variations
- Planned maintenance windows
- New product launches
- Historical resource utilization patterns

- Set up regular review cycles to validate forecasts against actual usage.
- Take advantage of cost saving mechanisms like AWS Savings Plans and Spot Instances.

## Key AWS services

- AWS Cost Explorer
- AWS Budgets
- AWS Supply Chain
- Amazon SageMaker AI Canvas
- AWS Data Exports with Quick

## Resources

**Related documents:**

- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Demand Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-planning.html)
- [Time Series Forecasts in Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-time-series.html)
- [Cloud Financial
Management with AWS](https://aws.amazon.com/aws-cost-management/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost01-bp01.html*

---

# MIDACOST01-BP02 Configure automated cost monitoring and alerts for manufacturing workloads

Set up a comprehensive alerting system that notifies teams within 24 hours when costs
exceed thresholds, generates cost reports by production line, identifies waste, and maintains
cost visibility across manufacturing operations. This includes setting up progressive alerting
using different severity levels and implementing automated remediation for common cost-related
issues.

**Desired outcome:** Set up a comprehensive alerting system
that:

- Notifies teams within 24 hours when costs exceed defined thresholds
- Generates daily/weekly cost reports by production line
- Identifies resource waste and cost anomalies automatically
- Maintains cost visibility across manufacturing operations

**Common anti-patterns:**

- Setting up generic alerts without considering manufacturing-specific cost patterns
- Creating too many alerts that lead to notification fatigue
- Failing to establish baseline costs before implementing monitoring
- Not differentiating between production and non-production environment alerts
- Sending alerts to a general distribution list instead of specific responsible teams
- Using the same thresholds for different types of manufacturing workloads
- Implementing alerts without defined response procedures
- Focusing only on total cost without considering cost per unit of production
- Not accounting for shift patterns in alert configurations

**Benefits of establishing this Best Practice:**

- Early detection of cost anomalies
- Reduced manual monitoring effort
- Improved cost visibility across teams
- Faster response to cost-related issues

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before setting up automation, verify that you have:

- Identified key stakeholders who need cost alerts (operations, finance, IT teams)
- Determined cost thresholds for different manufacturing processes
- Mapped your AWS resources to specific production lines or cells
- Established baseline costs for normal operations

Then, implement monitoring systems that:

- Track daily or weekly cost variations against production schedules
- Alert relevant teams when costs deviate your set thresholds (for example, 20%) or more from
baseline
- Generate automated reports showing cost per unit of production
- Monitor resource utilization during different manufacturing shifts

### Implementation steps

- Define cost thresholds or budgets for different manufacturing workload
components.
- Configure automated alerts for:

Budget overruns
- Unusual usage patterns
- Idle resources
- Storage growth rates

- Create automated reports for:

Daily, weekly, or monthly cost trends
- Resource utilization and production output
- Cost per manufacturing line, cell, or product

- Establish escalation procedures for cost-related incidents.

## Key AWS services

- AWS Cost Explorer
- AWS Budgets
- AWS CloudTrail
- AWS CloudWatch
- Amazon Simple Notification Service
- AWS Pricing Calculator
- AWS Lambda

## Resources

**Related documents:**

- [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

- [Cost
Optimization with AWS](https://aws.amazon.com/aws-cost-management/cost-optimization/)
- [Logging AWS Cost Management API calls with AWS CloudTrail](https://docs.aws.amazon.com/cost-management/latest/userguide/logging-with-cloudtrail.html)
- [Create a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost01-bp02.html*

---

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

# MIDACOST03 — Migration optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# MIDACOST03-BP01 Analyze all components of your industry workloads for migration and modernization

Develop an optimized migration strategy that reduces costs while maintaining or improving
operational capabilities for manufacturing-specific workloads. This includes analyzing OT and IT
dependencies, assessing modernization opportunities, and planning migrations that minimize
production impact.

**Desired outcome:** Optimized migration strategy that reduces
costs while maintaining or improving operational capabilities.

**Common anti-patterns:**

- Migrating manufacturing systems without analyzing OT and IT dependencies
- Implementing direct migration strategies for all workloads while disregarding
potential optimization opportunities
- Migrating critical production systems first without proper testing
- Overlooking data transfer costs between cloud and on-premises manufacturing equipment
- Planning migration without input from shop floor operations teams
- Ignoring regulatory compliance requirements specific to manufacturing processes
- Making migration decisions based solely on IT costs without considering production
impact
- Not accounting for legacy manufacturing systems' integration requirements

**Benefits of establishing this best practice:**

- Reduced infrastructure costs
- Improved operational efficiency
- Optimized resource utilization
- Clear migration roadmap

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Before starting, verify that you have:

- Complete inventory of IT/OT systems and their dependencies
- Manufacturing process maps and criticality levels
- Compliance and regulatory requirements documented

Key decisions needed:

- Which systems are candidates for migration based on criticality
- Migration strategy selection (rehost, replatform, or refactor) per system
- Migration sequence aligned with production impact
- Cost-saving validation thresholds

Then, analyze industrial workloads by documenting current infrastructure costs, mapping
OT and IT system dependencies (like SCADA to MES connections), and analyzing data transfer
patterns. Evaluate options including rehost, replatform, or modernize based on each
component's needs. Create cost-benefit analyses comparing current versus projected cloud
costs, with particular attention to manufacturing-specific requirements and production
continuity.

### Implementation steps

- Conduct comprehensive workload assessment:

Current infrastructure costs
- Application dependencies
- Performance requirements
- Data transfer patterns

- Evaluate migration options:

Rehost (lift and shift)
- Replatform
- Refactor or modernize

- Create a cost-benefit analysis.
- Develop a migration timeline.
- Plan for optimization post-migration.

## Key AWS services

- AWS Migration Hub
- AWS Application Discovery Service
- AWS Migration Evaluator
- AWS Transform MGN

## Resources

**Related documents:**

- [AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/)
- [AWS Application
Discovery Service](https://docs.aws.amazon.com/application-discovery/)
- [AWS Migration
Evaluator](https://aws.amazon.com/migration-evaluator/)
- [AWS Application Migration
Service](https://docs.aws.amazon.com/mgn/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost03-bp01.html*

---

# MIDACOST04 — Forecast resource provisioning

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# MIDACOST04-BP01 Perform an analysis on the historical manufacturing workloads

Make data-driven resource provisioning decisions based on accurate historical usage
patterns in manufacturing environments. This involves analyzing at least one full production
cycle's data, considering seasonal variations, and accounting for planned maintenance windows
in resource forecasting.

**Desired outcome:** Data-driven resource provisioning
decisions based on accurate historical usage patterns in manufacturing environments.

**Common anti-patterns:**

- Using IT-only metrics without considering manufacturing operations data
- Basing forecasts on insufficient historical data (needs at least one full production
cycle)
- Ignoring seasonal production variations in resource planning
- Not differentiating between development, testing, and production environment needs
- Failing to account for planned maintenance windows in resource forecasting
- Using the same forecasting model for both batch and continuous production processes
- Overlooking equipment upgrade cycles in long-term resource planning
- Not considering quality control and compliance requirements in resource forecasting

**Benefits of establishing this best practice:**

- Improved capacity planning
- Reduced overprovisioning
- Better alignment with production patterns
- Optimized resource costs

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- At least one full production cycle's data
- Historical resource usage patterns across seasons
- Manufacturing schedules and maintenance windows documented

Key decisions needed:

- Forecast horizon based on production cycles
- Resource allocation thresholds for different workload types
- Scaling trigger points aligned with manufacturing needs
- Data retention requirements for compliance

Systematically collect and analyze resource utilization data from manufacturing
systems to identify usage patterns and correlations with production cycles. Use these
insights to create forecasting models that align with actual manufacturing operations,
considering both IT and OT systems for comprehensive resource planning.

### Implementation steps

- Collect historical data on:

Resource utilization
- Production cycles
- Seasonal variations
- Peak usage periods

- Analyze patterns and trends:

Daily/weekly/monthly patterns
- Production correlation
- Seasonal impacts

- Create baseline metrics.
- Develop forecasting models.
- Validate predictions against actual usage.

## Key AWS services

- Quick
- AWS Cost Explorer
- Amazon CloudWatch
- AWS Systems Manager
- Amazon SageMaker AI

## Resources

**Related documents:**

- [Quick](https://docs.aws.amazon.com/quicksight/latest/user/creating-visuals.html)
- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Metrics in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)
- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/best-practices-for-compute-optimizer.html)
- [Use the
SageMaker AI AI DeepAR forecasting algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar.html)
- [Time Series Forecasts in Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-time-series.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost04-bp01.html*

---

# MIDACOST05 — Balancing resources

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MIDACOST05-BP01 Implement a buffering or throttling approach

Implement balanced resource utilization that handles varying workload demands while
maintaining cost efficiency for manufacturing systems. This includes prioritizing critical
processes while queuing less time-sensitive tasks and implementing appropriate scaling
triggers aligned with production cycles.

**Desired outcome:** Balanced resource utilization that handles
varying workload demands while maintaining cost efficiency.

**Common anti-patterns:**

- Implementing throttling on time-critical manufacturing processes
- Using the same buffering strategy for all types of industrial data
- Overlooking real-time requirements of production monitoring systems
- Setting queue limits without considering production batch sizes
- Implementing aggressive throttling that impacts quality data collection
- Not accounting for upstream and downstream dependencies in manufacturing processes
- Using standard IT buffering patterns without adapting to manufacturing needs

**Benefits of establishing this best practice:**

- Controlled resource consumption
- Avoided system overload
- Optimized costs during peak periods
- Improved system stability

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Documented critical and non-critical manufacturing processes
- Peak resource utilization patterns for different production phases
- Response time requirements for various manufacturing systems

Key decisions needed:

- Resource allocation priorities for critical vs. non-critical processes
- Throttling thresholds for different types of manufacturing workloads
- Queue configurations for deferrable processes
- Scaling triggers aligned with production cycles and peaks

Implement buffering and throttling mechanisms to manage cloud resource utilization
during manufacturing peaks. Design a system that prioritizes critical processes (for
example, real-time monitoring, quality control) for immediate resource access, while queuing
less time-sensitive tasks (for example, batch analytics, report generation). Use
auto-scaling for baseline capacity but implement throttling to help prevent non-critical
tasks from consuming resources needed for production-critical operations.

Consider the following:

- Using Spot Instances for interruptible, non-critical workloads
- Implementing reserved capacity for predictable, critical processes
- Using serverless technologies for sporadic, scalable tasks

Regularly review and adjust your buffering and throttling strategies based on changing
production patterns and business needs.

### Implementation steps

- Identify and categorize manufacturing workloads:

Critical real-time processes (for example, process control, safety systems)
- Time-sensitive operations (for example, quality inspections, inventory
updates)
- Deferrable tasks (for example, long-term analytics, reporting)

- Design resource allocation strategies:

Priority-based access for critical systems
- Queueing mechanisms for non-critical operations
- Load balancing across production lines or facilities

- Implement OT-aware monitoring:

Set up real-time monitoring for critical production KPIs
- Configure alerts based on manufacturing thresholds
- Integrate with SCADA or MES for comprehensive visibility

- Establish OT-IT integrated scaling mechanisms:

Automatic scaling triggered by production volumes
- Resource reservation for planned production increases
- Gradual scale-down aligned with shift changes or maintenance windows

- Conduct regular performance and cost reviews:

Analyze resource utilization against production output
- Identify opportunities for optimization without impacting OT
- Adjust strategies based on changing manufacturing requirements

- Implement feedback loops with shop floor:

Gather input from operators on system performance
- Align IT resource adjustments with production schedules
- Continuously refine based on real-world manufacturing impact

## Key AWS services

- Amazon SQS
- Amazon Kinesis
- AWS Auto Scaling
- Amazon API Gateway

## Resources

**Related documents:**

- [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [Amazon Kinesis Data Streams Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)
- [Throttle requests to your REST APIs for better throughput in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp01.html*

---

# MIDACOST05-BP02 Implement dynamic resource provisioning

Enable automated resource scaling that matches manufacturing workload demands while
optimizing costs. This includes implementing warm pools for faster scaling, considering
application warm-up times, and aligning scaling policies with production schedules and peak
processing times.

**Desired outcome:** Automated resource scaling that matches
manufacturing workload demands while optimizing costs.

**Common anti-patterns:**

- Implementing automatic scaling without considering production schedule requirements
- Setting scaling thresholds without consulting manufacturing operations teams
- Using the same scaling policies for both production and non-production workloads
- Neglecting warm-up times for manufacturing applications when scaling
- Implementing aggressive scale-in policies that could impact production monitoring
- Not accounting for data retention requirements when scaling storage resources
- Ignoring the impact of scaling on integrated manufacturing systems
- Setting up dynamic provisioning without consideration for compliance requirements

**Benefits of establishing this best practice:**

- Optimized resource utilization
- Reduced manual intervention
- Cost-efficient scaling
- Improved responsiveness

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- Detailed production schedules and patterns
- Peak resource usage data by workload type
- System warm-up and response time requirements

Key decisions needed:

- Scaling thresholds for different manufacturing workloads
- Resource retention periods based on production needs
- Performance impact limits for critical systems
- Cost optimization targets by workload type

Design your manufacturing workloads to automatically adjust resource provisioning
based on current demand and production schedules. Implement a data-driven approach that
correlates IT resource needs with manufacturing operations, providing appropriate safeguards
for critical production systems and consideration for startup times and warm pools.

### Implementation steps

- Define scaling metrics:

Production demand indicators
- Resource utilization thresholds
- Cost constraints

- Configure auto scaling policies:

Scale-out conditions
- Scale-in conditions
- Cool-down periods

- Implement monitoring.
- Set up cost tracking.
- Perform regular policy review and optimization.

## Key AWS services

- AWS Auto Scaling
- Amazon EC2 Auto Scaling
- AWS Lambda
- Amazon CloudWatch

## Resources

**Related documents:**

- [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html)
- [Amazon EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [AWS Lambda: Configuring reserved concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html)
- [AWS Lambda: Configuring provisioned concurrency for a function PDF RSS](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [Amazon CloudWatch: Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost05-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
