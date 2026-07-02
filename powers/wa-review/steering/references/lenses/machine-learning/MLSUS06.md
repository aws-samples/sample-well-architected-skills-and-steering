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
