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
