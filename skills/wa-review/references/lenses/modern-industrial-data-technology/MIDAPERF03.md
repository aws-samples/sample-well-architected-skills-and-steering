# MIDAPERF03 — Data processing infrastructure

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF03-BP01 Use cloud observability tools for manufacturing systems

In manufacturing environments, comprehensive visibility into system performance, data
processing pipelines, and infrastructure health is critical for maintaining operational
excellence. Implementing cloud-native observability tools provides unified monitoring,
actionable alerting, and diagnostic capabilities across the entire manufacturing technology
stack. This integrated approach enables rapid identification and resolution of performance
issues before they impact production operations.

**Desired outcome:** A comprehensive observability framework that provides real-time visibility into
manufacturing data systems, enabling proactive performance optimization, rapid
troubleshooting, and data-driven capacity planning while providing maximum uptime for critical
manufacturing operations.

**Common anti-patterns:**

- Waiting for system failures before implementing monitoring instead of proactive performance tracking
- Collecting massive amounts of data without establishing manufacturing-specific KPIs or business relevance
- Only monitoring at infrastructure level while ignoring application and business process performance
- Setting too many low-priority alerts or poorly tuned thresholds that create noise instead of actionable insights
- Using disconnected monitoring solutions that prevent correlation across system components
- Operating manufacturing systems without comprehensive API activity logging and analysis
- Ignoring API call patterns and frequency that could indicate over-utilization or inefficient integrations
- Storing critical operational logs in systems where they can be modified, compromising audit trails
- Mixing production logs with development/testing data instead of maintaining dedicated audit accounts
- Manually configuring edge devices instead of using standardized fleet management approaches
- Pushing configuration changes directly to all devices without canary or blue/green deployment strategies
- Operating edge devices without hardware performance monitoring and health tracking
- Relying on human intervention for common device communication issues instead of automated remediation
- Collecting metrics without establishing appropriate performance thresholds for manufacturing-critical systems
- Using only critical alerts instead of progressive severity levels based on threshold proximity
- Creating alerts that don't run automated remediation or clear escalation procedures
- Learning about performance issues only after they affect manufacturing operations
- Operating manufacturing data flows without end-to-end visibility into processing steps and dependencies
- Either over-sampling (performance impact) or under-sampling (missing critical issues) distributed traces
- Running manufacturing systems without understanding request flow timing and bottleneck identification

**Benefits of establishing this best practice:**

- [Reduces MTTD for performance anomalies by 65-85%](https://newrelic.com/resources/white-papers/observability-as-a-priority)
- Enables correlation of issues across different system components for faster root
cause analysis
- Provides quantifiable metrics to justify optimization investments and measure their
impact
- Enhances capacity planning through historical performance trend analysis
- Minimizes production impact through early detection of emerging performance
bottlenecks

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Deploy AWS CloudTrail
across all manufacturing data services to capture API calls from SCADA systems, MES
integrations, and data pipelines. Store logs in a dedicated Amazon S3 bucket with S3
Object Lock for immutability. Use AWS CloudWatch Insights to analyze patterns in equipment
data ingestion rates and identify potential security issues in your OT/IT bridge
connections. Configure AWS Organizations to centralize trail management across production,
staging, and development environments.

Implement Amazon CloudWatch as your unified metrics system, capturing infrastructure metrics from EC2
instances running historian services, custom manufacturing metrics using CloudWatch Custom
Metrics for OEE, throughput, and quality indicators, application performance from
containerized services using Amazon ECS/EKS with Container Insights, and business process
metrics through CloudWatch Embedded Metric Format in your Lambda functions processing
production data. Use Amazon Managed Service for Prometheus for time-series data from edge
devices and Amazon Managed Grafana for manufacturing dashboards.

Configure CloudWatch Alarms
with manufacturing-specific thresholds (for example, data ingestion gaps indicating
equipment downtime). Implement progressive alerting using Amazon SNS topics with different
severity levels: Critical for production line stoppage detection, Warning for trending
toward SLA violations, and Info for planned maintenance windows. Use AWS Lambda functions
triggered by CloudWatch Events for automated remediation, such as restarting stuck data
collection services or switching to backup data sources.

Deploy AWS X-Ray across your manufacturing
data pipeline to trace requests from edge devices through AWS IoT Core, Kinesis Data
Streams, Lambda processing functions, and final storage in Amazon Timestream or S3.
Configure sampling rules to capture 100% of critical production data flows while sampling
routine maintenance data at lower rates. Use X-Ray service maps to visualize dependencies
between your MES, ERP, and analytics systems.

Use AWS IoT Device Management to manage your industrial edge devices and gateways. Deploy AWS IoT Greengrass
for edge computing capabilities. Implement fleet-wide updates using IoT Jobs with
controlled rollout strategies by using IoT Device Management Fleet Indexing to group
devices by production line or equipment type, configuring progressive deployment patterns
with canary releases to test configuration changes on non-critical equipment first, and
monitoring deployment success rates with automatic rollback of failed updates.

Configure AWS IoT Events to detect offline devices, abnormal sensor readings, or communication pattern
anomalies. Set up AWS IoT Device Defender for security monitoring of your industrial
devices. Create automated recovery procedures using AWS Step Functions to orchestrate
device troubleshooting workflows, AWS Systems Manager to remotely diagnose and restart
edge gateway services, and Amazon SNS notifications to operations teams when manual
intervention is required.

Implement intelligent data retention
using Amazon S3 Intelligent Tiering for historical manufacturing data, S3 Lifecycle
policies to transition detailed sensor data from Standard to IA to Glacier based on access
patterns, Amazon Timestream with automatic data tiering for time-series data (memory for
recent data, magnetic storage for historical), and CloudWatch Logs retention policies
configured by criticality (30 days for debug logs, one year for production events). Use AWS Cost Explorer and AWS Budgets to monitor storage costs and set alerts for unexpected data
growth. Consider Amazon Redshift with automatic table optimization for long-term analytics
on production trends while maintaining cost efficiency through Reserved Instance planning
for predictable workloads.

## Key AWS services

- AWS CloudTrail for API activity monitoring
- Amazon CloudWatch for metrics, logs, and alerting
- AWS X-Ray for distributed tracing
- AWS IoT Greengrass for edge device management
- AWS Systems Manager for configuration management
- AWS IoT Events for device state monitoring

## Resources

- [Monitoring AWS IoT Applications](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [Analyzing API Calls with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS X-Ray features](https://aws.amazon.com/xray/features/)
- [AWS IoT Device Management features](https://aws.amazon.com/iot-device-management/features/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/implementations/centralized-logging/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf03-bp01.html*

---

# MIDAPERF03-BP02 Implement comprehensive performance measurement for manufacturing data infrastructure

Understanding the performance characteristics of data processing infrastructure is
essential for maintaining performance efficiency and planning for growth. Implementing robust
measurement frameworks with appropriate metrics, dashboards, and alerting enables
organizations to proactively manage performance, optimize resource utilization, and justify
infrastructure investments with quantifiable data.

**Desired outcome:** A comprehensive performance measurement framework that provides real-time visibility into
all aspects of manufacturing data infrastructure, enabling data-driven optimization decisions,
capacity planning, and early detection of performance degradation before it impacts production
operations.

**Common anti-patterns:**

- Waiting for system failures or user complaints before investigating performance issues instead of implementing proactive monitoring and alerting
- Using separate, disconnected monitoring tools for different infrastructure components without centralized observability and correlation
- Creating technical dashboards with standard IT metrics that don't relate to manufacturing operations or business context
- Setting fixed performance thresholds that don't account for normal manufacturing workload variations and production cycle patterns
- Deploying monitoring without first conducting controlled testing to understand normal performance characteristics
- Failing to track API usage patterns, leading to undetected redundant calls, inefficient integrations, and quota exhaustion
- Monitoring only basic system metrics while ignoring manufacturing-specific measurements like message throughput by device type or processing latency for time-sensitive data
- Configuring too many low-priority alerts or alerts without clear escalation paths, leading to ignored notifications
- Not retaining sufficient performance history for trend analysis and capacity planning decisions
- Implementing only critical threshold alerts without predictive or warning-level notifications for emerging performance trends
- Requiring human intervention for common, predictable performance issues that could be automatically resolved
- Operating without granular resource utilization tracking, making it impossible to allocate costs by workload or justify optimization investments
- Not implementing distributed tracing to understand end-to-end data processing delays across manufacturing workflows
- Skipping controlled performance validation during infrastructure changes or capacity planning exercises

**Benefits of establishing this best practice:**

- Enables proactive identification of performance bottlenecks before they impact
production
- Provides quantifiable metrics to justify optimization investments and infrastructure
scaling
- Facilitates accurate capacity planning based on historical performance trends
- Improves cost allocation through precise measurement of resource utilization by
workload
- Reduces troubleshooting time by pinpointing specific performance constraints

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- Deploy Amazon CloudWatch agents on
EC2 instances and integrate with AWS IoT Core device metrics to collect comprehensive
performance data across the manufacturing infrastructure components. Configure
CloudWatch Custom Metrics specific to industrial data processing needs alongside
standard system metrics through AWS Systems Manager and Amazon Kinesis Data Streams.
- Key metrics to consider:

Message throughput rates (messages per second) by device type and production area
using AWS IoT Device Management groupings
- Data storage utilization trends with forecasted growth patterns via Amazon S3
Storage Lens and Amazon EBS monitoring
- Bandwidth consumption during different production phases through VPC Flow Logs
and AWS Direct Connect monitoring
- Processing latency for time-sensitive manufacturing data flows using Amazon Kinesis Analytics and AWS Lambda duration metrics
- API call volumes and patterns with service quota utilization percentages
through AWS CloudTrail and Service Quotas integration

- Establish a unified monitoring environment
using Amazon CloudWatch Dashboards and AWS Grafana that aggregates metrics from the
infrastructure components. Create manufacturing-specific dashboards using Quick that visualize performance metrics in the context of production operations
rather than just technical indicators, integrated with AWS IoT SiteWise for operational
technology data correlation.
- Enable comprehensive API activity logging
through AWS CloudTrail and Amazon API Gateway access logging to track service usage
patterns. Configure Amazon CloudWatch Insights and AWS X-Ray to identify redundant or
inefficient API calls that could impact performance or exceed service quotas, with cost
optimization insights from AWS Cost Explorer API usage analysis.
- Conduct controlled performance testing using AWS
Load Testing Solution and Amazon CloudWatch Synthetics to establish baseline metrics for
normal operations. Configure dynamic thresholds using CloudWatch Anomaly Detection based
on these baselines to account for expected variations in manufacturing workloads,
leveraging Amazon Forecast for predictive baseline modeling.
- Design a multi-tiered alerting strategy using Amazon CloudWatch Alarms with Amazon SNS notifications and predictive alerts through CloudWatch
Anomaly Detection that identify concerning trends before they reach critical thresholds.
Implement automated remediation using AWS Systems Manager Automation, AWS Lambda
functions, and Amazon EventBridge rules for common performance issues to minimize human
intervention in manufacturing operations.

## Key AWS services

- Amazon CloudWatch for metrics collection and visualization
- AWS X-Ray for distributed tracing and latency analysis
- AWS CloudTrail for API activity monitoring
- AWS Compute Optimizer for resource optimization recommendations
- Amazon Managed Service for Prometheus and Amazon Managed Grafana for advanced
monitoring scenarios

## Resources

- [Monitoring AWS IoT Applications with
CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [Analyzing API Calls with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS X-Ray: Use a console](https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html#xray-console-servicemap)
- [Service Quotas and Amazon CloudWatch
alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf03-bp02.html*

---
