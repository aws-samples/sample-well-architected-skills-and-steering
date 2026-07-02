# MLREL03 — Model development

**Pillar**: Reliability  
**Best Practices**: 4

---

# MLREL03-BP01 Enable CI/CD/CT automation with traceability

Enable source code, data, and artifact version control of ML
workloads to enable roll back to a specific version. Incorporate
continuous integration (CI), continuous delivery (CD), and
continuous training (CT) practices to ML workload operations,
providing automation with added traceability.

**Desired outcome:** You establish
automated pipelines that handle the entire machine learning
lifecycle from development to deployment and continuous training.
You gain the ability to track every artifact, model version,
dataset, and code change throughout the ML workflow, enabling
transparent auditing, reproducibility of experiments, and the
capability to quickly roll back to previous versions when needed.

**Common anti-patterns:**

- Manual deployment and training processes without version
control.
- Lack of documentation on model lineage and data provenance.
- Inability to reproduce ML experiments due to missing environment
configurations.
- Performing model training only when necessary without automated
testing and validation.
- Siloed development and operations teams working separately on ML
workflows.

**Benefits of establishing this best
practice:**

- Increases productivity through automation of repetitive ML
development tasks.
- Improves reproducibility of ML experiments and model training.
- Enhances collaboration between data scientists and operations
teams.
- Accelerates time-to-market for ML-powered features and
applications.
- Reduces risk through ability to quickly roll back problematic
deployments.
- Improves adherence to audit requirements through comprehensive
traceability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing CI/CD/CT for machine learning workloads requires a
different approach than traditional software development due to
the data-centric nature of ML systems. While software CI/CD
focuses primarily on code, ML pipelines must also track data,
model artifacts, and training environments for full
reproducibility.

MLOps combines DevOps practices with machine learning to automate
and streamline the entire lifecycle of ML systems. By implementing
MLOps with traceability, you create a foundation that supports
reproducible science, auditability, and operational excellence.
This allows your organization to deploy ML models with confidence
while maintaining the ability to understand exactly how each model
was created and what data influenced its behavior.

Amazon SageMaker AI provides a comprehensive solution to implement
MLOps practices with built-in version control, lineage tracking,
and pipeline automation. By using SageMaker AI and complementary AWS
services, you can establish a robust MLOps framework that makes
your ML workflows reproducible, traceable, and maintainable.

### Implementation steps

- **Implement version control for ML
artifacts**. Set up repositories for code, data,
models, and configurations using version control systems.
Use
[AWS CodeCommit](https://aws.amazon.com/codecommit/) or integrate with GitHub to version your
ML code and configurations. For data and models, use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to version and catalog your
models, creating a system of record that tracks the lineage
of each model.
- **Set up data versioning and lineage
tracking**. Implement data version control to track
changes in your datasets over time. Use
[Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to store, share, and manage
features for ML development, which you can use to track and
version feature values. Implement Lineage Tracking to track
the relationships between ML artifacts including data,
models, training jobs, and deployments.
- **Establish continuous integration
practices**. Configure automated tests that verify
both code quality and model performance. Set up CI pipelines
using
[AWS CodeBuild](https://aws.amazon.com/codebuild/) that run unit tests, integration tests, and
model quality tests when changes are pushed to your
repositories. Implement automated code review practices to
maintain quality standards across your ML codebase.
- **Build continuous delivery pipelines
for models**. Create automated deployment pipelines
for ML models using
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) or
[AWS CodePipeline](https://aws.amazon.com/codepipeline/). Configure pipelines to include stages
for data preparation, model training, evaluation, and
deployment. Implement approval gates for human validation
before models are deployed to production environments.
- **Implement continuous training
mechanisms**. Set up automated retraining pipelines
that can be triggered by data drift, scheduled intervals, or
on-demand. Use Amazon SageMaker AI Pipelines to create
end-to-end workflows for model retraining. Implement
monitoring for model drift using
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) and trigger retraining when performance
degrades below thresholds.
- **Establish model governance and
approval workflows**. Create a governance framework
that requires appropriate reviews and approvals before
models move to production. Use SageMaker AI Model Registry to
implement model approval workflows with different approval
stages. Configure integration with notification services
like [Amazon SNS](https://aws.amazon.com/sns/) to alert stakeholders when models need review.
- **Implement immutable infrastructure
for reproducibility**. Use infrastructure as code
(IaC) to define your ML environments consistently. Leverage
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[AWS CDK](https://aws.amazon.com/cdk/) to define your SageMaker AI environments,
maintaining consistency across development, testing, and
production. Create standardized container images for
training and inference to improve environment
reproducibility.
- **Set up comprehensive monitoring and
logging**. Implement monitoring for your ML
pipelines and deployed models. Use
[CloudWatch](https://aws.amazon.com/cloudwatch/)
to track operational metrics of your pipeline runs and model
endpoints. Configure SageMaker AI Model Monitor to track data
drift, model drift, and prediction quality over time.
- **Create rollback mechanisms for
models and pipelines**. Establish automated
rollback procedures that can quickly revert to previous
model versions when issues are detected. Configure SageMaker AI
endpoints with production variants to support blue/green
deployments and canary testing, enabling safe rollbacks when
needed.

## Resources

**Related documents:**

- [Implement
MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html)
- [Pipelines
overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-sdk.html)
- [AWS DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)
- [Create
Amazon SageMaker AI projects with image building CI/CD
pipelines](https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/)

**Related videos:**

- [Deliver
high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc)
- [Accelerate
production for gen AI using Amazon SageMaker AI MLOps &
FMOps](https://www.youtube.com/watch?v=-3Otl7GVeCc)

**Related examples:**

- [Amazon
Sagemaker MLOps](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)
- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp01.html*

---

# MLREL03-BP02 Verify feature consistency across training and inference

Provide consistent, scalable, and highly available features between
training and inference using a feature storage. This results in
reducing the training-serving skew by keeping feature consistency
between training and inference.

**Desired outcome:** You create a
centralized feature repository where feature definitions are stored,
versioned, and shared across your organization. This makes the same
features used during model training consistently available during
inference, which reduces training-serving skew. You can discover,
reuse, and share features across different ML projects, reducing
duplicate work and standardizing feature engineering practices.

**Common anti-patterns:**

- Recreating feature transformations separately for training and
inference pipelines.
- Storing features in different formats or locations for training
versus production.
- Lack of versioning for features, leading to inconsistencies when
models are updated.
- Duplicating feature engineering work across different teams or
projects.
- Using non-standardized approaches to feature storage and
retrieval.

**Benefits of establishing this best
practice:**

- Reduces training-serving skew, leading to more reliable model
performance in production.
- Increases developer productivity through feature reusability.
- Standardizes feature definitions across the organization.
- Improves model governance and auditability through feature
versioning.
- Saves costs by avoiding redundant feature computation and
storage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Feature consistency between training and inference is critical for
machine learning system reliability. When the features used to
train a model differ from those used during inference, model
performance can degrade, a problem known as training-serving skew.
To avoid this issue, you need a centralized feature repository
that provides consistent access to the same feature definitions
and transformations across both training and inference
environments.

A feature store serves as this centralized repository, enabling
you to define, store, and retrieve features consistently. It
provides mechanisms for versioning features, which verifies that
you can maintain compatibility between models and the features
they expect as your data and feature engineering processes evolve.
Additionally, a feature store allows for the sharing and reuse of
features across multiple ML projects, increasing efficiency and
standardizing feature engineering practices across your
organization.

### Implementation steps

- **Set up Amazon SageMaker AI Feature
Store**. Create and configure a
[SageMaker AI
Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to serve as your centralized repository
for ML features. SageMaker AI Feature Store provides both
online and offline storage capabilities: the online store
supports low-latency, real-time inference use cases, while
the offline store supports training and batch inference
processes. Create a feature group that defines your feature
structure, data types, and storage configurations using the
SageMaker AI SDK or console.
- **Define feature groups and
schemas**. Organize your features into logical
groups based on business domains, data sources, or ML use
cases. Define schemas for your features, including data
types, descriptions, and metadata. This organization makes
features more discoverable and more straightforward to
manage across your organization.
- **Implement feature ingestion
pipelines**. Build automated pipelines to ingest
and process raw data into features. Use
[SageMaker AI
Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html),
[AWS Glue](https://aws.amazon.com/glue/), or
[Amazon EMR](https://aws.amazon.com/emr/) to transform raw data into feature values.
Configure both batch ingestion for historical data and
streaming ingestion for real-time updates using services
like
[Amazon Kinesis](https://aws.amazon.com/kinesis/) with SageMaker AI Feature Store.
- **Develop feature retrieval
mechanisms**. Create standardized ways to retrieve
features for both training and inference. For training
datasets, implement code that pulls features from the
offline store, while for inference, develop services that
query the online store. Verify that both paths use the same
feature definitions and transformations.
- **Integrate with ML
workflows**. Connect your feature store to your ML
pipelines by integrating it with
[SageMaker AI
Pipelines](https://aws.amazon.com/sagemaker/pipelines/) or your custom ML workflows. This makes
feature retrieval consistent throughout the ML lifecycle,
from experimentation to production deployment.
- **Monitor and validate
features**. Implement monitoring for your feature
store to detect data drift, missing values, or other quality
issues. Use
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) or custom validation scripts for
feature consistency and quality over time. Set up alerts for
deviations in feature distributions.
- **Enable feature discovery and
sharing**. Document your features with metadata and
descriptions to make them discoverable across your
organization. Integrate with data catalogs like
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) to enhance discoverability and
governance of features.

## Resources

**Related documents:**

- [Get
started with Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-getting-started.html)
- [Feature
Store concepts](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-concepts.html)
- [Store,
Discover, and Share Machine Learning Features with Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/)
- [Unlock
ML insights using the Amazon SageMaker AI Feature Store Feature
Processor](https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/)

**Related videos:**

- [Amazon SageMaker AI Feature Store: Store, discover, & share features
for ML apps](https://www.youtube.com/watch?v=pEg5c6d4etI)
- [Deep
dive on Amazon SageMaker AI Feature Store](https://www.youtube.com/watch?v=mHEUlPFT6xg)

**Related examples:**

- [Introduction
to Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html)
- [Amazon SageMaker AI Feature Store SageMaker AI Examples](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore)
- [Amazon SageMaker AI Feature Store: Streaming Aggregation](https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp02.html*

---

# MLREL03-BP03 Validate models with relevant data

Testing and validating machine learning models with appropriate data
is essential for reliable performance in production. Use real and
representative data that covers many possible patterns and scenarios
to avoid model failures when deployed in real-world environments.

**Desired outcome:** You establish
processes that validate your machine learning models with
real-world, representative data before deployment. You can identify
distribution mismatches between training, validation, test, and
inference data early, allowing you to address issues before they
impact production performance. Your validation approach includes
both real-world and engineered data to account for the scenarios
your model might encounter.

**Common anti-patterns:**

- Testing models with only synthetic data that doesn't represent
real-world conditions.
- Failing to check for distribution mismatch between training and
production data.
- Ignoring edge cases and rare scenarios in validation datasets.
- Using validation data that lacks diversity or has sampling
biases.
- Neglecting periodic revalidation after models are deployed.

**Benefits of establishing this best
practice:**

- Reduces risk of model failures in production environments.
- Enables early detection of data drift and model quality
degradation.
- Creates more robust models that perform well across expected
scenarios.
- Increases trust in model predictions from stakeholders.
- Improves alignment between model performance in testing and
production.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Validating your machine learning models with relevant data is a
critical step in the ML development lifecycle. Data that fails to
represent the full range of scenarios your model will encounter in
production can lead to poor performance, biased outputs, or
complete failures when deployed. The key challenge lies in
obtaining and using data that accurately mirrors your production
environment.

Begin by analyzing your data sources to capture the breadth and
depth of real-world scenarios. This includes common cases as well
as edge cases that might be rare but important. For example, a
model designed to detect fraudulent transactions needs exposure to
both typical and unusual fraud patterns. Missing these edge cases
can create vulnerabilities in your deployed model.

Pay particular attention to distribution mismatches, where the
statistical properties of your training, validation, test, and
eventual inference data differ. These mismatches often lead to
degraded model performance in production. For instance, if you
train a product recommendation model on data from one demographic
group but deploy it for a different group, the model may make
irrelevant recommendations.

Implement continuous monitoring after deployment to detect when
the data distribution shifts over time, which is common in
real-world applications. This allows you to retrain models before
performance degradation impacts business outcomes.

### Implementation steps

- **Establish data quality
criteria**. Define what constitutes representative
data for your use case. Include requirements for data
completeness, diversity, and coverage of edge cases.
Document these criteria as part of your ML development
process to create consistency across projects.
- **Implement cross-validation
techniques**. Use techniques like k-fold
cross-validation to verify that your model generalizes well
across different subsets of your data. This can identify
potential overfitting issues before deployment and provides
a more robust estimate of how your model will perform in
production.
- **Use Amazon SageMaker AI MLFlow
Tracking**. Set up experiments to track and compare
different training runs with various data configurations.
[SageMaker AI
MLFlow Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html) allows you to organize, monitor, and
evaluate your machine learning experiments systematically.
This can identify which data configurations lead to the best
performance and provides a historical record for future
reference.
- **Create engineered test
data**. Generate synthetic data to supplement
real-world data, especially for rare but important edge
cases. Verify that this synthetic data maintains the
statistical properties of real data while providing coverage
for scenarios that might be underrepresented in your
original dataset.
- **Implement data drift
detection**. Set up processes to continuously
compare the distribution of inference data with your
baseline training data. Use this comparison to identify when
the real-world data begins to diverge from what the model
was trained on, which can signal the need for retraining.
- **Use Amazon SageMaker AI Model
Monitor**. Deploy
[Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automatically track and analyze model
behavior in production. Configure alerts for deviations in
model quality, data quality, bias drift, and feature
attribution drift. SageMaker AI Model Monitor continuously
evaluates your deployed models and notifies you when action
is needed.
- **Establish a regular validation
cadence**. Schedule periodic evaluations of your
model using fresh data, even if drift hasn't been detected.
This can catch subtle changes that might not trigger
automated alerts but could still affect model performance
over time.
- **Document validation
results**. Create detailed reports of validation
processes and outcomes for each model version. Include
metrics on data representativeness, performance across
different data segments, and identified gaps or biases.

## Resources

**Related documents:**

- [Evaluating
ML Models](https://docs.aws.amazon.com/machine-learning/latest/dg/evaluating_models.html)
- [Cross-Validation](https://docs.aws.amazon.com/machine-learning/latest/dg/cross-validation.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/)
- [Detect
data drift using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/)
- [Monitoring
in-production ML models at large scale using Amazon SageMaker AI
Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/)

**Related videos:**

- [How
To Efficiently Manage ML experiments using Amazon SageMaker AI ML
Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k)
- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)

**Related examples:**

- [Amazon SageMaker AI Model Monitor](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp03.html*

---

# MLREL03-BP04 Establish data bias detection and mitigation

Detect and mitigate bias to avoid inaccurate model results.
Establish bias detection methodologies at data preparation stage
before training starts. Monitor, detect, and mitigate bias after the
model is in production. Establish feedback loops to track the drift
over time and initiate a re-training.

**Desired outcome:** You can identify
and address biases in your machine learning data and models,
providing fair and accurate predictions. You have established
systematic approaches for detecting bias before training and
continuously monitoring bias in production. Your AI systems produce
more reliable, fair, and trustworthy results through automated
detection and mitigation processes.

**Common anti-patterns:**

- Waiting until after model deployment to consider bias detection.
- Using a single bias metric for each use case without
understanding context-specific requirements.
- Focusing only on training data bias and ignoring bias that may
emerge in production.
- Failing to establish feedback mechanisms to monitor and address
drift over time.
- Treating bias detection as a one-time activity rather than an
ongoing process.

**Benefits of establishing this best
practice:**

- Improves model accuracy and fairness across different
demographic groups.
- Reduces risk of deploying models with harmful or discriminatory
outcomes.
- Enhances transparency and explainability for model predictions.
- Increases trust from users and stakeholders in AI systems.
- Improves adherence to emerging AI regulations and ethical
guidelines.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Bias in machine learning models can lead to unfair or inaccurate
outcomes that disproportionately impact certain groups. You need a
systematic approach to detect and mitigate bias throughout the
machine learning lifecycle. This begins with careful analysis of
your training data to identify potential imbalances or historical
biases that could be propagated by your models. By implementing
bias detection methodologies before training, you can address
issues early in the development process.

Once your models are in production, ongoing monitoring is
essential as new data patterns may introduce unexpected biases
over time. Setting up automated detection systems allows you to
continuously evaluate model fairness and take corrective actions
when necessary. Building feedback loops provides the data needed
to understand how bias manifests in real-world applications and
informs model retraining strategies.

Amazon SageMaker AI provides comprehensive tools like SageMaker AI
Clarify to implement bias detection and mitigation strategies
throughout the ML lifecycle. These tools offer quantitative
metrics to measure different types of bias and provide
explanations for model predictions to understand and address the
root causes of unfairness.

### Implementation steps

- **Understand different types of
bias**. Begin by educating your team about various
forms of bias that can affect machine learning models,
including selection bias, measurement bias, aggregation
bias, and evaluation bias. Educate your team members on how
bias can be introduced at different stages of the ML
lifecycle and the potential impacts on model predictions.
- **Analyze your training
data**. Use
[Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) to examine your training data for
potential bias before model development. Analyze the
distribution of sensitive attributes and identify imbalances
or correlations that could lead to unfair outcomes. Address
data imbalances through techniques like resampling,
weighting, or generating synthetic data for underrepresented
groups.
- **Select appropriate bias
metrics**. Choose bias metrics that align with your
specific use case and fairness requirements. SageMaker AI
Clarify provides multiple pre-training bias metrics
including class imbalance, difference in proportions of
labels, and conditional demographic disparity. For
post-training, metrics like disparate impact, difference in
positive proportions across predicted labels, and accuracy
difference can evaluate model fairness.
- **Run SageMaker AI Clarify processing
jobs**. Integrate
[SageMaker AI
Clarify processing jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html) into your ML pipeline to
analyze bias and provide explainability. Configure these
jobs to calculate bias metrics on your training data and
model predictions, identifying potential issues before
deployment.
- **Implement bias mitigation
strategies**. Address identified biases using
techniques like preprocessing (modifying training data),
in-processing (incorporating fairness constraints during
training), or post-processing (adjusting model outputs).
Experiment with different approaches and measure their
impact on both fairness metrics and model performance.
- **Set up production
monitoring**. Configure
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously track bias
metrics on production data. Create alerts that alarm when
bias metrics exceed predefined thresholds, enabling prompt
investigation and remediation of emerging issues.
- **Establish feedback loops**.
Implement mechanisms to collect and analyze feedback on
model predictions, particularly focusing on cases where bias
may be present. Use this feedback to improve your
understanding of real-world bias patterns and inform model
retraining strategies.
- **Generate model governance
reports**. Use SageMaker AI Clarify to create
comprehensive reports on model fairness and explainability
for stakeholders, including risk and compliance-aligned
teams and external regulators. These reports should document
your bias detection and mitigation efforts, providing
transparency into your responsible AI practices.
- **Conduct regular model
reviews**. Schedule periodic reviews of your
models' fairness performance, bringing together
cross-functional teams to evaluate bias metrics, examine
challenging cases, and decide on necessary interventions or
improvements.

## Resources

**Related documents:**

- [Run
SageMaker AI Clarify Processing Jobs for Bias Analysis and
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency
of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/)
- [Build
a secure enterprise machine learning platform on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.html)

**Related videos:**

- [Introducing
Amazon SageMaker AI Clarify, part 1 - Bias detection](https://www.youtube.com/watch?v=jvcPZmnXaxo)
- [Introducing
Amazon SageMaker AI Clarify, part 2 - Model explainability](https://www.youtube.com/watch?v=1IGMG_c280E)
- [Responsible
use of artificial intelligence and machine learning](https://pages.awscloud.com/Responsible-Use-of-Artificial-Intelligence-and-Machine-Learning_2022_1007-MCL_OD.html)

**Related examples:**

- [Amazon SageMaker AI Clarify: ML Bias Detection and Explainability](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify)
- [Amazon SageMaker AI Model Monitoring](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp04.html*

---
