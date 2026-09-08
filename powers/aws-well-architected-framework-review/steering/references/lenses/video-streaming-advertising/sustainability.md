# Sustainability

**Pillar**: Sustainability  
**Questions**: 10

---

# ADVSUS01 — Region selection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS01-BP01 Distribute data and workloads across Regions when necessary to minimize network usage and latency

When selecting regions to host workloads for sustainability,
distribute data and workloads across multiple Regions to minimize
network usage and latency, prioritising the most sustainable
Regions available that leverage renewable energy sources. The
millisecond latency of programmatic advertising workloads
typically requires ad-servicing architectures be near consuming
workloads. However, there is opportunity to consolidate data
analysis for these workloads into fewer Regions.

## Implementation guidance

- Identify the latency requirements for your workloads, and
determine which AWS Regions can meet those requirements.
- From the eligible regions, select the one with the lowest carbon footprint,
considering factors such as the energy mix (prioritize Regions with 100% renewable
energy).
- Use AWS tools to measure and report your carbon footprint.
- Consolidate infrastructure needs for analytics workloads
(real-time bidding, privacy-enhanced data collaboration, ad
intelligence, and measurement) in fewer AWS Regions with
100% renewable energy.
- Use AWS services designed for energy efficiency, such as
Amazon EBS gp3 volumes, Amazon EC2 Instances with AWS
Graviton processors, and Amazon EC2 Tranium and Inferentia
instances for AI workloads.
- Periodically review and optimize the regional distribution
of workloads as new, more sustainable AWS regions become
available, balancing sustainability goals with performance
requirements.
- Aggregate analytical data in local regions and move the
aggregates to the central reporting region when data needs
to be centralized for business reasons.

## Key AWS services

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/)
- [Amazon EBS volume types](https://aws.amazon.com/ebs/volume-types/)
- [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus01-bp01.html*

---

# ADVSUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 2

---

# ADVSUS02-BP01 Break down system components to determine which are business critical and compare the trade-offs

When aligning SLAs with sustainability goals for advertising
workloads, break down system components to identify
business-critical elements, and evaluate trade-offs to balance
SLAs with environmental objectives while minimizing waste.

## Implementation guidance

- Categorize workloads by business impact, customer impact,
and latency, monitor performance, and set SLA requirements
accordingly to optimize resource allocation.
- For batch workloads like privacy-enhanced data
collaboration, consider scheduling them to run during
periods when the carbon footprint is lower, such as time of
the day or week when more renewable energy is available or
when demand is lower.
- For time-sensitive and business-critical workloads like
real-time bidding, prioritize meeting SLA requirements, even
if it means running during peak demand periods with a higher
carbon footprint.

## Key AWS services

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) (Automatically scales resources)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) (Recommends optimal compute
resources)
- [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) (Schedules starting/stopping
instances)
- [AWS Spot
Instances](https://aws.amazon.com/ec2/spot/) (Discounted spare compute capacity)
- [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (Energy-efficient ARM processors)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus02-bp01.html*

---

# ADVSUS02-BP02 Identify redundant infrastructure and unnecessary data movement to reduce usage where possible

Identify and eliminate redundant infrastructure components and
unnecessary data movement within your advertising workloads, as
this can help reduce resource usage, lower the overall carbon
footprint, and improve sustainability-related key performance
indicators (KPIs).

## Implementation guidance

- Audit your advertising workload infrastructure to identify
any redundant or underutilized resources, such as idle
instances, oversized instances, or unnecessary data
replication.
- Analyze data movement patterns and network traffic to
identify opportunities for reducing data transfers,
especially over long distances or between regions. Use
Amazon CloudFront to cache and serve ad files closer to
consumers.
- Implement auto scaling and right-sizing mechanisms to
automatically adjust resource allocation based on actual
workload demands, minimizing over-provisioning. For example,
with real-time bidding workloads that use Amazon EKS,
implement a scaling policy that is determined by the number
of bids being served, which optimizes resource usage.
- Consolidate workloads and data storage where possible,
reducing the overall infrastructure footprint and associated
energy consumption. Implement lifecycle policies to remove
old ad file assets that are no longer needed.
- Establish monitoring and reporting processes to track
resource utilization, data movement, and sustainability KPIs
over time, enabling continuous optimization.

## Key AWS services

- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) (Identify optimization opportunities)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) (Visualizes and analyzes cost/usage
data)
- [AWS Config](https://aws.amazon.com/config/) (Monitors and records resource configurations)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) (Cache and serve ad files)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) (Logs API calls and events)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) (Automatically scales resources)
- [AWS Lambda](https://aws.amazon.com/lambda/) (Serverless computing)
- [AWS Data Transfer Cost Estimator](https://calculator.aws/#/createCalculator/DataTransfer) (Estimates data transfer
costs)
- [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) (Remove unneeded ad assets)
- [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) (Provides architecture best
practices)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus02-bp02.html*

---

# ADVSUS03 — Data caching

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS03-BP01 Use caching techniques to prevent frequent data access

Implement caching techniques to store frequently accessed data in
cache, preventing repeated data retrieval and thereby reducing
computing time and energy consumption for advertising workloads.

## Implementation guidance

- Implement caching strategies for advertising content and
data to minimize frequent data access and reduce computing
time and energy consumption.
- Use AWS caching services like
[Amazon ElastiCache](https://aws.amazon.com/elasticache/) (for in-memory caching) and
[Amazon CloudFront](https://aws.amazon.com/cloudfront/) (for content delivery network caching) to
store frequently accessed data closer to the consumers,
reducing latency and compute requirements.
- Consider using
[AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/) and CloudFront Functions to run
lightweight logic at edge locations, minimizing the need for
data transfer to centralized servers and reducing overall
energy consumption.

## Key AWS services

- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) (for optimizing data transfer over
the AWS Cloud)
- [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (for energy-efficient compute
instances)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus03-bp01.html*

---

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

# ADVSUS05 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS05-BP01 Identify and remove redundant data across storage

Participants in the real-time advertising supply chain can accrue
large volumes of data. Consider how you use data and data
preservation as outlined in ADPERF04-BP01. Don't keep data that
has no purpose, can easily be recreated, and expedite the removal
of low value or short-lived data. Remove unwanted advertisement
video, images, files, and any other associated data that is no
longer needed.

## Implementation guidance

- Optimize data handling needs based on workload requirements,
and verify that it reflects the nature of the business and
short-lived advertising content (delete or archive based on
data class).
- Consider if duplicate ad files or versions of ad files are
be being saved that can be easily recreated.
- Use
[Amazon S3 storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) rules to automate the expiration
(and deletion) of draft ad content versions. For content
that should be preserved for historical purposes, use Amazon S3 storage lifecycles to transition content to another
storage class, such as Amazon Glacier.
- [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-optimize-storage.html) can identify incomplete multipart
uploads, buckets that have numerous noncurrent versions, and
if lifecycle rules are not present. Storage Lens can also
provide activity metrics to identify ad objects or even
prefixes that are infrequently used.
- [AWS Config](https://aws.amazon.com/config/) can also identify if you have unused
resources, such as
[EBS
volumes](https://aws.amazon.com/ebs/).
- Use
[Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to expire old images used for
real-time bidding containers.
- Evaluate how users are using data to eliminate use cases,
dimensions, and queries that no longer provide value.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus05-bp01.html*

---

# ADVSUS06 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 2

---

# ADVSUS06-BP01 Shut down resources when not in use, and implement energy-efficient machine learning models

Resources for machine learning may have real-time demands that
fluctuate or not be needed at certain times, such as when data can
be processed as a batch. Set machine learning workloads to respond
to demand in real-time, including turning off or shutting down
resources when not needed. Use available tools to optimize the
compute resources and models used for machine learning workloads.

## Implementation guidance

- Organizations can use machine learning to draw insights on
correlation and causation from data sets in order to
optimize advertising activities. However, resources for data
preparation, identity resolution, data collaboration, and
creation of machine learning models do not need to run 24/7.
Optimize and shut down these resources when not in use to
reduce carbon emissions.
- When using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), customers can take multiple steps to
optimize their compute usage:

Use Graviton-based instances when possible.
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) can specify the
most performant instance type.
- [Inference
optimization techniques](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) can be applied to
SageMaker AI models.
- SageMaker AI can dynamically adjust the number of instances
provisioned for a model in response to changes in your
workload by
using [scaling
policies](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html).

- Use AI chips that provide the highest performance for
training and inference, such as
[AWS Tranium](https://aws.amazon.com/ai/machine-learning/trainium/) and
[AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus06-bp01.html*

---

# ADVSUS06-BP02 Continuously monitor and right-size your AWS resources, and use the minimum resources required to meet your workload needs

Monitoring workloads allows you to optimize and elastically scale
your workloads to meet demand. Using serverless offerings can also
help you automatically scale to reduce resource usage and improve
the ability to meet sustainability targets. Consider how your
requirements change based on advertising campaigns, and take
advantage of the elasticity and agility of cloud to optimize your
resource usage.

## Implementation guidance

- Advertising SSPs and DSPs should use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards for visibility into active connections and bytes process
per endpoint to drive resource usage.
- Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify
the optimal resources for workloads. For example, when using [Amazon EMR](https://aws.amazon.com/emr/) to analyze ad impression and click-through data, Compute Optimizer can
recommend the optimal EC2 instance types based on utilization data.
- Monitor boot time for improvements, such as pre-installing dependent libraries in
container images for bidder processing.
- For downstream analytics and reporting of bidder transactions, use [Amazon Kinesis](https://aws.amazon.com/pm/kinesis/) Data Streams and Amazon Data Firehose to send
data to Amazon S3. The use of a data stream enables faster responses and allows independent
scaling for components of the real-time bidding architecture.
- Ad servers and click-through servers should be in [Auto Scaling
groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) to automatically scale in when load is reduced.

## Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Karpenter](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/) (Open-Source Kubernetes cluster autoscaler built with AWS)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus06-bp02.html*

---

# ADVSUS07 — Process and culture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS07-BP01 Incorporate an improvement process to reduce low utilization and idle resources or maximize the output from resources

Advertising workloads are changing at a rapid rate. As changes are
introduced consider which resources are the most efficient and
where resources can be removed. Use automation to create and
remove infrastructure as needed.

## Implementation guidance

- Establish a cadence to revisit SLAs with advertising partners.
- Prioritize how to reduce use when over-provisioning is identified (for example,
start with compute, then storage, then network usage).
- Continue to iterate with advertising partners on reducing the infrastructure needed
for a minimum viable representation of production for testing.
- Use [infrastructure as code (IaC)](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) to set up a test environment, so they can be
removed when a testing or staging environment is no longer needed but easily recreated
when beneficial.

## Resources

- [Well-Architected Lab - Optimize Hardware Patterns and Observe Sustainability
KPIs](https://wellarchitectedlabs.com/sustainability/200_labs/200_optimize_hardware_patterns_observe_sustainability_kpis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus07-bp01.html*

---

# ADVSUS08 — Privacy-enhanced collaboration

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS08-BP01 Optimize privacy workload processing patterns and resource allocation for sustainability

For privacy-enhanced collaboration, advertising workloads have specific sustainability considerations for combining first and third-party customer data directly.

## Implementation guidance

- Schedule intensive privacy computations during periods of
lower carbon intensity.
- Use batch processing for data cleansing and matching
operations.
- Implement efficient data compression and formatting using
formats such as Parquet.
- Leverage AWS Graviton processors for energy-efficient
computing.
- Use serverless architectures for matching operations where
possible.
- Implement auto scaling based on actual collaboration
workload patterns.
- Configure Regional data aggregation before central
processing to reduce transfer needs.

## Key AWS services

- AWS Lambda
- AWS Graviton Processors
- AWS Auto Scaling

## Resources

- [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)
- [AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/optimization.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus08-bp01.html*

---

# ADVSUS09 — Ad intelligence, measurement, and security

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS09-BP01 Optimize fraud detection systems for resource efficiency

Fraud detection systems can perform efficiently and have a reduced carbon impact when using approaches such as intelligent sampling, scheduled analysis, and Regional detection.

## Implementation guidance

- Use energy-efficient processing for continuous fraud
monitoring. If running compute instances, select AWS
Graviton processors.
- Implement intelligent sampling for fraud detection where
appropriate to reduce computational overhead while meeting
business requirements.
- Schedule intensive fraud pattern analysis during
low-carbon periods.
- Use serverless architectures for variable detection
workloads.
- Use efficient data storage patterns for fraud signals and
patterns. Archive data that is not readily needed and
remove data that is no longer required for
compliance/security purposes.
- Use AWS Clean Rooms for measurement analysis across
partners, with the ability to analyze data sets where they
are, with no data movement.
- Implement caching for frequently accessed fraud detection
rules.
- Configure Regional detection systems to minimize data
transfer.

## Key AWS services

- Amazon EC2 with Graviton processors
- AWS Lambda
- Amazon ElastiCache
- AWS Clean Rooms
- Amazon CloudWatch

## Resources

- [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus09-bp01.html*

---

# ADVSUS10 — Moderation and brand safety

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS10-BP01 Optimize content moderation systems for sustainable operation

As content grows for organizations, optimizing content moderation systems can benefit sustainability-related key performance indicators (KPIs). Implement or build architectures that include efficient machine learning models, automated scaling, and optimized storage patterns.

## Implementation guidance

- Use efficient machine learning models for content
classification. Use AWS Inferentia chips when possible,
for improved performance per watt.
- Implement batch processing for non-real-time moderation
tasks.
- Configure regional content analysis to minimize data
movement.
- Use caching strategies for frequently accessed moderation
rules.
- Use energy-efficient computing resources, such as AWS
Graviton, for moderation workloads.
- Implement automated scaling based on moderation demand
using auto scaling rules and Amazon CloudWatch metrics.
- Optimize storage patterns for moderation results and audit
trails. For workloads using Amazon S3, use Storage Lens for
insights and recommendations to optimize storage use.

## Key AWS services

- Amazon Rekognition
- AWS Inferentia
- Amazon SageMaker AI
- AWS Auto Scaling
- AWS CloudWatch
- Amazon ElastiCache
- Amazon S3 Storage Lens

## Resources

- [Optimize AI/ML workloads for sustainability: Part 1, identify business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus10-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
