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
