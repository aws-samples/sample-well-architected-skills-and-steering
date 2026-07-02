# MLSUS05 — Deployment

**Pillar**: Sustainability  
**Best Practices**: 4

---

# MLSUS05-BP01 Align SLAs with sustainability goals

Define service level agreements (SLAs) that support your
sustainability goals while meeting your business requirements.
Define SLAs to meet your business requirements, not exceed them.
Make trade-offs that significantly reduce environmental impacts in
exchange for acceptable decreases in service levels.

**Desired outcome:** You establish
SLAs that balance business requirements with sustainability
objectives, optimizing resource utilization while maintaining
acceptable service levels. By implementing appropriate inference
methods based on latency tolerance, availability needs, and response
time requirements, you can reduce idle resources, minimize energy
consumption, and lower your machine learning workload's
environmental impact.

**Common anti-patterns:**

- Maintaining always-on inference endpoints for workloads with
sporadic or batch processing needs.
- Setting unnecessarily stringent response time requirements when
users can tolerate some latency.
- Configuring excessive redundancy beyond what's needed for
business continuity.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs through optimized resource
utilization.
- Lower carbon footprint from minimized idle computing resources.
- Alignment of technical operations with organizational
sustainability goals.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When designing machine learning systems, your SLA choices directly
impact resource consumption and environmental sustainability. By
carefully analyzing your actual business requirements rather than
automatically opting for maximum performance, you can identify
opportunities to make sustainable trade-offs without compromising
essential functionality.

Consider your application's true latency requirements,
availability needs, and processing patterns. For example, if your
users can tolerate a response time of seconds rather than
milliseconds, asynchronous or batch processing approaches can
dramatically reduce resource usage compared to always-on real-time
endpoints. Similarly, if your application can gracefully handle
occasional unavailability during instance failures, you can avoid
overprovisioning redundant capacity.

The goal is to make conscious trade-offs that balance
sustainability with business needs, focusing on what's truly
required rather than defaulting to full time maximum performance.

### Implementation steps

- **Queue incoming requests and process
them asynchronously**. If your users can tolerate
some latency, deploy your model on
[serverless](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
or
[asynchronous
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) to reduce resources that are idle between
tasks and minimize the impact of load spikes. These options
will automatically scale the instance or endpoint count to
zero when there are no requests to process, so you only
maintain an inference infrastructure when your endpoint is
processing requests.
- **Adjust availability**. If
your users can tolerate some latency in the rare case of a
failover, don't provision extra capacity. If an outage
occurs or an instance fails, Amazon SageMaker AI
[automatically
attempts to distribute your instances across Availability
Zones](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html#deployment-best-practices-availability-zones). Adjusting availability is an example of a
[conscious
trade off](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-as-a-non-functional-requirement.html) you can make to meet your sustainability
targets.
- **Adjust response time**.
When you don't need real-time inference, use
[SageMaker AI Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html). Unlike a persistent endpoint,
clusters are decommissioned when batch transform jobs finish
so you don't continuously maintain an inference
infrastructure.
- **Conduct workload
analysis**. Assess your machine learning workload's
usage patterns and latency requirements to determine the
most sustainable deployment option. Identify periods of peak
activity versus low or no usage to determine if on-demand
scaling is appropriate for your needs.
- **Define sustainability
metrics**. Establish key metrics to track your
sustainability improvements, such as compute hours saved,
idle time reduced, or overall carbon footprint reduction.
Include these metrics alongside traditional performance
indicators in your operational dashboards.
- **Leverage enhanced serverless
inference capabilities**. Use improved
[SageMaker AI
Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) with increased memory
configurations and better cold-start performance for
variable workloads that don't require always-on
infrastructure.
- **Optimize large language model
deployments with serverless deployment or batch
processing**. For generative AI workloads using
large language models (LLMs), consider serverless model
inference through SageMaker AI or implement
[Bedrock
batch processing](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) for non-interactive generation tasks
like content summarization or document analysis to reduce
resource consumption.

## Resources

**Related documents:**

- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
- [Batch
transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Best
practices for deploying models on SageMaker AI Hosting
Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Sustainability
as a non-functional requirement](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-as-a-non-functional-requirement.html)
- **Related services:**
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus05-bp01.html*

---

# MLSUS05-BP02 Use efficient silicon

Choosing the right compute architecture for your machine learning
workloads can significantly reduce energy consumption and carbon
footprint while maintaining high performance.

**Desired outcome:** You select and
deploy the most energy-efficient instance types for your machine
learning workloads, resulting in reduced power consumption, lower
costs, and a more sustainable ML infrastructure without compromising
performance or functionality.

**Common anti-patterns:**

- Using general-purpose instances for specialized ML workloads.
- Selecting hardware based primarily on performance without
considering power efficiency.
- Not optimizing ML models to work efficiently on specialized
hardware.

**Benefits of establishing this best
practice:**

- Reduced energy consumption by up to 60% with purpose-built ML
accelerators.
- Decreased carbon footprint of your ML operations.
- Improved performance-per-watt metrics for your ML
infrastructure.
- Better alignment with organizational sustainability goals.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The energy efficiency of your ML infrastructure directly impacts
both your operating costs and environmental footprint. By
selecting purpose-built hardware accelerators designed
specifically for ML workloads, you can achieve significant
sustainability improvements while maintaining or even improving
performance.

AWS has developed several specialized compute architectures
optimized for different ML workload types, from training to
inference. Each is designed to deliver maximum performance per
watt to assist in meeting sustainability goals while effectively
running your ML applications. These purpose-built solutions are
particularly important for large-scale ML deployments where small
efficiency improvements can result in substantial energy savings
when scaled across your infrastructure.

When choosing compute resources for your ML workloads, consider
not only the raw performance but also the energy efficiency of the
hardware. The most powerful instance sometimes isn't the most
sustainable choice, as matching the hardware capabilities to your
specific workload requirements can often lead to better
sustainability outcomes.

### Implementation steps

- **Assess your ML workload
requirements**. Before selecting compute resources,
analyze your ML workload characteristics including model
size, batch processing capabilities, latency requirements,
and throughput needs. This assessment can determine which
specialized hardware will provide the optimal balance
between performance and sustainability.
- **Use AWS Graviton3 for CPU-based ML
inference**.
[AWS Graviton3](https://aws.amazon.com/ec2/graviton/) processors offer the best performance per
watt in Amazon EC2, using up to 60% less energy than
comparable instances. They deliver up to three times better
performance compared to Graviton2 processors for ML
workloads and support bfloat16, making them ideal for
efficient CPU-based inference.
- **Deploy AWS Inferentia for deep
learning inference**. Amazon EC2
[Inf2
instances](https://aws.amazon.com/machine-learning/inferentia/) offer up to 50% better performance per watt
over comparable Amazon EC2 instances. These instances are
purpose-built to run deep learning models at scale and
assist in meeting sustainability goals when deploying
ultra-large models.
- **Leverage AWS Trainium for ML
training**. Amazon EC2
[Trn2
instances](https://aws.amazon.com/machine-learning/trainium/) based on custom-designed AWS Trainium chips
offer up to 50% cost-to-train savings over comparable
instances. When using a Trainium-based instance cluster,
total energy consumption for training BERT Large from
scratch is approximately 25% lower compared to same-sized
clusters of comparable accelerated EC2 instances.
- **Optimize your models for the target
hardware**. Use the
[AWS Neuron SDK](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) to compile and optimize your ML models
specifically for AWS Inferentia and Trainium chips. This
verifies that your models can take full advantage of the
hardware's power-efficient design and specialized ML
acceleration features.
- **Monitor and measure power
efficiency**. Use Amazon CloudWatch metrics to
track the resource utilization of your ML workloads. Compare
performance-per-watt metrics across different instance types
to validate your efficiency improvements and identify areas
for further optimization.
- **Leverage purpose-built training
infrastructure**. For large-scale model training,
use
[SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) which provides purpose-built infrastructure
for distributed training with automatic checkpoint storage
and recovery, optimizing resource utilization for
long-running training jobs.
- **Evaluate serverless options for
intermittent workloads**. For ML inference
workloads with variable traffic patterns, consider
[Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) to automatically scale
compute resources based on traffic, reducing idle resource
waste.

## Resources

**Related documents:**

- [Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
- [Specifications
for Amazon EC2 accelerated computing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html#aws-inferentia-instances)
- [AWS Neuron SDK Documentation](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)

**Related examples:**

- [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus05-bp02.html*

---

# MLSUS05-BP03 Optimize models for inference

Optimize machine learning models for inference to achieve higher
performance with lower computational resources, reducing both costs
and environmental impact.

**Desired outcome:** You achieve more
efficient machine learning inference with optimized models that use
less computational resources, consume less energy, and deliver
faster predictions. This optimization can reduce operational costs
and carbon footprint while improving the user experience through
faster response times.

**Common anti-patterns:**

- Deploying models directly from training without optimization.
- Using generic frameworks for inference when optimized
alternatives exist.
- Selecting oversized models when smaller ones would suffice for
the task.
- Ignoring hardware-specific optimizations for deployment targets.

**Benefits of establishing this best
practice:**

- Reduced inference costs through more efficient resource
utilization.
- Improved response times for better user experience.
- Extended battery life for edge device deployments.
- Ability to deploy complex models on resource-constrained
devices.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Model optimization for inference represents a critical step in the
machine learning lifecycle that is often overlooked. While data
scientists typically focus on model accuracy during development,
the computational efficiency of these models during deployment
significantly impacts costs, energy consumption, and user
experience.

Model compilation transforms your trained models into optimized
forms that can run more efficiently on specific hardware. This
process analyzes your model's computational graph, applies various
optimizations like operator fusion and memory layout
transformations, and generates optimized code that takes advantage
of hardware-specific capabilities. The result is a model that
delivers the same predictions but requires less computational
resources and energy.

The optimization approach varies based on your model type and
deployment target. For tree-based models like XGBoost, specialized
compilers can significantly reduce inference latency. For deep
learning models, frameworks can avoid training-specific operations
and optimize the execution path. For edge deployments, additional
optimizations like quantization can reduce model size while
maintaining acceptable accuracy.

### Implementation steps

- **Select appropriate model
architectures**. Choose model architectures that
naturally lend themselves to efficient inference. Consider
simpler architectures or distilled versions of larger models
when possible. Balance accuracy requirements against
efficiency needs for your specific use case.
- **Use open-source model
compilers**. Use specialized tools like
[Treelite](https://treelite.readthedocs.io/en/latest/)
for decision tree ensembles such as XGBoost, LightGBM, and
RandomForest. These compilers transform models into
optimized C code that improves prediction throughput through
more efficient memory access patterns and computational
optimizations.
- **Leverage Amazon SageMaker AI
Neo**. Use
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to optimize models for inference on
Amazon SageMaker AI in the cloud and supported edge devices.
Neo automatically optimizes models trained in TensorFlow,
PyTorch, MXNet, and other frameworks, delivering up to 25
times the performance improvement while maintaining
accuracy. The Neo runtime consumes only a fraction of the
resources required by full deep learning frameworks.
- **Consider quantization
techniques**. Apply post-training quantization to
reduce model precision from 32-bit floating point to 16-bit
or 8-bit integers where appropriate. This reduces model size
and improves computational efficiency, particularly on
hardware with specialized integer arithmetic capabilities.
- **Optimize for specific hardware
targets**. Configure your model compilation process
to target the specific hardware where inference will run.
Different optimizations apply to CPUs, GPUs, and specialized
accelerators like AWS Inferentia or AWS Trainium.
- **Use efficient model serving
architectures**. Implement
[SageMaker AI
multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) and inference pipelines to
build modular inference architectures that efficiently share
resources across models and processing stages, allowing for
improved resource utilization and optimization.
- **Leverage AI-powered code generation
for optimization automation**. Use AI-powered
development tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
model optimization code, automate inference pipeline
creation, and accelerate the implementation of efficient
deployment strategies.
- **Test performance under realistic
conditions**. Measure inference latency,
throughput, and resource utilization under realistic
workloads before deploying to production. Compare optimized
models against baselines to quantify improvements and verify
that optimization doesn't impact accuracy.

## Resources

**Related documents:**

- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Edge
Devices](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-edge-devices.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus05-bp03.html*

---

# MLSUS05-BP04 Deploy multiple models behind a single endpoint

Host multiple models behind a single endpoint to improve endpoint utilization. Sharing
endpoint resources is more sustainable and less expensive than deploying a single model behind
one endpoint.

**Desired outcome:** Your organization achieves greater efficiency
in your model deployments by consolidating multiple models on shared infrastructure. This can
reduce costs by increasing utilization of your endpoint resources, minimize environmental impact
through reduced carbon emissions, and simplify your model deployment architecture.

**Common anti-patterns:**

- Deploying each model on its own dedicated endpoint regardless of utilization patterns.
- Over-provisioning resources for endpoints that serve infrequently accessed models.
- Creating separate infrastructure for similar models that could share resources.

**Benefits of establishing this best practice:**

- Reduced costs through better utilization of compute resources.
- Decreased carbon footprint by up to 90% compared to single-model deployments.
- Improved scalability for serving multiple models.
- Enhanced operational efficiency for inference workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Model deployment architecture significantly impacts both cost and sustainability. By
hosting multiple models behind a single endpoint, you can substantially improve resource
utilization, reducing both expenses and environmental impact. Amazon SageMaker AI provides several
approaches to implement this practice, each suitable for different scenarios depending on your
model types, access patterns, and processing requirements.

Consider your workload characteristics when selecting a deployment approach. For a large
collection of similar models that aren't accessed simultaneously, multi-model endpoints (MME)
offer the most efficient solution. When you need to deploy different model types with varying
framework requirements, multi-container endpoints (MCE) provide flexibility. For sequential
processing workflows, inference pipelines allow you to chain preprocessing, prediction, and
postprocessing steps.

### Implementation steps

- **Assess your model deployment needs**. Evaluate your
current deployment architecture, focusing on model similarity, access patterns, and
resource requirements. Identify opportunities to consolidate models based on these
characteristics.
- **Select the appropriate deployment method**. Choose from
one of SageMaker AI's three approaches based on your workload requirements:

Multi-model endpoints for similar models with varied access patterns
- Multi-container endpoints for heterogeneous models requiring different
frameworks
- Inference pipelines for sequential processing workflows

- **Implement multi-model endpoints**. Use SageMaker AI's multi-model
endpoint capability to host multiple models within a single container. This approach is
ideal when you have many similar models that use the same framework and don't need to be
accessed simultaneously. Configure the endpoint to dynamically load and unload models
based on usage patterns to optimize memory utilization.
- **Deploy multi-container endpoints**. When your models
require different containers or frameworks, use [SageMaker AI multi-container
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) to host up to 15 containers on a single endpoint. Configure each
container with its specific model and framework requirements while sharing the
underlying infrastructure resources.
- **Create inference pipelines**. For workflows that require
sequential processing, implement a [SageMaker AI inference pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) to
chain multiple containers. Define the sequence to handle preprocessing, model inference,
and postprocessing steps as a unified flow, passing outputs from one container as inputs
to the next.
- **Monitor and optimize resource utilization**. Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track endpoint metrics
including CPU utilization, memory usage, and invocation patterns. Analyze this data to
further optimize your deployment by adjusting instance types or scaling configurations
based on actual usage.
- **Implement cost tracking**. Set up cost allocation tags to
monitor the efficiency gains from your consolidated endpoint deployment. Compare the
costs before and after implementation to quantify savings and justify the architectural
approach.
- **Leverage modular deployment architectures**. Use [SageMaker AI
multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) and [inference pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) to
create modular inference architectures that can efficiently share resources across
different model components and processing stages.
- **Consider sustainability metrics**. Track carbon emission
reductions resulting from your optimized deployment architecture. Using [AWS
Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/), you can measure the environmental impact of
your workloads and report on sustainability improvements.

## Resources

**Related documents:**

- [Multi-model endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html)
- [Inference
pipelines in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus05-bp04.html*

---
