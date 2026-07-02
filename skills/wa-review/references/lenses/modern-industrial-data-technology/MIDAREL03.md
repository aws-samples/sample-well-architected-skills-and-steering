# MIDAREL03 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# MIDAREL03-BP01 Implement dynamic scaling for shop floor data ingestion pipelines

Manufacturing operations generate varying volumes of data from machines, sensors, and
production lines. Dynamic scaling verifies that your data ingestion pipelines can handle peak
production times without overprovisioning during slower periods.

**Desired outcome:**

A resilient data ingestion system that automatically scales to accommodate fluctuating
data volumes from the shop floor, providing consistent performance during peak production
while optimizing costs during lower activity periods.

**Benefits of establishing this best practice:**

- Cost optimization by avoiding overprovisioning of resources.
- Improved system reliability during production surges.
- Consistent data processing regardless of production volumes.
- Enhanced ability to capture critical manufacturing data during unexpected events.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

**Design scalable data ingestion architecture**

Assess your manufacturing data sources, volumes, and velocity requirements. Document
peak production periods, shift patterns, and seasonal variations that affect data generation
rates.

Identify critical data streams that require guaranteed delivery and establish
performance baselines for normal operations.

Define acceptable latency thresholds for different types of manufacturing data.

For implementation, create a flexible ingestion architecture that can automatically
adapt to changing production volumes. Design ingestion paths with appropriate buffering and
throttling mechanisms to handle sudden surges in manufacturing data.

Consider using AWS IoT Core and AWS Lambda for serverless ingestion points that
automatically scale with the volume of incoming sensor data from manufacturing equipment.

**Configure stream processing capabilities**

Map your data processing requirements and identifying real-time analytics needs.

Document throughput requirements for different production scenarios and establish
monitoring thresholds.

Define scaling triggers based on production metrics rather than just system metrics.

For implementation, establish stream processing mechanisms that can handle variable
throughput from production lines while maintaining data consistency. Include automatic
scaling capabilities based on actual production demands and data volumes.

Consider setting up Amazon Kinesis Data Streams with appropriate shard management to
handle varying throughput from production lines.

**Implement data flow controls**

Analyze your data priority levels and establish handling rules for different data
types.

Define quality of service requirements for critical manufacturing data and document
acceptable processing delays for non-critical data.

Establish clear overflow handling procedures for peak production periods.

For implementation, deploy mechanisms to manage data flow rates and help prevent system
overload during production peaks. Create prioritization schemes that process critical
manufacturing data first during high-load periods.

Consider implementing Amazon SQS queues between data collection points and processing
systems to handle sudden surges in manufacturing data.

**Establish comprehensive monitoring**

Define key performance indicators for your data ingestion system. Document alerting
thresholds based on production requirements and establish escalation procedures.

Create baseline metrics for normal operations across different production scenarios.

For implementation, deploy monitoring systems that track both technical metrics and
production-related indicators. Configure automated alerts for potential bottlenecks or
capacity issues before they impact production.

Consider using Amazon CloudWatch to track performance metrics and adjust scaling
parameters based on historical production patterns and seasonal manufacturing demands.

## Key AWS services

- Amazon Kinesis Data Streams
- AWS Lambda
- Amazon SQS
- AWS IoT Core
- Amazon CloudWatch
- AWS Auto Scaling

## Resources

- [Auto Scaling for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
- [Serverless event-driven architecture for industrial data
ingestion](https://docs.aws.amazon.com/serverless/latest/devguide/serverless-transition.html)
- [Implementing the IoT analytics pipeline for
manufacturing](https://docs.aws.amazon.com/iotanalytics/latest/userguide/create-pipeline.html)
- [Designing scalable IoT applications with
AWS](https://aws.amazon.com/blogs/iot/how-to-build-a-scalable-multi-tenant-iot-saas-platform-on-aws-using-a-multi-account-strategy/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel03-bp01.html*

---
