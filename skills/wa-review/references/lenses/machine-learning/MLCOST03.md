# MLCOST03 — Data processing

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# MLCOST03-BP01 Use managed data labeling

Use managed labeling tools that provide automation and access to
cost-effective teams of human data labelers. These tools should
offer flexibility to choose a variable number of labelers for each
input, include a user-friendly interface, and incorporate learning
capabilities to improve labeling efficiency over time.

**Desired outcome:** You have access
to high-quality labeled datasets for your machine learning models
without building and managing your own labeling infrastructure. Your
data labeling process is streamlined, cost-efficient, and scales
according to your needs, allowing you to focus on model development
rather than data preparation logistics.

**Common anti-patterns:**

- Building custom data labeling infrastructure from scratch.
- Relying solely on in-house teams for labeling tasks regardless
of scale.
- Using labeling solutions that don't improve through machine
learning.
- Managing inconsistent labeling quality without proper oversight
tools.

**Benefits of establishing this best
practice:**

- Reduce time-to-market for ML models by accelerating the data
labeling process.
- Lower total labeling costs through efficient automation and
on-demand workforce.
- Improve labeling quality and consistency through specialized
tools and workflows.
- Scale labeling operations up or down based on project
requirements.
- Focus your team's effort on model development rather than
labeling infrastructure.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To build effective machine learning models, you need large,
high-quality labeled datasets. Creating these datasets manually is
time-consuming, expensive, and difficult to scale. By using
managed data labeling services, you can accelerate this critical
step in the ML development process while controlling costs and
maintaining quality.

Managed data labeling combines human intelligence with machine
learning to improve efficiency over time. As your models process
more data, they can begin to automate parts of the labeling
process, reducing costs and time required. These services also
provide quality control mechanisms through consensus models, where
multiple labelers evaluate the same data to check accuracy.

When selecting a managed data labeling solution, consider factors
like the types of data you need to label (like images, text, and
video), the complexity of your labeling tasks, integration with
your existing ML workflow, and cost structure. The right solution
will scale with your needs and provide consistent, high-quality
labeled data.

### Implementation steps

- **Assess your data labeling
requirements**. Define what types of data you need
labeled (images, text, audio, or video), the complexity of
annotations required, expected volume, and quality
standards. Determine whether you need specialized domain
expertise for your labeling tasks.
- **Use Amazon SageMaker Ground Truth**. To train a machine learning model, you
need a large, high-quality, labeled dataset.
[Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) assists you to build
high-quality training datasets for your ML models. With
Ground Truth, you can use ML along with workers from a
vendor company that you choose, or an internal, private
workforce to create a labeled dataset. You can use the
labeled dataset output from Ground Truth to train your own
models. You can also use the output as a training data set
for an Amazon SageMaker AI model.
- **Use Amazon SageMaker Ground Truth
Plus**. Ground Truth Plus is a turn-key service
that uses an expert workforce to deliver high-quality
training datasets fast, and reduces costs by up to 40
percent.
[Amazon SageMaker Ground Truth Plus](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html) enables you to create
high-quality training datasets without having to build
labeling applications and manage the labeling workforce on
your own. By using this approach, you don't need to have
deep ML expertise or extensive knowledge of workflow design
and quality management. You simply provide data along with
labeling requirements and Ground Truth Plus sets up the data
labeling workflows and manages them on your behalf in
accordance with your requirements.
- **Configure active learning
workflows**. Set up your labeling projects to use
active learning, where the system learns from human
annotations and begins to automate labeling for similar
items. This reduces the number of items requiring manual
labeling over time, improving efficiency and reducing costs.
Amazon SageMaker Ground Truth provides built-in support for
active learning.
- **Implement quality control
mechanisms**. Configure your labeling jobs to use
multiple workers per data item and determine consensus
approaches based on your quality requirements. Monitor
labeling performance and adjust your quality control
parameters as needed.
- **Set up real-time data labeling
pipelines**. For ongoing ML projects, establish
continuous data labeling pipelines that can process new data
as it becomes available. This way, your models can be
regularly retrained with fresh data.
- **Create custom labeling interfaces
when needed**. For specialized labeling tasks, use
Ground Truth's custom template capabilities to create
tailored labeling interfaces that make the process more
efficient for your specific use case.
- **Use enhanced Ground Truth
capabilities**. Use improved Ground Truth Plus
features that provide up to 40% cost reduction through
expert workforce management and automated quality control
mechanisms.
- **Use foundation models for
pre-labeling**. Use generative AI models through
Amazon Bedrock to assist with initial data labeling, which
can then be verified by human labelers. This hybrid approach
can significantly accelerate the labeling process while
maintaining quality control.

## Resources

**Related documents:**

- [Training
data labeling using humans with Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)
- [Use
Amazon SageMaker Ground Truth Plus to Label Data](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html)
- [Using
the Amazon Mechanical Turk Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-public.html)
- [Automate
data labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html)
- [Custom
labeling workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates.html)
- [Annotation
consolidation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html)
- [Ground
Truth streaming labeling jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html)
- [Implementing
a custom labeling GUI with built-in processing logic with
Amazon SageMaker Ground Truth](https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/)

**Related examples:**

- [Bring
your own model for SageMaker AI labeling workflows with active
learning](https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning.ipynb)
- [SageMaker AI
Ground Truth recipe](https://github.com/aws-samples/aws-sagemaker-ground-truth-recipe)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp01.html*

---

# MLCOST03-BP02 Use no-code or low-code and code generation tools for interactive analysis

Prepare data through data wrangler tools for interactive data
analysis and model building. The no-code/low-code, automation, and
visual capabilities improve productivity and reduce the cost for
interactive analysis. Integrate with generative AI code generation
tools.

**Desired outcome:** You will be able
to streamline your data preparation workflow using visual interfaces
with minimal coding required. By implementing no-code or low-code
tools like Amazon SageMaker AI Canvas and Data Wrangler, you reduce
time spent on data preprocessing tasks and gain improved insights
through interactive visualizations. Amazon Q integration provides
intelligent assistance for data preparation and code generation,
enabling faster iteration cycles on model development while
maintaining data quality and consistency across your machine
learning projects.

**Common anti-patterns:**

- Writing custom data preparation scripts for every analysis task.
- Using disjointed tools for data import, transformation, and
visualization.
- Manually performing repetitive data cleaning operations.
- Creating non-reproducible data preparation workflows.

**Benefits of establishing this best
practice:**

- Reduced time and cost for data preparation and feature
engineering.
- Improved productivity through visual interfaces and automation.
- Streamlined workflow from data import to model deployment.
- Support for code and no-code approaches to accommodate different
skill levels.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data preparation is often cited as the most time-consuming aspect
of machine learning projects, typically consuming 60-80% of data
scientists' time. Data wrangler tools provide visual interfaces to
simplify and accelerate this process through automation and
low-code solutions.

Amazon SageMaker AI Data Wrangler offers an end-to-end solution for
data preparation that integrates directly with your machine
learning workflow. By using a visual interface, you can import
data from various sources, identify and fix data quality issues,
transform features, and generate insights—all with minimal coding
required. The tool provides transparency by generating code for
your transformations, fostering reproducibility and allowing
customization when needed.

Data wrangler tools are particularly valuable for exploratory data
analysis, where quick iteration and visualization are essential.
They allow you to rapidly identify patterns, outliers, and
relationships in your data, accelerating the feature engineering
process. With built-in data quality and insights features, you can
understand your data characteristics and address issues before
model training begins.

### Implementation steps

- **Set up Amazon SageMaker AI Canvas or
Studio environment**. Access SageMaker AI Canvas for a
no-code experience or SageMaker AI Studio for more advanced
capabilities through the AWS Management Console. Canvas
provides a visual, drag-and-drop interface for business
analysts and citizen data scientists, while Studio offers
Data Wrangler for more technical users. Both environments
support the complete machine learning workflow with varying
levels of coding requirements.
- **Import data from various
sources**. Use SageMaker AI Canvas or Data Wrangler to
connect to multiple data sources including Amazon S3, Amazon Athena, Amazon Redshift, Snowflake, and various databases.
Canvas provides a simplified point-and-click interface for
business users, while Data Wrangler offers more advanced
data source connectivity options. Both tools avoid the need
for custom connector code.
- **Explore and visualize your
data**. USe Data Wrangler's built-in data
visualizations to understand distributions, correlations,
and outliers. These visualizations assist to identify
potential issues early and inform feature engineering
decisions without writing complex plotting code.
- **Use Amazon Q for generative
AI-powered data preparation and code generation**.
Use Amazon Q integrated within SageMaker AI Canvas and Data
Wrangler to get natural language assistance for data
preparation tasks, automated code generation, and
intelligent suggestions for data transformations. Amazon Q
can explain data patterns, suggest optimal preprocessing
steps, and generate code snippets for custom
transformations, significantly reducing the time needed for
data preparation tasks. Additionally, use AI-powered
development tools like Kiro for intelligent code generation
and optimization of your data processing workflows.
- **Apply transformations to prepare
your data**. Use the visual transformation
interface to clean and prepare data through operations like
handling missing values, encoding categorical features,
scaling numerical values, and feature extraction. Data
Wrangler provides over 300 built-in transformations while
allowing custom Python transformations when needed.
- **Analyze data quality and generate
insights**. Use the built-in data quality and
insights features to detect anomalies, check for imbalanced
data, and understand feature importance. These automated
analyses identify potential issues before model training
begins.
- **Balance your datasets**.
Address imbalanced datasets using built-in techniques like
random oversampling, random undersampling, and synthetic
minority oversampling (SMOTE). Data Wrangler provides visual
controls to implement these techniques without specialized
knowledge.
- **Scale to larger datasets**.
Process larger datasets by configuring instance types and
using distributed processing capabilities. Data Wrangler
supports processing wide datasets with thousands of columns
and large datasets with billions of rows through appropriate
resource allocation.
- **Prepare time series data**.
Use specialized time series transformations to handle
temporal data, including resampling, lagged feature
creation, and time-based aggregations. These operations
simplify working with sequential data patterns.
- **Export your data flow for
production**. Deploy your data preparation workflow
by exporting to various destinations including Amazon S3,
SageMaker AI Feature Store, or directly to model building
workflows. Data Wrangler generates Python code that can be
integrated into production pipelines. Canvas workflows can
also be exported to SageMaker AI notebooks for further
customization and integration into production pipelines.
- **Use enhanced Canvas
capabilities**. Use SageMaker AI Canvas's improved
natural language support and Q integration for
conversational data analysis, enabling business users to
perform complex data preparation tasks without technical
expertise.
- **Integrate with the broader machine
learning workflow**. Connect your prepared data
directly to SageMaker AI's model building capabilities like
SageMaker AI Autopilot for automated model development or
custom model training. This integration creates a seamless
path from data to deployed models.

## Resources

**Related documents:**

- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Get
Started with Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html)
- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [What
is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)
- [What
is AWS Glue DataBrew?](https://docs.aws.amazon.com/databrew/latest/dg/what-is.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Accelerate
data preparation with data quality and insights in Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/accelerate-data-preparation-with-data-quality-and-insights-in-amazon-sagemaker-data-wrangler/)
- [Process
larger and wider datasets with Amazon SageMaker AI Data
Wrangler](https://aws.amazon.com/blogs/machine-learning/process-larger-and-wider-datasets-with-amazon-sagemaker-data-wrangler/)
- [Fuel
Your Data with Generative AI](https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/)

**Related examples:**

- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/data-wrangler.md)
- [SageMaker AI
Data Wrangler Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-datawrangler)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp02.html*

---

# MLCOST03-BP03 Use managed data processing capabilities

With managed data processing, you can use a simplified, managed
experience to run your data processing workloads, such as feature
engineering, data validation, model evaluation, and model
interpretation.

**Desired outcome:** By implementing
managed data processing capabilities, you can streamline your
machine learning workflow with fully managed infrastructure for data
preprocessing and postprocessing tasks. You gain the ability to run
processing jobs that integrate with popular frameworks while
maintaining operational efficiency, allowing your team to focus on
creating valuable ML models rather than managing infrastructure.

**Common anti-patterns:**

- Building and maintaining custom data processing infrastructure.
- Managing your own compute clusters for data processing tasks.
- Manually handling scaling, deployment, and cleanup of processing
resources.
- Using inconsistent processing environments across development
and production.

**Benefits of establishing this best
practice:**

- Reduced operational overhead with fully managed infrastructure.
- Simplified integration with popular ML frameworks and AWS
services.
- Enhanced productivity by focusing on ML development rather than
infrastructure management.
- Seamless integration with other SageMaker AI capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Amazon SageMaker AI Processing provides a managed solution for
running these data processing workloads. Instead of provisioning
and managing your own infrastructure, SageMaker AI handles the
provisioning, scaling, and cleanup of resources. Processing jobs
accept data from Amazon S3 as input and store processed results
back to S3 as output. You can use AWS-provided container images
that come pre-configured with popular data science frameworks, or
you can bring your own custom containers for specialized
processing needs.

By using SageMaker AI Processing, you can integrate data processing
steps seamlessly into your ML pipelines and create consistency
between development and production environments while reducing
operational overhead. This allows your data scientists and ML
engineers to focus on extracting insights from data rather than
managing infrastructure.

### Implementation steps

- **Set up your processing job
environment**. Create an Amazon SageMaker AI notebook
instance or Studio environment from which you'll configure
and launch your processing jobs. This provides an
interactive environment for development and testing of your
data processing scripts before scaling to larger datasets.
- **Select or create a processing
container**. Choose from SageMaker AI's built-in
processing containers for frameworks like scikit-learn,
PyTorch, TensorFlow, or Apache Spark. Alternatively, create
a custom Docker container if you have specialized framework
requirements. The container will include the runtime
environment and dependencies needed for your processing
tasks.
- **Prepare your processing
script**. Develop a script that runs within the
processing container to perform your data transformation,
feature engineering, model evaluation, or other processing
tasks. This script should read input data, process it
according to your requirements, and write output to the
designated locations.
- **Configure storage
locations**. Set up Amazon S3 buckets to store your
input data, processing scripts, and output results.
SageMaker AI Processing jobs use S3 as the primary storage
mechanism for exchanging data between steps in your ML
workflow.
- **Launch a processing job**.
Use the SageMaker AI Python SDK or AWS console to configure and
start your processing job. Specify parameters such as
instance type, instance count, environment variables, and
input and output configurations. SageMaker AI will provision
the requested resources, run your processing script, and
then automatically clean up the resources when the job
completes.
- **Monitor job progress and analyze
results**. Track your processing job through the
SageMaker AI console or API. Review logs to debug issues. Once
completed, access the processed data in the specified S3
output locations for use in subsequent ML workflow steps.
- **Integrate with ML
pipelines**. Incorporate your processing jobs into
[SageMaker AI
Pipelines](https://aws.amazon.com/sagemaker/pipelines/) to create automated end-to-end ML
workflows. This enables you to orchestrate data
preprocessing, model training, evaluation, and deployment
steps in a repeatable manner.
- **Optimize resource utilization and
costs**. Review processing job metrics to identify
opportunities for optimizing instance selection and
parallelization strategies. Consider using Spot instances
for cost savings on non-time-sensitive processing jobs.
- **Use enhanced processing
capabilities**. Use SageMaker AI Processing with
better integration to popular ML frameworks and enhanced
monitoring capabilities for more efficient data processing
workflows.
- **Use AI-powered code generation for
data processing**. Use AI-powered development tools
like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
data processing scripts, automate pipeline creation, and
accelerate the development of custom data transformation
workflows.
- **Implement data validation and
quality checks**. Incorporate data validation steps
in your processing jobs to check data quality before model
training. Use SageMaker AI Clarify within processing jobs to
detect bias in your datasets and implement model
explainability.

## Resources

**Related documents:**

- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/)
- [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/)

**Related examples:**

- [Amazon SageMaker AI Processing jobs](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.html)
- [SageMaker AI
Processing with Spark](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/spark_distributed_data_processing)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp03.html*

---

# MLCOST03-BP04 Enable feature reusability

Reduce duplication and the rerunning of feature engineering code
across teams and projects by using feature storage. The store should
have online and offline storage, and data encryption capabilities.
An online store with low-latency retrieval capabilities is ideal for
real-time inference. An offline store maintains a history of feature
values and is suited for training and batch scoring.

**Desired outcome:** You gain a
centralized repository for storing, sharing, and managing machine
learning features that reduces redundant work across teams and
projects. You access features with low latency for real-time
applications while maintaining a historical record for training
purposes. Your feature store integrates seamlessly with your ML
workflows, enhancing collaboration and accelerating model
development while maintaining data security through robust
encryption.

**Common anti-patterns:**

- Recreating the same features repeatedly across different teams
and projects.
- Storing features in isolated data silos that avoid reuse.
- Lacking version control for features, leading to inconsistencies
between training and inference.
- Using separate systems for real-time and batch feature access.
- Implementing homegrown feature storage solutions that lack
scalability and proper governance.

**Benefits of establishing this best
practice:**

- Reduces redundant work and computational costs.
- Creates consistency between training and inference environments.
- Enables collaboration and knowledge sharing across teams.
- Provides feature governance, lineage, and traceability.
- Reduces time to production for ML models.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Feature engineering is often one of the most time-consuming
aspects of machine learning development. When teams work in silos,
they frequently recreate the same features, wasting valuable time
and resources. By implementing a centralized feature store, you
create a single source of truth for ML features that promotes
reusability across your organization.

A well-designed feature store addresses the dual requirements of
offline storage for training and batch inference and online
storage for low-latency real-time inference. This dual-storage
paradigm creates consistency between training and serving
environments while optimizing for different access patterns. The
feature store should also provide capabilities for feature
versioning, access control, and monitoring to maintain data
quality and governance.

Amazon SageMaker AI Feature Store offers these capabilities as a
fully managed service, which reduces the need to build and
maintain complex infrastructure. It seamlessly integrates with
your ML pipelines and supports both batch and real-time inference
workflows, making it an ideal solution for feature reusability.

### Implementation steps

- **Identify common features across
projects**. Begin by analyzing your existing ML
workflows to identify frequently used features that would
benefit from centralization. Look for redundancies in
feature engineering code across different teams and
prioritize these for migration to the feature store.
- **Set up Amazon SageMaker AI Feature
Store**. Create feature groups in
[Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to organize related
features. Define the schema for each feature group,
including feature names, data types, and primary keys.
Consider the access patterns for both training and inference
when designing your feature groups.
- **Configure storage options based on
requirements**. Determine whether each feature
group needs online storage, offline storage, or both.
Configure the appropriate storage options:

**Online store:** Set up
for low-latency access (milliseconds) needed for
real-time inference
- **Offline store:**
Configure Amazon S3 storage for training and batch
inference workloads
- **Online and offline:**
Implement both for maximum flexibility

- **Implement data ingestion
pipelines**. Develop automated pipelines to ingest
data into your feature store. You can use
[Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) for data preparation and
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) for orchestration.
- **Establish feature access
patterns**. Create standardized methods for
retrieving features for both training and inference. For
training, use the offline store with Amazon Athena queries
to efficiently access historical data. For real-time
inference, implement API calls to the online store for
low-latency feature retrieval.
- **Enable cross-account and cross-team
sharing**. Configure resource policies to enable
feature sharing across different teams and AWS accounts.
This promotes collaboration and maximizes feature reuse
across your organization while maintaining appropriate
access controls.
- **Implement feature versioning and
lineage tracking**. Track changes to features over
time using versioning capabilities. Link features to models
through
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to maintain full lineage
tracking from data source to deployed model.
- **Monitor feature usage and
drift**. Implement monitoring for your feature
store to detect data drift and track feature usage patterns.
Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to detect changes in feature
distributions that might impact model performance.
- **Create documentation and discovery
mechanisms**. Document features and their intended
use cases to facilitate discovery and reuse. Implement
tagging and search capabilities so that data scientists can
find relevant features for their projects.
- **Use enhanced Feature Store
capabilities**. Use improved SageMaker AI Feature
Store with better performance, enhanced monitoring
capabilities, and improved integration with other SageMaker AI
services for more efficient feature management.
- **Use generative AI for feature
discovery and documentation**. Use large language
models through
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to automatically generate feature
descriptions, identify potential feature relationships, and
improve feature discoverability through natural language
search capabilities.

## Resources

**Related documents:**

- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Amazon SageMaker AI Feature Store resources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-notebooks.html)
- [Understanding
the key capabilities of Amazon SageMaker AI Feature
Store](https://aws.amazon.com/blogs/machine-learning/understanding-the-key-capabilities-of-amazon-sagemaker-feature-store/)

**Related examples:**

- [Amazon SageMaker AI Feature Store Notebook Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-notebooks.html)

**Related videos:**

- [Training
and Tuning State-of-the-Art Models with Amazon SageMaker AI](https://aws.amazon.com/awstv/watch/90cac7f03b4/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp04.html*

---
