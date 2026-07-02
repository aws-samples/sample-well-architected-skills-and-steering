# MLOPS03 — Data processing

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# MLOPS03-BP01 Profile data to improve quality

Data profiling is essential for understanding data characteristics
such as distribution, descriptive statistics, data types, and
patterns. By systematically reviewing source data for content and
quality, you can filter out or correct problematic data, leading to
significant quality improvements in your machine learning workflows.

**Desired outcome:** You gain
comprehensive insights into your data's characteristics, enabling
you to identify and remediate quality issues before they impact your
machine learning models. Through systematic profiling, you establish
a robust data preprocessing pipeline that provides high-quality,
consistent data flows to your ML models, resulting in more accurate
predictions and better business outcomes.

**Common anti-patterns:**

- Skipping data profiling and moving directly to model training.
- Manually reviewing data without automated profiling tools.
- Performing one-time data quality checks without continuous
monitoring.
- Ignoring data distribution shifts between training and inference
data.
- Failing to document data quality issues and their resolutions.

**Benefits of establishing this best
practice:**

- Improved model performance through higher quality training data.
- Earlier detection of data anomalies and inconsistencies.
- Enhanced understanding of data characteristics and limitations.
- Reduced time spent debugging model issues caused by data
problems.
- More transparent and reproducible machine learning workflows.
- Increased stakeholder confidence in model outputs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data profiling is a critical step in the machine learning
workflow. By thoroughly examining your data before model training,
you gain valuable insights that improve data quality and
ultimately lead to better model performance. Data profiling
involves analyzing the statistical properties, distributions, and
patterns within your dataset to identify anomalies, missing
values, outliers, and other quality issues.

Effective data profiling requires both automated tools and human
judgment. While tools can quickly generate statistical summaries
and visualizations, subject matter experts should interpret these
findings to determine appropriate actions for data cleaning and
transformation. For instance, you might discover that a numerical
feature has an unexpected distribution that requires
normalization, or that categorical variables contain inconsistent
values requiring standardization.

Consider a retail company building a customer churn prediction
model. Through data profiling, they discover that 15% of customer
records have missing age values, 5% have impossibly high
transaction amounts, and several categorical fields contain
inconsistent formatting. By addressing these issues early, they
can significantly improve their model's performance.

### Implementation steps

- **Set up Amazon SageMaker AI Unified
Studio for visual data review**. Use
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) with enhanced collaborative
features and team sharing capabilities to visually review
data characteristics and remediate data-quality problems
directly in your integrated environment. The unified
solution provides improved debugging and monitoring
capabilities for data processing workflows, automatically
generating charts to identify data quality issues and
suggesting transformations to fix common problems.
- **Implement Amazon SageMaker AI Data
Wrangler for comprehensive data preparation**.
Import, prepare, transform, visualize, and analyze data with
[SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) with
[Q
integration for interactive analysis](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-q-integration.html). You can
integrate Data Wrangler into your ML workflows to simplify
and streamline data pre-processing and feature engineering
with little to no coding. Import data from
[Amazon S3](https://aws.amazon.com/s3/),
[Amazon Redshift](https://aws.amazon.com/redshift/), or other data sources, and then query the
data using
[Amazon Athena](https://aws.amazon.com/athena/). Use Data Wrangler's built-in and custom data
transformations and analysis features, including feature
target leakage detection and quick modeling, to create
sophisticated machine learning data preparation workflows.
- **Build an automatic data profile and
reporting system**. Use
[AWS Glue Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) to crawl your data sources and
automatically create a data schema. The crawler detects the
schema of your data and registers tables in the
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html), providing a comprehensive listing
of tables and schemas. Use
[Amazon Athena](https://aws.amazon.com/athena/) for serverless SQL querying to constantly
profile your data, and create
[Quick](https://aws.amazon.com/quicksight/) dashboards for data visualization and
monitoring.
- **Create a baseline dataset with
SageMaker AI Model Monitor**. The training dataset
used to train your model typically serves as a good baseline
dataset. Verify that the training dataset schema and the
inference dataset schema exactly match (the number and order
of the features). With
[SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html), you can automatically detect
concept drift in deployed models by comparing production
data against this baseline.
- **Implement continuous data quality
monitoring**. Set up automated checks that
continuously monitor data quality metrics like completeness,
uniqueness, consistency, and validity. Configure alerts to
notify relevant stakeholders when data quality issues arise,
enabling prompt intervention and resolution. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to create dashboards and set up alerts for
key data quality metrics.
- **Document data profiling insights and
transformations**. Maintain comprehensive
documentation of data profiling findings, quality issues
discovered, and the transformations applied to address them.
This documentation promotes transparency, facilitates
knowledge sharing across teams, and supports regulatory
adherence in regulated industries.
- **Use generative AI for enhanced data
profiling**. Use large language models in
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) or
[Amazon
Nova](https://aws.amazon.com/ai/generative-ai/nova/) to automatically extract and enrich metadata,
identify patterns in your data, and generate natural
language summaries of data quality issues. Generative AI can
analyze unstructured data fields and provide insights that
traditional data profiling tools might miss, though you
should validate AI-generated suggestions before
implementation.

## Resources

**Related documents:**

- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [Get
Started with Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html)
- [Data
quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)
- [Create
a Baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html)
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
- [Data
discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)
- [Amazon SageMaker AI notebooks](https://aws.amazon.com/sagemaker/notebooks/)
- [What
is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [What
is Amazon Quick Suite?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops03-bp01.html*

---

# MLOPS03-BP02 Create tracking and version control mechanisms

Machine learning model development requires robust tracking and
version control mechanisms due to its iterative and exploratory
nature. By implementing proper tracking systems, you can maintain
visibility of your experiments, data processing techniques, and
model versions while enabling reproducibility and collaboration.

**Desired outcome:** You have
comprehensive tracking of ML model development with experiment
tracking capabilities, version-controlled data processing code, and
a model registry that enables you to identify the best performing
models. Your development processes are reproducible, collaborative,
and automated with CI/CD pipelines for model deployment.

**Common anti-patterns:**

- Manually tracking experiments in spreadsheets or documents.
- Not documenting data processing steps or model configurations.
- Keeping models and datasets in local environments without
version control.
- Starting new experiments from scratch instead of building on
previous work.

**Benefits of establishing this best
practice:**

- Enhanced reproducibility of experiments and model training.
- Improved collaboration among data science teams.
- Better visibility into the performance of different model
iterations.
- Faster identification of the best performing models.
- Ability to roll back to previous model versions if needed.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning development involves experimenting with multiple
combinations of data, algorithms, and parameters while observing
how incremental changes impact model accuracy. Without proper
tracking and version control, you risk losing valuable insights
and the ability to reproduce successful experiments.

To address these challenges, you need a systematic approach to
track experiments, version control your code and data processing
techniques, and manage model deployment. AWS SageMaker AI provides
integrated tools for experiment tracking, version control, and
model registry that can streamline your machine learning
operations.

By implementing proper tracking and versioning mechanisms, you can
document your model development journey, track performance metrics
across experiments, and reliability reproduce and deploy your
models. This creates a foundation for continuous improvement of
your machine learning applications.

### Implementation steps

- **Track your ML experiments with
SageMaker AI Experiments**. Use Amazon SageMaker AI
Experiments to you create, manage, analyze, and compare your
machine learning experiments. SageMaker AI Experiments
automatically tracks inputs, parameters, configurations, and
results of your iterations as runs. You can assign, group,
and organize these runs into experiments. SageMaker AI
Experiments integrates with Amazon SageMaker AI Studio,
providing a visual interface to browse active and past
experiments, compare runs on key performance metrics, and
identify the best-performing models.
- **Process data with SageMaker AI
Processing**. For analyzing data, documenting
processing, and evaluating ML models, use
[Amazon SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html). This capability can be used for
feature engineering, data validation, model evaluation, and
model interpretation. SageMaker AI Processing provides a
standardized way to run your data processing workloads,
fostering consistency and reproducibility.
- **Use SageMaker AI Unified Studio for
enhanced collaboration**. Use
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) with enhanced collaborative
features and team sharing capabilities for integrated data
and AI workflows. The unified solution provides improved
debugging and monitoring capabilities, VS Code server
integration, and enhanced project sharing. This approach
keeps your data processing code and documentation accessible
while facilitating better collaboration and version tracking
across teams.
- **Use SageMaker AI Model
Registry**. Catalog, manage, and deploy models
using SageMaker AI Model Registry. Create a model group and,
for each run of your ML pipeline, create a model version
that you register in the model group. The Model Registry
provides a centralized repository for model versions, making
it more straightforward to track model lineage, compare
model performance, and promote models to production.
- **Implement CI/CD for model
deployment**. Automate your model deployment
process using CI/CD pipelines for consistent and reliable
deployments. SageMaker AI Pipelines can be used to create
end-to-end workflows that include model building,
evaluation, and deployment steps. Implement CI/CD for model
deployment to thoroughly test your models before they are
deployed to production, reducing the risk of
deployment-related issues.
- **Integrate data version
control**. Use tools like Data Version Control
(DVC) in conjunction with SageMaker AI Experiments to track
both your model code and the datasets used for training and
evaluation. With these tools, you can completely reproduce
your machine learning experiments.
- **Create model cards for
documentation**. For each model version in your
registry, create comprehensive
[SageMaker AI
Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) with enhanced documentation and
governance capabilities that document the model's purpose,
training data, performance metrics, limitations, and usage
guidelines. This documentation helps users understand when
and how to use specific model versions and supports improved
model governance.

## Resources

**Related documents:**

- [Amazon SageMaker AI Experiments in Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Git
repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html)
- [MLOps
Automation With SageMaker AI Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects.html)
- [Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)

**Related examples:**

- [SageMaker AI
Experiment Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments)
- [SageMaker AI
Model Registry Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines)
- [Amazon SageMaker AI processing](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops03-bp02.html*

---
