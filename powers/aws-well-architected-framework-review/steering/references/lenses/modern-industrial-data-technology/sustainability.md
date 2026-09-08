# Sustainability

**Pillar**: Sustainability  
**Questions**: 6

---

# MIDASUS01 — Region selection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS01-BP01 Select Regions that offer services required by Manufacturing organizations that maximizes the reduction of your carbon footprint

Choose Regions with lower carbon footprint for your manufacturing workloads while meeting
technical, compliance, and performance requirements.

**Desired outcome:** Manufacturing workloads deployed in regions that minimize carbon footprint while
maintaining operational excellence, compliance requirements, and optimizing for latency to
manufacturing facilities.

**Benefits of establishing this best practice:**

- Reduced environmental impact and energy costs for manufacturing IT operations.
- Enhanced sustainability reporting for regulatory compliance and improved brand
reputation.
- Strategic alignment with carbon reduction goals prepares the organization for
evolving environmental regulations in manufacturing.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Select cloud regions with lower carbon footprint that also satisfy your
manufacturing compliance requirements, data sovereignty needs, and performance
thresholds.
- Deploy manufacturing workloads on energy-efficient computing systems within these
sustainable regions to maximize environmental benefits.
- Configure automatic scaling policies that align with manufacturing production
patterns to verify that computing resources are only active when needed.
- Implement edge processing at manufacturing facilities to reduce data transfer
volumes between factories and cloud regions.
- Use efficient data transfer mechanisms and compression techniques when moving
manufacturing data between regions to minimize network impact.
- Consider hybrid deployment models for manufacturing workloads that must remain
geographically close to production facilities while still benefiting from cloud
sustainability features.

### Implementation steps

- **Carbon footprint assessment:**

Conduct an environmental impact assessment of your current manufacturing
workload deployment using the AWS Customer Carbon Footprint Tool
- Map manufacturing compliance and technical requirements against available
lower-carbon regions
- Create a phased migration plan for manufacturing workloads to greener
regions, prioritizing non-critical applications first

- **Deploy energy-efficient computing:**

Deploy EC2 Graviton instances with Auto Scaling configurations that align
with production schedules and peak processing times
- Configure Amazon EC2 Auto Scaling groups based on manufacturing production
patterns

- **Optimize edge processing:**

Implement AWS IoT Greengrass at manufacturing facilities to optimize edge
processing and reduce unnecessary data transfers
- Configure IoT rules to filter and aggregate manufacturing data at the edge
- Set up AWS DataSync for efficient transfer of required manufacturing data
between regions

- **Implement hybrid solutions:**

Deploy AWS Outposts or AWS Local Zones for manufacturing workloads requiring
low-latency access to production facilities
- Configure AWS Direct Connect for high-throughput, low-latency connectivity
between manufacturing sites and sustainable regions
- Implement Amazon S3 Transfer Acceleration for optimized cross-regional data
movement when required

- **Establish monitoring and governance:**

Create Amazon CloudWatch dashboards to track resource utilization and carbon
metrics across regions
- Establish sustainability KPIs and monitoring dashboards to track carbon
reduction progress
- Implement quarterly reviews to reassess regional deployment decisions based
on sustainability performance metrics

- **Continuous optimization:**

Use AWS Cost Explorer and Sustainability reports to identify further
optimization opportunities
- Regularly review and update regional deployment strategy as cloud provider
sustainability features evolve

## Key AWS services

- AWS Customer Carbon Footprint Tool
- Amazon EC2 Auto Scaling
- AWS Graviton
- AWS DataSync
- AWS IoT Greengrass
- AWS Outposts
- Amazon CloudWatch
- AWS Cost Explorer
- AWS Direct Connect
- AWS Local Zones

## Resources

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/)
- [Get started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)
- [AWS DataSync](https://aws.amazon.com/datasync/)
- [AWS Outposts Gives Manufacturers the Power of AWS On Premises](https://d1.awsstatic.com/Solutions/Outposts%20Manufacturing%20Solution%20Brief%20US%20Letter%20AWS%2009.30.20%20FINAL.pdf)
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus01-bp01.html*

---

# MIDASUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS02-BP01 Actively manage workloads and resource allocation based on production demands

Identify critical and non-critical manufacturing systems, then align computing resources
with actual production schedules and operational requirements to reduce waste while providing
reliability for the essential manufacturing systems.

**Desired outcome:** Cloud resources that efficiently scale with manufacturing operations, prioritizing
time-sensitive shop floor systems while optimizing resource usage for enterprise applications,
resulting in reduced energy consumption, lower costs, and improved environmental
sustainability.

**Benefits of establishing this best practice:**

- Reduced energy consumption and carbon footprint by removing over provisioning of
resources.
- Lower operational costs while maintaining reliability for the production systems.
- Enhanced sustainability reporting metrics with quantifiable improvements in cloud
resource efficiency aligned with manufacturing operations.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Analyze production schedules and system criticality to categorize manufacturing
applications as time-critical (shop floor control, real-time monitoring) and
non-time-critical (reporting functions, data processing) using workload assessment
tools.
- Implement auto scaling mechanisms for all manufacturing systems based on their
specific demand patterns, verifying that enterprise planning and design systems maintain
necessary availability while optimizing resource allocation.
- Use batch processing systems for scheduling background data processing jobs
like quality analysis, production reporting, and maintenance analytics during periods of
lower resource demand.
- Deploy high performance computing (HPC) solutions and run resource-intensive
engineering workloads such as computational fluid dynamics (CFD) and computer aided
engineering (CAE) simulations during off-peak production hours to optimize resource
utilization.

### Implementation steps

- **Assessment and classification:**

Conduct workload assessment of manufacturing applications using AWS Well-Architected Tool
- Document peak usage patterns using Amazon CloudWatch
- Classify applications into real time and batch processing categories

- **Demand pattern mapping:**

Create demand heat maps using Amazon CloudWatch metrics
- Identify off-peak windows for non-time-critical workloads

- **Resource optimization configuration:**

Configure AWS Auto Scaling policies with appropriate thresholds
- Implement scaling plans that align with production schedules
- Define resource constraints to help prevent over-provisioning

- **Workload scheduling implementation:**

Create AWS Batch job configurations for non-critical processing tasks
- Configure AWS ParallelCluster for engineering simulations during off-hours
- Implement prioritization logic for computing resources

- **Monitoring and continuous improvement:**

Deploy CloudWatch dashboards to track resource utilization efficiency
- Establish KPIs using AWS Cost and Usage Reports
- Create sustainability improvement reporting and quarterly review process

## Key AWS services

- AWS Auto Scaling
- Amazon EC2
- AWS Batch
- AWS ParallelCluster
- Amazon CloudWatch
- AWS Cost and Usage Reports

## Resources

- [Step and simple scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html)
- [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
- [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html)
- [Amazon EC2 instance
types](https://aws.amazon.com/ec2/instance-types/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus02-bp01..html*

---

# MIDASUS03 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS03-BP01 Implement edge data and cross-region movement strategies

Implement strategies that process information at the edge when possible and strategically
manage cross-Region transfers in manufacturing environments. This approach reduces unnecessary
network traffic, lowers energy consumption, and improves operational efficiency in factory
environments.

**Desired outcome:** Reduced data transfer across networks, optimized energy usage, faster access to
manufacturing data, and improved application performance with lower carbon impact.

**Benefits of establishing this best practice:**

- Decreased network bandwidth consumption and associated energy usage
- Reduced carbon footprint from data centers and networking equipment
- Lower latency for manufacturing applications requiring real-time data
- Cost savings from reduced data transfer fees

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Process data at the source or edge locations to filter, compress, or aggregate data
before transmitting to centralized storage, reducing unnecessary data movement and
processing requirements.
- Implement efficient data transfer mechanisms when cross-region or cross-zone data
movement is necessary, using compression, batching, and optimized transfer strategies.
- Store data in locations geographically closest to where it will be processed and
accessed most frequently to minimize network latency and reduce energy consumed during
data transit.
- Apply data lifecycle management strategies to automatically tier, archive, or
delete data based on access patterns, compliance requirements, and business value,
reducing storage footprint and associated energy costs.

### Implementation steps

- **Edge processing implementation:**

Deploy AWS IoT Greengrass to process sensor data locally at the edge
- Configure data filtering rules to send only aggregated results to the cloud
- Set up Lambda functions for edge-based data processing and reduction

- **Efficient data transfer configuration:**

Implement Amazon S3 Transfer Acceleration and AWS Global Accelerator for
cross-region data movement
- Use Amazon CloudFront to cache frequently accessed data closer to end users

- **Geographic data optimization:**

Store data in AWS Regions closest to production facilities
- Configure Amazon S3 lifecycle policies for efficient data management
- Monitor data access patterns using CloudWatch to identify optimization
opportunities

## Key AWS services

- AWS IoT Greengrass
- Amazon S3 Transfer Acceleration
- AWS Global Accelerator
- Amazon CloudFront

## Resources

- [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html)
- [Configuring fast, secure file transfers using Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)
- [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
- [AWS for the Edge](https://aws.amazon.com/edge/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus03-bp01..html*

---

# MIDASUS04 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS04-BP01 Design backup strategies that focus on critical data

Manufacturing data varies in criticality from essential production recipes and regulatory
compliance records to temporary operational logs. Design backup strategies that prioritize
truly valuable data while minimizing resource consumption.

**Desired outcome:** A data backup system that balances business continuity needs with sustainability goals,
reducing storage requirements, energy consumption, and carbon footprint while maintaining
manufacturing operational resilience.

**Benefits of establishing this best practice:**

- Reduced storage costs and energy consumption
- Lower carbon footprint from decreased data center resources
- Optimized network bandwidth usage
- Improved recovery time for truly critical manufacturing data

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Categorize data by importance (critical production recipes, compliance records,
operational logs) to determine appropriate backup strategies for each category.
- Establish tiered backup strategies based on data importance, with more frequent and
comprehensive backups for critical data while implementing less resource intensive
approaches for lower priority data.
- Implement data compression, deduplication, and efficient formats to minimize
storage footprint and processing requirements for backups across the data categories.
- Store manufacturing data in AWS Regions closest to production facilities to reduce
energy used for data transfer and improve access speeds for operational systems.

### Implementation steps

- **Data classification and assessment:**

Conduct comprehensive data audits across Amazon EBS volumes, Amazon EFS file
systems, and on-premises data connected through AWS Storage Gateway
- Document recovery time objectives (RTOs) and recovery point objectives (RPOs)
for each data category in AWS Backup

- **Tiered backup strategy design:**

Configure AWS Backup plans with different frequencies for critical EBS
volumes, EFS file systems, and Storage Gateway volumes
- Implement lifecycle policies in Amazon S3 to automatically transition
infrequently accessed backups to cold storage classes

- **Storage optimization configuration:**

Enable compression and deduplication features in AWS Backup for EBS snapshots
and EFS backups
- Configure Amazon EFS Infrequent Access storage class for rarely accessed file
data
- Implement AWS Storage Gateway with deduplication enabled to reduce backup
data footprint

- **Geographic distribution setup:**

Deploy EBS and EFS backups to AWS Regions closest to primary usage locations
- Configure AWS Storage Gateway to cache frequently accessed data locally while
storing backups in energy-efficient regions

- **Performance monitoring:**

Create CloudWatch dashboards to track backup storage utilization across EBS,
EFS, and Storage Gateway
- Establish quarterly review processes using AWS Trusted Advisor storage
recommendations

## Key AWS services

- AWS Backup
- Amazon S3
- Amazon Glacier
- Amazon EBS
- Amazon EFS
- AWS Storage Gateway
- Amazon CloudWatch
- AWS Trusted Advisor

## Resources

- [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Amazon Simple Storage Service: Managing the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Cloud Storage on AWS](https://aws.amazon.com/storage/)
- [Optimize
Siemens Teamcenter with Amazon FSx for NetApp ONTAP](https://d1.awsstatic.com/fsx/FSxONTAP-whitepaper-PLM.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus04-bp01..html*

---

# MIDASUS05 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS05-BP01 Implement optimized compute, storage and networking hardware

Manufacturing workloads have diverse requirements - from compute intensive simulations,
storage to real time shop floor systems. Choosing the right hardware architecture and service
models helps minimize environmental impact while meeting manufacturing performance
demands.

**Desired outcome:** Manufacturing workloads running on optimally sized and energy-efficient infrastructure
that minimizes waste and carbon footprint while meeting performance requirements for critical
operations, resulting in quantifiable sustainability improvements without compromising
production reliability.

**Benefits of establishing this best practice:**

- Reduced energy consumption and carbon emissions through removal of over provisioning
and inefficient hardware choices.
- Lower operational costs through optimized resource utilization.
- Improved sustainability reporting metrics that demonstrate concrete steps toward
environmental goals without sacrificing manufacturing performance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Analyze hardware requirements for manufacturing workloads including PLM (Product
Lifecycle Management), MES (Manufacturing Execution Systems), and ERP (Enterprise
Resource Planning) applications based on vendor specifications and performance needs,
selecting minimal resources necessary to meet functional requirements.

Implement right sizing strategies for all compute resources supporting
manufacturing operations, verifying that production systems use the most efficient
configurations based on actual workload demands rather than over-provisioned
specifications.

Deploy storage tiering mechanisms to align manufacturing data accessibility
requirements with appropriate storage technologies, moving infrequently accessed
historical production data to more energy efficient storage options.

Use hardware sharing approaches where possible across manufacturing systems to
increase utilization rates of deployed resources, improving efficiency through
consolidated infrastructure and reducing the total environmental footprint.

### Implementation steps

**Manufacturing application resource assessment:**

- Conduct workload profiling of PLM, MES, and ERP systems using AWS Compute Optimizer to identify optimization opportunities
- Implement instance rightsizing recommendations, prioritizing Graviton based instances for better performance and efficiency

**Business application resource scheduling:**

- Configure Amazon EC2 Auto Scaling with scheduled actions aligned to manufacturing business hours and usage patterns
- Implement hibernation policies for non-production environments during off-hours to reduce idle resource consumption

**Manufacturing data storage tiering:**

- Configure Amazon S3 Lifecycle policies to automatically transition production data to appropriate storage classes based on access patterns
- Implement intelligent tiering for files, documentation, and historical manufacturing data to optimize storage costs and efficiency

**Engineering workload optimization:**

- Deploy AWS Batch for compute-intensive manufacturing simulations with job queuing that maximizes resource utilization
- Deploy AWS ParallelCluster for high performance computing needs like CFD, FEA, and engineering simulations

**Edge computing optimization:**

- Deploy AWS IoT Greengrass for local processing of shop floor data to minimize unnecessary data transfer

## Key AWS services

- AWS Compute Optimizer
- AWS Graviton processors
- AWS IoT Greengrass
- AWS Batch
- AWS ParallelCluster
- Amazon EC2 Auto Scaling
- Amazon S3

## Resources

- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)
- [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/)
- [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)
- [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
- [High-Performance Computing with AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus05-bp01..html*

---

# MIDASUS06 — Process and culture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS06-BP01 Implement sustainability driven manufacturing processes

Building a sustainability focused culture in manufacturing environments helps drive
energy efficiency from the shop floor to enterprise systems. By aligning sustainability goals
with operational excellence initiatives, organizations can reduce environmental impact while
improving manufacturing performance.

**Desired outcome:** Measurably reduced environmental impact across manufacturing operations through
systematized processes that track sustainability metrics, optimize resource usage, and
continuously improve efficiency. Manufacturing teams at all levels actively participate in
sustainability initiatives as part of standard operating procedures rather than as separate
efforts.

**Benefits of establishing this best practice:**

- Holistic approach to sustainability that drives long term behavioral change rather
than isolated initiatives.
- Improved cross functional collaboration as sustainability becomes a shared
organizational value.
- Enhanced employee engagement through meaningful participation in environmental
stewardship aligned with organizational purpose.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Incorporate sustainability KPIs into existing manufacturing performance dashboards,
creating visibility of environmental impact alongside traditional metrics to drive a
culture of sustainable operations.

Establish systematic tracking and reporting of resource utilization across
manufacturing systems, enabling teams to identify inefficiencies and prioritize
improvements that reduce environmental impact.

Apply advanced analytics and predictive modeling to identify process optimization
opportunities that balance production objectives with sustainability goals.

Implement financial accountability mechanisms that link resource consumption to
costs, encouraging more efficient practices and sustainability-minded decision making
throughout operations.

### Implementation steps

**Sustainability dashboard integration:**

- Implement manufacturing dashboards using Quick that combine traditional metrics (OEE, quality, throughput) with sustainability KPIs

**Resource utilization tracking:**

- Deploy AWS Systems Manager to monitor resource consumption and maintain efficient software versions
- Create automated reports using Quick to highlight opportunities for improved resource efficiency across manufacturing systems

**Predictive process optimization:**

- Utilize Amazon SageMaker AI to develop models that identify process improvements that reduce resource consumption
- Implement data pipelines using AWS Glue to make manufacturing data available for sustainability analysis

**Financial accountability framework:**

- Configure AWS Cost Explorer with sustainability focused tags to track resource usage against production output
- Implement AWS Budgets to set sustainability targets and alert teams when consumption thresholds are approached

## Key AWS services

- Quick
- AWS Systems Manager
- Amazon SageMaker AI
- AWS Cost Explorer
- AWS Budgets
- AWS Resource Groups & Tag Editor

## Resources

- [Quick: Publishing dashboards](https://docs.aws.amazon.com/quicksight/latest/user/creating-a-dashboard.html)
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus06-bp01..html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
