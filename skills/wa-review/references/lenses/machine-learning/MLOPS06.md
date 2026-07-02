# MLOPS06 — Monitoring

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# MLOPS06-BP01 Synchronize architecture and configuration, and check for skew across environments

Synchronize your systems and configurations across development and
deployment phases for consistent machine learning model inference
results. By maintaining identical environments, you can avoid
discrepancies that arise from architectural differences, leading to
more reliable and predictable model performance.

**Desired outcome:** You have
established a systematic approach to foster architectural and
configuration consistency across development, staging, and
production environments for machine learning models. This includes
automated infrastructure deployment, continuous model quality
monitoring, and proactive detection of environmental skew. Your
machine learning systems deliver the same range of accuracy
regardless of which environment they run in, and you can quickly
identify and address deviations.

**Common anti-patterns:**

- Manually configuring each environment, leading to
inconsistencies.
- Neglecting to validate model performance across different
environments.
- Assuming model behavior will be identical across environments
without verification.
- Using different hardware specifications or software versions
between environments.
- Making changes only when needed to production environments
without documenting or replicating them in other environments.

**Benefits of establishing this best
practice:**

- Consistent model performance across environments.
- Reduced debugging time for environment-specific issues.
- Improved reliability of machine learning applications.
- Straightforward identification of the root causes of performance
deviations.
- Streamlined promotion process from development to production.
- Enhanced confidence in deployed models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Synchronizing your machine learning environments is critical for
checking that a model trained in one environment behaves the same
way when deployed in another. Differences in system architectures,
software dependencies, or configuration settings can cause
unexpected variations in model performance, leading to inaccurate
predictions or even system failures.

By treating your infrastructure as code and implementing automated
monitoring, you can maintain consistency across environments and
quickly detect deviations. This approach allows you to focus on
improving your models rather than debugging environment-specific
issues. It also provides a reliable foundation for continuous
delivery of machine learning solutions.

Environmental skew can occur in various ways, such as through
differences in hardware capabilities, software versions, or system
configurations. For example, a model trained on a development
environment with specific CPU architecture might behave
differently when deployed to a production environment with
different specifications. Similarly, differences in underlying
libraries or dependencies can lead to subtle variations in model
behavior.

Regular validation of model performance across environments should
be part of your standard promotion process. This includes
comparing not only the accuracy metrics but also the distribution
of predictions and the model's behavior for edge cases.

### Implementation steps

- **Define infrastructure as code using
AWS CloudFormation**. Create CloudFormation
templates that define resources, configurations, and
dependencies for your machine learning environments. With
this strategy, each environment is provisioned consistently
and can be recreated identically when needed. Include
compute resources, networking configurations, security
settings, and machine learning-specific components.
- **Implement version control for
infrastructure templates**. Store your
CloudFormation templates in a version control system like
AWS CodeCommit or GitHub. This allows you to track changes
over time, roll back to previous configurations if needed,
and verify that your environments are using the same version
of the infrastructure definition.
- **Set up CI/CD pipelines for
infrastructure deployment**. Use AWS CodePipeline
or AWS CodeBuild to automate the deployment of your
infrastructure changes across environments. This reduces
manual intervention and the potential for human error when
updating environments.
- **Configure Amazon SageMaker AI Model
Monitor for continuous quality evaluation**. Set up
Model Monitor to automatically track the quality of your
models in production and compare the results with the
baseline established during training. This can identify when
model performance starts to drift due to environmental
factors or data changes.
- **Implement data quality
monitoring**. Use SageMaker AI Model Monitor's data
quality monitoring capability to detect changes in the
statistical properties of your input data across
environments. This capability provides similar input
distributions to your models regardless of environment.
- **Set up model quality
monitoring**. Configure SageMaker AI Model Monitor to
track model quality metrics such as accuracy, precision, and
recall over time. Compare these metrics between your
development, staging, and production environments to detect
inconsistencies.
- **Enable bias drift
monitoring**. Use SageMaker AI Model Monitor's bias
drift monitoring to detect if your models exhibit different
biases in different environments, which could indicate
environment-specific issues.
- **Configure alerts for
deviations**. Set up Amazon CloudWatch alarms to
notify you when SageMaker AI Model Monitor detects significant
deviations in model performance or data characteristics
across environments. This allows for proactive intervention
before small issues become major problems.
- **Establish a promotion
checklist**. Create a formal checklist that
includes verifying model performance consistency across
environments before promoting a model to the next stage.
Document the acceptable thresholds for performance
differences between environments.
- **Implement regular cross-environment
validation**. Schedule periodic validation of model
performance across your environments, even when no changes
are being made. Use this validation to catch gradual drift
that might occur due to external factors.
- **Create environment comparison
dashboards**. Use
[Quick with GenBI capabilities](https://aws.amazon.com/quicksight/generative-bi/) to automatically
generate visualizations and dashboards for model performance
metrics across different environments, making it more
straightforward to spot discrepancies and track trends over
time.
- **Utilize foundation models for
anomaly detection**. Implement
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) or
[SageMaker AI
JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) with expanded library of foundation models
to analyze performance patterns and identify anomalous
behavior that might indicate environmental inconsistencies,
especially for complex ML systems where traditional
monitoring might miss subtle differences.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [What
is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [What
is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [Detect
unmanaged configuration changes to stacks and resources with
drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [Amazon SageMaker AI best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html)

**Related examples:**

- [Introduction
to Amazon SageMaker AI Model Monitor](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.html)
- [Model
Monitor Visualization](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/visualization/SageMaker AI-Model-Monitor-Visualize.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops06-bp01.html*

---

# MLOPS06-BP02 Enable model observability and tracking

Establish model monitoring mechanisms to identify and proactively
avoid inference issues. ML models can degrade in performance over
time due to drifts. Monitor metrics that are attributed to your
model's performance. For real time inference endpoints, measure the
operational health of the underlying compute resources hosting the
endpoint and the health of endpoint responses. Establish lineage to
trace hosted models back to versioned inputs and model artifacts for
analysis.

**Desired outcome:** You can
continuously monitor your machine learning models in production to
detect and avoid performance degradation over time. You have
mechanisms in place to track model lineage, identify various types
of drift, and receive alerts when models deviate from expected
behavior. Your monitoring solution provides clear visibility into
both the technical health of model endpoints and the business
performance of the models themselves, enabling you to maintain
high-quality predictions and make informed decisions about model
updates.

**Common anti-patterns:**

- Deploying models without monitoring capabilities.
- Failing to establish model lineage tracking for audit and
governance.
- Not monitoring for data drift or concept drift in production
models.
- Ignoring model bias and fairness considerations after
deployment.
- Lacking documentation of model information and performance
metrics.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation.
- Improved model governance and adherence through comprehensive
documentation.
- Enhanced ability to explain model predictions and address bias
concerns.
- Reduced operational risk through proactive monitoring of model
health.
- Streamlined model updates and improvements based on real-world
performance data.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model observability is critical for maintaining the reliability,
fairness, and performance of machine learning systems in
production. Without proper monitoring mechanisms, ML models can
silently degrade over time as the data they process begins to
differ from the data they were trained on, a phenomenon known as
drift.

You need to implement comprehensive monitoring across several
dimensions: data quality to check that inputs remain consistent
with training data, model quality to track performance metrics,
bias detection to verify fairness, and explainability to
understand model decisions. Additionally, model lineage tracking
can trace issues back to specific model versions, training
datasets, and hyperparameters.

Amazon SageMaker AI provides integrated tools that make implementing
these monitoring capabilities straightforward. SageMaker AI Model
Monitor can automatically detect deviations in your model's data
and performance characteristics, while SageMaker AI Clarify
identifies bias and explains predictions. By setting up proper
alerts, you can be notified when issues arise and take corrective
action before they impact your business.

Documentation is equally important for model governance. SageMaker AI
Model Cards provide a centralized location to store important
model information, including performance metrics, intended use
cases, and potential limitations.

### Implementation steps

- **Set up Amazon SageMaker AI Model
Monitor**. Configure
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automatically monitor the
quality of your ML models in production. Create baseline
statistics and constraints during model training, then
monitor for deviations in production data. Set up the
following types of monitoring:

Data quality monitoring to detect changes in data
distributions
- Model quality monitoring to track accuracy and other
performance metrics
- Bias drift monitoring to detect changes in model
fairness
- Feature attribution drift monitoring to track changes in
feature importance

- **Integrate with Amazon CloudWatch**. SageMaker AI Model Monitor automatically
sends metrics to
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), allowing you to track usage statistics
for your ML models. Set up CloudWatch dashboards to
visualize key metrics and create alarms that go off when
metrics exceed predefined thresholds. Configure
notifications through Amazon SNS to alert relevant teams
when issues are detected.
- **Implement SageMaker AI Model
Dashboard**. Use the
[SageMaker AI
Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html) to gain a centralized view of your
models. From the SageMaker AI console, you can search, view,
and explore your models in one place. Set up monitors to
track the performance of models deployed on real-time
inference endpoints and identify models that violate
thresholds for data quality, model quality, bias, and
explainability.
- **Enable bias detection with SageMaker AI
Clarify**. Deploy
[SageMaker AI
Clarify](https://aws.amazon.com/sagemaker/clarify/) to identify various types of bias that can
emerge during model training or when the model is in
production. Configure both pre-training and post-training
bias metrics to understand how your model's predictions
affect different segments of your user base. Use Clarify's
monitoring capabilities to detect bias drift in production
models.
- **Implement model
explainability**. Configure SageMaker AI Clarify's
feature attribution capabilities to explain how your models
make predictions. This builds trust with stakeholders and
can identify potential issues with model logic. Set up
monitoring to detect when feature attribution patterns drift
from baseline, which could indicate underlying problems with
the model.
- **Establish ML lineage
tracking**. Implement
[SageMaker AI
ML Lineage Tracking](https://sagemaker.readthedocs.io/en/v2.77.0/workflows/lineage/) to create and store information
about each step in your machine learning workflow, from data
preparation to model deployment. This creates a running
history of your ML experiments and establishes model
governance by tracking model lineage artifacts for auditing
and adherence verification.
- **Create Model Cards for
documentation**. Use
[Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) with enhanced documentation and
governance capabilities to document critical information
about your models in a single location. Include business
requirements, key decisions, observations during
development, performance goals, risk ratings, and evaluation
results. This streamlines documentation throughout a model's
lifecycle and supports approval workflows, registration, and
audits.
- **Implement shadow testing for model
validation**. Before deploying new model versions
to production, use
[Amazon SageMaker AI Shadow Testing](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html) to compare the performance
of new models against production models using real-world
inference request data. Configure SageMaker AI to route copies
of production inference requests to the new model variant
and generate dashboards displaying performance differences
across key metrics in real-time.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html)
- [Shadow
tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)
- [Lineage
Tracking Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html)
- [Using
CloudWatch outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Monitoring
Amazon ML with Amazon CloudWatch Metrics](https://docs.aws.amazon.com/machine-learning/latest/dg/cw-doc.html)
- [New
for Amazon SageMaker AI – Perform Shadow Tests to Compare
Inference Performance Between ML Model Variants](https://aws.amazon.com/blogs/aws/new-for-amazon-sagemaker-perform-shadow-tests-to-compare-inference-performance-between-ml-model-variants/)
- [Integrate
Amazon SageMaker AI Model Cards with the model registr](https://aws.amazon.com/blogs/machine-learning/integrate-amazon-sagemaker-model-cards-with-the-model-registry/)
- [Improve
governance of your machine learning models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/improve-governance-of-your-machine-learning-models-with-amazon-sagemaker/)

**Related examples:**

- [Monitoring
bias drift and feature attribution drift with Amazon SageMaker AI
Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/fairness_and_explainability/SageMaker AI-Model-Monitor-Fairness-and-Explainability.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops06-bp02.html*

---
