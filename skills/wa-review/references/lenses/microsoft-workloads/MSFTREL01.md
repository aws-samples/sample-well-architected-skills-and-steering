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
