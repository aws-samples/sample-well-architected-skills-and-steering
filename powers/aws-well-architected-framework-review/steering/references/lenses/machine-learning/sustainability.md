# Sustainability

**Pillar**: Sustainability  
**Questions**: 6

---

# MLSUS01 — Business goal identification

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MLSUS01-BP01 Define the overall environmental impact or benefit

Measure your workload's impact and its contribution to the overall
sustainability goals of the organization. Understand the
environmental footprint of machine learning systems to make informed
decisions about resource allocation and optimization.

**Desired outcome:** You gain a clear
understanding of how your ML workload impacts your organization's
sustainability objectives, including energy consumption, carbon
emissions, and resource utilization. You have established specific
sustainability objectives and success criteria to measure against,
which assists you when optimizing your ML workloads and
demonstrating their environmental value proposition in relation to
their impact.

**Common anti-patterns:**

- Focusing solely on model accuracy without considering
environmental trade-offs.
- Implementing ML systems without measuring their carbon
footprint.
- Overprovisioning resources for ML workloads.
- Unnecessarily retraining models when not required.

**Benefits of establishing this best
practice:**

- Improved alignment between ML initiatives and organizational
sustainability goals.
- Enhanced ability to meet regulatory and reporting requirements.
- Transparent assessment of the sustainability impact of ML
projects.
- Identification of opportunities to optimize ML systems for lower
environmental impact.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Understanding the environmental impact of your ML workloads is
essential for sustainable AI development. ML operations can be
resource-intensive, requiring substantial computing power for
training and inference, which translates to energy consumption and
carbon emissions. By measuring and tracking this impact, you can
make informed decisions about architecture choices, region
selection, and optimization strategies.

The cloud provides significant advantages for sustainable ML
development through its economies of scale and renewable energy
investments. By leveraging AWS's efficiency, you can reduce your
carbon footprint compared to on-premises alternatives. However,
you still need to make conscious decisions about how you design,
deploy, and operate your ML workloads.

Consider the full lifecycle of your ML system, from data
collection and processing to model training, deployment, and
ongoing operations. Each stage has different resource requirements
and environmental impacts. For example, training large models is
typically more computationally intensive than inference, but if
your model serves millions of predictions daily, the inference
stage might have a larger cumulative impact over time.

### Implementation steps

- **Establish sustainability objectives
for ML workloads**. Begin by defining specific
sustainability goals for your ML projects that align with
your organization's broader environmental commitments.
Determine what metrics you'll track (for example, carbon
emissions per training run or energy efficiency per
inference) and set concrete targets for improvement.
- **Assess the environmental impact of
data processing**. Evaluate how much data you're
storing and processing for your ML workloads. Consider
implementing data lifecycle management using
[Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) policies to automatically transition
infrequently accessed data to more efficient storage classes
or archive data that's no longer needed for active training.
- **Measure the impact of model
training**. Calculate the computational resources
and associated carbon emissions of your model training
processes using tools like the
[AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/). Consider factors such
as instance types, training duration, and region selection.
Track these metrics over time to identify trends and
opportunities for improvement.
- **Optimize model training frequency
and approach**. Determine how often retraining is
truly necessary based on model drift monitoring. Implement
incremental training where possible using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to update existing models with new data
rather than retraining from scratch. Use techniques like
transfer learning to leverage pre-trained models and reduce
computational requirements.
- **Assess inference
efficiency**. Evaluate the environmental impact of
your deployed models in production. Consider techniques like
model compression, quantization, and distillation to reduce
the computational requirements of inference while
maintaining acceptable accuracy. Use
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to automatically optimize models for
specific deployment targets.
- **Calculate the net sustainability
value**. Compare the environmental impact of your
ML workload with its benefits, including the sustainability
improvements it enables. For example, if your ML system
optimizes energy usage in manufacturing processes, calculate
the net reduction in emissions to demonstrate its overall
positive impact.
- **Implement ongoing monitoring and
reporting**. Establish a regular cadence for
reviewing sustainability metrics and reporting on progress
toward your goals. Use
[AWS CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor resource utilization and create
dashboards to track your sustainability KPIs over time.
- **For GenAI workloads, consider your
model customization strategy**. When implementing
generative AI solutions, evaluate whether fine-tuning
existing foundation models like
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) models is more environmentally efficient than
training custom models from scratch. Consider prompt
engineering and retrieval-augmented generation (RAG)
approaches that can achieve business goals with lower
computational intensity than full model training.

## Resources

**Related documents:**

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Sustainability Data Initiative](https://sustainability.aboutamazon.com/about/the-climate-pledge)
- [AWS Well-Architected Framework: Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [Corporate
Climate Action - Science Based Targets initiative
(SBTi)](https://sciencebasedtargets.org/)
- [Greenhouse Gas
Protocol](https://ghgprotocol.org/)
- [Optimize
AI/ML workloads for sustainability: Part 1, identify business
goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus01-bp01.html*

---

# MLSUS02 — ML problem framing

**Pillar**: Sustainability  
**Best Practices**: 2

---

# MLSUS02-BP01 Consider AI services and pre-trained models

Using AI services and pre-trained models can significantly reduce
the resources needed for machine learning workloads, enabling you to
quickly implement AI capabilities without developing custom models
from scratch.

**Desired outcome:** You identify
opportunities to use managed AI services or pre-trained models
instead of building custom models, reducing the environmental impact
of training and deploying ML solutions while accelerating time to
market. By using existing capabilities through APIs or fine-tuning
pre-trained models, you minimize computational resources required
for data preparation, model training, and deployment.

**Common anti-patterns:**

- Building custom models from scratch when suitable managed
services already exist.
- Collecting and processing large datasets unnecessarily when
pre-trained models could be utilized.
- Ignoring transfer learning opportunities that could reduce
training time and computational resources.
- Overlooking model optimization techniques that could reduce
inference resource requirements.

**Benefits of establishing this best
practice:**

- Reduced environmental impact through decreased computational
resource usage.
- Lower operational costs for ML development and deployment.
- Faster time-to-market for ML-powered solutions.
- Access to state-of-the-art models without specialized ML
expertise.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning solutions, evaluate whether you
truly need to build a custom model or if existing services and
pre-trained models can meet your requirements. Many common use
cases like image recognition, natural language processing, or
recommendation systems can use pre-built capabilities available
through APIs. These managed services handle the underlying
infrastructure, data processing, and model maintenance, reducing
both environmental impact and operational overhead.

If fully managed services don't meet your specific requirements,
consider starting with pre-trained models that you can fine-tune
with your data. This approach, known as transfer learning, allows
you to benefit from models that have already undergone
resource-intensive training on large datasets. By fine-tuning, you
can achieve similar or better performance than training from
scratch while using significantly fewer computational resources.

For example, instead of training a computer vision model from
scratch, you could use a pre-trained image recognition model from
Amazon Rekognition or fine-tune a model available through
SageMaker AI JumpStart with your specific images. This approach
reduces the carbon footprint associated with extensive model
training while delivering high-quality results.

### Implementation steps

- **Assess your ML use case
requirements**. Before developing an ML solution,
clearly define your requirements and success criteria.
Understand the specific problem you're trying to solve, the
data you have available, and the performance metrics that
matter for your application.
- **Explore AWS AI services**.
[AWS AI services](https://aws.amazon.com/machine-learning/ai-services/) provide ready-to-use capabilities through
APIs for common ML tasks. These services include
[Amazon Rekognition](https://aws.amazon.com/rekognition/) for image and video analysis,
[Amazon Comprehend](https://aws.amazon.com/comprehend/) for natural language processing,
[Amazon
Forecast](https://aws.amazon.com/forecast/) for time-series forecasting, and
[Amazon Personalize](https://aws.amazon.com/personalize/) for personalization and recommendations.
- **Evaluate foundation models in Amazon
Bedrock**.
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) provides serverless access to leading
foundation models from AI companies like Anthropic, Cohere,
AI21 Labs, and Amazon's own Nova models through a single
API. These models can handle tasks like text generation,
summarization, chatbots, and content creation without
requiring model training.
- **Explore pre-trained models from AWS Marketplace**.
[AWS Marketplace](https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1) offers over 1,400 ML-related assets that
you can subscribe to, including pre-trained models for
various industry-specific use cases that can be deployed
with minimal configuration.
- **Leverage SageMaker AI
JumpStart**.
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) provides pre-trained, open-source models
for a wide range of problem types to get started with
machine learning. You can incrementally train and fine-tune
these models before deployment, reducing the computational
resources needed compared to training from scratch.
- **Consider Hugging Face
models**.
[Hugging
Face with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html) enables you to use
thousands of pre-trained transformer models for NLP,
computer vision, and audio tasks. These models can be
fine-tuned with your specific data to achieve high-quality
results with minimal training.
- **Implement efficient fine-tuning
techniques**. When customizing pre-trained models,
use efficient fine-tuning methods like parameter-efficient
fine-tuning (PEFT), low-rank adaptation (LoRA), or
quantization to minimize computational resources while
maintaining performance.
- **Monitor resource usage and
optimize**. After deploying your solution,
continuously monitor its resource consumption and
performance. Look for opportunities to optimize through
model compression, quantization, or pruning to further
reduce computational requirements.
- **Leverage expanded pre-trained model
libraries**. Use the expanded
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) catalog which now includes broader
selection of pre-trained models and industry-specific
solutions, reducing the need for custom model development
and associated computational resources.
- **For generative AI workloads,
implement retrieval-augmented generation (RAG)**.
For generative AI applications requiring domain-specific
knowledge, consider using
[retrieval-augmented
generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/) with SageMaker AI JumpStart foundation models
instead of fine-tuning large models, which can significantly
reduce computational resources while improving accuracy.

## Resources

**Related documents:**

- [AWS AI Services](https://aws.amazon.com/machine-learning/ai-services/)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Choose
the best data source for your Amazon SageMaker AI training
job](https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/)
- [Pre-trained
machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models)
- [Resources
for using Hugging Face with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html)
- [Optimize
AI/ML workloads for sustainability: Part 2, model
development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus02-bp01.html*

---

# MLSUS02-BP02 Select sustainable Regions

Choose the Regions where you implement your workloads based on both
your business requirements and sustainability goals.

**Desired outcome:** You select AWS Regions that align with your organizational sustainability
objectives while meeting your business requirements. By choosing
Regions with renewable energy sources and lower carbon intensity,
you reduce the environmental impact of your machine learning
workloads while maintaining optimal performance for your business
needs.

**Common anti-patterns:**

- Selecting Regions based solely on proximity without considering
environmental impact.
- Ignoring renewable energy availability when deploying machine
learning workloads.
- Deploying workloads across multiple Regions without considering
their carbon footprints.

**Benefits of establishing this best
practice:**

- Alignment with organizational sustainability goals and ESG
initiatives.
- Enhanced reputation as an environmentally responsible
organization.
- Potential cost savings through efficient Region selection.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When deploying your machine learning workloads, Region selection
plays a crucial role in meeting both your operational requirements
and sustainability goals. While factors such as latency, data
residency, and service availability remain important,
incorporating sustainability considerations into your Region
selection process can minimize your environmental impact. AWS is
continuously expanding its renewable energy projects globally,
making it increasingly possible to host your workloads in Regions
powered by sustainable energy sources.

The cloud offers significant sustainability advantages compared to
on-premises deployments due to higher utilization rates, more
energy-efficient infrastructure, and AWS' commitment to renewable
energy. By selecting Regions thoughtfully, you can further enhance
these sustainability benefits while still meeting your business
needs.

### Implementation steps

- **Understand your business
requirements first**. Identify the non-negotiable
requirements for your workload, including data sovereignty
regulations, compliance-aligned needs, latency requirements,
and service availability in specific Regions. Create a
shortlist of Regions that meet these baseline requirements.
- **Research AWS renewable energy
projects**. Use the
[Amazon
Around the Globe](https://sustainability.aboutamazon.com/about/around-the-globe?energyType=true) resource to identify Regions that
are near Amazon renewable energy projects. AWS achieved
powering its operations with
[100%
renewable energy](https://www.aboutamazon.com/news/sustainability/amazon-renewable-energy-goal) in 2023, seven years ahead of their
original 2030 commitment.
- **Consider the grid's carbon
intensity**. Look for Regions where the electrical
grid has lower published carbon intensity. This information
may be available through regional utility reports or
sustainability documentation. Lower carbon intensity means
reduced emissions even for non-renewable energy sources.
- **Evaluate the trade-offs**.
When selecting Regions, consider potential trade-offs
between sustainability goals and business requirements such
as latency or availability. In some cases, minor performance
trade-offs may be acceptable to achieve significant
sustainability improvements.
- **Monitor sustainability
metrics**. After deployment, track relevant
sustainability metrics to verify that your Region selection
is delivering the expected environmental benefits. Consider
implementing dashboards with key performance indicators
(KPIs) for sustainability tracking.
- **Review and adjust
periodically**. As AWS adds more renewable energy
projects and as your business requirements evolve,
periodically reassess your Region selections to continually
align with your sustainability goals.

## Resources

**Related documents:**

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Delivering
on net-zero carbon by 2040](https://sustainability.aboutamazon.com/about/around-the-globe)
- [Climate
solutions](https://sustainability.aboutamazon.com/about/the-climate-pledge)
- [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [How
to select a Region for your workload based on sustainability
goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus02-bp02.html*

---

# MLSUS03 — Data processing

**Pillar**: Sustainability  
**Best Practices**: 3

---

# MLSUS03-BP01 Minimize idle resources

Minimize your environmental impact by efficiently managing compute
resources in your ML data pipeline. Use serverless architectures
that provision resources only when needed, reducing energy
consumption and carbon footprint.

**Desired outcome:** You implement a
serverless, event-driven architecture for your ML data pipelines
that only provisions resources when work needs to be done. This
approach reduces idle resources, optimizes utilization of computing
infrastructure, and reduces your organization's environmental impact
while maintaining performance and scalability.

**Common anti-patterns:**

- Provisioning compute instances that run 24/7 regardless of
workload requirements.
- Overprovisioning resources rather than scaling dynamically.
- Using traditional batch processing with fixed schedules instead
of event-driven approaches.
- Failing to monitor and optimize resource utilization metrics.

**Benefits of establishing this best
practice:**

- Lower carbon footprint and energy consumption.
- Improved resource efficiency across your ML pipeline.
- Automatic scaling to match workload demands.
- Simplified maintenance with managed services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopting a serverless architecture for your ML data pipelines
significantly reduces idle resources by allocating compute power
only when needed. This approach uses AWS managed services that
automatically scale based on workload, avoiding the need to
maintain an always-on infrastructure. When you design your data
pipeline using serverless technologies like AWS Glue and AWS Step Functions, you not only optimize resource utilization but also
distribute the sustainability impact across the tenants of those
services, reducing your individual environmental contribution.

The key principle is to transition from a static infrastructure
model to an event-driven approach where resources are provisioned
in response to triggers. This verifies that compute resources are
only active during actual processing tasks rather than sitting
idle waiting for work. AWS managed services handle the underlying
infrastructure optimization, allowing you to focus on your ML
workloads while maintaining efficiency.

### Implementation steps

- **Evaluate your current
infrastructure**. Assess your existing data
pipeline architecture to identify components that run
continuously but have low utilization. Look for workloads
with predictable patterns or batch processes that could
benefit from an event-driven approach using
[AWS CloudWatch metrics](https://aws.amazon.com/cloudwatch/) to identify utilization patterns.
- **Adopt managed services**.
Replace self-managed infrastructure with AWS managed
services to distribute sustainability impact across service
tenants. Services like
[AWS Glue](https://aws.amazon.com/glue/),
[AWS Lambda](https://aws.amazon.com/lambda/), and
[Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) provision resources on-demand and
automatically scale with your workloads.
- **Create serverless, event-driven data
pipelines**. Use
[AWS Glue](https://aws.amazon.com/glue/) for data processing and
[AWS Step Functions](https://aws.amazon.com/step-functions/) for orchestration to build ETL and ELT
pipelines that only consume resources when triggered. Step
Functions can coordinate AWS Glue jobs efficiently,
provisioning compute resources only when needed and
releasing them immediately after completion.
- **Implement efficient data
storage**. Choose appropriate storage solutions
like [Amazon S3](https://aws.amazon.com/s3/) for your data lake and
[Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically move data
between access tiers based on usage patterns, reducing
storage costs and resource waste.
- **Configure event-based
triggers**. Set up event notifications through
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) to automatically launch processing jobs
when new data arrives. This avoids the need for scheduled
jobs that might run when no new data is available, reducing
unnecessary compute usage.
- **Optimize compute
resources**. For AWS Glue jobs, configure
appropriate worker types and dynamically allocate resources
based on workload requirements. Use features like
[AWS Glue Auto Scaling](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) to automatically adjust capacity as
needed during jobs.
- **Implement monitoring and
metrics**. Set up comprehensive monitoring of your
serverless infrastructure using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track resource utilization, job
execution time, and idle periods. Use these metrics to
identify further optimization opportunities.
- **Establish automatic cleanup
processes**. Implement automated processes to
remove temporary resources, intermediate data, and other
artifacts after job completion to avoid unnecessary storage
costs and reduce digital waste.
- **Optimize data transfer**.
Minimize data movement between services by processing data
close to where it's stored when possible. Use
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data preparation tasks within the
same environment as your data storage.
- **Use AI-powered
optimization**. Use Amazon Q data integration in
AWS Glue to automatically generate optimized ETL jobs for
common data sources. This reduces development time while
implementing efficient resource utilization patterns from
the start.

## Resources

**Related documents:**

- [What
is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [What
is Amazon EMR Serverless?](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)
- [Using
auto scaling for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html)
- [What
is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Start
an AWS Glue job with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html)
- [Serverless
Applications Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)
- [Optimize
AI/ML workloads for sustainability: Part 3, deployment and
monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/)
- [Fuel
your data with Generative AI](https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus03-bp01.html*

---

# MLSUS03-BP02 Implement data lifecycle policies aligned with your sustainability goals

Classify your data to identify its business relevance and implement
efficient storage strategies that support your sustainability goals.
By understanding your data's importance, you can appropriately tier
storage, implement retention policies, and manage the entire
lifecycle to reduce your environmental footprint while meeting
business requirements.

**Desired outcome:** You have a
comprehensive data management strategy that classifies data based on
business importance and implements automatic storage optimization.
Your workloads store data in the most energy-efficient storage tiers
possible, and data that no longer serves a business purpose is
automatically purged, resulting in minimal storage footprint and
reduced environmental impact.

**Common anti-patterns:**

- Storing data indefinitely without classification or lifecycle
policies.
- Using a single storage tier for data regardless of access
patterns.
- Manually managing data retention and deletion.
- Keeping redundant or obsolete data that no longer serves
business purposes.

**Benefits of establishing this best
practice:**

- Reduced storage infrastructure and energy consumption.
- Improved data governance and adherence.
- Enhanced system performance with streamlined data management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing data lifecycle policies begins with understanding the
relationship between your data and business outcomes. Each
category of data has different requirements for retention, access
patterns, and eventual disposal. By aligning these requirements
with sustainability goals, you can optimize storage utilization
while improving business continuity.

Start by creating a data classification framework that categorizes
data based on its criticality, frequency of access, and business
value over time. This classification will guide your decisions
about which storage tiers to use and when data should be moved or
deleted. For instance, frequently accessed operational data might
remain in high-performance storage, while rarely accessed archival
data can be moved to more energy-efficient cold storage options.

Once you've classified your data, use AWS storage features like S3
Lifecycle policies to automate data transitions between storage
tiers and eventual deletion. For example, you can configure
policies that automatically transition data from S3 Standard to S3
Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, and
eventually to Amazon Glacier or S3 Glacier Deep Archive based on
access patterns and age.

### Implementation steps

- **Define your data classification
framework.** Develop a comprehensive data
classification system that categorizes data based on
business importance, access frequency, and regulatory
requirements. Include clear definitions for each data
category and establish ownership for classification
decisions.
- **Map retention requirements to data
classes.** For each data classification, determine
appropriate retention periods that satisfy business needs,
regulatory requirements, and sustainability goals. Document
these requirements to guide policy implementation.
- **Analyze current storage usage
patterns.** Use
[Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/) to gain visibility into your current
storage usage patterns, identifying opportunities for
optimization and tracking progress on storage efficiency
metrics.
- **Implement S3 Lifecycle
policies.** Configure
[Amazon S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition
data between storage classes and enforce deletion timelines
based on your defined retention requirements.
- **Deploy intelligent storage
tiering.** Implement
[Amazon S3 Intelligent-Tiering storage class](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically
move data between access tiers based on changing access
patterns, optimizing for both cost and sustainability.
- **Establish monitoring and
reporting.** Create dashboards to track storage
optimization metrics, including total storage used, storage
class distribution, and lifecycle transition metrics.
Regularly review these metrics to identify further
optimization opportunities.
- **Continuously refine data
classification.** Review and update your data
classification framework regularly to align it with evolving
business needs and sustainability goals.

## Resources

**Related documents:**

- [Managing
the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Managing
storage costs with Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [Comparing
the Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-compare)
- [Assessing
your storage activity and usage with Amazon S3 Storage
Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html)
- [Setting
an S3 Lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)
- [Data
discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus03-bp02.html*

---

# MLSUS03-BP03 Adopt sustainable storage options

Reduce the volume of data to be stored and adopt sustainable storage
options to limit the carbon impact of your workload. For artifacts
like models and log files that must be kept for long-term regulatory
and audit requirements, use efficient compression algorithms and use
energy efficient cold storage.

**Desired outcome:** You optimize
your ML workload storage to minimize environmental impact while
improving adherence to regulatory requirements. By implementing
efficient storage practices, you reduce data redundancy, properly
size resources, use energy-efficient storage options, and implement
effective compression techniques. This results in reduced carbon
footprint, lower storage costs, and improved overall sustainability
of your ML systems.

**Common anti-patterns:**

- Storing redundant copies of datasets across multiple locations.
- Over-provisioning storage resources for notebooks and instances.
- Using inefficient file formats like CSV instead of columnar
formats such as parquet.
- Keeping data in high-performance storage regardless of access
frequency.

**Benefits of establishing this best
practice:**

- Lower operational costs through efficient resource utilization.
- Improved data access performance through appropriate format
selection.
- Improved ability to adhere to regulatory requirements through
proper long-term storage planning.
- Reduced waste through optimization of storage resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Storage is a critical component of ML workloads, with large
datasets and model artifacts requiring significant resources. By
optimizing how you store, compress, and manage this data, you can
substantially reduce the environmental impact of your ML systems.
Consider the entire lifecycle of your data, from initial
collection through processing to long-term retention. For
frequently accessed data, choose efficient formats and compression
algorithms. For infrequently accessed data, use Amazon S3 storage
tiers that minimize energy consumption while improving your
adherence to regulatory requirements. By right-sizing your storage
resources and removing redundant data, you can achieve both
sustainability goals and cost optimization.

### Implementation steps

- **Reduce redundancy of processed
data**. If you can re-create an infrequently
accessed dataset, use the
[Amazon S3 One Zone-IA](https://aws.amazon.com/s3/storage-classes/#__) class to minimize the total data
stored. Implement S3 Lifecycle policies to automatically
transition objects to more energy-efficient storage tiers
based on access patterns.
- **Right size block storage for
notebooks**. Don't over-provision block storage of
your notebooks and use centralized object storage services
like [Amazon S3](https://aws.amazon.com/s3/) for common datasets to avoid data duplication.
Monitor usage patterns and adjust storage allocations
accordingly.
- **Use efficient file
formats**. Use
[Parquet](https://parquet.apache.org/)
to train your models. Compared to CSV, they can reduce
[your
storage by up to 87%](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.html#data-lake-optimization2). These columnar formats not only
reduce storage requirements but also improve query
performance.
- **Migrate to more efficient
compression algorithms**. Evaluate different
compression algorithms and select the most efficient for
your data. For example,
[Zstandard](https://github.com/facebook/zstd)
produces 10–15% smaller files than
[Gzip](https://www.gzip.org/) at the
same compression speed.
- **Implement storage lifecycle
management**. Configure
[S3
Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically move data
between access tiers based on changing usage patterns. For
long-term archival needs, use
[S3 Glacier Deep Archive](https://aws.amazon.com/s3/storage-classes/glacier/) to minimize energy consumption
for rarely accessed data.
- **Monitor and optimize storage
utilization**. Regularly review and clean up
unnecessary data and snapshots. Use
[Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/) to gain visibility into usage
patterns and identify optimization opportunities across your
organization.
- **Centralize and share
datasets**. Implement a centralized data catalog
using
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) to make datasets discoverable and
reusable, reducing the need for multiple copies of the same
data.
- **For generative AI workloads, use AI
for intelligent data management**. Implement
embeddings storage with efficient vector databases like
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) to optimize storage of large language
model context.

## Resources

**Related documents:**

- [Understanding
and managing Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Managing
storage costs with Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [Amazon S3 Storage Analytics and Insights](https://aws.amazon.com/s3/storage-analytics-insights/)
- [AWS Well-Architected Framework: Performance Efficiency Pillar -
Data Management](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/data-management.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus03-bp03.html*

---

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

# MLSUS06 — Monitoring

**Pillar**: Sustainability  
**Best Practices**: 2

---

# MLSUS06-BP01 Measure material efficiency

Measure efficiency of your workload in provisioned resources per
unit of work to determine not only the business success of the
workload, but also its material efficiency. Use this measure as a
baseline for your sustainability improvement process.

**Desired outcome:** You can quantify
and track the resources required by your machine learning workload
to deliver its business outcomes. By measuring resources per unit of
work, you create a sustainable baseline that allows you to track
improvements over time, make data-driven decisions about resource
optimization, and demonstrate the environmental impact of your
sustainability efforts.

**Common anti-patterns:**

- Focusing exclusively on business metrics without considering
resource consumption.
- Measuring total resource usage without normalizing by business
outcomes.
- Making optimization decisions without quantitative data on
resource efficiency.

**Benefits of establishing this best
practice:**

- Creates a clear way to measure sustainability progress over
time.
- Enables comparison of different implementations based on
material efficiency.
- Provides data to demonstrate ROI on sustainability improvements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Material efficiency is a critical aspect of sustainable machine
learning workloads. By measuring the resources provisioned per
unit of work, you gain visibility into how efficiently your
workload uses cloud resources to deliver business value. This
approach normalizes your sustainability metrics across different
workload sizes, usage patterns, and business outcomes.

When implementing material efficiency measurements, you should
first determine what constitutes a *unit of
work* for your specific ML workload. This could be a
model training run, a prediction request, a processed transaction,
or another relevant business outcome. Then, establish which
resources to track. Typically, this is compute (vCPU minutes),
storage (GB), and network (GB transferred). By dividing your
provisioned resources by these units of work, you create a
normalized efficiency metric that can be tracked over time.

For example, a recommendation engine might track vCPU minutes per
recommendation delivered, or a fraud detection system could
measure GB of storage per fraudulent transaction identified.
Tracking these metrics can determine if changes to your
architecture, algorithms, or deployment strategies are improving
efficiency or creating waste.

### Implementation steps

- **Define your unit of work**.
Identify what business outcomes your ML workload produces,
such as model training completions, predictions made,
insights generated, or transactions processed. Verify that
this metric directly relates to business value delivered.
- **Establish resource
metrics**. Track key resource consumption metrics
using Amazon CloudWatch. For ML workloads, important metrics
include compute utilization (vCPU minutes), memory usage,
storage consumption (GB), and network transfer (GB). AWS Cost Explorer can identify key cost drivers in your ML
workload.
- **Calculate baseline
efficiency**. Divide your resource consumption
metrics by your units of work to create efficiency ratios
(for example, vCPU minutes per prediction, GB storage per
model training run, or network transfer per transaction).
Document these values as your baseline for future
comparisons.
- **Set improvement targets**.
Based on your baseline measurements, set realistic targets
for reducing resource consumption per unit of work. Consider
both absolute reductions (total resources) and percentage
improvements over the baseline.
- **Implement monitoring and
reporting**. Use Amazon CloudWatch dashboards to
visualize your efficiency metrics over time. Set up alerts
for significant deviations from expected efficiency. Amazon SageMaker AI provides built-in monitoring capabilities for ML
workloads to track resource utilization.
- **Quantify improvement
benefits**. When implementing changes, calculate
both the immediate resource savings and the projected
long-term benefits. Include the return on investment from
your improvement activities to demonstrate value to
stakeholders.
- **Review and optimize
regularly**. Schedule regular reviews of your
efficiency metrics to identify new optimization
opportunities. As your workload evolves, your baseline and
targets may need adjustment.

## Resources

**Related documents:**

- [Analyzing
your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-what-is.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)
- [Measure
results and replicate successes](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/measure-results-and-replicate-successes.html)
- [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [Cloud
Financial Management with AWS](https://aws.amazon.com/aws-cost-management/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus06-bp01.html*

---

# MLSUS06-BP02 Retrain only when necessary

Because of model drift, robustness requirements, or new ground truth
data being available, models usually need to be retrained. Instead
of retraining arbitrarily, monitor your ML model in production,
automate your model drift detection and only retrain when your
model's predictive performance has fallen below defined KPIs.

**Desired outcome:** You will
establish a data-driven approach to model retraining that optimizes
computational resources while maintaining model performance. By
implementing automated monitoring and drift detection systems, you
can identify when your model's performance degrades below acceptable
thresholds and retrain only when necessary. This reduces unnecessary
computational overhead while verifying that your models remain
accurate and relevant.

**Common anti-patterns:**

- Retraining models on a fixed schedule regardless of performance.
- Manual monitoring of model performance leading to delayed
detection of drift.
- Retraining without clear performance thresholds or KPIs.

**Benefits of establishing this best
practice:**

- Reduced computational resources and carbon footprint.
- Lower operational costs for model maintenance.
- More efficient use of data science team resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning models deployed in production environments
naturally experience degradation in performance over time due to
changes in data patterns, user behaviors, or business
environments. This phenomenon, known as model drift, requires
retraining to maintain optimal performance. However, retraining a
model consumes significant computational resources, which impacts
both operational costs and environmental sustainability.

By implementing automated monitoring systems and establishing
clear performance thresholds, you can make data-driven decisions
about when to retrain your models. This approach verifies that
you're using computational resources efficiently while maintaining
the effectiveness of your ML systems. Through continuous
monitoring, you can detect both concept drift (changes in the
relationship between input and output variables) and data drift
(changes in the distribution of input data).

Your monitoring strategy should incorporate both technical metrics
(such as accuracy, precision, recall) and business-relevant KPIs
that directly tie to organizational outcomes. By correlating these
metrics with specific thresholds for retraining, you create a
sustainable approach to model maintenance that optimizes both
performance and resource utilization.

### Implementation steps

- **Determine key performance
indicators**. Work with business stakeholders to
identify minimum acceptable accuracy levels and maximum
acceptable error rates for your models. These KPIs should
directly connect to business outcomes and provide clear
thresholds for when retraining becomes necessary. Consider
both technical metrics (precision, recall, F1 score) and
business metrics (conversion rates, user engagement, revenue
impact) when establishing these thresholds.
- **Monitor your model deployed in
Production**. Implement
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously evaluate your
deployed models. SageMaker AI Model Monitor provides
capabilities for data quality monitoring, model quality
monitoring, bias drift monitoring, and feature attribution
drift monitoring. Configure alerts based on your established
KPIs to automatically notify your team when performance
begins to degrade.
- **Set up baseline metrics**.
Create a baseline of your model's performance metrics
immediately after deployment. This serves as a reference
point against which future performance can be measured.
SageMaker AI Model Monitor can automatically generate these
baselines from your training data or initial inference data.
- **Configure drift detection
thresholds**. Define specific threshold values that
indicate when drift has occurred to a degree that warrants
retraining. These thresholds should be based on your KPIs
and statistical measures of data or concept drift. Configure
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms to go off when these thresholds are
exceeded.
- **Automate your retraining
pipelines**. Use
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/),
[AWS Step Functions for Amazon SageMaker AI](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sagemaker.html), or third-party
tools to create automated workflows that can be initiated
when drift is detected. These pipelines should handle data
preparation, model training, evaluation, and deployment with
minimal manual intervention.
- **Optimize retraining
frequency**. Based on historical drift patterns,
adjust monitoring sensitivity and retraining thresholds to
optimize the frequency of retraining. Finding the right
balance keeps models performant while minimizing
computational overhead.
- **Establish canary
deployments**. When deploying retrained models, use
[SageMaker AI
deployment options](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html) like canary deployments to
gradually shift traffic to the new model while monitoring
performance, allowing for quick rollback if issues arise.
- **Leverage enhanced bias and drift
detection**. Use improved
[SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) capabilities with enhanced bias detection,
new fairness metrics, and better visualization tools to more
accurately detect when retraining is necessary.
- **Implement feedback loops for
generative models**. Establish mechanisms to
collect user feedback and engagement metrics to detect when
outputs become less relevant or helpful. Use
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) for fine-tuning foundation models
when drift is detected in generative applications.

## Resources

**Related documents:**

- [Amazon SageMaker AI Model Monitor documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Pipelines documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [AWS Step Functions for Data Science](https://docs.aws.amazon.com/step-functions/latest/dg/connect-sagemaker.html)
- [SageMaker AI
Deployment Guardrails](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html)
- [SageMaker AI Governance](https://aws.amazon.com/sagemaker/ai/ml-governance/)
- [Optimizing
MLOps for Sustainability](https://aws.amazon.com/blogs/machine-learning/optimizing-mlops-for-sustainability/)

**Related videos:**

- [SageMaker AI
HyperPod: Revolutionizing Foundation Model Training with
Resilience and Performance](https://aws.amazon.com/awstv/watch/c60e1437f63/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus06-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
