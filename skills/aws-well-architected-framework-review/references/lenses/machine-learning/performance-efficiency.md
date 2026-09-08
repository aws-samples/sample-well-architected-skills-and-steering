# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 6

---

# MLPERF01 — Business goal identification

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# MLPERF01-BP01 Determine key performance indicators

Use guidance from business stakeholders to capture key performance
indicators (KPIs) relevant to the business use case. The KPIs should
be directly linked to business value to guide acceptable model
performance. Consider that machine learning inferences are
probabilistic and will not provide exact results. Identify a minimum
acceptable accuracy and maximum acceptable error in the KPIs. This
enables you to achieve the required business value and manage the
risk of variable results.

**Desired outcome:** By defining
direct, measurable KPIs, ML initiatives deliver quantifiable
business outcomes, such as cost savings, expanded scale, and faster
response times. Clear performance thresholds set realistic
stakeholder expectations and enable risk management based on the
probabilistic nature of ML.

**Common anti-patterns:**

- Implementing ML solutions without defining clear
business-oriented success metrics.
- Focusing solely on technical metrics (like model accuracy)
without connecting them to business outcomes.
- Setting unrealistic expectations for ML performance without
accounting for probabilistic results.
- Failing to define acceptable error thresholds for critical
business processes.
- Neglecting to quantify the actual business value of ML
implementations.

**Benefits of establishing this best
practice:**

- Aligns machine learning (ML) outcomes with business objectives
for measurable value.
- Creates clear expectations about model performance that account
for ML's probabilistic nature.
- Enables objective evaluation of ML solution success based on
business impact.
- Improves prioritization of ML investments based on tangible
results.
- Accelerates decision-making by translating ML insights into
business actions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start by identifying business challenges ML aims to solve and how
success translates into specific, quantifiable benefits. Engage
stakeholders throughout KPI selection to verify that business
priorities drive metric design. Use metrics that reflect business
value—such as cost reduction, customer retention rate, or time
savings—rather than technical measures alone.

Regularly review KPIs to stay aligned with strategic shifts.
Feedback from business results informs necessary adjustments to
both models and evaluation metrics. Common pitfalls include
proceeding without clear business KPIs, focusing only on technical
metrics such as accuracy, or establishing unrealistic expectations
that ignore the probabilistic nature of ML results. Failing to set
acceptable error thresholds exposes critical business processes to
unmanaged risk, and overlooking the business value of ML adoption
makes it hard to measure impact or secure stakeholder support.

### Implementation steps

- **Quantify the value of machine
learning for the business**. Consider measures of
how machine learning and automation will impact the
business:

How much will machine learning reduce costs?
- How many more users will be reached by increasing scale?
- How much time will the business save by being able to
respond faster to changes, such as in demand and supply
disruptions?
- How many hours of manual effort will be reduced by
automating with machine learning?
- How much will machine learning be able to change user
behavior, such as reducing churn?

- **Evaluate risks and the tolerance for
error**. Quantify the impact of machine learning on
the business. Rank order the value of impacts to identify
the primary KPIs to optimize with machine learning. Define
the cost of error for automated inferences that will be
performed by ML models in the use case. Determine the
tolerance of the business for error. For example, determine
how far off a cost reduction estimate would have to be to
negatively impact the business goals. Finally, evaluate the
risks of machine learning for the business, and whether the
benefits of ML solutions are of high enough value to
outweigh those risks.
- **Establish baseline
metrics**. Before implementing ML solutions,
document current performance metrics to create a baseline
against which to measure improvements. Collect data on
existing processes, including costs, time requirements,
error rates, and other relevant performance indicators. This
baseline will serve as a reference point for demonstrating
the business value of your ML implementation.
- **Define predictive and prescriptive
KPIs**. Move beyond retrospective metrics to
develop KPIs that offer predictive and prescriptive
insights. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and
[Quick](https://aws.amazon.com/quicksight/) to create dashboards that visualize these
forward-looking KPIs, making them accessible to business
stakeholders.
- **Create a KPI governance
framework**. Develop a structured approach for
monitoring, reviewing, and refining your KPIs over time.
Gather executive alignment on metrics, establish consistent
data collection processes, and define protocols for taking
corrective actions when negative trends emerge. Regularly
analyze trends and periodically refine KPIs to accurately
gauge the business impact of ML implementations.
- **Leverage advanced analytics for
insights**. Enhance KPI discovery and accessibility
by integrating advanced analytics services, such as
[Amazon Q](https://aws.amazon.com/q/). These tools uncover hidden business patterns and
translate complex results into conversational analytics for
non-technical audiences.

## Resources

**Related documents:**

- [Improve
Business Outcomes with Machine Learning](https://aws.amazon.com/machine-learning/ml-use-cases/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [Machine
Learning (ML) Governance with Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/ml-governance/)
- [Amazon Q for
Business Analytics](https://aws.amazon.com/q/)
- [AI/ML
| AWS Executive Insights](https://aws.amazon.com/executive-insights/generative-ai-ml/)
- [Thought
Leadership | Artificial Intelligence - AWS](https://aws.amazon.com/blogs/machine-learning/category/post-types/thought-leadership/)
- [Keys
to maximizing AI value](https://aws.amazon.com/isv/resources/keys-to-maximizing-generative-ai-value-in-software-companies/)

**Related videos:**

- [How
to Drive Business Value with AI/ML](https://www.youtube.com/watch?v=W4Xd8mPqqKU)
- [Creating
Business Value with AWS AI/ML](https://www.youtube.com/watch?v=A2bIIznG-80)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf01-bp01.html*

---

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

# MLPERF03 — Data processing

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# MLPERF03-BP01 Use a modern data architecture

Get the best insights from exponentially growing data using a modern
data architecture. This architecture enables movement of data
between a data lake and purpose-built stores including a data
warehouse, relational databases, non-relational databases, ML and
big data processing, and log analytics. A data lake provides a
single place to run analytics across mixed data structures collected
from disparate sources. Purpose-built analytics services provide the
speed required for specific use cases like real-time dashboards and
log analytics.

**Desired outcome:** You implement a
modern data architecture that enables seamless data movement between
storage systems, provides unified governance, and supports diverse
ML workloads. This architecture accelerates data preparation,
improves data quality, and enables efficient feature engineering for
machine learning models.

**Common anti-patterns:**

- Creating isolated data silos where different teams manage
separate data stores without coordination.
- Building data architecture without establishing proper
governance, access controls, or compliance-aligned frameworks.
- Using one-size-fits-all storage solutions without considering
specific workload requirements.
- Relying on manual processes for data movement, transformation,
and quality checks.
- Neglecting to implement proper data cataloging and discovery
mechanisms.

**Benefits of establishing this best
practice:**

- Unified data governance and access control across data stores.
- Reduced data preparation time through integrated data services.
- Improved data quality and consistency for ML model training.
- Enhanced scalability for growing data volumes and ML workloads.
- Better cost optimization through purpose-built storage
solutions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When building machine learning solutions, you need a modern data
architecture that can handle diverse data types, support various
ML workloads, and provide unified governance across data stores.
This architecture enables efficient data movement between storage
systems while maintaining security, quality, and cost
optimization.

Avoid creating isolated data silos where different teams manage
separate data stores without coordination. Many organizations
struggle with inconsistent data governance policies across
different storage systems, lack unified access controls for ML
teams, fail to implement proper data cataloging and discovery
mechanisms, and neglect to optimize storage costs based on access
patterns. These issues create bottlenecks in ML workflows and
increase operational complexity.

For example, in a retail ML use case, you might need to combine
customer transaction data from a data warehouse, real-time
clickstream data from streaming services, and product catalog
information from operational databases. A modern data architecture
enables seamless access to these data sources while maintaining
consistent security policies and enabling efficient feature
engineering for recommendation models.

Different ML workloads require different data access patterns.
Batch training jobs benefit from optimized data lake storage with
efficient querying capabilities, while real-time inference
requires low-latency access to feature stores and streaming data
pipelines. Custom data processing workflows can be developed when
standard ETL processes don't adequately support your specific ML
requirements.

Continuous monitoring of data quality and pipeline performance is
crucial for maintaining reliable ML systems. Setting up automated
data quality checks and pipeline monitoring allows for early
detection of data issues that could impact model performance.

### Implementation steps

- **Design your data lake
foundation**. Begin by establishing a centralized
data lake using
[Amazon S3](https://aws.amazon.com/s3/) as the primary storage layer. Organize data using
a logical structure that supports both current and future ML
use cases, such as organizing by business domain, data
source, and processing stage. Implement data partitioning
strategies based on common query patterns to optimize
performance and reduce costs. For example, partition
time-series data by date and customer data by region to
enable efficient querying for ML feature extraction.
- **Implement unified data
governance**. Use
[AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) to build a scalable and secure data
lake with centralized governance. Establish consistent
security policies, access controls, and audit trails across
data stores. Apply fine-grained permissions that enable
self-service access for ML practitioners while maintaining
security and and addressing requirements. Create data
stewardship roles and processes to improve ongoing data
quality and governance.
- **Integrate purpose-built analytics
services**. Build a high-speed analytic layer with
purpose-built services selected based on your specific ML
workload requirements:

Use
[Amazon Redshift](https://aws.amazon.com/redshift/) for data warehousing and complex
analytical queries
- Implement
[Amazon Kinesis](https://aws.amazon.com/kinesis/) for real-time streaming data processing
- Deploy
[Amazon Athena](https://aws.amazon.com/athena/) for interactive queries and ad-hoc
analysis
- Consider
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for high-performance operational
workloads
- Use
[Amazon Timestream](https://aws.amazon.com/timestream/) for time-series data applications

- **Enable seamless data
integration**. Use
[AWS Glue](https://aws.amazon.com/glue/) to integrate data across services and data
stores. Implement automated data cataloging to maintain
metadata and enable data discovery across your organization.
Create ETL pipelines that prepare data for ML workloads
while maintaining data lineage and enabling reproducibility.
Design workflows that can handle both batch and streaming
data processing requirements.
- **Optimize for ML
workloads**. Design data pipelines that support
both batch and real-time ML training scenarios. Implement
feature stores using services like
[Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to manage and share ML
features across teams and models. Create standardized
feature engineering processes that can be reused across
different ML projects and provide consistent data
transformations.
- **Establish data quality
monitoring**. Implement automated data quality
checks and monitoring for data reliability for ML models.
Use
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data profiling and quality
assessment. Set up automated alerts for data quality issues
such as missing values, schema changes, or statistical
anomalies that could impact ML model performance.
- **Implement cost optimization
strategies**. Use appropriate storage classes in
Amazon S3 based on data access patterns. Implement lifecycle
policies to automatically transition data to lower-cost
storage tiers such as S3 Infrequent Access or Amazon Glacier for
archival data. Monitor and optimize query performance to
control compute costs, and use reserved capacity where
appropriate for predictable workloads.
- **Enable real-time data
processing**. For ML use cases requiring real-time
inference, implement streaming data pipelines using Amazon Kinesis and
[AWS Lambda](https://aws.amazon.com/lambda/) to process data as it arrives and update
feature stores in near real-time. Design architectures that
can handle varying data volumes and provide consistent
low-latency access to features for real-time ML predictions.
- **Implement data lineage and
versioning**. Establish comprehensive data lineage
tracking to understand data flow from source to ML models.
Use versioning for both datasets and feature definitions to
enable reproducible ML experiments and model rollbacks when
necessary. This is crucial for improving regulatory
adherence and debugging ML model issues.
- **Create self-service data
access**. Build data catalogs and discovery tools
that enable ML practitioners to find and access relevant
data without requiring deep technical knowledge of the
underlying storage systems. Implement standardized APIs and
interfaces that abstract the complexity of the data
architecture while providing the flexibility needed for
diverse ML workloads.

## Resources

**Related documents:**

- [The
lakehouse architecture of Amazon SageMaker AI](https://aws.amazon.com/sagemaker/lakehouse/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)
- [What
is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [AWS Lake Formation: How it works](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [What
is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Modern
Data Architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/)
- [Amazon SageMaker AI Lakehouse | AWS Big Data
Blog](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-sagemaker-lakehouse/)moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/)
- [Amazon SageMaker AI | AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/category/artificial-intelligence/sagemaker/)

**Related videos:**

- [Understanding
Amazon S3 Tables: Architecture, performance, and
integration](https://www.youtube.com/watch?v=e1ypMWSHgsM)
- [Accelerate
your Analytics and AI with Amazon SageMaker AI LakeHouse](https://www.youtube.com/watch?v=qZTbS0xPN-U)
- [Unifying
data governance with Immuta and AWS Lake Formation](https://www.youtube.com/watch?v=X09-n2jJZKw)
- [The
lake house approach to data warehousing with Amazon Redshift](https://www.youtube.com/watch?v=35wXL0Q1Dcc)

**Related services:**

- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [Amazon Athena](https://aws.amazon.com/athena/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf03-bp01.html*

---

# MLPERF04 — Model development

**Pillar**: Performance Efficiency  
**Best Practices**: 6

---

# MLPERF04-BP01 Optimize training and inference instance types

Selecting appropriate instance types for training and inference
workloads provides optimal performance, reduced costs, and faster
time-to-market for your machine learning models. By understanding
your model's specific requirements and data characteristics, you can
choose the right computational resources to maximize efficiency.

**Desired outcome:** You achieve
optimal performance and cost-effectiveness for your machine learning
workloads by selecting appropriate instance types for both training
and inference. You understand how model complexity and data
characteristics influence hardware decisions, enabling you to
accelerate model development, improve inference speeds, and manage
resources efficiently.

**Common anti-patterns:**

- Using the same instance type for both training and inference
workloads.
- Overprovisioning resources just to be safe without performance
testing.
- Selecting expensive GPU instances for inference when CPU
instances would suffice.
- Ignoring model-specific hardware requirements when selecting
instances.
- Not scaling training across multiple instances for large
datasets.

**Benefits of establishing this best
practice:**

- Reduced training time and faster model iterations.
- Lower operational costs through right-sized resources.
- Improved inference latency and throughput.
- Better utilization of available computational resources.
- Enhanced scalability for varying workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Understanding how your model type and data characteristics
influence instance selection is essential for optimizing machine
learning workloads. For training, the computational requirements
depend largely on the model complexity, dataset size, and training
approach. Deep learning models, particularly those processing
image, video, or language data, often benefit from GPU-accelerated
instances due to their parallel processing capabilities.
Meanwhile, traditional machine learning algorithms may be
efficiently trained on CPU instances.

For inference, requirements vary based on deployment scenarios.
Real-time applications with strict latency requirements might need
powerful compute-optimized instances, while batch prediction
workloads can use more cost-effective options. Generally, CPUs are
sufficient for many inference scenarios, though complex models may
still benefit from GPU acceleration.

When evaluating instance options, consider memory requirements
(especially for large models or datasets), network performance for
distributed training, and storage I/O capabilities when working
with large datasets. The right balance between performance and
cost is key to sustainable machine learning operations.

### Implementation steps

- **Analyze your model and data
requirements**. Begin by understanding the
computational needs of your machine learning algorithm.
Assess memory requirements, model complexity, and dataset
size. For deep learning models processing image, video, or
language data, GPU instances like P4, G4, or P3 typically
offer the best performance. For traditional ML algorithms,
CPU instances may be more cost-effective.
- **Benchmark different instance types
for training**. Run small-scale training jobs
across various instance types in
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to measure performance and cost metrics.
Compare training times, resource utilization, and overall
costs to identify the optimal instance type for your model.
Track
[Experiments
with Managed MLFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to track and compare results.
- **Implement distributed training for
large datasets**. For large datasets or complex
models, leverage distributed training across multiple
instances to reduce training time. Use
[SageMaker AI
distributed training libraries](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html) to automatically
partition data and optimize communication between nodes,
which accelerates training for deep learning models.
- **Optimize storage configuration for
I/O performance**. Configure fast storage options
to avoid I/O bottlenecks during training. Consider using
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) for high-performance file systems or
optimize your data pipeline to use
[Amazon S3](https://aws.amazon.com/s3/) efficiently. Proper data formatting and efficient
loading strategies can improve GPU utilization.
- **Select appropriate inference
instance types**. Evaluate latency and throughput
requirements for your inference needs. For real-time
inference with strict latency requirements, consider
compute-optimized instances or GPU-accelerated instances for
complex models. For batch inference, less expensive CPU
instances often suffice. Use
[Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to get automated
recommendations for optimal deployment configurations.
- **Monitor and optimize
costs**. Implement continuous monitoring of
resource utilization and costs. Use
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and
[SageMaker AI
Studio](https://aws.amazon.com/sagemaker/studio/) resource monitoring to identify
inefficiencies. Consider using
[Amazon SageMaker AI Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/) for frequently used instance
types to reduce costs.
- **Consider model optimization
techniques**. Implement model optimization
techniques like quantization, pruning, or knowledge
distillation to reduce computational requirements for both
training and inference. Explore using
[SageMaker AI
Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to automatically optimize models for target
hardware.
- **Explore serverless inference
options**. For variable or unpredictable workloads,
consider
[Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) to automatically scale
resources based on traffic and avoid the need to choose
instance types manually.
- **Leverage specialized ML
hardware**. For large-scale training and inference
workloads, consider
[AWS Trainium instances](https://docs.aws.amazon.com/dlami/latest/devguide/trainium.html) for training and AWS Inferentia
instances for inference to achieve better price-performance
ratios compared to traditional GPU instances.

## Resources

**Related documents:**

- [Train
a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)
- [Deploy
models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Recommended
Trainium Instances](https://docs.aws.amazon.com/dlami/latest/devguide/trainium.html)
- [What
are AWS Deep Learning Containers?](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html)
- [Learn
how to select ML instances on the fly in Amazon SageMaker AI
Studio](https://aws.amazon.com/blogs/machine-learning/learn-how-to-select-ml-instances-on-the-fly-in-amazon-sagemaker-studio/)
- [Ensure
efficient compute resources on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/right-sizing-resources-and-avoiding-unnecessary-costs-in-amazon-sagemaker/)

**Related videos:**

- [How
to choose the right instance type for ML inference](https://www.youtube.com/watch?v=0DSgXTN7ehg)
- [The
right instance type in Amazon SageMaker AI](https://www.youtube.com/watch?v=vRB9Uncsia8)

**Related examples:**

- [Amazon SageMaker AI End-to-End Example](https://github.com/aws/amazon-sagemaker-examples/tree/main/end_to_end)
- [SageMaker AI
Inference Recommender Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-recommender)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf04-bp01.html*

---

# MLPERF04-BP02 Explore alternatives for performance improvement

Benchmarking your machine learning models allows you to
systematically improve performance by evaluating and comparing
different algorithms, features, and architectural resources. Use
this practice to identify the optimal combination and achieve your
desired performance metrics.

**Desired outcome:** You implement a
systematic approach to improving your machine learning model's
performance through benchmarking various techniques. You'll
establish a baseline model and methodically explore alternatives
including data volume increases, feature engineering, algorithm
selection, ensemble methods, and hyperparameter tuning. This results
in optimized models that provide higher accuracy and better business
value.

**Common anti-patterns:**

- Selecting a complex algorithm without establishing a baseline.
- Ignoring feature engineering in favor of only trying different
algorithms.
- Using more data without understanding its quality or relevance.
- Focusing exclusively on accuracy while ignoring other important
metrics.
- Manually testing hyperparameters without a systematic approach.

**Benefits of establishing this best
practice:**

- Improved model accuracy and performance.
- Better understanding of which factors most influence model
performance.
- More efficient use of computational resources.
- Systematic approach to model improvement instead of random
experimentation.
- Ability to document and reproduce experiments for future
reference.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Performance improvement in machine learning requires a structured,
iterative approach. Benchmarking assists you in systematically
comparing different approaches and determining the most effective
path to improved model performance. Start by establishing a
baseline with simple algorithms and obvious features, then
methodically explore alternatives to improve upon that baseline.

You can explore multiple avenues for improving performance:
increasing data volume, engineering better features, selecting
more appropriate algorithms, combining models through ensemble
methods, and tuning hyperparameters. Each approach provides unique
benefits and may be more or less effective depending on your use
case. The key is to follow a systematic process, measure results
accurately, and document what you learn.

### Implementation steps

- **Establish a baseline
model**. Start with a simple architecture, obvious
features, and a straightforward algorithm to create your
baseline. Use
[Amazon SageMaker AI built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) to quickly develop this
initial model. This gives you a reference point for
comparing future experiments and improvements.
- **Set up experiment
tracking**. Use
[Amazon SageMaker AI Managed MLFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to organize, track, compare,
and evaluate your machine learning experiments. Create a
structured framework that tracks performance metrics,
algorithm choices, features used, and hyperparameter
settings so you can effectively compare results across
different approaches.
- **Test different
algorithms**. Systematically test various
algorithms, starting with simpler ones and progressively
trying more complex options. SageMaker AI provides many
built-in algorithms that you can compare. Document how each
algorithm performs relative to your baseline and identify
which ones show the most promise for your data and problem.
- **Apply feature
engineering**. Extract important signals in your
data through feature engineering. This may include feature
selection, transformation, creation of new features,
normalization, and encoding techniques. Use
[SageMaker AI
Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-create-feature-group.html) to manage and share features across
experiments and teams.
- **Increase data volume and
quality**. Evaluate whether adding more data or
improving data quality could assist your model. More data
often broadens the statistical range and improve model
performance, but only if the additional data is relevant and
of good quality.
- **Implement ensemble
methods**. Combine multiple models to leverage
different strengths and compensate for individual
weaknesses. Techniques like bagging, boosting, and stacking
can often improve overall accuracy. SageMaker AI makes it
simple to implement ensemble predictions from multiple
models.
- **Perform hyperparameter
tuning**. Use
[Amazon SageMaker AI Automatic Model Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html) to optimize your
model's hyperparameters. This service automates the search
through different hyperparameter combinations to find
optimal values that improve model performance. You can run
multiple HPO jobs in parallel to speed up the process.
- **Evaluate improvements
systematically**. For each change, rigorously
evaluate whether performance has improved based on relevant
metrics for your problem. Use SageMaker AI's evaluation tools
to compare results across experiments and determine which
approaches deliver the most gains.
- **Optimize for production**.
Once you've identified the best performing approach,
optimize it for production deployment. Consider factors like
inference latency, model size, and resource requirements
alongside pure performance metrics.
- **Document findings and
methodology**. Create comprehensive documentation
of your benchmarking process, including what worked, what
didn't, and why. This provides valuable information for
future model improvements and builds institutional
knowledge.

## Resources

**Related documents:**

- [Built-in
algorithms and pretrained models in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Automatic
model tuning with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [Use
Feature Store with SDK for Python (Boto3)](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-create-feature-group.html)
- [Feature
Processing with Spark ML and Scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipeline-mleap-scikit-learn-containers.html)
- [Running
multiple HPO jobs in parallel on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/)
- [Optimizing
portfolio value with Amazon SageMaker AI automatic model
tuning](https://aws.amazon.com/blogs/machine-learning/optimizing-portfolio-value-with-amazon-sagemaker-automatic-model-tuning/)

**Related videos:**

- [How
To Efficiently Manage ML experiments using Amazon SageMaker AI ML
Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k)
- [Train
large models on Amazon SageMaker AI for scale and
performance](https://www.youtube.com/watch?v=cryA1LFwS98)

**Related examples:**

- [Feature
Engineering Immersion Day Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab1-feature-engineering)
- [Ensemble
Predictions From Multiple Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html)
- [Amazon SageMaker AI Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf04-bp02.html*

---

# MLPERF04-BP03 Establish a model performance evaluation pipeline

Establish an end-to-end model performance evaluation pipeline that
captures key metrics to evaluate your model's success, align with
business KPIs, and automatically test performance when models or
data are updated.

**Desired outcome:** You can
systematically evaluate model performance through automated
pipelines that measure relevant metrics specific to your use case.
Your evaluation process runs automatically whenever model or data
updates occur, creating a continuous quality assessment. This
assists you in maintaining high-performing models that deliver
business value while providing transparency into model behavior and
performance over time.

**Common anti-patterns:**

- Relying solely on training accuracy without considering
real-world performance metrics.
- Manual evaluation of models that leads to inconsistency.
- Using generic metrics that don't align with business KPIs.
- Waiting until deployment to evaluate model performance.
- Not establishing automated evaluation triggers when models or
data change.

**Benefits of establishing this best
practice:**

- Verifies that models maintain expected performance levels over
time.
- Provides data-driven decision making for model selection and
deployment.
- Aligns machine learning outcomes with business objectives.
- Enables faster identification and resolution of performance
degradation.
- Improves regulatory adherence through consistent evaluation
protocols.
- Increases stakeholder confidence through transparent performance
reporting.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model performance evaluation is critical to verify that your
machine learning solutions deliver on their intended business
outcomes. By establishing a robust, automated evaluation pipeline,
you can consistently assess how well your models perform against
business KPIs and make data-driven decisions about deployment
readiness.

Avoid relying solely on training accuracy without considering
real-world performance metrics. Many organizations use manual,
ad-hoc evaluation of models that leads to inconsistency, use
generic metrics that don't align with business KPIs, wait until
deployment to evaluate model performance, and fail to establish
automated evaluation runs when models or data change.

Your evaluation pipeline should incorporate metrics specific to
your use case. For regression problems, this might include Root
Mean Squared Error (RMSE). For classification tasks, accuracy,
precision, recall, F1 score, and area under the curve (AUC) are
common metrics. These technical metrics should tie directly to
business KPIs, helping stakeholders understand the model's
contribution to business goals.

Automating the evaluation process provides consistency and reduces
manual errors. When new data arrives or models are updated, your
pipeline should automatically run evaluations, providing
continuous feedback on model performance and enabling rapid
identification of any degradation issues.

### Implementation steps

- **Define business objectives and
evaluation criteria**. Begin by clearly defining
what success means for your machine learning use case.
Identify relevant business KPIs and determine which
technical metrics (like accuracy, precision, recall, F1
score, RMSE, AUC) best align with these business goals.
Document these metrics and their target values to establish
clear evaluation criteria.
- **Create an end-to-end workflow with
Amazon SageMaker AI Pipelines**. Start with a workflow
template to establish an initial infrastructure for model
training and deployment.
[SageMaker AI
Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) can automate different steps of the ML
workflow including data loading, data transformation,
training, tuning, and deployment. Within SageMaker AI
Pipelines, the
[SageMaker AI
Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) tracks model versions and respective
artifacts, including metadata and lineage data collected
throughout the model development lifecycle.
- **Implement model evaluation
components in your pipeline**. Design dedicated
evaluation steps within your pipeline that calculate
relevant metrics for your model. Use
[SageMaker AI
Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) jobs or custom Python scripts to perform
evaluations on validation datasets. Store evaluation results
in a central location for tracking performance over time.
- **Set up automated prompts for
evaluation**. Configure your pipeline to
automatically initiate the evaluation process whenever
there's a model update or new training data becomes
available. This provides continuous quality assessment and
identifies performance degradation early.
- **Create visualization and reporting
mechanisms**. Implement dashboards or reports that
display model performance metrics in a straightforward
format. Stakeholders can use visualizations to quickly
assess model performance against business KPIs and make
informed decisions about model deployment.
- **Establish model approval
workflows**. Define criteria for model approval
based on evaluation results. Implement approval workflows in
the SageMaker AI Model Registry that automatically promote
models meeting performance thresholds to production, while
flagging underperforming models for review.
- **Implement A/B testing
capabilities**. For production models, set up A/B
testing infrastructure to compare performance of new models
against baseline models using real-world data. This provides
additional validation before fully deploying model updates.
- **Monitor production model
performance**. Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously monitor
deployed models for data drift, model drift, and performance
degradation. Set up alerts when performance metrics fall
below acceptable thresholds.
- **Implement bias detection and
fairness evaluation**. Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html) to detect bias in your models and
check fairness across different demographic groups. Include
bias metrics as part of your evaluation criteria.
- **Create feedback loops for continuous
improvement**. Design mechanisms to capture
feedback from production model performance and incorporate
these insights into future model iterations. This creates a
cycle of continuous improvement based on real-world
performance.

## Resources

**Related documents:**

- [Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [Define
a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/define-pipeline.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness
and Explainability with SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html)
- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)
- [Extend
Amazon SageMaker AI Pipelines to include custom steps using
callback steps](https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/)

**Related videos:**

- [Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=Hvz2GGU3Z8g)
- [How
to create fully automated ML workflows with Amazon SageMaker AI
Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg)

**Related examples:**

- [Orchestrate
your build and train pipeline with SageMaker AI Pipelines](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab6-mlops/pipelines)
- [SageMaker AI
Model Evaluation Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines)
- [MLOps
with SageMaker AI Pipelines](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf04-bp03.html*

---

# MLPERF04-BP04 Establish feature statistics

Establishing key statistics to measure changes in data that affect
model outcomes is crucial for maintaining ML model performance. By
analyzing feature importance and sensitivity, you can select the
most critical features to monitor and detect when data drifts
outside acceptable ranges so you can determine when model retraining
is necessary.

**Desired outcome:** You establish a
robust monitoring system that tracks key statistics for the most
influential features in your machine learning models. You can detect
data drift that could impact model performance, allowing for timely
model retraining decisions based on quantitative measures rather
than intuition. Your monitoring system alerts you when important
features drift outside their expected statistical ranges, providing
continuous model reliability and performance.

**Common anti-patterns:**

- Monitoring features equally without considering their relative
importance to model outcomes.
- Failing to establish baseline statistics for important features
before deploying models.
- Not setting appropriate thresholds for data drift alerts.
- Monitoring only model outputs without analyzing input feature
distributions.
- Neglecting to perform sensitivity analysis to understand model
behavior at decision boundaries.

**Benefits of establishing this best
practice:**

- Early detection of data quality issues that could affect model
performance.
- Reduced model performance degradation through timely retraining.
- Greater understanding of which features most impact model
predictions.
- Improved model reliability in production environments.
- Enhanced ability to explain model behavior and decision
boundaries to stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establishing feature statistics is essential for maintaining model
performance over time. As real-world data evolves, your model's
predictive power can deteriorate if the data drift exceeds certain
thresholds. By focusing on the most influential features and
understanding your model's sensitivity to changes in these
features, you can create an effective monitoring strategy.

Start by analyzing which features have the greatest impact on your
model's predictions through feature importance analysis. Then
establish baseline statistics for these critical features using
your training data. Monitor these statistics in production,
comparing them to your baseline, and set up alerts when deviations
occur. This approach allows you to proactively address potential
model performance issues before they impact your business
outcomes.

### Implementation steps

- **Analyze feature distributions with
Data Wrangler**. Use
[Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-analyses.html) to perform exploratory data
analysis on your dataset. Examine the distribution of each
feature, identify outliers, and understand relationships
between features. Data Wrangler provides visualizations such
as histograms, scatter plots, and correlation matrices to
understand your data's characteristics before training.
- **Train your model with proper
tracking**. When training your model, capture
metadata about the training process using
[SageMaker AI
Managed MLFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html). This can establish a baseline for
comparison and enables reproducibility of your experiments.
Track key metrics, parameters, and the training dataset
version to maintain a complete record of model development.
- **Determine feature
importance**. After training your model, analyze
which features have the greatest impact on predictions. Use
built-in feature importance methods in SageMaker AI, such as
SHAP (SHapley Additive exPlanations) values or permutation
importance. Alternatively, use model-specific methods like
feature importance in tree-based models or coefficient
magnitudes in linear models.
- **Perform sensitivity
analysis**. Map out regions in feature space where
predictions change abruptly or remain invariant. Focus
particularly on features near decision boundaries where
small changes can alter model outputs. Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html) to analyze how variations in input
features affect predictions and understand which features
require the closest monitoring.
- **Check for data bias**. Use
Amazon SageMaker AI Clarify to analyze your dataset for
potential biases. Imbalances or biases in your training data
can lead to poor generalization and unfair predictions.
Identify and address these issues before deploying your
model to create ethical and reliable ML systems.
- **Establish monitoring
baseline**. Configure
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to create a baseline from
your training data. This baseline captures the expected
statistical properties of your features, including
distributions, ranges, and relationships. SageMaker AI
automatically analyzes and creates constraints for each
feature based on the training data.
- **Configure data quality
monitoring**. Set up SageMaker AI Model Monitor to
continuously evaluate production data against your
established baseline. Configure monitoring schedules based
on your application's requirements—hourly, daily, or weekly.
Define thresholds for acceptable deviation from the baseline
for each important feature.
- **Implement data drift
detection**. Configure alerts to notify you when
important features drift outside their acceptable
statistical ranges. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to set up alarms that run when drift
metrics exceed thresholds. This enables timely intervention
when data quality issues arise.
- **Create model retraining
prompts**. Establish criteria for when to retrain
your model based on data drift metrics. For example, if
multiple important features show drift, or if a single
critical feature drifts beyond a certain threshold, run the
model retraining process.
- **Set up continuous feedback
loop**. Implement a system to continuously gather
new labeled data for model retraining. This verifies that
your model can adapt to legitimate changes in data
distribution over time. Use
[AWS Step Functions](https://aws.amazon.com/step-functions/) to orchestrate workflows that include
data collection, preprocessing, model training, and
deployment.

## Resources

**Related documents:**

- [Pre-training
Data Bias](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-detect-data-bias.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Data
quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)

**Related videos:**

- [Prepare
data for machine learning with ease, speed, and
accuracy](https://www.youtube.com/watch?v=Wi3eJxfX754)
- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)

**Related examples:**

- [Lab
1. Feature Engineering](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab1-feature-engineering)
- [SageMaker AI
Model Monitor Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)
- [SageMaker AI
Clarify Explainability Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf04-bp04.html*

---

# MLPERF04-BP05 Perform a performance trade-off analysis

Perform a trade-off analysis to identify optimal ML model
configurations that balance competing requirements for your business
needs. This practice enables you to maximize both model accuracy and
overall business value.

**Desired outcome:** You develop a
structured approach to evaluate and select machine learning models
based on multiple dimensions including accuracy, complexity, bias,
fairness, and operational constraints. You'll be able to make
informed decisions about model selection that align with your
business requirements and ethical considerations.

**Common anti-patterns:**

- Focusing solely on model accuracy without considering other
important factors like explainability, fairness, or inference
speed.
- Ignoring bias in training data that may lead to unfair model
outcomes for certain groups.
- Deploying overly complex models that are difficult to explain
and maintain when simpler models could achieve adequate
performance.
- Not testing different model configurations against business
requirements.

**Benefits of establishing this best
practice:**

- Optimized machine learning models that balance performance with
operational constraints.
- Models that can be explained and trusted by stakeholders and end
users.
- Reduced risk of unfair or biased model outcomes.
- Better alignment between model performance and business
requirements.
- More cost-effective model deployment and maintenance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Performance trade-off analysis requires careful consideration of
your use case and business requirements. You need to determine
which aspects of model performance are most important for your
application - whether that's accuracy, explainability, fairness,
latency, or other factors. Different business contexts may
prioritize these dimensions differently.

For example, in a credit scoring application, fairness and
explainability might be primary concerns due to regulatory
requirements and the need to provide reasons for decisions. In
contrast, a real-time product recommendation system might
prioritize prediction speed and accuracy over explainability.
Understanding these requirements upfront can guide your model
development process.

Trade-off analysis is not a one-time activity but should be
incorporated throughout the machine learning lifecycle. As you
gather more data, refine your models, and receive feedback from
stakeholders, you should continually reassess these trade-offs to
verify that your models continue to meet business needs.

### Implementation steps

- **Define performance metrics aligned
with business goals**. Start by clearly defining
what success looks like for your use case. Identify the key
performance indicators (KPIs) that matter most to your
business stakeholders. These might include technical metrics
like precision, recall, or latency, as well as business
metrics like conversion rate or cost reduction.
- **Establish a baseline for trade-off
analysis**. Create a simple model as a baseline to
compare against more complex approaches. This provides a
reference point for measuring improvements and understanding
the minimum acceptable performance for your use case.
Techniques like cross-validation can determine if your
baseline is robust.
- **Explore the accuracy versus
complexity trade-off**. Test models with different
levels of complexity, from simple linear models to more
sophisticated deep learning approaches. Use
[Amazon SageMaker AI Managed MLFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to track different model
architectures and their performance characteristics.
Remember that simpler models are often more explainable and
simpler to deploy, even if they sacrifice some accuracy.
- **Analyze bias and fairness
implications**. Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html) to detect potential bias in your
data and models. Identify sensitive attributes that might
lead to unfair outcomes for certain groups. Implement
mitigation strategies such as balanced datasets,
regularization techniques, or fairness-aware algorithms to
reduce bias while maintaining acceptable performance.
- **Optimize the bias versus variance
trade-off**. Address underfitting (high bias) and
overfitting (high variance) through systematic
experimentation. Techniques like cross-validation can
identify the optimal model complexity for your data.
Consider using more training data, implementing
regularization techniques, or simplifying your model
architecture depending on whether bias or variance is your
primary concern.
- **Evaluate precision versus recall
trade-offs**. For classification problems,
determine whether false positives or false negatives are
more problematic for your use case. Use tools like
precision-recall curves to visualize this trade-off and ROC
curves to understand the relationship between true positive
and false positive rates. Adjust classification thresholds
based on the relative costs of different types of errors.
- **Consider operational
constraints**. Evaluate how models perform under
real-world constraints like latency requirements, memory
limitations, or compute availability. For edge deployment
scenarios, use
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to optimize your models for hardware
targets while maintaining accuracy. This is particularly
important for applications that need to run in
resource-constrained environments.
- **Implement explainability
techniques**. Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) to generate feature importance
explanations and understand how your model makes
predictions. This builds trust with stakeholders and may be
necessary to address regulatory adherence in some
industries. Consider the trade-off between model complexity
and explainability when selecting your final model.
- **Document trade-off
decisions**. Create comprehensive documentation of
your trade-off analysis, including the experiments
performed, results observed, and the rationale behind your
final model selection. This provides transparency for
stakeholders and provides an understanding to future teams
on why certain decisions were made.
- **Establish continuous
monitoring**. After deployment, use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to track model performance
and detect drift in data or predictions. This allows you to
identify when your trade-off assumptions may no longer be
valid and when retraining might be necessary.

## Resources

**Related documents:**

- [Evaluating
ML Models](https://docs.aws.amazon.com/machine-learning/latest/dg/evaluating_models.html)
- [AI
Fairness and Explainability Whitepaper](https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf)
- [Optimize
model performance using Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Accelerating
generative AI development with fully managed MLflow 3.0 on
Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/)
- [Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency
of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/)
- [Unlock
near 3x performance gains with XGBoost and Amazon SageMaker AI
Neo](https://aws.amazon.com/blogs/machine-learning/unlock-performance-gains-with-xgboost-amazon-sagemaker-neo-and-serverless-artillery/)

**Related videos:**

- [Building
explainable AI models with Amazon SageMaker AI](https://www.youtube.com/watch?v=UbeyQmY1qCw)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf04-bp05.html*

---

# MLPERF04-BP06 Detect performance issues when using transfer learning

Transfer learning can accelerate machine learning development by
using pre-trained models for new tasks. Monitoring the performance
of these transferred models verifies that they yield accurate
results in new contexts and stops inherited weaknesses from
affecting your solutions.

**Desired outcome:** You can
effectively identify and address hidden problems in transfer
learning applications, which improves the reliability of your model
predictions. By implementing proper monitoring and validation
techniques, you gain confidence that inherited prediction weights
perform as expected for your use case while minimizing risks
associated with using pre-trained models.

**Common anti-patterns:**

- Assuming a pre-trained model will automatically perform well on
your task without validation.
- Neglecting to monitor prediction accuracy and model behavior
after transfer learning implementation.
- Failing to examine model predictions for subtle but
consequential errors.
- Overlooking the need to validate input preprocessing techniques
for transferred models.

**Benefits of establishing this best
practice:**

- Early detection of performance issues that might otherwise
remain hidden.
- Improved model reliability and prediction accuracy.
- Better understanding of what capabilities are truly inherited
from pre-trained models.
- Reduced risk of model failures in production environments.
- More effective fine-tuning strategies based on identified
weaknesses.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Transfer learning can dramatically reduce the time and
computational resources needed to develop effective machine
learning models by leveraging knowledge gained from solving one
problem and applying it to a different but related problem.
However, this approach comes with unique challenges that require
careful monitoring and validation.

When using transfer learning, it's essential to understand that
the pre-trained model's performance characteristics may not
directly translate to your use case. The underlying patterns and
relationships learned by the original model might not fully align
with your target domain, leading to subtle but potentially serious
performance issues. These problems can be especially challenging
to identify because they often don't manifest as obvious failures
but rather as biased or suboptimal predictions.

For effective transfer learning implementations, you need
comprehensive monitoring and debugging strategies that can detect
these hidden issues. This involves validating not just overall
model performance but also examining individual predictions,
understanding the inherited capabilities, and properly
preprocessing the inputs.

### Implementation steps

- **Set up Amazon SageMaker AI Debugger for
monitoring**. Configure
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) to monitor your transfer learning
model during training and inference. This service can
identify hidden issues that might otherwise go undetected by
automatically analyzing tensors, tracking model convergence,
and detecting anomalies.
- **Examine model predictions for
errors**. Analyze the outputs of your transfer
learning model to identify patterns in prediction errors.
Look beyond aggregate metrics like accuracy or F1 score to
understand what types of inputs are causing the most
confusion. Create confusion matrices and error distribution
reports to visualize where your model's performance deviates
from expectations.
- **Validate model
robustness**. Test your model's performance under
various input conditions to determine how much of its
robustness comes from the pre-trained weights versus your
fine-tuning process. Perform adversarial testing by
introducing slight variations to inputs and measuring how
the predictions change. Use SageMaker AI Debugger's built-in
rules to detect training anomalies, such as vanishing
gradients or exploding tensors.
- **Verify input preprocessing
methods**. Align your data preprocessing pipeline
with the expectations of the pre-trained model.
Inconsistencies in normalization, tokenization, or feature
engineering can impact performance. Document and validate
the preprocessing steps to maintain consistency between
training and inference stages.
- **Implement continuous performance
monitoring**. Deploy systems to continually monitor
your model's performance after deployment. Configure
automated alerts for deviations in key performance metrics
to catch potential issues early. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) in conjunction with
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to set up comprehensive monitoring
dashboards and alerting systems.
- **Leverage foundation models with
fine-tuning**. When using foundation models for
transfer learning, implement
[Amazon SageMaker AI JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) to access pre-trained models and
fine-tune them for your tasks. Monitor the alignment between
generated outputs and expected results, particularly for
tasks requiring domain-specific knowledge.

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [Data
and model quality monitoring with SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Detecting
data drift using SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/)
- [Detecting
hidden but non-trivial problems in transfer learning models
using Amazon SageMaker AI Debugger](https://aws.amazon.com/blogs/machine-learning/detecting-hidden-but-non-trivial-problems-in-transfer-learning-models-using-amazon-sagemaker-debugger/)

**Related videos:**

- [Introduction
to Amazon SageMaker AI Debugger](https://www.youtube.com/watch?v=MqPdTj0Znwg)
- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf04-bp06.html*

---

# MLPERF05 — Deployment

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MLPERF05-BP01 Evaluate cloud versus edge options for machine learning deployment

Evaluate machine learning deployment options to determine if your
application requires near-instantaneous inference results or needs
to operate without network connectivity. When the lowest possible
latency is essential, deploying inference directly on edge devices
avoids costly roundtrips to cloud API endpoints. Edge deployments
are particularly valuable for use cases like predictive maintenance
in factories, where immediate local responses are critical.

**Desired outcome:** You can make
informed decisions about where to deploy your machine learning
models based on your business requirements. You understand when to
use cloud resources for training and when to deploy optimized models
to edge devices for low-latency inference. Your edge deployments can
operate autonomously when needed while maintaining security,
performance, and the ability to update models as new data becomes
available.

**Common anti-patterns:**

- Defaulting to cloud-based inference without evaluating latency
requirements.
- Deploying models to edge devices without proper optimization,
resulting in poor performance.
- Neglecting to establish a strategy for model updates and
monitoring on edge devices.
- Overlooking security considerations for models deployed at the
edge.
- Failing to evaluate hardware constraints of edge devices before
deployment.

**Benefits of establishing this best
practice:**

- Dramatically reduced inference latency for time-sensitive
applications.
- Ability to operate ML models in environments with limited or no
connectivity.
- Lower operational costs by reducing network traffic and cloud
compute usage.
- Enhanced privacy by keeping sensitive data local to edge
devices.
- Improved resilience against network outages.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning deployments require careful consideration of
where inference should take place based on your use case
requirements. While training complex models is computationally
intensive and best suited for the cloud, inference operations
require less computing power and can often be performed directly
on edge devices.

Avoid defaulting to cloud-based inference without evaluating
latency requirements. Many organizations deploy models to edge
devices without proper optimization, resulting in poor
performance, neglect to establish a strategy for model updates and
monitoring on edge devices, overlook security considerations for
models deployed at the edge, and fail to evaluate hardware
constraints of edge devices before deployment.

When evaluating cloud versus edge deployment, consider factors
like latency requirements, connectivity constraints, data privacy
needs, and the computational capabilities of your edge devices.
For applications requiring real-time responses, such as autonomous
vehicles, industrial equipment monitoring, or smart security
systems, edge deployment reduces network latency and provides
continuous operation even during connectivity disruptions.

AWS provides comprehensive tools to optimize models for edge
deployment while maintaining the ability to train and manage those
models in the cloud. This hybrid approach gives you the best of
both worlds: powerful cloud resources for development and
optimization, with efficient edge deployment for operational
performance.

### Implementation steps

- **Assess your deployment
requirements**. Begin by clearly defining your
application's latency, connectivity, and privacy
requirements. Determine if your use case needs
millisecond-level response times, must function in
environments with unreliable connectivity, or needs to
process sensitive data locally. These factors will guide
your decision between cloud and edge deployment options.
- **Optimize models for edge
deployment**. Training and optimizing machine
learning models require massive computing resources, making
cloud environments ideal for this phase.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides powerful tools for building and
training models that can later be optimized for edge
deployment. Consider the computational constraints of your
target edge devices and select model architectures that
balance accuracy with efficiency.
- **Deploy with Amazon SageMaker AI Neo for
cross-solution compatibility**.
[Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/) enables ML models to be trained once
and run anywhere in the cloud or at the edge. The Neo
compiler reads models exported from various frameworks,
converts them to framework-agnostic representations, and
generates optimized binary code for target hardware. This
process makes your models run faster without accuracy loss.
- **Implement edge ML with AWS IoT Greengrass**.
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/) provides a robust solution for running
ML inferences on edge devices using cloud-trained models.
These models can be built using Amazon SageMaker AI,
[AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/), or
[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/). Models are stored in
[Amazon S3](https://aws.amazon.com/s3/) before deployment to edge devices.

## Resources

**Related documents:**

- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/)
- [Set
up Neo on Edge Devices](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge.html)
- [AWS Internet of
Things](https://aws.amazon.com/iot/)
- [Optimize
image classification on AWS IoT Greengrass using ONNX
Runtime](https://aws.amazon.com/blogs/iot/optimize-image-classification-on-aws-iot-greengrass-using-onnx-runtime/)

**Related videos:**

- [Machine
Learning at the Edge](https://www.youtube.com/watch?v=EAz-qAL5z2U)
- [Getting
Started Using Machine Learning at the Edge](https://pages.awscloud.com/Getting-Started-Using-Machine-Learning-at-the-Edge_2020_0202-IOT_OD.html)
- [AWS IoT Greengrass and Machine Learning at the Edge](https://www.youtube.com/watch?v=keaq6sy46ek)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf05-bp01.html*

---

# MLPERF05-BP02 Choose an optimal deployment option in the cloud

When deploying machine learning models in the cloud, selecting the
right deployment option is crucial for performance efficiency. By
matching your deployment method to your use case requirements for
request frequency, latency, and runtime, you can optimize both
performance and cost.

**Desired outcome:** You can deploy
your machine learning models in a way that meets your application's
needs for throughput, response time, and cost efficiency. The
selected deployment option provides the optimal balance between
performance and resource utilization while accommodating your
workload patterns.

**Common anti-patterns:**

- Deploying models on persistent endpoints regardless of traffic
patterns or workload spikes.
- Overlooking payload size and processing time requirements when
selecting deployment options.
- Using real-time inference for batch processing use cases that
don't require immediate responses.
- Failing to consider cost implications of different deployment
options.
- Not monitoring and optimizing deployment configurations after
initial setup.

**Benefits of establishing this best
practice:**

- Improved cost efficiency by matching resources to actual usage
patterns.
- Enhanced performance through selection of appropriate deployment
methods.
- Better scalability to handle varying workloads.
- Reduced operational overhead with managed deployment options.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Selecting the optimal deployment option for your machine learning
models involves understanding your use case requirements and
matching them to the capabilities of different AWS SageMaker AI
deployment services. Consider factors such as request frequency,
payload size, processing time, and response latency needs.

Avoid deploying models on persistent endpoints regardless of
traffic patterns or workload spikes. Many organizations overlook
payload size and processing time requirements when selecting a
deployment option, use real-time inference for batch processing
use cases that don't require immediate responses, and fail to
consider cost implications of different deployment options.

For time-sensitive applications requiring immediate responses,
real-time inference provides persistent endpoints, while workloads
with inconsistent traffic patterns might benefit from serverless
options that scale automatically. For larger payloads or longer
processing times, asynchronous inference is appropriate, and for
non-time-sensitive bulk processing, batch transformation offers an
efficient option.

Your deployment choice should align with your application's
operational patterns to balance performance and cost efficiency. A
chatbot requiring immediate responses would benefit from real-time
inference, while overnight batch processing of transactions might
use batch transform.

### Implementation steps

- **Evaluate your model deployment
requirements**. Begin by clearly defining your
application's requirements for inference frequency, latency
needs, payload sizes, and budget constraints. Consider how
often model predictions will be requested, how quickly
responses must be delivered, and what resource constraints
you may have.
- **Implement Amazon SageMaker AI Real-time
Inference for continuous, low-latency needs**.
Deploy models that require near-instantaneous responses and
consistent availability using
[SageMaker AI
real-time endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html). These fully managed endpoints
support auto-scaling and are ideal for applications like
real-time recommendation engines, chatbots, or fraud
detection systems where immediate response is critical.
- **Implement Amazon SageMaker AI
Serverless Inference for variable traffic
patterns**. For workloads with inconsistent request
patterns or idle periods between traffic spikes, use
[SageMaker AI
Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html). This option automatically
provisions and scales compute resources based on traffic,
avoiding the need to manage server infrastructure while
optimizing costs during periods of low utilization.
- **Implement Amazon SageMaker AI
Asynchronous Inference for large payloads or long
processing**. For use cases involving large input
files (up to 1GB) or models requiring extended processing
time (up to 15 minutes), deploy using
[SageMaker AI
Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html). This option queues incoming
requests and processes them when resources are available,
making it ideal for tasks like video processing, large
document analysis, or complex NLP tasks.
- **Implement Amazon SageMaker AI Batch
Transform for scheduled bulk processing**. For
non-time-sensitive workloads where predictions can be
processed in batches, such as overnight processing of
transactions or weekly sentiment analysis of customer
feedback, use
[SageMaker AI
Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html). This option automatically
distributes workloads across compute instances and shuts
down resources when processing is complete.
- **Monitor and optimize your
deployment**. Once deployed, continuously monitor
your model's performance, resource utilization, and costs.
Use Amazon CloudWatch metrics to track invocation metrics,
errors, latency, and resource utilization. Adjust
auto-scaling configurations or switch deployment options if
your usage patterns change over time.
- **Implement security and
governance**. Incorporate proper security controls
in your model deployments, including IAM roles with least
privilege access, network isolation where appropriate, and
encryption of data in transit and at rest. Use
[Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html) to create persona-based IAM
roles for different ML user types (data scientists, MLOps
engineers, business analysts) with preconfigured templates
that follow least-privilege principles. For regulated
industries, implement model governance practices to track
model versions, approvals, and changes.

## Resources

**Related documents:**

- [Real-time
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
- [Batch
transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)
- [Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html)
- [Deploy
models with Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/inference/index.html)
- [Deploying
ML models using SageMaker AI Serverless Inference](https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/)
- [Optimize
deployment cost of Amazon SageMaker AI JumpStart foundation
models with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/)
- [Announcing
managed inference for Hugging Face models in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/announcing-managed-inference-for-hugging-face-models-in-amazon-sagemaker/)
- [Run
computer vision inference on large videos with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/)

**Related videos:**

- [Achieve high
performance and cost-effective model deployment](https://youtu.be/gWuO0gNKlm8)
- [Amazon SageMaker AI serverless inference](https://youtu.be/KB6vLQGixjA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf05-bp02.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
