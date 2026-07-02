# MLSUS04 — Model development

**Pillar**: Sustainability  
**Best Practices**: 4

---

# MLSUS04-BP01 Define sustainable performance criteria

Creating machine learning models that balance accuracy with
environmental impact is essential for sustainable AI development.
When we focus exclusively on model accuracy, we overlook the
economic, environmental, and social costs of achieving marginal
performance improvements. Since the relationship between model
accuracy and complexity is logarithmic at best, continuing to train
a model longer or searching extensively for better hyperparameters
often yields only minimal gains while significantly increasing
resource consumption.

**Desired outcome:** You establish
balanced performance criteria for your ML models that satisfy your
business requirements without excessive resource usage. You
implement mechanisms to optimize training efficiency, reducing
carbon footprint and costs while maintaining appropriate model
performance. Your machine learning lifecycle incorporates
sustainability as a core consideration alongside traditional metrics
like accuracy.

**Common anti-patterns:**

- Pursuing maximum model accuracy without considering
environmental impact.
- Using oversized models when smaller models would be sufficient.
- Allowing training jobs to run indefinitely with minimal
performance improvements.
- Ignoring resource utilization metrics during model development.

**Benefits of establishing this best
practice:**

- Reduced energy consumption and carbon footprint from ML
operations.
- Lower computational costs for model training and deployment.
- Faster development cycles with earlier training completion.
- Better alignment between business requirements and model
capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning models, balancing accuracy with
sustainability requires deliberate consideration of how much
performance is actually needed. The incremental gains in accuracy
often diminish significantly beyond certain thresholds, while
computational costs continue to rise. By defining sustainable
performance criteria upfront, you create guardrails that reduce
unnecessary environmental impact.

These criteria should reflect your specific business needs rather
than abstract notions of best possible performance. For many
applications, a model that is 95% accurate may provide the same
business value as one that is 96% accurate but requires twice the
computational resources to train. Understand this relationship to
make informed trade-offs.

Early stopping mechanisms represent one practical implementation
of sustainable criteria. These techniques automatically terminate
training when improvement plateaus, avoiding wasted computation.
Tools like SageMaker AI Debugger and Automatic Model Tuning
provide built-in capabilities to implement early stopping without
compromising model quality.

Regularly measuring and monitoring resource utilization can
identify opportunities for optimization. Tracking metrics like CPU
and GPU utilization, memory consumption, and training duration
provides visibility into your model development's environmental
impact and can identify inefficiencies.

### Implementation steps

- **Establish sustainable performance
criteria**. Define concrete performance thresholds
that meet your business requirements without excessive
resource consumption. Consider both the absolute performance
levels needed and the point at which additional gains become
negligible. Include both accuracy and efficiency metrics in
your criteria, such as inference latency, model size, and
training resource requirements.
- **Analyze the accuracy-resource
tradeoff**. Conduct experiments to understand the
relationship between model performance and resource
consumption for your specific use case. Plot accuracy
against training time, model size, or computational
resources to identify the point of diminishing returns. Use
this data to set reasonable stopping criteria for your
training jobs.
- **Configure early stopping in training
jobs**. Set up SageMaker AI Automatic Model Tuning
with early stopping to terminate training jobs that are not
showing significant improvement. Navigate to the SageMaker AI
console, create a hyperparameter tuning job, and enable the
early stopping option. Alternatively, configure early
stopping programmatically using the SageMaker AI Python SDK by
setting the early_stopping_type parameter
to **Auto**.
- **Implement debugging
rules**. Use SageMaker AI Debugger to automatically
stop training when specific conditions are met. Add rules
like LossNotDecreasing to your training
script to detect when your model stops improving. For
example, configure the rule to stop training if the loss
doesn't decrease by at least 0.01% over the last ten epochs.
- **Monitor resource
utilization**. Track the efficiency of your
training jobs using CloudWatch metrics or SageMaker AI
Debugger's Profiling Report. Monitor metrics such as
CPUUtilization,
GPUUtilization,
GPUMemoryUtilization,
MemoryUtilization, and
DiskUtilization. Identify patterns of
resource underutilization that might indicate opportunities
for right-sizing your infrastructure.
- **Right-size your training
infrastructure**. Based on utilization metrics,
adjust the instance types and counts for your training jobs.
Select the most efficient instance type that meets your
performance requirements rather than defaulting to the most
powerful option. For distributed training jobs, verify that
you're using an appropriate number of instances to maximize
utilization.
- **Validate against business
requirements**. Before finalizing your model,
verify that it meets the business requirements while
adhering to your sustainable performance criteria. Document
the tradeoffs made and the rationale behind them to provide
transparency to stakeholders.
- **Use no-code ML for rapid
prototyping**. Use
[SageMaker AI
Canvas](https://aws.amazon.com/sagemaker/canvas/) with natural language support for data
exploration and model development to quickly validate ML
approaches before investing in resource-intensive custom
development. Canvas can generate models with minimal
computational overhead for initial feasibility testing.
Export Canvas-generated models and code to notebooks for
further optimization and sustainable development practices.
- **Use AI-powered code generation for
sustainable development**. Use AI-powered
development tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
efficient ML code, automate performance optimization
scripts, and accelerate the implementation of sustainable ML
practices while reducing development resource consumption.
- **Consider smaller specialized
models**. For generative AI applications, evaluate
whether smaller, domain-specific models can meet your needs
instead of using large general-purpose models. Techniques
like retrieval-augmented generation (RAG) can enhance
smaller models' capabilities while maintaining lower
resource requirements. Fine-tuning a smaller base model on
your specific data often provides better sustainability
outcomes than using larger generic models.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Stop
Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html)
- [Model
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)
- [Amazon SageMaker AI Debugger - Built-in Rules:
LossNotDecreasing](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html#loss-not-decreasing)
- [SageMaker AI job metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html#cloudwatch-metrics-jobs)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus04-bp01.html*

---

# MLSUS04-BP02 Select energy-efficient algorithms

Choosing energy-efficient algorithms minimizes resource usage while
maintaining performance, reducing your machine learning workloads'
environmental impact and operational costs.

**Desired outcome:** You establish a
systematic approach for selecting and optimizing algorithms that
deliver the necessary performance while minimizing computational
resources. Your ML workloads run more efficiently, reducing energy
consumption, carbon footprint, and infrastructure costs without
significant performance degradation.

**Common anti-patterns:**

- Defaulting to the most complex algorithm without evaluating
simpler alternatives.
- Ignoring model compression techniques that could reduce resource
requirements.
- Overlooking the environmental impact of computational resources.
- Focusing solely on model accuracy without considering resource
efficiency.

**Benefits of establishing this best
practice:**

- Reduced energy consumption and carbon footprint.
- Faster inference times and improved user experience.
- Ability to deploy ML models on resource-constrained devices.
- Extended battery life for edge devices running ML workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Energy-efficient algorithm selection requires balancing model
performance with resource consumption. When developing machine
learning models, computational efficiency directly impacts
sustainability and cost. Starting with simpler algorithms provides
a baseline for comparison and often delivers sufficient results
without excessive resource demands. Modern approaches like model
distillation, pruning, and quantization enable you to achieve
near-equivalent results using significantly fewer resources.

The environmental impact of ML workloads increases with model
complexity, making optimization techniques essential for
sustainable AI development. By systematically evaluating algorithm
efficiency alongside performance metrics, you can make informed
decisions that reduce your carbon footprint while maintaining
service quality.

### Implementation steps

- **Begin with a simple algorithm to
establish a baseline:** Start your development
process with straightforward algorithms that provide a
reference point for performance and resource usage. Then
[test
different algorithms with increasing complexity](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-07.html) to
observe whether performance improvements justify additional
resource consumption. Measure both model accuracy and
resource utilization metrics to make informed decisions
about complexity trade-offs.
- **Explore simplified versions of
popular algorithms:** Research and implement
distilled or optimized versions of standard algorithms that
deliver similar performance with reduced computational
requirements. For example, DistilBERT, a distilled version
of
[BERT](https://en.wikipedia.org/wiki/BERT_(language_model)),
has 40% fewer parameters, runs 60% faster, and preserves 97%
of its performance. Similar approaches exist for many common
model architectures.
- **Implement model compression
techniques:** Apply pruning to remove model weights
that contribute minimally to predictions, reducing model
size and computational requirements. Use quantization to
represent numerical values with lower precision,
significantly decreasing memory usage and processing demands
while maintaining acceptable accuracy levels.
- **Leverage AWS optimization
services:** Deploy
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to automatically optimize your ML
models for inference on cloud resources and edge devices.
SageMaker AI Neo analyzes your model and generates optimized
code that maximizes performance while minimizing resource
consumption, allowing you to deploy more efficient models
across diverse deployment targets.
- **Monitor and optimize resource
utilization:** Track the
[resources
provisioned](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceConfig.html) for your training and inference jobs
(InstanceCount, InstanceType, and VolumeSizeInGB) and their
[efficient
use](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html#cloudwatch-metrics-jobs) (CPUUtilization, GPUUtilization,
GPUMemoryUtilization, MemoryUtilization, and
DiskUtilization) through the
[SageMaker AI
Console](https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html#view-train-metrics-sm),
[CloudWatch
Console](https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html#view-train-metrics-cw) or your
[SageMaker AI
Debugger Profiling Report](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profiling-report.html#debugger-profiling-report-walkthrough-system-usage). Use these insights to
right-size your resources and identify optimization
opportunities.
- **Consider hardware-specific
optimizations:** Choose appropriate instance types
for training and inference based on your model's
characteristics. Some algorithms perform better on GPU
instances, while others may be more efficient on CPU or
specialized accelerators like AWS Inferentia. Matching your
algorithm to the optimal hardware can significantly improve
energy efficiency.
- **Use optimized foundation model
containers:** Deploy models using SageMaker AI's
optimized foundation model containers that include
pre-configured environments with built-in quantization and
optimization techniques. These containers support frameworks
like Hugging Face Transformers and provide automatic
performance optimizations.
- **Use AI-powered code generation for
algorithm optimization**. Use AI-powered
development tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
optimized algorithm implementations, automate model
compression code, and accelerate the development of
energy-efficient ML solutions.
- **Apply efficient architectures for
foundation models:** When working with generative
AI models, consider parameter-efficient fine-tuning
approaches like LoRA (Low-Rank Adaptation) or P-tuning
instead of full fine-tuning. These techniques can reduce the
computational resources required while achieving comparable
performance. Leverage pre-trained foundation models
available through SageMaker AI JumpStart to avoid the
energy-intensive process of training from scratch.

## Resources

**Related documents:**

- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)
- [The
AWS Inferentia Chip With DLAMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia.html)
- [Prepare
Model for Compilation](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-compilation-preparing-model.html)
- [Optimize
AI/ML workloads for sustainability: Part 2, model
development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/)

**Related videos:**

- [Deploy
an ML model for best performance, cost, and prediction
quality](https://www.youtube.com/watch?v=ftCFf57dQQY)
- [SageMaker AI
HyperPod: Revolutionizing Foundation Model Training with
Resilience and Performance](https://aws.amazon.com/awstv/watch/c60e1437f63/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus04-bp02.html*

---

# MLSUS04-BP03 Archive or delete unnecessary training artifacts

Remove training artifacts that are unused and no longer required to
limit wasted resources. Determine when you can archive training
artifacts to more energy-efficient storage or safely delete them.

**Desired outcome:** You reduce your
environmental footprint by removing unnecessary storage of ML
training artifacts. Your organization maintains only essential
training data and models, efficiently archives what might be needed
later, and systematically removes what is no longer required. This
approach not only conserves resources but also simplifies management
of your machine learning assets.

**Common anti-patterns:**

- Keeping training artifacts indefinitely.
- Ignoring the accumulation of unused logs, models, and experiment
data.
- Not implementing systematic cleanup processes for completed
experiments.

**Benefits of establishing this best
practice:**

- Reduced storage costs and resource consumption.
- Improved organization and discoverability of important ML
artifacts.
- Enhanced security through reduced data surface area.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning workflows generate substantial volumes of
artifacts during the development process. These include experiment
data, logs, model checkpoints, and various intermediary outputs.
While some of these artifacts are essential for long-term use,
many become unnecessary after model deployment or project
completion.

Consider the lifecycle of your ML artifacts. Some might need
preservation for compliance-aligned or reproducibility purposes,
while others can be safely removed once they've served their
immediate purpose. For artifacts that must be retained but are
rarely accessed, consider using tiered storage options that
balance accessibility with resource efficiency.

### Implementation steps

- **Organize your ML experiments with
management tools**. Use
[SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/) to track, compare, and organize your
machine learning experiments in a structured manner. This
organization makes it more straightforward to identify which
artifacts are essential and which can be archived or
deleted.
- **Implement regular cleanup
procedures**. Follow the
[clean
up training resources](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html) guidance from AWS to
systematically remove SageMaker AI resources you no longer
need. Create automated cleanup workflows that run on a
schedule to avoid the accumulation of unused artifacts.
- **Set appropriate log retention
policies**. By default, Amazon CloudWatch retains
logs indefinitely, which consumes unnecessary resources.
Implement
[limited
retention time](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) for your notebooks and training logs
to automatically expire and delete logs after they're no
longer needed.
- **Establish storage lifecycle
policies**. Configure
[Amazon S3 lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition
training artifacts to more cost-effective and
energy-efficient storage classes like Amazon Glacier or S3 Glacier Deep Archive based on access patterns.
- **Monitor storage
utilization**. Use
[Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/) to gain visibility into your storage
usage patterns and identify opportunities for optimization.
Track metrics regularly to verify that your cleanup
procedures are effective.
- **Implement container image
cleanup**. Use
[Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to automatically clean up
unused container images that may have been created during
training jobs. This avoids the accumulation of outdated or
unused container images.
- **Establish artifact tagging
standards**. Create a consistent tagging strategy
for ML artifacts to identify their purpose, associated
projects, and expiration dates. This makes it simpler to
determine what can be archived or deleted during cleanup
processes.
- **Leverage managed MLflow for
experiment tracking**. Use
[managed
MLflow on SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to create, manage, analyze, and
compare your machine learning experiments with better
organization and tracking capabilities, making it more
straightforward to identify which experiments and associated
artifacts can be safely archived or deleted.
- **For GenAI foundation models,
implement token usage monitoring and cleanup**. For
generative AI projects, monitor token usage and intermediate
outputs, which can quickly accumulate. Implement automated
cleanup of temporary prompts, completions, and generated
content that isn't required for the final model.

## Resources

**Related documents:**

- [Clean
up Amazon SageMaker AI notebook instance resources](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-cleanup.html)
- [Cataloging
and analyzing your data with S3 Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html)
- [What
Is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Working
with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention)
- [Automate
the cleanup of images by using lifecycle policies in Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)
- [AWS Systems Manager for Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [What
Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [Optimizing
MLOps for Sustainability](https://aws.amazon.com/blogs/machine-learning/optimizing-mlops-for-sustainability/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus04-bp03.html*

---

# MLSUS04-BP04 Use efficient model tuning methods

Optimize your machine learning model's hyperparameters with
resource-efficient strategies that minimize computational needs
while improving performance. Efficient tuning methods can
significantly reduce costs, energy consumption, and time-to-market
compared to resource-intensive brute force approaches.

**Desired outcome:** You can
systematically find optimal hyperparameters for your machine
learning models while minimizing computational resource consumption.
By implementing intelligent search strategies and following best
practices for optimization, you achieve better model performance
with fewer resources, reduce your environmental footprint, and
accelerate time-to-market for your ML solutions.

**Common anti-patterns:**

- Using grid search, which tests the most possible combinations of
hyperparameters.
- Running many concurrent training jobs without considering how
results from previous jobs can inform later ones.
- Specifying excessively broad hyperparameter ranges without
proper understanding of their impact.
- Using random search when more efficient options like Bayesian or
Hyperband are available.

**Benefits of establishing this best
practice:**

- Reduce computational resources required for hyperparameter
tuning by up to 10x compared to random search.
- Decrease energy consumption and associated carbon emissions from
ML training.
- Find optimal hyperparameters faster, accelerating
time-to-market.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hyperparameter tuning is a crucial step in machine learning model
development that directly impacts both model performance and
resource utilization. Efficient tuning strategies can dramatically
reduce the computational resources required while finding optimal
or near-optimal parameter settings.

When approaching hyperparameter tuning, consider the relationship
between tuning strategy and resource consumption. Grid search,
which exhaustively tests the most possible combinations, is the
most resource-intensive approach and should generally be avoided.
Random search provides better resource efficiency but lacks
intelligence in selecting which configurations to test. More
sophisticated approaches like Bayesian optimization and Hyperband
can find optimal hyperparameters with significantly fewer training
jobs, reducing both time and resource usage.

The efficiency of your hyperparameter tuning is also affected by
how you configure concurrent jobs and specify parameter ranges.
Running too many concurrent jobs can waste resources when using
methods that benefit from sequential exploration. Similarly,
specifying unnecessarily wide parameter ranges increases the
search space complexity without adding value.

### Implementation steps

- **Choose an efficient search
strategy**. Implement Bayesian optimization or
Hyperband search strategies instead of random or grid
search. Bayesian search uses information from previous
trials to make intelligent guesses about promising
hyperparameter configurations, typically requiring 10 times
fewer jobs than random search to find optimal parameters.
For large models like deep neural networks addressing
computer vision problems,
[Amazon SageMaker AI Hyperband](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) can find optimal hyperparameters
up to three times faster than Bayesian search.
- **Optimize job concurrency
settings**. Configure your hyperparameter tuning
jobs with appropriate concurrency settings. With Bayesian
optimization, running fewer concurrent jobs often yields
better results since the algorithm benefits from information
gathered in previous iterations. Balance the tradeoff
between parallelism (which speeds up overall completion
time) and sequential learning (which improves optimization
efficiency) based on your specific requirements for
time-to-completion versus resource efficiency.
- **Define thoughtful parameter
ranges**. Carefully select which hyperparameters to
tune and their corresponding value ranges. Focus on
parameters that significantly impact model performance and
limit ranges to reasonable values based on domain knowledge
or prior experiments. For parameters known to be log-scaled
(learning rates, regularization strengths), convert them to
log space to improve optimization efficiency. This focused
approach reduces the search space complexity, discovering
optimal configurations with fewer resources.
- **Leverage early stopping
capabilities**. Implement mechanisms to terminate
underperforming training jobs early to avoid wasting
resources on unpromising hyperparameter configurations. Use
Amazon SageMaker AI's built-in early stopping functionality
that automatically terminates training jobs that are
unlikely to produce better models than previously completed
jobs.
- **Monitor resource
utilization**. Track metrics related to resource
provisioning and utilization for your hyperparameter tuning
jobs. Use Amazon SageMaker AI's integration with Amazon CloudWatch to monitor CPU utilization, GPU utilization,
memory usage, and other resource metrics. Analyze these
metrics to identify optimization opportunities in your
tuning strategy.
- **Integrate with your MLOps
pipeline**. Incorporate efficient hyperparameter
tuning as a standard component of your MLOps workflow.
Automate the process of selecting optimal hyperparameters
and retraining models when necessary. This verifies the
consistent application of efficient tuning practices across
your machine learning projects.
- **Leverage pre-trained models to
reduce tuning scope**. Start with pre-trained
models from the expanded
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) catalog or
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) foundation models, which often require
minimal hyperparameter tuning for your use case,
significantly reducing computational resources compared to
training from scratch.
- **Leverage AI-powered code generation
for tuning automation**. Use AI-powered development
tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
efficient hyperparameter tuning scripts, automate
optimization workflows, and accelerate the implementation of
resource-efficient tuning strategies.
- **Consider warm-starting tuning
jobs**. Use the results from previous
hyperparameter tuning jobs to initialize new jobs when
incrementally improving models or adapting to changing data
patterns. This approach reduces the resources required to
find good hyperparameters compared to starting from scratch.

## Resources

**Related documents:**

- [Best
Practices for Hyperparameter Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html)
- [Automatic
model tuning with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Amazon SageMaker AI Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler.html)
- [Choosing
the Best Number of Concurrent Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html#automatic-model-tuning-parallelism)
- [Choosing
Hyperparameter Ranges](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html#automatic-model-tuning-choosing-ranges)
- [Amazon SageMaker AI Hyperband Search Strategy](https://aws.amazon.com/about-aws/whats-new/2022/09/amazon-sagemaker-automatic-model-tuning-provides-faster-hyperparameter-tuning-hyperband-search-strategy/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus04-bp04.html*

---
