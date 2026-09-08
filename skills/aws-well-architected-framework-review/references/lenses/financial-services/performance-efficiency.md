# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 9

---

# FSIPERF01: How do you select the best performing architecture?

Performance objectives for workloads can vary depending on the criticality of the
workload. While more stringent performance requirements are expected for critical systems
such as core banking, payments processing, trade performance, and market data feeds, all
cloud workloads benefit from defining performance requirements.

## FSIPERF01-BP01 Use internal and external risk to determine performance requirements

External regulatory, as well as internal risk requirements, are often a good place to
start for performance requirements. For some systems, regulators release sector-wide
guidance including potential stress tests. For others, regulators require that financial
institutions have the capability to deliver on the operational resilience and the
performance targets they have set for themselves.

## FSIPERF01-BP02 Factor in rate of increase in load and scale-out intervals

Identify the upper bounds of the peak load against a system, as well as the amount of
time needed to reach peak load. Load tests often overlook the rate of increase in traffic
and create tests that scale up too quickly or too slowly. If the load test ramps up too
quickly, the system may not be able to add capacity rapidly enough to meet the demand,
which degrades performance and introduces errors. Load tests need to be run periodically
and with every major release of the system.

## FSIPERF01-BP03 Benchmark your solution

Benchmark your existing solution and its components in order to understand their
performance characteristics and capacity to exceed their current profiles. AWS services
like AWS Lambda and CloudWatch can be useful tools for building, running and monitoring a load
testing environment due to their low overhead for setup and extensive scaling
capabilities. For more information, see [AWS Prescriptive Guidance
for load testing](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/welcome.html) and [Distributed Performance
Testing](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf01.html*

---

# FSIPERF02: How do you select your compute architecture?

## FSIPERF02-BP01 Select your compute architecture based on workload requirements

The optimal compute solution for a particular architecture depends on the workload
deployment method, degree of automation, usage patterns, and configuration. Third-party
solutions can bring their own requirements for infrastructure, which must also be
considered. Different compute solutions may be chosen for each step of a process.
Selecting the wrong compute solutions for an architecture can lead to lower performance
efficiency.

Some financial services computing workloads, like risk modeling, are typically
loosely coupled and can benefit from event-driven architectures leveraging the scaling
capacity of AWS serverless compute options like AWS Lambda and AWS Fargate, combined
with messaging services including Amazon SQS and Amazon EventBridge to decouple components. These
serverless solutions minimize the overhead of capacity management, automatically scaling
in or out to meet demands.

Containerized infrastructure can enable financial services institutions to achieve
their goals for speed and scalability by providing a standardized environment to leverage
across multiple solutions, and supporting the development of microservice-based
architectures. Where scale is the primary factor, AWS serverless container compute
engine, AWS Fargate, can be used with both Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS),
removing the overhead of managing and provisioning compute resources.

For solutions with more specific performance requirements, or needing to run on
virtual machines as their compute solution, AWS offers a wide range of Amazon Elastic Compute Cloud (Amazon EC2)
instance types, which you can use to select the configuration that is best suited to your
needs at any given time. This allows you to both take advantage of the latest CPU
technologies as they are released without consideration for prior investment, and choose
instance types with features that best suit your workload's requirements, for example
instance variants optimized for network, storage, or compute performance.

The [Financial Services Grid Computing on AWS](https://docs.aws.amazon.com/whitepapers/latest/financial-services-grid-computing/grid-computing-on-aws.html) whitepaper explores this topic in
more detail for specific workloads.

## FSIPERF02-BP02 Select appropriate GPU and accelerated computing for AI workloads

Financial services AI workloads require careful selection of
compute infrastructure to balance performance, cost, and
regulatory requirements. Different AI use cases within
financial services have varying compute requirements that
should guide infrastructure selection.

**GPU instance selection:**

- P4d instances for large-scale model training and fine-tuning
of foundation models on financial datasets
- P5 instances for the most demanding AI training workloads
requiring maximum GPU performance
- G5 instances for real-time AI inference workloads like fraud
detection and trading algorithm
- G4dn instances for cost-effective AI inference at scale for
applications like document processing and customer service
chatbots
- Inf2 instances powered by AWS Inferentia2 chips for
high-throughput, low-cost inference of transformer models

**Implementation
considerations:**

- Use Amazon EC2 Spot Instances for non-critical AI training
workloads to reduce costs.
- Use Elastic Fabric Adapter (EFA) for distributed AI training
across multiple instances.
- Consider AWS Batch for managing AI training jobs that can
run on mixed instance types.
- Use Amazon SageMaker AI managed infrastructure for production
AI workloads with built-in optimization.

**Accelerated computing for specific
financial AI workloads:**

- Use G5 instances with GPU memory optimized for low-latency
inference.
- Use parallel computing capabilities of P4d instances for
risk modeling and Monte Carlo simulations.
- For document processing and regulatory compliance, use Inf2
instances for transformer-based document analysis.
- Consider F1 instances with FPGAs for ultra-low latency
requirements and algorithmic trading.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf02.html*

---

# FSIPERF03: How do you select your storage architecture?

AWS offers a wide range of storage options and as with compute, the best performance
is obtained when targeting the specific storage needs of an application.

## FSIPERF03-BP01 Select your storage architecture based on workload requirements

When you select a storage solution, verify that it aligns with your access patterns to
achieve the desired performance. It is simple to experiment with different storage types
and configurations without having to make commitments.

Financial services grid compute workloads can take advantage of Amazon FSx for Lustre, which
provides a fully managed file system that’s optimized for the performance and costs of
workloads requiring file system access across thousands of Amazon EC2 instances, optionally
backed by an S3 bucket, which makes it simple for clients to persist input and results of
the calculations.

Consider whether your solutions can make use of caching services to improve
performance, by storing frequently used data in memory, or bringing data closer to
consumers. Many AWS services offer features for caching or dedicated services including
Amazon ElastiCache, and Amazon File Cache.

Financial services solutions have historically made use of databases as a key
component, often to verify transactional integrity, and here AWS also offers a wide
range of database options. Select database options that align with your performance
requirements, using different database technologies for different purposes, such as
Amazon Timestream time-series database for storing ticking market data, rather than a
one-size-fits-all use of traditional relational databases.

## FSIPERF03-BP02 Consider changing needs over the entire lifecycle of your data

Financial services workloads often have requirements to keep data available for many
years to help meet regulatory requirements, leading to significant amounts of data being
retained. Amazon S3 and Amazon Glacier storage classes provide the optimal solution for many data
retention requirements with their almost unlimited capacity and predictable performance.
Consider the use of the services’ own lifecycle policies (supported by Amazon Elastic File System and Amazon S3
among others) to help meet your requirements. These services offer integrated
lifecycle-based policies for moving data between tiers of storage based on access patterns
and user-defined requirements. If the features of a single service do not meet your
requirements, combine multiple storage services to satisfy requirements, rather than
selecting a single storage service to help meet your requirements, for example persisting
Amazon FSx for Lustre file systems to Amazon S3 for long-term, low-cost retention. Note that costs
for the service remain low, provided that the services are restricted to a single
AWS Region.

## FSIPERF03-BP03 Optimize storage for AI model and data requirements

AI workloads in financial services generate unique storage
requirements due to large model files, extensive training
datasets, and real-time inference data needs. Optimize storage
architecture to support AI model lifecycle management and data
processing pipelines.

**Storage optimization
strategies:**

- Use Amazon S3 with S3 Transfer Acceleration for fast model
artifact uploads and downloads.
- Use Amazon FSx for Lustre for high-throughput access to
large financial datasets during model training.
- Use Amazon ElastiCache to cache frequently accessed model
predictions and reference data.
- Implement S3 versioning and lifecycle policies for model
artifact management.

**Performance considerations for
financial AI storage:**

- Use Amazon EBS gp3 volumes with provisioned IOPS for
consistent I/O performance during model training.
- Implement data partitioning strategies to optimize access
patterns for time-series financial data.
- Configure cross-region replication for disaster recovery of
critical AI models and training data.
- Use Amazon S3 Intelligent Tiering to automatically optimize
costs for infrequently accessed training datasets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf03.html*

---

# FSIPERF04: How do you select your network architecture?

Use performance requirements to drive the selection of network components and
architecture.

## FSIPERF04-BP01 Use AWS services to optimize your network routes

Proximity to data sources, both internal and external, and the distance between
components can be a key factor for financial services workloads, like high-frequency
automated trading systems, so make use of AWS services to sit your solution as close as
possible to dependencies. Where this location is outside of an AWS Region, make use of
AWS edge location solutions such as AWS Outposts and AWS Local Zones to deploy workloads
in the most suitable location, making the trade-off that not all AWS services may be
compatible with these. For example Low Latency Trading has strict latency service level
agreements (SLAs), where a millisecond can make the difference between completing a
transaction or missing an opportunity, and due to these low latency requirements, brokers'
low latency trading systems must be in close proximity to the exchanges.

Use AWS Direct Connect to provide the shortest and most reliable path to AWS resources
for components hosted outside of AWS. Use Amazon CloudFront to cache static content closer to use
cases, and AWS Global Accelerator to route connections to the closest possible source, leveraging the
AWS backbone network and bringing your solutions closer to markets, users, and data.
When using multiple AWS Regions, use Route 53 latency-based routing to serve requests from
the AWS Region with the lowest latency.

## FSIPERF04-BP02 Use Amazon EC2 instances and features to optimize your networking

Consider network performance when selecting Amazon EC2 instances, with specific network
optimized variants indicated by the n-suffix, and bare metal instances offering direct
access to the underlying host, further optimizing the networking stack.

Within an Amazon VPC, when inter-process communication latency, throughput, and consistency
is a consideration, use Amazon EC2 Placement Groups to have greater control over the location
of your virtual instances and optimize network communication, resulting in improved
network performance reduction in latency and increased packet processing rates. The use of
cluster placement groups is covered in greater detail in the[Crypto market-making latency and Amazon EC2 shared placement groups](https://aws.amazon.com/blogs/industries/crypto-market-making-latency-and-amazon-ec2-shared-placement-groups/) blog post
on optimizing market-making systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf04.html*

---

# FSIPERF05: How do you select and optimize generative AI components for your workload?

Selecting and optimizing generative AI components requires
defining your use case requirements—including accuracy
thresholds, latency constraints, and compliance needs—then
evaluating foundation models using automated benchmarks and
task-specific criteria before optimizing through prompt
engineering or fine-tuning. This enables you to build
generative AI systems that deliver reliable business value
while meeting the rigorous standards required for production
deployment, particularly in regulated industries like
financial services.

## FSIPERF05-BP01 Define a ground truth data set of prompts and responses for financial services use cases

For financial services applications using generative AI,
develop a ground truth dataset that captures domain-specific
prompts and expected responses. This dataset should include
scenarios relevant to financial applications such as
regulatory adherence queries, transaction anomaly detection,
risk assessment, and customer service interactions common in
financial institutions.

**Implementation steps:**

- Define a series of prompts and expected responses specific
to financial services use cases.
- Create a structured dataset that organizes these
prompt-response pairs by business domain (like banking,
trading, and risk management).
- Store this dataset in a secure object storage or database
with appropriate access controls given the sensitive
nature of financial data.
- Develop a testing harness that can evaluate model
performance against these financial services scenarios.

## FSIPERF05-BP02 Select and customize models appropriate for financial services use cases

When implementing generative AI models in financial services
workloads, evaluate model performance against
domain-specific requirements including regulatory adherence,
accuracy in financial terminology, and consistency in risk
assessment. Consider model customization through fine-tuning
or continuous pre-training to improve performance on
financial domain knowledge and financial
institution-specific scenarios.

**Implementation steps:**

- Test multiple models against your financial services
ground truth dataset.
- Consider customizing models using techniques like
fine-tuning to improve performance on financial tasks.
- Evaluate model response consistency and accuracy,
particularly for regulated processes.
- Consider model distillation techniques for deploying
smaller, more efficient models in production that maintain
accuracy for specific financial tasks.

## FSIPERF05-BP03 Optimize vector stores for financial data retrieval

Financial services applications often require high-precision
data retrieval from large datasets of financial information,
regulatory documents, or transaction histories. Optimize
vector databases to enhance the retrieval accuracy and speed
when used in conjunction with generative AI models.

**Implementation steps:**

- Test different chunking strategies for financial
documents, considering their specialized structure.
- Select appropriate approximate nearest neighbor (ANN)
algorithms based on the precision and recall requirements
for financial use cases.
- Optimize vector dimensions based on the complexity and
specificity of financial information.
- Implement hierarchical indices that allow efficient
navigation from general financial concepts to specific
details.
- Regularly test and monitor performance metrics including
latency, throughput, and accuracy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf05.html*

---

# FSIPERF06: How do you evaluate compliance with performance requirements?

Here are several methods for doing so:

- Monitoring of your workload at multiple levels helps verify
that your resources are performing as expected and you are
aware of deviations.
- Consider all dimensions of the solution for monitoring, for
example client-side and server-side metrics, application
metrics and infrastructure metrics, technical and functional
metrics.
- Monitor for failure rates and alert when they are above
expected values.
- Identify KPIs and create threshold alerts for them and
determine what actions to take (like autoscaling) when
thresholds are breached - this allows you to observe the
overall health of your system and identify
[non-binary,
or grey, failure states](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.html).
- Provide visibility of data loss in your metrics, for example
by monitoring for lost messages.
- Where possible capture inter-solution and inter-process
communication streams to aid with the reproduction of
issues.

## FSIPERF06-BP01 Use Application Performance Monitoring (APM) tools

Use APM tools to provide your organization the capability to verify that application
performance meets its defined requirements. AWS offers features and services to monitor
and subsequently right-size the cloud services that you need to meet performance
requirements.

For example, you can monitor and set alarms on latency and error rates for each user
request using Amazon CloudWatch metrics and alarms, or on your downstream dependencies, or on the
success and failure of key operations. Amazon CloudWatch Synthetics can be used to create
*canaries*, configurable scripts that run on a schedule, or to
monitor your endpoints, and APIs.

The required level of monitoring generates huge amounts of data, which can be
challenging for operation teams to store, analyze, and visualize, so make use of services
including Amazon Managed Service for Prometheus to monitor and alert on containers, Amazon Managed Grafana to visualize metrics and
logs, and the wide range of features found in Amazon CloudWatch, to provide the appropriate tools
for monitoring your systems without the overhead of managing additional infrastructure.
Teams need training to update their skills and processes and take full advantage of this
new fidelity of insight.

## FSIPERF06-BP02 Integrate performance testing into the release cycle

Rather than considering performance testing to be a separate part of the workload
release cycle, integrate performance testing into your release process and CI/CD tooling.
This allows you to record and evaluate performance metrics across releases, being aware of
and taking action when metrics change as early as possible.

## FSIPERF06-BP03 Verify consistency and failure recovery during load tests

You must verify data consistency and recovery during periods of high load. Ensuring
that your workload's RTO and RPO is still valid under the highest load can uncover gaps in
your architecture and operational resilience.

## FSIPERF06-BP04 Understand performance of the system under peak load and in failure scenarios

Include testing of common failure scenarios in your performance testing suites to
understand your workload behaviour in these situations and determine areas for
improvement.

Extend the range of performance testing scenarios to cover testing at loads beyond
current peak loads, and testing the scaling processes themselves of the application to
understand how the environment behaves under increasing load.

Under common or anticipated failure scenarios, workloads should exhibit predictable
failure patterns with performance degrading gracefully using techniques such as [fail-open behavior,](https://www.wellarchitectedlabs.com/reliability/300_labs/300_health_checks_and_dependencies/4_fail_open/) and the transformation of [hard dependencies into soft dependencies.](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html)

## FSIPERF06-BP05 Include dependencies in your load tests

Financial institutions need to map resources they need to continuously deliver their
important business services. These resources are your people, processes, technology,
facilities, and information, including third-party service providers. This mapping allows
the identification of operational dependencies, vulnerabilities, and threats.
Incorporating the dependencies of your workload (such as on financial messaging providers)
as part of your performance tests enables you to demonstrate the overall resiliency of
your workload.

## FSIPERF06-BP06 Collect and analyze generative AI performance metrics

For financial services workloads using generative AI,
implement comprehensive monitoring of model performance,
including response latency, accuracy metrics, and token usage.
Set up monitoring specifically for regulatory adherence
concerns, such as bias detection and unexpected outputs that
might impact financial decisions or customer interactions.

**Implementation steps:**

- Configure CloudWatch metrics for AI services like Amazon
Bedrock or Amazon SageMaker AI endpoints.
- Implement trace frameworks like OpenLLMetry to capture model
performance metrics.
- Establish alert thresholds specific to AI components in
financial workloads.
- Create dashboards that visualize AI model performance
alongside other application metrics.
- Set up automated remediation actions for common performance
issues.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf06.html*

---

# FSIPERF07: How do you make trade-offs in your architecture?

Financial services workloads often have to make trade-offs in their architecture to
meet their most important goals and KPIs, where performance of the system is deemed more
important than other factors, or vice-versa.

## FSIPERF07-BP01 Understand your priorities and architect to meet them

For example, a low-latency trading system needs to preserve the performance of the
system above all other factors, and be prepared to compromise on the cost of
infrastructure to meet their goals. In this situation it is still important not to
compromise on availability, and this may require significant investment in parallel,
independent, deployments for example an independent deployment of the application stack in
multiple AWS Availability Zones or Regions rather than a failover architecture.

Within the workload it may be necessary to trade-off between persistent capacity and
elasticity to make sure that the application always has the ability to handle peak
workloads without needing timed or reactive scaling up. Consider how much of your peak
workload you need to be able to service at any time.

When choosing services consider performance determinism. AWS serverless services
like AWS Lambda and AWS Fargate can bring significant performance benefits due to their
ability to scale elastically on demand, without intervention, but this is often coupled
with less fine control over the underlying environment, for example CPU clock speed, and
this can introduce an element of variability into workload performance. Where the workload
performance must be as consistent as possible, consider using Amazon EC2, where you get the
widest choice, and greatest level of control, over the production environment. For
example, using Amazon EC2 directly enables the use of [ENA Express](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html), to increase network
throughput and reduce latency, but brings restrictions on the Amazon EC2 instances that support
this feature.

Consider trade-offs in your application architecture. For example, to preserve
network latency you may choose to use certain services and configurations that are more
complex to implement and maintain, but offer better performance, such as using [VPC Peering instead of AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/best-practices-and-considerations-to-migrate-from-vpc-peering-to-aws-transit-gateway/) to minimize the number of network hops for
your most critical traffic. For optimal connectivity to on-premises workloads consider the
best position for your AWS Direct Connect Gateway to bring it closest to the most sensitive
workloads.

## FSIPERF07-BP02 Balance AI model complexity with performance requirements

For financial services applications utilizing generative AI,
carefully evaluate the trade-offs between model complexity,
response quality, and performance. For time-sensitive
financial applications like real-time fraud detection or
trading analysis, consider using smaller, specialized models
that can provide faster response times. For less
time-sensitive tasks like regulatory documentation analysis,
larger models with higher accuracy might be more appropriate.

**Implementation steps:**

- Evaluate different model sizes and architectures against
your ground truth dataset.
- Consider using model distillation to create smaller, faster
models for time-sensitive financial applications.
- Test prompt caching for common financial queries to reduce
latency.
- Implement streaming responses for improved perceived latency
in user-facing applications.
- Consider using model routers to direct different types of
financial queries to the appropriate model based on
complexity and time sensitivity.

## FSIPERF07-BP03 Optimize cost-performance trade-offs for AI infrastructure

Financial services organizations must carefully balance the
costs of high-performance AI infrastructure with the business
value generated by AI applications, considering regulatory
requirements and competitive advantages.

**Cost optimization
strategies:**

- Use EC2 Spot instances for AI training workloads that can
tolerate interruptions.
- Commit to reserved capacity for predictable AI inference
workloads to reduce costs.
- Deploy multiple models on shared infrastructure to improve
resource utilization.
- Implement time-based scaling for AI workloads with
predictable usage pattern.

**Performance and cost
considerations:**

- Balance model accuracy requirements with inference costs and
latency constraints.
- Evaluate GPU costs against performance benefits for specific
financial AI use cases.
- Consider trade-offs between real-time processing costs and
batch processing latency.
- Balance performance benefits of edge deployment with
infrastructure costs.

**Implementation guidance:**

- Use AWS Cost Explorer and AWS Trusted Advisor to identify AI
infrastructure optimization opportunities.
- Implement budget alerts and cost allocation tags for AI
workload cost management.
- Configure SageMaker AI inference endpoints with appropriate
auto scaling policies to balance cost and performance.
- Use Savings Plans and Reserved Instances for predictable AI
workloads to reduce infrastructure costs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf07.html*

---

# FSIPERF08: How do you optimize AI model inference performance?

Financial services AI applications require sophisticated
inference optimization to meet real-time performance
requirements while maintaining regulatory compliance and
accuracy standards.

## FSIPERF08-BP01 Implement inference acceleration techniques

Apply specialized optimization techniques to reduce model
inference latency and improve throughput for financial AI
workloads.

### Optimization strategies:

- Remove unnecessary model parameters while maintaining
accuracy for financial predictions.
- Create smaller, faster models that maintain the accuracy of
larger models for specific financial tasks.
- Combine multiple neural network layers to reduce computation
overhead.
- Use gradient checkpointing and mixed precision training to
reduce memory requirements.

### Implementation guidance:

- Use AWS Inferentia2 chips with the Neuron SDK for optimized
transformer model inference.
- Leverage NVIDIA TensorRT on GPU instances for accelerated
deep learning inference.
- Implement ONNX Runtime for cross-platform model optimization
and deployment.
- Apply Apache TVM for automated optimization of machine
learning models.

## FSIPERF08-BP02 Optimize real-time inference for financial applications

Configure inference infrastructure to meet the stringent
latency requirements of financial services applications such
as fraud detection, algorithmic trading, and real-time risk
assessment.

### Real-time optimization techniques:

- Keep models loaded in memory to eliminate cold start
latency.
- Maintain persistent connections to inference endpoints to
reduce network overhead.
- Use intelligent load balancing to route requests to the
optimal inference endpoint.
- Implement asynchronous inference for batch predictions
within acceptable latency bounds.

### Performance monitoring and tuning:

- Configure Amazon CloudWatch metrics for inference latency,
throughput, and error rates.
- Set up automated alerts for performance degradation that
could impact financial operations.
- Implement canary deployments for testing model performance
improvements in production.
- Use AWS X-Ray for distributed tracing of inference request
paths through financial AI systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf08-how-do-you-optimize-ai-model-inference-performance.html*

---

# FSIPERF09: How do you monitor and tune AI system performance?

Financial services AI systems require sophisticated monitoring
and tuning approaches to maintain optimal performance while
meeting regulatory requirements and business objectives.

## FSIPERF09-BP01 Implement comprehensive AI performance monitoring

Establish monitoring frameworks that capture the full
spectrum of AI system performance metrics relevant to
financial services operations.

### Key monitoring dimensions:

- Accuracy, precision, recall, F1 score, and domain-specific
metrics for financial predictions.
- GPU utilization, memory consumption, CPU usage, and network
latency for AI workloads.
- Revenue impact of AI decisions, regulatory compliance
scores, and customer satisfaction metrics.
- Model drift detection, data quality scores, and prediction
confidence levels.

### Implementation steps:

- Deploy Amazon CloudWatch Container Insights for monitoring
containerized AI workloads.
- Use AWS X-Ray for distributed tracing of AI inference
pipelines through financial systems.
- Configure Amazon SageMaker AI Model Monitor for automated
detection of model drift and data quality issues.
- Implement custom CloudWatch metrics for business-specific
KPIs related to AI performance.

## FSIPERF09-BP02 Establish automated performance tuning for AI workloads

Implement automated tuning mechanisms that can adapt AI system
performance to changing workload patterns and performance
requirements in financial services environments.

### Automated tuning approaches:

- Configure dynamic scaling based on inference volume, latency
targets, and cost constraints.
- Use Amazon SageMaker AI Automatic Model Tuning for continuous
model improvement.
- Implement automated instance type selection based on
workload characteristics and performance requirements.
- Use intelligent routing to distribute AI workloads across
optimal inference endpoints.

### Implementation steps:

- Implement A/B testing frameworks. Continuously test model
improvements against production baselines.
- Perform a canary analysis. Gradually roll out performance
improvements with automated rollback capabilities
- Use multi-armed bandit algorithms. Optimize model selection
and routing for maximum business value.
- Use feedback loops. Incorporate real-time performance data
into model retraining and optimization pipelines.

## FSIPERF09-BP03 Monitor AI model accuracy and business impact

Establishing monitoring systems that track both technical
performance and business outcomes enables financial
institutions to proactively identify model degradation,
regulatory risks, and revenue impact, reducing operational
losses, preventing costly regulatory penalties, and verifying
that AI systems continue delivering measurable ROI while
maintaining the trust and transparency required for
customer-facing financial decisions.

### Implementation steps:

- Compare model predictions against known outcomes for
accuracy assessment.
- Monitor prediction confidence levels and flag
low-confidence decisions for human review.
- Implement statistical tests to detect changes in input
data distribution that may affect model performance.
- Track model decisions for bias, fairness, and regulatory
compliance requirements.

### Business impact tracking:

- Monitor revenue impact, cost savings, and risk reduction
attributed to AI decisions.
- Track processing time reductions and automation rates
achieved through AI implementation.
- Measure customer satisfaction and engagement improvements
from AI-powered services.
- Monitor false positive and negative rates for fraud
detection and credit risk models.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf09-how-do-you-monitor-and-tune-ai-system-performance.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
