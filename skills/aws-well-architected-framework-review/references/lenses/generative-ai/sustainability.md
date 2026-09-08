# Sustainability

**Pillar**: Sustainability  
**Questions**: 3

---

# GENSUS01 — Energy-efficient infrastructure and services

**Pillar**: Sustainability  
**Best Practices**: 2

---

# GENSUS01-BP01 Implement auto scaling and serverless architectures to optimize resource utilization

Adopt efficient and sustainable AI/ML practices to minimize resource
usage, reduce costs, and lower environmental impact. Use serverless
architectures, auto scaling, and specialized hardware to optimize
resource utilization. This approach enhances performance efficiency,
aligns with cost optimization, and supports sustainability goals.
Implementing these practices enables responsible and economical
deployment of generative AI workloads and promotes effective scaling
without unnecessary resource waste.

**Desired outcome:** After
implementing this best practice, customers can improve the
elasticity of their generative AI workloads and benefit from the
efficiencies of scale of the AWS Cloud.

**Benefits of establishing this best
practice:**
[Optimize
resource utilization](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) - Minimize environmental impact by
maximizing the efficiency of generative AI resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopting serverless architectures and auto-scaling capabilities is
essential for verifying that resources are provisioned and
consumed only when needed. This approach minimizes idle
consumption and reduces the associated environmental impact. While
training jobs may run overnight, the notebook and ML development
instances that are not in use can be shut down either through
configuring an idle time-out or through scheduling. You can
further enhance the efficiency of your workload's resource
utilization by using AWS managed services and managed offerings.

Amazon Bedrock and Amazon Q are fully-managed services, which
means that AWS handles the infrastructure management, scaling, and
maintenance. As a result, users can focus on model development
rather than infrastructure utilization. Similarly,
[Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) helps optimize the
deployment of machine learning models by automating load testing.
It assists in selecting the best instance type by considering
factors like instance count, container parameters, and model
optimizations. This tool provides recommendations for both
real-time and serverless inference endpoints, which helps you
verify that models are deployed with the best performance at the
lowest resource consumption.

For hosting and running generative AI models efficiently, consider
using Amazon EC2 Inferentia instances. These instances deliver
some of the highest compute power and accelerator memory in among
EC2 instance families, which is crucial for handling large
language models and other generative AI workloads. Inferentia
instances support scale-out distributed inference to optimize
compute consumption. The improved performance per watt translates
to more efficient use of resources. By integrating these AWS
services and features, organizations can achieve a more
sustainable and cost-effective approach to generative AI
workloads.

In SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, use the system's managed infrastructure
capabilities and built-in scaling mechanisms to minimize
resource waste while maintaining optimal performance.

Self-hosted models can scale to zero when not in use.
Implement scale-to-zero for periods of low-utilization,
configuring autoscaling policies to scale back up quickly
where appropriate.

### Implementation steps

- Adopt serverless or fully-managed architectures.

Use Amazon Bedrock for generative AI tasks to alleviate
server management overhead
- Use Amazon Q Business-related AI applications to
streamline operations
- Use Amazon SageMaker AI Serverless Inference for on-demand
ML inference without managing servers

- Configure auto scaling capabilities.

Set up auto scaling for Amazon SageMaker AI Endpoints to
handle varying loads efficiently
- Set up EC2 Auto Scaling for custom ML infrastructure to
match resource allocation with demand

- Optimize ML development environments.

For
[SageMaker AI
notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html), configure idle time-out to
release resources when not in use
- For ML development instances, schedule automatic
shutdown for unused instances to conserve resources

- Use SageMaker AI Inference Recommender.

Conduct automated load testing to assess model
deployments under various loads
- Select optimal instance types based on recommendations
for cost-effective and performance
- Consider both real-time and serverless inference

- Implement efficient model hosting.

For model deployments, consider EC2 Inferentia instances
for enhanced performance and efficiency
- For large models, scale and distribute the load across
multiple instances

- Perform continuous monitoring and optimization.

Use Amazon CloudWatch to track resource metrics and
identify optimization opportunities
- Track token lengths of prompts and model responses to
measure utilization
- Identify idle time periods to scale down or suspend the
inference endpoints
- Set up SageMaker AI Model Monitor to continuously monitor
model performance and data quality

- Educate your team on sustainable AI practices.

Provide training to foster a culture of sustainability
- Encourage the use of pre-trained models to reduce
training time and resource consumption

## Resources

**Related best practices:**

- [SUS02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_user_a2.html)
- [SUS05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_hardware_a3.html)
- [SUS02-BP03](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)

**Related documents:**

- [Sustainability pillar – Best practices](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/sustainability-pillar-best-practices-5.html)
- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Amazon SageMaker AI Best Practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Optimizing Costs for Machine Learning with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-for-machine-learning-with-amazon-sagemaker/)
- [The
executive's guide to generative AI for sustainability](https://aws.amazon.com/blogs/machine-learning/the-executives-guide-to-generative-ai-for-sustainability/)
- [Optimize
generative AI workloads for environmental
sustainability](https://aws.amazon.com/blogs/machine-learning/optimize-generative-ai-workloads-for-environmental-sustainability/)
- [Integrating
generative AI effectively into sustainability
strategies](https://www.youtube.com/watch?v=8vAMOPLnN-w)
- [Optimize
your AI/ML workloads with Amazon EC2 Graviton](https://www.youtube.com/watch?v=QIAaMlW1fVo)
- [Orchestrating
SageMaker AI HyperPod clusters with Amazon](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks.html)
- [Orchestrating
SageMaker AI HyperPod clusters with Slurm](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-slurm.html)
- [Deploy models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)

**Related examples:**

- [Supercharge
your auto scaling for generative AI inference – Introducing
Container Caching in SageMaker AI Inference](https://aws.amazon.com/blogs/machine-learning/supercharge-your-auto-scaling-for-generative-ai-inference-introducing-container-caching-in-sagemaker-inference/)
- [SageMaker AI
Inference Recommender Example](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-recommender)
- [AWS can help reduce the carbon footprint of AI workloads by up to
99%](https://www.aboutamazon.com/news/aws/aws-carbon-footprint-ai-workload)
- [Carrier Uses
Amazon Bedrock to Help Customers Achieve Their Sustainability Goals](https://aws.amazon.com/solutions/case-studies/carrier-bedrock-sustainability-testimonial/)
- [Introducing
Amazon SageMaker AI HyperPod, a purpose-built infrastructure for
distributed training at scale](https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-hyperpod-a-purpose-built-infrastructure-for-distributed-training-at-scale/)

**Related tools:**

- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
- [AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/)
- [New – Customer
Carbon Footprint Tool](https://aws.amazon.com/blogs/aws/new-customer-carbon-footprint-tool/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus01-bp01.html*

---

# GENSUS01-BP02 Use efficient model customization services

To maximize efficiency and sustainability in large-scale generative
AI model deployments, adopt best practices for distributed training
and parameter-efficient fine-tuning. These techniques optimize
resource utilization and reduce energy consumption, leading to cost
savings and enhanced performance. This helps maintain a balance
between computational demands and environmental considerations,
promoting responsible cloud resource use.

**Desired outcome:** After
implementing this practice, your organization can create an
environmentally-sustainable infrastructure for training,
customizing, and hosting generative AI workloads.

**Benefits of establishing this best
practice:**
[Optimize
resource utilization](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) - Minimize environmental impact through
efficient use of generative AI model customization resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Amazon Bedrock offers managed model customization features for
fine-tuning and continued pre-training to improve the model's
domain knowledge. It optimizes the infrastructure management,
scaling, and maintenance, allowing developers to focus on model
performance rather than the underlying infrastructure.

Amazon SageMaker AI offers several features to train generative AI
models efficiently. SageMaker AI HyperPod is designed specifically
for large-scale generative AI model training. HyperPod provides
pre-tested training stacks for popular generative AI models, which
helps users start their training processes with confidence. It
offers optimized distributed training and enables the efficient
use of multiple instances for large-scale model training. This
distributed approach speeds up training times, making it feasible
to train even advanced models in a reasonable timeframe.

Users can choose from a variety of instance types, including GPU
and AWS Trainium instances. AWS Trainium instances deliver a
reduction in energy consumption compared to comparable instances
for training large deep learning models, including large language
models (LLMs). This makes training more cost-effective and
efficient.

Parameter-efficient fine tuning (PEFT) techniques, such as
low-rank adaptation (LoRA), can be applied when using Trainium
with HyperPod. These techniques make the fine-tuning of LLMs more
efficient by reducing the number of parameters that need to be
updated, which speeds up the fine-tuning process and reduces time
and cost.

Managed spot training is a feature that allows the use of spare
Amazon EC2 capacity which can lead to more efficient resource
utilization across the infrastructure. This means that users can
get lower-cost, surplus computing power while meeting quality and
speed of training goals.

SageMaker AI Debugger helps detect and stop training jobs early if
issues are identified, minimizing wasted compute resources. This
feature helps verify that users are only paying for the resources
they actually need, further optimizing the cost and efficiency of
their generative AI model training processes.

### Implementation steps

- Select the right AWS services.

Amazon Bedrock has managed model customization where
resource utilization is handled by AWS
- Amazon SageMaker AI offers advanced training features and
full control of the underlying infrastructure choices

- Set up SageMaker AI HyperPod for large-scale distributed
training.

Use pre-tested stacks for popular models to streamline
setup
- Consider AWS Trainium instances for reduced energy
consumption compared to traditional instances
- Apply parameter-efficient fine-tuning with HyperPod for
fine-tuning large language models, reducing the
computational and energy requirements

- Use managed spot training.

Implement managed spot training to utilize spare Amazon EC2 capacity, leading to better underlying resource
utilization
- Set up the checkpointing feature to handle spot instance
interruptions and restart from the last point of
completion

- Enable SageMaker AI Debugger.

Use Debugger to monitor and optimize training job
resource utilization
- Configure rules to identify and halt training jobs early
in case of issues, minimizing wasted compute resources

- Optimize resource utilization and cost.

Analyze usage patterns to adjust instance types and
counts
- Use auto scaling features
- Use cost allocation tags to track detailed resource
consumption and for billing analysis

## Resources

**Related best practices:**

- [SUS02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_user_a2.html)
- [SUS05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_hardware_a3.html)

**Related documents:**

- [Customize
your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)
- [Customize
models in Amazon Bedrock with your own data using fine-tuning
and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
- [Distributed training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)
- [Parameter-Efficient
Fine-Tuning (PEFT) on SageMaker AI HyperPod with AWS
Trainium](https://aws.amazon.com/blogs/machine-learning/peft-fine-tuning-of-llama-3-on-sagemaker-hyperpod-with-aws-trainium/)

**Related examples:**

- [Bedrock
Model Customization Workshop Notebooks](https://github.com/aws-samples/amazon-bedrock-customization-workshop)
- [SageMaker AI
HyperPod recipe repository](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipe-repository.html)
- [Guidance
for Optimizing MLOps for Sustainability on AWS](https://aws.amazon.com/solutions/guidance/optimizing-mlops-for-sustainability-on-aws/)

**Related tools:**

- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [AWS Trainium](https://aws.amazon.com/ai/machine-learning/trainium/)
- [Amazon SageMaker AI HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/)
- [Amazon SageMaker AIDebugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus01-bp02.html*

---

# GENSUS02 — Consume sustainable data processing and storage services

**Pillar**: Sustainability  
**Best Practices**: 1

---

# GENSUS02-BP01 Optimize data processing and storage to minimize energy consumption

Organizations should optimize data processing and storage, which
aims to enhance the sustainability and cost-effectiveness of their
data processing and storage systems, particularly for generative AI
workloads. Optimizing the use of computational resources helps you
minimize energy consumption and operational costs while maintaining
high performance and scalability.

**Desired outcome:** After
implementing this practice, you can achieve more efficient data
management, reduce carbon footprint, and allocate resources more
effectively, which leads to cost and resource efficiency. This
approach not only supports sustainable practices but also help
organizations scale their generative AI initiatives without
incurring unnecessary expenses or resource wastage.

**Benefits of establishing this best
practice:**
[Optimize
resource utilization](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) - Increase sustainability of data
processing and storage.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To enhance sustainability and efficiency in data processing and
storage, minimize runtime and optimize resource utilization. Use
serverless architectures, which offer a fully-managed approach to
scaling resources dynamically based on demand. Serverless services
can reduce the need for maintaining persistent infrastructure,
lowering both operational overhead and energy consumption.

Amazon S3 is a highly scalable and energy-efficient storage
solution that integrates seamlessly with generative AI services.
With intelligent tiering, data can be automatically moved to the
most cost-effective storage class based on access patterns,
verifying that frequently-accessed data remains readily available
while less active data is stored more cost-effectively. S3
Lifecycle policies further enhance this by enabling the transition
of data between storage classes or the deletion of data when it is
no longer needed, which optimizes underlying resource usage.

For analytical workloads, using columnar formats like Apache
Parquet can reduce data transfer and processing requirements.
Compression techniques should be applied where appropriate to
further minimize storage and transfer costs. Amazon Athena
provides a serverless query service that allows for the analysis
of data directly in Amazon S3 without the need for persistent
infrastructure, enhancing both flexibility and efficiency.

AWS Glue offers serverless ETL capabilities, automatic schema
discovery, and cataloging, which helps you verify that data
integration services run only when needed. This reduces idle
resource consumption and aligns resource usage with actual demand.

AWS Lambda enables serverless computing that automatically scales
and operates only when initiated, further reducing unnecessary
resource consumption. While serverless approaches like AWS Lambda
are beneficial for many use cases, it is important to be cautious
when applying them to data processing tasks that require
long-running batch processing. In such scenarios, services like
Amazon EMR with auto scaling may offer more efficient resource
utilization.

In Amazon SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, establish differentiated service-level
objectives that balance training performance requirements with
resource efficiency and environmental impact considerations.

For EKS-based HyperPod, use Kubernetes resource quotas and
priority classes to define different service tiers for various
training workloads, implementing horizontal pod autoscaling
policies that align with actual performance needs rather than
peak theoretical capacity. Configure task governance
capabilities to automatically prioritize critical training
jobs while verifying that lower-priority experimentation
workloads use sustainable resource allocation patterns.

For Slurm-based HyperPod, use Slurm's fair share scheduling
and quality of service (QoS) features to establish training
job SLAs that correspond to business criticality, implementing
job preemption policies that allow high-priority workloads to
temporarily utilize resources from less critical tasks.

Both systems benefit from establishing differentiated training
SLAs where production model training receives consistent
resources and fast completion times, while development and
experimentation workloads operate with longer acceptable
completion windows, enabling better resource sharing and
utilization.

Additionally, implement flexible training plans that
automatically find cost-efficient combinations of compute
capacity blocks, auto-resume functionality to handle
acceptable interruptions for non-critical workloads, and usage
reporting to continuously monitor and optimize the
relationship between SLA commitments and actual sustainability
impact.

In summary, adopting serverless data storage and processing
services, combined with intelligent data management practices such
as tiering, lifecycle policies, and efficient data formats, can
significantly enhance sustainability and operational efficiency in
data handling.

### Implementation steps

- Use Amazon S3 for data storage.

Enable S3 Intelligent-Tiering to automatically optimize
storage costs based on access patterns
- Implement S3 Lifecycle policies to manage data
transitions and deletions efficiently
- Automate processes to remove redundant data
- Use S3 Storage Lens for data usage insights and
optimization

- Optimize data formats and compression.

Adopt columnar formats and convert data to formats like
Parquet for enhanced analytical performance
- Apply compression techniques to reduce storage and
transfer costs using appropriate compression methods

- Use serverless query and processing services.

Use Athena to perform serverless SQL queries on S3 data
- Use AWS Glue to run serverless ETL jobs, discover
schemas, and catalog data
- AWS Lambda to handle event-driven computing tasks

- Automatically scale batch processing.

Consider Amazon EMR with autoscaling to process
large-scale Spark jobs efficiently
- Assess resource efficiency between Lambda, EMR, and AWS Batch
- Use Lambda for short (under 15 minutes) processing jobs
- Consider EMR or Batch for larger scale jobs

- Monitor your resource utilization.

Use AWS Cost Explorer and AWS Trusted Advisor for cost
and resource optimization recommendations
- Review Amazon CloudWatch metrics to identify efficiency
improvements

## Resources

**Related best practices:**

- [SUS04-BP04](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html)
- [SUS04-BP03](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html)
- [SUS04-BP02](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a3.html)

**Related documents:**

- [AWS Well Architected Framework Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html)
- [Revolutionizing Real-World Evidence: How Generative AI Can Simplify Data
Exploration](https://aws.amazon.com/blogs/industries/revolutionizing-real-world-evidence-how-generative-ai-can-simplify-data-exploration/)
- [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/)
- [Examples of S3
Lifecycle configurations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)
- [Zero-ETL
integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html)
- [AWS Lambda Machine Learning Blogs and Sample Applications](https://aws.amazon.com/blogs/machine-learning/category/compute/aws-lambda/)

**Related examples:**

- [Optimizing
streaming media workflows to reduce your carbon
footprint](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)
- [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Advanced Scaling for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/managed-scaling-allocation-strategy-optimized.html)

**Related tools:**

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Data discovery
and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus02-bp01.html*

---

# GENSUS03 — Consume energy efficient models

**Pillar**: Sustainability  
**Best Practices**: 1

---

# GENSUS03-BP01 Leverage smaller models and optimized inference techniques to reduce carbon footprint

To manage computational demands and costs of deploying large
language models, implement model optimization techniques. This best
practice aims to increase AI operational efficiency by reducing
resource consumption while meeting performance goals. Strategies
like quantization, pruning, and model distillation help lower
operational expenses, improve response times, and promote
environmental sustainability. This approach enables you to deploy
efficient, cost-effective, and eco-friendly AI solutions, allowing
for application scaling without excessive costs or environmental
impact.

**Desired outcome:** After
implementing model optimization practices, you will have
cost-effective and carbon-effective AI solutions.

**Benefits of establishing this best
practice:**
[Optimize
resource utilization](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) - Minimize environmental impact by
maximizing the efficiency of generative AI resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To effectively reduce the computational requirements of generative
AI models without compromising performance, it is essential to
implement a combination of optimization techniques such as
quantization, pruning, and the adoption of efficient model
architectures. Quantization involves reducing the precision of the
numbers used to represent the model's weights and activations.
This technique can decrease the model size and speed up inference
times with minimal impact on performance. Pruning, on the other
hand, involves removing redundant or unnecessary parameters from
the model. By identifying and alleviating weights that contribute
little to the model's predictions, pruning can lead to more
compact and efficient models.

In addition to these techniques, leveraging efficient model
architectures specifically designed for reduced computational
requirements can further enhance performance. Instead of relying
on large, general-purpose models, fine-tuning smaller models
tailored to specific use cases can often yield comparable results
with less computational resources. This approach allows for more
targeted optimization and can lead to more efficient deployments.

Amazon Bedrock supports this through its model distillation
feature. Model distillation involves training a smaller, more
efficient model to mimic the performance of a larger, more complex
model. This process results in a distilled model that maintains
similar performance levels while requiring fewer resources. By
utilizing such techniques, organizations can reduce computational
costs, making generative AI more accessible and scalable for a
wider range of applications.

With Amazon SageMaker AI, you can improve the performance of your
generative AI models by applying inference optimization techniques
to attain lower resource utilization and costs. Choose which of
the supported optimization techniques to apply, including
quantization, speculative decoding, LoRA and A, and compilation. After your
model is optimized, you can run an evaluation to see performance
metrics for latency, throughput, and price.

### Implementation steps

- Select optimization techniques.

Evaluate considerations between model size, speed, and
accuracy. Evaluate the effect on tasks and overall
performance
- Use SageMaker AI inference optimization techniques like LoRa
and quantization
- Use Amazon Bedrock Model Distillation feature to knowledge
transfer from a larger model to a smaller model

- Evaluate optimized models.

Compare performance with original models
- Assess resource savings and verify accuracy and
functionality taking edge cases into considerations

## Resources

**Related best practices:**

- [SUS02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_user_a2.html)
- [SUS05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_hardware_a3.html)
- [SUS02-BP03](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html)

**Related documents:**

- [Impel enhances automative dealership customer experience with fine-tuned LLMs on SageMaker AI](https://aws.amazon.com/blogs/machine-learning/impel-enhances-automotive-dealership-customer-experience-with-fine-tuned-llms-on-amazon-sagemaker/)
- [A
guide to Amazon BedrockModel Distillation (preview)](https://aws.amazon.com/blogs/machine-learning/a-guide-to-amazon-bedrock-model-distillation-preview/)
- [Fine-tune
large language models with Amazon SageMaker AI Autopilot](https://aws.amazon.com/blogs/machine-learning/fine-tune-large-language-models-with-amazon-sagemaker-autopilot/)
- [Inference
optimization for Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html)
- [Quantum-amenable
pruning of large language models and large vision models using
block coordinate descent](https://aws.amazon.com/blogs/quantum-computing/quantum-amenable-pruning-of-large-language-models-and-large-vision-models-using-block-coordinate-descent/)
- [Improve
the relevance of query responses with a reranked model in
Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html)

**Related examples:**

- [LLM
Rank pruning](https://github.com/amazon-science/llm-rank-pruning)
- [Optimizing
Generative AI LLM Inference Deployment on AWS GPUs By
Leveraging Quantization](https://github.com/aws-samples/optimizing-llm-inference-with-quantization)
- [Amazon SageMaker AI inference optimization toolkit for generative AI
using quantization](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-launches-the-updated-inference-optimization-toolkit-for-generative-ai/)

**Related tools:**

- [Amazon Bedrock](https://aws.amazon.com/bedrock/?nc2=type_a)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai/)
- [AWSCloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gensus03-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
