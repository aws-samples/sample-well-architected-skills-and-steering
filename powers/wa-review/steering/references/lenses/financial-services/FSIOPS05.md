**Pillar**: Operational Excellence

# FSIOPS5: How do you understand the health of your workload?

Financial services institutions are required to communicate service disruptions,
operational events, and failures to downstream stakeholders and regulatory bodies. They
should continually monitor their workloads in the cloud and conduct root cause analysis
(RCA) as an exercise in understanding the events and circumstances that led to unexpected
results, as well as mitigation efforts put in place to prevent recurrence.

## FSIOPS05-BP01 Use enhanced monitoring in the cloud

High availability for financial services workloads that support critical functions
requires the ability to detect failures and quickly recover from them. You can understand
the operational state of your workloads by defining, collecting, and analyzing metrics in
the cloud that can be incorporated into your operating model. These metrics are emitted by
your code, workloads, and user activity, and need to be collected in a centralized,
queryable system that can be used to visualize and examine real-world performance data.
This is important for diagnosing issues that are often not clear from looking at just at
application logs, Amazon CloudWatch, or system logs in isolation.

### Prescriptive guidance

Review [Monitoring and Observability](https://aws.amazon.com/cloudops/monitoring-and-observability/) to familiarize yourself with the capabilities of
AWS services. Financial institutions require logs and metrics for two distinct use
cases: operational analysis (such as troubleshooting during an incident) and regulatory
compliance. Application logs can be collected with Amazon CloudWatch Logs and stored in a centralized
AWS account dedicated to logging. Access to the dedicated logging AWS account should
be limited and based on least privilege, and the data can be shared in a read-only
manner to other AWS accounts for analysis.

If immutable log storage is required for regulatory or corporate policy compliance,
use [Amazon S3 Object Lock](https://aws.amazon.com/s3/features/object-lock/)

or [Amazon Glacier Vault
Lock](https://aws.amazon.com/blogs/aws/glacier-vault-lock/) for WORM storage.

Use AWS tools such as [OpenSearch](https://aws.amazon.com/opensearch-service/) or [Amazon Athena](https://aws.amazon.com/athena/), or
third party tools such as Splunk, Datadog, or Sumo Logic, to provide indexing, search,
analysis, and visualization capabilities.

Use [CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html) for metrics and [CloudWatch anomaly
detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) to detect changes in trends and send alerts to Operations
teams.

[AWS X-Ray](https://aws.amazon.com/xray/) helps you understand how your
application and its underlying services perform to identify and troubleshoot performance
issues and errors.

You can also experience these capabilities in your own AWS account by running the
[One Observability Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US), where you learn about AWS observability
functionalities on [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html),
[AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html), [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html), [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html), and [AWS Distro for
OpenTelemetry](https://aws-otel.github.io/). This workshop deploys a microservice-based application and
guides you in discovering actionable insights through various monitoring tools. Upon
conclusion, the learner is expected to have a clear understanding of logging, metrics,
and traces, as well as techniques for using them across a variety of workload types.

For critical or regulated workloads workloads, Enterprise Support customers should
consider subscribing to [AWS Incident Detection and
Response](https://aws.amazon.com/premiumsupport/aws-incident-detection-response/).

AWS Incident Detection and Response offers eligible AWS Enterprise Support
customers proactive engagement and incident management to reduce the potential for
failure and accelerate recovery of critical workloads from disruption. It achieves these
objectives by fostering joint preparation with AWS to develop runbooks and response
plans customized to the context of each workload onboarded to the service. Onboarded
workloads are monitored by a team of Incident Management Engineers (IMEs) to detect and
engage you on a call bridge within five minutes of a critical alarm.

AWS Incident Detection and Response begins with a review of your workloads for
reliability and operational excellence. AWS experts work with you to define critical
metrics and alarms that provide improved visibility into the application and
infrastructure layers of your workloads, which makes it easier to find and prioritize
issues during an incident. AWS Incident Management Engineers continually monitor your
workloads, detect critical incidents, and engage you on a call bridge with the right
AWS experts to accelerate the recovery of your workloads. All incidents are managed
with the highest level of severity and escalation, and AWS remains engaged until the
incidents are resolved. Lessons learned from previous incidents inform improvements to
response plans and workload architecture, which drives a continuous improvement cycle to
improve the resiliency of your workloads.

## FSIOPS05-BP02 Monitor cloud provider events

Financial institutions should use the AWS Health Dashboard, which provides
information and remediation guidance when AWS is experiencing events that may impact
workloads. The dashboard displays relevant and timely information to help manage events in
progress, and provides proactive notifications to help plan for scheduled activities. With
AWS Health Dashboard, alerts are generated by changes in the health of the AWS
resources used in your applications, giving you event visibility and guidance to help
quickly diagnose and resolve issues. Enterprise support and business support accounts who
have access to the AWS Health API can use this API to integrate the information from
AWS Health Dashboard into the centralized monitoring system and define a consistent
and comprehensive alerting mechanism.

### Prescriptive guidance

[AWS Health](https://docs.aws.amazon.com/health/) provides ongoing
visibility into your resource performance and the availability of your AWS services
and accounts. You can use AWS Health events to learn how service and resource changes
might affect your applications running on AWS. AWS Health provides relevant and
timely information to help you manage events in progress. AWS Health also helps you be
aware of and prepare for planned activities. The service delivers alerts and
notifications initiated by changes in the health of AWS resources, which provides
event visibility and guidance to help accelerate issue resolution. AWS Health provides
information about service operations, such as operational issues, planned maintenance,
and planned software lifecycle events.

For comprehensive visibility into AWS Health event details, such as affected
resource IDs, current status (open or closed), and resource status, use AWS Health
endpoints, such as the AWS Health API, the `aws.health` source in Amazon EventBridge,
and the AWS Health Dashboard. These endpoints provide the most detailed and real-time information
about ongoing events and changes that might affect your workloads.

[AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/what-is-service.html) notifies you through additional UX channels (email, chat, or push
notifications to the AWS Management Console mobile application). AWS Health event notifications don’t
contain as much detailed data as the endpoints listed previously. However, they provide a
simple and effective way to notify stakeholders of issues and changes. Based on rules that
you create, User Notifications creates and sends a notification when an event matches the values that
you specify in a rule. You can select which UX delivery channels a notification is sent to
and set up aggregation to reduce the number of notifications generated for specific
events. Notifications are also visible in the AWS Management Console Notifications Center. For example,
you can receive chat notifications if you have resources in your AWS account that are
scheduled for updates, such as EC2 instances. For more detail, see [Getting
started with AWS User Notifications](https://docs.aws.amazon.com/notifications/latest/userguide/getting-started.html).

You can integrate AWS Health events with Jira and ServiceNow to receive operational
and account information, prepare for scheduled changes, and manage AWS Health events
using the AWS Service Management Connector. The Service Management Connector integration with AWS Health can use AWS Health events
sent through EventBridge to automatically create, map, and update JIRA tickets and ServiceNow
incidents.

You can use organizational view and delegated administrator access to manage
AWS Health events across the organization within Jira and ServiceNow and incorporate
AWS Health information directly into your team’s workflow. For more detail on ServiceNow
integration using the Service Management Connector, see [Integrating AWS Health in ServiceNow](https://docs.aws.amazon.com/smc/latest/ag/sn-aws-health.html).
For more detail on Jira Management Cloud integration using the Service Management Connector, see [AWS Health](https://docs.aws.amazon.com/smc/latest/ag/cloud-sys-health.html).

## FSIOPS05-BP03 Implement comprehensive generative AI observability

Deploy [specialized monitoring](https://aws.amazon.com/cloudwatch/features/generative-ai-observability/) for generative AI workloads that tracks model performance, output quality, token usage, latency, and cost metrics. Monitor for hallucinations, bias, and drift in model outputs. Implement automated alerting for anomalous model behavior and establish prompt performance monitoring to track effectiveness and model response quality over time with automated alerting.

Define escalation procedures for prompt-related security incidents and integrate with existing incident response frameworks.

### Prescriptive guidance

Use Amazon CloudWatch custom metrics to track generative AI-specific KPIs (like tokens per second, prompt success rates, and output validation scores) and customer satisfaction metrics for generative AI-powered interactions. Implement Amazon Bedrock's built-in logging capabilities to capture all model interactions.

Deploy automated quality checks using AWS Lambda to validate model outputs against expected patterns. Use Amazon SageMaker AI Model Monitor for continuous model performance tracking.

Set up cost alerting for token usage to prevent unexpected expenses and optimize resource utilization.

Use Amazon Bedrock's model evaluation capabilities for automated quality assessments and performance benchmarking.

Establish baseline performance metrics and use Amazon CloudWatch anomaly detection for automated drift identification and alerting.

Implement data leakage detection in model outputs and monitor unauthorized access attempts to generative AI endpoints.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiops5.html*
