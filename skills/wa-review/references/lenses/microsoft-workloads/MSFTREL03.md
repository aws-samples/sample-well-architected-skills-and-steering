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
