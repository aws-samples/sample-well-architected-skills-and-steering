# Operational excellence

**Pages**: 25

---

## 1 - Design SAP workload to allow understanding and reaction to its state

# Best Practice 1.1 – Implement prerequisites for monitoring SAP on AWS

SAP certification requirements for SAP on AWS are outlined in SAP Note 1656250. This
note includes instructions for setting up the AWS Data Provider for SAP, enabling Amazon
CloudWatch detailed monitoring, and using SAP enhanced monitoring for SAP NetWeaver
solutions. Enabling these prerequisites helps ensure that your SAP workload state is able
to be fully understood and investigated by AWS and SAP. These prerequisites should feed
into your overall SAP monitoring strategy.

**Suggestion 1.1.1 - Check SAP support prerequisites**

Check SAP Note 1656250 on the SAP support portal for the most up-to-date support
requirements for SAP on AWS workloads. Follow the detailed instructions in this note.

- SAP Note: [1656250
- SAP on AWS: Support Prerequisites](https://launchpad.support.sap.com/#/notes/1656250) [Requires SAP Portal Access]

**Suggestion 1.1.2 - Install AWS Data Provider for SAP NetWeaver
workloads**

The AWS Data Provider for SAP is a required installation on each of your EC2
instances supporting SAP NetWeaver workloads. The AWS Data Provider for SAP is an agent
which collects performance-related metrics from AWS services and provides them to the
SAP internal application monitoring system. SAP tools, such as transaction code ST06n and
Solution Manager monitoring that use external metrics usually collected from the SAPOSCOL
service, require the AWS Data Provider for SAP to access AWS metrics.

There are indirect costs associated with running the AWS Data Provider for SAP
because of the detailed monitoring and increased API calls required for SAP to receive
monitoring data at speciﬁc intervals. See [AWS Data
Provider for SAP - Introduction - Pricing](https://docs.aws.amazon.com/sap/latest/general/data-provider-intro.html#data-provider-pricing) for details.

- AWS Documentation: [AWS
Data Provider for SAP](https://docs.aws.amazon.com/sap/latest/general/aws-data-provider.html)

**Suggestion 1.1.3 - Create a monitoring strategy for your SAP
workloads**

Decide how you will observe the current and historical health of your SAP application
from both an inside-out and outside-in perspective. Consider all components which work
together to provide the end-user experience. Consider how you will capture metrics from
underlying AWS compute, storage, and network services in addition to internal SAP
application metrics and external user performance and reliability monitoring. Evaluate
different tools for each component and decide how you can bring these together in a single
place (for example, log aggregation) to perform root cause analysis when needed. Determine
how you will use this information to design alert thresholds and remediation actions to be
taken when thresholds are breached.

Understand the capabilities of SAP Solution Manager monitoring, third-party
monitoring tools, and CloudWatch dashboards that can ingest custom SAP monitoring metrics
as a starting point for your design.

- AWS Documentation: [SAP
NetWeaver on AWS: Monitoring Guide](https://docs.aws.amazon.com/sap/latest/sap-netweaver/monitoring.html)
- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [Set
up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/)
- AWS Service Video: [Gaining Better Observability
of Your VMs with Amazon CloudWatch](https://youtu.be/1Ck_me4azMw?ref=wellarchitected)
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)
- SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html)
- SAP Documentation: [SAP NetWeaver Alert Monitor](https://help.sap.com/docs/ABAP_PLATFORM_NEW/984899fe989d4efab0409b818433f892/4907442b4cab209ce10000000a42189d.html?locale=en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-1.html*

---

# Best Practice 1.2 – Implement infrastructure monitoring for SAP

Set up your infrastructure monitoring to provide information about supporting services
that are used to keep your SAP application running and supporting your users. Some examples
include CPU and memory utilization, storage and filesystem usage and performance (IOPS and
throughput), and network throughput. Include any dependent foundational services used by
SAP, such as on-premises Active Directory services, DNS, and third-party tools, such as high
availability (HA) and backup software. Evaluate AWS tools and SAP-specific tools from the
AWS Marketplace that can help correlate and visualize this information, such as DataDog,
Splunk, DynaTrace, and Avantra. Use this information to identify trends and determine when a
corrective action is required.

**Suggestion 1.2.1 - Implement CloudWatch metrics and alarms for
services supporting SAP**

Implement Amazon CloudWatch detailed monitoring metrics and thresholds with alarms for
all of your SAP systems. These metrics and alarms should include monitoring for common
problems which can affect SAP system availability and performance. Common infrastructure
monitoring areas focus on Amazon Elastic Compute Cloud (EC2) instances, Amazon Elastic
Block Storage (Amazon EBS) volumes, and Elastic Load Balancing (ELB).

Common monitoring items include the following:

- Amazon EC2 high CPU utilization
- Amazon EC2 high memory utilization
- Amazon EBS storage paging
- Amazon EBS storage throughput
- Amazon EBS storage IOPS
- Amazon EBS storage space free and volumes full %
- Amazon EC2 network saturation
- ELB/ALB health and target group health

Base your alarm thresholds on healthy patterns of historical production usage of your
system. Continually review and tweak your alarm thresholds to prevent problems.

Review the following resources to get started:

- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- AWS Documentation: [Create a CloudWatch Custom Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- AWS Documentation: [Create a CloudWatch Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html)
- AWS Documentation: [Using CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

**Suggestion 1.2.2 - Implement AWS service quota monitoring for SAP
services**

Implement a monitoring tool, such as Amazon CloudWatch, or other process to keep track of your
[AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) for required SAP resources in your landscape. Amazon EBS and
Amazon EC2 instance quotas are the most common quotas to affect a SAP workload.

For EC2 instance quotas, consider that SAP landscapes can often use a mix of Amazon EC2
instance types and that some types have a different [On-Demand service quota](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits). For example, the `x*` and `u*`
(High Memory) EC2 instance types have a different service quota that is separate from the
combined quota for standard types like `c6`, `m6`, and `r6`
instance families.

When planning new or scaling existing workloads, verify that your service quotas will
support this and engage Support if a quota increase is required.

- AWS Blog: [AWS Systems Manager Automation now enables monitoring of service usage quota in
Amazon CloudWatch](https://aws.amazon.com/about-aws/whats-new/2022/01/aws-systems-manager-automation-usage-quota-amazon-cloudwatch/)
- AWS Documentation: [Service
Quotas - AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- AWS Documentation: [On-Demand Instances - Amazon Elastic Compute Cloud Service Quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits)
- AWS Documentation: [Requesting a quota increase - Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-2.html*

---

# Best Practice 1.3 – Implement application and database monitoring for SAP

Set up your application and database monitoring to provide information about its
internal state, status, and achievement of business outcomes. Some examples include
transaction response time, available work processes, queue depth, error and dump messages,
stalled batch jobs, and transaction throughput. Use this information to determine when a
corrective action is required.

**Suggestion 1.3.1 - Implement monitoring for databases supporting SAP
applications**

Continually monitor your SAP databases and establish alerts for common problems that
can affect SAP system availability and performance. Common monitoring items include the
following:

- Free space in data area
- Free space in logging area
- Excessive locking activity
- Cache utilization rates
- Average query response time
- Required security patches and hot fixes
- Top table sizes and growth

Base alerting thresholds on healthy patterns of historical productive usage of your
system. Continually review and adjust your alarm thresholds to prevent problems and to
react to workload changes or growth.

For details on how to enable monitoring for your specific database, see your database
software provider installation and operational guides.

Consider Amazon CloudWatch Application Insights for SAP HANA databases to analyze metric patterns using historical
data to detect anomalies, and continuously track errors and exceptions from HANA, operating
system, and infrastructure logs.

- SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/)

**Suggestion 1.3.2 - Use SAP transactions and tools to understand the
SAP application**

Configure your SAP applications to provide information about their internal state,
status, and the achievement of business outcomes. Use this information to determine when a
response is required. Common monitoring items include the following:

- Availability of application (ASCS, PAS, AAS) and database services
- Number of active and concurrent users
- Availability of work processes for users
- Response time of user transactions
- Response time of batch and non-interactive transactions
- Error messages and dumps
- Failed jobs
- Full and slow queues

Set up the SAP
EarlyWatch Alert reporting system in SAP Solution Manager to create regular
reports on the status of your SAP systems. Regularly review and remediate issues found in
these reports to prevent problems and avoid interruptions to workload service.

- SAP Note: [2729186
- General Process of EWA Generation](https://launchpad.support.sap.com/#/notes/2729186) [Requires SAP Portal Access]
- SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html)
- SAP Lens [Performance efficiency]: [Best
Practice 16.1 – Have data to evaluate performance](./best-practice-16-1.html)

**Suggestion 1.3.3 - Implement monitoring for your data recovery and
protection mechanisms**

Implement monitoring for mechanisms that safeguard your SAP data in the case of a
failure or disaster. Common monitoring items include:

- Alerts for regular database backups, for example, to Amazon S3 with the AWS
Backint Agent
- Alerts for database replication, for example, HANA system replication failure or
delays across Availability Zones
- Alerts for file storage backups, for example, an EBS snapshot, an Amazon EFS
backup, or an Amazon FSx backup
- Alerts for recovery mechanisms which provide data resilience across Regions, for
example, Amazon S3 buckets with cross-Region replication, Amazon S3 sync or
CloudEndure Disaster Recovery
- Alerts for any recovery mechanisms which provide data resilience across accounts,
for example, Amazon S3 buckets with same-Region replication to a WORM S3 bucket or
logging account

See the following links for further information:

- AWS Blog: [Monitor, Evaluate, and Demonstrate Backup Compliance with AWS Backup Audit
Manager](https://aws.amazon.com/blogs/aws/monitor-evaluate-and-demonstrate-backup-compliance-with-aws-backup-audit-manager/)
- SAP Documentation: [SAP HANA System Replication Verification and Monitoring](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/ba383103029f45fe92a98ecc1eef2f56.html?locale=en-US)

**Suggestion 1.3.4 - Expose SAP monitoring data outside of SAP tools
for independent observability**

SAP monitoring tools are limited to application and operating system level monitoring
and do not cover the wide range of supporting services that give an end-to-end view of SAP
service availability and health. Configure your SAP applications to provide metrics to a
more holistic, external monitoring and visualization tool of your choice.

Use the metrics collected in the previous best practices and externalize these
results such that you have an independent tool which can monitor, alert, and report on
trends. An independent tool allows observability, root cause analysis, historical and
trend reporting without being linked to the SAP system’s availability (that is, when SAP
is in a disaster or fault mode).

- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/)
- AWS Documentation: [Create a CloudWatch Custom Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-3.html*

---

# Best Practice 1.4 – Implement workload configuration monitoring

Design and configure your workload to provide information about its current
configuration and changes to this configuration. Some examples are new or removed EC2
instances, scaling events, code change, patch levels, security group configuration, and
resource deletion. Use this information to determine when a response is required and to
decide whether a change was expected or permitted. Monitor the cost implications of
configuration changes and adjust or analyze budgets if required.

**Suggestion 1.4.1 - Implement workload configuration
monitoring**

Set up and configure AWS CloudTrail to monitor high priority and critical events,
particularly in your SAP production accounts. Example events include new Amazon EC2 instances,
Amazon EC2 decommissioning or changes, security group changes, and AWS KMS and IAM security
change events. Use these events to configure CloudWatch Log Alarms (if required) and take
action in the event of an unexpected change.

- AWS Documentation: [What Is
AWS CloudTrail?](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- AWS Service: [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- AWS Documentation: [Monitoring CloudTrail Log Files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)
- AWS Documentation: [AWS CloudTrail Security Best Practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html)

**Suggestion 1.4.2 - Implement workload configuration enforcement and
remediation**

Set up and configure AWS Config to track, evaluate, and enforce configuration
policy of your AWS resources supporting your SAP production applications. Common
examples include enforcing read-only protection on S3 buckets containing SAP backups,
mandatory Amazon EBS encryption, blocking common network ports, and checking that all
resources have required tags. Use AWS Config [Managed Rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) to improve the security and change control posture of your AWS
environment supporting SAP. Use AWS tags to enforce configuration rules and apply
automated remediation where possible.

- AWS Service: [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- AWS Documentation: [Getting started with AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html)
- AWS Documentation: [Using AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)
- SAP on AWS Blog: [Audit your SAP systems with AWS Config – Part I](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-i/)
- SAP on AWS Blog: [Audit your SAP systems with AWS Config – Part II](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-ii/)
- SAP on AWS Blog: [Tagging Recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/)

**Suggestion 1.4.3 - Implement workload cost monitoring**

Set up and configure [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) with
custom budgets that alert you when you exceed (or are forecasted to exceed) your billing
thresholds. Align budgets with your projected SAP environment spend and monitor for any
anomalies to prevent cost overruns. Monitor your use and coverage of Reserved Instances
and Savings Plans by using budget reports. Use AWS tags to assist in understanding cost
allocation and usage across your SAP workload.

- AWS Blog: [Getting Started with AWS Budgets](https://aws.amazon.com/blogs/aws-cost-management/getting-started-with-aws-budgets/)
- AWS Blog: [AWS Budgets Reports](https://aws.amazon.com/blogs/aws-cost-management/launch-aws-budgets-reports/)
- AWS Documentation: [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- AWS Documentation: [AWS
Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/)
- SAP on AWS Blog: [Tagging Recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-4.html*

---

# Best Practice 1.5 – Implement user activity monitoring

Configure your SAP applications to provide information about user activity, for
example, response time, number of active users, transaction abandonment rates, and order
processing time. Consider both inside-out approaches (monitoring SAP internal dialogue
response time) and outside-in approaches (deploying agents or robots at end-user locations
geographically) to understand how connectivity plays a role in the experience. Use this
information to help understand how the application is used, patterns of usage, and to
determine when a response is required due to poor performance.

**Suggestion 1.5.1 - Implement user experience monitoring from
end-user locations**

Consider outside-in monitoring approaches by deploying user agents or robots at
end-user locations geographically to understand how network and connectivity play a role
in SAP user experience. Often this type of end-user location-based monitoring can provide
insight and early warning of problems not detectable in the central infrastructure and
applications.

Implement Amazon CloudWatch RUM, SAP, or third-party tools which provide end-user experience
reporting to measure the responsiveness of your SAP application from end-user locations. For
example, SAP provides End-User Experience Monitoring in Solution Manager, and Amazon CloudWatch RUM
allows the deployment of monitoring scripts to measure front-end user experience.

- SAP on AWS Blog: [Monitor and Optimize SAP Fiori User Experience on AWS using CloudWatch RUM](https://aws.amazon.com/blogs/awsforsap/monitor-and-optimize-sap-fiori-user-experience-on-aws/)
- SAP Documentation: [SAP User Experience Monitoring](https://help.sap.com/viewer/82f6dd44db4e4518aad4dfce00116fcf/LATEST/en-US/1083786db5f1461c8cff8fbcc1666a4d.html)
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-5.html*

---

# Best Practice 1.6 – Implement dependency monitoring

Configure your workload to provide information about the status (for example,
reachability or response time) of resources it depends on. Examples of external
dependencies can include interfaces (for example, through SAP PI/PO), external data
stores, DNS, on premises components, Active Directory controllers and network devices. Use
this information to determine when a response is required. Consider third party monitoring
tools that can provide cross-technology metrics to monitor the health of end-to-end
dependencies.

**Suggestion 1.6.1 - Implement health tracking for your key SAP
interfaces and cross system business processes**

Identify and monitor your key interfaces which your SAP workload is dependent on.
Monitor the health of these interfaces endpoints, errors, queue length and success rates.
Use in-built mechanisms in SAP or third-party integration tools to set up alerts on
interface failure or delay and feed these into your monitoring tools. Consider all
interface pathways:

- Between different AWS hosted SAP systems (direct via RFC or web
service/HTTPS)
- Between AWS hosted SAP systems and on-premises systems (HTTPS/SFTP - through SAP
PI or third-party integration platform)
- Between AWS hosted SAP systems and SAP Business Technology Platform (via SAP
Cloud Connector)
- Between AWS hosted SAP systems and external party systems (typically via HTTPS
over the internet/VPN)

Consider Solution Manager Business Process Monitoring for cross-system dependency
monitoring throughout your SAP and non-SAP landscape.

- SAP Documentation: [SAP Business Process and Interface Monitoring](https://help.sap.com/viewer/c458e6a97c6746f2afb2a3d1bf0a630b/LATEST/en-US/2ffcb651ade3147fe10000000a44176d.html)
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)

**Suggestion 1.6.2 - Implement health tracking for your enterprise
services which SAP is dependent on**

An SAP workload is typically dependent on several foundational enterprise services to
be healthy for business users. Consider these foundation services in your monitoring
approach and tools. Example foundational services include Direct Connect for on-premises
system connectivity, Active Directory for authentication/SSO, Network Time Protocol (NTP)
for time synchronization, antivirus services and connectivity to an operating system patch
repository (for example, Microsoft Windows Update or SUSE patching).

- AWS Documentation: [Collect metrics and logs from Amazon EC2 instances and on-premises servers with the
CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
- AWS Documentation: [Enhanced monitoring capabilities for AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-6.html*

---

# Best Practice 1.7 – Implement single pane of glass health monitoring across your SAP workloads

Configure your SAP applications, AWS services, and any dependent components to
provide information about the flow of transactions across the workload. Combine metrics
from multiple sources to create a single pane of glass visualization for the health of
your SAP workload and make this dashboard accessible to your key users. Use this
information to determine when a response is required and to assist you in quickly
identifying the factors contributing to an issue impacting your business.

**Suggestion 1.7.1 - Combine application metrics, workload
configuration, user metrics, and dependency health in a single location**

Combine application monitoring metrics, workload configuration data, user metrics and
dependency health in a single location or tool to allow end-to-end monitoring of your SAP
workload and its health for end-user business processes. This can be achieved through the
use of SAP Solution Manager, custom CloudWatch dashboards and metrics, or third-party
monitoring tools.

Best practice is to create business facing health dashboards with traffic light
health and trends, which allow a drill-down view of workload availability. Drill down
capabilities allow users and operators to assess the specific component of the technology
stack which may be causing a problem or underperforming.

- AWS Documentation: [Create a CloudWatch Dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_dashboard.html)
- SAP on AWS Blog: [Serverless Monitoring for SAP NetWeaver](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [Serverless Monitoring for SAP HANA](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- AWS Marketplace: [Products and Tools for SAP Monitoring](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=SAP&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)
- SAP Documentation: [SAP Solution Manager 7.2 - Application Operations](http://help.sap.com/viewer/c3c5ec585ee248228ddb6c3f08073ea9/LATEST/en-US/456408e2a51b476c960fda046c96cb76.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-7.html*

---

# Best Practice 1.8 – Use automated response and recovery techniques to react to monitoring alerts

Automate responses to events to reduce errors caused by manual processes, and to
ensure prompt and consistent responses.

**Suggestion 1.8.1 - Use automation services to automate your
responses to events**

There are multiple ways to automate the running of remediation activities for events
triggered from your monitoring tools. Generally, you should seek to funnel all of your SAP
application and database events into a single channel which can provide event-based
automation in response.

- To respond to an event from a state change in your AWS resources, or from your
own custom events from SAP, you could create [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) to
invoke actions in Event [targets](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-targets.html) (for example,
Lambda functions, Amazon Simple Notification Service (Amazon SNS) topics, Amazon ECS tasks,
and AWS Systems Manager Automation). AWS Systems Manager automation can be used to
call the `sapcontrol` command and perform SAP system tasks automatically.
- To respond to a metric that crosses a threshold for a resource (for example, wait
time), you should create [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) to perform one or more actions using [Amazon EC2 actions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/OperationList-query-ec2.html), [Auto Scaling actions](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_Operations_List.html), or to send a notification to an [Amazon SNS topic](http://aws.amazon.com/sns/).
- If you need to perform custom actions in response to an alarm, invoke Lambda
through Amazon SNS notification or an AWS Systems Manager Automation (for example,
using Action `aws:runCommand` ) see [AWS Blog: Automate Start or Stop of Distributed SAP HANA systems using AWS
Systems Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/).
- Use Amazon SNS to publish Event Notifications and escalation messages to keep people
informed.
- AWS also supports third-party systems through the AWS service APIs and SDKs.
There are a number of monitoring tools provided by AWS Partners and third parties that
allow for monitoring, notifications, and responses. Some of these tools include Avantra,
New Relic, Splunk, Loggly, SumoLogic, and Datadog.
- Consider pushing events and interactions into third-party ITIL tools where
applicable for your organization - such as [AWS to ServiceNow](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/integrations-servicenow.html) integration.

You should keep critical manual procedures available for use when automated procedures
fail.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-1-8.html*

---

## 2 – Reduce defects, ease remediation, and improve workflow of SAP change

# Best Practice 2.1 – Use version control and configuration management

Configuration Management systems reduce errors caused by manual processes and reduce
the level of effort to deploy changes. Doing so supports tracking changes, deploying new
versions, detecting changes to existing versions, and reverting to prior versions (for
example, rolling back to a known good state in the event of a failure). Integrate the
version control capabilities of your configuration management systems into all your
procedures across SAP – the infrastructure, the database, the application, and SAP custom
code and developments (for example, ABAP, Java, and UI5/JavaScript).

Consider different version control systems for each type of configuration, but
consolidate metrics into a central release planning tool. Consider how non-transportable
configuration and binary versioning is managed across your environments (for example - how
do you know that your SAP Kernel versions are aligned across your landscape?).

**Suggestion 2.1.1 - Implement SAP change control or other third-party
tools for managing your SAP development code and versioning**

Ensure you implement change control for all development approaches and custom code
that support your SAP applications - ABAP, Java, UI5/JavaScript, and any other extensions
or scripting areas. Consider all your SAP applications and how you will orchestrate code
deployment across multiple SAP deployment patterns (for example, how will you
simultaneously release related developments hosted on AWS and SAP Business Technology
Platform).

- AWS Service: [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html?ref=wellarchitected)
- AWS Video: [Introduction to AWS CodeCommit](https://youtu.be/46PRLMW8otg?ref=wellarchitected)
- SAP on AWS Blog: [AWS DevOps tools for SAP, Part 1: Cloud Foundry](https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-1-cloud-foundry-apps/)
- SAP on AWS Blog: [AWS DevOps tools for SAP, Part 2: SAP Fiori Apps](https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-2-sap-fiori-apps/)
- SAP Documentation: [SAP Change Control Management](https://help.sap.com/viewer/8b923a2175be4939816f0981b73856c7/LATEST/en-US/2b614e1cb8204f35b477eac703073589.html)
- SAP Documentation: [Best
Practices for SAP BTP - Lifecycle Management](https://help.sap.com/viewer/df50977d8bfa4c9a8a063ddb37113c43/Cloud/en-US)

**Suggestion 2.1.2 - Implement configuration management systems for
your SAP applications**

Implement configuration management tools for ABAP, Java, and other SAP technologies
and consider how non-transportable configuration and binary versioning is managed across
your landscape (for example - how do you know that your SAP Kernel versions are aligned
across your environment?). Use SAP Solution Manager to plan and implement configuration
and version changes to your SAP applications.

- SAP on AWS Blog: [Maintain an SAP landscape inventory with AWS Systems Manager and Amazon Athena](https://aws.amazon.com/blogs/awsforsap/maintain-an-sap-landscape-inventory-with-aws-systems-manager-and-amazon-athena/)
- SAP Documentation: [Enhanced Change & Transport System (CTS+)](https://support.sap.com/en/tools/software-logistics-tools/enhanced-change-and-transport-system.html)
- SAP Documentation: [SAP Solution Manager: Planning Landscape Changes](https://www.sap.com/germany/documents/2016/08/8ea1d93a-857c-0010-82c7-eda71af511fa.html)

**Suggestion 2.1.3 - Implement configuration management systems for
operating systems**

Use AMI baking or in-place configuration management software such as Ansible, Chef or
Puppet to align configuration management across your SAP workload operating systems.
Consider security focused configuration management tools which will alert you to
vulnerabilities and prompt you to keep your operating systems patched and hardened.

- AWS Documentation: [AWS Systems Manager - State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html)
- AWS Documentation: [Configuration management in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuration-management.html)
- AWS Documentation: [What is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html)

**Suggestion 2.1.4 - Implement configuration management systems for
databases**

Work with your database software vendor to understand configuration management
approaches for your database.

- SAP Documentation: [SAP HANA Platform Lifecycle Management](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/571d0bb4b1b2402f8e7caf0fe0290b61.html)

**Suggestion 2.1.5 - Implement configuration management systems for
infrastructure**

Use infrastructure as code (IaC) approaches to provision and manage AWS resources
supporting your SAP workloads. AWS CloudFormation and AWS Cloud Development Kit (AWS CDK) are tools you can use to provision
and manage configuration in AWS resources programmatically.

Consider configuration audit and control tools such as [AWS Config: Conformance Packs](https://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html) that allow you to deploy rules and policies to evaluate
your infrastructure periodically to assess compliance and resolve any problems with
applicable best practices and standards.

- AWS Documentation: [AWS
Launch Wizard for SAP](https://aws.amazon.com/launchwizard/)
- AWS Documentation: [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)
- AWS Documentation: [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)
- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/)
- SAP Lens [Reliability]: [Best Practice 11.3 -
Define an approach to restore service availability](./best-practice-11-3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-1.html*

---

# Best Practice 2.2 – Implement practices to improve code quality

Implement practices to improve code quality and minimize defects. For example,
test-driven development, code reviews, and standards adoption. Use SAP Code Inspector
tools at a minimum.

**Suggestion 2.2.1 - Implement practices to improve code
quality**

For example, test-driven development, pair programming, code reviews, and standards
adoption.

**Suggestion 2.2.2 - Use Code Amazon Inspector tools for SAP
development and integrate this process into your CI/CD pipeline**

Consider the following tools for automated code inspection and linting in your SAP
workloads:

- AWS Documentation: [Amazon
CodeGuru - for AWS Java and Python development](https://aws.amazon.com/codeguru/)
- SAP Documentation: [SAP Code Inspector for ABAP and SAP-specific development](https://help.sap.com/viewer/ba879a6e2ea04d9bb94c7ccd7cdac446/LATEST/en-US/49205531d0fc14cfe10000000a42189b.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-2.html*

---

# Best Practice 2.3 – Use build and deployment management systems

Use build and deployment management systems. Ensure you are using SAP certified build
and deployment systems such as the ABAP Change and Transport System (CTS), Web IDE or SAP
tools. These systems reduce errors caused by manual processes and reduce the level of
effort to deploy changes.

**Suggestion 2.3.1 - Implement SAP build and deployment
systems**

Implement SAP certified build and deployment systems such as the ABAP Change and
Transport System (CTS), Web IDE, SAP BTP Continuous Delivery service or other SAP tools.

- AWS Whitepaper: [Practicing Continuous Integration and Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html)
- SAP on AWS Blog: [AWS DevOps tools for SAP, Part 2: SAP Fiori Apps](https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-2-sap-fiori-apps/)
- SAP Documentation: [Software Logistics Toolset - Change and Transport Tools](https://support.sap.com/en/tools/software-logistics-tools.html?anchorId=section_612068808)
- SAP Documentation: [Deploying Applications to BTP](https://help.sap.com/viewer/825270ffffe74d9f988a0f0066ad59f0/LATEST/en-US/4478283a220b46d9a46bb28d6a9140e8.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-3.html*

---

# Best Practice 2.4 – Use multiple environments

Use multiple SAP environments to experiment, develop, and test your workload. Use
increasing levels of controls as environments approach production to gain confidence your
workload will operate as intended when deployed. Generally, a three-tier environment for
development, test, and production is minimum for SAP landscapes.

**Suggestion 2.4.1 - Use temporary environments for
experimentation**

Provide technology testing and developer teams with sandbox or temporary environments
with minimized controls to enable experimentation and risk mitigation.

- AWS Documentation: [AWS
Launch Wizard for SAP](https://aws.amazon.com/launchwizard/)
- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/)
- SAP on AWS Blog: [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems
Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/)

**Suggestion 2.4.2 - Provide development environments to allow work in
parallel and improved agility**

Provide non-production environments to allow work in parallel, increasing development
and test agility. Implement more rigorous controls in the environments approaching
production to allow developers the necessary means for innovation. Generally, a three-tier
environment for Development, Test and Production is minimum for SAP environments.

**Suggestion 2.4.3 - Provide a consolidated test environment that
replicates production as closely as possible to improve release quality**

Test and staging environments should mirror as closely as possible the interfaces,
security, resilience, and performance characteristics of your production environment to
identify architectural and code interaction problems before being released. Consider
shutting down secondary resources in clusters or scaling down (both horizontally and
vertically) application server performance of this environment when not in use to improve
landscape cost efficiency.

**Suggestion 2.4.4 - Use infrastructure as code (IaC) and
configuration management systems to deploy environments consistently**

Use infrastructure as code (IaC) and configuration management systems to deploy
environments that are configured consistent with the controls present in production to
ensure systems operate as expected when deployed. Use tagging and resource groups to label
and enhance environment metadata such that it can be used for automation and compliance
purposes.

- AWS Documentation: [AWS Launch
Wizard for SAP](https://aws.amazon.com/launchwizard/)
- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/)
- AWS Documentation: [What are AWS
Resource Groups?](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
- SAP on AWS Blog: [Tagging Recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/)

**Suggestion 2.4.5 - Turn off non-production environments when not in
use**

When environments are not in use, turn them off to avoid costs associated with idle
resources (for example, development systems on evenings and weekends).

- SAP on AWS Blog: [Automate Start or Stop of Distributed SAP HANA systems using AWS Systems
Manager](https://aws.amazon.com/blogs/awsforsap/automate-start-or-stop-of-distributed-sap-hana-systems-using-aws-systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-4.html*

---

# Best Practice 2.5 – Test and validate changes

Changes should be tested and the results validated at all lifecycle stages (for
example, development, test, and production). Use testing results to confirm new features
and mitigate the risk and impact of failed deployments. Automate testing and validation to
ensure consistency of review, to reduce errors caused by manual processes, and reduce the
level of effort.

**Suggestion 2.5.1 - Changes should be tested and the results
validated at all lifecycle stages (for example, development, test, and
production)**

**Suggestion 2.5.2 - Maintain a baseline of testing results across
functional testing, performance and resiliency to compare to when releasing change and
major projects.**

**Suggestion 2.5.3 - Understand what level of testing is required for
differing levels of change. For example, a full suite of testing vs targeted regression
testing for minor changes. Agree on test definitions and scope of change testing
required to release to production.**

**Suggestion 2.5.4. - Automate testing where possible with third-party
tools and test harnesses. Focus on regular change types and frequent releases
first.**

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-5.html*

---

# Best Practice 2.6 – Make frequent, small, and reversible changes

Frequent, small, and reversible changes reduce the scope and impact of a change.
Although many SAP NetWeaver solutions only support a “patch forward” approach, consider
using feature toggles in custom development to allow rollback. This eases troubleshooting,
enables faster remediation, and provides the option to roll back a change.

**Suggestion 2.6.1 - Divide development and releases into frequent and
smaller changes where possible**

**Suggestion 2.6.2 - Because many SAP solutions only support a “patch
forward” approach (and do not allow reversible transports), consider using feature toggles
in custom development to allow disablement of features rather than
rollback/withdraw**

**Suggestion 2.6.3 - For non-reversible SAP changes, consider
additional rollback options, such as whole system snapshots, database backup, and
restore options**

- AWS Blog: [Amazon EBS crash-consistent snapshots](https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/)
- AWS Documentation: [Restoring to a specified time using Point-In-Time Recovery (PITR)](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html)
- AWS Documentation: [AWS
Backint for SAP HANA](https://aws.amazon.com/backint-agent/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-6.html*

---

# Best Practice 2.7 – Automate testing, integration, and deployment of changes

Automate build, deployment, and testing of the workload. This reduces errors caused by
manual processes and reduces the effort to deploy changes.

**Suggestion 2.7.1 - Fully automate the integration and deployment
pipeline from code check-in through build, testing, deployment, and
validation**

**Suggestion 2.7.2 - Implement SAP Solution Manager ChaRM, Focused
Build or third-party change and release management tools to orchestrate end-to-end build
to deployment pipelines for application changes**

- SAP Documentation: [SAP Solution Manager Change Request Management](https://help.sap.com/viewer/8b923a2175be4939816f0981b73856c7/LATEST/en-US/4c3acb82b50843b4e10000000a42189e.html)
- SAP Documentation: [SAP Focused Build](https://support.sap.com/en/alm/focused-build.html)
- AWS Marketplace: [Products and Tools for DevOps](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=sap&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)
- AWS Marketplace: [Products and Tools for Testing](https://aws.amazon.com/marketplace/search/results?searchTerms=SAP+Testing&category=b1cf3403-729a-4df1-908d-51105b3574a3)
- SAP on AWS Blog: [AWS DevOps tools for SAP, Part 1: Cloud Foundry](https://aws.amazon.com/blogs/awsforsap/aws-devops-tools-for-sap-part-1-cloud-foundry-apps/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-7.html*

---

## 3 – Understand how you will operate the workload

# Best Practice 3.1 – Ensure personnel capability

Have a mechanism to validate that you have the appropriate number of trained personnel
to provide hands-on support for operational needs and that they have the appropriate SAP,
AWS, or third-party certifications. Train personnel and adjust personnel capacity as
necessary to maintain effective support.

**Suggestion 3.1.1 - Assess the learning and certification needs of
your SAP operations team**

According to your environment and dependencies, different certifications might apply.
Assess the certification needs of your team to be able to support your technology stack:

- AWS Documentation: [AWS
Training](https://aws.amazon.com/training/)
- AWS Documentation: [AWS
Certifications](https://aws.amazon.com/certification/)
- SAP Documentation: [SAP
Certifications](https://training.sap.com/certification/)
- Operating System Certifications

SUSE Documentation: [SUSE Enterprise Linux Certifications](https://training.suse.com/certification/)
- Red Hat Documentation: [Red Hat Enterprise Linux
Certifications](https://www.redhat.com/en/services/certifications)
- Microsoft Documentation: [Microsoft Windows
Certifications](https://docs.microsoft.com/en-us/learn/certifications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-3-1.html*

---

# Best Practice 3.2 – Ensure your cloud operating model matches your operational aims

Identify the appropriate cloud operating model for your SAP workloads such that it
aligns with your identified business requirements for speed to deployment, security,
operations, and responsibility of cloud platform support. An appropriate cloud operating
model is critical for successful adoption of cloud and delivering greater business
agility.

**Suggestion 3.2.1 - Adopt the appropriate cloud operating model for
your business aims**

According to your IT and business requirements, ensure that the appropriate cloud
operating model is adopted. Decide which teams will build and operate your workload. Plan
to move towards a model of shared ownership where the SAP Basis/Technology team and
development team both build and run your SAP workload in a DevOps model.

- AWS Guidance: [AWS Cloud Adoption Framework (AWS CAF)](https://aws.amazon.com/professional-services/CAF/)
- AWS Well-Architected Framework [Operational Excellence]: [Operating Models 2x2](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model-2-by-2-representations.html)
- AWS Well-Architected Framework [Operational Excellence]: [Organizational Culture](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/organizational-culture.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-3-2.html*

---

# Best Practice 3.3 – Share design standards and educate new support personnel in procedures

Share existing best practices, design standards, checklists, operating procedures, and
governance requirements across teams. Ensure all teams are aware of support procedures
across all components of your SAP workload.

**Suggestion 3.3.1 - Share existing best practices, design standards,
checklists, operating procedures, and guidance and governance requirements across teams
to reduce complexity and maximize the benefits from development efforts**

**Suggestion 3.3.2 - Ensure that procedures exist to request changes,
additions, and exceptions to design standards to support continual improvement and
innovation**

**Suggestion 3.3.3 - Ensure that teams are aware of published content
so that they can limit rework and wasted
effort**

**Suggestion 3.3.4 - Ensure that teams know how to log support calls
for different components of your SAP workload**

Who provides support for your operating system, database, and SAP application? For
example, understand whether AWS or your operating system vendor would provide support
directly for clustering or patching issues. In the case of EC2-inclusive operating system
licenses, AWS provides this support directly.

- AWS Documentation: [How to
log a case with AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)
- AWS Documentation: [AWS
Support](https://aws.amazon.com/premiumsupport/)
- SAP Note: [1656250
- SAP on AWS: Support prerequisites](https://launchpad.support.sap.com/#/notes/1656250) [Requires SAP Portal Access]

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-3-3.html*

---

# Best Practice 3.4 – Use runbooks to perform SAP landscape operations

Runbooks are documented procedures to achieve specific outcomes. Enable consistent
and prompt responses to well-understood events by documenting procedures in runbooks.
Understand common SAP operations that are run and create specific, versioned documentation
with a review cycle.

- AWS Well-Architected Framework [Operational Excellence]: [Operational Readiness](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-readiness.html)
- AWS Documentation: [Runbooks and automation using AWS Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/runbooks.html)

**Suggestion 3.4.1 - Create specific runbooks for SAP security
operations**

Consider creating runbooks for common SAP security operations:

- User provisioning and identity management
- Firefighter access
- Authorization changes
- Security and authorization audits
- Encryption key rotation
- TLS certificate management

**Suggestion 3.4.2 - Create specific runbooks for SAP scaling and
performance operations**

Consider creating runbooks for common scaling and performance operations:

- Disk volume re-sizing
- Horizontal and vertical scaling of SAP application servers
- Re-sizing of database server
- Addition or removal of servers from load balancing

**Suggestion 3.4.3 - Create specific runbooks for SAP operations
during faults**

Consider creating runbooks for operations during faults:

- System restarts and order of restarting systems
- SAP backups and restores
- Cluster failover
- Storage failure
- Critical interface restarts and replays
- DNS and network routing changes
- Ransomware recovery

- SAP Lens [Reliability]: [Best Practice 10.3 –
Define an approach to help ensure the availability of critical SAP data](./best-practice-10-3.html)

**Suggestion 3.4.4 - Create specific runbooks for SAP maintenance
operations**

Consider creating runbooks for maintenance operations:

- Starting and stopping SAP
- Refreshing / System Copy of SAP
- Daily health checks
- Error management / ABAP dumps
- Patching SAP application, operating system, and database
- Log rotation, clean up, and archival

Consider database and application log and trace files cleanups for your SAP
environment, for example, SAP Note: [2399996 - Automating SAP HANA
Cleanup](https://launchpad.support.sap.com/#/notes/2399996) [Requires SAP Portal Access]

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-3-4.html*

---

# Best Practice 3.5 – Use playbooks to investigate issues

Enable consistent and prompt responses to issues that are not well understood, by
documenting the investigation process in playbooks. Validate and evolve these playbooks by
using them regularly in operations but also in non-production environments and designated
practice sessions like game days.

**Suggestion 3.5.1 - Create problem playbooks for use in incident
response**

Understand the frequently occurring problems and troubleshooting steps used for each
of the identified problems and create specific, versioned documentation with a review
cycle. Suggested playbooks should include:

- Performance Issue Investigation
- Capacity Issue Investigation
- Authentication and Sign On Issue Investigation
- Security Incident Investigation
- Connectivity and Networking Investigation
- Ransomware and Virus Investigation
- Interface Error Investigation
- Batch Job Error Investigation
- Deployment or Transport Error investigation

Ensure that your playbooks include integration and communication steps with related
support functions and teams. Common communications steps include notification and progress
updates to a critical incident desk, a security incident team and/or a change management
team.

**Suggestion 3.5.2 - Run regular SAP game days to test operational
procedures and validate playbooks**

Consider running SAP game days regularly for your operational team. A game day
simulates a failure or event to test systems, processes, and team responses. The purpose
is to actually perform the actions the team would perform as if an exceptional event
happened. These should be conducted regularly so that your team builds "muscle memory" on
how to respond. Your game days should cover the areas of operations, security,
reliability, performance, and cost. Using a dedicated experimentation environment,
simulate real world scenarios in order to validate and practice operational procedures and
recovery processes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-3-5.html*

---

# Best Practice 3.6 – Use automation to perform SAP landscape operations

Create automation pipelines for your SAP environment builds and landscape operations.
Automation using Infrastructure as Code techniques (for example, CloudFormation, Launch
Wizard for SAP) allows repeatable and agile environment creation or extension. Automated
pipelines and landscape operations reduce errors caused by manual processes, reduce the
effort to deploy changes and improves speed to react to your business needs.

Create automated SAP landscape operational pipelines that allow you to perform common
environment tasks in an automated fashion (for example, System Copy, Start SAP, Stop SAP,
Scale SAP). Invoke these pipelines in response to operational events such as time-based
system shutdown or automatic scaling due to user load.

**Suggestion 3.6.1- Implement infrastructure as code techniques to
create repeatable and code-driven build pipelines for your SAP landscape**

Use tools such as AWS CloudFormation, AWS Cloud Development Kit (AWS CDK) or AWS Launch Wizard for SAP to create
repeatable, controlled and quick environment deployments.

- SAP on AWS Blog: [Infrastructure as Code Example: Terraform and SAP on AWS](https://aws.amazon.com/blogs/awsforsap/terraform-your-sap-infrastructure-on-aws/)
- AWS Documentation: [AWS
Launch Wizard for SAP](https://aws.amazon.com/launchwizard/)

**Suggestion 3.6.2 - Implement common SAP landscape operations with
automation**

Use orchestration and infrastructure as code (IaC) tools in combination to perform
your common SAP landscape operations in an automated fashion. Tools such as AWS CloudFormation, AWS
Systems Manager – Run Automations, SAP Landscape Management (LaMa) and AWS Lambda can be
orchestrated to perform common SAP landscape operations in deployment pipelines.

Consider third-party automation tools where complex or deep integration between tools
is required (For example: Terraform, Ansible, Chef).

Consider using automated operations as responses to SAP workload events to allow a
self-healing and self-maintaining landscape.

- SAP Note: [2574820
- SAP Landscape Management Cloud Manager for Amazon Web Services (AWS)](https://launchpad.support.sap.com/#/notes/2574820)
[Requires SAP Portal Access]
- AWS Documentation: [AWS
Launch Wizard for SAP](https://aws.amazon.com/launchwizard/)
- AWS Documentation: [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- AWS Marketplace: [Products and Tools for DevOps](https://aws.amazon.com/marketplace/search/results?page=1&searchTerms=sap&category=45c68cc2-ccd6-426b-94bd-92a791004dc2)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-3-6.html*

---

## 4 – Validate and improve your SAP workload regularly

# Best Practice 4.1 – Understand and plan for lifecycle events of your SAP workload

SAP workloads are highly reliant on SAP to provide new software and vulnerability
patching, operating system and database kernels, and escalation for support. SAP regularly
publishes information about SAP software releases: Release types, maintenance durations,
planned availability, and upgrade paths in their [Product Availability
Matrix (PAM)](https://support.sap.com/en/release-upgrade-maintenance.html) and SAP Notes. You should obtain specific details each of your SAP
applications and track these locally to understand if your SAP software is current,
supported and when it will be end of life from a maintenance perspective.

The PAM also offers information about platform availability and compatibility:
including database platform and operating systems supported which should guide you in
patching and upgrading these underlying components of your SAP workload. Operating System
vendors also have their own patching and support lifecycle which should be taken into
account when planning SAP maintenance and lifecycle events such as upgrades.

**Suggestion 4.1.1 - Create an operational roadmap for your SAP
applications taking into account key support and lifecycle dates**

List all of your SAP software applications, kernel versions. operating systems, and
database versions in a central register and consolidate with PAM information on supported
versions and maintenance windows. Use this list as a consolidated view to plan patching,
upgrades and platform changes in all components required to keep SAP current and within
support.

- SAP Documentation: [SAP Release &
Maintenance Strategy: Product Availability Matrix](https://support.sap.com/en/release-upgrade-maintenance.html) [Requires SAP Portal
Access]

**Suggestion 4.1.2 - Maintain a calendar for expiring of credentials,
certificates and licenses**

Alongside the major SAP lifecycle events and patching mentioned previously, ensure
you have an operational calendar which plans minor system events. Examples of these
maintenance events could be expiry of system credentials, expiry of certificates (for
example, for STRUST integration between systems) and any license renewal work or updates
required (for example, temporary SAP or database licenses for migration, development or
POC purposes).

- AWS Documentation: [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)

**Suggestion 4.1.3 - Plan for upgrades or alternatives before SAP
software becomes end of life**

Create an SAP landscape roadmap visualizing your key SAP lifecycle events and
operational upkeep - patching, software upgrades, migrations and re-platforming if
required. Communicate this lifecycle calendar to business and technical stakeholders. Plan
investment to fund these SAP lifecycle activities/projects. Plan in advance with your
business stakeholders where maintenance windows can occur and downtime or restarts will be
required.

- SAP Documentation: [SAP
Roadmap Explorer](https://www.sap.com/products/roadmaps.html)

**Suggestion 4.1.4 - Stay up to date and subscribe to key SAP notes
for support advice**

Subscribe to key SAP notes and Knowledge Base Articles (KBAs) for your SAP workload
such that you will be notified upon any changes or updates to supportability and advice.
Use “Favorite” SAP notes functionality to keep a list of frequently accessed and important
notes for your SAP workload to make them easily accessible and comparable.

- [SAP Support
Portal - Favorite SAP Notes](https://launchpad.support.sap.com/#/mynotes?tab=Favorites) [Requires SAP Portal Access]

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-4-1.html*

---

# Best Practice 4.2 – Regularly perform patch management for software currency

Perform regular patch management to gain features, address issues, and remain
compliant with governance. Consider patches at the operating system, database and SAP
application layer. Understand whether your patching process will be to patch your existing
servers, or provision and patch a new server. Automate patch management to reduce errors
caused by manual processes, reduce the level of effort to patch and reduce the application
downtime required for major SAP, database, and kernel patching.

**Suggestion 4.2.1 - Implement SAP patch management procedures to
regularly review SAP Security Notes and newly released patches**

Consider patches at the operating system, database and SAP application layer.

- AWS Documentation: [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/?card-body.sort-by=item.additionalFields.bulletinDateSort&card-body.sort-order=desc)
- SAP Documentation: [SAP EarlyWatch Alert](https://support.sap.com/en/offerings-programs/support-services/earlywatch-alert.html)
- SAP Documentation: [SAP Security News](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html)

Operating System
Guidance

SUSE Linux Enterprise Server

[SUSE Update Advisories](https://www.suse.com/support/update/)

Red Hat Enterprise Linux

[Red Hat Security
Advisories](https://access.redhat.com/security/security-updates/#/)[Red Hat
Customer Portal](https://access.redhat.com/articles/amazon-web-services-access) (Sign in with AWS)

Microsoft Windows

[Microsoft Security Alerts](https://www.microsoft.com/en-us/msrc/technical-security-notifications)

Oracle Enterprise Linux

[Oracle Security
Alerts](https://www.oracle.com/security-alerts/)

For further discussion on this item see [Security]: [Best Practice 6.2 - Build and protect the operating system](./best-practice-6-2.html).

**Suggestion 4.2.2 - Consider automated tools to align and automate
patches across your SAP landscape**

Tools such as AWS Systems Manager and OpsWorks can assist you to align, plan, test, and
deploy patching across your SAP workload. Consider an automated approach to patching to
minimize effort and maintenance windows.

- AWS Documentation: [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html?ref=wellarchitected)
- SAP Lens [Security]: [Best Practice 6.2 - Build
and protect the operating system.](./best-practice-6-2.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-4-2.html*

---

# Best Practice 4.3 – Regularly test business continuity plans and fault recovery

SAP systems are generally business critical and depended upon for major customer
facing transactions. Enabling the quick resumption of IT operations and minimizing data
loss during a fault or disaster situation is critical for operational excellence. Business
continuity plans (BCP) and fault recovery procedures are required to ensure that your
operations team and systems know what to do, when to do it, and workload service can be
resumed promptly in case of a fault.

Critical to the successful resumption of services is that your BCP procedures and
fault recovery plans are regularly tested, improved upon and refined as your systems and
support team evolves. Testing your BCP and recovery plans outside of real crisis
situations ensures that when a real system fails or disaster does occur, you can be
confident in your ability to successfully resume service and that you will meet your
recovery time objective (RTO) and recovery point objective (RPO).

**Suggestion 4.3.1. - Create a BCP and fault recovery testing
calendar**

Create a calendar which schedules regular (at least annually) BCP and fault scenario
recovery testing for your SAP workload. Involve technology operational teams, support
personnel and business stakeholders in this test so that procedures are understood and
expectations are aligned. Aim to test your systems in as real a situation as
possible.

Consider testing the following scenarios and validating recovery metrics for each of
them:

- SAP application service failure

*(for example, SAP application service fails to start due to a configuration
change)*
- Single instance host failure

*(for example, SAP application server EC2 instance becomes
unreachable)*
- Single storage volume failure

*(for example, a single EBS volume becomes unreachable)*
- Network failure and switch over to redundant connection

*(for example, your on-premises Direct Connect connection is
unreachable)*
- Automated failover between primary and secondary clustered components

*(for example, SUSE HAE cluster forces primary HANA database to move to the
secondary database in an alternate Availability Zone)*
- Manual fail over between primary and secondary components

*(for example, manual invocation of Oracle DataGuard switch over to secondary
database in an alternate Availability Zone)*
- Load balancing between multiply redundant components

*(for example, primary web dispatcher fails in a high availability pair
across Availability Zones)*
- Recovery of your SAP application in an alternate AWS Region (if required)
- Recovery from backup in event of ransomware

*(for example, recovering your entire SAP ERP system from Amazon S3 WORM
backup)*

**Suggestion 4.3.2 - Regularly review and update BCP and fault
recovery procedures as part of workload changes**

As your workload evolves and changes over time, ensure that BCP and recovery
procedures are considered in these changes. When a code or infrastructure change might
affect your RTO or RPO, ensure that documentation and configuration is updated, and the
new BCP and recovery process is tested as part of the release process or regular test
calendar.

- AWS Documentation: [Business Continuity Plan (BCP) Definition](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html)
- AWS Documentation: [Architecture Guidance for Availability and Reliability of SAP on AWS](https://docs.aws.amazon.com/sap/latest/general/architecture-guidance-of-sap-on-aws.html)
- SAP Lens [Reliability]: [Best Practice 11.4 -
Conduct periodic tests of resilience](./best-practice-11-4.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-4-3.html*

---

# Best Practice 4.4 – Perform regular workload reviews to optimize for resiliency, performance, agility, and cost

When running SAP on AWS, plan and dedicate time and resources for continual
incremental improvement to evolve the effectiveness and efficiency of your workload. AWS
regularly releases new services, approaches, improved SLAs, and price reductions that you
can take advantage of to optimize your SAP workload. Understand and validate whether new
service releases are applicable to your SAP workload and, where appropriate, implement
them in your production environment to evolve your workload.

**Suggestion 4.4.1 - Plan regular reviews of your SAP
workload**

Work with your AWS team, AWS Partner, or internal experts to periodically review
your SAP workload using the Well-Architected Framework SAP Lens (this document). Plan to
review your workload at least every once a year. Identify, validate, and prioritize
improvement activities and issue remediation and incorporate this into your
backlog.

Consider harvesting your learnings from operational incidents into curated questions
with best practices guidance. Create Operational Readiness Review (ORR) runbooks to assist
when deploying new SAP landscapes, applications, or workloads.

- AWS Whitepaper (this document): [SAP
Lens for Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/sap-lens.html)
- AWS Whitepaper: [Operational Readiness Reviews (ORR)](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html)

**Suggestion 4.4.2 - Review Amazon EC2 instance sizing and
performance**

Review the CPU usage and memory utilization of your SAP workload by validating
historical CloudWatch metrics. Review each SAP component for low CPU or memory utilization
and consider right sizing EC2 instances to better match workload requirements. Consider
newly released and SAP-certified EC2 instance types for performance fit and cost
optimization. Plan to take advantage of new improvements in your operational
backlog.

See [Cost Optimization](./cost-optimization.html) for Amazon EC2 usage
in SAP workloads.

- AWS Documentation: [Amazon EC2 instance types for SAP](https://docs.aws.amazon.com/sap/latest/general/ec2-instance-types-sap.html)

**Suggestion 4.4.3 - Review Amazon EBS sizing and
performance**

Review storage usage across your SAP workload by validating volume consumption,
throughput and IOPS usage from CloudWatch historical metrics. Review each SAP component
for oversized storage or low throughput/IOPS utilization and consider right sizing
Amazon EBS storage sizes and types in order to better match workload requirements. Consider newly
released and SAP certified Amazon EBS types for performance fit and cost optimization.
Plan to take advantage of new improvements in your operational backlog

- AWS Documentation: [Right Sizing](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/)
- SAP Lens [Cost Optimization]: [Best Practice
18.4 - Evaluate the cost impact of storage options based on the required
characteristics](./best-practice-18-4.html)

**Suggestion 4.4.4 - Review new services that improve agility or
improve efficiency in your SAP workload operations**

Review new supporting service releases that could improve operations in your SAP
workload. If you have a technical account manager (TAM) as part of an AWS Support
agreement, they can assist you in a new service briefing and optimization
discussion.

Consider new releases such as shared file storage, interface services (for example,
AWS Transfer, API Gateway), security services (for example, Amazon GuardDuty, AWS
Firewall), backup tools (for example, AWS Backint) and automation tools (for example,
Launch Wizard for SAP).

Plan to take advantage of new improvements in your operational backlog.

- AWS Documentation: [“What’s New”
Feed](https://aws.amazon.com/new/)
- AWS Documentation: [Proactive Services from Support](https://aws.amazon.com/premiumsupport/technology-and-programs/proactive-services/)

**Suggestion 4.4.5 - Monitor SAP on AWS blogs and
announcements**

Consider subscribing to the SAP on AWS Blog feed and AWS “What’s New” feed to
stay up to date with newly released service announcements, innovation approaches and price
reductions.

- [SAP on AWS Blog Feed](https://aws.amazon.com/blogs/awsforsap/)

**Suggestion 4.4.6 - Plan periodic enhancement work to take advantage
of new and improved AWS services**

Ensure that your operational budget allows for planned support team effort for
implementation and testing of new AWS services and workload evolution on a periodic
basis.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-4-4.html*

---
