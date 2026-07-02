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
