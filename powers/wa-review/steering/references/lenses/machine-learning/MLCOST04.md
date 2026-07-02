# MLCOST04 — Model development

**Pillar**: Cost Optimization  
**Best Practices**: 14

---

# MLCOST04-BP01 Select optimal computing instance size

Right size your machine learning training instances according to the
algorithm and workload requirements to maximize efficiency and
reduce costs. By selecting the most appropriate computing resources,
you can improve performance while minimizing unnecessary expenses.

**Desired outcome:** You can identify
and select the optimal computing instance types for your machine
learning workloads based on actual resource utilization metrics. You
can systematically evaluate different instance options, understand
their cost implications, and optimize your machine learning
infrastructure spending while maintaining or improving performance.

**Common anti-patterns:**

- Using oversized instances for training jobs regardless of model
complexity.
- Ignoring resource utilization metrics during training.
- Failing to experiment with different instance types to find the
optimal cost-performance balance.
- Not considering the communication overhead in distributed
training scenarios.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs for machine learning workloads.
- Improved resource utilization and efficiency.
- Better understanding of ML workload performance characteristics.
- Optimization of price-performance ratio for different model
types.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning training workloads vary significantly in their
resource requirements based on model complexity, dataset size, and
algorithm characteristics. Simple models might not train faster on
larger instances because they cannot effectively utilize
additional compute resources, and might even train slower due to
high GPU communication overhead. By evaluating your workload's
resource needs, you can identify the most cost-effective instance
configuration.

The key to optimizing instance selection is understanding the
actual resource utilization patterns of your machine learning
workloads. Start with smaller instances and scale up only when
necessary based on performance data. Amazon SageMaker AI provides
tools like Debugger to monitor resource utilization and
Experiments to compare training performance across different
instance configurations. This data-driven approach assists you to
avoid paying for unused resources while maintaining optimal
training performance.

### Implementation steps

- **Understand your algorithm's resource
requirements**. Begin by analyzing whether your
machine learning algorithm is compute-bound, memory-bound,
or I/O-bound. Different algorithms have different scaling
characteristics and resource needs. For deep learning
workloads, consider whether GPU acceleration would provide
significant benefits or if CPU instances would be more
cost-effective for your specific model.
- **Use Amazon SageMaker AI
Experiments**.
[Amazon EC2](https://aws.amazon.com/ec2/instance-types/) provides a wide selection of instance types
optimized to fit different use cases. Machine learning
workloads can use either a CPU or a GPU instance. Select an
instance type from
[the
available EC2 instance types](https://aws.amazon.com/ec2/instance-types/) depending on the needs
of your ML algorithm. Experiment with both CPU and GPU
instances to learn which one gives you the best cost
configuration. Amazon SageMaker AI lets you use a single
instance or a distributed cluster of GPU instances. Use
[Amazon SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/) to evaluate alternative
options, and identify the size resulting in optimal outcome.
With the pricing broken down by time and resources, you can
optimize the cost of Amazon SageMaker AI and only pay for
what is needed.
- **Use Amazon SageMaker AI
Debugger**.
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) automatically monitors the
utilization of system resources, such as GPUs, CPUs,
network, and memory, and profiles your training jobs to
collect detailed ML framework metrics. You can inspect
resource metrics visually through SageMaker AI Studio and
take corrective actions if the resource is under-utilized to
optimize cost.
- **Start small and scale
gradually**. Begin with smaller instance sizes for
new models and monitor performance. Only increase instance
size when you have data showing that your workload can
benefit from additional resources. This approach assists you
to avoid overprovisioning and unnecessary costs.
- **Consider the communication
overhead**. For distributed training across
multiple GPUs or instances, evaluate the communication
overhead between nodes. In some cases, adding more compute
resources might actually slow down training due to increased
coordination requirements.
- **Monitor and analyze training
metrics**. Track key metrics like CPU/GPU
utilization, memory usage, I/O patterns, and training
throughput across different instance types to identify
bottlenecks and optimization opportunities.
- **Use Spot Instances for cost
savings**. For non-critical training jobs, consider
using
[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) through SageMaker AI to reduce costs
by up to 90%. Configure your training jobs to checkpoint
regularly to minimize the impact of potential interruptions.
- **Use SageMaker AI Inference Recommender
for optimal instance selection**. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) with enhanced algorithms and
support for multi-model endpoints to get sophisticated cost
optimization recommendations for your specific workloads.
- **For generative AI workloads, use
foundation model optimization techniques**. For
generative AI workloads, consider techniques like
quantization, distillation, and efficient fine-tuning
methods to reduce the computational resources needed while
maintaining model quality.
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) provides optimized foundation
models that can significantly reduce training time and
resource requirements.

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [Accelerate
generative AI development with Amazon SageMaker AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)
- [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Amazon SageMaker AI Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp01.html*

---

# MLCOST04-BP02 Use managed build environments

Using managed build environments for machine learning development
instead of local setups provides significant cost, time, and
resource advantages. Managed notebooks come pre-configured with
security, networking, storage, and compute capabilities that would
otherwise require extensive development and maintenance effort.
These environments also offer flexible machine selection, including
access to powerful GPUs and high-memory instances that may be
impractical in local setups.

**Desired outcome:** You can quickly
start machine learning development work without spending time
setting up infrastructure, managing dependencies, or configuring
development environments. You gain access to scalable compute
resources, including specialized hardware like GPUs, and benefit
from built-in security and collaboration features, allowing you to
focus on building ML models rather than managing infrastructure.

**Common anti-patterns:**

- Spending excessive time configuring local development
environments for each project.
- Encountering hardware limitations when training complex models
locally.
- Struggling with inconsistent development environments across
team members.
- Managing security and networking configurations manually.
- Inability to scale resources up or down based on workload
requirements.

**Benefits of establishing this best
practice:**

- Reduced time to start development with pre-configured
environments.
- Access to powerful compute resources on demand.
- Consistent development environments for team members.
- Built-in security, networking, and storage capabilities.
- Simplified collaboration and sharing of notebooks and models.
- Cost optimization through pay-for-what-you-use model.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing machine learning projects, your development
environment plays a critical role in productivity and efficiency.
Local development environments often lead to inconsistencies
between team members, dependency conflicts, and hardware
limitations. Managed build environments address these challenges
by providing standardized, scalable, and secure solutions for ML
development.

Amazon SageMaker AI offers several managed environment options
tailored to different user needs and expertise levels. These
include SageMaker AI Notebook Instances for individual developers,
SageMaker AI Studio for comprehensive ML development, and SageMaker AI
Canvas for no-code ML solutions. These environments come
pre-configured with the necessary tools and libraries, saving
setup time and fostering consistency.

These managed environments integrate seamlessly with other AWS
services, making it simple to access data stored in Amazon S3, use
specialized hardware like GPUs, and deploy models to production
endpoints. They also provide built-in security features, version
control, and collaboration capabilities that would be difficult to
implement in a local setup.

### Implementation steps

- **Evaluate your ML development
needs**. Begin by assessing your team's
requirements, including technical expertise, project
complexity, and compute resource needs. Identify which
SageMaker AI offering best matches these requirements.
- **Use Amazon SageMaker AI Notebook
Instances**. Set up SageMaker AI Notebook Instances
which provide a fully managed Jupyter notebook environment.
These instances come pre-loaded with popular ML frameworks
and libraries, allowing you to start working immediately.
- **Implement Amazon SageMaker AI
Studio**. Deploy SageMaker AI Studio as your
comprehensive ML development environment. SageMaker AI Studio
provides a web-based visual interface where your team can
perform ML development steps from data preparation to model
deployment. Access Studio by creating a SageMaker AI domain
through the SageMaker AI console, which enables team management
and resource sharing capabilities.
- **Deploy SageMaker AI Canvas for business
users**. Implement SageMaker AI Canvas for business
analysts and non-technical team members who need to create
ML models without coding. Canvas provides an intuitive
visual interface for importing data, creating models, and
generating predictions.
- **Set up proper IAM roles and
permissions**. Configure appropriate IAM roles for
your SageMaker AI environments to provide secure access to AWS
resources. Create specific roles that follow the principle
of least privilege, granting only the permissions necessary
for your ML workflows.
- **Configure data access and
storage**. Set up connections between your
SageMaker AI environments and data sources such as Amazon S3,
Amazon Redshift, or Amazon RDS. Configure appropriate
permissions to access these data sources securely.
- **Implement version control and
collaboration**. Integrate your managed
environments with version control systems like Git to track
changes to notebooks and code. Use SageMaker AI Studio's
built-in collaboration features to share work among team
members.
- **Optimize for cost
efficiency**. Configure auto-shutdown policies for
notebook instances when they're idle to reduce costs.
Monitor resource usage and adjust instance types as needed
to balance performance and cost.
- **Use SageMaker AI HyperPod for
large-scale training**. For distributed training of
large models, use
[SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) which provides purpose-built infrastructure
with automatic checkpoint storage and recovery, optimizing
resource utilization for long-running training jobs.
- **Enable SageMaker AI JupyterLab 3
features**. Take advantage of the productivity
improvements in JupyterLab 3, which is available in both
SageMaker AI Studio and Notebook Instances, providing better
performance and enhanced features for developers.

## Resources

**Related documents:**

- [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/)
- [Amazon SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp02.html*

---

# MLCOST04-BP03 Select local training for small scale experiments

When developing machine learning models, choosing the right training
environment is crucial for both cost efficiency and rapid
experimentation. By evaluating whether to train your ML model
locally or in the cloud, you can optimize your development workflow
and appropriately match resources to the scale of your experiment.

**Desired outcome:** You can rapidly
iterate on machine learning experiments with small datasets by
training models locally, while having a clear path to scale up to
cloud-based training when working with larger datasets. This
approach enables faster development cycles during the
experimentation phase and cost-effective scaling when required for
production workloads.

**Common anti-patterns:**

- Deploying cloud-based training clusters regardless of dataset
size.
- Using oversized compute instances for small-scale
experimentation.
- Not considering the time and cost implications of repeatedly
launching training clusters during the experimentation phase.
- Failing to right-size compute resources based on specific
workload requirements.

**Benefits of establishing this best
practice:**

- Reduced development costs during experimentation phases.
- Faster iteration cycles when testing various algorithms and
configurations.
- Simplified workflow for early-stage development.
- Clear scaling path from local experimentation to production
deployment.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning models, you often need to
experiment with multiple algorithms, configurations, and
hyperparameters before finding an optimal solution. The choice
between local training and cloud-based training significantly
impacts both development speed and cost efficiency.

Local training is most advantageous during early experimentation
phases when working with small datasets. This approach reduces the
overhead of provisioning cloud resources and waiting for training
clusters to spin up for each experiment iteration. Your
development cycle becomes more agile as you can quickly test
hypotheses and make adjustments without incurring additional cloud
costs.

As your models and datasets grow in size and complexity,
transitioning to cloud-based training becomes necessary. Cloud
environments offer scalable computing resources that can handle
large datasets and complex models that would be impractical to
process on local machines. By right-sizing your compute instances
based on your specific workload requirements, you can maintain
cost efficiency while gaining the performance benefits of cloud
infrastructure.

### Implementation steps

- **Evaluate your training
requirements**. Before deciding on local or
cloud-based training, assess your dataset size, model
complexity, and computational requirements. Small datasets
(typically under a few gigabytes) and simpler models are
generally good candidates for local training, especially
during initial experimentation.
- **Set up Amazon SageMaker AI local
mode**. When experimenting with small datasets, use
Amazon SageMaker AI's local mode to train models directly on
your notebook instance. This approach allows you to test and
iterate on your code without provisioning separate training
clusters. To implement local mode:

```
`from sagemaker.estimator import Estimator

estimator = Estimator(
image_uri="your-container-image",
role="your-sagemaker-role",
instance_count=1,
instance_type="local"
)

estimator.fit({"train": "s3://your-bucket/train-data"})`
```
- **Use local development environment
with SageMaker AI SDK**. For development outside of
SageMaker AI notebooks, install the SageMaker AI Python SDK on
your local machine. This allows you to develop and test
locally while still having the ability to deploy models to
AWS:

```
`pip install sagemaker`
```
- **Profile your workloads for cloud
deployment**. As your models mature and datasets
grow, prepare for cloud deployment by profiling your
workloads. Identify memory usage, CPU and GPU requirements,
and processing time to determine appropriate instance types
for cloud-based training.
- **Right-size cloud-based training
clusters**. When moving to cloud training, select
appropriate instance types based on your workload profiling.
Consider factors such as:

Model architecture (CPU and GPU requirements)
- Memory needs
- Dataset size and I/O patterns
- Training time constraints
- Cost constraints

- **Implement distributed training for
large-scale workloads**. For large datasets or
complex models, configure distributed training across
multiple instances to reduce training time.
- **Monitor and optimize cloud resource
usage**. Regularly review your training job metrics
to identify opportunities for optimization. Use SageMaker AI
Experiments to track and compare resource utilization across
different training configurations.
- **Use enhanced local development
capabilities**. Use improved SageMaker AI local mode
with better debugging and monitoring capabilities, allowing
for more efficient local experimentation before scaling to
cloud resources.
- **For generative AI workloads, use
foundation models efficiently**. When working with
generative AI and foundation models, consider using Amazon SageMaker AI JumpStart for local experimentation with smaller,
distilled versions of foundation models before fine-tuning
larger models in the cloud. This approach allows for rapid
prototyping while managing costs effectively.

## Resources

**Related documents:**

- [Model
training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)
- [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/SageMaker AI)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [SageMaker AI
Python SDK Documentation](https://sagemaker.readthedocs.io/en/stable/)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Generative
AI Cost Optimization Strategies](https://aws.amazon.com/blogs/enterprise-strategy/generative-ai-cost-optimization-strategies/)

**Related videos:**

- [Train
with Amazon SageMaker AI on your local machine](https://www.youtube.com/watch?v=K3ngZKF31mc)

**Related examples:**

- [SageMaker AI
Local Mode Examples](https://github.com/aws-samples/amazon-sagemaker-local-mode)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp03.html*

---

# MLCOST04-BP04 Select an optimal ML framework

Selecting the most cost-effective machine learning (ML) framework
for your requirements can significantly impact your operational
efficiency and return on investment. By systematically comparing
frameworks like TensorFlow, PyTorch, and Scikit-learn, you can
determine which delivers the best performance for your specific use
cases at the optimal cost.

**Desired outcome:** You establish a
systematic approach for evaluating ML frameworks and instance types,
and you can select the optimal combination based on performance,
cost, and use case requirements. You can track, compare, and analyze
experiments across different frameworks, leading to informed
decisions that maximize performance while minimizing costs.

**Common anti-patterns:**

- Selecting ML frameworks based on popularity rather than
suitability for your specific use case.
- Using a single framework for ML projects regardless of workload
characteristics.
- Not tracking experiment metrics systematically across different
frameworks.
- Failing to benchmark performance and cost metrics before moving
to production.

**Benefits of establishing this best
practice:**

- Reduced operational costs through optimized infrastructure
selection.
- Improved model performance by selecting the most suitable
framework.
- Enhanced productivity by streamlining experiment tracking and
comparison.
- Faster iteration and deployment of ML models.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Selecting the optimal ML framework involves evaluating different
options against your specific requirements and constraints.
Consider factors such as model complexity, data volume,
performance requirements, and team expertise when choosing between
frameworks. Tracking experiments systematically assists you to
compare approaches objectively and make data-driven decisions.

When implementing this best practice, use AWS' comprehensive ML
infrastructure, which supports major frameworks and provides tools
for experiment tracking and resource optimization. Regular
performance benchmarking and cost analysis should become standard
procedures in your ML development process.

### Implementation steps

- **Implement systematic experiment
tracking with SageMaker AI Experiments**. Amazon SageMaker AI Experiments enables you to organize, track,
compare, and evaluate your machine learning experiments.
Create experiments to group related trials, assign
parameters, metrics, and artifacts to each trial, and track
the lineage of model artifacts to experiments for governance
and reproducibility.
- **Compare multiple ML
frameworks**. Evaluate frameworks like TensorFlow,
PyTorch, Apache MXNet, and Scikit-learn for your specific
use cases. Use
[AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/) and
[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/) to experiment with different
frameworks using consistent infrastructure. These AMIs come
with popular frameworks preinstalled, making it simple to
switch between them for comparison.
- **Benchmark framework
performance**. Design standardized benchmarking
tests for your specific workloads across different
frameworks. Track metrics such as training time, inference
latency, memory usage, and accuracy to determine which
framework performs best for your use case.
- **Implement right-sizing strategies
for ML instances**. Use SageMaker AI's managed
instances to automatically select the most appropriate and
cost-effective instance type for your workloads. Experiment
with different instance types to find the optimal balance
between performance and cost.
- **Use SageMaker AI's
bring-your-own-container capability**. If you need
to use specialized ML frameworks or versions not available
in standard containers, use SageMaker AI's flexibility to bring
your own containers so that you can use a framework while
maintaining the benefits of SageMaker AI's managed
infrastructure.
- **Implement automatic resource
scaling**. Configure automatic scaling for
inference endpoints based on traffic patterns to optimize
costs during varying load conditions. Use SageMaker AI
Inference Recommender to identify the best configuration for
deployment.
- **Use enhanced experiment tracking
with MLflow**. Use
[managed
MLflow on SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to create, manage, analyze, and
compare your machine learning experiments across different
frameworks with better organization and tracking
capabilities.
- **Monitor and optimize costs
continuously**. Implement cost monitoring using AWS Cost Explorer and SageMaker AI's built-in monitoring
capabilities. Set up alerts for unusual spending patterns
and regularly review resource utilization to identify
optimization opportunities.

## Resources

**Related documents:**

- [AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/)
- [Machine
Learning Frameworks and Languages](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html)
- [Accelerate
generative AI development with Amazon SageMaker AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)
- [Amazon SageMaker AI Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp04.html*

---

# MLCOST04-BP05 Use automated machine learning

Automate your model development process by using systems that
experiment with and select the best algorithms from high-performing
options. These automated systems test various solutions and
parameter settings to achieve optimal models, significantly speeding
up development while reducing the need for manual experimentation
and comparisons.

**Desired outcome:** You gain the
ability to develop high-quality machine learning models in a
fraction of the time traditionally required. By using automated
machine learning tools like Amazon SageMaker AI Autopilot, you can
focus on business problems rather than algorithm selection and
parameter tuning. Your team can produce optimized models with better
performance, reduce development costs, and accelerate time-to-market
for ML-powered solutions.

**Common anti-patterns:**

- Manually testing multiple algorithms and configurations one by
one.
- Spending excessive time on hyperparameter tuning without
systematic approach.
- Using the same algorithm for each problem without considering
alternatives.
- Neglecting cross-validation during model selection.

**Benefits of establishing this best
practice:**

- Dramatically reduced time to develop production-ready models.
- Access to a broader range of algorithms and optimization
techniques.
- Improved model performance through systematic evaluation.
- Lower costs through optimized resource utilization.
- Ability for domain experts to build models without deep ML
expertise.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Automated machine learning (AutoML) systems democratize the
process of building machine learning models. By automating key
steps in model development—from data preparation to algorithm
selection and hyperparameter tuning—these systems enable even
those without extensive machine learning expertise to develop
high-quality models.

When using AutoML solutions like Amazon SageMaker AI Autopilot,
you provide your dataset and define your objective, and the system
handles the complex work of exploring potential algorithms,
optimizing parameters, and evaluating model performance. The
system applies cross-validation procedures automatically to check
that models can generalize well to new data. By ranking optimized
models by their performance, AutoML can identify the best solution
for your specific problem.

Beyond simply producing models, modern AutoML systems provide
visibility into the development process, allowing you to
understand what choices were made and why. This transparency
builds trust in the models and provides learning opportunities for
your team to understand what approaches work best for different
problem types.

### Implementation steps

- **Evaluate your use case
compatibility**. Determine if your ML problem is
suitable for automated machine learning solutions. AutoML
works particularly well for standard machine learning tasks
like classification, regression, and some time series
forecasting scenarios.
- **Prepare your data for
AutoML**. Clean your dataset, handle missing
values, and convert categorical features appropriately.
While AutoML handles feature engineering, providing
high-quality data improves results. Use
[Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) to simplify this preparation
process.
- **Set up Amazon SageMaker AI Autopilot
with Canvas**. Open
[Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html), import your dataset into Amazon S3,
and configure to access this data. Define your target
variable and specify your problem type (classification or
regression) if known.
- **Launch the automated ML
job**. Start Canvas training and let it analyze
your data, select algorithms, and optimize models. Specify
resources like maximum runtime and instance types to control
costs. Canvas will automatically handle data preprocessing,
feature engineering, algorithm selection, and hyperparameter
optimization.
- **Review candidate models**.
Examine the generated models along with their performance
metrics. Autopilot provides detailed reports on the data
exploration, feature engineering decisions, and model
optimization steps it performed.
- **Deploy the best model**.
Select the best-performing model from the Canvas
recommendations and deploy it using Amazon SageMaker AI's
deployment capabilities. You can deploy as a real-time
endpoint or for batch inference depending on your needs.
- **Monitor and evaluate
performance**. Set up model monitoring to track
your model's performance in production and detect concept
drift. Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automate this process.
- **Customize and refine
models**. If needed, extract and customize the
models generated by Autopilot. The solution provides full
visibility into the notebooks and artifacts it creates,
allowing you to further refine specific aspects of the
model.
- **Enhance model development with
foundation models**. Use
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to incorporate foundation model capabilities
into your AutoML workflow for tasks like text processing,
content generation, and multimodal applications. Foundation
models can complement traditional ML approaches handled by
Autopilot.
- **Use enhanced Canvas capabilities
with Q integration**. Use
[SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) with improved natural language support and Q
integration for conversational data analysis, enabling
business users to build models through natural language
interactions.
- **Implement intelligent preprocessing
with generative AI**. Use generative AI tools to
enhance data preprocessing, augment training datasets,
generate synthetic data for edge cases, and improve feature
engineering through intelligent text and image processing.

## Resources

**Related documents:**

- [Getting
started with using Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html)
- [SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/)

**Related examples:**

- [SageMaker AI Autopilot](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/automl/README.rst)
- [Amazon SageMaker AI Autopilot Sample Notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp05.html*

---

# MLCOST04-BP06 Use managed training capabilities

Machine learning model training can be an iterative,
compute-intensive, and time-consuming process. Instead of using the
notebook itself, which might be running on a small instance,
offloading the training to a managed cluster of compute resources
including both CPUs and GPUs enables more efficient and
cost-effective model training.

**Desired outcome:** By using managed
training capabilities, you optimize your machine learning training
workflows and infrastructure management. You gain access to scalable
computing resources that automatically adjust based on your workload
needs, from single GPUs to thousands, without managing the
underlying infrastructure. You can significantly reduce training
costs through specialized hardware options, compiler optimizations,
and spot instance utilization while maintaining visibility into
metrics and logs for proper monitoring and governance.

**Common anti-patterns:**

- Running complex model training jobs on notebook instances,
leading to resource constraints and inefficiency.
- Managing your own GPU clusters for training, requiring
significant operational overhead.
- Using exclusively on-demand instances for training jobs,
resulting in higher costs.
- Not using specialized training optimizations like distributed
training or compiler acceleration.

**Benefits of establishing this best
practice:**

- Lower training costs by up to 90% using managed spot instances.
- Accelerate training time by up to 50% with training compiler
optimizations.
- Scale resources automatically based on training job
requirements.
- Track and monitor training experiments and resource utilization
effectively.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning training is computationally intensive and can
become prohibitively expensive when not optimized properly. Using
managed training capabilities allows you to focus on model
development while the infrastructure scales and optimizes
automatically to your needs. Managed training services provide a
range of optimization options from distributed training across
multiple GPUs to cost-saving options through spot instances.
Additionally, these services integrate with monitoring tools to
track resource utilization, model metrics, and training progress
to continually refine your training approach.

For example, when training large language models, you can use
SageMaker AI's distributed training libraries to split the model
across multiple GPUs and instances, reducing training time from
weeks to days while maintaining control over your training costs
through automatic scaling and spot instance usage.

### Implementation steps

- **Use Amazon SageMaker AI managed
training capabilities**. Amazon SageMaker AI
reduces the time and cost to train and tune ML models
without the need to manage infrastructure. With SageMaker AI, you can train and tune ML models using built-in tools to
manage and track training experiments, automatically choose
optimal hyperparameters, debug training jobs, and monitor
the utilization of system resources such as GPUs, CPUs, and
network bandwidth. SageMaker AI can automatically scale
infrastructure up or down based on your training job
requirements, from one GPU to thousands, or from terabytes
to petabytes of storage. SageMaker AI also offers the
highest-performing ML compute infrastructure currently
available-including
[Amazon EC2 P4d instances](https://aws.amazon.com/ec2/instance-types/p4/), which can reduce ML training costs
by up to 60% compared with previous generations. And, since
you pay only for what you use, you can manage your training
costs more effectively.
- **Use Spot Instances for cost
optimization**. Amazon SageMaker AI makes it simple
to train machine learning models using managed Amazon EC2
Spot Instances. Managed Spot training can optimize the cost
of training models up to 90% over On-demand Instances.
SageMaker AI manages the Spot interruptions on your behalf.
You can specify which training jobs use Spot Instances and a
stopping condition that specifies how long SageMaker AI
waits for a job to run using Spot Instances. Metrics and
logs generated during training runs are available in Amazon CloudWatch.
- **Configure optimal data
sources**. Select the appropriate data source for
your training job to optimize performance and cost. Consider
using [Amazon S3](https://aws.amazon.com/s3/) for persistent storage,
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) for high-performance file systems, or
[Amazon EFS](https://aws.amazon.com/efs/) based on your specific training requirements and
dataset characteristics.
- **Implement experiment tracking and
management**. Use
[Amazon SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/) to track training jobs, compare
results, and manage different versions of your models. This
provides visibility into model performance, resource
utilization, and training metrics to optimize future
iterations.
- **Use SageMaker AI HyperPod for
large-scale training**. Use
[SageMaker AI
HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/) to scale and accelerate generative AI model
development across thousands of AI accelerators with
purpose-built infrastructure, automatic checkpoint storage
and recovery, and support for both Slurm and Amazon EKS for
cluster orchestration.
- **For generative AI, optimize large
language model training**. Use
[SageMaker AI
Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-v2.html) to efficiently distribute model
parameters across multiple devices and instances. Consider
using
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for foundation model access and fine-tuning
capabilities to further reduce the computational cost of
training generative AI models from scratch.

## Resources

**Related documents:**

- [SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Train
a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)
- [Model
training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)
- [Distributed
training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)
- [Accelerate
generative AI development with Amazon SageMaker AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)

**Related examples:**

- [SageMaker AI
Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples)
- [SageMaker AI
Training Workshop](https://github.com/aws-samples/amazon-sagemaker-immersion-day)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp06.html*

---

# MLCOST04-BP07 Use distributed training

Accelerate your machine learning model training process by utilizing
distributed computing resources, which can significantly reduce
training time and optimize costs. Amazon SageMaker AI distributed
training capabilities enable efficient processing of large models
and datasets across multiple compute instances.

**Desired outcome:** You achieve
faster training times for your machine learning models by
distributing the workload across multiple instances. You optimize
resource utilization and reduce overall training costs by using
SageMaker AI's managed distributed training capabilities, which
automatically handle infrastructure provisioning and termination
when training completes. This approach allows you to train complex
models that may be too large for a single machine or train standard
models much faster through parallel processing.

**Common anti-patterns:**

- Training large models on a single instance even when they could
benefit from distribution.
- Manually managing distributed training infrastructure rather
than using managed services.
- Keeping training instances running after training is complete.
- Implementing custom distributed training code when built-in
libraries would suffice.

**Benefits of establishing this best
practice:**

- Significantly reduced training time for large models and
datasets.
- Cost optimization through efficient resource utilization.
- Ability to train models that are too large to fit on a single
GPU.
- Automatic infrastructure management with no need to maintain
distributed training clusters.
- Enhanced team productivity by reducing waiting time for model
results.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Distributed training allows you to split your machine learning
workloads across multiple compute instances to accelerate the
training process. This approach is particularly valuable when
working with large models or datasets that would otherwise take
too long to train on a single instance. Amazon SageMaker AI provides
built-in support for distributed training through its specialized
libraries that handle the complexity of distributing workloads
efficiently.

When implementing distributed training, you need to consider the
most appropriate approach based on your model architecture and
data size. Data parallelism works by dividing your dataset across
multiple GPUs, with each GPU having a complete copy of the model.
This approach is ideal for scenarios where your model fits on a
single GPU but training on the full dataset is time-consuming.
Alternatively, model parallelism is designed for situations where
your model is too large to fit on a single GPU. In this case, the
model itself is partitioned across multiple GPUs.

SageMaker AI's distributed training libraries automatically handle
the communication between nodes and optimize the distribution
strategy, making it straightforward to scale your training
workloads without managing the underlying infrastructure.

### Implementation steps

- **Evaluate your workload for
distributed training suitability**. Assess if your
training job would benefit from distribution by considering
factors like model size, dataset size, and current training
times. Ideal candidates are models that take hours or days
to train on a single instance or models too large to fit in
a single GPU's memory.
- **Choose the appropriate distributed
training approach**. Select between data
parallelism and model parallelism based on your specific
needs. Use data parallelism when your model fits on a single
GPU but you want to process data faster. Use model
parallelism when your model is too large to fit on a single
GPU.
- **Utilize Amazon SageMaker AI distributed
training libraries**. Implement distributed
training using
[SageMaker AI's
distributed training libraries](https://aws.amazon.com/sagemaker/distributed-training/), which automatically
handle the complexities of distributing workloads across
multiple instances. These libraries provide optimized
implementations for both data parallelism and model
parallelism strategies.
- **Configure your training
cluster**. Define the number and type of instances
for your training cluster in your SageMaker AI training job
configuration. Consider using GPU-optimized instance types
like P3, P4d, or G4dn based on your model requirements and
budget constraints.
- **Adapt your training script for
distributed processing**. Modify your training code
to work with SageMaker AI's distributed training libraries. For
data parallelism, you'll need to use the SageMaker AI data
parallelism library to distribute data across workers. For
model parallelism, you'll integrate the SageMaker AI model
parallelism library to partition your model across devices.
- **Monitor and optimize training
performance**. Use
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) to monitor your distributed
training jobs, identify bottlenecks, and optimize resource
utilization. Analyze metrics like GPU utilization,
communication overhead, and training throughput to fine-tune
your distributed training configuration.
- **Consider Amazon SageMaker AI HyperPod
for persistent training clusters of foundation
models**. For workloads requiring long-running or
repeated distributed training jobs, use
[Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) to create persistent, managed
clusters that can handle multiple training jobs efficiently
while maintaining cost optimization through automatic
scaling and resource management.
- **Use SageMaker AI HyperPod for
persistent training clusters**. Use
[SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) for workloads requiring long-running or
repeated distributed training jobs, providing persistent,
managed clusters with automatic scaling, checkpoint storage
and recovery, and support for various instance types
including P5e, G6, and Trn2.
- **Use AI-powered code generation for
distributed training implementation**. Use
AI-powered development tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
complex distributed training code, automate infrastructure
setup scripts, and accelerate the implementation of
distributed training workflows.
- **Consider Amazon Bedrock for
fine-tuning foundation models**. For generative AI
applications, consider using
[Amazon
Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html/) for fine-tuning foundation models, model
distillation, or continued pretraining, which provides
optimized distributed training capabilities specifically
designed for large language models.

## Resources

**Related documents:**

- [Run
distributed training with the SageMaker AI distributed data
parallelism library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel.html)
- [SageMaker AI
model parallelism library v2](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-v2.html)
- [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Distributed
Training](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/index.html)
- [Amazon SageMaker AI XGBoost now offers fully distributed GPU
training](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/)

**Related examples:**

- [Distributed
Training](https://github.com/aws/amazon-sagemaker-examples/blob/master/training/distributed_training/index.rst)
- [Distributed
training using Amazon SageMaker AI Distributed Data Parallel
library and debugging using Amazon SageMaker AI Debugger](https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger)
- [SageMaker AI
developer guide on distributed training](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/distributed-training.md#distributed-training-optimize)
- [Distributed
Training Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp07.html*

---

# MLCOST04-BP08 Stop resources when not in use

Stop resources that are not in use to reduce cost. For example,
hosted Jupyter environments used to explore small samples of data
can be stopped when not actively in use. Where practical, commit the
work, stop them, and restart when needed. The same approach can be
used to stop the computing and the data storage services.

**Desired outcome:** You
significantly reduce your ML infrastructure costs by only paying for
resources when they are actively being used. You have automated
systems in place to monitor and shut down idle resources, along with
proper alerts to track spending patterns and avoid unexpected
charges. You maintain the ability to quickly restart resources when
needed while minimizing wasteful spending on idle compute and
storage.

**Common anti-patterns:**

- Leaving development environments running regardless of actual
usage.
- Neglecting to set up automatic shutdown mechanisms for idle
resources.
- Ignoring cost monitoring tools and billing alerts.
- Using persistent storage for temporary data that could be
deleted.

**Benefits of establishing this best
practice:**

- Significant cost savings (up to 75% by running resources only
during business hours compared to running continually).
- Better alignment of spending with actual usage patterns.
- Reduced environmental impact through more efficient resource
consumption.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Optimizing costs is a crucial aspect of running machine learning
workloads in the cloud. ML workloads often require significant
computational resources, but those resources aren't needed
continuously. By implementing automatic shutdown mechanisms for
idle resources, you can achieve substantial cost savings while
maintaining the ability to rapidly resume work when needed.

For ML development environments like SageMaker AI notebooks, the
cost-optimization opportunity is particularly significant since
these environments are typically used intermittently during the
exploration and development phases. By committing code to
repositories regularly and shutting down environments when not in
use, you improve both cost efficiency and version control of your
work.

Additionally, proper monitoring of spending patterns assists you
in identifying optimization opportunities and avoiding unexpected
costs. With AWS tools, you can set up alerts, track resource
utilization, and implement automated responses to idle resources.

### Implementation steps

- **Set up Amazon CloudWatch billing
alarms**. Use
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) to monitor your estimated AWS charges.
When you enable monitoring of estimated charges, these
calculations are sent several times daily to CloudWatch as
metric data. Configure alerts to be notified when your
resource charges exceed predefined thresholds to stay within
budget and quickly identify unexpected spending patterns.
- **Configure Amazon SageMaker AI notebook
lifecycle configurations**. Create
[lifecycle
configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) that include shell scripts to run when
you create or start notebook instances. These scripts can
check for notebook instance activity and automatically shut
down idle instances. This way, you're not paying for compute
resources when they aren't actively processing workloads.
- **Implement Amazon SageMaker AI Studio
idle shutdown**. For
[Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html) environments, install the
auto-shutdown JupyterLab extension either
[manually
or automatically](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension). This extension detects idle Studio
resources and can shut down individual components, including
notebooks, terminals, kernels, applications, and instances
when they're not being used.
- **Use AWS Cost Explorer to identify
optimization opportunities**. Regularly analyze
your ML infrastructure spending patterns using
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to identify resources that might be
consistently underutilized. Look for patterns that indicate
resources could benefit from scheduled shutdowns during
off-hours.
- **Implement instance
scheduling**. Use the
[AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) to create automated schedules for
starting and stopping resources based on your team's working
hours. This is particularly useful for development
environments that are only needed during business hours.
- **Train teams on cost-aware
practices**. Educate your ML teams on the
importance of shutting down resources when not in use and
committing their work regularly. Create a cost-aware culture
where resource efficiency is valued alongside development
productivity.
- **Implement enhanced auto-shutdown
capabilities**. Use improved SageMaker AI Studio
auto-shutdown features with better idle detection and more
granular control over resource shutdown policies to minimize
costs from unused resources.
- **Use Spot Instances for interruptible
workloads**. For ML training jobs that can handle
interruptions, use
[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) to achieve significant cost
savings compared to on-demand pricing. Make sure your
workloads are designed to checkpoint progress and can resume
from interruptions.

## Resources

**Related documents:**

- [Idle
shutdown](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html)
- [Customization
of a SageMaker AI notebook instance using an LCC script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)
- [Instance
Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/)
- [Create
a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/)
- [Cloud
Financial Management with AWS](https://aws.amazon.com/aws-cost-management/)

**Related videos:**

- [Saving
cost on your machine learning training and inference on
AWS](https://www.youtube.com/watch?v=keowy9YfxlcDeploy)
- [Deploy
an ML model for best performance, cost, and prediction
quality](https://www.youtube.com/watch?v=ftCFf57dQQY)

**Related examples:**

- [AWS CloudFormation templates for automated instance
scheduling](https://github.com/aws-solutions/aws-instance-scheduler)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp08.html*

---

# MLCOST04-BP09 Start training with small datasets

Start experimentation with smaller datasets on a small compute
instance or local system. This approach allows you to iterate
quickly at low cost. After the experimentation period, scale up to
train with the full dataset available on a separate compute cluster.
Choose the appropriate storage layer for training data based on the
performance requirements.

**Desired outcome:** You can develop
your machine learning models cost-effectively by starting with small
datasets for rapid iteration and experimentation. When you're
confident in your approach, you scale up to the full dataset on
appropriate compute resources. This progressive scaling methodology
optimizes both development time and infrastructure costs while
maintaining the flexibility to refine your models before committing
to full-scale training.

**Common anti-patterns:**

- Immediately training with the full dataset on large instances,
leading to excessive costs during experimentation.
- Using the same compute resources for both experimentation and
full-scale training.
- Not planning for the transition from small-scale to large-scale
training.

**Benefits of establishing this best
practice:**

- Reduced costs during the experimentation phase.
- Faster iteration cycles for model development.
- More efficient use of compute resources.
- Ability to identify and fix issues early in the development
process.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning development often requires multiple iterations to
achieve optimal results. Using smaller, representative samples of
your dataset during initial experimentation can significantly
reduce costs and increase productivity. This approach lets you
rapidly test various model architectures, hyperparameters, and
preprocessing techniques without the expense and time required to
process the full dataset.

When implementing this approach, check that your smaller dataset
properly represents the characteristics of your full dataset to
avoid developing models that don't generalize well. Once you've
established effective approaches using the smaller dataset, you
can scale up your training to use the complete dataset on
appropriately sized compute resources.

The cloud makes this approach particularly powerful, as you can
scale your compute resources to match your current phase of
development. For example, you might use a notebook instance with
modest resources during experimentation, then transition to
distributed training on a cluster of more powerful instances when
you're ready for full-scale training.

### Implementation steps

- **Create a representative subset of
your data**. Extract a small but representative
sample of your full dataset that maintains the same
distribution of features and classes as your original data.
Aim for 10-20% of your data or a size that can be processed
on your local machine or small instance.
- **Set up SageMaker AI notebook instances
for experimentation**.
[Amazon SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) provide a hosted Jupyter
environment ideal for exploring and experimenting with your
sample dataset. Choose a smaller instance type to keep costs
low during experimentation.
- **Configure notebook lifecycle
management**. Use
[lifecycle
configuration scripts](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples) to automate the setup of your
development environment, including installing necessary
libraries and dependencies when your notebook instance
starts.
- **Develop and iterate on your
model**. Use the notebook environment to build,
train and evaluate your models on the sample data. Take
advantage of this faster iteration cycle to explore
different approaches, hyperparameters, and preprocessing
techniques.
- **Test scaling
considerations**. Before moving to full-scale
training, test your code with slightly larger data samples
to identify scaling issues that might arise when processing
the full dataset.
- **Prepare for distributed
training**. Once your approach is validated with
the sample data, refactor your code as needed to support
distributed training using SageMaker AI's distributed training
capabilities.
- **Scale up compute resources for full
training**. Launch appropriately sized training
instances or clusters for your full-scale training job.
SageMaker AI training jobs allow you to select the instance
type and count that matches your workload requirements.
- **Monitor training metrics and
costs**. Use Amazon CloudWatch to track the
performance and resource utilization of your training jobs
to check that they're running efficiently.

## Resources

**Related documents:**

- [Amazon SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)
- [Amazon SageMaker AI Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab.html)
- [Customization
of a SageMaker AI notebook instance using an LCC script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)
- [Distributed
training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)

**Related examples:**

- [SageMaker AI
Notebook Instance Lifecycle Config Samples](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples)
- [SageMaker AI
Local Mode](https://github.com/aws-samples/amazon-sagemaker-local-mode)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp09.html*

---

# MLCOST04-BP10 Use warm start and checkpointing hyperparameter tuning

When training machine learning models, you can significantly reduce
time and costs by using previous training efforts. This practice
shows how to use warm start and checkpointing techniques in
hyperparameter tuning to accelerate your model development process
and optimize resource utilization.

**Desired outcome:** You can create
more efficient hyperparameter tuning jobs by using knowledge from
previous tuning efforts and saved model states. By implementing warm
start capabilities, you can initialize new tuning jobs with
information from previous runs, avoiding unnecessary repetition.
With checkpointing, you can save intermediate model states during
training, allowing you to resume jobs from the last checkpoint
rather than starting from scratch. These techniques enable you to
accelerate your model development process, reduce computational
costs, and find optimal hyperparameter configurations more
efficiently.

**Common anti-patterns:**

- Starting every hyperparameter tuning job from scratch without
using previous knowledge.
- Not saving model checkpoints during lengthy training jobs,
risking complete loss of progress if interrupted.
- Using unnecessarily wide hyperparameter search ranges when
previous jobs have already identified promising areas.

**Benefits of establishing this best
practice:**

- Lower computational costs through more efficient resource
utilization.
- Accelerated convergence to optimal model configurations.
- Improved resilience to training interruptions through checkpoint
recovery.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hyperparameter tuning is an essential but computationally
intensive part of machine learning model development. Without warm
start capabilities, each tuning job begins with no prior
knowledge, potentially wasting resources by exploring
already-evaluated hyperparameter combinations. Without
checkpointing, an interrupted training job must restart from the
beginning, losing progress.

You can overcome these inefficiencies by implementing warm start
and checkpointing strategies in your ML workflow. Warm start
allows you to use knowledge from previous hyperparameter tuning
jobs, focusing the search on promising areas of the hyperparameter
space. Checkpointing enables you to save model states periodically
during training, providing a recovery point if training is
interrupted.

Amazon SageMaker AI offers built-in support for both warm start and
checkpointing capabilities. For warm start, you can specify one or
more parent tuning jobs whose results inform the new job's
hyperparameter search. SageMaker AI offers two warm start types:
TRANSFER_LEARNING for adapting knowledge to new
datasets and IDENTICAL_DATA_AND_ALGORITHM for
continuing tuning with the same dataset. For checkpointing, you
can configure your training jobs to periodically save model states
to Amazon S3, which can be used to resume training if needed.

### Implementation steps

- **Configure warm start for
hyperparameter tuning jobs**. Set up a new
hyperparameter tuning job that builds upon the knowledge
gained from previous tuning jobs. In Amazon SageMaker AI, you
can configure this by specifying one or more parent tuning
jobs and selecting an appropriate warm start type. This
approach is particularly effective when you want to refine
hyperparameter search after initial exploration or adapt a
model to a similar dataset.
- **Select appropriate parent jobs for
warm start**. Choose parent jobs that are relevant
to your current tuning objective. The best parent jobs are
those that used similar datasets, algorithms, or
optimization objectives. In SageMaker AI, you can specify up to
five parent jobs when configuring a warm start tuning job.
- **Choose the right warm start
type**. Select
IDENTICAL_DATA_AND_ALGORITHM when
continuing tuning with the same dataset and algorithm, or
TRANSFER_LEARNING when adapting knowledge
to a new but related dataset or problem. The warm start type
determines how SageMaker AI will use information from the
parent jobs.
- **Configure checkpointing for training
jobs**. Enable checkpointing in your training
script by saving model states at regular intervals. In
SageMaker AI, specify a checkpoint S3 location where these
model states will be stored. This allows you to resume
training from the last saved checkpoint if a job is
interrupted or if you want to extend training later.
- **Implement checkpoint saving in your
training code**. Add callback functions in your ML
framework (such as TensorFlow, PyTorch, or MXNet) to
periodically save model states during training. These
frameworks typically provide built-in checkpoint
functionality that you can configure with minimal code
changes.
- **Set up checkpoint recovery
mechanisms**. Configure your training jobs to check
for existing checkpoints at startup and resume from the
latest checkpoint if available. In SageMaker AI, you can
specify the checkpoint configuration when creating a
training job, including the S3 location where checkpoints
are stored.
- **Optimize hyperparameter search
ranges based on previous results**. When using warm
start, refine your hyperparameter search ranges based on
promising values identified in parent jobs. Narrowing search
ranges around previously successful values can significantly
improve tuning efficiency.
- **Run parallel hyperparameter tuning
jobs strategically**. Use warm start to distribute
the hyperparameter tuning workload across multiple jobs that
can share knowledge. This approach is particularly effective
for exploring large hyperparameter spaces efficiently.
- **Monitor and evaluate warm start
efficiency**. Track the performance and efficiency
gains from warm start by comparing with cold-start
approaches. This analysis refines your warm start strategy
for future jobs.
- **Use enhanced hyperparameter tuning
capabilities**. Use improved SageMaker AI
hyperparameter tuning with better algorithms and support for
multi-objective optimization to find optimal configurations
more efficiently.
- **Use generative AI for hyperparameter
selection**. Use large language models to suggest
promising hyperparameter ranges based on model architecture
and dataset characteristics. Generative AI can identify
sensible starting points for hyperparameter tuning jobs,
especially for new model architectures.

## Resources

**Related documents:**

- [Run
a Warm Start Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html)
- [Checkpoints
in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html)
- [Automatic
model tuning in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [HyperparameterTuner](https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html)

**Related examples:**

- [Automatic
Model Tuning: Warm Starting Tuning Jobs](https://github.com/aws/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/image_classification_warmstart/hpo_image_classification_warmstart.ipynb)
- [Hyperparameter
Optimization with Checkpointing Example](https://github.com/aws/amazon-sagemaker-examples/tree/master/hyperparameter_tuning)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp10.html*

---

# MLCOST04-BP11 Use hyperparameter optimization technologies

Optimize your machine learning models through automatic
hyperparameter tuning to find the optimal model configuration with
minimal manual effort, reducing the time and resources needed to
achieve peak model performance.

**Desired outcome:** You achieve
better performing machine learning models by using automatic
hyperparameter optimization technologies that run multiple training
jobs in parallel. You can efficiently explore a wide range of
hyperparameter combinations to find the optimal configuration that
maximizes model performance according to your specified metrics,
ultimately delivering better business results while reducing the
time and resources spent on manual tuning.

**Common anti-patterns:**

- Manually tuning hyperparameters through trial and error.
- Using a narrow range of hyperparameter values that don't
adequately explore the solution space.
- Selecting arbitrary hyperparameter values without considering
the specific requirements of your business problem.
- Running one training job at a time instead of using parallel
capabilities.

**Benefits of establishing this best
practice:**

- Reduced time to develop high-performing machine learning models.
- Lower computational costs by efficiently exploring the
hyperparameter space.
- Consistent and repeatable approach to model optimization.
- Ability to scale hyperparameter tuning efforts across multiple
algorithms.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

*Hyperparameter optimization (HPO)* is a
critical aspect of developing effective machine learning models.
Unlike model parameters that are learned during training,
hyperparameters are configuration variables that govern the
training process itself and significantly impact model
performance. Finding the optimal combination of hyperparameters
manually is time-consuming and inefficient.

By implementing automatic hyperparameter tuning, you can
systematically explore the hyperparameter space and identify the
configuration that maximizes model performance. SageMaker AI's
automatic model tuning service employs techniques like Bayesian
optimization to intelligently search through the hyperparameter
space, focusing computational resources on the most promising
regions and accelerating the discovery of the optimal
configuration.

When implementing hyperparameter optimization, you should define
appropriate search spaces for your hyperparameters based on domain
knowledge and previous experiments. You also need to select
relevant evaluation metrics that align with your business
objectives. For classification problems, this might include
accuracy, F1 score, or AUC-ROC, while for regression problems, it
could be mean squared error or mean absolute error.

### Implementation steps

- **Identify key hyperparameters for
your model**. Begin by determining which
hyperparameters have the greatest impact on your model's
performance. For neural networks, this might include
learning rate, batch size, and network architecture
parameters. For tree-based models, this could include tree
depth, number of trees, and minimum samples per leaf.
- **Define appropriate hyperparameter
ranges**. Establish meaningful ranges for each
hyperparameter based on domain knowledge and best practices
for your chosen algorithm. Use logarithmic scales for
parameters that span multiple orders of magnitude (like
learning rate) for efficient exploration.
- **Select relevant evaluation
metrics**. Choose metrics that align with your
business requirements and the problem you're solving. Check
that these metrics provide a meaningful assessment of model
performance in the context of your specific application.
- **Configure SageMaker AI automatic model
tuning**. Create a hyperparameter tuning job using
the
[SageMaker AI
Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html) or the SageMaker AI console. Specify the
algorithm or framework you're using, the hyperparameter
ranges, and the evaluation metric to optimize.
- **Implement early stopping for
efficiency**. Enable early stopping features to
automatically terminate poorly performing training jobs,
saving computational resources. SageMaker AI can monitor the
evaluation metric during training and stop jobs that are
unlikely to produce competitive models.
- **Use warm start for incremental
tuning**. Use the warm start feature to accelerate
new hyperparameter tuning jobs by using information from
previous tuning jobs, reducing the time and resources needed
to find optimal configurations.
- **Implement parallel training
jobs**. Configure SageMaker AI to run multiple
training jobs concurrently to explore different
hyperparameter combinations simultaneously, dramatically
reducing the time required to find optimal values.
- **Analyze tuning job
results**. Review the performance of different
hyperparameter combinations to understand how each parameter
affects model performance. Use this information to refine
your hyperparameter ranges for future tuning jobs.
- **Select the best model for
deployment**. After the tuning job completes,
identify the best-performing model based on your evaluation
metric and deploy it using SageMaker AI's deployment
capabilities.
- **Use no-code hyperparameter
optimization**. Use
[SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) with enhanced capabilities for business users
to perform hyperparameter optimization through natural
language interfaces without requiring deep technical
expertise.
- **Document hyperparameter
configurations**. Maintain comprehensive
documentation of hyperparameter configurations, tuning
strategies, and results to facilitate knowledge sharing and
reproducibility.

## Resources

**Related documents:**

- [Automatic
model tuning with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [Stop
Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html)
- [Best
Practices for Hyperparameter Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html)
- [Create
a Hyperparameter Optimization Tuning Job for One or More
Algorithms (Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.html)
- [Run
a Warm Start Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html)

**Related examples:**

- [SageMaker AI
examples - hyperparameter tuning](https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp11.html*

---

# MLCOST04-BP12 Set up a budget and use resource tagging to track costs

Setting up budgets and implementing resource tagging for machine
learning workloads provides clear visibility into your ML-related
expenses and optimizes costs across your organization. By tracking
costs effectively, you can make data-driven decisions about resource
allocation and identify opportunities for cost optimization.

**Desired outcome:** You gain
complete visibility into your machine learning costs across
development, training, and production environments. You can track
expenses by project, business unit, or environment, allowing for
accurate cost allocation and forecasting. Through tagging and
budgeting tools, you can proactively manage your ML spending,
receive alerts before exceeding budgeted amounts, and make informed
decisions about resource provisioning and termination.

**Common anti-patterns:**

- Running ML workloads without cost monitoring mechanisms in
place.
- Using generic cost tracking that doesn't differentiate between
ML projects or environments.
- Failing to tag ML resources consistently, making cost allocation
difficult.
- Ignoring budget alerts or failing to take action when exceeding
thresholds.

**Benefits of establishing this best
practice:**

- Clear visibility into where ML spending occurs across your
organization.
- Ability to accurately allocate costs to specific projects or
business units.
- Early warning through alerts when costs exceed or are forecasted
to exceed budgeted amounts.
- Improved governance and financial accountability for ML
initiatives.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Cost management is a critical aspect of running machine learning
workloads in the cloud. Without proper cost tracking and budget
controls, ML expenses can quickly escalate due to
compute-intensive training jobs, large storage requirements for
datasets, and continuous inference endpoints. By implementing
comprehensive budgeting and tagging strategies, you gain
visibility and control over these costs.

AWS provides several tools that work together to track, analyze,
and optimize your ML costs. AWS Budgets allows you to set custom
budgets for your SageMaker AI resources, while AWS Cost Explorer
provides visualization and analysis capabilities to understand
spending patterns. Resource tagging serves as the foundation for
detailed cost tracking, enabling you to categorize expenses by
project, team, environment, or other dimension important to your
organization.

For example, you might tag resources related to a fraud detection
model with a Project tag value of
FraudDetection and an
Environment tag value of
Production. This allows you to track the total
cost of this specific ML use case across its components, from
development notebooks to training jobs to deployment endpoints.

### Implementation steps

- **Set up AWS Budgets for ML cost
tracking**. Create customized budgets in AWS
Budgets to monitor your Amazon SageMaker AI costs across
development, training, and hosting. Configure the budget to
track specific services (such as SageMaker AI) or specific
tagged resources. Set thresholds for actual costs and
forecasted costs to receive notifications before you exceed
your budget. This gives you time to make adjustments to your
resource usage if needed. Access your budgets through the
[AWS Budgets console](https://aws.amazon.com/aws-cost-management/aws-budgets/) to track progress and make
adjustments as necessary.
- **Implement a tagging strategy for ML
resources**. Develop a consistent tagging strategy
for all your ML resources. Define mandatory tags such as
Project, BusinessUnit, Environment (dev/test/prod), and
Owner. Document your tagging standards and verify that team
members understand and follow these standards. Apply these
tags to relevant resources, including
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) notebook instances, training jobs, models,
endpoints, and related resources like
[Amazon S3](https://aws.amazon.com/s3/) buckets for dataset storage.
- **Activate cost allocation
tags**. After implementing your tagging strategy,
activate your tags as cost allocation tags in the AWS Billing and Cost Management console. Note that it may take up to 24 hours for
newly activated tags to appear in your cost management
tools. Once activated, you can use your tags to filter and
group costs in AWS Cost Explorer and other cost reporting
tools.
- **Configure detailed cost analysis
using AWS Cost Explorer**. Use
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to visualize and analyze your ML costs
over time. Create custom reports that filter costs by
specific tags (like Project or Environment) or by specific
services like SageMaker AI. Set up regular reports to track
spending trends, identify cost spikes, and understand usage
patterns. Use the insights gained to optimize your resource
allocation and scheduling for ML workloads.
- **Create cost anomaly
detection**. Set up
[AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to automatically identify
unusual spending patterns in your ML workloads. Configure
alerts to notify relevant stakeholders when anomalies are
detected. This assists you in quickly identifying and
addressing unexpected cost increases, which can happen with
ML workloads due to extended training times or inefficient
resource usage.
- **Establish cost governance
processes**. Create clear processes for reviewing
costs, responding to budget alerts, and making cost
optimization decisions. Assign responsibility for cost
monitoring to specific individuals or teams. Conduct regular
cost reviews with stakeholders to discuss spending trends,
identify optimization opportunities, and align ML resource
usage with business priorities. Document cost-saving actions
taken and their impact on the overall budget.
- **Optimize ML resources based on cost
data**. Use the cost insights gained from your
tagging and budgeting tools to optimize ML resource usage.
Identify underutilized notebook instances that can be
stopped when not in use. Select appropriate instance types
based on workload requirements. Consider using
[Amazon SageMaker AI Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) to reduce training
costs by up to 90%. Implement auto-scaling for inference
endpoints to match capacity with demand.

## Resources

**Related documents:**

- [Managing
your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Getting
started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [Cost
Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/)
- [AWS Cloud Financial Management](https://aws.amazon.com/aws-cost-management/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp12.html*

---

# MLCOST04-BP13 Enable data and compute proximity

Positioning data and compute resources in the same AWS Region
reduces data transfer costs and improves processing speeds for
machine learning workloads. By minimizing the physical distance
between data storage and compute resources, you can significantly
decrease latency and avoid cross-region data transfer fees.

**Desired outcome:** You achieve
cost-efficient and high-performance machine learning operations by
placing your data and compute resources in the same AWS Region. You
experience faster training times, reduced latency, and avoid
unnecessary data transfer costs that can significantly impact your
ML project budgets.

**Common anti-patterns:**

- Storing data in one Region and running compute resources in
another Region.
- Repeatedly transferring large datasets across Regions for
training or inference.
- Failing to consider the impact of data transfer costs on overall
ML project budgets.

**Benefits of establishing this best
practice:**

- Decreased latency for data access during model training and
inference.
- Improved overall machine learning workflow performance.
- Simplified management of data compliance and sovereignty
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data transfer costs between AWS Regions can significantly impact
your machine learning project's budget, especially when working
with large datasets that are repeatedly accessed during model
training. By keeping your compute resources in the same Region as
your data storage, you minimize these costs and improve
performance.

When planning your machine learning infrastructure on AWS,
consider data locality as a primary design principle. For example,
if your organization stores datasets in Amazon S3 buckets in the
US West (Oregon) Region, you should provision EC2 instances,
SageMaker AI notebooks, or other ML compute resources in that same
Region.

This principle applies to various machine learning scenarios,
including model training, data preprocessing, and inference. Even
though AWS provides high-speed network connections between
Regions, the laws of physics still impose latency limitations, and
cross-Region data transfers incur additional costs that can be
avoided.

### Implementation steps

- **Identify data storage
locations**. Determine where your primary data is
stored on AWS. Check which Regions contain your Amazon S3
buckets, Amazon EFS file systems, or other storage services
holding your training data. Use the AWS Management Console,
AWS CLI, or infrastructure as code tools to inventory your
data storage resources across Regions.
- **Audit compute resource
placement**. Review your current machine learning
compute resources, including Amazon EC2 instances, Amazon SageMaker AI notebooks, and training jobs. Verify if they are
in the same Regions as your data sources. Use AWS Cost Explorer and AWS Trusted Advisor to identify cross-Region
data transfer costs that may indicate misaligned resources.
- **Consolidate resources by
Region**. When creating new compute resources for
machine learning workloads, consistently provision them in
the same Region as your data. For example, if using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), create your notebook instances, training
jobs, and endpoints in the Region where your training data
is stored in Amazon S3.
- **Use Regional data transfer
analysis**. Review your AWS billing information to
identify and quantify cross-Region data transfer costs. The
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) service can assist you in analyzing
data transfer costs between AWS services and across Regions.
Set up cost allocation tags to track expenses related to
machine learning projects specifically.
- **Consider data replication for
specific use cases**. In scenarios requiring
multi-Region deployments for high availability or disaster
recovery, implement a data replication strategy to maintain
copies of datasets in each Region where compute resources
exist. Services like
[Amazon S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) can automate this process
while managing costs.
- **Leverage edge computing for
distributed ML workloads**. When working with data
that exists at the edge of the network, consider using
[AWS Outposts](https://aws.amazon.com/outposts/),
[AWS Wavelength](https://aws.amazon.com/wavelength/), or
[AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to bring compute resources closer to your
data sources, especially for applications requiring
low-latency inference.
- **Implement data caching
strategies**. For frequently accessed data,
implement caching solutions like
[Amazon ElastiCache](https://aws.amazon.com/elasticache/) or
[Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) in the same Region as your
compute resources to further reduce latency and data
transfer costs.

## Resources

**Related documents:**

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Replicating
objects within and across Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [AWS Data Transfer Pricing](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer)
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [AWS Outposts](https://aws.amazon.com/outposts/)
- [Regions
and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp13.html*

---

# MLCOST04-BP14 Select optimal algorithms

Selecting optimal algorithms for machine learning (ML) workloads is
crucial for balancing cost efficiency and performance. By
identifying appropriate ML paradigms and carefully evaluating
algorithmic choices, you can optimize both technical performance and
business outcomes while managing costs.

**Desired outcome:** You are able to
identify the most suitable ML algorithm for your specific use case
that balances accuracy, explainability, computational requirements,
and cost efficiency. You can conduct effective trade-off analyses
between different approaches and use AWS services to optimize
algorithm selection, training, and deployment.

**Common anti-patterns:**

- Using complex deep learning solutions without first exploring
simpler algorithms.
- Ignoring the explainability requirements of the business use
case.
- Failing to consider data constraints when selecting algorithms.
- Not evaluating computational and maintenance costs alongside
accuracy metrics.

**Benefits of establishing this best
practice:**

- Reduced computational costs by using algorithms appropriate for
the specific problem.
- Improved model performance through systematic comparison of
algorithm options.
- Enhanced model explainability when required by business
stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Selecting the optimal algorithm requires understanding your
specific ML problem type and the business constraints around it.
Begin by categorizing your problem into basic ML paradigms:
supervised learning (for labeled data), unsupervised learning (for
unlabeled data), or reinforcement learning (for sequential
decision problems). Consider what matters most for your use case,
whether it's prediction accuracy, model explainability, inference
speed, or a balance of these factors.

Algorithm selection significantly impacts both the performance and
cost efficiency of your ML solutions. A computationally expensive
algorithm might deliver marginally better accuracy but at
substantially higher operational costs. Similarly, a complex but
highly accurate algorithm might sacrifice the explainability
needed for regulatory adherence or business transparency. Finding
the right balance requires systematic experimentation and
evaluation against your business requirements.

AWS provides various services test, compare, and optimize
algorithms, allowing you to make data-driven decisions about which
approach delivers the best value for your specific use case.

### Implementation steps

- **Define your machine learning problem
type**. Categorize your problem as supervised
learning (classification, regression), unsupervised learning
(clustering, dimensionality reduction), or reinforcement
learning. This initial classification narrows down the
appropriate algorithms to consider.
- **Determine business requirements and
constraints**. Document specific accuracy targets,
explainability needs, inference time requirements, and
budget constraints. These requirements will serve as
criteria for evaluating algorithm options.
- **Start with simple algorithms
first**. Begin experimentation with simpler
algorithms like linear or logistic regression, decision
trees, or k-means clustering before moving to more complex
approaches. These algorithms are computationally efficient,
simpler to interpret, and establish important baselines for
performance comparison.
- **Conduct structured
experimentation**. Use
[Amazon SageMaker AI Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html) to track different algorithm
trials, hyperparameter configurations, and their results.
This creates reproducibility and facilitates comparison
between approaches.
- **Perform comprehensive trade-off
analysis**. When comparing algorithms, consider
multiple dimensions beyond accuracy:

Data requirements (amount needed for training)
- Computational resources required for training and
inference
- Model explainability and interpretability
- Deployment complexity and operational overhead
- Long-term maintenance costs

- **Use AWS optimized algorithms and
frameworks**. Use
[Amazon SageMaker AI built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) that are optimized for
performance and cost-efficiency on AWS infrastructure. AWS
also provides optimized versions of popular frameworks like
TensorFlow, PyTorch, and MXNet that include performance
enhancements for training across
[Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance families.
- **Consider automated ML
approaches**. For exploratory projects or when
seeking optimal performance with minimal manual tuning, use
SageMaker AI Canvas for rapid algorithm prototyping with the
ability to export generated code to notebooks for further
customization.
- **Explore pre-trained
models**. Search AWS Marketplace for pre-trained
models that can accelerate development through transfer
learning or direct deployment. Pre-trained models can
significantly reduce computational costs and development
time.
- **Implement continuous
evaluation**. As new algorithms and model versions
emerge, periodically reassess whether your chosen approach
remains optimal. Business requirements and available
technologies evolve over time.
- **Document algorithm selection
rationale**. Create clear documentation explaining
why specific algorithms were selected, what trade-offs were
accepted, and how these decisions align with business
requirements.
- **For generative AI projects, consider
foundation models from
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for natural language processing, image
generation, and other tasks where these models can provide
state-of-the-art performance with lower development
costs.** Use techniques like prompt engineering and
fine-tuning to adapt foundation models to your specific
business needs while avoiding the computational expense of
training from scratch.

## Resources

**Related documents:**

- [Built-in
algorithms and pretrained models in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html#mlflow-tracking)
- [How
custom models work](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-build-model.html)
- [Types
of Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html)
- [SageMaker AI
JumpStart pretrained Models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp14.html*

---
