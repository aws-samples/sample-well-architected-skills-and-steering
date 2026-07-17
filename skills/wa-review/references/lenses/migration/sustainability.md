# Sustainability

**Pages**: 3

---

# Assess

By migrating to AWS, customers can benefit from our investments in
renewable energy and economy-of-scale to run their workloads with
lower carbon emissions. As part of the assess phase, you can
calculate the expected carbon emission reductions when migrating
to AWS by comparing estimated annual carbon emissions for a
customer's current on-premises infrastructure with corresponding
carbon emissions of right-sized workloads in AWS. This phase also
enables you to identify sustainability related key performance
indicators (KPIs) to align key stakeholders.

MIG-SUS-01: Is sustainability a consideration for creating your migration business case?

Sustainability is increasingly becoming a motivator to migrate
to the cloud. By migrating to AWS, customers can benefit from
our investments in renewable energy and economy-of-scale to run
their workloads with lower carbon emissions. The migration
business case should demonstrate the carbon emission reductions
customers can expect when migrating to AWS.

## MIG-SUS-BP-1.1: Include sustainability considerations as part of your migration business case and preliminary assessments

This BP applies to the following best practice areas: Process and culture

A complete migration business case includes the following business impact areas: cost savings, staff productivity, operational resilience, business agility, and sustainability considerations and goals. Sustainability should be included in the business case and aligned with organizational goals.

### Implementation guidance

**Suggestion 1.1.1:** Identify a migration stakeholder to own sustainability goals.

A single-threaded owner is required to identify and align sustainability goals to overall migration goals. The owner also owns the sustainability portion of the business case for migration. The owner is responsible for capturing sustainability-relevant data before, during, and after the migration.

**Suggestion 1.1.2:** Include sustainability impact in the business case along with TCO and return on investment (ROI) calculations.

Sustainability impact should be included in the final business case for the migration. Alignment with organizational sustainability goals can be showcase here. You can use tools such as [AWS Migration Evaluator](https://aws.amazon.com/migration-evaluator/) to highlight estimated carbon emission reductions when migrating to AWS with right-sized workloads.

MIG-SUS-02: Does your migration strategy include assessing an AWS Region to meet business and sustainability goals?

An important decision that needs to be made prior to migrating
to AWS is the Region you select to deploy and migrate your
workloads. This choice significantly affects KPIs, including
latency, cost, and carbon footprint. To effectively improve
these KPIs, you should choose Regions for your workloads based
on both business requirements and sustainability goals.

## MIG-SUS-BP-2.1: Choose a Region for the workloads you plan to migrate based on your business requirements and your sustainability goals

This BP applies to the following best practice areas: Region selection

It can be challenging to select the optimal Region for a workload to migrate. This decision must be made carefully, as it has an impact on compliance, cost, performance, services available for your workloads, and sustainability goals.

### Implementation guidance

**Suggestion 2.1.1:** Shortlist potential Regions for your workloads based on your business requirements.

If your workload contains data that is bound by local regulations, shortlist Regions that comply with those regulations. This applies to workloads that are bound by data residency laws, where choosing an AWS Region located in that country is mandatory.

There are four key business factors to consider when evaluating and shortlisting each AWS Region for a workload: compliance, latency, cost, and services and features. Evaluating all these factors can make coming to a decision complicated. [Try to shortlist potential Regions based on these KPIs](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/).

**Suggestion 2.1.2:** Select Regions to support your sustainability goals as part of your migration strategy.

After shortlisting the potential Regions, the next step is to choose Regions near Amazon renewable energy projects, or Regions where the grid has a lower published carbon intensity.

For more detail, see the following:

- [How to select a Region for your workload based on sustainability goals.](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/)
- [Renewable Energy Methodology](https://sustainability.aboutamazon.com/amazon-renewable-energy-methodology)
- [Understanding your carbon emission estimations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ccft-estimation.html)
- [Video - Architecting sustainably and reducing your AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/assess-sus.html*

---

# Mobilize

The next step in preparing your workforce and resources to migrate
your enterprise at scale is to break down the
[mobilize
activities](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/mobilize-phase.html) into different workstreams. Although
the goal of the mobilize phase is the migration of business
applications, most prescriptive guidance and answers on achieving
your sustainability goals are found here.

MIG-SUS-03: How do you define and optimize cloud resources during migration so that you become more energy efficient by minimizing idle resources?

As a part of your migration planning, one of the important tasks
is to define the key workload performance matrix based on your
assessment. This plays the significant part in deciding how you
would like to migrate the target workload, instead of
replicating as-is on-premises configuration. Optimizing cloud
resources by removing idle resources helps lower carbon
emissions without compromising business requirements.

## MIG-SUS-BP-3.1: Focus on efficiency across all aspects of infrastructure

For example, during migration, verify that you use only the required resources, instead of trying to match with source on-premises capacity.

This BP applies to the following best practice areas: Alignment to demand

### Implementation guidance

**Suggestion 3.1.1:** Review the on-premises capacity to plan the workload requirements for your target environment.

During migration assessment, define the workload performance metrics for client requests. To optimize cloud resources, take advantage of elasticity in the cloud so you can meet the increasing demand of the migrating workload.

As part of your assessment, review and analyze the following:

- How to respond to the overall demand, rate of change,
and required response time, which could potentially help
to minimize the environmental impact. Implement dynamic
scaling and automation practice aligning to your SLAs to
remove excess capacity and assign only needed capacity.
- Identify redundancy, underutilization, and potential
decommission targets, and plan how you can consolidate
the redundant content, scale down underutilized
resources, and decommission unused assets.

**Suggestion 3.1.2:** Use proven workflow templates to migrate enterprise applications.

The way you plan your migration can help you identify the automation opportunity to improve the efficiency during migration process. For example:

- You can use
[Migration
Hub Orchestrator](https://docs.aws.amazon.com/migrationhub/latest/ug/gs-orchestrator.html) templates to create a
migration workflow that can be customized to fit your
unique migration requirements, instead of manually
performing all the tasks.
- You can leverage services like
[AWS Control Tower](https://aws.amazon.com/controltower/) to get started. Control
Tower helps you set up a multi-account environment and
automate the creation of AWS accounts with built-in
governance.

**Suggestion 3.1.3:** Evaluate your migrated workload to consider and configure auto scaling mechanism.

AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance. Define the [metrics](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html) that have the most relevance to your application's performance to meet changes in demand, and ensure that workloads can scale down quickly and easily during periods of low user load.

**Suggestion 3.1.4:** Define and update service-level agreements (SLAs).

- Review and optimize your workload service-level
agreements (SLA) based on your sustainability goals to
minimize the resources required to support your
workload, while continuing to meet business needs.
Consider your SLA requirements as part of your design
and architecture as well.
- Define and update SLAs of the migrating workload, such
as:

Availability
or data retention periods, to minimize the number of
resources required to support your

workload.
For more detail, see

[SUS02-BP02 Align SLAs with sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html)
- Power off the workload during non-functional period.
You can use
[Instance
Scheduler on AWS](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/schedules.html) to do this, which automates
the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances.
- Identify if use of a messaging component can lead to
relaxed service-level requirements that can be met
with fewer resources. Employ batching requests,
where possible, for optimal use of resources. For
more detail, see
[SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html).

For more detail, see the following:

- [Throttle API requests for better throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [Working with Service auto scaling](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)
- [AWS Summit SF 2022 - Optimizing your AWS infrastructure for sustainability](https://www.youtube.com/watch?v=9WJv2re6hlE)
- [Capacity management made easy with Amazon EC2 Auto Scaling](https://www.youtube.com/watch?v=9BlsFNBnKHc)
- [Architecting sustainably and reducing your AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8)

MIG-SUS-04: Do you consider sustainability when selecting and prioritizing applications for migration and modernization?

Have sustainability in mind when deciding which applications to
migrate and modernize. To do this, first identify metrics that
can act as a stand-in for your application's sustainability.
Then, use these metrics to initiate migration and modernization
projects that improve the application's sustainability.

## MIG-SUS-BP-4.1: Adopt metrics that can signal the sustainability of your application

This BP applies to the following best practice areas: Process and culture

Adopt metrics to understand what you have provisioned and how those resources are consumed. Evaluate potential improvements, and estimate their potential impact, the cost to implement, and the associated risks. Measure improvements over time to study trends and the impacts of any migration and modernization initiatives.

### Implementation guidance

**Suggestion 4.1.1:** Adopt [sustainability metrics](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html) relevant to the application.

Understand the resources provisioned by your application to complete a unit of work. Leverage monitoring tools to define [proxy metrics](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/), business metrics, and sustainability key performance indicators (KPI) for your workloads. Documenting sustainability impact over time, including after migration and modernization, enables iterative improvement of your application over time.

You can also add other sustainability attributes that signal the efficiency of your application. An example of this is the version of your operating systems, runtimes, middleware, libraries, and applications. Keeping your workloads up-to-date can improve workload efficiency, and capturing this information keeps stakeholder informed. Another example of this is an indicator to note if you are using Graviton-based instances improve the performance efficiency of your application. For more detail, see [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html).

For more detail, see

[Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/).

**Suggestion 4.1.2:** Introduce organizational dashboards to share sustainability metrics with stakeholders.

Leverage automation to report, visualize, and enforce sustainability metrics for your application. Introduce organizational dashboards for sustainability that can be shared with application owners and other stakeholders, including key organizational functions such as a Cloud Center of Excellence (CCoE) and Application Review Board (ARB). Make sustainability metrics a part of your architectural decisions.

## MIG-SUS-BP-4.2: Include sustainability metrics in the application portfolio analysis to drive migration and modernization initiatives

This BP applies to the following best practice areas: Process and culture

Include sustainability metrics when scoping and prioritizing applications for migrations. Sustainability may be excluded if alignment from migration goals and organizational goals is missing.

### Implementation guidance

**Suggestion 4.2.1:** Include sustainability metrics in the application portfolio analysis.

Establish a [sustainability improvement process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html) and adopt methods that can rapidly [introduce sustainability improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a2.html) and [keep your workloads up-to-date](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a3.html).

Including sustainability metrics in the application portfolio analysis assures that relevant data is captured early and is included in architecture and implementation considerations. These metrics capture the business and technical value of retiring applications, and prioritize rightsizing and application scaling to meet infrequent demand.

MIG-SUS-05: How do you implement efficient workload design to support your sustainability goals?

Compute and storage services make up the foundation of many
customers, which brings great potential for workload design
consideration that can improve the energy efficiency of the
migrating workload.

## MIG-SUS-BP-5.1: Implement efficient workload design by leveraging the underlying infrastructure.

For example, right-size the workload for the target state before migrating to minimize idle resources, and to avoid over provisioned capacity.
This BP applies to the following best practice areas: Hardware and services

### Implementation guidance

**Suggestion 5.1.1:** Select the most efficient hardware and services for your workload migration.

Amazon EC2 provides a wide selection of [instance types](https://aws.amazon.com/ec2/instance-types/) optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the [appropriate mix of resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a3.html) for your applications. For example, Graviton3 provides up to 60% less energy for the same performance as non-Graviton EC2 instances.

**Suggestion 5.1.2:** Gain insight into workload performance.

Gain insight into workload performance metrics like CPU utilization, memory utilization, network utilization, and disk and usage patterns to perform the right alignment of the cloud resource.

- Key matrices to consider are the following:

If the workload is idle for a long time, it's a good
sign to investigate if this workload can retire
instead of migrating it.
- Understand your average CPU and memory utilization,
and identify resources that are underutilized.
Rightsize those instances to reduce your carbon
footprint.
- Identify the network and storage performance, such
as I/OPS, and size for the target workload. Analyze
the overall demand, rate of change, and required
response time to rightsize the throttle or buffer
required.
- For fault-tolerant, flexible, and stateless
workloads that can trade-off with minimal
interruption, adopt Spot Instances in your design.
- Evaluate your migrated workload continually using
AWS Compute Optimizer and
[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), and proactively
make rightsizing adjustments on your workload.

**Suggestion 5.1.3:** Consider managed services in your workload design.

Remove the need for you to run and maintain physical servers, as AWS operates at scale and is responsible for their efficient operation. For example, instead of migrating your virtual machine or container to Amazon ECS running on Amazon EC2, consider using a service like Amazon Fargate, where you can run containers without having to manage the servers, or package and deploy Lambda functions as container images.

Containerize and migrate existing applications using , for migrating and modernizing Java and .NET web applications into container format. Use [managed services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html) to operate more efficiently in the cloud.

**Suggestion
5.1.4:** Configure your
[instance
tenancy](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-dedicated-instances.html), which defines how EC2 instances are
distributed across physical hardware.

Tenancy provides the opportunity to further optimize the
workload. Migrating to shared instances instead of migrating
to dedicated underutilized instances or hosts can be more
beneficial when working towards the sustainability goal.

For more detail, see the following:

- [Right Size Before Migrating](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/right-size-before-migrating.html)
- [Getting started with Graviton](https://aws.amazon.com/ec2/graviton/getting-started/)
- [Streamline selection and right size EC2 with AWS Compute Optimizer](https://www.youtube.com/watch?v=flhuwVwYomg)
- [Effortless migration - Is your app already Graviton-ready?](https://www.youtube.com/watch?v=aa_FjqYCJpY)
- [Design patterns for success in serverless microservices](https://www.youtube.com/watch?v=ReRB_xEtEjY)
- [Lift and shift a web application to serverless](https://www.youtube.com/watch?v=O-hSs7aF7JE)

MIG-SUS-06: How do you take advantage of software and architecture patterns for workloads you are going to migrate to support your sustainability goals?

Software and architecture patterns can be used to influence
utilization of resources while migrating workloads. The aim is
to use patterns that maximize utilization so that resources
consumed for the workloads are minimized. Idling of resources
due to user behavior or nature of workload can also be minimized
by applying appropriate software and architecture patterns.
on-premises workloads are not designed to take advantage of AWS
cloud features that can optimize utilization of resources, like
autoscaling. These workloads can have multiple instances of
software or services running at multiple locations or are
overprovisioned all the time to cater to peak demand. Some
workloads are running all the time, even when not in use. Using
the 7 Rs can optimize resource usage. Adopt patterns and
architecture to consolidate underutilized components to increase
overall utilization. Retire components that are no longer
required.

## MIG-SUS-BP-6.1: Identify environments and workloads that can be consolidated or retired

****
This BP applies to the following best practice areas: Software and architecture

### Implementation guidance

**Suggestion 6.1.1:** Consolidate environments and workloads in the AWS Cloud.

When moving workloads from multiple on-premises environments or in merger and acquisition cases, consolidating environments on AWS leads to optimal usage of resources and eliminates duplicate functionality. Identify workloads during the assess stage that can be eliminated or consolidated. Identify multiple instances of services or applications running at multiple locations on-premises.

Retire workloads that are not used. Use automated tools such as [Migration Evaluator](https://aws.amazon.com/migration-evaluator/) to identify workloads that are not being used.

## MIG-SUS-BP-6.2: Identify workloads that can use efficient software and architecture patterns to maintain consistent high utilization of deployed resources

This BP applies to the following best practice areas: Software
and architecture

### Implementation guidance

**Suggestion 6.2.1:** Optimize software and architecture for asynchronous and scheduled jobs.

Identify applications and workloads that can benefit from software and architecture patterns to maintain consistently-high utilization of deployed resources while migrating applications.

While migrating applications, evaluate use of integration patterns to scale the processing independently of the receiving of messages, which reduces resource utilization. Identify if use of a messaging component can lead to relaxed service level requirements that can be met with fewer resources. Employ batching requests where possible for optimal use of resources, as batching provides consistent usage. Scheduling the batch jobs reduces idle time for resources. For detail, see [SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html).

## MIG-SUS-BP-6.3: Analyze your data access patterns and data lifecycle processes, and evaluate how you can become more efficient and sustainable in your data management

****This BP applies to the following best practice areas: Software and architecture

### Implementation guidance

Storing and accessing data efficiently, in addition to reducing idle storage resources, results in a more efficient and sustainable architecture. When migrating data, understand how data is used within your workload, consumed by your users, transferred, and stored. Use software patterns and architectures that best support data access and storage to minimize the compute, networking, and storage resources required to support the workload.

**Suggestion 6.3.1:** Define and implement a data lifecycle process for data in your object store.

Design a data lifecycle management process based on your data access patterns, observed in your on-premises facility. That process either removes data that is no longer required or archives data into less resource-intensive storage. While migrating data, implement a data lifecycle policy. For more detail, see [Best practice 15.4 – Implement data retention processes to remove redundant data from your analytics environment](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.4-implement-data-retention-processes-to-remove-redundant-data-from-your-analytics-environment..html).

**Suggestion 6.3.2:** Evaluate use of columnar data formats and compression.

While migrating data, evaluate if columnar data formats like Parquet and ORC can be used. These formats [require less storage capacity](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/) compared to row-based formats like CSV and JSON.

- Parquet consumes up to
[six
times](https://docs.aws.amazon.com/redshift/latest/dg/r_UNLOAD.html) less storage in Amazon S3
compared to text formats. This is because of features
such as
[column-wise
compression, different encodings, or compression based
on data type](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/).
- You can improve performance and reduce query costs of
[Amazon Athena](https://aws.amazon.com/athena/) by

[30–90
percent](https://aws.amazon.com/athena/faqs/) by compressing, partitioning,
and converting your data into columnar formats. Using
columnar data formats and compressions reduces the
amount of data scanned.

## MIG-SUS-BP-6.4: Understand and influence business requirements, and optimize areas of code to reach your sustainability goals

****This BP applies to the following best practice areas: Software and architecture

Understanding your sustainability goals is the first step to focusing on the factors needed to meet those goals. Defining such criteria involves adopting metrics that can be used to measure and evaluate your current sustainability posture, report progress against goals, and accelerate improvements. By analyzing the current environmental impact of the underlying cloud-based infrastructure, you can quantify the tradeoffs and changes required to meet your sustainability objectives.

### Implementation guidance

**Suggestion 6.4.1:** Define criteria to measure and understand your sustainability impact after your migration.

Post-migration, you can use sustainability proxy metrics for your monitoring scenarios. [Proxy metrics](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/) allow architecture teams to evaluate correlated improvements made to a workload instead of real-time carbon metrics. Defining proxy metrics across compute, storage, and network infrastructure can help you understand how infrastructure changes can impact sustainability results.

Example proxy metrics include vCPU minutes for compute, GBs provisioned for storage, and GBs transferred for network traffic. Proxy metrics combined with business metrics can define sustainability KPIs, which can be used to drive sustainability optimizations while keeping business needs in focus. One example would be to measure vCPU minutes per transaction and define an improvement goal to minimize this metric. Business stakeholders would have to weigh the cost, as reducing vCPUs could ultimately become detrimental to delivering on business needs. When running workloads in AWS, the change in these measured resources correlates with a similar change in cost (except as noted in the following), making overall infrastructure spend a useful proxy metric.

By agreeing on a set of sustainability metrics, the architect team can evaluate different technical approaches to reduce environmental impact.

For more detail, see the following:

- [Cloud sustainability](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/cloud-sustainability.html)
- [Evaluate specific improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html)
- [Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/)
- [Best Practices from IBM and AWS for Optimizing SaaS Solutions for Sustainability](https://aws.amazon.com/blogs/apn/best-practices-from-ibm-and-aws-for-optimizing-saas-solutions-for-sustainability/)
- [re:Invent 2022: Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)

**Suggestion
6.4.2:** Consider using
[Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/) to reduce your cloud costs, improve
your application performance, and

[reduce
your carbon emissions](https://aws.amazon.com/blogs/compute/building-sustainable-efficient-and-cost-optimized-applications-on-aws/) attributable to your workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/mobilize-sus.html*

---

# Migrate

In the migrate phase, we ensure the migration proceeds as planned,
monitor the migration process, and have a plan in place to
rollback in case any issue encountered during the migration.
During migration, you can scale your resources corresponding to
the volume of data to be migrated. Furthermore, you can adopt best
practices that can reduce interim resource consumption during your
migration.

MIG-SUS-07: Does your on-premises to AWS data migration strategy consider sustainability?

Data makes up the large portion of the scope of many workload
migrations. Identifying and optimizing the data storage with
latest technologies helps improve the power efficiency and
reduce carbon footprint.

## MIG-SUS-BP-7.1: Implement data management practices

This BP applies to the following best practice areas: Data

Data management is a continuous process and should be implemented during and after the migration. With the latest storage technologies, it provides the opportunity to configure and provision sufficient storage without compromising the business needs.

### Implementation guidance

**Suggestion 7.1.1**: Avoid
over-provisioning for storage system to influence your
environmental impact.

- Perform application discovery to identify data
characteristics and access patterns that can be
supported by storage technology.
- You can use shared file systems or storage that allows
for sharing data to one or more consumers without having
to copy the data. For example, you can have a shared
drive to store common files instead of copying those
common files to each VM.
- After migrating the workload, from time to time, analyze
data access and date movement to identify opportunities
to become more efficient. When opportunities are found,
change the lifecycle by moving to other storage classes
or deleting unneeded data.
- Use technologies that support data access and storage
patterns. For example, migrating data to other object
storage types eliminates provisioning the excess
capacity from fixed volume sizes on block storage. For
more detail, see
[SUS04-BP02
Use technologies that support data access and storage
patterns](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a3.html).

**Suggestion 7.1.2**: As part
of your per-migration planning evaluate your current
[recovery
time objective (RTO) and recovery point objective
(RPO](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html)).

- Design your backup strategy based on your actual
business requirements. Avoid backing up non-critical
data that has no business value, and detach volumes from
clients that are not used before considering to migrate
those workloads. For more detail, see
[SUS04-BP08
Back up data only when difficult to recreate](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a9.html).
- Use an automated solution or managed service to back up
business-critical data.
[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a fully-managed service that
makes it easy to centralize and automate data protection
across AWS services, in the cloud, and on-premises. Next
to other capabilities, AWS Backup helps you become more
sustainable. For example, you can use Backup to set an
expiration on your manual snapshots.
- Set automated lifecycle policies to enforce lifecycle
rules for the migrated data. For more detail, see
[SUS04-BP03
Use policies to manage the lifecycle of your
datasets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html).
- If you are setting up disaster recovery for your
migrating workload, evaluate your RTO and RPO, and see
if you could meet the requirement using the backup data
instead of replicating the entire data to the recovery
site. For more detail, see
[AWS Elastic Disaster Recovery](https://aws.amazon.com/de/disaster-recovery/).

**Suggestion 7.1.3:** Choose
the right migration tool, and scale your resources
corresponding to the volume of data to be migrated.

- AWS provides migration services like
[AWS Database Migration Service](https://aws.amazon.com/dms/) and

[AWS Application Migration Service](https://aws.amazon.com/application-migration-service/). You may
be able to scale down the replication instance type
selected if the amount and velocity of the ongoing data
is much smaller than the amount of historical data.
- Another alternative is to use a serverless migration
tool like
[AWS DMS Serverless](https://aws.amazon.com/blogs/aws/new-aws-dms-serverless-automatically-provisions-and-scales-capacity-for-migration-and-data-replication/).
- Here are some other options to choose from to migrate
your storage with their key characteristics.

Migrate your storage

Key Characteristic

[AWS DataSync](https://aws.amazon.com/datasync/)

Simplify, automate, and accelerate data movement to
and from AWS Storage, as well as between AWS
Storage. Easily manage data movement workloads with
bandwidth throttling, migration scheduling, task
filtering, and task reporting with a fully managed
service that seamlessly scales as data loads
increase.

[AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/)

Simply and seamlessly move your files to Amazon S3
and Amazon Elastic File System (Amazon EFS) using
SFTP, FTPS and FTP protocol. Store information in
Amazon S3 or Amazon EFS, manage workflows, and
initiate automated, event-driven tasks with a
fully-managed, low-code service. Quickly scale your
business-to-business (B2B) file transfers for each
line-of-business user.

[AWS Snow Family](https://aws.amazon.com/snow/)

Collect and process data at the edge, and migrate
data into and out of AWS through physical devices
and capacity points. Device options range to
optimize for space- or weight-constrained
environments, portability, and flexible networking
options.

For more detail, see the following:

- [Data lifecycle management](https://docs.aws.amazon.com/whitepapers/latest/best-practices-building-data-lake-for-games/data-lifecycle-management.html)
- [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [I/O characteristics and monitoring](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
- [Optimizing your AWS Infrastructure for Sustainability, Part III: Networking](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-iii-networking/)
- [Top 10 Data Migration Best Practices](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf)
- [AWS Summit SF 2022 - Optimizing your AWS infrastructure for sustainability](https://www.youtube.com/watch?v=9WJv2re6hlE)
- [Amazon EBS and Snapshot Optimization Strategies for Better Performance and Cost Savings](https://www.youtube.com/watch?v=h1hzRCsJefs)

MIG-SUS-08: Are you adopting practices that can reduce interim resource consumption during the migration?

During a migration, your consumption of resources may increase due to the provisioning of resources in both the source and target environments. The increase in consumption is often referred to as a *double bubble*. In addition, your consumption may also increase due to provisioning of migration resources, such as the networking between your source and target environments, SFTP servers, AWS Application Migration Service (MGN), or AWS Database Migration Service (DMS).

*Typical migration process flow*

You can reduce the resource consumption during the migration either by reducing the resources deployed or by reducing the duration of their deployment.

*Additional resource consumption equation*

## MIG-SUS-BP-8.1: Adopt methods that can reduce interim resource consumption during the migration

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 8.1.1**: Reduce
interim resources created in the target environment.

- Reconsider the migration of development and other
non-production environments, as these can be rebuilt
when required in AWS. If you decide on migrating your
non-production environments, revisit the portions of the
environment that need to be migrated. For example, you
may choose to migrate only some of the databases in a
database server.
- If you decide to migrate your build environment,
[increase
the utilization of these environments](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a4.html).
- [Use
managed device farms to test](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a5.html) new
features on a representative set of hardware.
- During the migration, consider the impact on
sustainability of day-to-day operations. For example,
consider avoiding frequent backups of the target
environment and setting up HA or DR during the
migration. You can also reduce the retention period of
logs or backup snapshots taken during the migration.

**Suggestion 8.1.2**: Reduce
interim resources used in the migration process.

- During a migration, you typically have to migrate
historical and on-going data. Historical data refers to
the data that was created prior to the start of the
migration. On-going data refers to the new data that is
generated in the source environment at the time of the
migration until the cutover. The resource needs for the
migration of historical data may differ from that of the
on-going data. Choose the right migration process and
tool, and also scale your resources corresponding to the
data to be migrated. For example, in the case of AWS DMS
and AWS MGN, you may be able to scale down the
replication instance type selected if the volume and
velocity of the ongoing data is significantly less to
volume of historical data. Another alternative is to use
a serverless migration tool like
[AWS DMS Serverless](https://aws.amazon.com/blogs/aws/new-aws-dms-serverless-automatically-provisions-and-scales-capacity-for-migration-and-data-replication/) that can automatically
scale based on the volume of data being migrated.
- Share your migration resources if possible. Some
migration tools let you share migration resources. An
example of this is AWS MGN, which automatically shares
the replication instance with multiple source servers
being migrated.
- For migration resources that cannot be scaled easily,
such as the networking resources between your data
center and AWS Cloud, consider
[flattening
the demand curve](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a7.html) using buffering and
throttling to reduce the required provisioned capacity
for the workload. For example, you can throttle your
network in AWS MGN when migrating your servers to AWS.
- Review the need to include migration resources in your
day-to-day operations. For example, avoid including AWS
MGN replication servers in your backup strategy. If you
are capturing logs for migration resources, you can
consider reducing the retention period for these logs.

**Suggestion 8.1.3**: Reduce
duration of deployment for the interim resources created
during the migration.

- Consider selecting a partner who has the technical
expertise and experience migrating to AWS
- Create a cross-functional
[cloud-enablement
team](https://d1.awsstatic.com/whitepapers/cloud-enablement-engine-practical-guide.pdf) to implement the governance, best
practices, training, and architecture needed for cloud
adoption. The team will define tools, processes, and
architectures that establish the organizations cloud
operating model. In addition, it will coordinate with
stakeholders across different units such as
infrastructure, security, applications, and business to
alleviate obstacles in a migration.
- Explore tooling that can facilitate your migration and
can automate and expedite aspects of the migration such
as discovery, project management, and testing.
- Train staff on tools and processes early in the
migration to give them the required skillset.
- Build a robust migration factory consisting of people,
tools, and processes that help streamline your
migration. Operate in an agile fashion increases the
velocity of the applications being moved to AWS.
- Assess the application to be migrated and satisfy all
prerequisites a few weeks prior to the migration.
- Start small to build experience, find patterns, and
create blueprints. Prioritize workloads and run the
migration in waves with short migration cycles. Create
reusable blueprints for common workload patterns that
increase the velocity of the migration. Empower your
team to automate the migration steps.

For more detail, see the following:

- [Strategy and best practices for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.html)
- [A beginners' guide for Finance and Operations teams in their cloud migration journey](https://aws.amazon.com/blogs/mt/a-beginners-guide-for-finance-and-operations-teams-in-their-cloud-migration-journey/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-sus.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
