# ADVSUS04 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 2

---

# ADVSUS04-BP01 Use batch processing for data cleansing and enrichment to create customer profiles

Use batch processing for data cleansing and customer profile
enrichment in advertising workloads. Schedule the batch jobs
during periods of lowest carbon consumption to minimize resource
usage and environmental impact.

## Implementation guidance

- For workloads like privacy-enhanced data collaboration that
involve data cleansing, enrichment, and customer profile
creation, implement batch processing architectures to
minimize resource usage.
- Use AWS services like
[AWS Batch](https://aws.amazon.com/batch/) and
[AWS Step Functions](https://aws.amazon.com/step-functions/) to queue up and schedule these batch
jobs during periods when the carbon intensity is lower, such
as times when more renewable energy is available or when
demand is lower.
- Consider using
[AWS Graviton](https://aws.amazon.com/ec2/graviton/)-based instances if supported, for batch
processing workloads, if as they offer energy-efficient
compute capabilities.
- Sample data sets when possible, to reduce compute,
analytics, and data transfer needs.

## Key AWS services

- [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) (for scheduling batch jobs during
low-carbon periods)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus04-bp01.html*

---

# ADVSUS04-BP02 Use serverless transaction processing

Implement serverless transaction processing, such as for ad
measurement, to reduce the required unit of work and associated
resource consumption for your advertising workloads.
[Proxy
metrics](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html#proxy-metrics), as defined in the Well-Architected Framework
Sustainability Pillar, can be used to measure improvements from
serverless use. For instance, instead of having long-running vCPU
usage and partially-used volumes in a number of workload
instances, use a serverless approach, so compute usage only occurs
at the time of a transaction.

## Implementation guidance

- For ad measurement workloads, use serverless architectures
to minimize the required infrastructure and resources per
unit of work.
- Implement services like
[Amazon API Gateway](https://aws.amazon.com/api-gateway/),
[AWS Glue](https://aws.amazon.com/glue/),
[AWS Lambda](https://aws.amazon.com/lambda/),
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), and
[Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) to build event-driven, scalable, and
efficient ad measurement pipelines.
- These services automatically scale up or down based on
demand, improving resource utilization and reducing waste.
- Serverless architectures can help minimize idle resources,
further contributing to sustainability goals.

## Key AWS services

- [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (for energy-efficient compute
instances, if using EC2 instances)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) (for optimizing resource
utilization, if using EC2 instances)
- [Proxy
Metrics](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html#proxy-metrics) (AWS Sustainability Pillar)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus04-bp02.html*

---
