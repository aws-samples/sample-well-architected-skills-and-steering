# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 2

---

# MSFTOPS01 — Monitoring and observability

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# MSFTOPS01-BP01 Implement infrastructure monitoring for your Microsoft workload

The implementation of infrastructure monitoring for Microsoft
workloads on AWS will provide comprehensive visibility into system
performance, resource utilization, and application health. This
monitoring solution will detect anomalies in real time, generate
actionable alerts, and enable rapid troubleshooting of issues before
they impact end users. Consider leveraging Microsoft Performance
Counters to cover the basic infrastructure monitoring for your
Microsoft workload servers. Besides operating system and performance
metrics, the counters will be expanded according to the Microsoft
product deployed, such as SQL Server, Internet Information Services
(IIS), Active Directory Federation Services, and others. The
Performance Counters can also be integrated with monitoring
solutions, like Amazon CloudWatch, Amazon Managed Service for Prometheus, and Amazon Managed Grafana.

**Desired outcome:** Establish
comprehensive infrastructure monitoring that provides real-time
visibility into the health and performance of your Microsoft
workload components, enabling proactive issue identification and
resolution while leveraging both Microsoft-native monitoring
capabilities and AWS monitoring services for optimal observability.

**Common anti-patterns:**

- Relying solely on basic system monitoring without leveraging
Microsoft Performance Counters, missing critical
application-specific metrics that could indicate performance
issues or potential failures before they impact users.
- Implementing monitoring in silos without integrating Microsoft
Performance Counters with centralized monitoring solutions,
leading to fragmented visibility and delayed incident response
across the Microsoft workload infrastructure.
- Monitoring only during business hours or reactive monitoring
after issues occur, rather than establishing continuous,
proactive monitoring that can predict and prevent problems
before they affect workload availability.

**Benefits of establishing this best
practice:**

- Enhanced visibility and proactive issue detection through
comprehensive monitoring of both operating system metrics and
Microsoft product-specific performance counters, enabling early
identification of potential problems before they impact business
operations.
- Improved operational efficiency by integrating Microsoft
Performance Counters with AWS monitoring services like Amazon CloudWatch, providing centralized dashboards, automated
alerting, and streamlined incident response processes.
- Better capacity planning and performance optimization through
detailed metrics collection across all Microsoft workload
components, enabling data-driven decisions for resource
allocation and performance tuning.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing comprehensive infrastructure monitoring for Microsoft
workloads requires a strategic approach that combines
Microsoft-native monitoring capabilities with AWS services. Start
by identifying the Microsoft products in your environment and
their specific Performance Counters, then configure collection and
integration with AWS monitoring services. This approach ensures
you capture both standard system metrics and application-specific
indicators that are crucial for maintaining optimal performance
and availability of your Microsoft workloads.

### Implementation steps

- Inventory your Microsoft workload components and identify
relevant Performance Counters for each product (Windows
Server, SQL Server, IIS, and Active Directory).
- Install and configure the Amazon CloudWatch Agent on Windows
instances to collect Performance Counters and system
metrics.
- Configure custom Performance Counter collection for
Microsoft-specific applications and services running in your
environment.
- Set up Amazon CloudWatch dashboards to visualize key
performance metrics and create a centralized monitoring
view.
- Establish Amazon CloudWatch alarms and notifications for
critical performance thresholds and anomaly detection.
- Integrate with Amazon Managed Service for Prometheus and
Amazon Managed Grafana for advanced monitoring and
visualization capabilities.
- Implement automated response mechanisms using AWS Systems Manager Automation for common performance issues.
- Establish regular review processes to evaluate monitoring
effectiveness and adjust thresholds based on workload
behavior.

## Resources

**Related documents:**

- [Recommended
metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/application-insights-recommended-metrics.html)
- [Monitoring
Windows pods with Prometheus and Grafana](https://aws.amazon.com/blogs/containers/monitoring-windows-pods-with-prometheus-and-grafana/)
- [Use
AWS Systems Manager to enable CloudWatch memory metrics for
Windows Server Amazon EC2 instances](https://aws.amazon.com/blogs/modernizing-with-aws/use-aws-systems-manager-to-enable-cloudwatch-memory-metrics-for-windows-server-amazon-ec2-instances/)

**Related tools:**

- [Collect
metrics, logs, and traces using the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
- [Using
Amazon CloudWatch Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
- [Amazon Managed Grafana - Grafana dashboards](https://aws.amazon.com/grafana/)
- [Prometheus
Windows Exporter](https://github.com/prometheus-community/windows_exporter)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops01-bp01.html*

---

# MSFTOPS01-BP02 Implement and collect logging for your Microsoft workload

Set up logs for your Microsoft workload infrastructure and
applications. Windows Event Logs are natively generated by the
Windows operating system and usually by the applications deployed.
Products such as SQL Server and Internet Information Services (IIS)
also provide text logs that can bring insights to observability.
Both Windows Event Logs and custom logs can be collected by Amazon CloudWatch Agent and have them centralized in the Amazon CloudWatch
console. For enhanced security monitoring and analysis, these logs
can be forwarded to Security Information and Event Management (SIEM)
solutions through built-in connectors or AWS service integrations,
enabling real-time security event monitoring, automated threat
detection, compliance reporting, and advanced security analytics.

**Desired outcome:** Establish
comprehensive logging collection and centralization for your
Microsoft workload, providing complete visibility into system
events, application behavior, and security activities while enabling
efficient log analysis, troubleshooting, and compliance reporting
through integrated AWS services and SIEM solutions.

**Common anti-patterns:**

- Relying only on local Windows Event Logs without centralized
collection, making it difficult to correlate events across
multiple systems and delaying incident response during critical
situations.
- Collecting logs without proper retention policies or analysis
capabilities, leading to storage inefficiencies and missed
opportunities to identify patterns or security threats in the
log data.
- Ignoring application-specific logs from Microsoft products like
SQL Server and IIS, missing valuable insights into application
performance, errors, and security events that could indicate
potential issues.

**Benefits of establishing this best
practice:**

- Centralized visibility and faster troubleshooting through
consolidated log collection from all Microsoft workload
components, enabling rapid identification of issues across the
entire infrastructure stack.
- Enhanced security posture by forwarding logs to SIEM solutions
for real-time threat detection, automated security analysis, and
compliance reporting, improving overall security monitoring
capabilities.
- Improved operational efficiency through automated log analysis,
pattern recognition, and alerting capabilities that help
identify recurring issues and optimize system performance
proactively.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing comprehensive logging for Microsoft workloads
requires a systematic approach to collect, centralize, and analyze
logs from multiple sources. Begin by identifying all log sources
in your Microsoft environment, configure the Amazon CloudWatch
Agent for log collection, and establish proper log retention and
analysis processes. This approach ensures you capture critical
events and application behaviors while maintaining efficient log
management and enabling effective troubleshooting and security
monitoring.

### Implementation steps

- Identify all log sources in your Microsoft workload
including Windows Event Logs, SQL Server logs, IIS logs, and
custom application logs.
- Install and configure the Amazon CloudWatch Agent on Windows
instances to collect and forward logs to Amazon CloudWatch Logs.
- Configure log groups and streams in Amazon CloudWatch Logs
with appropriate retention policies based on compliance and
operational requirements.
- Set up log filtering and metric filters to identify critical
events and create automated alerts for important log
patterns.
- Implement log forwarding to SIEM solutions using AWS
services like Amazon Data Firehose or AWS Lambda for
enhanced security analysis.
- Create Amazon CloudWatch Insights queries for efficient log
analysis and troubleshooting across your Microsoft workload
components.
- Establish log monitoring dashboards and automated alerting
for critical events and security incidents.
- Implement log archiving strategies using Amazon S3 for
long-term retention and compliance requirements.

## Resources

**Related documents:**

- [How
do I upload my Windows logs to CloudWatch?](https://repost.aws/knowledge-center/cloudwatch-upload-windows-logs)
- [Amazon EKS: Monitoring](https://docs.aws.amazon.com/eks/latest/best-practices/windows-monitoring.html)
- [Centralized
Logging for Windows Containers on Amazon EKS using Fluent
Bit](https://aws.amazon.com/blogs/containers/centralized-logging-for-windows-containers-on-amazon-eks-using-fluent-bit/)

**Related tools:**

- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [SIEM
on Amazon OpenSearch Service](https://github.com/aws-samples/siem-on-amazon-opensearch-service)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops01-bp02.html*

---

# MSFTOPS01-BP03 Implement Application Performance Monitoring (APM) for your Microsoft workload

Microsoft workloads developed with .NET and SQL technologies should
also have Application Performance Monitoring (APM) implemented.
Amazon CloudWatch Application Insights for .NET and SQL Server can
be used for that purpose. AWS X-Ray can be used as well to improve
traceability over the workload.

**Desired outcome:** Establish
comprehensive Application Performance Monitoring (APM) for your
Microsoft workloads, providing deep visibility into application
behavior, performance bottlenecks, and user experience while
enabling proactive optimization and rapid troubleshooting of .NET
applications and SQL Server databases.

**Common anti-patterns:**

- Monitoring only infrastructure metrics without implementing
application-level monitoring, missing critical insights into
application performance, user experience, and business
transaction flows that could indicate problems before they
affect users.
- Implementing APM tools without proper configuration for
Microsoft-specific technologies, failing to capture important
.NET application metrics, SQL Server performance indicators, and
transaction traces that are essential for effective
troubleshooting.
- Using APM reactively only during incidents rather than
proactively monitoring application performance trends, missing
opportunities to optimize performance and prevent issues before
they impact business operations.

**Benefits of establishing this best
practice:**

- Enhanced application visibility and faster issue resolution
through detailed monitoring of .NET application performance, SQL
Server operations, and end-to-end transaction tracing, enabling
rapid identification and resolution of performance bottlenecks.
- Improved user experience and business outcomes by monitoring
application performance from the user perspective, identifying
slow transactions, and optimizing critical business processes
before they impact customer satisfaction.
- Proactive performance optimization through continuous monitoring
of application metrics, enabling data-driven decisions for code
optimization, database tuning, and infrastructure scaling to
maintain optimal performance.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing Application Performance Monitoring for Microsoft
workloads requires a comprehensive approach that covers both .NET
applications and SQL Server databases. Start by configuring Amazon CloudWatch Application Insights to automatically discover and
monitor your Microsoft applications, then enhance visibility with
AWS X-Ray for distributed tracing. This approach provides
end-to-end visibility into application performance and enables
proactive optimization of your Microsoft workloads.

### Implementation steps

- Enable Amazon CloudWatch Application Insights for your .NET
applications and SQL Server instances to automatically
discover and monitor application components.
- Configure Application Insights to collect custom metrics
specific to your Microsoft workload business logic and
critical transactions.
- Implement AWS X-Ray daemon in your .NET applications to
track requests across distributed components and identify
performance bottlenecks.
- Set up custom dashboards in Amazon CloudWatch to visualize
application performance metrics, error rates, and response
times for critical business transactions.
- Configure automated alerts for application performance
thresholds, error rates, and anomaly detection to enable
proactive issue identification.
- Implement synthetic monitoring using Amazon CloudWatch
Synthetics to continuously test critical application
workflows and user journeys.
- Establish performance baselines and regularly review APM
data to identify optimization opportunities and performance
trends.
- Integrate APM data with your incident response processes to
enable faster troubleshooting and root cause analysis.

## Resources

**Related documents:**

- [Monitoring
.NET applications on AWS](https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/monitoring.html)
- [Amazon CloudWatch Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [Monitor
.NET and SQL Server applications using CloudWatch Application Insights](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-appinsights.html)
- [.NET
observability with Amazon CloudWatch and AWS X-Ray: Part 1 —
Metrics](https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part1-metrics/)
- [.NET
observability with Amazon CloudWatch and AWS X-Ray: Part 2 —
Logging](https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part2-logging/)
- [.NET
Observability with Amazon CloudWatch and AWS X-Ray: Part 3 –
Distributed Trace](https://aws.amazon.com/blogs/modernizing-with-aws/net-observability-cloudwatch-aws-x-ray-part3-distributed-trace/)

**Related tools:**

- [What
is APM (Application Performance Monitoring)?](https://aws.amazon.com/what-is/application-performance-monitoring/)
- [Detect
common application problems with CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html)
- [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-gettingstarted.html)
- [Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance/actions)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops01-bp03.html*

---

# MSFTOPS02 — Operational automation

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# MSFTOPS02-BP01 Implement Management and Governance solutions

Set up Management and Governance solutions to ensure your Microsoft
workload is patched and compliant with your security requirements.
AWS Systems Manager functions as an operations hub for your
workload, addressing fleet management, compliance, inventory, admin
session management, state management, patch management, and running
remote commands or scripts. Additionally, leverage AWS Systems Manager OpsCenter to provide a central location for viewing,
investigating, and resolving operational issues related to your
Microsoft workloads. OpsCenter aggregates and standardizes
operations items across services while providing contextual
investigation data about each operations item, related items, and
related resources.

**Desired outcome:** Establish
comprehensive management and governance capabilities for your
Microsoft workloads through AWS Systems Manager, ensuring consistent
patch management, compliance monitoring, and centralized operational
issue resolution while maintaining security standards and
operational efficiency across your Windows-based infrastructure.

**Common anti-patterns:**

- Managing Microsoft workloads manually without centralized
management tools, leading to inconsistent patch levels, security
vulnerabilities, and increased operational overhead across the
Windows infrastructure.
- Implementing patch management without proper testing and
rollback procedures, risking system stability and application
availability when updates are applied to production Microsoft
workloads.
- Operating without centralized visibility into operational issues
and compliance status, making it difficult to identify and
resolve problems quickly across distributed Microsoft workload
environments.

**Benefits of establishing this best
practice:**

- Enhanced security posture and compliance through automated patch
management, configuration compliance monitoring, and centralized
governance of Microsoft workloads, reducing security
vulnerabilities and ensuring adherence to organizational
policies.
- Improved operational efficiency through centralized management
capabilities, automated administrative tasks, and streamlined
incident resolution processes that reduce manual effort and
human error.
- Better visibility and control over Microsoft workload operations
through centralized dashboards, automated reporting, and
integrated operational issue management that enables faster
problem resolution and improved system reliability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing comprehensive management and governance for Microsoft
workloads requires a systematic approach using AWS Systems Manager
capabilities. Begin by setting up the Systems Manager Agent on all
Windows instances, configure patch management policies, and
establish compliance monitoring. This approach ensures consistent
management across your Microsoft workload infrastructure while
maintaining security and operational standards.

### Implementation steps

- Install and configure the AWS Systems Manager Agent (SSM
Agent) on all Windows instances in your Microsoft workload
environment.
- Set up AWS Systems Manager Patch Manager with maintenance
windows and patch baselines appropriate for your Microsoft
workload requirements.
- Configure AWS Systems Manager Compliance to monitor
configuration compliance and security standards across your
Windows infrastructure.
- Implement AWS Systems Manager Inventory to maintain an
up-to-date inventory of software, configurations, and system
information.
- Set up AWS Systems Manager Session Manager for secure
administrative access to Windows instances without requiring
RDP or VPN connections.
- Configure AWS Systems Manager State Manager to maintain
consistent configuration states across your Microsoft
workload components.
- Implement AWS Systems Manager OpsCenter to centralize
operational issue management and incident response for your
Microsoft workloads.
- Establish automated workflows using AWS Systems Manager
Automation for common administrative tasks and incident
response procedures.

## Resources

**Related documents:**

- [What
is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [Patch
Manager requirements and WSUS](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-prerequisites.html#source-connectivity)

**Related tools:**

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)
- [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp01.html*

---

# MSFTOPS02-BP02 Implement infrastructure deployment and update automation for your Microsoft workload

Set up Infrastructure as Code (IaC) to apply patterns to the
infrastructure of your Microsoft workload. You can use AWS CloudFormation to help model and deploy the required AWS resources
based on templates. Third-party solutions, such as Terraform, are
also useful for the case.

**Desired outcome:** Establish
automated, repeatable, and version-controlled infrastructure
deployment processes for your Microsoft workloads using
Infrastructure as Code (IaC) practices, ensuring consistent
environments, reducing deployment errors, and enabling rapid scaling
and recovery of your Windows-based infrastructure.

**Common anti-patterns:**

- Deploying Microsoft workload infrastructure manually through the
AWS console or CLI without using Infrastructure as Code, leading
to configuration drift, inconsistent environments, and
difficulty in reproducing deployments across different stages.
- Creating IaC templates without proper version control, testing,
or documentation, making it difficult to track changes, rollback
deployments, or collaborate effectively on infrastructure
modifications.
- Implementing IaC without considering Microsoft workload-specific
requirements such as Windows licensing, Active Directory
integration, or SQL Server configuration, resulting in
incomplete or non-functional deployments.

**Benefits of establishing this best
practice:**

- Consistent and reliable deployments through standardized
Infrastructure as Code templates that ensure all Microsoft
workload components are deployed with the same configuration
across development, testing, and production environments.
- Improved operational efficiency and reduced deployment time
through automated infrastructure provisioning, enabling rapid
scaling, disaster recovery, and environment replication for
Microsoft workloads.
- Enhanced change management and auditability through
version-controlled infrastructure templates that provide clear
documentation of infrastructure changes and enable easy rollback
when issues occur.
- IaC can help enforce security best practices by defining secure
configurations within templates.
- By automating resource provisioning and de-provisioning, IaC can
help optimize resource utilization and reduce costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing Infrastructure as Code for Microsoft workloads
requires careful consideration of Windows-specific requirements
and AWS services. Start by identifying your Microsoft workload
components and their dependencies, then create modular IaC
templates that can be reused across environments. This approach
ensures consistent deployments while accommodating the specific
needs of Windows-based applications and services.

### Implementation steps

- Analyze your Microsoft workload architecture and identify
all AWS resources, dependencies, and configuration
requirements.
- Choose an appropriate IaC tool (AWS CloudFormation, AWS CDK,
or Terraform) based on your team's expertise and
organizational requirements.
- Create modular IaC templates for common Microsoft workload
components such as Windows EC2 instances, SQL Server
databases, and Active Directory services.
- Implement version control for your IaC templates using Git
repositories with proper branching strategies and code
review processes.
- Set up automated testing and validation for your IaC
templates using tools like AWS CloudFormation Guard or
Terraform validation.
- Establish CI/CD pipelines for infrastructure deployment
using AWS CodePipeline, GitHub Actions, or similar tools to
automate template deployment.
- Create environment-specific parameter files and
configuration management to support deployment across
development, testing, and production environments.
- Implement infrastructure monitoring and drift detection to
ensure deployed resources remain consistent with your IaC
templates.

## Resources

**Related documents:**

- [AWS CloudFormation and Windows](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-windows-stacks.html)

**Related videos:**

- [AWS re:Invent 2024 - Use generative AI to optimize cloud
operations for Microsoft workloads (XNT312)](https://www.youtube.com/watch?v=FXul8gfj1Qk&t=3s)

**Related examples:**

- [Use
Terraform to Build Microsoft Infrastructure on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/e5122482-ded0-4259-94f0-c373f23c5257/en-US)

**Related tools:**

- [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/)
- [Terraform
AWS Windows Workloads](https://github.com/aws-samples/terraform-aws-windows-workloads-on-aws)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp02.html*

---

# MSFTOPS02-BP03 Implement operating system image control

AWS has developed a set of Amazon Machine Images (AMIs) for popular
Microsoft solutions with License Included software, enabling
standardized and automated deployments of Windows Server instances
in Amazon EC2. You can either use the latest images that are built
by AWS or create your own. You can subscribe to AWS Windows AMI
notifications or create custom AMIs of your own to apply the
standards required by your environment, such as regional settings,
agents, base patches, and general tools. EC2 Image Builder is a
fully managed AWS service that helps you to automate the creation,
management, and deployment of customized, secure, and up-to-date
server images.

**Desired outcome:** Establish
standardized, secure, and consistently configured Windows Server
images for your Microsoft workloads through automated AMI
management, ensuring rapid deployment capabilities, security
compliance, and operational consistency across all Windows instances
in your environment.

**Common anti-patterns:**

- Using outdated or unpatched base AMIs without regular updates,
leading to security vulnerabilities and inconsistent
configurations across Windows instances in your Microsoft
workload environment.
- Creating custom AMIs manually without automation or version
control, resulting in configuration drift, difficulty in
reproducing images, and challenges in maintaining security and
compliance standards.
- Deploying Windows instances without standardized configurations,
leading to operational inconsistencies, increased
troubleshooting time, and potential security gaps across your
Microsoft workload infrastructure.

**Benefits of establishing this best
practice:**

- Faster deployment and improved consistency through standardized
Windows Server images that include all necessary configurations,
patches, and tools, reducing instance launch time and ensuring
uniform environments.
- Enhanced security posture through automated image updates and
patch management, ensuring all Windows instances are deployed
with the latest security updates and compliance configurations.
- Reduced operational overhead through automated AMI creation and
management processes that eliminate manual image preparation
tasks and ensure consistent, repeatable deployments across
environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing operating system image control for Microsoft
workloads requires a systematic approach to AMI management and
automation. Begin by establishing your image requirements and
standards, then implement EC2 Image Builder to automate the
creation and maintenance of custom Windows AMIs. This approach
ensures consistent, secure, and up-to-date images for your
Microsoft workload deployments.

### Implementation steps

- Define your Windows Server image requirements including base
configurations, security settings, required software, and
organizational standards.
- Set up EC2 Image Builder with appropriate IAM roles and
permissions to automate AMI creation and management
processes.
- Create Image Builder recipes that include your required
Windows configurations, software installations, and security
hardening steps.
- Configure automated testing pipelines to validate AMI
functionality and security compliance before distribution.
- Implement automated AMI distribution to multiple AWS regions
and accounts as needed for your Microsoft workload
deployment strategy.
- Set up AMI lifecycle management policies to automatically
deprecate and delete outdated images while maintaining
required retention periods.
- Subscribe to AWS Windows AMI notifications to stay informed
about security updates and new releases for base Windows
Server images.
- Establish regular AMI update schedules to incorporate
security patches, software updates, and configuration
changes into your custom images.

## Resources

**Related documents:**

- [What
is EC2 Image Builder?](https://docs.aws.amazon.com/imagebuilder/latest/userguide/how-image-builder-works.html)
- [How
Amazon creates AWS Windows AMIs](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-ami-versions.html)

**Related tools:**

- [Amazon EC2 AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp03.html*

---

# MSFTOPS02-BP04 Leverage managed services for your Microsoft workload

To reduce operational overhead, implement the use of AWS managed
services to address your Microsoft workload requirements. Consider
AWS Managed Microsoft Active Directory, Amazon Relational Database Service for SQL Server, Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, AWS Elastic Beanstalk, and others.

**Desired outcome:** Reduce
operational complexity and overhead for your Microsoft workloads by
strategically adopting AWS managed services that handle
infrastructure management, patching, backups, and scaling
automatically, allowing your team to focus on application
development and business value rather than infrastructure
maintenance.

**Common anti-patterns:**

- Managing Microsoft infrastructure components manually when
equivalent AWS managed services are available, leading to
increased operational overhead, higher maintenance costs, and
potential security vulnerabilities from delayed patching.
- Choosing self-managed solutions without evaluating the total
cost of ownership, including operational effort, expertise
requirements, and ongoing maintenance compared to AWS managed
service alternatives.
- Implementing managed services without proper integration
planning, resulting in architectural complexity, security gaps,
or performance issues that could have been avoided with better
design considerations.

**Benefits of establishing this best
practice:**

- Significantly reduced operational overhead through AWS-managed
infrastructure components that handle patching, backups,
monitoring, and scaling automatically, freeing up resources for
higher-value activities.
- Improved reliability and availability through AWS-managed
services that provide built-in high availability, disaster
recovery, and automated failover capabilities designed and
tested by AWS experts.
- Enhanced security posture through managed services that include
automatic security updates, encryption capabilities, and
compliance features that are maintained and updated by AWS
according to industry best practices.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing AWS managed services for Microsoft workloads requires
careful evaluation of your current architecture and identification
of components that can be replaced or enhanced with managed
alternatives. Begin by assessing your Microsoft workload
components and their operational requirements, then systematically
migrate to appropriate AWS managed services while ensuring proper
integration and security.

### Implementation steps

- Conduct a comprehensive assessment of your current Microsoft
workload architecture to identify components suitable for
managed service replacement.
- Evaluate AWS managed service options including AWS Managed Microsoft AD, Amazon RDS for SQL Server, Amazon FSx for Windows File Server, and AWS Elastic Beanstalk.
- Develop a migration strategy that prioritizes
high-maintenance components and considers dependencies
between services and applications.
- Implement pilot migrations with non-critical workloads to
validate managed service configurations and integration
patterns.
- Configure managed services with appropriate security
settings, backup policies, and monitoring to meet your
operational requirements.
- Establish connectivity and integration between managed
services and existing Microsoft workload components using
VPC networking and security groups.
- Migrate production workloads systematically, ensuring proper
testing and rollback procedures are in place for each
migration phase.
- Update operational procedures and documentation to reflect
the new managed service architecture and reduced maintenance
requirements.

## Resources

**Related documents:**

- [AWS Managed Services for Microsoft Workloads](https://aws.amazon.com/windows/)

**Related tools:**

- [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)
- [Amazon RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html)
- [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp04.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
