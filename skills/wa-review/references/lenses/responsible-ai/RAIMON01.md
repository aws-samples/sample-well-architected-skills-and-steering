# RAIMON01 — Monitoring for deviations

**Best Practices**: 5

---

# RAIMON01-BP01 Obtain consent for monitoring production data

As appropriate, implement consent mechanisms that inform users about
what data will be collected for monitoring purposes and obtain
appropriate permissions before beginning data collection activities.
This includes considering opt-in and opt-out data collection
strategies while adhering to guidance from your legal counsel. When
appropriate, design transparent consent processes that explain
monitoring objectives, data usage, retention periods, and user
rights regarding their monitored data for opting in or opt out.
Establish procedures for managing consent changes over time,
including mechanisms for users to withdraw consent and processes for
handling data from users who have opted out.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- As appropriate, create a consent framework defining data
collection types and purposes. For example, a music
recommendation system might ask for user consent to use system
inputs and outputs for validating and improving system
performance.
- Build verification mechanisms to check consent before data
collection. For example, an e-commerce system might verify
consent status before collecting browsing behavior for
personalization.
- Deploy technical controls to filter data based on consent
preferences. For instance, a smart home system might adjust
data collection granularity based on user consent levels. Use
Amazon S3 for storing data by consent levels.
- If appropriate and feasible, set up automated processes for
consent changes.
- Maintain audit trails of consent activities. For example, a
financial AI system might track consent changes with
timestamps in an immutable ledger.

## Resources

**Related documents:**

- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon S3](https://aws.amazon.com/s3/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon01-bp01.html*

---

# RAIMON01-BP02 Set operational performance baselines and apply methods for drift detection

Set performance trend baselines by collecting initial production
data over a representative time period to capture your system's
actual operating performance, which may vary from your release
criteria thresholds. Use statistical methods to characterize normal
performance variation patterns, seasonal trends, and expected
behavioral ranges for each monitored metric based on observed system
behavior. Implement drift detection techniques such as statistical
process control charts, change point detection algorithms, and trend
analysis that can identify when current performance deviates
significantly from established baseline trends, indicating the
system is not performing as expected.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Establish a baseline using either the training data or a
representative validation dataset, defining the expected data
distribution and model behavior.
- Establish data collection to gather relevant metrics during
normal operations, capturing representative system behavior
including peak/off-peak periods and seasonal variations.
- Use statistical tests and algorithms to compare live data and
monitored metrics against the established baseline. Pre-built
rules or custom rules can be configured to define thresholds
for acceptable deviations. When a deviation exceeds these
thresholds, it may indicate potential data drift, model
performance degradation, or bias. Amazon SageMaker AI Model
Monitor and SageMaker AI Clarify are examples of services
supporting these functions.

## Resources

**Related tools:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Bias
drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift.html)

**Related documents**

- [Automated
monitoring of your machine learning models with Amazon SageMaker AI AIModel Monitor and](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/)
[sending
predictions to human review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/)
- [Amazon SageMaker AI AI Model Monitor– Fully Managed Automatic Monitoring
for Your Machine Learning](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/)
[Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/)
- [AWS re:Invent 2020: Detect machine learning (ML) model drift in
production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)
- [ISO/IEC
42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon01-bp02.html*

---

# RAIMON01-BP03 Preserve data privacy and set access controls on monitored data

Apply data governance processes that specify what monitoring data
can be collected, processed, stored, and accessed throughout the
monitoring lifecycle. Consider implementing privacy-preserving
techniques including anonymization, differential privacy, and secure
computation methods that enable system oversight without exposing
individual user information. Using the principle of least privilege,
create role-based access controls that limit monitoring data access
to authorized personnel based on job function, with detailed audit
trails tracking data access activities. Establish data retention
policies that specify how long different types of monitoring data
should be stored, with automated deletion processes and procedures
for handling individual data requests.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Apply data governance processes that specify what AI
monitoring data can be collected, processed, stored, and
accessed throughout the monitoring lifecycle. This involves
implementing policies that define permissible data collection
scope, processing methods, storage requirements, and access
protocols for AI model monitoring activities. For instance, a
facial recognition AI system allows collection of prediction
accuracy metrics and inference latency but prohibits storage
of actual facial images or biometric features. Use AWS Config
to enforce data governance rules and AWS CloudTrail to audit
adherence with data collection policies.
- Implement privacy-preserving techniques including
anonymization, differential privacy, and secure computation
methods that enable AI system oversight without exposing
individual user information. This requires deploying technical
safeguards that protect user privacy while maintaining
monitoring capabilities. For example, a healthcare chatbot
application could anonymize patient identifiers in
conversation logs, apply differential privacy to response
accuracy metrics, and encrypt the monitoring data. Use Amazon SageMaker AI Processing jobs to run anonymization and
differential privacy implementations, Amazon Macie to identify
and protect sensitive data in monitoring datasets, and AWS KMS
for encryption and key management.
- Create role-based access controls that limit AI monitoring
data access to authorized personnel based on job function,
with detailed audit trails tracking data access activities.
This involves implementing granular permissions that restrict
monitoring data visibility to specific roles and
responsibilities. For example, data scientists access model
accuracy metrics while security teams access only anomaly
detection alerts, with access types logged and monitored. Use
AWS IAM to implement role-based access controls and AWS CloudTrail to maintain detailed audit trails of monitoring
data access.
- Establish data retention policies that specify how long
different types of AI monitoring data should be stored, with
automated deletion processes and procedures for handling
individual data requests. This requires defining lifecycle
management rules for various monitoring data types and
implementing automated compliance-aligned processes.

## Resources

**Related documents:**

- [Amazon SageMaker AI solution for privacy in natural language
processing](https://www.amazon.science/code-and-datasets/amazon-sagemaker-solution-for-privacy-in-natural-language-processing)
- [Differentially
Private Fair Learning](https://arxiv.org/abs/1812.02696)
- [Approximate,
adapt, anonymize (3A): A framework for privacy preserving
training data release for machine learning](https://www.amazon.science/publications/approximate-adapt-anonymize-3a-a-framework-for-privacy-preserving-training-data-release-for-machine-learning)
- [Privacy
preserving data selection for bias mitigation in speech
models](https://www.amazon.science/publications/privacy-preserving-data-selection-for-bias-mitigation-in-speech-models)
- [ISO/IEC
42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001)

**Related tools:**

- [AWS Config](https://aws.amazon.com/config/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon SageMaker AI Processing](https://aws.amazon.com/sagemaker/processing/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon01-bp03.html*

---

# RAIMON01-BP04 Create monitoring dashboards for operational visibility

Design role-based monitoring dashboards that present relevant system
health, performance, and risk indicators tailored to each
stakeholder group's responsibilities and expertise levels. Create
technical dashboards for engineering teams that show detailed
performance metrics, error rates, and component-level health
indicators with capabilities for deep-dive analysis. Develop
executive dashboards that present summary-level information about
benefit realization, risk mitigation effectiveness, and overall
system performance against business objectives. Implement governance
dashboards for teams that track adherence to release criteria and
incident response metrics with historical trending capabilities.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Map stakeholder dashboard requirements by role. For example, a
healthcare AI system can create separate views for clinical
staff showing patient outcomes, technical teams showing model
performance, and executives showing system impact. Use
QuickSight for dashboards and IAM for access control.
- Create dashboards for performance metrics and have mechanisms
for triggering alarms when threshold is met. For example, you
can monitor each part of your Amazon Bedrock application using
Amazon CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. You can graph the
metrics using the CloudWatch console. You can also set alarms
to watch for certain thresholds and send notifications or take
actions when values exceed those thresholds. Amazon CloudWatch
metric may include Bedrock Guardrails metrics like total
requests intervened by guardrail for various reasons like
denied topics, in appropriate content, sensitive information
or context grounding concerns. Controlling CloudWatch metrics
visibility by role is accomplished through AWS Identity and Access Management (IAM) policies.
- When using Amazon SageMaker AI Model Monitor, Amazon SageMaker AI
Model Dashboard can be used to track the performance of models
as they make real-time predictions on live data. Use a
dashboard to find models that violate thresholds you set for
data quality, model quality, bias and explainability.

- Data Quality: Compares live data to training data. If they
diverge, your model's inferences may no longer be accurate.
- Model Quality: Compares the predictions that the model makes
with the actual Ground Truth labels that the model attempts to
predict.
- Bias Drift: Compares the distribution of live data to training
data, which can also cause inaccurate predictions.
- Feature Attribution/Explainability Drift: Compare the relative
rankings of your features in training data versus live data,
which could also be a result of bias drift.

## Resources

**Related documents**

- [Data
quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)
- [Model
quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-model-quality.html)
- [Bias
drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-bias-drift.html)
- [Feature
attribution drift for models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-monitor-feature-attribution-drift.html)
- [Implement
safeguards for your application by associating a guardrail
with your agent](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-guardrail.html)
- [Monitor
Amazon Bedrock Guardrails using CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html)
- [Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html)
- [Automated
monitoring of your machine learning models with Amazon SageMaker AI Model Monitor and sending predictions to human
review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/)
- [Amazon SageMaker AI Model Monitor – Fully Managed Automatic Monitoring
For Your Machine Learning Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/)
- [ISO/IEC
42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001)

**Related tools**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon01-bp04.html*

---

# RAIMON01-BP05 Design protocols that trigger human oversight of automated monitoring alerts

Set protocols for when human reviewers should be involved in system
oversight decisions. Create sampling-based human review processes
that validate the accuracy and effectiveness of automated monitoring
systems, including procedures for evaluating edge cases and
challenging scenarios. Implement feedback mechanisms that enable
human reviewers to improve automated monitoring through labeling
ambiguous cases, refining alert criteria, and identifying new
monitoring requirements. Design human oversight workflows that
provide escalation paths, decision-making authority, and
documentation requirements for monitoring decisions that affect
system operation.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Configure human review triggers in monitoring systems based on
alert severity, confidence thresholds, and business impact.
Use workflow orchestration tools like AWS Step Functions to
route decisions and Amazon A2I for human review management.
- Establish sampling protocols to validate monitoring accuracy,
focusing on edge cases and high-risk scenarios. Integrate
annotation tools for human reviewers to assess and label
sampled alerts.
- Create feedback loops allowing reviewers to label ambiguous
cases and suggest monitoring improvements. Use Amazon A2I for
feedback collection and AWS Step Functions to route feedback
for monitoring system improvements.
- Design escalation paths with clear authority levels and
documentation requirements for critical monitoring decisions.
Configure workflow tools to manage approvals and maintain
audit trails of human oversight activities.
- Document human oversight decisions, rationale, and outcomes to
support continuous improvement of monitoring protocols. For
example, documenting human interventions on monitoring alerts
with timestamps, reviewer identity, decision rationale, and
subsequent monitoring system behavior changes.

## Resources

**Related documents**

- [Amazon
Augmented AI](https://docs.aws.amazon.com/augmented-ai/latest/developerguide/what-is.html)
- [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html)
- [ISO/IEC
42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon01-bp05.html*

---
