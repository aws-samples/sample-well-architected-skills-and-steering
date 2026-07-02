# Reliability

**Pages**: 13

---

## 10 – Design to withstand failure

# Best Practice 10.1 – Agree on SAP workload availability goals that align with your business requirements

Understanding your availability goals is the first step to help ensure that you focus
on the factors important to your organization. This helps you to define criteria that can
be used to evaluate your architectural patterns.

**Suggestion 10.1.1 – Identify SAP applications in scope and their
interdependencies**

Identify the SAP applications that you have deployed or will deploy in AWS.
Understand any dependencies these applications have regardless of their location.

**Suggestion 10.1.2 – Classify systems based on the impact of
failure**

There is no open standard for system classification aligned with planned availability
and risk of failure. Defining systems using terms such as Mission Critical or Highly
Important can help with defining patterns, identifying application grouping, and
justifying costs. Production applications might be impacted differently by an outage.
Factors to consider might include:

- Revenue generating or revenue reporting
- External or internal facing
- Core business vs. technical support
- Closely coupled vs. loosely coupled with other systems

Non-production environments can also play an important role in indirectly supporting
the business. They should also be classified according to project phase and scale, taking
into account transport paths (such as business as usual and projects) and supporting role
(such as development, unit test, production copy, and training).

**Suggestion 10.1.3 – Assess the business impact of an
outage**

The impact should be measurable and take into consideration the duration of the
outage. Examples of areas of impact include health and safety, financial, legal,
regulatory, or brand.

**Suggestion 10.1.4 – Understand compliance and regulatory
requirements**

Understand compliance or regulatory requirements for data residency and distance
between locations to help ensure business continuity.

**Suggestion 10.1.5 – Define minimum acceptable percentage
uptime**

For each system, or group of systems, agree and document an acceptable availability
percentage which matches with business requirements. The following terms are used in this
context

- MTTR – Mean Time to Recovery
- RTO – Recovery Time Objective
- RPO – Recovery Point Objective

A full explanation of the terms can be found in the Well-Architected Framework
[Reliability]: [Availability](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/availability.html). Additional information on reliability in SAP can be found in the
whitepaper:

- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-10-1.html*

---

# Best Practice 10.2 – Select an architecture suitable for your availability and capacity requirements

There are standard architectural patterns for SAP availability to suit the
requirements of most customers deploying SAP on AWS. Use the following suggestions to
determine what patterns best meet your availability and capacity requirements. Evaluate
the risk and impact of each failure scenario against your business requirements.

Additional information on availability in SAP can be found in the whitepaper [Architecture Guidance for Availability and Reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html).

**Suggestion 10.2.1 – Identify all components and AWS services that
are required for your SAP system**

Identify all the required technical components of your SAP system, starting with the
core (database, application servers, central services, global file systems) and extending
to optional components (for example, Web Dispatchers, SAProuter, Cloud Connector).
Determine the required AWS services to support these components and review the
shared responsibility model for resiliency.

- AWS Documentation: [Shared Responsibility Model for Resiliency](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.html)

**Suggestion 10.2.2 – Use SLAs, durability, availability, and
historical data as a guide to the likelihood of failure**

Likelihood of failure is subjective. Published service level agreements (SLAs) and
past performance can only be used to guide the risk of potential future failure. However,
the assumed frequency of various scenarios remains a useful data point. Something which is
statistically likely to happen once a year might have a greater impact on design decisions
than a failure that is yet to occur.

The following information can be used to better understand the services:

- [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/) provides alerts and remediation guidance when AWS is experiencing
events that might impact you
- [AWS Post-Event
Summaries](https://aws.amazon.com/premiumsupport/technology/pes/) are provided for all major service events which impact AWS
service availability
- [Amazon Compute Service Level
Agreement](https://aws.amazon.com/compute/sla/) lists service level agreements (SLAs) for compute services
- AWS Documentation: [Amazon EBS Durability and Availability](https://docs.aws.amazon.com/whitepapers/latest/aws-storage-services-overview/durability-and-availability-3.html)
- AWS Documentation: [Amazon EFS
Data Protection and availability](https://aws.amazon.com/efs/faq/#Data_protection_and_availability)
- AWS Documentation: [Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/?nc=sn&loc=4&dn=2)

The likelihood of failure of other supporting services should also be evaluated
including, but not limited to, domain name services, load balancers, and serverless
functions.

More information can be found in the [Architecture Guidance for Availability and Reliability of SAP on AWS
whitepaper](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html).

**Suggestion 10.2.3 – Assess options for clustering, resilience, and
load balancing**

An SAP system can be distributed across multiple hosts, with differing mechanisms for
ensuring availability. For example, a clustering solution can be used to protect single
points of failure (for example, the SAP database and SAP Central Services). The SAP
application tier can be scaled horizontally and load balancing can be used to make the web
dispatcher highly available.

- AWS Documentation: [SAP NetWeaver Deployment and Operations Guide for Windows - High Availability
System Deployment](https://docs.aws.amazon.com/sap/latest/sap-netweaver/net-win-high-availability-system-deployment.html)
- AWS Documentation: [SAP
on AWS – IBM Db2 HADR with Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-AnyDB/sap-ibm-pacemaker.html)
- AWS Documentation: [SQL Server Deployment for High Availability](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.html)
- SAP Documentation: [High Availability Partners](https://wiki.scn.sap.com/wiki/display/SI/High+Availability+Partner+Information)

**Suggestion 10.2.4 - Determine the availability of EC2 instance
families within Availability Zones**

Some Amazon EC2 instance families (for example, `X` and `U`)
are not available across all AZs. Check with your AWS account team or Support to confirm
that the EC2 instance families you want to use are available in the intended Availability
Zones. Note that the logical AZ identifiers might be different across different accounts.
See the AWS documentation for more information.

- AWS Documentation: [AZ
IDs for your AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)

**Suggestion 10.2.5 – Investigate strategies for ensuring
capacity**

The best way to help ensure capacity is to have a similarly sized instance available
in case of failure. Other strategies include cloud native options (for example, On-Demand
Instances, EC2 instance recovery) or re-allocating shared capacity.

We recommend that you make a capacity commitment in at least two AZs for Amazon EC2
instances that support SAP single points of failure so that the capacity is available at the
time you need it.

Amazon EC2 capacity can be reserved using [Zonal Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-scope.html) or [On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-using.html). Both Zonal Reserved Instances and On-Demand
Capacity Reservations can be shared between AWS accounts within the same AWS
organization, which allows for the approach of using sacrificial capacity from another
environment in the event of significant failure (for example, a complete AZ failure).

Further guidance on capacity reservations is available in:

- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html)

**Suggestion 10.2.6 – Design your VPC across multiple Availability
Zones**

Design your VPC and subnets to ensure that instances can be provisioned in multiple
Availability Zones, even if your initial design only relies on one or two AZs. This builds
resilience into your design and helps ensure that connectivity and access to services can
be confirmed in advance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-10-2.html*

---

# Best Practice 10.3 – Define an approach to help ensure the availability of critical SAP data

The business data for an SAP application is primarily stored within the database, but
may also include file-based data or binaries (for example, executables, libraries, scripts,
configuration, and interface files).

**Suggestion 10.3.1 – Evaluate MTTR requirements and identify how they
can be met**

In [Reliability] [Suggestion 10.1.5 – Define
minimum acceptable percentage uptime](./best-practice-10-1.html), you will have defined the MTTR requirements
for each of your applications. Having assessed the risk of failures and the mechanisms for
protecting system availability, confirm your requirements can be met, and document the
expectations for MTTR against each failure scenario. If compromises need to be made for
cost, complexity, or consistency, consult with the business owners to reach an agreement.

**Suggestion 10.3.2 – Determine in which failure scenarios a recovery
from backup would be necessary**

Backup is often a secondary mechanism for ensuring or recovering availability, but
most architectures will have some reliance on backups. The following are examples of
failure scenarios that could be used to guide your analysis. The granularity of the
scenarios, classification, and impact will vary depending on your requirements and
architecture.

Comparative Risk of Occurrence
Backup Required
Potential Data Loss
Estimated Recovery Time

Planned / Controlled Maintenance
Planned

Resource exhausted or compromised (High CPU utilization /
File system full / Out of memory / Storage issues)
Medium

Distributed stateless component failure (for example, Web
Dispatchers)
Medium

Distributed stateful component failure (for example,
application servers)
Medium

Single Point of Failure (Database / SAP Central
Services)
Medium

AZ / Network Failure
Low

Core service failure (DNS / Amazon EFS / API
calls)
Low / Medium

Corruption / Accidental deletion / Malicious activities /
Faulty code deployment
Low

Region failure
Very low

**Suggestion 10.3.3 – Determine where data replication is
required**

Data replication is used to improve reliability by having copies of the same data in
multiple locations and is often a requirement for systems with a low RPO. When determining
whether replication is required for availability or recovery, consider whether the service
is Zonal (for example, Amazon EC2 and Amazon EBS and the databases they support) or Regional (for
example, shared storage and Amazon S3).
Database replication

Database
Replication Technology
Guidance

SAP HANA
HANA System Replication
SAP Documentation: [HANA System Replication](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/676844172c2442f0bf6c8b080db05ae7.html)

SAP ASE
SAP Replication Server
SAP Documentation: [SAP Replication
Server](https://help.sap.com/viewer/product/SAP_REPLICATION_SERVER)

Oracle
Oracle Data Guard
SAP Note: [105047 - Support for
Oracle functions in the SAP environment](https://launchpad.support.sap.com/#/notes/105047) [Requires SAP Portal Access]

Microsoft SQL Server
SQL Server Always ON

- SAP Documentation: [Database High-Availability with SQL Server AlwaysOn](https://help.sap.com/viewer/34ba60e8526d4110921c9c0fd05b4b6d/LATEST/en-US/483523b4fd7c433998ec38dadcd67d3c.html)
- AWS Documentation: [SQL Server Deployment for High Availability](https://docs.aws.amazon.com/sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.html)

SAP MaxDB
MaxDb Standby Database
SAP Note: [952783 - FAQ: SAP MaxDB
high availability](https://launchpad.support.sap.com/#/notes/952783) [Requires SAP Portal Access]

IBM Db2
HADR
SAP Note: [1612105 - DB6: FAQ on
Db2 High Availability Disaster Recovery (HADR)](https://launchpad.support.sap.com/#/notes/1612105) [Requires SAP Portal
Access]

AWS service replication options

Service
Operating level
Replication options available
Guidance

Amazon EFS
File system

Continuous asynchronous replication within a Region and cross Region

[Amazon EFS Replication](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html)

Amazon FSx for Windows File Server
File system

Scheduled asynchronous replication within a Region and cross Region using
AWS DataSync

[Scheduled replication using AWS DataSync](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/scheduled-replication-datasync.html)

Amazon FSx for NetApp ONTAP
File system

Scheduled asynchronous replication within a region and cross region via NetApp
SnapMirror

[Scheduled replication using NetApp SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html)

Amazon S3
S3 bucket
Continuous asynchronous replication within a Region and cross Region

[Amazon S3 Replicating objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)

AWS Elastic Disaster Recovery
EC2 instance
Continuous asynchronous replication within a Region and cross Region

[AWS Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)

**Suggestion 10.3.4 – Build a strategy to ensure consistent
configuration data and binaries**

It is important to have consistent configuration data and binaries to help ensure
predictable behavior and a tested setup following a failure. This can include operating
system packages, application parameters, and cluster configuration. Determine how you
could ensure alignment across all instances for an application, including those which are
there for resilience (for example, additional application servers, secondary database
nodes).

Amazon EFS, Amazon FSx, and Amazon S3 provide a durable location for shared binaries
or configuration that can be managed centrally.

Refer to [Operational Excellence] [Best Practice 2.1
- Use version control and configuration management](./best-practice-2-1.html) pillar for mechanisms to
control versions and manage configuration.

**Suggestion 10.3.5 – Have a holistic approach to data
consistency**

The approach to ensuring the consistency of critical SAP data should not only focus on
a single set of data but also should consider the dependencies within and between datasets
and systems. For example, if you need to recover an SAP BW system, but not the source
systems it pulls from, what would be the impact on change pointers and what mechanisms are
in place to ensure a consistent recovery?

**Suggestion 10.3.6 – Build a strategy for interfaces that permits
data to be replayed or re-sent**

For data exchange between systems, determine whether the integration is loosely
coupled and if data can be replayed or re-sent, either at the source or target. Review if
there are queuing capabilities to allow the scenario to be suspended or cached during an
outage.

**Suggestion 10.3.7 – Evaluate the use of a data bunker**

Failure scenarios that result in the online data becoming unusable or unavailable due
to situations such as accidental deletion or a malicious act might require a different
approach to help ensure that data is protected or recoverable.

Although prevention is the best defense through a security framework covering network
isolation and access control, the impact should be considered in the context of recovery
and resilience.

Using a *write only* backup account with a reduced retention
period is a common approach for this rare but potentially high impact scenario.

- SAP Lens [Security]: [Best Practice 8.3 - Secure
your data recovery mechanisms to protect against threats](./best-practice-8-3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-10-3.html*

---

# Best Practice 10.4 – Validate the design against a set of criteria based on your business requirements

Establish a set of criteria based on your business requirements, balancing the risk of
failure, impact on the business, and acceptable trade-offs. Use these criteria to validate
the design and make adjustments where necessary.

**Suggestion 10.4.1 – Assess the cost to your business of an
outage**

Failures, of either AWS services or SAP components, will impact your SAP system
differently depending on the resilience and recovery strategies. The type of failure will
determine the duration of the outage (RTO) and the potential data loss (RPO).

For each failure, assess the risk of an outage and the cost to your business. For
example, are there revenue generating processes that will be impacted and what is the
hourly cost associated with the system not being available?

**Suggestion 10.4.2 – Assess the cost of your architecture**

In SAP Landscapes, the largest elements of the AWS monthly bill typically are for
Amazon EC2 and storage-related services. Understand the cost implications so that you
select the best architecture to meet your reliability requirements. Key contributors
include:

- Deployment patterns that don’t maximize hardware utilization
- Redundant copies of data
- Operating system license costs
- Clustering software license costs
- Costs associated with maintenance, testing, and skilled resources

Refer to [Cost Optimization]: [Cost optimization
Best Practices](./cost-optimization.html) for further details.

**Suggestion 10.4.3 – Evaluate your design against other pillars in
the framework**

Reliability cannot be designed in isolation, but should be assessed against the rest
of the pillars of the AWS Well-Architected Framework. Example questions you might ask to
evaluate this include:

- Operational excellence — Do you have the experience and skills to manage the
solution?
- Security — Is your data protected during replication, recovery, etc.
- Performance — Does replication or the backup activity impact user
performance?
- Cost optimization — Does the cost of the solution align with the assumed
risk?
- Sustainability — Does the solution align with your sustainability and environmental
impact initiatives?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-10-4.html*

---

## 11 – Detect and react to failures

# Best Practice 11.1 – Monitor failures of the SAP application, AWS resources, and connectivity

Monitoring for failures of the SAP application, AWS resources, and connectivity
helps you to react to failures or potential failures in a timely manner.

**Suggestion 11.1.1 – Use AWS Personal Health Dashboard and
notifications**

The [Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/) gives you a personalized view of the status of the AWS services that
power your applications, enabling you to quickly see when there are issues impacting your
SAP workload. For example, in the event of a lost [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) volume associated with one of your [Amazon EC2](https://aws.amazon.com/ec2/) instances.

The dashboard also provides forward looking notifications, and you can set up alerts
across multiple channels, including email, so that you receive timely and relevant
information to help plan for scheduled changes. For example, in the event of AWS hardware
maintenance activities that impact one of your [Amazon EC2](https://aws.amazon.com/ec2/) instances, you would receive a notification with information to help you
plan for and proactively address any issues associated with the upcoming change.

**Suggestion 11.1.2 – Evaluate AWS services to understand the health
of your SAP system**

AWS provides a number of [management and
governance](https://aws.amazon.com/products/management-and-governance/) services that you should evaluate, including Amazon CloudWatch and Amazon CloudWatch Application Insights for
SAP. Focus on the metrics that indicate a failure or potential failure, such as EC2 instance
failure, high CPU utilization, and file system utilization.

Refer to the Operational Excellence pillar for more details:

- SAP Lens [Operational Excellence]: [Best
Practice 1.1 - Implement prerequisites for monitoring SAP on AWS](./best-practice-1-1.html)
- SAP Lens [Operational Excellence]: [Best
Practice 1.4 - Implement workload configuration monitoring](./best-practice-1-4.html)

**Suggestion 11.1.3 – Evaluate the capability of SAP tools to monitor
failures**

Tools from SAP, such as Solution Manager and Landscape Manager, allow you to view any
monitoring data in the context of the application. The following monitoring solutions are
available from SAP. Review any additional licensing costs as part of the evaluation of
these tools.

- SAP Documentation: [SAP Focused run](https://support.sap.com/en/alm/sap-focused-run.html)
- SAP Documentation: [SAP Solution
Manager](https://support.sap.com/en/alm/solution-manager.html)
- SAP Documentation: [SAP
Landscape Manager (LaMa)](https://help.sap.com/viewer/lama_help)
- SAP Note: [2574820
- SAP Landscape Management Cloud Manager for Amazon Web Services (AWS)](https://launchpad.support.sap.com/#/notes/2574820)
[Requires SAP Portal Access]

**Suggestion 11.1.4 – Evaluate third-party tools for AWS and SAP
monitoring**

The following monitoring solutions are available from the AWS Marketplace. You should evaluate
these and other third-party tools.

- AWS Documentation: [Monitoring Solutions in AWS Marketplace](https://aws.amazon.com/marketplace/b/2649280011?ref_=mp_nav_category_2649280011)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-11-1.html*

---

# Best Practice 11.2 – Define an approach to maintain availability

Maintain availability by having a resilient architecture that can sustain the failure
of a single technical component or AWS service. Implement mechanisms, which could include
redundant capacity, load balancing, and software clusters.

**Suggestion 11.2.1 – Avoid failures due to exhausted resources or
service deterioration**

Investigate over-provisioning of resources, proactive monitoring of growth, and
throttling usage by setting limits.

The operational excellence pillar covers the different ways in which you can
understand the state of your SAP application and ensure that the appropriate actions are
taken, see [Operational Excellence]: [1 - Design SAP
workload to allow understanding and reaction to its state](./design-principle-1.html).

The performance pillar can assist with guidance on right-sizing and scaling capacity
[Performance]: [16 - Understand ongoing performance and
optimization options](./design-principle-16.html).

**Suggestion 11.2.2 – Have a strategy for scheduled
maintenance**

If your business has a requirement to minimize scheduled outages, you should develop
a strategy for maintenance at all levels – SAP application, database, operating system,
and AWS. Consider the following:

- Use of replication and cluster solutions to alternate the primary and secondary
node.
- Excess capacity and mechanisms to scale up and down to facilitate rolling
outages.
- Use of a live patching approach for the operating system, if possible.

[SUSE Linux Enterprise
Live Patching](https://www.suse.com/products/live-patching/)
- [Red Hat Reducing downtime for SAP HANA Whitepaper](https://www.redhat.com/cms/managed-files/pa-sap-hana-reducing-downtime-overview-f22788pr-202004-en.pdf)

- AWS Documentation: [AWS Systems Manager Patch Manager Patch Groups](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
- SAP Note: [1913302
- HANA: Suspend DB connections for short maintenance tasks](https://launchpad.support.sap.com/#/notes/1913302) [Requires SAP
Portal Access]
- SAP Note: [2077934
- Rolling kernel switch in HA environments](https://launchpad.support.sap.com/#/notes/2077934) [Requires SAP Portal Access]
- SAP Note: [953653 -
Rolling Kernel Switch](https://launchpad.support.sap.com/#/notes/953653) [Requires SAP Portal Access]
- SAP Note: [2254173
- Linux: Rolling Kernel Switch in Pacemaker-based NetWeaver HA environments](https://launchpad.support.sap.com/#/notes/2254173)
[Requires SAP Portal Access]

You should also evaluate the elastic capabilities of AWS services to reduce the
overall downtime of scheduled maintenance by temporarily increasing performance. For
example, scaling up the size of the Amazon EC2 instance running your database to provide more CPU
and storage throughput for upgrade activities, or switching your EBS volumes type from
`gp2` to `io2` to improve storage throughput during a database
reorganization.

**Suggestion 11.2.3 – Protect SAP single points of failure with
software clusters or other mechanisms**

You can use a high availability (HA) clustering solution for autonomous failover of
SAP single points of failure (SAP Central Services and database) across Availability
Zones.

There are multiple SAP-certified clustering solutions [listed on
the SAP website](https://wiki.scn.sap.com/wiki/display/SI/Certified+HA-Interface+Partners). SAP clustering solutions are supported by the cluster software
vendors themselves, not by SAP. SAP only certifies the solution. Any custom-built solution
is not certified and will need to be supported by the solution builder.

If you choose not to use a clustering solution for your single points of failure,
consider scripting or runbooks to minimize the errors associated with restoring
services.

**Suggestion 11.2.4 – Consider redundant capacity or automatic scaling
for components that support it**

Evaluate static, dynamic, or scheduled capacity changes to match your usage. Examine
the minimum capacity requirements and how they would be impacted by failures and
maintenance. Overprovision where appropriate to allow time to recover from failure.

If you need to maintain 100% capacity in the event of an AZ failure, then you should
consider deploying the application tier across three AZs, each with 50% of the total
required capacity.

In addition to deploying the SAP Application Server Layer across multiple AZs, you
could consider scaling solutions such as the one described in the following SAP on AWS
Blog post that leverages the capabilities of [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling).

- SAP on AWS Blog: [Using AWS to enable SAP Application Auto Scaling](https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/)
- AWS Documentation: [Amazon EC2 Instance Types for SAP](https://aws.amazon.com/sap/instance-types/)
- SAP Note: [1656099
- SAP Applications on AWS: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099) [Requires SAP
Portal Access]

**Suggestion 11.2.5 – Ensure the availability of capacity for all
identified failure scenarios**

The following are examples of failure scenarios that could be used to guide your
analysis. Granularity and coverage of the scenarios, classification, and impact will vary
depending on your requirements and architecture.

Failure scenario examples
Comparative Risk of Occurrence

Planned / Controlled Maintenance
Planned

Resource exhausted or compromised (High CPU utilization /
File system full / Out of memory / Storage issues)
Medium

Distributed stateless component failure (for example, web
dispatchers)
Medium

Distributed stateful component failure (for example,
application servers)
Medium

Single point of failure (Database / SAP Central
Services)
Medium

AZ / Network failure
Low

Core service failure (DNS / Amazon EFS / API calls)
Low / Medium

Corruption / Accidental deletion / Malicious activities /
Faulty code deployment
Low

Region failure
Very Low

Further guidance on capacity reservations is available in [Reliability]: [Suggestion 10.2.5 - Investigate strategies for ensuring
capacity](./best-practice-10-2.html) and in the AWS whitepaper: [Architecture Guidance for Availability and Reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html).

You can review what Reserved Instances you have available within your AWS account
using the [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-concepts-buying.html#view-reserved-instances) section of the Amazon EC2 console. You can review what On-Demand
Capacity Reservations you have available using the [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-using.html#capacity-reservations-view) section of the Amazon EC2 console.

**Suggestion 11.2.6 – Use AWS services that have inherent
availability where applicable**

Several AWS services have inherent availability as part of their design and run
across multiple Availability Zones for high availability. Some of the relevant services
used in an SAP context include:

- AWS Service: [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/how-it-works.html)
- AWS Service: [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html)
- AWS Service: [Route 53](https://aws.amazon.com/route53/faqs/)
- AWS Service: [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/how-transit-gateways-work.html)
- AWS Service: [Amazon S3](https://aws.amazon.com/s3/)
- AWS Service: [Amazon FSx](https://docs.aws.amazon.com/fsx/index.html)

In addition, components that use stateless services, such as bastian hosts or
SAProuter, can use Auto Scaling Groups to achieve high availability.

**Suggestion 11.2.7 -– Follow AWS best practices to ensure network
connectivity**

Evaluate one or more of the following AWS best practices to ensure the resilience
of network connectivity to the AWS Region in use:

- AWS Documentation: [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resilency_toolkit.html)
- AWS Documentation: [AWS VPN CloudHub](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-vpn-cloudhub.html)
- AWS Documentation: [AWS Cloud
WAN](https://aws.amazon.com/cloud-wan/)

If your cluster solution relies on an overlay IP consider the following to enable
access from outside of the VPC:

- AWS Documentation: [SAP on
AWS High Availability with Overlay IP Address Routing](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-ha-overlay-ip.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-11-2.html*

---

# Best Practice 11.3 – Define an approach to restore service availability

Restoring availability assumes that for a particular failure scenario, some loss of
service will occur. The restore approach should examine the amount of time needed to
restore service, and the actions required to meet the availability goal.

**Suggestion 11.3.1 – Enable instance recovery for EC2
instances**

AWS provides two modes of instance recovery: simplified (on by default) and
Amazon CloudWatch action-based (configurable). Both modes monitor an Amazon EC2 instance and automatically
recover the instance if it becomes impaired due to an underlying hardware failure. This
feature can remove the need for manual intervention, but startup, application restart, and
load times should be factored into the recovery time objective (RTO).

CloudWatch action-based alarms are customizable, which can help you to control the recovery
time of an instance for standalone instances.

If you intend to use a clustering solution to protect against hardware failure, you
should evaluate if instance recovery is compatible with the cluster solution.

- AWS Documentation: [Amazon EC2 Instance Recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
- SAP on AWS Documentation: [Technical requirements for high availability clusters](https://docs.aws.amazon.com/sap/latest/sap-netweaver/technical-requirements.html)

**Suggestion 11.3.2 – Have a strategy to rebuild EC2 instances using
AMIs and infrastructure as code**

The benefit of infrastructure as code (IaC) is the ability to build and tear down
entire environments programmatically. If architected for resiliency, an environment can be
implemented in minutes using [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) templates or [AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html). Automation is critical for maintaining high
availability and fast recovery.

You should evaluate the following AWS services as part of your strategy:

- AWS Service: [EC2 Image
Builder](https://aws.amazon.com/image-builder/)
- AWS Service: [AWS Launch Wizard for SAP](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html)
- AWS Service: [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)
- SAP on AWS Blog: [DevOps for SAP](https://aws.amazon.com/blogs/awsforsap/category/devops/)

**Suggestion 11.3.3 – Understand Amazon EBS failures**

Failure of one or more EBS volumes could impact the availability and durability of
your SAP workload. Therefore, you should understand the Amazon EBS failure rates, notification
mechanisms, and recovery options.

- AWS Documentation: [Amazon EBS Durability](https://aws.amazon.com/ebs/features/#Amazon_EBS_availability_and_durability)
- AWS Documentation: [Monitor the status of your volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html)
- AWS Service: [AWS Health Dashboard](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/)
- AWS Documentation: [Volume
recovery using Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

**Suggestion 11.3.4 – Have a strategy for reacting to AWS Personal
Health Dashboard notifications**

You should have a strategy for receiving and actioning notifications from your AWS
Personal Health Dashboard. This could include using CloudWatch to start Amazon SNS or
integration with your ITSM tools via the [AWS Health
API](https://docs.aws.amazon.com/health/latest/ug/health-api.html).

**Suggestion 11.3.5 – Ensure that you are protected against accidental
or malicious events impacting availability**

You should consider the following approaches for ensuring that you are protected
against accidental or malicious events that could impact the availability of your SAP
workload.

- Implement a [principle of least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and enforce separation of duties within AWS
Identity and Access Management.
- Follow the guidance in AWS Knowledge Center article: [How do I protect my data against accidental EC2 instance termination?](https://aws.amazon.com/premiumsupport/knowledge-center/accidental-termination/)
- Follow the [Best
practices for Amazon EC2.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html)
- You should also follow the security guidance in [Security]: [Best Practice 8.3 - Secure your data recovery mechanisms
to protect against threats.](./best-practice-8-3.html)

**Suggestion 11.3.6 – Identify dependencies beyond the SAP workload in
AWS**

Understand the underlying dependencies for your SAP business processes, including
shared services and supporting components or systems. Some examples include Active
Directory, DNS, identity providers, SaaS services, and on-premises systems. Assess the
impact of failure and the required mitigations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-11-3.html*

---

# Best Practice 11.4 – Conduct periodic tests of resilience

Periodically test resilience against critical failure scenarios to prove that software
and procedures result in a predictable outcome. Evaluate any changes to architecture,
software, or support personnel to determine if additional testing is necessary.

**Suggestion 11.4.1 – Define the in-scope critical failure scenarios
based on your business requirements**

You should define which critical failure scenarios you are able to test, aligned with
your business requirements. The following are examples of failure scenarios which could be
used to guide your analysis. Granularity and coverage of the scenarios, classification and
impact will vary depending on your requirements and architecture.

Failure Scenario Examples
Comparative Risk of Occurrence

Planned / Controlled Maintenance
Planned

Resource exhausted or compromised (High CPU utilization /
File system full / Out of memory / Storage issues)
Medium

Distributed stateless component failure (for example, web
dispatchers)
Medium

Distributed stateful component failure (for example,
application servers)
Medium

Single point of failure (Database / SAP Central
Services)
Medium

AZ / Network failure
Low

Core service failure (DNS / Amazon EFS / API
calls)
Low / Medium

Corruption / Accidental deletion / Malicious activities /
Faulty code deployment
Low

Region failure
Very Low

**Suggestion 11.4.2 – Define a set of test cases to simulate critical
failures**

You should have a complete set of tests defined to simulate the critical failure
scenarios that would impact your SAP workload.

You should be aware that for some failure scenarios a simulation might not fully
represent the actual failure that would occur. For example, to simulate a hardware issue,
you cannot cause a failure of an EC2 instance, but for Nitro-based instances you can
generate a kernel panic to cause the instance to reboot.

In addition, [AWS Fault Injection
Simulation](https://aws.amazon.com/fis/) is designed to help simulate failures within your AWS resources.

- AWS Documentation: [High Availability Configuration Guide for SAP on HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-ha-configuration.html)
- AWS Documentation: [Send a diagnostic interrupt](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/diagnostic-interrupt.html#diagnostic-interrupt-prereqs)

**Suggestion 11.4.3 – Define the expected behavior for each test
case**

You should have a documented set of expected outcomes to baseline your testing.

**Suggestion 11.4.4 – Define an approach for evaluating the impact of
a change and the subsequent testing required**

You should have an approach defined to evaluate the impact of a change on your
environment and the testing required as part of that change to help ensure that it does
not invalidate your approach to availability and reliability. Examples of these types of
changes include software upgrades, patches, and parameter changes.

**Suggestion 11.4.5 – Define a test schedule**

Ensure that you have a test schedule that covers the initial implementation, testing
of changes, and periodic validation of your environment.

**Suggestion 11.4.6 – Review the testing outcomes**

Based on the test outcomes, identify any improvements to the test cases, configuration
or architecture.

**Suggestion 11.4.7 – Define the required activities to return to a
pre-test state**

As part of each test, you should define the required activities to return to the
pre-test state. This is to ensure that each test case is isolated from other tests and
that the testing does not impact the availability and reliability of a production
system.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-11-4.html*

---

# Best Practice 11.5 – Automate reaction to failure

You can minimize the impact to service by automating the response to failure. Design
automation to respond to failure, impaired capacity, or loss of connectivity. Ensure clear
arbitration criteria are defined to avoid false positives.

**Suggestion 11.5.1 – Evaluate your automation for application
awareness**

For automation solutions that protect an application, evaluate the impact on state – for
example, connected user sessions, logon targets, data replication consistency, and data
corruption risk.

**Suggestion 11.5.2 – Evaluate the health check mechanisms that
initiate automation**

Health checks should be designed with controls to help ensure that automations are not
started because of false positives.

Where possible, rely on the data plane over the control plane for resilience. The
control plane is used to configure resources, and the data plane delivers services. Data
planes typically have higher availability design goals than control planes and are usually
less complex.

- AWS Documentation: [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-11-5.html*

---

## 12 – Plan for data recovery

# Best Practice 12.1 – Establish a method for consistent recovery of business data

Define data recovery plans that can help ensure business data consistency for an
individual system in the event of data loss or corruption.

**Suggestion 12.1.1 - Ensure that database backups are consistent by
using backup mechanisms that are aware of database state**

SAP provides mechanisms for integrating with a database vendor’s backup capability
(for example, brtools) and providing visibility within SAP transactions or management
consoles. In addition, there are options to integrate with third-party backup providers or
storage solutions including [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html). These supported options have awareness of
database state, continuously capturing changes or quiescing the database (pausing or
reducing activity) while a consistent copy is taken, for example using storage snapshots.

Review the SAP guides for individual database vendors as well as AWS documentation:

- AWS Documentation: [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-sap-hana.html)
- SAP Documentation: [Guide
Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/viewer/nwguidefinder)
- SAP on AWS Blog: [How to back up Microsoft SQL Server databases for SAP with VSS Snapshots](https://aws.amazon.com/blogs/awsforsap/how-to-back-up-microsoft-sql-server-databases-for-sap-with-vss-snapshots/)
- AWS Blog: [Taking crash-consistent snapshots across multiple Amazon EBS volumes on an Amazon
EC2 instance](https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/#:~:text=AWS%20Storage%20Blog-,Taking%20crash%2Dconsistent%20snapshots%20across%20multiple%20Amazon%20EBS,on%20an%20Amazon%20EC2%20instance&text=Snapshots%20retain%20the%20data%20from,to%20as%20crash%2Dconsistency).)

**Suggestion 12.1.2 – Evaluate the durability and recoverability of
file-based data critical to your business**

Business data that is not stored within a database might require a separate backup
strategy.

In a standard SAP NetWeaver system, this often includes file-based interface files,
SAP transport directory contents, and logs including batch logs, job logs, and work process
directory logs. Non-SAP NetWeaver and supporting systems, such as document management
solutions, might have other file-based business data which should be evaluated. Evaluate
[Amazon EFS](https://aws.amazon.com/efs/) or [Amazon FSx](https://aws.amazon.com/fsx/) to increase availability and durability of
such file systems.

File system backups can be performed using snapshots, [AWS Backup](https://aws.amazon.com/backup/), or third-party backup solutions.

Business data should be evaluated independently from binaries and configuration data,
which might be able to be re-provisioned via SAP download, re-install, or infrastructure as
code.

- SAP Lens [Operational Excellence]: [Suggestion
12.2.1 - Define infrastructure as code approach to the creation and change of
configuration](./best-practice-12-2.html)
- SAP Lens [Operational Excellence]: [Suggestion
12.2.2 - Define an approach for backups of file system contents, including the root
volume](./best-practice-12-2.html)

**Suggestion 12.1.3 – Evaluate the durability and location of database
backups and logs**

Backups and logs contain a record of your live data, but can themselves be
susceptible to failure. Consider how you minimize the impact of a failure by evaluating
the location of your backups in relation to your active data copies. It’s important to
consider the following:

- The time it takes to secure the backups – impacting your recovery point
- The time it takes to retrieve/recover the backups – impacting your recovery
time

Additional information:

- AWS Documentation: [AWS
Backint Agent for HANA](https://aws.amazon.com/backint-agent/)
- AWS Documentation: [FSR (Fast Snapshot Restores)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.html)
- AWS Documentation: [Amazon S3
Replication options](https://docs.aws.amazon.com/AmazonS3/latest/dev/replication.html)

**Suggestion 12.1.4 – Evaluate your requirements for a point-in-time
recovery**

If you have a requirement to recover to any particular point in time, does your backup
design allow for this? Is the backup method database-aware and can you roll your database
forward to a consistent recovery point? Have you considered any file-based recovery
required for consistency?

Consider the following:

- The log interval and how quickly logs are secured
- Incremental or differential backups to improve the recovery time
- If a backup catalog or other mechanism is required
- Is it possible to use database or storage options to go back in time?

**Suggestion 12.1.5 – Review mechanisms for recovery caused by data
loss**

Determine the implications of recovering from a significant data loss situation, such
as data corruption, deletion, or a faulty code deployment that is unable to be reverted.
Evaluate the propagation of data loss when using database or storage-based replication,
and the RTO and RPO impact of using a secondary restore mechanism, such as backups.

**Suggestion 12.1.6 – Create a data bunker**

Following the guidance in [Suggestion 10.3.7 -
Determine in which failure scenarios a recovery from backup would be necessary](./best-practice-10-3.html),
create a data bunker to secure your backups from accidental deletion or malicious
activities.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-12-1.html*

---

# Best Practice 12.2 – Establish a method for recovering configuration data

A number of different types of data, which are required to run an SAP workload, do not
reside in the SAP database. This includes operating system configuration, metadata to
recreate the required AWS resources, and data required by the SAP applications stored
within a file system. Define a process for recovering or recreating this data in the event
of data loss.

**Suggestion 12.2.1 – Define infrastructure as code approach to the
creation and change of configuration**

Manual changes made directly to individual instances can quickly lead to
inconsistencies in configuration between systems and a reliance on backups to recover
state. By using infrastructure as code, you can deploy your SAP systems and implement
changes in the same manner that you would manage application code. DevOps mechanisms, such
as a code pipeline, can provide additional control and testing to help ensure consistency
and repeatability within your landscape.

You should evaluate the following AWS services as part of your approach:

- AWS Service: [AWS Launch
Wizard for SAP](https://aws.amazon.com/launchwizard/)
- AWS Service: [EC2 Image
Builder](https://aws.amazon.com/image-builder/)
- AWS Service: [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)
- SAP on AWS Blog: [DevOps for SAP](https://aws.amazon.com/blogs/awsforsap/category/devops/)
- AWS Documentation: [Introduction to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/welcome.html)
- AWS Documentation: [Launch Service Catalog products created with AWS Launch Wizard](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap-service-catalog.html)

**Suggestion 12.2.2 – Define an approach for backups of file system
contents, including the root volume**

Operating system packages and configuration, application binaries, and file system
contents are integral to running an SAP system, but are not part of the core SAP database
backup. Evaluate mechanisms to secure and restore this data, including Amazon Machine
Images (AMIs), EBS volume snapshots, and other backup options.

The frequency and alignment of AMIs, snapshots, and file system copies should be
considered, as well as the granularity for recovery and the time taken.

In certain scenarios, using infrastructure as code might reduce backup requirements
for non-business data by focusing on recreation versus restoration.

- SAP Documentation: [Required File Systems and Directories](https://help.sap.com/viewer/910828cec5d14d6685da380aec1dc4ae/CURRENT_VERSION/en-US/de6cad1446a743d3853dbcae48bddfba.html)
- AWS Documentation: [Designing a backup and recovery solution](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/design.html)

**Suggestion 12.2.3 – Document any manual settings**

Any manual activities which are not contained in the database, deployable by code, or
able to be restored using volume backups, should be recorded to ensure an SAP system can
be recreated in the worst case scenario.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-12-2.html*

---

# Best Practice 12.3 - Define a recovery approach for your complete SAP estate

If your SAP estate consists of multiple SAP systems, you need to create a detailed
approach that defines the order in which each system is recovered, based on business
priorities. Evaluate how data loss might impact consistency across systems and business
operations.

**Suggestion 12.3.1 – Create a business continuity plan that includes
restore priority and plans to ensure consistency**

Have a business continuity plan (BCP) that determines the priority to restore each
SAP system based on the classification of systems determined in [Reliability]: [Suggestion 10.1.2 – Classify systems based on the impact of
failure](./best-practice-10-1.html). The plan should also consider the impact of cross system consistency
requirements as well as the use of multi-tenant databases on the restore priority.

**Suggestion 12.3.2 – Evaluate any dependencies on shared
services**

As you define your recovery approach, consider which shared services are either part of
the foundation for running your SAP workload (for example, DNS, Active Directory) or
required to perform the restore itself (for example, backup tools). Evaluate risks and
restore prerequisites associated with these dependencies.

**Suggestion 12.3.3 – Create runbooks to be followed in a
disaster**

A predefined runbook ensures that a proven set of steps is followed in the event of a
disaster, reducing the risk or critical activities being missed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-12-3.html*

---

# Best Practice 12.4 – Conduct periodic tests to validate your recovery procedure

Periodically test recovery from critical failure scenarios to prove that software and
procedures result in a predictable outcome, and to validate the state and health of the
backup files. You should evaluate any change to architecture, software, or support
personnel to determine if additional testing is necessary.

**Suggestion 12.4.1 – Identify the failure scenarios for recovery
testing**

You should define the failure scenarios in which a recovery would be required based
on [Reliability]: [Suggestion 10.3.2 – Determine in
which failure scenarios a recovery from backup would be necessary](./best-practice-10-3.html) and decide the
appropriate level of testing required to validate the process and tooling.

**Suggestion 12.4.2 – Determine the impact of a system change on your
recovery approach**

Define an approach for evaluating the impact of a change and the subsequent recovery
testing required to ensure it does not invalidate your approach. Examples of the types of
change that could impact your workload recovery include software upgrades, patches and
parameter changes.

A recovery test should also be planned in the event of a significant change in the
operating model used to support your SAP environments, for example, a change in Managed
Service Partner or key personnel.

**Suggestion 12.4.3 – Define a recovery test plan**

You should have a complete set of tests defined to simulate the critical failure
scenarios that would result in the need for a recovery. Recovery testing should be planned
for during initial implementation and subsequently on a periodic basis or when required.

- SAP Lens [Operational Excellence]: [Best
Practice 4.3 - Regularly test business continuity plans and fault recovery](./best-practice-4-3.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-12-4.html*

---
