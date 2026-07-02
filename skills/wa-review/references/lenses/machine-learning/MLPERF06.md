# MLPERF06 — Monitoring

**Pillar**: Performance Efficiency  
**Best Practices**: 6

---

# MLPERF06-BP01 Include human-in-the-loop monitoring

Including human-in-the-loop monitoring is an effective method for
efficiently tracking and maintaining model performance. By
incorporating human review into automated decision processes,
organizations can establish a reliable quality assurance mechanism
that validates model inferences and detects performance degradation
over time.

**Desired outcome:** You implement a
robust human-in-the-loop monitoring system that enables continuous
assessment of your machine learning models. You can compare human
labels with model inferences to detect model drift and performance
degradation, allowing timely mitigation through retraining or other
remediation actions. This creates a feedback loop that maintains
high model quality and reliability in production environments.

**Common anti-patterns:**

- Relying solely on automated metrics without human validation.
- Ignoring edge cases and low-confidence predictions.
- Not establishing a systematic review process for model outputs.
- Failing to incorporate human feedback into model retraining
cycles.
- Using untrained reviewers without subject matter expertise.

**Benefits of establishing this best
practice:**

- Early detection of model drift and performance degradation.
- Higher quality assurance for critical model predictions.
- Better understanding of edge cases and model limitations.
- Continuous improvement of model performance through expert
feedback.
- Increased trust in AI systems through human oversight.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Human-in-the-loop monitoring provides a crucial safety net for
your machine learning systems by adding appropriate human
oversight to important decisions. This approach is particularly
valuable when automated systems make predictions that impact
critical business processes or customer experiences. By
establishing a workflow where human experts review model outputs,
particularly those with low confidence or selected randomly for
quality assurance, you create a reliable mechanism to evaluate
model performance in real-world scenarios.

Avoid relying solely on automated metrics without human
validation. Many organizations ignore edge cases and
low-confidence predictions, don't establish a systematic review
process for model outputs, fail to incorporate human feedback into
model retraining cycles, and use untrained reviewers without
subject matter expertise.

This monitoring approach can identify when models begin to drift
or perform poorly on new data. The comparison between human labels
and model predictions serves as a key indicator of model health,
signaling when retraining or other interventions are necessary.
This feedback loop is essential for maintaining high-quality,
reliable AI systems over time.

### Implementation steps

- **Design a quality assurance system
for model inferences**. Create a comprehensive plan
for how human review will integrate with your machine
learning workflow. Determine which predictions will be sent
for human review (low-confidence predictions, random
samples, or high-risk categories) and establish clear
guidelines for reviewers to follow when evaluating model
outputs.
- **Establish a team of subject matter
experts**. Identify and recruit individuals with
domain expertise who can accurately evaluate model
inferences. These reviewers should understand both the
technical aspects of your models and the business context in
which they operate, allowing them to provide valuable
feedback on model performance and identify potential issues.
- **Implement Amazon Augmented AI for
human review workflows**. Use
[Amazon
Augmented AI](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html) (Amazon A2I) to create and manage human
review workflows for your machine learning models. Amazon
A2I integrates with other AWS services like
[IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html),
[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html), and
[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to handle the entire review process.
- **Configure review criteria and
thresholds**. Define the conditions that initiate
human review, such as confidence score thresholds or types
of predictions that require human validation. Set up rules
in Amazon A2I to automatically route these cases to your
human reviewers while allowing high-confidence, routine
predictions to proceed without review.
- **Develop feedback integration
mechanisms**. Create systems to incorporate human
feedback into your model improvement cycle. This includes
storing human labels alongside model predictions, analyzing
disagreement patterns, and using this information to
identify areas where your model needs improvement.
- **Monitor and analyze human-model
agreement rates**. Track how often human reviewers
agree with model predictions and analyze patterns in
disagreements. This data can identify systematic issues with
your model so that you can prioritize areas for improvement.
- **Implement model retraining based on
feedback**. Use the labeled data gathered through
human review to periodically retrain your models. This
creates a continuous improvement loop where your models
learn from past mistakes and adapt to changing patterns in
your data.
- **Measure and optimize
cost-effectiveness**. Analyze the ROI of your
human-in-the-loop system by comparing the costs of human
review with the benefits of improved model accuracy. Adjust
your review sampling strategy to focus human attention where
it provides the most value.

## Resources

**Related documents:**

- [Using
Amazon Augmented AI for Human Review](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Customized
model monitoring for near real-time batch inference with
Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/customized-model-monitoring-for-near-real-time-batch-inference-with-amazon-sagemaker/)-
- [Human-in-the-loop
review of model explanations with Amazon SageMaker AI Clarify and
Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/)

**Related videos:**

- [Easily
Implement Human in the Loop into Your Machine Learning
Predictions with Amazon A2I](https://www.youtube.com/watch?v=jNUp1SO_0YU)
- [Accelerate
foundation model evaluation with Amazon SageMaker AI
Clarify](https://www.youtube.com/watch?v=9X2oDkOBYyA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf06-bp01.html*

---

# MLPERF06-BP02 Evaluate model explainability

Model explainability allows you to understand and interpret how your
machine learning models arrive at their decisions. By evaluating
model explainability, you gain insights into the factors that
influence predictions to build trustworthy AI systems that meet
business requirements and regulatory standards.

**Desired outcome:** You can
demonstrate why your machine learning models make predictions, which
enables you to build trust with stakeholders, adhere to regulatory
requirements, and identify potential biases in model outcomes. You
have the tools to balance model complexity with explainability based
on your business needs and can produce documentation that satisfies
governance requirements.

**Common anti-patterns:**

- Treating machine learning models as unknown without
understanding their decision-making process.
- Ignoring explainability requirements until after model
deployment.
- Prioritizing model performance metrics over interpretability
when business or regulations requires explainability.
- Failing to document model explanations for regulatory adherence.
- Using complex models when simpler, more interpretable
alternatives would meet business requirements.

**Benefits of establishing this best
practice:**

- Increased trust from stakeholders and end-users in AI systems.
- Improves adherence with regulations requiring transparent AI
decision-making.
- Ability to detect and mitigate biases in model predictions.
- Enhanced model debugging and performance improvement.
- Better alignment between model behavior and business objectives.
- More effective model governance and risk management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model explainability is a critical aspect of responsible AI
development. When you evaluate explainability, you assess how
transparently your machine learning models make decisions and
whether those decisions can be explained to stakeholders,
regulators, and end-users. This transparency is particularly
important in regulated industries and for applications where
decisions impact individuals.

Avoid treating machine learning models as opaque without
understanding their decision-making process. Many organizations
ignore explainability requirements until after model deployment,
prioritize model performance metrics over interpretability when
business or regulatory requirements demand explainability, and
fail to document model explanations for regulatory adherence.

The trade-off between model complexity and explainability is a key
consideration. Complex models like deep neural networks may
deliver higher accuracy but are often harder to interpret. Simpler
models like decision trees or linear regression provide more
straightforward explanations but might sacrifice some performance.
Your choice should be guided by your business context, including
regulatory requirements and the importance of building trust with
end-users.

For example, a credit approval system may require clear
explanations for why applications are denied, while a
manufacturing quality control system might prioritize accuracy
over explainability. By evaluating these requirements early, you
can select appropriate modeling approaches and develop the right
metrics for assessing both performance and interpretability.

### Implementation steps

- **Assess explainability
requirements**. Begin by understanding the business
and compliance-aligned needs that drive your explainability
requirements. Consider regulatory constraints (like GDPR,
which includes a right to explanation), business
transparency goals, and stakeholder expectations. Document
these requirements clearly and prioritize them based on
their importance to your use case.
- **Select appropriate model
types**. Choose model architectures that align with
your explainability needs. If high explainability is
required, consider inherently interpretable models like
decision trees, rule-based systems, or linear models. For
applications where performance takes priority, more complex
models with post-hoc explanation techniques may be
appropriate.
- **Implement Amazon SageMaker AI
Clarify**.
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html) provides tools to explain model
predictions using feature attribution methods. It can
identify which features contribute most to a prediction,
enabling you to understand and communicate model behavior.
SageMaker AI Clarify supports various model types and
integrates seamlessly with the SageMaker AI environment.
- **Apply feature attribution
techniques**. Use feature attribution methods like
[SHAP
(SHapley Additive exPlanations) values](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-shapley-values.html) through
SageMaker AI Clarify to quantify the contribution of each
feature to individual predictions. These techniques explain
both global model behavior (which features are most
important overall) and local explanations (why a prediction
was made).
- **Establish explainability
metrics**. Define quantitative metrics to assess
model explainability, such as feature importance stability,
explanation fidelity, or consistency. Use these metrics to
objectively evaluate explainability alongside traditional
performance metrics like accuracy or F1 score. Include these
metrics in your model evaluation framework and monitoring
systems.
- **Create model
documentation**. Develop comprehensive
documentation that describes how your model works, what
features influence its decisions, and how explanations are
generated. This documentation should be understandable by
both technical and non-technical stakeholders. SageMaker AI
Clarify can generate reports that contribute to model
governance documentation.
- **Implement bias detection**.
Use
[SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) to detect potential bias in your models
during development and production. Configure the appropriate
bias metrics based on your use case and sensitive
attributes. Regularly assess these metrics to verify that
your model remains fair across different demographic groups.
- **Set up continuous
monitoring**. Configure SageMaker AI Clarify to
monitor production inferences for bias or feature
attribution drift. This allows you to detect when model
explanations change over time, which might indicate problems
with the model or changes in the underlying data. Establish
alerts for shifts in explanations or bias metrics.
- **Integrate human review
processes**. For high-stakes decisions, implement
human-in-the-loop review of model explanations using Amazon SageMaker AI Clarify in combination with
[Amazon
Augmented AI (A2I)](https://aws.amazon.com/augmented-ai/). This provides an additional layer
of oversight and can build confidence in the model's
decisions.

## Resources

**Related documents:**

- [Model
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)
- [Feature
Attributions that Use Shapley Values](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-shapley-values.html)
- [Run
SageMaker AI Clarify Processing Jobs for Bias Analysis and
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [ML
model explainability with Amazon SageMaker AI Clarify and the
SKLearn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/)
- [Human-in-the-loop
review of model explanations with Amazon SageMaker AI Clarify and
Amazon A2I](https://aws.amazon.com/blogs/machine-learning/human-in-the-loop-review-of-model-explanations-with-amazon-sagemaker-clarify-and-amazon-a2i/)

**Related examples:**

- [Fairness
and Explainability with SageMaker AI Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-experiments/sagemaker_clarify_integration/tracking_bias_explainability.html)
- [Explainability
with Amazon SageMaker AI Debugger](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-debugger/xgboost_census_explanations/xgboost-census-debugger-rules.html)
- [Amazon SageMaker AI Clarify Processing GitHub Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf06-bp02.html*

---

# MLPERF06-BP03 Evaluate data drift

Data drift can impact the performance of your machine learning
models, leading to inaccurate predictions and diminished business
value. By implementing effective monitoring and detection
strategies, you can identify when your models are no longer
performing optimally due to changes in the underlying data patterns.

**Desired outcome:** You can detect
and mitigate data drift in your machine learning models, providing
continued accuracy and reliability over time. By implementing model
monitoring capabilities, you gain visibility into changes in data
distributions and model performance, allowing for timely
interventions and retraining when necessary.

**Common anti-patterns:**

- Deploying models without drift monitoring mechanisms.
- Ignoring gradual changes in input data distribution until model
performance deteriorates.
- Assuming that a model trained on historical data will remain
accurate indefinitely.
- Manually checking model performance at arbitrary intervals
rather than implementing continuous monitoring.
- Retraining models on fixed schedules without considering actual
data drift patterns.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation before it
impacts business outcomes.
- Increased trust in ML model predictions through continuous
quality assurance.
- Improved model lifecycle management with data-driven retraining
decisions.
- Reduced operational risks associated with inaccurate
predictions.
- Enhanced ability to detect and mitigate bias in ML models over
time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data drift occurs when the statistical properties of model inputs
change over time, causing discrepancies between training data and
production data. This can happen gradually due to evolving user
behaviors, market conditions, or abrupt changes like economic
shifts. When your model encounters data drift, it's essentially
making predictions on data distributions it wasn't trained on,
which can lead to decreased accuracy and potentially harmful
business decisions.

Avoid deploying models without drift monitoring mechanisms. Many
organizations ignore gradual changes in input data distribution
until model performance deteriorates, assume that a model trained
on historical data will remain accurate indefinitely, and manually
check model performance at arbitrary intervals rather than
implementing continuous monitoring.

Implementing a robust data drift monitoring strategy assists you
in maintaining high-performing models by identifying when
retraining becomes necessary. Rather than retraining models on
arbitrary schedules, you can make data-driven decisions based on
actual changes in your data distributions and model performance
metrics. This approach verifies that you're optimizing both model
performance and resource utilization.

Amazon SageMaker AI provides comprehensive tools to monitor your ML
models in production environments, allowing you to detect data
drift, concept drift, and bias. By setting up automated monitoring
pipelines, you can receive alerts when your models require
attention, enabling proactive management of your ML systems.

### Implementation steps

- **Set up baseline data for
monitoring**. Establish a reference dataset that
represents your model's expected input and output
distributions. This baseline will be used to compare against
your production data to detect drift. Use the training data
or a representative subset that performed well during model
validation.
- **Configure SageMaker AI Model
Monitor**. Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automatically detect
deviations in your model's data quality and performance
metrics. SageMaker AI Model Monitor can be set up to run on a
schedule, analyzing incoming production data and comparing
it to your baseline.
- **Define data quality and drift
metrics**. Determine which statistical metrics are
most relevant for detecting drift in your use case.
SageMaker AI Model Monitor supports various statistical
measures like KL divergence, Jensen-Shannon divergence, and
population stability index to quantify differences between
distributions.
- **Establish threshold
values**. Set appropriate threshold values for your
metrics that, when exceeded, will initiate alerts. These
thresholds should balance sensitivity to meaningful changes
while avoiding false alarms from minor variations.
- **Create automated monitoring
schedules**. Configure SageMaker AI Model Monitor to
run analysis jobs at regular intervals that match your
business requirements. For critical models, consider more
frequent monitoring schedules.
- **Implement bias detection**.
Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html) to detect bias in your ML models
both pre-training and during production. SageMaker AI Clarify
can identify if your model is developing biases over time as
the data distribution changes.
- **Set up alert mechanisms**.
Configure Amazon CloudWatch alarms to notify appropriate
stakeholders when data drift exceeds your defined
thresholds. Integrate these alerts with your team's
communication tools for timely responses.
- **Develop a retraining
strategy**. Establish clear criteria for when to
retrain models based on drift detection results. This should
include considerations for data collection, feature
engineering updates, and model revalidation.
- **Implement automated retraining
pipelines**. Create SageMaker AI pipelines that can be
run automatically when drift exceeds critical thresholds,
streamlining the retraining process and minimizing the time
models operate with degraded performance.
- **Document drift patterns and
interventions**. Maintain records of detected drift
incidents, their causes, and the effectiveness of
interventions. This documentation builds institutional
knowledge that can improve future model development and
monitoring strategies.

## Resources

**Related documents:**

- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Model
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)
- [Detecting
bias after training](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-post-training-bias.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency
of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/)
- [Detecting
data drift using Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/)

**Related videos:**

- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)

**Related examples:**

- [Amazon SageMaker AI Clarify](https://github.com/aws/amazon-sagemaker-clarify)
- [Amazon SageMaker AI Model Monitor examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf06-bp03.html*

---

# MLPERF06-BP04 Monitor, detect, and handle model performance degradation

Model performance could degrade over time for reasons such as data
quality, model quality, model bias, and model explainability.
Continuously monitor the quality of the ML model in real time.
Identify the right time and frequency to retrain and update the
model. Configure alerts to notify and initiate actions if a drift in
model performance is observed.

**Desired outcome:** You establish a
comprehensive monitoring system for your machine learning models
that detects performance degradation, alerts relevant stakeholders,
and takes appropriate remediation actions. Your ML systems maintain
high accuracy and reliability over time through automated
monitoring, detection, and handling of performance issues.

**Common anti-patterns:**

- Implementing ML models without ongoing monitoring.
- Relying solely on periodic manual checks of model performance.
- Ignoring data drift or concept drift until model performance
severely degrades.
- Not having an established retraining strategy or schedule.
- Missing alert systems for model performance degradation.

**Benefits of establishing this best
practice:**

- Early detection of model performance issues.
- Automated notifications when models start to degrade.
- Improved model reliability and accuracy over time.
- Reduced operational risk from poor model predictions.
- Better understanding of model behavior in production
environments.
- Increased trust in ML-powered systems.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model performance monitoring is critical for maintaining reliable
machine learning systems in production environments. As real-world
data changes over time, models can experience data drift (changes
in the distribution of input data) or concept drift (changes in
the relationship between inputs and target variables). Establish a
robust monitoring framework to detect these issues early and take
appropriate action.

Avoid implementing ML models without ongoing monitoring. Many
organizations rely solely on periodic manual checks of model
performance, ignore data drift or concept drift until model
performance severely degrades, don't have an established
retraining strategy or schedule, and miss alert systems for model
performance degradation.

When implementing model monitoring, you should establish baseline
performance metrics during the training and validation phases.
These baselines serve as the foundation for comparison once the
model is deployed. Monitor not just accuracy metrics, but also
data statistics, feature distributions, and prediction patterns to
identify subtle changes that might indicate underlying problems.

Setting up automated alerts notifies your team when key
performance indicators fall below acceptable thresholds. These
alerts should be configured with appropriate severity levels to
reflect the business impact of model degradation. Additionally,
implement automated scaling to handle varying workloads
efficiently, which keeps your model endpoints responsive
regardless of demand.

### Implementation steps

- **Monitor model
performance**.
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) continually monitors the
quality of Amazon SageMaker AI machine learning models in
production. Establish a baseline during training before
model is in production. Collect data while in production and
compare changes in model inferences. Observations of drifts
in the data statistics will indicate that the model may need
to be retrained. Use
[SageMaker AI
Clarify](https://aws.amazon.com/sagemaker/clarify/) to identify model bias. Configure alerting
systems with
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to send notifications for unexpected bias
or changes in data quality.
- **Perform automatic
scaling**. Amazon SageMaker AI includes automatic
scaling capabilities for your hosted model to dynamically
adjust underlying compute supporting an endpoint based on
demand. This capability verifies that that your endpoint can
dynamically support demand while reducing operational
overhead.
- **Monitor endpoint metrics**.
Amazon SageMaker AI also outputs endpoint metrics for
monitoring the usage and health of the endpoint. Amazon SageMaker AI Model Monitor provides the capability to monitor
your ML models in production and provides alerts when data
quality issues appear. For enhanced observability, leverage
one-click metrics and monitoring for HyperPod training jobs,
deployments, health, resource usage, and historical job
traces to drive faster debugging and operational excellence
in foundation model workflows. Create a mechanism to
aggregate and analyze model prediction endpoint metrics
using services, such as
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/). OpenSearch Service supports
[dashboards](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/dashboards.html)
for visualization. Consider integrating third-party AI tools
(Comet, Deepchecks, Fiddler AI, Lakera) for extended
governance, bias detection, explainable AI, and vertical
solutions. The traceability of hosting metrics back to
versioned inputs allows for analysis of changes that could
be impacting current operational performance.
- **Establish data quality
monitoring**. Configure SageMaker AI Model Monitor to
track data quality metrics such as missing values,
statistical outliers, and feature distribution shifts. Set
up constraints that define acceptable ranges for these
metrics and generate alerts when violations occur.
- **Implement bias detection and
tracking**. Use SageMaker AI Clarify to detect bias in
your model predictions over time. Monitor for changes in
fairness metrics across different segments of your data and
create visualizations to track these metrics over time.
- **Set up model explainability
analysis**. Deploy SageMaker AI Clarify to track
feature importance and SHAP values over time. These values
can determine if the model's decision-making process is
changing in unexpected ways that might indicate performance
issues.
- **Create a retraining
pipeline**. Develop an automated pipeline that can
retrain your models when performance degradation is
detected. Use
[AWS Step Functions](https://aws.amazon.com/step-functions/) to orchestrate the retraining
workflow, including data preparation, model training,
evaluation, and deployment.
- **Implement A/B testing for model
updates**. When deploying updated models, use
SageMaker AI's
[production
variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html) to perform A/B testing between the current
and new model versions. This allows you to validate
performance improvements before fully replacing the existing
model.

## Resources

**Related documents:**

- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness
and Explainability with SageMaker AI Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.html)
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/)
- [Monitoring
in-production ML models at large scale using Amazon SageMaker AI
Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/)
- [ML
model explainability with Amazon SageMaker AI Clarify and the
SKLearn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/)

**Related videos:**

- [Understand
ML model predictions & biases with Amazon SageMaker AI
Clarify](https://www.youtube.com/watch?v=t2SJTYiTnYM)
- [Deep
Dive on Amazon SageMaker AI Debugger & Amazon SageMaker AI Model
Monitor](https://www.youtube.com/watch?v=0zqoeZxakOI)
- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)

**Related examples:**

- [Amazon SageMaker AI Model Monitor Examples - Github](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)
- [SageMaker AI
Clarify Examples - Github](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf06-bp04.html*

---

# MLPERF06-BP05 Establish an automated re-training framework

Monitor data and model predictions to identify errors due to data
and concept drift. By implementing automated model re-training at
scheduled intervals or when performance metrics reach defined
thresholds, you can maintain model accuracy and effectiveness over
time. This approach keeps your machine learning models relevant as
data patterns evolve.

**Desired outcome:** You can detect
when your deployed ML models experience data drift or performance
degradation, and automatically run retraining processes. You
establish mechanisms to monitor data statistics and ML inferences in
production, allowing you to maintain high-quality predictions
without manual intervention. Your models are consistently updated
with new data, and model versions are properly tracked to maintain
traceability and reproducibility.

**Common anti-patterns:**

- Waiting for model performance to fail catastrophically before
initiating retraining.
- Manually monitoring model performance without automated alerts
or prompts.
- Retraining on a fixed schedule regardless of model performance
or data patterns.
- Lacking proper version control for retrained models.
- Not maintaining consistent evaluation metrics across model
versions.

**Benefits of establishing this best
practice:**

- Maintains model accuracy and relevance as data patterns evolve.
- Reduces manual intervention required to keep models performing
optimally.
- Enables quick response to data drift and concept drift.
- Creates a documented, repeatable process for model updates.
- Provides consistent model quality through automated evaluation.
- Maximizes return on investment for machine learning solutions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establishing an automated retraining framework is crucial for
maintaining ML model performance over time. As new data becomes
available or as the underlying patterns in your data change, your
models can drift and become less accurate. By implementing a
systematic approach to model monitoring and retraining, you can
verify that your ML solutions continue to deliver business value.

Avoid waiting for model performance to fail catastrophically
before initiating retraining. Many organizations manually monitor
model performance without automated alerts or prompts, retrain on
a fixed schedule regardless of model performance or data patterns,
lack proper version control for retrained models, and don't
maintain consistent evaluation metrics across model versions.

Start by defining clear performance metrics for your models that
align with your business objectives. These metrics should be
continuously monitored in production to detect performance
degradation. Additionally, monitor your input data for statistical
changes that may indicate drift from the training distribution.
When changes are detected, your automated framework should run
retraining workflows.

The process should include data preparation, model training with
both existing and new data, thorough evaluation, and controlled
deployment. Each retrained model should be versioned appropriately
to maintain traceability and allow for rollback if needed.

### Implementation steps

- **Define model performance
metrics**. Establish clear metrics that measure how
well your model is performing relative to business
objectives. These could include accuracy, precision, recall,
F1 score, or custom domain-specific metrics. Verify that
these metrics can be calculated automatically and regularly
in your production environment.
- **Configure monitoring
systems**. Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously monitor the
quality of your ML models in production. Set up data quality
monitoring to detect drift in input features, model quality
monitoring to track prediction quality, bias drift
monitoring to detect changes in fairness metrics, and
feature attribution drift to identify changes in feature
importance.
- **Establish retraining
prompts**. Define the conditions that will initiate
model retraining. These can include scheduled intervals
based on business requirements, performance degradation
beyond defined thresholds, detection of data drift above
acceptable limits, and availability of new training data.
Set up
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alerts to notify or automatically run
retraining workflows.
- **Design retraining
pipelines**. Create automated pipelines using
[Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) that handle the entire retraining
workflow, including data preparation, feature engineering,
model training, evaluation, and deployment. For large-scale
foundation model training or distributed workloads, leverage
[Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) which provides managed, resilient
high-performance clusters with automatic health checks and
PyTorch auto-resume capabilities for long-running training
jobs. In your pipeline, include steps for validation against
holdout data before deployment.
- **Implement model
versioning**. Use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to track and manage
different versions of your models. As a result, you can
recreate a model version if needed and provide traceability
for your deployed models. Associate metadata with each
version to document training data, hyperparameters, and
performance metrics.
- **Automate data processing for new
training data**. Set up automated data processing
workflows that prepare new data for training. Configure
[Amazon S3](https://aws.amazon.com/s3/) event notifications to run Lambda functions or

[AWS Step Functions](https://aws.amazon.com/step-functions/) workflows when new data becomes
available. Use

[Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to manage features
consistently across training and inference.
- **Set up orchestration**. Use
[AWS Step Functions Data Science SDK for SageMaker AI](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-python-sdk.html) to
orchestrate complex ML workflows. Define each step in the
workflow and configure alerts to initiate the process. For
detecting new training data, combine
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) with Amazon CloudWatch Events to
automatically start Step Function workflows.
- **Implement deployment
safeguards**. Use deployment techniques like
blue-green deployment or canary releases to safely
transition to new model versions. Monitor the performance of
new models closely during initial deployment and configure
automatic rollback if performance degrades.
- **Create feedback loops**.
Establish mechanisms to collect ground truth data from
production to continually evaluate and improve your models.
This might involve user feedback, delayed outcomes, or
manual labeling processes for a subset of predictions.
- **Document the retraining
process**. Create comprehensive documentation for
your retraining framework, including prompts, pipelines,
evaluation criteria, and deployment strategies. This process
fosters knowledge transfer and consistent application of the
process.

## Resources

**Related documents:**

- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Retraining
Models on New Data](https://docs.aws.amazon.com/machine-learning/latest/dg/retraining-models-on-new-data.html)
- [Data
and model quality monitoring with SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Train
a Machine Learning Model (using AWS Step Functions)](https://docs.aws.amazon.com/step-functions/latest/dg/sample-train-model.html)
- [Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Best practices and design patterns for building machine learning workflows with Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/best-practices-and-design-patterns-for-building-machine-learning-workflows-with-amazon-sagemaker-pipelines/)
- [Create SageMaker AI Pipelines for training, consuming and monitoring your batch use cases](https://aws.amazon.com/blogs/machine-learning/create-sagemaker-pipelines-for-training-consuming-and-monitoring-your-batch-use-cases/)
- [Launch Amazon SageMaker AI Autopilot experiments directly from within Amazon SageMaker AI Pipelines to easily automate MLOps workflows](https://aws.amazon.com/blogs/machine-learning/automating-complex-deep-learning-model-training-using-amazon-sagemaker-debugger-and-aws-step-functions/)

**Related videos:**

- [Automating Machine Learning Workflows: Leveraging Amazon SageMaker AI Pipelines and Autopilot for Efficient Model Development and Deployment](https://aws.amazon.com/awstv/watch/f2ed03696ea/)

**Related examples:**

- [Amazon SageMaker AI MLOps Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab6-mlops)
- [Amazon SageMaker AI MLOps](https://github.com/aws-samples/mlops-amazon-sagemaker-devops-with-ml)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf06-bp05.html*

---

# MLPERF06-BP06 Review for updated data and features for retraining

Establishing a framework to regularly review and update your machine
learning model's data and features is essential for maintaining
model accuracy. As business environments evolve, new data patterns
emerge that can impact your model's performance. By systematically
reviewing your data and features at appropriate intervals, you can
keep your models accurate and reliable.

**Desired outcome:** You establish a
systematic approach to monitor data changes, explore new features,
and incorporate updated data into your models. Through regular data
exploration and feature engineering, you maintain model accuracy
even as underlying data patterns evolve. This creates a proactive
rather than reactive approach to model maintenance and verifies that
your ML solutions consistently deliver business value.

**Common anti-patterns:**

- Assuming that data patterns remain stable over time.
- Retraining models only when performance degrades.
- Failing to explore new potential features as business evolves.
- Using the same feature engineering approach regardless of
changing data characteristics.
- Not establishing regular review schedules for data and feature
updates.

**Benefits of establishing this best
practice:**

- Improved model accuracy through updated training data and
features.
- Early detection of data drift and proactive model updates.
- Continuous discovery of new, potentially valuable features.
- Consistent model performance despite changing business
conditions.
- Extended model lifecycle and reduced need for complete rebuilds.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data is the foundation of a machine learning model, and its
characteristics can change over time due to various factors such
as seasonal variations, market shifts, or changes in customer
behavior. Without a framework to regularly review and update your
data and features, models can gradually become less accurate as
they fail to account for these changes.

Avoid assuming that data patterns remain stable over time. Many
organizations retrain models only when performance degrades, fail
to explore new potential features as their business evolves, and
use the same feature engineering approach regardless of changing
data characteristics.

To implement this practice effectively, you need to understand the
volatility of your business environment and establish appropriate
review intervals. For example, retail businesses might need more
frequent reviews during holiday seasons when consumer behavior
changes rapidly. You also need tools to efficiently explore data,
identify new patterns, and engineer features that capture these
insights.

Amazon SageMaker AI provides comprehensive capabilities for data
preparation, feature engineering, and model monitoring. By using
these tools, you can create an efficient pipeline for regularly
reviewing and updating your model's data and features, providing
continued accuracy and relevance.

### Implementation steps

- **Assess data volatility in your
business environment**. Analyze how quickly your
business data changes by examining historical data patterns
and identifying seasonal trends, market shifts, or other
factors that affect your data. This assessment can determine
how frequently you need to review your model's data and
features.
- **Establish a review
schedule**. Based on your data volatility
assessment, create a calendar for regular data and feature
reviews. For highly volatile environments, you may need
monthly reviews, while more stable contexts might require
quarterly or biannual reviews.
- **Set up data monitoring**.
Implement
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously track data
drift by comparing production data against your model's
training data. Configure alerts when deviations occur to run
expedited reviews.
- **Create a data exploration workflow
with Amazon SageMaker AI Canvas**. Use
[Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-prep.html) to build data exploration workflows.
The unified SageMaker AI Studio environment provides seamless
integration with S3, Redshift, and EMR for comprehensive
data exploration, engineering, training, and deployment
workflows. Canvas now includes enhanced no/low-code ML tools
with templates, automation, and wizards that enable
non-engineering users to train custom models for verticals
like sales, fraud, and demand with minimal technical
expertise. These workflows should include data
visualizations, statistical analyses, and data quality
assessments.
- **Implement feature engineering
processes**. Develop standardized feature
engineering pipelines in SageMaker AI Data Wrangler that can
transform raw data into model features. Include steps to
identify potential new features during each review cycle.
- **Integrate with SageMaker AI Feature
Store**. Store engineered features in
[Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to maintain feature
consistency between training and inference. This creates a
single source of truth for features and simplifies
retraining with updated data.
- **Establish an evaluation
framework**. Create a systematic approach to
compare model performance using original features versus
updated or new features. This quantifies the impact of
feature changes and supports data-driven decisions about
model updates.
- **Form a cross-functional review
team**. Assemble a team including data scientists,
domain experts, and business stakeholders who can
collectively evaluate data changes, validate new features,
and authorize model retraining when necessary.
- **Document changes and maintain
version control**. Track changes to data sources,
feature definitions, and transformation logic using version
control systems. This creates an audit trail and supports
reproducibility.
- **Automate the retraining
pipeline**. Use
[Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) to create automated workflows
that can retrain models with updated data and features when
approved by the review team.

## Resources

**Related documents:**

- [Automate
data preparation with Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-data-export.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [No-code
data preparation for time series forecasting using Amazon SageMaker AI Canvas](https://aws.amazon.com/blogs/machine-learning/no-code-data-preparation-for-time-series-forecasting-using-amazon-sagemaker-canvas/)

**Related videos:**

- [Introducing
Amazon SageMaker AI Canvas](https://www.youtube.com/watch?v=Tb4NTq9n_Hc)
- [Automating
Machine Learning Workflows with SageMaker AI Pipelines](https://aws.amazon.com/awstv/watch/f2ed03696ea/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf06-bp06.html*

---
