# MLCOST06 — Monitoring

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# MLCOST06-BP01 Monitor usage and cost by ML activity

Use cloud resource tagging to manage, identify, organize, search
for, and filter resources. Tags categorize resources by purpose,
owner, environment, or other criteria. Associate costs with
resources using ML activity categories, such as re-training and
hosting, by using tagging to manage and optimize cost in deployment
phases. Tagging can be useful for generating billing reports with
breakdown of cost by associated resources.

**Desired outcome:** You gain
visibility into your machine learning costs by activity type,
allowing for better allocation, forecasting, and optimization of ML
resources. You can track expenses across different phases of the ML
lifecycle including development, training, and deployment. This
enables data-driven decisions about resource allocation and
identifies cost-saving opportunities while maintaining performance.

**Common anti-patterns:**

- Using default AWS account structure without proper tagging
strategy for ML resources.
- Not separating costs between development, training, and
production environments.
- Failing to automate tagging as part of resource provisioning.
- Overlooking unused or idle resources that continue to incur
costs.

**Benefits of establishing this best
practice:**

- Clear visibility into costs associated with different ML
activities.
- Ability to allocate costs to appropriate business units or
projects.
- Improved forecasting and budgeting for ML initiatives.
- Identification of cost-saving opportunities across the ML
lifecycle.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Monitoring and optimizing costs for machine learning workloads
requires a systematic approach to resource tagging and usage
tracking. ML workloads typically have distinct phases—development,
training, inference, and experimentation—each with different
resource requirements and cost profiles. By implementing a
comprehensive tagging strategy, you can track and attribute costs
to specific ML activities, making it more straightforward to
understand where your cloud spend is going and identify
opportunities for optimization.

AWS provides various tools and services to implement cost
monitoring for ML workloads. With proper tagging, you can generate
detailed cost reports, set up budgets with alerts, and make
data-driven decisions about resource allocation. This practice is
particularly important for ML workloads, which can be
compute-intensive and potentially costly if not properly managed.

### Implementation steps

- **Establish a tagging strategy for ML
resources**. Create a consistent tagging schema
that captures relevant dimensions for ML activities. Include
tags for project name, environment (development, testing,
and production), ML phase (training, inference, and
experiment), owner, and cost center. Document this strategy
and verify that your team members understand and follow it
when creating resources.
- **Implement AWS tagging**. A
[tag](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
is a label that you or AWS assigns to an AWS resource. Each
tag consists of a key and a value. For each resource, each
tag key must be unique, and each tag key can have only one
value. You can use tags to organize your resources, and cost
allocation tags to track your AWS costs on a detailed level.
AWS uses the cost allocation tags to organize your resource
costs on your cost allocation report. This streamlines
categorizing and tracking your AWS costs. AWS provides two
types of cost allocation tags, an AWS-generated tag and
user-defined tags.
- **Activate cost allocation
tags**. After creating your tags, you need to
activate them for cost tracking in the AWS Billing and Cost Management and Cost
Management console. Note that it can take up to 24 hours for
new tags to appear in your billing reports.
- **Automate resource
tagging**. Use AWS CloudFormation templates, AWS CDK, or Terraform to automate the application of tags when
provisioning resources. For SageMaker AI resources, implement
tagging in your deployment pipelines and notebook
initialization scripts. Consider using AWS Tag Editor for
bulk tagging operations on existing resources.
- **Use AWS Budgets to keep track of
cost**. AWS Budgets can track your Amazon SageMaker AI cost, including development, training, and hosting. You
can also set alerts and get a notification when your cost or
usage exceeds (or is forecasted to exceed) your budgeted
amount. After you create your budget, you can track the
progress on the AWS Budgets console.
- **Implement cost monitoring and
reporting**. Use AWS Cost Explorer to visualize and
analyze your ML costs across different dimensions. Create
custom reports filtered by your ML activity tags to
understand spending patterns. Schedule regular exports of
cost reports for stakeholders review.
- **Establish cost optimization
processes**. Regularly review resource utilization
and costs to identify optimization opportunities. Implement
automated shutdown of idle resources such as SageMaker AI
notebooks when not in use. Consider using SageMaker AI Managed
Spot Training to reduce training costs by up to 90%.
- **Create governance for
tagging**. Use AWS Config Rules or AWS CloudFormation Hooks to enforce tagging policies. Implement
processes to review and correct untagged or incorrectly
tagged resources. Consider using AWS Organizations Tag
Policies to standardize tags across multiple accounts.
- **Implement enhanced cost tracking
with improved tagging**. Use enhanced AWS tagging
capabilities with better automation and governance features
to make your cost allocation more consistent across ML
workloads and improve your visibility into spending
patterns.
- **Use cost optimization
services**. Use AWS Cost Anomaly Detection to
identify unusual spending patterns in your ML workloads.
Consider AWS Compute Optimizer for recommendations on
right-sizing your ML compute resources based on historical
utilization data.

## Resources

**Related documents:**

- [Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Managing
your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Getting
started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- [What
is Tag Editor?](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 1: Overview](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp01.html*

---

# MLCOST06-BP02 Monitor return on investment for ML models

Once a model is deployed into production, establish a reporting
capability to track the value which is being delivered. For example:

- **If a model is used to support customer
acquisition:** How many new customers are acquired and what
is their spend when the model's advice is used compared with a
baseline?
- **If a model is used to predict
when maintenance is needed:** What savings are being made
by optimizing the maintenance cycle?

Effective reporting compares the value delivered by an ML model
against the ongoing runtime cost and to take appropriate action. If
the ROI is substantially positive, are there ways in which this
might be scaled to similar challenges, for example. If the ROI is
negative, could this be addressed by remedial action, such as
reducing the model latency by using serverless inference, or
reducing the run time cost by changing the compromise between model
accuracy and model complexity, or layering in an additional simpler
model to triage or filter the cases that are submitted to the full
model.

**Desired outcome:** By implementing
this practice, you establish a clear line of sight between your ML
investments and business outcomes. You can continuously track the
value delivered by your ML models in terms of measurable business
KPIs, enabling data-driven decisions about scaling successful
models, optimizing underperforming ones, or sunsetting those with
negative ROI. Your organization has transparency into the
cost-effectiveness of ML initiatives and can strategically allocate
resources based on proven business value.

**Common anti-patterns:**

- Deploying ML models without defining success metrics or business
KPIs.
- Focusing only on technical metrics like accuracy without linking
to business outcomes.
- Measuring ROI only once after initial deployment rather than
continuously.
- Failing to account for the full costs of ML model operation in
ROI calculations.
- Ignoring opportunities to scale successful models to similar
business challenges.

**Benefits of establishing this best
practice:**

- Clear visibility into the business value generated by ML
investments.
- Ability to make data-driven decisions about model optimization
or retirement.
- Improved accountability for ML investments across the
organization.
- Better allocation of ML resources to high-impact use cases.
- Enhanced stakeholder confidence in ML initiatives through
transparent reporting.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitoring the return on investment for your ML models requires an
intentional approach that connects technical model performance
with tangible business outcomes. You need to establish a
continuous feedback loop between model operations and business
metrics to understand the true value being generated. This means
going beyond traditional ML metrics like accuracy or precision and
focusing on how the model's predictions translate into business
results.

Start by defining clear business KPIs that your model is expected
to influence before deployment. These KPIs should be measurable
and directly tied to business objectives, such as increased
revenue, reduced costs, or improved customer satisfaction. For
customer acquisition models, track metrics like conversion rates,
customer lifetime value, and acquisition costs. For predictive
maintenance models, measure metrics like maintenance cost savings,
reduced downtime, and extended equipment lifespan.

Once deployed, collect data on both the model's performance and
these business metrics to establish correlation between the two.
Use A/B testing where possible to compare outcomes with and
without the model's influence. This can isolate the specific
impact of your ML investment against other factors that might
affect business outcomes.

Regularly review the ROI of your models and be prepared to take
action based on the findings. For models with strong positive ROI,
explore opportunities to scale the approach to similar business
problems or increase the scope of the current implementation. For
models with marginal or negative ROI, consider optimization
strategies like reducing inference costs through more efficient
infrastructure, simplifying model complexity while maintaining
acceptable accuracy, or implementing a multi-tiered approach where
simpler models handle routine cases and complex models only
process edge cases.

### Implementation steps

- **Define business-oriented success
metrics.** Before deploying your ML model, clearly
define the business KPIs that will be used to measure its
impact. Work with business stakeholders to connect these
metrics directly to business outcomes and measure them
practically. For example, for a customer churn prediction
model, success metrics might include reduction in churn
rate, increase in retention-driven revenue, and decreased
cost of retention campaigns.
- **Establish baseline
performance.** Measure and document the current
performance on your defined KPIs before implementing the ML
model. This baseline is essential for determining the
incremental value the model delivers. Consider using A/B
testing approaches where feasible, sending some cases
through the ML-driven process and others through the
traditional approach.
- **Implement data collection
pipelines.** Set up automated data collection for
both model metrics and business outcomes. Use AWS services
like
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor technical aspects of your model
and
[Amazon Kinesis](https://aws.amazon.com/kinesis/) to capture business event data. Store this
data in [Amazon S3](https://aws.amazon.com/s3/) or
[Amazon Redshift](https://aws.amazon.com/redshift/) for further analysis.
- **Create ROI dashboards using Quick.** Develop business-focused dashboards
in
[Quick](https://aws.amazon.com/quicksight/) that visualize the relationship between
model performance and business outcomes. Include metrics
that show both the value generated (increased revenue, cost
savings) and costs incurred (infrastructure, maintenance,
human review). Use QuickSight's ML Insights to automatically
identify trends and anomalies in your ROI data.
- **Schedule regular ROI
reviews.** Establish a cadence for reviewing model
ROI with both technical and business stakeholders. These
reviews should assess whether the model continues to deliver
positive business impact and identify opportunities for
optimization. Use these sessions to make data-driven
decisions about continuing investment, scaling successful
approaches, or adjusting underperforming models.
- **Optimize underperforming
models.** For models not meeting ROI targets,
implement strategic improvements. Consider
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) Serverless Inference to reduce costs for
infrequent or variable workloads. Explore model compression
techniques like
[SageMaker AI
Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to improve inference efficiency without
sacrificing accuracy. Implement tiered prediction approaches
where simple, low-cost models filter cases before routing to
more complex models.
- **Scale successful models.**
When models demonstrate strong positive ROI, look for
opportunities to expand their impact. Apply similar modeling
approaches to related business problems, increase the scope
of existing models, or integrate the model with additional
business processes to maximize value creation.
- **Use enhanced QuickSight capabilities
for ROI analysis**. Use improved
[Quick](https://aws.amazon.com/quicksight/) with generative AI insights and natural
language query capabilities to automatically identify
trends, anomalies, and optimization opportunities in your
ROI data.
- **Use generative AI for enhanced
insights.** Use generative AI capabilities through
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to analyze patterns in your ROI data and
suggest optimization strategies. Generative AI can identify
non-obvious correlations between model configurations and
business outcomes, leading to better ROI optimization
decisions.

## Resources

**Related documents:**

- [What
is Quick?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)
- [Publish
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [What
are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
- [Quick](https://aws.amazon.com/quicksight/)
- [Cost
Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp02.html*

---

# MLCOST06-BP03 Monitor endpoint usage and right-size the instance fleet

Use efficient compute resources to run models in production. Monitor
your endpoint usage and right-size the instance fleet. Use automatic
scaling (auto scaling) for your hosted models. *Auto
scaling* dynamically adjusts the number of instances
provisioned for a model in response to changes in your workload.

**Desired outcome:** You have
optimized SageMaker AI endpoints that automatically adjust to workload
demands while maintaining performance and minimizing costs. Your
model deployment uses appropriately sized instances that are neither
over-provisioned nor under-provisioned, and you have continuous
monitoring in place to inform scaling decisions.

**Common anti-patterns:**

- Provisioning static endpoint configurations that remain
unchanged regardless of workload fluctuations.
- Over-provisioning instances "just to be safe"
without analyzing actual resource utilization.
- Ignoring endpoint metrics and failing to adjust resource
allocation based on usage patterns.
- Deploying resources across different Availability Zones without
consideration for data transfer costs.
- Using default instance types without evaluating performance
requirements.

**Benefits of establishing this best
practice:**

- Reduced compute costs by reducing over-provisioned resources.
- Improved performance during peak usage periods through automatic
scaling.
- Higher resource utilization through right-sizing.
- Increased availability by distributing instances across
Availability Zones.
- Better understanding of model usage patterns to inform future
optimizations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitoring and optimizing your SageMaker AI endpoints is essential
for maintaining cost-efficiency while providing high availability
and performance. By implementing CloudWatch monitoring and auto
scaling, your deployments use only the resources they needs when
they need them. Start by establishing baseline metrics for your
endpoints to understand typical usage patterns and resource
requirements. Then implement auto scaling policies based on these
metrics to automatically adjust capacity in response to changing
workloads.

For production environments, distribute your endpoint deployment
across multiple Availability Zones to maintain high availability.
Consider the placement of related resources, such as data storage
solutions like FSx for Lustre, to minimize cross-AZ data transfer
costs and optimize performance. Regular review of your metrics and
scaling configurations assists you to continuously refine your
deployment for optimal cost and performance.

### Implementation steps

- **Monitor Amazon SageMaker AI endpoints
with Amazon CloudWatch**. You can monitor Amazon SageMaker AI using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), which collects raw data and processes it
into readable, near real-time metrics. Use metrics such as
CPUUtilization, GPUUtilization, MemoryUtilization, and
DiskUtilization to view your endpoint's resource utilization
and make informed decisions about right-sizing your endpoint
instances. Set up CloudWatch dashboards to visualize these
metrics over time and identify patterns in resource usage.
- **Implement CloudWatch alarms for
proactive monitoring**. Configure alarms for key
metrics that can indicate when an endpoint is
under-provisioned or over-provisioned. For example, set up
alarms that go off when CPU utilization consistently exceeds
80% (indicating potential under-provisioning) or remains
below 20% (indicating over-provisioning). These alarms can
notify your team to take action or run automated responses
through AWS Lambda functions.
- **Configure auto scaling for SageMaker AI
endpoints**.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) supports auto scaling that monitors your
workloads and dynamically adjusts capacity to maintain
steady performance at the lowest possible cost. When
workload increases, auto scaling brings more instances
online. When workload decreases, auto scaling removes
unnecessary instances, which can reduce compute costs.
Define appropriate scaling policies based on your
application's requirements, including minimum and maximum
instance counts, target metrics, and scale-in and scale-out
cooldown periods.
- **Distribute instances across
Availability Zones**. SageMaker AI automatically
attempts to distribute your instances across Availability
Zones, so deploy multiple instances for each production
endpoint to provide high availability. If you're using a
VPC, configure at least two subnets in different
Availability Zones to allow SageMaker AI to distribute your
instances across those zones, providing resilience against
zone failures.
- **Optimize resource placement for data
access**. When using
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) as an input data source for SageMaker AI,
deploy FSx for Lustre and SageMaker AI in the same Availability
Zone to avoid cross-AZ data transfer costs. This
configuration removes the initial Amazon S3 download step,
accelerating ML training jobs while minimizing costs.
Consider similar placement strategies for other related
resources to optimize performance and cost.
- **Regularly review and adjust instance
types**. Periodically evaluate whether your
selected instance types are appropriate for your workload.
SageMaker AI offers a variety of
[instance
types](https://aws.amazon.com/sagemaker/pricing/) optimized for different workload
characteristics. Analyze your CloudWatch metrics to
determine if you could achieve better price-performance by
switching to a different instance family, such as
compute-optimized, memory-optimized, or GPU instances.
- **Use inference optimization
techniques**. Implement model optimization
techniques such as
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to automatically optimize models for
your target hardware, improving performance and potentially
allowing you to use smaller instance types. Consider
techniques like model compression, quantization, and
batching to improve inference efficiency and throughput.
- **Use enhanced SageMaker AI Inference
Recommender**. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) with enhanced algorithms and
support for multi-model endpoints to get sophisticated
instance selection and cost optimization recommendations.
- **Implement specialized instance types
for generative AI models**. For large language
models and other generative AI workloads, use specialized
instances like
[AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) or
[AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), which are designed specifically for machine
learning inference and training. These instances can provide
significant cost savings compared to general-purpose GPU
instances when running transformer-based models. Consider
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for fully managed generative AI capabilities
with built-in scaling.

## Resources

**Related documents:**

- [Amazon SageMaker AI metrics in Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
- [Best
practices for deploying models on SageMaker AI Hosting
Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp03.html*

---

# MLCOST06-BP04 Enable debugging and logging

Implementing comprehensive logging and debugging capabilities for
your machine learning workflows assists you to understand resource
consumption patterns and identify optimization opportunities. By
collecting and analyzing runtime metrics, you can reduce costs and
enhance the efficiency of your ML training operations.

**Desired outcome:** You gain
visibility into training jobs through metrics and logs that reveal
resource consumption patterns. This practice identifies optimization
opportunities, reduces costs, and improves ML model training
performance. You implement monitoring systems to track compute and
storage utilization, and instrument code to record key metrics.

**Common anti-patterns:**

- Training ML models without performance visibility.
- Ignoring resource consumption data until costs become
problematic.
- Deploying ML solutions without adequate logging infrastructure.
- Using manual methods to track performance metrics.
- Waiting for issues to arise before implementing monitoring.

**Benefits of establishing this best
practice:**

- Early identification of model training inefficiencies.
- Reduced compute and storage costs through resource optimization.
- Faster troubleshooting of training job issues.
- Enhanced visibility into ML pipelines.
- Data-driven decisions for infrastructure provisioning.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Proper debugging and logging are crucial for cost management in
machine learning workflows. As ML models grow in complexity, the
computational resources required for training also increase. By
implementing comprehensive monitoring, you can identify
inefficiencies, optimize resource allocation, and reduce overall
costs.

Effective logging and debugging require instrumentation at
multiple levels, from the ML code itself to the underlying
infrastructure. This visibility provides an understanding of how
resources are being utilized during training jobs and identifies
bottlenecks so that you can make data-driven decisions about when
and how to scale resources. The metrics and logs collected can
reveal patterns of inefficient resource utilization that might
otherwise go unnoticed.

Additionally, monitoring storage consumption is important as data
preparation and feature engineering can generate large
intermediate datasets. By tracking both compute and storage
metrics, you can identify opportunities for optimization across
your entire ML pipeline.

### Implementation steps

- **Set up Amazon SageMaker AI
Debugger**.
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) captures training job states at
regular intervals, providing visibility into the ML training
process. It monitors, records, and analyzes data during
training, enabling you to:

Track model parameters, gradients, and tensor values
- Identify training issues like vanishing gradients or
tensor explosions
- Receive automated alerts for common training problems
- Visualize and analyze captured data interactively

- **Implement CloudWatch
logging**. Integrate
[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) with your SageMaker AI training jobs to
centralize and analyze log data. Configure CloudWatch to:

Collect standard output and error logs from training
jobs
- Encrypt log data using an
[AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) for security
- Set up custom log groups and streams for different ML
workflows
- Create log retention policies to manage storage costs

- **Instrument ML code for metrics
collection**. Add instrumentation code to your ML
training scripts to capture performance metrics and resource
utilization data:

Track timing information for different training phases
- Monitor memory usage during training operations
- Record batch processing statistics and convergence
metrics
- Log hyperparameter values and their impact on training
performance

- **Configure resource
monitoring**. Set up monitoring for compute and
storage resources used by your ML workflows:

Use CloudWatch metrics to track instance utilization
- Monitor data transfer volumes between storage and
compute resources
- Set up alerts for abnormal resource consumption patterns
- Create dashboards to visualize resource utilization
trends

- **Implement automated
alerting**. Configure notification systems to alert
you when resource consumption exceeds expected thresholds:

Set up CloudWatch alarms for high CPU, memory, or GPU
utilization
- Create alerts for extended training job durations
- Configure notifications for storage capacity issues
- Establish alerting for debugging rule violations in
SageMaker AI Debugger

- **Analyze and optimize training
jobs**. Use the collected metrics and logs to
identify optimization opportunities:

Review resource utilization patterns to identify
right-sizing opportunities
- Analyze training job logs for inefficient code paths
- Examine data loading and preprocessing bottlenecks
- Optimize hyperparameters based on performance metrics

- **Use enhanced debugging
capabilities**. Use improved SageMaker AI Studio
debugging and monitoring capabilities with better
integration to popular ML frameworks and enhanced
visualization tools for more efficient troubleshooting.
- **Use generative AI for log
analysis**. Use generative AI capabilities to
analyze and extract insights from ML training logs. Utilize
Q Diagnostics integrated into the console or your preferred
IDE for log analysis.

Implement natural language processing to summarize log
patterns
- Use Amazon Bedrock to build intelligent log analysis
assistants
- Deploy ML models that can predict resource needs based
on historical data
- Create automated reports of cost optimization
opportunities from log data

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [What
is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [Analyzing
log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [Logging
and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-incident-response.html)
- [Logging
Amazon ML API Calls with AWS CloudTrail](https://docs.aws.amazon.com/machine-learning/latest/dg/logging-using-cloudtrail.html)
- [Amazon SageMaker AI Debugger API](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html)

**Related examples:**

- [Debugger
example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-debugger))
- [SageMaker AI
Debugger GitHub Repository](https://github.com/awslabs/sagemaker-debugger)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp04.html*

---
