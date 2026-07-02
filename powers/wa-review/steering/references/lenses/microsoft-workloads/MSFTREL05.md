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
