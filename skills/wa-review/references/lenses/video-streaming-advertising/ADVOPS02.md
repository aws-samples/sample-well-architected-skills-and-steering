# ADVOPS02 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# ADVOPS02-BP01 Implement monitoring across each layer of your advertising stack including infrastructure, applications, and user experience

Ensuring operational excellence in advertising workloads requires
a holistic approach to monitoring. This best practice emphasizes
the importance of implementing comprehensive monitoring solutions
that span all layers of the advertising stack. The advertising
stack includes the ad-serving infrastructure, data pipelines,
application performance, and user experience. By monitoring these
various components, you can gain a complete understanding of the
overall health and performance of your advertising workload. This
understanding helps you identify and address issues, optimize
resource utilization, and deliver a seamless customer experience.
With a multi-layered monitoring approach, you can proactively
detect and resolve problems before they impact your business.

## Implementation guidance

Monitor and set KPIs and SLOs for infrastructure services using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for services like
[Amazon EC2](https://aws.amazon.com/ec2/)
and [Amazon EBS](https://aws.amazon.com/ebs/). Set up CloudWatch Alarms for resource utilization,
performance, and availability.

## Resources

- [Observability using native Amazon CloudWatch and AWS X-Ray for serverless modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)
- [AWS Observability Maturity Model](https://aws-observability.github.io/observability-best-practices/guides/observability-maturity-model/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp01.html*

---

# ADVOPS02-BP02 Collect and analyze detailed metrics for successful operations and ad campaigns

Advertising workloads can experience significant spikes in traffic
and resource utilization, which can impact performance and
availability. To maintain observability across these dynamic
workloads, collect granular, one-second metrics with near
real-time latency. Use advanced analytics, machine learning, and
anomaly detection to continuously analyze this data and
proactively identify issues before they impact campaigns. This
level of observability and proactive issue detection improves the
reliability and responsiveness of your advertising infrastructure,
even during periods of high demand.

## Implementation guidance

Consider the following for collecting important ad-serving
metrics:

- **Granular metrics:** Collect
metrics at a one-second granularity to capture spikes and
fluctuations in advertising workloads. Key metrics to
monitor include:

**Bid requests per
second:** Number of bid requests received.
- **Bid response time:**
Time taken to respond to bid requests.
- **Successful bids:**
Number of successful bids placed.
- **Bid win rate:**
Percentage of bids won compared to total bids placed.
- **Latency metrics:**
Measure network latency, processing time, and database
query times.

For database metrics for RTB platforms:

- **Read and write latency:**
Measure the time taken for read and write operations in your
databases including
[DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html)
and
[Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html).
- **Throughput:** Monitor
[read
and write capacity units](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html) to verify that your database
can handle the load.
- **Error rates:** Track the
number of failed read/write operations.
- **Connection count:** Monitor
the number of
[active
connections](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-metrics.html) to the database.

Consider the following for effective analysis of ad serving
insights:

- **Anomaly detection:** Use
Amazon CloudWatch anomaly detection to detect anomalies in
your metrics based on historical data patterns
automatically. This can help identify potential issues
before they impact campaigns.

Create useful alarms for monitoring and alerting. Configure
CloudWatch alarms for critical metrics such as:

- **High latency:** Set alarms
for when bid response times exceed a defined threshold (for
example, 100ms).
- **Low bid win rate:**
Initiate alerts if the bid win rate drops below a specific
percentage.
- **Database latency:** Create alarms for read or write
latency thresholds to ensure database performance.

Configure your notification mechanisms. Use Amazon Simple Notification Service (Amazon SNS) to send alerts to relevant
stakeholders using email or SMS when alarms go off. This makes
it possible for the appropriate teams to respond quickly to
potential issues.

Other important considerations for observability of advertising
workloads:

- **Impact on cost:**
CloudWatch has charges for custom metrics, alarms, and API
requests, which can add to the overall AWS costs. The cost
can vary based on the number of metrics, alarms, and API
calls configured. SNS has charges for the number of
notifications sent, which can also contribute to the overall
cost.
- **To reduce impact on cost:**
Analyze the expected usage patterns and configure CloudWatch
and SNS based on specific needs to optimize costs. Consider
cost-optimized approaches, such as using sampling or
aggregation for high-volume metrics, to reduce the number of
custom metrics and API calls.
- **Impact on latency:** The
monitoring and logging solutions recommended, when
implemented correctly, should have minimal impact on the
latency of your advertising workloads. CloudWatch provides
near real-time data ingestion and processing, which helps in
quickly detecting and diagnosing issues. However, it's
important to verify that the monitoring and logging
solutions are non-blocking and do not introduce additional
latency in your critical advertising workflows.
- **To reduce impact on
latency:** Implement monitoring and logging
solutions using asynchronous, non-blocking approaches to
minimize the impact on latency. Consider using sampling or
batching techniques to reduce the number of API calls and
optimize the performance of your monitoring and logging
solutions.
- **Ad fraud metrics:** Monitor
invalid traffic rates, bot detection rates, and suspicious
activity patterns.
- **Brand safety metrics:**
Track content classification accuracy, moderation response
times, and policy violation rates.
- **Measurement consistency:**
Monitor cross-system measurement discrepancies,
attribution model performance, and conversion path
integrity.

## Resources

- Set up
[custom
metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) in CloudWatch
- [Monitoring
metrics in an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html)
- [Creating
cross-service dashboards](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-dashboards-visualizations.html)
- [Aggregating
metrics using CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#publishingDataPoints1)
- [Analyzing
performance anomalies with Amazon DevOps Guru for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/devops-guru-for-rds.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp02.html*

---

# ADVOPS02-BP03 Implement centralized logging to aggregate logs from all components of your advertising stack

To provide comprehensive visibility and operational efficiency
across your advertising stack, implement a centralized logging
solution. You can gain a holistic view of your system's
performance and behavior by aggregating logs from all components
of your advertising stack, including third-party integrations and
custom applications.

## Implementation guidance

Review
[centralized
logging with opensearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) to aggregate logs from
all core components of the advertising workload.

**Amazon OpenSearch Service**

Use Amazon OpenSearch Service to aggregate logs from all core
components of the advertising workload, including ad serving
components like AWS Fargate tasks, Amazon EC2 instances, or AWS Lambda functions. OpenSearch provides a robust, scalable, and
highly-available log aggregation solution with powerful search
and analytics capabilities. Use this approach to have a
consolidated view of logs across your entire advertising
ecosystem, facilitating faster issue detection and resolution.

**Amazon CloudWatch Logs**

Alternatively, you can use Amazon CloudWatch Logs to capture and
aggregate logs specifically from your ad serving components.
CloudWatch Logs is a fully-managed service that makes it easy to
monitor, store, and access your log files from various AWS
services and on-premises sources. If your primary focus is on
monitoring and analyzing the logs related to your ad serving
components, CloudWatch Logs can be a suitable option.

The choice between OpenSearch and CloudWatch Logs for ad serving
logs depends on your specific requirements and the overall
complexity of your advertising workload. If you need a
comprehensive, cross-component log aggregation and analysis
solution, OpenSearch may be the preferred choice. However, if
your needs are more focused on the ad serving components,
CloudWatch Logs can be a simpler and more cost-effective option.

## Resources

- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp03.html*

---

# ADVOPS02-BP04 Instrument your advertising application code and infrastructure to emit detailed, structured logs and metrics

Instrument your advertising application code and infrastructure to
emit detailed, structured logs and metrics to achieve
comprehensive visibility into advertising workloads. Organizations
can monitor all components of their workloads, define KPIs, and
set up alerts for critical metrics by using observability services
like Amazon CloudWatch. This structured approach enables teams to
detect, diagnose, and resolve issues quickly. This approach also
optimizes performance and reliability of advertising campaigns.

## Implementation guidance

To gain comprehensive visibility into your advertising workload
and quickly detect, diagnose and resolve issues, use the
following logging strategy:

- Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and
[AWS X-Ray](https://aws.amazon.com/xray/) to capture key performance metrics,
error rates, latency data, and detailed logs from ad serving
infrastructure.
- Centralize all logs from the advertising stack, including third-party integrations
and partner platforms, using a log aggregation solution like Amazon CloudWatch Logs.
- Implement distributed tracing with AWS X-Ray to track user journeys and identify
performance bottlenecks across advertising applications and services.
- Integrate with ad tech platforms and partners to receive comprehensive event-level
data like bid requests, ad impressions, and conversions to power observability and
analytics.

## Resources

- [Observability
using native Amazon CloudWatch and AWS X-Ray for serverless
modern applications](https://aws.amazon.com/blogs/mt/observability-using-native-amazon-cloudwatch-and-aws-x-ray-for-serverless-modern-applications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops02-bp04.html*

---
