# MIDAPERF04 — Troubleshoot and optimize pipelines

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF04-BP01 Implement end-to-end observability for manufacturing data pipelines

In manufacturing environments, comprehensive visibility into data processing and
ingestion infrastructures is critical for maintaining operational excellence and providing
timely delivery of production insights. Implementing robust observability solutions enables
rapid identification and resolution of issues that could impact data quality, processing
efficiency, or analytical outcomes.

**Desired outcome:** A fully observable data processing and ingestion infrastructure that provides immediate
visibility into performance metrics, error conditions, and processing bottlenecks, enabling
teams to quickly troubleshoot issues, minimize downtime, and maintain reliable data flows that
support critical manufacturing operations.

**Common anti-patterns:**

- Waiting for production teams to report data issues instead of proactive monitoring and alerting
- Using separate, disconnected monitoring tools that prevent correlation of issues across the entire data pipeline
- Implementing basic logging without contextual information like correlation IDs, production batch identifiers, or equipment-specific metadata
- Failing to trace data flows end-to-end through multi-stage processing pipelines, making bottleneck identification difficult
- Not monitoring edge gateways, industrial PCs, and on-premises servers that are critical points of failure
- Failing to track API interactions, retries, throttling, and authentication failures that can silently degrade pipeline performance
- Either over-sampling (causing performance overhead) or under-sampling (missing critical performance insights) in trace collection
- Inability to correlate symptoms across distributed manufacturing systems during troubleshooting
- Relying on manual detection of data quality issues, latency increases, or data gaps instead of automated monitoring
- Not configuring appropriate logging verbosity or failing to enhance detail levels during active troubleshooting scenarios
- Tracking only technical metrics without correlating to manufacturing KPIs like production batch status or equipment performance
- Lacking systematic protocols that isolate bottlenecks from sensor collection through visualization systems

**Benefits of establishing this best practice:**

- Reduces mean time to identification and resolution for data pipeline issues
- Enables correlation of symptoms across distributed manufacturing systems
- Provides transparency into third-party component interactions
- Facilitates root cause analysis through comprehensive tracing capabilities
- Supports continuous improvement of pipeline reliability and performance

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- Implement structured logging across the data pipeline components using Amazon CloudWatch Logs for centralized log aggregation, AWS IoT Device Management for edge device logging, and Amazon Data Firehose for high-volume log streaming. Use AWS X-Ray trace IDs as correlation identifiers and leverage CloudWatch Log Insights for querying logs with manufacturing context like batch numbers and equipment tags.
- Deploy AWS X-Ray across your data services including Lambda functions, ECS containers, and API Gateway endpoints to trace data flow end-to-end. Configure X-Ray sampling rules to reduce overhead while maintaining visibility for critical manufacturing processes and use AWS App Mesh for service mesh tracing in containerized environments.
- Install Amazon CloudWatch agent on edge gateways and industrial PCs to collect system metrics, logs, and custom manufacturing metrics. Use AWS Systems Manager for agent deployment and configuration management and leverage AWS IoT Greengrass for edge computing monitoring with local data processing capabilities.
- Enable AWS CloudTrail for API call logging, configure Amazon API Gateway access logging and throttling monitoring, and use Amazon CloudWatch alarms to detect retry patterns and authentication failures. Implement AWS WAF logging for additional API security monitoring and use Amazon EventBridge for real-time API event processing.
- Create unified dashboards using Amazon CloudWatch Dashboards combined with AWS X-Ray service maps for end-to-end pipeline visualization. Use Amazon OpenSearch Service for advanced log analytics, Amazon Managed Grafana for custom manufacturing dashboards, and AWS Systems Manager OpsCenter for centralized operational issue management and correlation.

## Key AWS services

- Amazon CloudWatch for metrics, logs, and dashboards
- CloudWatch Agent for on-premises monitoring
- AWS X-Ray for distributed tracing and service maps
- AWS CloudTrail for API activity monitoring
- Amazon OpenSearch Service for advanced log analytics
- Amazon Managed Grafana for visualization (where applicable)

## Resources

- [Monitoring AWS IoT Applications with CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [Installing and Configuring the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
- [Getting Started with AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Analyzing API Calls with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf04-bp01.html*

---

# MIDAPERF04-BP02 Decouple data ingestion from processing in manufacturing systems

In manufacturing environments, tightly coupled data pipelines create single points of
failure that can lead to data loss and operational disruptions. Implementing a decoupled
architecture that separates ingestion from processing enhances system resilience, enables
independent scaling of components, and provides the foundation for reliable data processing
even during partial system failures common in industrial settings.

**Desired outcome:** A resilient manufacturing data architecture where ingestion and processing components
operate independently, enabling continuous data capture during processing failures, supporting
reprocessing capabilities when ingestion recovers from outages, and maintaining overall system
performance through appropriate component scaling.

**Common anti-patterns:**

- Tightly coupling data ingestion directly to processing components - Creates single
points of failure that can cause complete system shutdowns and data loss during processing
failures
- Implementing synchronous processing without buffering - Forces ingestion to wait for
processing completion, creating bottlenecks and reducing overall system throughput
- Using shared scaling policies for ingestion and processing - Leads to
over-provisioning or under-provisioning of resources since components have different load
patterns and scaling requirements
- Designing non-idempotent processing operations - Causes data corruption and
inconsistencies during replay scenarios, requiring expensive cleanup operations that
impact performance
- Failing to implement dead-letter queues or error handling - Results in infinite retry
loops that consume resources and degrade system performance during data quality issues
- Configuring insufficient buffer retention periods - Forces data loss during extended
outages, requiring expensive data recovery operations and potential reprocessing from
external sources
- Omitting queue depth monitoring for scaling decisions - Causes reactive rather than
proactive scaling, leading to buffer overflows and performance degradation during traffic
spikes
- Creating processing components without replay capabilities - Requires rebuilding
entire datasets during recovery, consuming significant computational resources and
extending downtime
- Using inadequate buffer storage capacity planning - Results in data loss during peak
ingestion periods or extended processing outages, requiring expensive data reconstruction
- Implementing blocking operations in ingestion pipelines - Creates cascading failures
where upstream data collection stops when downstream processing experiences issues
- Designing stateful processing without proper checkpointing - Forces complete
reprocessing from the beginning during failures, wasting computational resources and
extending recovery times
- Configuring overly aggressive retry policies without backoff - Overwhelms failing
components and prevents recovery while consuming network and computational resources
unnecessarily

**Benefits of establishing this best practice:**

- Helps prevent critical production data loss during equipment shutdowns or unplanned
downtime – Continually captures sensor readings, alarm states, and process variables even
when historians, SCADA systems, or edge devices require maintenance or experience hardware
failures.
- Allows dynamic resource allocation to match plant operational cycles and data volumes
- Enables scaling data ingestion during high-production periods or maintenance windows
while independently adjusting processing power for complex analytics like predictive
maintenance algorithms or real-time quality control calculations.
- Provides data replay capabilities for root cause analysis and process optimization -
Supports reprocessing historical operational data after system outages, calibration
changes, or when new analytics models are deployed to backfill insights for compliance
reporting or process improvement initiatives.
- Maintains data pipeline integrity despite industrial network instabilities and
equipment faults – Continually operates through common industrial challenges like network
congestion, PLC communication errors, fieldbus disruptions, or temporary sensor
malfunctions that frequently impact manufacturing environments.
- Minimizes production impact during system upgrades and reduces maintenance windows -
Enables rolling updates of data processing systems without disrupting critical real-time
monitoring, trending, or automated control loops, allowing maintenance activities during
normal production hours rather than costly scheduled downtime.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- Implement Durable Ingestion Buffers - Deploy Amazon Kinesis Data Streams or Amazon MSK (Kafka) for high-throughput streaming data with configurable retention periods up to
365 days. For batch workloads, use Amazon SQS with extended message retention and DLQ
configuration, combined with Amazon S3 for long-term storage overflow when queue limits
are approached.
- Design Idempotent Processing - Leverage Amazon DynamoDB conditional writes or
Amazon RDS with upsert operations for processing idempotency. Implement AWS Lambda with
event source mapping deduplication features or use Amazon Managed Service for Apache Flink for
exactly-once processing semantics. Store processing state in DynamoDB with composite
keys to track message processing status.
- Configure Dead-Letter Handling - Set up Amazon SQS Dead Letter Queues with Amazon CloudWatch alarms for message count thresholds. Use Amazon SNS to trigger notifications
when DLQ thresholds are exceeded. Store failed messages in Amazon S3 with lifecycle
policies for cost optimization and use AWS Step Functions for orchestrating retry logic
and failure investigation workflows.
- Implement Replay Capabilities - Utilize Kinesis Data Streams' time-based replay
functionality or Amazon MSK's offset management for streaming data replay. For batch
data, implement S3-based data lake architecture with AWS Glue ETL jobs that can
reprocess partitioned data based on timestamps. Use AWS Batch for large-scale
reprocessing jobs with automatic retry and scaling capabilities.
- Establish Independent Scaling - Configure Amazon EC2 Auto Scaling Groups with
custom CloudWatch metrics for queue depth monitoring. Use AWS Application Auto Scaling
for Kinesis shard scaling based on incoming records and iterator age metrics. Implement
AWS Lambda concurrent execution limits and reserved concurrency to help prevent
downstream system overload while allowing independent scaling of processing components.

## Key Services

- Amazon Kinesis Data Streams for scalable data ingestion
- Amazon SQS for durable message queuing
- Amazon MSK (Managed Streaming for Apache Kafka) for high-throughput streaming
- Amazon S3 for durable data landing and replay capabilities
- AWS Lambda for serverless processing of ingested data
- Amazon EventBridge for event-based processing orchestration

## Resources

- [Resilience in AWS Data Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/disaster-recovery-resiliency.html)
- [AWS Prescriptive Guidance Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/decouple-microservices-using-amazon-sqs-and-aws-lambda.html)
- [Amazon EventBridge features](https://aws.amazon.com/eventbridge/features/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf04-bp02.html*

---
