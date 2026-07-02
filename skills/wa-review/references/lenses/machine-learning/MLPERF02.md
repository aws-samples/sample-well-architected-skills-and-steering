# MLPERF02 — ML problem framing

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MLPERF02-BP01 Define relevant evaluation metrics

Establishing clear, meaningful evaluation metrics is essential for
validating machine learning model performance against business
objectives. By selecting metrics that directly relate to your key
performance indicators (KPIs), you can verify that your ML solutions
deliver measurable business value.

**Desired outcome:** You have a
comprehensive set of evaluation metrics that accurately reflect your
business requirements and tolerance for errors. These metrics enable
you to tune your models directly to business objectives, monitor
performance in production, and make data-driven decisions about
model improvements.

**Common anti-patterns:**

- Using the same generic metrics for each model type regardless of
business context.
- Focusing only on technical metrics without considering business
impact.
- Overlooking the cost implications of different types of errors
(false positives and false negatives).
- Failing to establish baseline performance metrics before
deployment.
- Neglecting continuous monitoring of metrics after model
deployment.

**Benefits of establishing this best
practice:**

- Alignment of ML models with business goals and objectives.
- Better decision-making through quantifiable performance
measurement.
- Early detection of model degradation or concept drift.
- Improved ROI from ML investments.
- Clearer communication between technical teams and business
stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When developing machine learning solutions, establish evaluation
metrics that directly connect to your business objectives. These
metrics must reflect how well your model performs in the context
of your specific use case rather than relying solely on generic
technical measures.

Avoid focusing only on technical metrics without considering
business impact. Many organizations use the same metrics for each
model type regardless of business context, overlook the cost
implications of different types of errors, fail to establish
baseline performance metrics before deployment, and neglect
continuous monitoring after deployment.

For example, in a predictive maintenance scenario, the business
impact of false positives (unnecessarily replacing functioning
equipment) differs from false negatives (missing actual failures).
Understand these business implications to select appropriate
metrics like precision (minimizing false positives) or recall
(minimizing false negatives) based on which error type is more
costly to your business.

Different ML problem types require different evaluation
approaches. Classification models benefit from confusion matrices
that break down performance by class, while regression models need
error measurements that quantify prediction deviations. Custom
metrics can be developed when standard metrics don't adequately
capture business requirements.

Continuous monitoring of these metrics in production is crucial
for detecting model drift and improving ongoing performance.
Setting up automated alerts when metrics fall below thresholds
allows for timely intervention and model updates.

### Implementation steps

- **Align metrics to business
objectives**. Begin by clearly understanding the
KPIs established during the business goal identification
phase. Determine how ML model performance directly impacts
these KPIs and identify which types of errors are most
costly to the business. For example, in fraud detection,
false negatives (missed fraudulent transactions) may be more
costly than false positives.
- **Select appropriate evaluation
metrics**. Choose metrics based on your ML problem
type:

**For classification
problems:** Implement confusion matrix
derivatives (precision, recall, accuracy, F1 score),
AUC, or log-loss as appropriate for your use case
- **For regression
problems:** Utilize RMSE, MAPE, or other error
measures that align with business sensitivity to
prediction errors
- **For recommendation
systems:** Consider metrics like Normalized
Discounted Cumulative Gain (NDCG) or precision@k
- **For time series
forecasting:** Apply metrics like Mean Absolute
Scaled Error (MASE) or symmetric Mean Absolute
Percentage Error (sMAPE)

- **Develop custom metrics if
needed**. When standard metrics don't adequately
capture business requirements, create custom evaluation
metrics that better reflect the business objectives. Use
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to implement these custom metrics during
model training and evaluation.
- **Establish performance
thresholds**. Calculate the maximum acceptable
error probability required for the ML model based on
business tolerance levels. Document these thresholds as
acceptance criteria for model deployment.
- **Implement comparative
experimentation**. Use
[Amazon SageMaker AI Managed MLFlow 3.0](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to organize, track, and
compare different models trained with various
hyperparameters and approaches. The enhanced MLFlow
integration provides robust experiment management at scale
for complex ML projects. This structured experimentation
identifies models that optimize your selected metrics within
acceptable bounds.
- **Monitor metrics in
production**. Deploy
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to track model and concept
drift in real time. Configure alerts when metrics deviate
from expected performance thresholds, enabling prompt
remediation actions.
- **Incorporate feedback
loops**. Establish mechanisms to collect real-world
performance data and incorporate it into your evaluation
process. This feedback assists you to refine metrics and
models over time to better align with evolving business
needs.
- **Balance competing
metrics**. When multiple metrics are relevant,
establish a weighting system that reflects their relative
importance to business outcomes. Document this
decision-making framework for consistency in model
evaluation.
- **Implement bias detection and model
explainability**. Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) to detect bias in your models and
provide explanations for model predictions. Your evaluation
framework should include fairness and interpretability
considerations alongside performance metrics.
- **Establish automated model evaluation
pipelines**. Create automated evaluation workflows
that run consistently across different model versions and
training iterations. Use
[SageMaker AI
Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) to standardize your evaluation processes
and provide reproducible results.

## Resources

**Related documents:**

- [Amazon CloudWatch Metrics for Monitoring and Analyzing Training
Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/training-metrics.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Evaluate,
explain, and detect bias in models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-explainability.html)
- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)

**Related videos:**

- [Organize,
Track, and Evaluate ML Training Runs with Amazon SageMaker AI
Managed MLFlow](https://www.youtube.com/watch?v=zLOMYKZGxK0)
- [Foundation
model evaluation with SageMaker AI Clarify](https://aws.amazon.com/awstv/watch/31248d9d747/)
- [How
to efficiently manage ML and Gen AI experiments](https://www.youtube.com/watch?v=3xkz_5HOP6k)

**Related examples:**

- [Scikit-Learn
Data Processing and Model Evaluation](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation)
- [Amazon SageMaker AI Model Monitor Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf02-bp01.html*

---

# MLPERF02-BP02 Use purpose-built AI and ML services and resources

Consider how the workload could be handled by pre-built AI services
or ML resources. Better performance can often be delivered more
efficiently by using pre-optimized components included in AI and ML
managed services. Select an optimal mix of bespoke and pre-built
components to meet the workload requirements.

**Desired outcome:** You achieve a
balanced approach to your machine learning workloads by implementing
purpose-built AI and ML services and resources. You leverage
pre-built components where appropriate to accelerate development,
reduce management overhead, and improve performance while
maintaining the flexibility to create custom solutions where your
business needs demand it. This approach optimizes both your team's
productivity and the overall effectiveness of your AI/ML solutions.

**Common anti-patterns:**

- Building ML components from scratch when suitable pre-built
solutions exist.
- Failing to evaluate the full range of AWS AI and ML services
before starting development.
- Over-customizing solutions when standard services would
adequately meet requirements.
- Underutilizing AWS marketplace solutions and pre-trained models.
- Not considering hybrid approaches that combine managed services
with custom ML models.

**Benefits of establishing this best
practice:**

- Accelerated time-to-market for ML solutions.
- Reduced operational overhead for maintaining ML infrastructure.
- Lower development costs through leveraging pre-built components.
- Access to continuously improved and updated AI technologies.
- Ability to focus resources on high-value business
differentiators.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement purpose-built AI and ML services to focus on business
outcomes rather than infrastructure management. AWS provides a
comprehensive portfolio of AI services, ranging from ready-to-use
APIs to fully customizable ML solutions. Each service addresses
different levels of complexity and customization requirements.

When evaluating your ML workloads, assess which components could
benefit from managed services. Tasks like image classification,
regression, clustering, or time series forecasting can often be
accomplished with
[SageMaker AI
built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) without requiring custom algorithm
development. For more specialized needs, you can leverage
pre-trained models through services like
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) or develop custom models using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/).

Resist the temptation to over-customize solutions when standard
services would adequately meet requirements. Organizations often
underutilize AWS marketplace solutions and pre-trained models,
missing opportunities to accelerate development. The key is
finding the right balance between using managed services for
common ML tasks and building custom solutions for your unique
business requirements. Consider hybrid approaches that combine
managed services with custom ML models rather than pursuing an
all-or-nothing strategy.

Consider your team's capabilities when making these decisions. If
you lack specialized ML expertise, starting with fully managed AI
services provides immediate value while your team builds skills.
As your team's capabilities grow, you can selectively add custom
components where they provide strategic advantage.

### Implementation steps

- **Assess your ML use cases and
requirements**. Begin by clearly defining your
business use cases and understanding the ML capabilities
needed. Evaluate whether your requirements can be met by
pre-built services or require custom development. Consider
factors like accuracy requirements, latency needs, and the
availability of training data.
- **Learn about AWS managed AI
services**. Determine whether
[AWS managed AI services](https://aws.amazon.com/machine-learning/ai-services/) are applicable to the business
use case. Understand how managed AWS AI services can relieve
the burden of training and maintaining an ML pipeline. Use
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to develop in the cloud and understand the
roles and responsibilities needed to maintain the ML
workload. Consider combining managed AI services with custom
ML models built on Amazon SageMaker AI.
- **Explore SageMaker AI built-in
algorithms and automated ML capabilities**. Learn
about
[SageMaker AI
built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) for supervised learning tasks
like classification, regression, and forecasting. Consider
[SageMaker AI
Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) for automated machine learning that handles
data analysis, feature engineering, algorithm selection, and
hyperparameter tuning. Explore
[Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) for pre-trained models across
various ML domains, including
[foundation
models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html) that can be fine-tuned for your specific ML
tasks. For enterprise environments, implement
[SageMaker AI
JumpStart Private Model Hubs](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html) to create curated
repositories of both prebuilt and custom models with
centralized governance and version management.
- **Investigate marketplace
solutions**. Learn about
[SageMaker AI
Algorithms and Models in AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html), a curated
digital catalog that makes it simple for you to find, buy,
deploy, and manage third-party software and services.
Explore specialized algorithms or pre-trained models that
might be relevant to your use case.
- **Implement a hybrid approach where
appropriate**. Design your ML architecture to
leverage the most suitable services for each component. Use
AWS managed services for standard ML tasks and focus custom
development on business differentiators. This balanced
approach optimizes both development efficiency and solution
effectiveness.
- **Establish a model evaluation
framework**. Create a systematic process for
evaluating pre-built models against your requirements.
Define clear metrics for accuracy, latency, cost, and other
relevant factors. Use this framework to make data-driven
decisions about which components to build versus buy.
- **Plan for operational
integration**. Verify that your chosen ML services
can integrate effectively with your existing systems and
workflows. Design appropriate data pipelines, APIs, and
monitoring systems to support your hybrid ML architecture.
For development flexibility, leverage remote IDE
connectivity to securely connect third-party developer
environments such as VS Code to SageMaker AI Studio, enabling
professional MLOps workflows while maintaining centralized
governance. Consider security, regulatory adherence, and
governance requirements when implementing these
integrations.
- **Optimize model performance and
deployment**. Use
[SageMaker AI
model optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) capabilities including
quantization, compilation, and speculative decoding to
improve inference performance. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to automatically benchmark and
select optimal instance types, configurations, and
parameters for your inference endpoints. Deploy using
[SageMaker AI
deployment options](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html) such as real-time hosting,
serverless inference, or batch transform based on your
latency and throughput requirements.
- **Implement model monitoring and
governance**. Establish monitoring for model
performance, data drift, and model drift using
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html). Implement proper model versioning, A/B
testing capabilities, and rollback procedures to maintain
model quality and reliability in production environments.

## Resources

**Related documents:**

- [Built-in
algorithms and pretrained models in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [SageMaker AI
JumpStart Foundation Models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html)
- [Private
curated hubs for foundation model access control in
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html)
- [Best
practices for deploying models on SageMaker AI Hosting
Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html)
- [Inference
optimization for Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Model
deployment options in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html)
- [Distributed
training optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training-optimize.html)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Machine
Learning on AWS](https://aws.amazon.com/machine-learning/)
- [Architecture
Best Practices for Machine Learning](https://aws.amazon.com/architecture/machine-learning/)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [SageMaker AI
Algorithms and Models in AWS Marketplace](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-marketplace.html)
- [Docker
containers for training and deploying models](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html)
- [Train
a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)

**Related videos:**

- [Building
and Deploying ML Models Fast with Amazon SageMaker AI
JumpStart](https://www.youtube.com/watch?v=i4W7SfP6_38)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf02-bp02.html*

---
