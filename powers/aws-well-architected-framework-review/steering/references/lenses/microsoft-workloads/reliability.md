# Reliability

**Pillar**: Reliability  
**Questions**: 5

---

# MSFTREL01 — Workload architecture and availability

**Pillar**: Reliability  
**Best Practices**: 3

---

# MSFTREL01-BP01 Define availability goals for Microsoft workloads

Identifying your organization's specific availability objectives is
crucial as it guides your focus towards critical factors. This
clarity enables you to establish relevant criteria for assessing and
selecting the most appropriate architectural patterns for your
workload.

**Desired outcome:** Have clearly
defined and documented availability requirements for Microsoft
workloads on AWS that align with business needs, enabling informed
architectural decisions and providing measurable performance targets
that support the organization's operational goals.

**Common anti-patterns:**

- Applying the same availability requirements to each of your
Microsoft workloads without considering their individual
business impact or criticality, leading to overprovisioning for
less critical services or underestimating the needs of
mission-critical applications.
- Defining initial availability goals but failing to review and
adjust them as business needs evolve, resulting in outdated
architectural decisions that no longer align with current
organizational priorities or growth.

**Benefits of establishing this best
practice:**

- Clear availability requirements avoid over-engineering or
under-engineering solutions, allocating resources efficiently
based on actual business needs rather than assumptions and
leading to better cost control and ROI.
- Well-defined availability goals enable precise architectural
planning and implementation of appropriate resilience measures,
resulting in fewer service disruptions and better alignment
between IT capabilities and business expectations.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin with stakeholder workshops to identify and document
availability requirements for each Microsoft workload. Create a
standardized template that captures key metrics (like RTO, RPO,
and SLAs) and business impact levels, then prioritize workloads
based on criticality.

Work with business units to validate these requirements, verifying
that they reflect actual operational needs rather than technical
assumptions.

Document the approved requirements in a central repository,
establish a regular review cycle (for example, quarterly), and use
these specifications to guide architectural decisions in AWS,
including the selection of appropriate Availability Zones, backup
strategies, and failover mechanisms.

### Implementation steps

- Conduct stakeholder workshops to gather and document
availability requirements for each Microsoft workload, using
a standardized template to capture RTO, RPO, and SLA
targets.
- Create a prioritized matrix of workloads based on business
criticality and required availability levels, validated by
business unit leaders.
- Establish a central documentation repository for storing and
managing availability requirements, with clear version
control and change management processes.
- Develop architectural blueprints that map the documented
availability requirements to specific AWS services and
design patterns.
- Implement a quarterly review cycle to reassess and update
availability requirements, continually aligning with
business needs and AWS best practices.

## Resources

**Related documents:**

- [Understanding
availability need](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/understanding-availability-needs.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel01-bp01.html*

---

# MSFTREL01-BP02 Align your architectural design with your availability needs and capacity demands

There are architecture recommendations regarding Microsoft
workloads, whether addressing Windows infrastructure, Active
Directory, SQL Server databases, .NET applications, or other
technologies. Review the vendor recommendations along with AWS
documentation to verify that your application is running with best
practices to improve availability and resiliency.

**Desired outcome:** A Microsoft
workload optimized for high availability and scalability and aligned
with vendor recommendations and AWS best practices. This strategy
verifies that the system meets availability targets and capacity
demands efficiently, while remaining resilient and maintainable.

**Common anti-patterns:**

- Directly migrating Microsoft workloads to AWS without
redesigning for cloud capabilities, resulting in missed
opportunities for improved availability and automated scaling.
- Ignoring Microsoft's recommended high-availability
configurations (like Always On Availability Groups for SQL
Server) in favor of simplified single-instance deployments.
- Treating AWS Regions as simple datacenter replacements rather
than using multi-AZ and Regional resilience patterns specific to
AWS infrastructure.

**Benefits of establishing this best
practice:**

- Increased system reliability through proven architectural
patterns, reducing downtime and improving customer satisfaction
while lowering operational overhead.
- Optimized cost-efficiency by properly sizing resources and
utilizing AWS's elastic scaling capabilities, avoiding
over-provisioning while maintaining performance.
- Enhanced disaster recovery capabilities through AWS-specific
resilience features combined with Microsoft's high-availability
solutions, maintaining business continuity.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Document your current Microsoft workload architecture and
availability needs, and consult AWS and Microsoft best practices
for your specific technologies.

Develop a phased migration plan incorporating these
recommendations, prioritizing critical components.

Use AWS managed services where possible and implement multi-AZ
deployments.

Regularly test resilience and conduct Well-Architected reviews to
align with best practices.

### Implementation steps

- Evaluate SQL Server Always On Availability Groups
configuration, Active Directory domain controller placement,
Exchange Database Availability Groups, SharePoint farm
topology, and .NET application dependencies. Document
current RTO/RPO requirements and identify single points of
failure in your Microsoft workload stack.
- Implement SQL Server Always On across multiple Availability
Zones using Amazon EC2 or Amazon RDS Multi-AZ, deploy Active
Directory domain controllers in separate Availability Zones
with AWS Managed Microsoft AD integration, establish
Exchange DAG with cross-AZ mailbox databases, and design
.NET applications for stateless operation with Application Load Balancer distribution. For more detail, see
[Microsoft
workload architecture patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/microsoft-workloads.html).
- Replace self-managed components with Amazon RDS for SQL
Server, AWS Managed Microsoft AD, Amazon FSx for Windows File Server, and AWS Systems Manager for Windows patch
management. This reduces operational overhead while
improving availability through AWS-managed infrastructure
resilience.
- Configure SQL Server Always On listener endpoints across
Availability Zones, establish Active Directory site topology
aligned with Availability Zones, implement Exchange
transport high availability, and verify that .NET
applications handle Availability Zone failures gracefully.
Reference
[Microsoft
SQL Server on AWS best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/welcome.html).
- Test SQL Server failover scenarios, Active Directory
replication across Availability Zones, Exchange mailbox
database switchovers, and .NET application resilience to
infrastructure failures. Establish automated testing
procedures that validate both AWS infrastructure and
Microsoft application layer availability.

## Resources

**Related documents:**

- [Design
your workload service architecture](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-service-architecture.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel01-bp02.html*

---

# MSFTREL01-BP03 Safeguard the continuous accessibility of essential data from your Microsoft workload

Microsoft workloads encompass diverse technologies including SQL
Server databases, Active Directory domain controllers, Exchange
Server mailbox databases, SharePoint content databases, IIS web
applications, and Windows file servers, each requiring specialized
backup and recovery approaches. A comprehensive data accessibility
strategy must address the unique backup requirements of each
Microsoft technology while using AWS services to maintain business
continuity and data protection.

**Desired outcome:** The organization
maintains comprehensive data accessibility by implementing a robust
strategy that maintains continuous access to Microsoft SQL Server
databases, Active Directory System State and SYSVOL, Exchange
mailbox databases and transaction logs, SharePoint content databases
and search indexes, IIS configurations and application pools, and
Windows system components including certificates and registry
settings. This strategy aligns with AWS best practices for Microsoft
workload management, enabling reliable data recovery and business
continuity while using AWS infrastructure and services.

**Common anti-patterns:**

- Focusing solely on SQL Server databases while ignoring critical
Active Directory System State backups, Exchange transaction
logs, SharePoint service applications, and IIS configuration
files.
- Implementing generic backup strategies without considering
Microsoft-specific requirements such as VSS integration,
application-consistent snapshots, and service dependencies.
- Migrating to AWS without adapting backup strategies to utilize
AWS-native tools for comprehensive Microsoft workload protection
including AWS Backup, FSx for Windows File Server, and
application-aware backup solutions.

**Benefits of establishing this best
practice:**

- Verifies complete Microsoft workload restoration by protecting
databases, system configurations, application states, and
supporting components across Microsoft technologies, minimizing
business disruption.
- Using AWS-specific tools and services for Microsoft workload
management reduces operational costs, improves resource
efficiency, and provides centralized backup management across
diverse Microsoft technologies.
- Maintains consistent access to critical data while enabling
quick recovery of complex Microsoft environments, supporting
uninterrupted business operations and improved adherence across
Microsoft services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a comprehensive inventory of Microsoft workload
components, including: - SQL Server databases and transaction logs
- Active Directory System State and SYSVOL folders - Exchange
mailbox databases and transport queues - SharePoint content
databases and service applications - IIS application pools and web
configurations, Windows certificates and registry settings - FSx for Windows File Server shares

Implement AWS Backup with VSS integration for
application-consistent snapshots, configure Amazon RDS for SQL
Server automated backups, establish AWS Managed Microsoft AD
backup procedures, and use AWS Systems Manager for Windows system
configuration backup.

Regularly test recovery procedures across your Microsoft
technologies, and train staff on AWS best practices for
comprehensive Microsoft workload management.

### Implementation steps

- Create a complete inventory of Microsoft workload components
requiring continuous accessibility, including:

SQL Server databases
- Active Directory System State and SYSVOL,
- Exchange mailbox databases,
- SharePoint content databases,
- IIS configurations,
- Windows system settings,
- and FSx for Windows File Server data

- Configure AWS Backup with VSS integration for
application-consistent snapshots of Microsoft workloads,
implement Amazon RDS automated backups for managed SQL
Server instances, establish AWS Managed Microsoft AD backup
procedures, and set up FSx for Windows File Server backup
policies.
- Establish and document comprehensive recovery procedures
including restoration order and dependencies between
Microsoft services, Active Directory domain controller
recovery, SQL Server Always On Availability Group
restoration, Exchange Database Availability Group recovery,
and SharePoint farm restoration procedures.
- Schedule regular recovery testing and validation exercises
across your Microsoft technologies to check the
effectiveness of the comprehensive data accessibility
strategy, including cross-service dependency validation and
disaster recovery scenario testing.

## Resources

**Related documents:**

- [Migrating
Microsoft SQL Server databases to the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/welcome.html)
- [Optimize
SQL Server backup strategies](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-backup.html)
- [How
to simplify Microsoft SQL Server backup using AWS Backup and
VSS](https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/)
- [Automating
SQL Server Point-in-Time Recovery Using EBS Snapshots](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-point-in-time-recovery-using-ebs-snapshots/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel01-bp03.html*

---

# MSFTREL02 — Workload architecture and availability

**Pillar**: Reliability  
**Best Practices**: 2

---

# MSFTREL02-BP01 Implement comprehensive monitoring for potential failures across the application, AWS infrastructure, and network connectivity

Monitoring your Microsoft application, AWS resources, and network
connectivity enables prompt responses to both actual and potential
failures, enhancing overall system reliability.

**Desired outcome:** Comprehensive
monitoring across the Microsoft application, AWS infrastructure, and
network components will enable early detection of issues and prompt
response to potential failures, optimizing system reliability and
performance.

**Common anti-patterns:**

- Only responding to issues after they cause significant
disruptions, rather than proactively monitoring for potential
problems.
- Monitoring individual components in isolation without
considering the interconnected nature of the application,
infrastructure, and network.
- Focusing monitoring efforts solely on the application layer
while neglecting AWS infrastructure and network connectivity
monitoring.

**Benefits of establishing this best
practice:**

- Comprehensive monitoring enables quick identification and
resolution of issues, reducing downtime and enhancing overall
system stability.
- Continuous monitoring provides valuable insights into system
behavior, allowing for data-driven optimizations and resource
allocation.
- Proactive monitoring reduces the time and resources spent on
troubleshooting, allowing IT teams to focus on strategic
initiatives rather than firefighting.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by identifying critical monitoring metrics across each layer
(application, infrastructure, and network) and implement a primary
monitoring solution like Amazon CloudWatch. Set up custom metrics
and dashboards for Microsoft application-specific monitoring,
configure detailed AWS resource monitoring, and establish network
connectivity checks.

Set up automated alerting and aggregate logs. Define clear
thresholds and escalation procedures, and implement automated
responses where appropriate.

Regularly review and refine your monitoring parameters to maintain
the effectiveness of the monitoring strategy.

### Implementation steps

- Define and configure essential metrics and alarms for
Microsoft workloads with thresholds appropriate to your
specific environment and SLA requirements, including:

SQL Server performance monitoring (CPU utilization,
memory availability, deadlock detection, backup status)
- Active Directory health checks (authentication failures,
replication status, SYSVOL synchronization)
- IIS or .NET application monitoring (application pool
health, HTTP error rates, worker process status)
- Windows system alerts (disk space, memory utilization,
critical service status)
- AWS infrastructure monitoring for underlying EC2, EBS,
and network components

- Create consolidated dashboards for unified visibility across
your monitored components.
- Set up topics and subscription endpoints for automated
alerting based on predefined thresholds.
- Implement centralized logging and configure log metric
filters.
- Establish automated remediation actions in response to
specific alarm conditions.

## Resources

**Related documents:**

- [Monitor
workload resources](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/monitor-workload-resources.html)
- [Designing
and implementing logging and monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/welcome.html)

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon Simple Notification Service](https://aws.amazon.com/sns/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel02-bp01.html*

---

# MSFTREL02-BP02 Develop a strategic plan for quickly reinstating service availability during outages

Microsoft workloads require specialized disaster recovery strategies
due to their unique architectural dependencies and state management
requirements. SQL Server Always On Availability Groups, Active
Directory domain controllers, Exchange Database Availability Groups,
and Windows Failover Clusters each have specific recovery procedures
that differ from generic cloud workload restoration, requiring
tailored approaches for rapid service reinstatement.

**Desired outcome:** Implement a
comprehensive service restoration strategy specifically designed for
Microsoft workloads that includes automated recovery procedures for
SQL Server Always On configurations, Active Directory hybrid
scenarios, and Windows-based clustering services. This plan should
use AWS Elastic Disaster Recovery (DRS) for block-level replication
while addressing Microsoft-specific challenges such as cluster
reformation, domain controller restoration, and
application-consistent recovery.

**Common anti-patterns:**

- Treating Microsoft workloads as generic applications during DR
planning, failing to account for Active Directory dependencies,
SQL Server cluster requirements, or Windows-specific services
that require specialized recovery procedures.
- Relying on AWS DRS replication alone without planning for
Microsoft cluster reformation, resulting in standalone SQL
Server instances instead of properly configured Always On
Availability Groups at the DR site.

**Benefits of establishing this best
practice:**

- Verifies that complex Microsoft services like SQL Server
clusters and Active Directory maintain their intended
architecture and functionality after disaster recovery events.
- Pre-planned procedures for reforming Windows Failover Clusters
and reestablishing Always On Availability Groups minimize manual
intervention and potential errors during critical recovery
operations.
- Maintains integration between on-premises Active Directory and
AWS-hosted domain controllers, preserving authentication
services and trust relationships during outages.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop Microsoft workload-specific disaster recovery procedures
that address SQL Server Always On Availability Groups restoration
using AWS DRS, Active Directory domain controller recovery with
proper site configuration, and Windows Failover Cluster
reformation at DR sites.

Implement AWS Backup for Active Directory System State backups and
configure cross-region replication for critical Microsoft
services.

Establish automated procedures for reestablishing trust
relationships, cluster quorum, and application dependencies
specific to Microsoft environments.

### Implementation steps

- Configure AWS Elastic Disaster Recovery (DRS) for SQL Server
Always On primary nodes with plans for cluster reformation
and secondary replica establishment at the DR site.
- Implement Active Directory disaster recovery using AWS DRS
for domain controllers combined with AWS Backup for System
State backups, providing a proper site and subnet
configuration for hybrid scenarios.
- Establish Windows Failover Cluster recovery procedures
including shared storage configuration using Amazon FSx for Windows File Server and cluster quorum reestablishment.
- Create automated runbooks for Microsoft-specific recovery
tasks including SQL Server Always On listener
reconfiguration, Active Directory trust relationship
validation, and Exchange Database Availability Group
restoration.
- Configure cross-Region backup strategies for Microsoft
workloads using AWS Backup with application-consistent
snapshots and coordinate with AWS DRS replication schedules.
- Implement regular testing procedures that validate Microsoft
service dependencies, cluster functionality, and hybrid
Active Directory connectivity after DR scenarios.

## Resources

**Related documents:**

- [Set
up high availability for SQL Server at DR site using AWS
Elastic Disaster Recovery](https://aws.amazon.com/blogs/modernizing-with-aws/set-up-high-availability-for-sql-server-at-dr-site-using-aws-elastic-disaster-recovery/)
- [Hybrid
Active Directory disaster recovery solutions on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/hybrid-active-directory-disaster-recovery-cyber-resiliency-and-high-availability-solutions-on-aws/)
- [Choose
a high availability and disaster recovery solution](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-hadr.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel02-bp02.html*

---

# MSFTREL03 — Monitoring and incident response

**Pillar**: Reliability  
**Best Practices**: 3

---

# MSFTREL03-BP01 Use Microsoft logs for incident analysis

Microsoft workloads generate rich diagnostic information through
specialized logging systems that provide deeper visibility into
application behavior, security events, and system performance than
standard infrastructure monitoring alone. These Microsoft log
sources offer unique insights into Active Directory authentication
patterns, SQL Server performance bottlenecks, IIS application
errors, and Windows system events that are essential for
comprehensive incident analysis and root cause identification.

**Desired outcome:** The
implementation of comprehensive incident analysis should result in a
detailed incident timeline constructed from CloudWatch and diverse
Microsoft log sources including categorized Windows Event Logs
(System, Security, Application events), Active Directory
authentication and directory service logs, SQL Server operational
and audit logs, IIS web server logs, Exchange messaging logs, and
SharePoint service logs, accompanied by thorough post-incident
documentation. Infrastructure improvements, derived from root cause
analysis, should be automated through infrastructure as code and
systematically deployed through AWS Systems Manager, providing for
consistent security patch management and configuration updates
across your Windows instances.

**Common anti-patterns:**

- Reactive manual patching and configuration changes without
proper documentation or version control, leading to inconsistent
Windows environments and untraceable security vulnerabilities.
- Neglecting to collect or analyze Windows Event Logs (or general
logs) during incidents, resulting in incomplete incident
understanding and recurring issues due to unidentified root
causes.
- Implementing infrastructure changes directly through the AWS Management Console instead of infrastructure as code, causing configuration
drift and making it impossible to reliably replicate or roll
back environment changes.

**Benefits of establishing this best
practice:**

- Systematic log analysis and documented post-mortems enable
faster, more effective resolution of future incidents and reduce
mean time to recovery (MTTR).
- Infrastructure as code (IaC) creates reproducible,
version-controlled environment configurations, eliminating
manual errors and configuration drift.
- Centralized patch management through AWS Systems Manager
maintains security standards across Windows instances while
reducing operational overhead.
- ßComprehensive documentation and standardized runbooks preserve
institutional knowledge, enabling better team collaboration and
reducing dependency on specific individuals.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Review Amazon CloudWatch and comprehensive Microsoft log sources
to analyze incidents, including: - Windows event logs (system,
security, application, setup, and forwarded events) - Active
Directory logs (security events, directory service logs, DNS
server logs) - SQL Server logs (error logs, agent logs, audit
logs, transaction logs) - IIS or .NET logs (access logs, error
logs, ASP.NET application logs) - Exchange Server logs (message
tracking, protocol logs, connectivity logs) - SharePoint ULS
(Unified Logging Service) logs.

Document findings in a post-incident report covering root cause,
impact, and fixes. Update infrastructure code (using AWS CloudFormation or AWS CDK) with improvements and revise Windows
configurations. Automate future security updates using AWS Systems Manager.

Begins with establishing a robust logging strategy using
CloudWatch and Windows event logs. A standardized post-incident
template should include sections for incident timeline, root cause
analysis, impact assessment, and remediation steps.

Migrate infrastructure to infrastructure as code using AWS CloudFormation or AWS CDK, incorporating lessons learned from
incidents. Configure AWS Systems Manager to automate regular
security patching and configuration updates across Windows
instances, maintaining consistent application of security
policies. Runbooks require regular review and updates to reflect
the latest best practices and incident response procedures.

### Implementation steps

- Configure comprehensive logging through CloudWatch and
Windows Event Logs, establishing appropriate retention
periods and log analysis workflows.
- Create standardized templates for incident documentation,
including post-incident analysis, root cause identification,
and remediation tracking.
- Develop infrastructure as code templates using
CloudFormation or CDK to manage and version control your
infrastructure components.
- Set up AWS Systems Manager for automated patch management
and configuration updates across Windows instances.
- Establish regular review cycles for runbooks and
documentation to maintain accuracy and incorporate new
learnings from incidents.

## Resources

**Related documents:**

- [Run
an automated operation powered by Systems Manager
Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-simple-automations.html)
- [Quick
Start: Enable your Amazon EC2 instances running Windows Server 2016 to send logs to CloudWatch Logs using the CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/QuickStartWindows2016.html)
- [Monitoring
Windows services with Amazon CloudWatch](https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/)

**Related tools:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel03-bp01.html*

---

# MSFTREL03-BP02 Establish a structured review process that combines insights from both AWS and Microsoft monitoring tools

Document lessons learned in a centralized knowledge base, update
incident response playbooks, and conduct regular tabletop exercises
to validate improvements. Configure automated reporting to track
incident metrics and measure the effectiveness of implemented
changes. Regular reviews of Windows security baselines and AWS
Well-Architected Framework improve your alignment with best
practices.

**Desired outcome:** The integration
of AWS Security Hub CSPM and Microsoft monitoring tools should provide
unified visibility while maintaining documented processes and
automated reporting to maintain continuous security improvement and
adherence to established standards.

**Common anti-patterns:**

- Siloed monitoring approaches where AWS and Microsoft tools are
used independently, creating blind spots and delayed incident
response.
- Unorganized documentation of incidents and lessons learned
without a structured knowledge base, leading to repeated issues
and inconsistent security practices.

**Benefits of establishing this best
practice:**

- Enhanced visibility across hybrid environments, enabling faster
threat detection and response.
- Improved operational efficiency through centralized knowledge
management and automated reporting.
- Consistent alignment with industry best practices, reducing
security risks and regulatory gaps.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Integrate AWS Security Hub CSPM with existing Microsoft monitoring
tools through APIs and automated workflows. Define standardized
documentation templates and establish a regular review cadence for
updating the knowledge base.

Configure automated reporting dashboards that combine metrics from
both platforms, and schedule quarterly tabletop exercises to
validate the integrated monitoring approach.

### Implementation steps

- Configure AWS Security Hub CSPM and enable integration with
Microsoft monitoring tools through APIs.
- Establish a centralized knowledge base system for
documenting incidents and lessons learned.
- Set up automated reporting workflows to track cross-platform
security metrics.
- Create standardized templates for incident documentation and
response procedures.
- Implement regular review cycles for security baselines and
Well-Architected alignment.
- Schedule quarterly tabletop exercises to validate monitoring
effectiveness and response procedures.

## Resources

**Related documents:**

- [Understanding
security standards in Security Hub CSPM CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-view-manage.html)
- [Govern
Microsoft workloads using the myApplications dashboard on
AWS](https://aws.amazon.com/blogs/modernizing-with-aws/govern-microsoft-workloads-using-the-myapplications-dashboard-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel03-bp02.html*

---

# MSFTREL03-BP03 Implement automated feedback loops

Automated feedback loops are critical for Microsoft workloads due to
their complex interdependencies and the need for continuous
monitoring of performance patterns, security posture, and
operational effectiveness. Microsoft environments require systematic
approaches to identify trends, measure improvement initiatives, and
translate monitoring investments into actionable insights for
maintaining system reliability and security.

**Desired outcome:** The
implementation of automated feedback loops establishes comprehensive
monitoring and continuous improvement mechanisms through Amazon CloudWatch dashboards, automated vulnerability assessments, and
metrics-driven compliance reporting, enabling data-driven
decision-making and proactive risk management for Windows workloads
on AWS.

**Common anti-patterns:**

- Relying solely on manual monitoring and reactive troubleshooting
instead of implementing automated alerts and dashboards
- Conducting unplanned or inconsistent vulnerability assessments
without a standardized schedule or automated scanning process
- Failing to maintain a prioritized improvement backlog,
addressing issues randomly rather than based on quantifiable
risk metrics and business impact

**Benefits of establishing this best
practice:**

- Custom CloudWatch dashboards provide real-time insights into
system performance and security patterns, enabling faster issue
detection and resolution.
- Regular automated vulnerability assessments help identify and
address potential threats before they can be exploited,
improving overall security posture.
- A prioritized backlog based on risk and business impact
allocates resources efficiently to address the most critical
issues first.
- Automated compliance reporting using CloudWatch metrics and
alarms streamlines the audit process and helps maintain ongoing
regulatory adherence with less manual effort.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement automated feedback loops by creating custom CloudWatch
dashboards to monitor patterns and resolution times. Set up
regular vulnerability assessments for EC2 instances running
Windows workloads, and maintain a continuous improvement backlog
prioritized by risk and business impact. Use CloudWatch metrics
and alarms to monitor the effectiveness of implemented controls
and automate compliance reporting.

Begin by creating custom dashboards that display key metrics for
Windows workloads. Next, establish automated vulnerability
scanning for EC2 instances on a regular schedule. Develop a
process for maintaining and prioritizing a continuous improvement
backlog based on identified risks and business impact. Finally,
configure CloudWatch metrics and alarms to monitor control
effectiveness and automate compliance reporting, verifying that
each component works together in a cohesive feedback loop.

### Implementation steps

- Set up specialized CloudWatch dashboards for Microsoft
workloads including:

SQL Server metrics (connection pools, deadlocks, wait
statistics, backup status)
- IIS or .NET performance (request queues, application
pool health, session state)
- Active Directory monitoring (authentication failures,
replication status, LDAP queries)
- Windows system performance (memory usage, disk I/O,
Event Logs)
- Exchange or SharePoint service health dashboards.

- Focus on key Windows Performance Counters to drive continual
improvement, such as:

\Memory\Available MBytes
- \Processor(_Total)\% Processor Time
- \PhysicalDisk(_Total)\Avg. Disk Queue Length
- Critical Windows Event Log patterns (Security Event ID
4625 for failed logons, System Event ID 6008 for
unexpected shutdowns)
- Application-specific metrics like
\SQLServer:General Statistics\User Connections
and
\Web Service(_Total)\Current Connections

- Enable Amazon Inspector for automated vulnerability
assessments on Windows EC2 instances, which automatically
discovers supported Windows instances and performs
continuous scanning every 6 hours by default. Configure
custom scan schedules using SSM associations and use
Inspector's integration with Systems Manager to assess
operating system vulnerabilities, software packages, and
network reachability for comprehensive security monitoring.
- Create and maintain a centralized improvement backlog system
with clear risk scoring and business impact criteria.
- Implement alarms with appropriate thresholds for identified
key performance and security metrics.
- Establish automated compliance reporting workflows using
metrics and AWS reporting tools.
- Develop documentation and runbooks for responding to
automated alerts and managing the continuous improvement
process.

## Resources

**Related documents:**

- [What
is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel03-bp03.html*

---

# MSFTREL04 — Automation and recovery management

**Pillar**: Reliability  
**Best Practices**: 1

---

# MSFTREL04-BP01 Use Amazon EC2 Auto Scaling in combination with Application Auto Scaling

Microsoft workloads often experience variable demand patterns that
require dynamic resource scaling to maintain performance and cost
efficiency. Applications like SharePoint farms, SQL Server
databases, and .NET web applications face fluctuating user loads,
batch processing requirements, and seasonal traffic variations that
make static resource provisioning ineffective and costly.

**Desired outcome:** Implement
automated scaling mechanisms that combine instance-level and
application-level auto scaling capabilities to optimize resource
utilization. Configure predictive scaling using historical data and
machine learning to anticipate capacity needs, while maintaining
regulatory requirements through dedicated host allocation. Automate
capacity management through system tooling that responds to
monitoring metrics and scheduled events.

**Common anti-patterns:**

- Relying on human intervention to adjust resources in response to
demand changes, leading to slow reactions and potential over- or
under-provisioning.
- Maintaining a fixed resource capacity based on peak demand
expectations, resulting in wasted resources during low-demand
periods and potential shortages during unexpected spikes.
- Focusing solely on infrastructure scaling without considering
the need for application-level scaling, potentially leading to
bottlenecks in database connections, caching, or other
application components.

**Benefits of establishing this best
practice:**

- Dynamically adjusts resource capacity to actual demand, reducing
waste from over-provisioning while reducing performance issues
from under-provisioning.
- Automatically responds to changes in workload patterns and
system failures, maintaining service availability without manual
intervention.
- Uses historical data and machine learning to anticipate and
prepare for demand spikes before they occur, reducing reactive
scaling delays.
- Maintains licensing and regulatory requirements through
controlled scaling of dedicated resources while still achieving
operational efficiency.
- Reduces administrative overhead through automated capacity
management, freeing up teams to focus on higher-value activities
while providing consistent performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Configure auto scaling groups to dynamically adjust compute
resources based on demand patterns. Enable predictive scaling
using historical metrics to proactively manage capacity before
peak loads occur. For applications with specific licensing
requirements, use dedicated hosts with auto scaling policies to
maintain adherence. Implement automation tools to handle routine
capacity management tasks, using monitoring alerts and scheduled
actions to control resource scaling.

Begin by establishing baseline metrics and performance thresholds
for both infrastructure and application components. Configure
scaling policies that combine predictive and dynamic adjustments,
using historical data to anticipate capacity needs while
maintaining real-time responsiveness to unexpected changes. Set up
monitoring and alerting to track scaling activities, and implement
gradual scaling steps to avoid resource thrashing. Document
scaling decisions and regularly review performance data to refine
thresholds and policies, providing optimal resource utilization
while maintaining service levels and regulatory requirements.

### Implementation steps

- Configure EC2 Auto Scaling groups with appropriate launch
templates and scaling policies for Windows instances,
including SQL Server and IIS workloads.
- Enable predictive scaling using AWS Auto Scaling with
machine learning forecasts, incorporating Microsoft workload
patterns and licensing considerations for dedicated hosts.
- Set up Amazon CloudWatch Application Insights to monitor
.NET and SQL Server applications, automatically detecting
anomalies and providing application-level metrics for
scaling decisions across IIS, SQL Server, and application
servers.
- Create CloudWatch alarms and custom metrics for Microsoft
applications including SQL Server connection counts, IIS
request queues, and .NET application performance counters to
trigger scaling actions, using Application Insights
automated dashboards.
- Implement application-level scaling automation for SQL
Server Always On Availability Groups, IIS worker process
scaling, and SharePoint farm expansion using Systems Manager
automation documents triggered by Application Insights
events.
- Configure session state management and connection pooling
strategies to support horizontal scaling of .NET
applications and SQL Server workloads across multiple
instances, using Application Insights correlation data for
optimization.

## Resources

**Related documents:**

- [Predictive
scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [What
is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Accelerate
Amazon EC2 Auto Scaling for Microsoft Windows workloads](https://aws.amazon.com/blogs/modernizing-with-aws/accelerate-amazon-ec2-auto-scaling-for-microsoft-windows-workloads/)
- [Automatically
scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)

**Related tools:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Auto
Scaling launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)
- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel04-bp01.html*

---

# MSFTREL05 — Automation and recovery management

**Pillar**: Reliability  
**Best Practices**: 4

---

# MSFTREL05-BP01 Implement disaster recovery automation

Disaster recovery (DR) automation is essential for Microsoft
workloads due to their complex interdependencies and stateful
nature. Microsoft environments often involve intricate relationships
between Active Directory, SQL Server databases, file services, and
application servers that require coordinated recovery procedures to
maintain business continuity and data integrity.

**Desired outcome:** An effective
disaster recovery implementation should automate the recovery of
Microsoft workloads using appropriate tools, providing for
consistent configuration restoration and automated traffic failover
while meeting defined RTO and RPO objectives.

**Common anti-patterns:**

- Manual DR procedures and runbooks that rely on human
intervention during critical recovery events, leading to
extended downtimes and potential configuration errors during
restoration.
- Maintaining inconsistent Windows Server and SQL Server
configurations between primary and DR environments, resulting in
failed recoveries or application compatibility issues
post-failover.
- Using single-region deployments for critical Microsoft workloads
without automated DNS failover mechanisms, creating a single
point of failure and complicating the recovery process during
regional outages.

**Benefits of establishing this best
practice:**

- Reduced recovery time objective (RTO) through automated DR
procedures, minimizing business disruption during outages.
- Improved consistency and reliability in recovering Microsoft
workloads, eliminating human errors associated with manual
recovery processes.
- Enhanced scalability and flexibility in managing DR across
multiple regions, allowing for easier testing and updates to
recovery plans.
- Cost optimization by using AWS services for DR, reducing the
need for dedicated standby infrastructure and manual management
overhead.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement automated disaster recovery for Microsoft workloads
using Infrastructure as Code templates and automation runbooks.
Use tools like AWS CloudFormation for infrastructure provisioning,
and configuration management solutions to maintain consistent
Windows Server and SQL Server setups.

Develop runbooks to automate recovery steps, including instance
launch and configuration restoration. Configure DNS failover and
load balancers for automatic traffic redistribution during DR
events.

Regularly test failover procedures and store code and
configurations in version control, providing robust security
across environments.

Implement disaster recovery automation by creating
infrastructure-as-code templates and automated runbooks for
orchestrating recovery procedures. Integrate DNS failover and load
balancing for traffic management. Develop scripts to maintain
consistent configurations across environments.

Regularly test and refine DR processes, and provide documentation
and version control to support ongoing improvements.

### Implementation steps

- Define DR requirements including RTO and RPO objectives, and
create CloudFormation templates to codify Microsoft workload
infrastructure, including AWS Managed Microsoft AD
multi-region replication, SQL Server Always On Availability
Groups, and FSx for Windows File Server cross-region backup
strategies.
- Develop Systems Manager Automation runbooks for
orchestrating recovery procedures, including Windows
instance restoration using AWS DRS (supporting Windows
Server 2008 R2 through 2022), SQL Server Always On failover
automation, and FSx file system recovery with DataSync for
cross-region data replication.
- Configure Amazon Route 53 DNS failover policies and
Application Load Balancers for automated traffic routing
between primary and DR regions, and integrate with
Windows-based authentication systems and SQL Server
connection string updates during failover events.
- Create and test automated scripts for maintaining Windows
Server and SQL Server configurations across environments,
including Always On Distributed Availability Groups for
cross-Region SQL replication and AWS Managed Microsoft AD
trust relationships between Regions.
- Implement monitoring and alerting to trigger automated DR
processes when failure conditions are detected, including
SQL Server Always On dashboard monitoring, FSx performance
metrics, and AWS Managed Microsoft AD health checks across
regions.
- Establish regular DR testing schedule and documentation
procedures to validate and improve recovery automation,
including SQL Server Always On failover testing, FSx restore
validation, and Microsoft workload recovery scenarios.

## Resources

**Related documents:**

- [Disaster
recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [Choose
a high availability and disaster recovery solution](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-hadr.html)
- [On-premises
DR to AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/on-prem-dr-to-aws.html)
- [DR
for cloud-native workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/dr-cloud-native.html)
- [Configuring
DNS failover](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/dns-failover-configuring.html)

**Related tools:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/)
- [Amazon Route 53](https://aws.amazon.com/route53/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel05-bp01.html*

---

# MSFTREL05-BP02 Implement backup automation

Backup automation is critical for Microsoft workloads running on
AWS, maintaining consistent data protection without manual
intervention. Microsoft applications like SQL Server, Exchange, and
SharePoint require application-aware backup strategies that maintain
data integrity and support reliable recovery scenarios.

**Desired outcome:** Implement
automated, application-consistent backups for Microsoft workloads on
AWS to provide for reliable data protection, reduce manual effort,
and enhance disaster recovery capabilities, ultimately improving
system resilience and recoverability.

**Common anti-patterns:**

- Relying solely on manual, unplanned backups of Windows instances
and databases, leading to inconsistent backup schedules, missed
backups, and potential data loss during critical application
states.
- Using basic snapshot mechanisms without VSS integration,
resulting in crash-inconsistent backups that may not properly
capture the state of running applications and could cause data
corruption during restoration.

**Benefits of establishing this best
practice:**

- Application-consistent backups captures data accurately,
including in-memory and in-flight transactions, which reduces
the risk of data corruption or loss.
- Automated backup processes reduce manual effort, minimize human
errors, and free up IT staff to focus on more strategic tasks.
- Regular, automated backups with cross-region replication provide
a robust foundation for quick and reliable recovery in case of
system failures or disasters, minimizing downtime and data loss.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Configure automated backups for servers, databases, and storage
volumes with defined schedules and retention policies. Enable
application-consistent snapshots for data integrity, implement
backup verification, and set up cross-Region copies for
resilience. This strategy provides for comprehensive protection
while maintaining application and file system consistency.

Configure AWS Backup with automated plans targeting Windows
workloads and setting appropriate retention policies. Start with
critical systems, establish backup windows during off-peak hours,
and implement cross-region replication for essential workloads.
Test backup integrity and recovery procedures regularly, and
monitor backup success rates through AWS Backup reports.

### Implementation steps

- Define backup requirements and policies for SQL Server
databases (EC2 and RDS), Active Directory domain
controllers, Exchange Server mailbox databases, FSx for Windows File Server, SharePoint farms, and Windows file
server volumes, considering RPO/RTO requirements for each
service.
- Configure AWS Backup plans with VSS-aware schedules for SQL
Server transaction log backups, AD System State backups,
Exchange VSS backups, FSx automatic backups, and SharePoint
farm-level backups with appropriate retention rules. For
advanced Microsoft workload backup scenarios, consider AWS
Partner solutions available in AWS Marketplace.
- Set up cross-Region backup replication for critical SQL
Server databases, AD domain controllers, Exchange databases,
and FSx file systems to maintain disaster recovery
capabilities. Additionally, configure cross-region
replication for customer-managed S3 buckets containing
backup data to enhance resilience.
- Implement automated backup integrity checks using SQL Server
CHECKDB, AD database verification, Exchange database
consistency checks, FSx backup validation, and SharePoint
content database consistency checks.
- Establish and test recovery procedures for SQL Server
point-in-time recovery, AD authoritative restore, Exchange
mailbox recovery, FSx file system restoration, SharePoint
farm recovery, and Windows file server volume recovery
scenarios.

## Resources

**Related documents:**

- [Create
a backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)
- [Create
Windows VSS backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html)
- [Application-consistent
backup for Windows application on Amazon EC2 with AWS Backup](https://aws.amazon.com/blogs/storage/application-consistent-backup-for-windows-application-on-amazon-ec2-with-aws-backup/)
- [How
to simplify Microsoft SQL Server backup using AWS Backup and
VSS](https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/)
- [Automating
SQL Server Point-in-Time Recovery Using EBS Snapshots](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-point-in-time-recovery-using-ebs-snapshots/)

**Related tools:**

- [AWS Backup](https://aws.amazon.com/backup/)
- [Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel05-bp02.html*

---

# MSFTREL05-BP03 Implement self-healing procedures

Establish automated remediation capabilities that can detect,
diagnose, and resolve common issues in Microsoft workloads without
human intervention. Self-healing procedures reduce mean time to
recovery (MTTR) and minimize the impact of transient failures on
business operations.

**Desired outcome:** Implement
automated self-healing procedures to proactively detect and
remediate common issues in Microsoft workloads, providing for
minimal downtime through automated instance recovery, health-based
reboots, and configuration management.

**Common anti-patterns:**

- Waiting for human operators to detect and respond to system
failures during off-hours.
- Implementing reactive fixes without addressing root causes
through automation.
- Creating complex automation that requires extensive maintenance
and troubleshooting.
- Over-automating without proper testing, leading to cascading
failures.

**Benefits of establishing this best
practice:**

- Significantly reduced mean time to recovery (MTTR) for common
failure scenarios.
- Improved availability during off-hours when human operators may
not be immediately available.
- Consistent and predictable response to system issues, reducing
human error.
- Enhanced operational efficiency by freeing teams to focus on
strategic initiatives rather than routine maintenance.
- Improved adherence to service level agreements (SLAs) through
automated response capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing self-healing procedures for Microsoft workloads,
consider the balance between automation sophistication and
operational complexity. Start with well-understood, low-risk
scenarios before expanding to more complex remediation actions.

**Key considerations for
customers**

- **Scope and prioritization:**
Begin by identifying the most common and impactful failure
scenarios in your Microsoft workloads. Focus on issues that
occur frequently, have clear remediation steps, and pose
minimal risk when automated. Examples include service
restarts, disk space cleanup, and basic connectivity issues.
- **Testing and validation:**
Thoroughly test automated remediation actions in
non-production environments. Establish clear success criteria
and rollback procedures. Consider implementing gradual
rollouts and canary deployments for automation changes.
- **Monitoring and alerting
strategy:** Design monitoring that can distinguish
between symptoms and root causes. Avoid creating automation
that treats symptoms without addressing underlying issues, as
this can mask systemic problems.
- **Impact scope control:**
Implement safeguards to avoid automated actions from causing
widespread impact. Use circuit breakers, rate limiting, and
approval workflows for high-risk remediation actions.
- **Documentation and knowledge
transfer:** Maintain clear documentation of automated
procedures, including trigger conditions, actions taken, and
escalation paths. Verify that team members understand when and
how automation will intervene.

### Implementation steps

- Analyze historical incidents to identify the most common and
impactful issues. Prioritize scenarios with clear
remediation steps and low automation risk.
- Configure Amazon CloudWatch alarms and custom metrics to
detect failure conditions. Verify that monitoring can
differentiate between transient issues and persistent
problems.
- Create AWS Systems Manager Automation documents for each
remediation scenario. Test thoroughly in non-production
environments with various failure conditions.
- Start with simple, low-risk actions like service restarts.
Gradually expand to more complex scenarios like instance
replacement or database failover as confidence builds.
- Configure specific Microsoft workload automation:

Deploy auto-recovery for EC2 instances running Windows
Server.
- Set up automated instance reboots based on health checks
for IIS and other Windows services.
- Configure automatic failover for SQL Server Always On
Availability Groups.
- Implement automated patch management through AWS Systems Manager Patch Manager.
- Use State Manager for configuration drift correction on
Windows systems.
- Active Directory and DNS automation:

Automatically restart Active Directory Domain
Services when authentication failures exceed
thresholds.
- Reset DNS service when name resolution failures are
detected.
- Trigger domain controller health checks and
automatic promotion of backup DCs.

- IIS and web application remediation:

Restart application pools when memory usage exceeds
defined limits.
- Clear IIS logs when disk space is low.
- Reset worker processes experiencing high CPU
utilization.
- Automatically recycle application pools based on
request failure rates.

- SQL Server specific automation:

Restart SQL Server services when connection timeouts
increase.
- Automatically shrink transaction logs when they
exceed size thresholds.
- Trigger index maintenance when fragmentation levels
are high.
- Reset SQL Server Agent jobs that fail due to
transient issues.

- Windows service and process management:

Restart Windows services that have stopped
unexpectedly.
- Kill and restart hung processes based on CPU or
memory thresholds.
- Clear Windows event logs when they reach capacity
limits.
- Reset network adapters when connectivity issues are
detected.

- File system and storage remediation:

Automatically clean temporary files when disk space
is low.
- Compress old log files to free up storage space.
- Move archived data to lower-cost storage tiers.
- Reset file permissions when access issues are
detected.

- Performance and resource optimization:

Automatically scale EC2 instances based on
performance metrics.
- Clear memory caches when system performance
degrades.
- Restart services consuming excessive resources.
- Trigger garbage collection for .NET applications
experiencing memory leaks.

- Monitor automation effectiveness and adjust thresholds based
on real-world performance. Implement logging and metrics to
track automation success rates.

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [Working
with SSM Agent on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-windows.html)
- [Patching
applications released by Microsoft on Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-patching-windows-applications.html)
- [Use
AWS Systems Manager to enable CloudWatch memory metrics for
Windows Server Amazon EC2 instances](https://aws.amazon.com/blogs/modernizing-with-aws/use-aws-systems-manager-to-enable-cloudwatch-memory-metrics-for-windows-server-amazon-ec2-instances/)

**Related tools:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel05-bp03.html*

---

# MSFTREL05-BP04 Implement testing automation

Establish comprehensive automated testing frameworks that
continuously validate the reliability and recoverability of
Microsoft workloads on AWS. Testing automation verifies that
disaster recovery (DR) procedures, backup systems, and failover
mechanisms work as expected when needed, reducing the risk of
surprises during actual incidents.

**Desired outcome:** Implementing
automated testing for disaster recovery processes maintains
continuous validation of recovery mechanisms, backup integrity, and
failover procedures. This approach enables regular verification of
system resilience, enhancing overall reliability and minimizing
manual intervention during critical recovery operations.

**Common anti-patterns:**

- Testing only during scheduled maintenance windows or annual DR
exercises, missing critical issues that develop over time.
- Focusing solely on infrastructure testing while ignoring
application-level validation and data integrity checks.
- Creating tests that don't reflect real-world failure scenarios
or business-critical workflows.
- Implementing testing automation without proper validation of
Microsoft-specific dependencies and licensing requirements.

**Benefits of establishing this best
practice:**

- Continuous validation of Microsoft workload recovery
capabilities, maintaining business continuity when failures
occur.
- Early detection of configuration drift, licensing issues, and
dependency problems that could impact recovery.
- Reduced recovery time objectives (RTO) through proven, tested
procedures that work reliably under pressure.
- Enhanced confidence in disaster recovery capabilities, enabling
better business decision-making around risk tolerance.
- Compliance validation for Microsoft licensing and regulatory
requirements during recovery scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Microsoft workloads on AWS require specialized testing approaches
that account for Windows-specific dependencies, Active Directory
integration, SQL Server clustering, and Microsoft licensing
considerations. Effective testing automation must validate not
just infrastructure recovery, but also application functionality,
data consistency, and regulatory requirements.

**Key considerations for Microsoft workload
testing**

- **Windows-specific validation
requirements:** Microsoft workloads have unique
dependencies that must be tested, including Windows services
startup order, registry configurations, Windows
authentication, and domain trust relationships. Testing must
verify that these components function correctly after recovery
operations.
- **Active Directory and authentication
testing:** Automated tests should validate domain
controller functionality, DNS resolution, Kerberos
authentication, and group policy application. This includes
testing domain trust relationships, LDAP connectivity, and
certificate services recovery.
- **SQL Server and database
validation:** Database recovery testing must go
beyond simple connectivity checks to include transaction log
integrity, Always On Availability Group functionality, SQL
Server Agent jobs, and linked server connections. Validate
backup chain integrity and point-in-time recovery
capabilities.
- **Microsoft licensing
compliance:** Automated testing should verify that
recovered systems maintain proper licensing adherence,
including Windows Server activation, SQL Server licensing
validation, and CAL (Client Access License) requirements.
- **Application-specific
testing:** Test Microsoft applications like
SharePoint, Exchange, or custom .NET applications to verify
that they function correctly after recovery, including service
dependencies, configuration settings, and data access
patterns.

### Implementation steps

- Catalog your Windows services, Active Directory
dependencies, SQL Server components, and Microsoft
applications. Identify critical recovery scenarios specific
to your Microsoft environment.
- Create test cases that validate Windows-specific
functionality, including:

Domain controller recovery and DNS functionality.
- SQL Server Always On Availability Group failover.
- Windows service startup and dependency chains.
- Active Directory replication and authentication.
- Microsoft application functionality and data access.

- Implement automated testing frameworks:

Use AWS Systems Manager State Manager with PowerShell
DSC to validate Windows configurations post-recovery.
- Create automated scripts to validate database integrity,
backup chain validation, and Always On cluster health.
- Implement automated domain controller health validation,
replication monitoring, and authentication testing.
- Automate testing of critical Windows services, IIS
application pools, and .NET application functionality.

- Configure AWS testing tools:

Use AWS Systems Manager Automation with Windows-specific
runbooks.
- Use AWS Fault Injection Service to test Windows
instance failures, network partitions, and storage
issues.
- Implement Amazon CloudWatch custom metrics for
Microsoft-specific monitoring during tests.

- Establish Microsoft workload-specific validation:

Automate checks for Windows activation status and SQL
Server licensing compliance.
- Validate that recovered systems meet performance
expectations for Microsoft workloads.
- Verify Windows security policies, firewall rules, and
certificate validity post-recovery.
- Implement automated database consistency checks and
application data validation.

- Create comprehensive reporting and alerting:

Generate detailed reports on Microsoft workload recovery
test results.
- Implement alerting for failed tests specific to Windows
and SQL Server components.
- Track compliance metrics for Microsoft licensing and
configuration standards.

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [What
is AWS Fault Injection Service?](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [Working
with SSM Agent on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-windows.html)
- [PowerShell
DSC and AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-powershell-dsc-support.html)
- [SQL
Server on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/SQL_Server.html)

**Related tools:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Fault
Injection Service](https://aws.amazon.com/fis/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Config](https://aws.amazon.com/config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel05-bp04.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
