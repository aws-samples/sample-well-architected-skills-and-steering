# MLCOST05 — Deployment

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MLCOST05-BP01 Use an appropriate deployment option

Use the right deployment option for your machine learning models to
optimize cost and performance based on your specific use case
requirements. Select real-time inference for low latency
applications, batch transform for large datasets, or edge deployment
for applications that require local processing.

**Desired outcome:** You have an
optimized model deployment strategy that balances performance and
cost efficiency. You can choose the appropriate deployment option
based on your specific use case requirements, whether that's
real-time inference for low-latency applications, batch processing
for large datasets, or edge deployment for scenarios requiring local
processing.

**Common anti-patterns:**

- Using real-time endpoints for deployment scenarios regardless of
traffic patterns.
- Overlooking serverless or asynchronous options when they would
be more cost-effective.
- Deploying separate endpoints for each model when multiple models
could be hosted more efficiently together.
- Running inference in the cloud when edge deployment would be
more efficient for local data processing.
- Overprovisioning compute resources for inference endpoints.

**Benefits of establishing this best
practice:**

- Cost optimization through selection of the most efficient
deployment option for each use case.
- Improved performance by matching deployment options to specific
latency requirements.
- Increased operational efficiency through managed inference
services.
- Flexibility to handle varying inference workloads and traffic
patterns.
- Simplified ML model management across cloud and edge
environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When deploying machine learning models, selecting the right
deployment option is crucial for achieving optimal performance and
cost efficiency. Amazon SageMaker AI provides multiple deployment
options that can be tailored to your specific use case
requirements. Real-time inference is ideal for applications
requiring low latency responses, such as real-time recommendations
or fraud detection. Batch transform is better suited for
processing large datasets in offline mode, such as document
processing or periodic scoring jobs. Edge deployment brings
inference capabilities directly to edge devices, reducing latency
and bandwidth requirements while enabling offline processing.

Consider the pattern of requests your application needs to handle.
If you need consistent, low-latency responses for interactive
applications with steady traffic, real-time inference is
appropriate. If you process data in batches without immediate
response requirements, batch transform offers cost efficiency. For
applications with unpredictable or bursty traffic patterns,
serverless inference can automatically scale to match demand while
minimizing costs during idle periods. For workloads with large
payloads or long processing times, asynchronous inference provides
a queuing mechanism that improves efficiency.

Also consider resource utilization. Multi-model endpoints and
multi-container endpoints enable you to optimize costs by sharing
resources across multiple models or containers. This approach is
particularly valuable when you have many models with variable
usage patterns or complementary resource requirements.

### Implementation steps

- **Evaluate your inference
requirements**. Determine your application's needs
for latency, throughput, payload size, and traffic patterns.
Consider whether your application requires real-time
responses or can process data in batches. Assess if your
models should run in the cloud or at the edge based on
connectivity, latency requirements, and data privacy
considerations.
- **Use Amazon SageMaker AI for model
deployment**.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) offers a comprehensive set of deployment
options to optimize price-performance for most use cases.
It's a fully managed service that integrates with MLOps
tools for effective model management in production with
reduced operational burden.
- **Select the appropriate inference
option based on your use case**. Choose from
several SageMaker AI inference options:

[Amazon SageMaker AI Real-time Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) for low-latency,
interactive applications requiring immediate responses
- [Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) for workloads with
intermittent or unpredictable traffic patterns
- [Amazon SageMaker AI Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) for large
payload sizes, long processing times, or when immediate
responses aren't required
- [Amazon SageMaker AI Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) for offline processing
of large datasets

- **Implement multi-model endpoints for
cost optimization**. Use
[Amazon SageMaker AI Multi-Model Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) to deploy multiple
models on a single endpoint with shared container resources.
This approach improves endpoint utilization and reduces
hosting costs compared to single-model endpoints. SageMaker AI
manages the loading of models into memory and scales them
based on traffic patterns.
- **Deploy multiple containers on a
single endpoint**. Implement
[SageMaker AI
multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) to deploy multiple
containers using different models or frameworks on a single
endpoint. Run containers in sequence as an inference
pipeline or access each container individually through
direct invocation to improve endpoint utilization and
optimize costs.
- **Automate endpoint changes through a
pipeline**. Use
[Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) to automate the model deployment
process. Create CI/CD pipelines that handle model training,
evaluation, and deployment, enabling consistent and
repeatable deployment processes.
- **Monitor and optimize your
deployment**. Implement continuous monitoring of
your inference endpoints to track performance metrics, cost,
and resource utilization. Use this data to fine-tune your
deployment strategy and make adjustments as needed to
optimize for cost efficiency and performance.
- **Use AI-powered code generation for
deployment automation**. Use AI-powered development
tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
deployment scripts, automate infrastructure configuration,
and accelerate the implementation of optimal deployment
strategies.
- **For generative AI workloads,
consider deployment options for foundation
models**. Evaluate specialized deployment options
like
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for fully managed foundation models or
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart.html) for pre-trained models with optimized
deployment configurations.

## Resources

**Related documents:**

- [Deploy
models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Batch
transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)
- [Hosting
options](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-options.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
- [Model
deployment at the edge with SageMaker AI Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html)
- [Inference
pipelines in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)

**Related examples:**

- [SageMaker AI
Serverless Inference Walkthrough](https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/Serverless-Inference-Walkthrough.ipynb)
- [SageMaker AI
Edge Manager Workshop](https://github.com/aws-samples/amazon-sagemaker-edge-manager-workshop)
- [SageMaker AI
Asynchronous Inference Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/async-inference)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp01.html*

---

# MLCOST05-BP02 Explore cost effective hardware options

Machine learning models that power AI applications are becoming
increasingly complex resulting in rising underlying compute
infrastructure costs. Up to 90% of the infrastructure spend for
developing and running ML applications is often on inference. Look
for cost-effective infrastructure solutions for deploying their ML
applications in production.

**Desired outcome:** You achieve
significant cost savings while maintaining or improving the
performance of your machine learning inference workloads. By
implementing cost-effective hardware options, you optimize your
infrastructure spend, reduce operational costs, and can allocate
resources more efficiently across your ML applications. Your ML
models run on purpose-built hardware that provides the right balance
of performance and cost for your specific use case.

**Common anti-patterns:**

- Using general-purpose compute instances for ML workloads without
considering specialized hardware options.
- Over-provisioning inference resources to handle peak loads
without implementing scaling strategies.
- Ignoring model optimization opportunities before deploying to
production.
- Selecting hardware based solely on performance metrics without
considering cost-efficiency.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs for ML model inference.
- Improved inference throughput and latency.
- More efficient use of computational resources.
- Lower total cost of ownership for AI applications.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning inference costs represent a significant portion
of the total expenses associated with running ML workloads in
production. As models become more complex, their computational
requirements increase, which can lead to higher infrastructure
costs. Selecting the right hardware for your ML workloads is
crucial for maintaining cost efficiency without sacrificing
performance.

AWS offers multiple options to optimize the cost and performance
of your ML inference workloads. These include services that
optimize models for specific hardware targets, instances that
provide cost-effective acceleration for inference workloads, and
deployment options that match your specific latency and throughput
requirements.

Evaluating your specific workload requirements is essential before
selecting hardware options. Consider factors such as latency
requirements, throughput needs, model complexity, batch size
capabilities, and budget constraints. This evaluation will assist
you to determine the most appropriate hardware solution for your
use case.

### Implementation steps

- **Use Amazon SageMaker AI Neo for model
optimization**. Amazon SageMaker AI Neo automatically
optimizes machine learning models for inference on cloud
instances and edge devices. For inference in the cloud,
SageMaker AI Neo speeds up inference and saves cost by creating
an inference optimized container in SageMaker AI hosting. For
inference at the edge, SageMaker AI Neo saves developers months
of manual tuning by automatically tuning the model for the
selected operating system and processor hardware. Neo
optimizes models trained in TensorFlow, PyTorch, MXNet, and
other frameworks for deployment on ARM, Intel, and NVIDIA
processors.
- **Deploy on Amazon EC2 Inf2
Instances**. Amazon EC2 Inf1 instances deliver
high-performance ML inference at the lowest cost in the
cloud. They deliver up to 2.3-times higher throughput and up
to 70% lower cost per inference than comparable current
generation GPU-based Amazon EC2 instances. Inf1 instances
are built from the ground up to support machine learning
inference applications. They feature up to 16 AWS Inferentia
chips, high-performance machine learning inference chips
designed and built by AWS. Additionally, Inf1 instances
include second generation Intel Xeon Scalable processors and
up to 100 Gbps networking to deliver high throughput
inference.
- **Explore Amazon EC2 Inf2
Instances**. The second generation of AWS
Inferentia-based instances, EC2 Inf2 instances, offer even
greater performance improvements over previous generations.
These instances are powered by AWS Inferentia2 chips and
provide up to 4x higher throughput and up to 10x lower
latency than Inf1 instances. They're ideal for more complex
generative AI models and large language models (LLMs) that
require high performance and cost-effective inference
solutions.
- **Consider Amazon SageMaker AI serverless
inference**. SageMaker AI serverless inference is a
purpose-built inference option that automatically
provisions, scales, and shuts down compute capacity based on
your workload needs. This pay-per-use model can reduce costs
by avoiding the need to continuously run instances when
there are no inference requests, making it ideal for
workloads with intermittent traffic patterns.
- **Evaluate batch and asynchronous
inference options**. For non-real-time inference
requirements, consider using SageMaker AI batch transform for
offline inference processing or SageMaker AI asynchronous
inference for workloads that can tolerate higher latency.
These options often allow for more efficient resource
utilization and lower costs compared to real-time inference
endpoints.
- **Implement automated scaling
policies**. Configure auto-scaling for your
SageMaker AI endpoints to dynamically adjust the number of
instances based on workload demands. This way, you can pay
for the resources you need while maintaining performance
requirements during peak usage periods.
- **Use enhanced SageMaker AI Inference
Recommender**. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) with enhanced algorithms and
support for multi-model endpoints to get sophisticated cost
optimization recommendations for your specific workloads.
- **Regularly monitor and analyze
inference costs**. Use AWS Cost Explorer and Amazon CloudWatch metrics to track your inference costs and
performance metrics. Regularly review this data to identify
optimization opportunities and adjust your hardware strategy
accordingly.

## Resources

**Related documents:**

- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)
- [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/)
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Deploy
models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)

**Related examples:**

- [AWS Neuron SDK Examples for Inferentia and Trainium
instances](https://github.com/aws-neuron/aws-neuron-sdk)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp02.html*

---

# MLCOST05-BP03 Right-size the model hosting instance fleet

Use efficient compute resources to run models in production. In many
cases, up to 90% of the infrastructure spend for developing and
running an ML application is on inference, making it critical to use
high-performance, cost-effective ML inference infrastructure.
Selecting the right way to host and the right type of instance can
have a large impact on the total cost of ML projects. Use automatic
scaling for your hosted models. Auto scaling dynamically adjusts the
number of instances provisioned for a model in response to changes
in your workload.

**Desired outcome:** You optimize
your ML infrastructure costs while maintaining performance by using
the right instance types and quantities for your model deployments.
You use automated tools to recommend the most cost-effective
configurations and implement dynamic scaling that adjusts capacity
based on actual demand patterns, resulting in significant cost
savings and consistent performance.

**Common anti-patterns:**

- Using the same instance types for each model regardless of their
specific requirements.
- Maintaining static instance counts rather than scaling with
workload demands.
- Selecting instance types based solely on performance without
considering cost implications.
- Not distributing model instances across multiple availability
zones for resilience.

**Benefits of establishing this best
practice:**

- Reduced ML infrastructure costs by up to 90% through optimal
instance selection.
- Improved model performance through use of appropriately sized
resources.
- Enhanced reliability through automatic scaling and multi-AZ
deployment.
- Better handling of variable workloads without performance
degradation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Optimizing ML inference costs requires a careful balance between
performance and cost. When selecting compute resources for model
hosting, consider both the model's specific requirements and the
expected workload patterns. CPU instances may be sufficient for
many traditional ML models, while GPU instances deliver better
performance for deep learning models but at a higher cost. The key
is using the right resource for the specific workload.

Amazon SageMaker AI provides tools that can automatically select
the optimal instance type and size for your models. By testing
different configurations, you can find the sweet spot that
delivers the required performance at the lowest possible cost.
Additionally, implementing auto scaling assists in verifying that
your deployment can handle varying loads efficiently, scaling up
during peak demand and down during quiet periods to avoid
unnecessary costs.

### Implementation steps

- **Use Amazon SageMaker AI Inference
Recommender for instance selection**. Amazon SageMaker AI Inference Recommender automatically selects the
right compute instance type, instance count, container
parameters, and model optimizations for inference to
maximize performance and minimize cost. You can use
SageMaker AI Inference Recommender from SageMaker AI Studio,
the AWS Command Line Interface (AWS CLI), or the AWS SDK,
and within minutes, get recommendations to deploy your ML
model. You can then deploy your model to one of the
recommended instances or run a fully managed load test on a
set of instance types you choose without worrying about
testing infrastructure. You can review the results of the
load test in SageMaker AI Studio and evaluate the tradeoffs
between latency, throughput, and cost to select the most
optimal deployment configuration.
- **Configure auto scaling for SageMaker AI
endpoints**. Amazon SageMaker AI supports an auto
scaling feature that monitors your workloads and dynamically
adjusts the capacity to maintain steady and predictable
performance at the lowest possible cost. When the workload
increases, auto scaling brings more instances online. When
the workload decreases, auto scaling removes unnecessary
instances, which can reduce your compute cost. SageMaker AI
automatically attempts to distribute your instances across
Availability Zones. So, we strongly recommend that you
deploy multiple instances for each production endpoint for
high availability. If you're using a VPC, configure at least
two subnets in different Availability Zones so Amazon SageMaker AI can distribute your instances across those
Availability Zones.
- **Implement proper scaling
policies**. Define appropriate scaling policies
based on your model's performance characteristics and usage
patterns. Set scaling metrics such as CPU utilization, GPU
utilization, model latency, or custom metrics that reflect
your workload's needs. Define appropriate target values and
cooldown periods to avoid rapid scaling oscillations.
- **Consider serverless inference
options**. For workloads with unpredictable or
intermittent traffic patterns, evaluate
[Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), which automatically
provisions and scales compute capacity based on traffic.
This option reduces the need to select instance types or
manage scaling policies while providing pay-per-use pricing.
- **Regularly review and optimize
deployments**. Set up a process to periodically
review your model deployments' performance and cost metrics.
As your models evolve and usage patterns change, rerun
Inference Recommender tests to keep your infrastructure
optimized. Look for opportunities to consolidate models or
use multi-model endpoints where appropriate.
- **Use SageMaker AI Training Plans for
predictable access**. Use
[SageMaker AI
Training Plans](https://aws.amazon.com/sagemaker/pricing/) as a compute reservation system for
predictable access to high-demand GPU resources, managing
large-scale AI training workloads more efficiently with
better resource planning and scheduling capabilities.
- **Use model optimization
techniques**. For large language models and other
generative AI workloads, consider techniques like
quantization, distillation, or pruning to reduce model size
and computational requirements. Amazon SageMaker AI supports
optimization techniques through
[SageMaker AI
Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) and integration with
[AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) for optimized inference on AWS Inferentia and
Trainium chips.

## Resources

**Related documents:**

- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)

**Related examples:**

- [SageMaker AI Inference Recommender](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb)
- [Right-sizing
your Amazon SageMaker AI Endpoints](https://github.com/aws-samples/aws-marketplace-machine-learning/blob/master/right_size_your_sagemaker_endpoints/Right-sizing%20your%20Amazon%20SageMaker AI%20Endpoints.ipynb)
- [SageMaker AI
Serverless Inference Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/serverless-inference)
- [Automatically
Scale Amazon SageMaker AI Models](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp03.html*

---
