# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 5

---

# GENOPS01 — Model performance evaluation

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GENOPS01-BP01 Periodically evaluate functional performance

Implement periodic evaluations using stratified sampling and custom
metrics to maintain the performance and reliability of large
language models. This practice verifies that models remain accurate
and relevant over time by regularly assessing their performance
against ground truth data and specific evaluation criteria. By
employing stratified sampling, organizations can obtain a
representative subset of data that reflects the diversity of
real-world inputs, leading to more reliable performance metrics.
Custom metrics allow for tailored assessments that align with
specific business goals and user expectations. This practice helps
customers achieve consistent model performance, detect and address
model drift promptly, and integrate evaluation results into
continuous improvement processes.

**Desired outcome:** When
implemented, this best practice improves the ability to identify and
remediate performance degradation issues in model responses.

**Benefits of establishing this best
practice:**

- [Implement
observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Model responses
to prompts can be observed using key performance indicators
(KPIs) to determine adherence to or deviation from acceptable
performance levels.
- [Anticipate
failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Periodic review of the model's performance
levels helps you proactively identify deviations in its
performance. This is because foundation models are inherently
non-deterministic with a realistic chance of failure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Evaluations can be conducted by periodically running ground truth
data and applying sampling techniques to run metrics for
monitoring purposes. Feed your prompts into the model to generate
outputs, compare those outputs to the known ground truth values,
and analyze the results to track the model's performance over
time, identifying potential drifts or degradation.

You can employ stratified sampling techniques to verify diverse
data representation within the sample set. Divide your ground
truth data into relevant categories (for example, different user
personas), and randomly sample from each category to provide a
balanced representation in the evaluation set. Consider
periodically updating your ground truth dataset as the inputs and
usage of your workload change over time. Address data drift where
actual usage diverges from your initial ground truth set.

You can use the model evaluation feature built-in with Amazon Bedrock or open-source libraries like
[fmeval](https://github.com/aws/fmeval) or
[ragas](https://docs.ragas.io/en/stable/).
Use Amazon Bedrock model invocation logging to collect metadata,
requests, and responses for model invocations in your account.

For Amazon SageMaker AI, you can set up manual evaluations for a
human workforce using Studio, automatically evaluate your model
with an algorithm using Studio, or automatically evaluate your
model with a customized workflow using the fmeval library.

The fmeval library provides a framework for defining and using
custom metrics. By creating a custom metric class, you can
encapsulate the logic for calculating a specific evaluation
criterion tailored to your use case. Use this to continuously
assess your language models using both standard metrics provided
by fmeval and your own specialized metrics.

Your organization’s AI policy should define the effective minimum performance levels for generative AI workloads, as well as how to validate performance on an ongoing basis. Consider identifying a single-threaded workload owner responsible for the operational considerations pertaining to ongoing performance evaluations. Run these evaluations when new candidate models are available, or when model customization techniques are applied. For example, fine-tuned and customized models should be subject to the same evaluation criteria and cadence as non-customized models.

### Implementation steps

- Create a ground truth dataset.

Verify that you have diverse data representation
- Consider various user personas and use cases

- Apply stratified sampling techniques.

Categorize ground truth data into relevant groups
- Randomly sample from each group to achieve balanced
representation

- Establish periodic evaluation processes.

For Amazon Bedrock:

Use the built-in model evaluation feature
- Implement model invocation logging

- For Amazon SageMaker AI:

Configure manual evaluations using Amazon SageMaker AI
Studio.
- Set up automatic evaluations using Amazon SageMaker AI
Studio or the fmeval library

- Define custom metrics.

Use the fmeval library to create custom metric classes
- Encapsulate logic for calculating specific evaluation
criteria

- Perform model evaluations.

Input prompts into the model
- Generate outputs and compare them to ground truth values
- Analyze results to track performance over time

- Monitor for performance drifts.

Identify potential degradation in model performance
- Address data drift where actual usage diverges from the
initial ground truth

- Regularly update the ground truth dataset.

Reflect changes in workload inputs and usage patterns
- Maintain the relevance of evaluation data

**Additional recommendations**

- Use open-source libraries.

Consider using libraries like ragas for additional
evaluation capabilities
- Explore complementary metrics and evaluation techniques

- Implement automated workflows.

Integrate evaluation processes into CI/CD pipelines
- Set up alerts for significant performance changes

## Resources

**Related best practices:**

- [OPS11-BP11](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_metrics_review.html)

**Related documents:**

- [Amazon SageMaker AI Model Evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-evaluate.html)
- [Evaluating
Models in Amazon Bedrock](https://aws.amazon.com/bedrock/evaluations/)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)

**Related videos:**

- [AWS re:Invent 2024 - Streamline RAG and model evaluation with
Amazon Bedrock (AIM359)](https://www.youtube.com/watch?v=7BP9nwFlFws)

**Related examples:**

- [SageMaker AI
Model Evaluation Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-test-model.html)
- [Bedrock
Model Evaluation Demo](https://aws.amazon.com/awstv/watch/1a5442fac30/)
- [Examples
with fmeval](https://github.com/aws/fmeval/tree/main/examples)

**Related tools:**

- [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [fmeval
library](https://github.com/aws/fmeval)
- [Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [AWS Step Functions](https://aws.amazon.com/blogs/aws/build-generative-ai-apps-using-aws-step-functions-and-amazon-bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01-bp01.html*

---

# GENOPS01-BP02 Collect and monitor user feedback

Supplement model performance evaluation with direct feedback from
users. Implement continuous feedback loops to optimize application
performance and enhance user satisfaction. Systematically collect,
analyze, and act on user feedback to drive continuous improvement.
By integrating this approach, you can achieve higher operational
excellence and reliability, which keeps applications performant and
aligned with user expectations. This proactive strategy helps to
improve user satisfaction and foster a culture of ongoing
enhancement and innovation.

**Desired outcome:** When
implemented, this best practice improves the ability to surface
performance degradation issues with foundation models as they happen
without requiring ground truth data.

**Benefits this practice helps
achieve:**

- [Implement
observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - User feedback
from model responses to prompts can inform the efficacy of a
model, a prompt, or both in addressing a customer problem.
- [Anticipate
failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Periodic review of the user feedback helps you
proactively identify deviations in subjective evaluation of a
model's performance. This is because foundation models are
inherently non-deterministic with a realistic chance
of failure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Collect and monitor user feedback to establish continuous
improvement and optimization of your applications. User feedback
can be as simple as thumbs up or thumbs down, which you can
capture in your application and store in a database. This approach
helps detect issues early in the process and serves as a feedback
mechanism for prompt engineering.

Regularly review monitoring data, user feedback, and incident
reports related to your application's integration with Amazon Bedrock and Amazon SageMaker AI models. Use these insights to
identify potential improvements, such as optimizing data
pipelines, refining integration patterns, or exploring new model
capabilities.

[Amazon Q Business](https://aws.amazon.com/q/business/) offers tools to monitor and analyze user feedback.
These include an analytics dashboard in the console that provides
usage trends, user conversations, query trends, and user feedback.
Use these insights to optimize your application and identify areas
for improvement. Use the `PutFeedback` API action
to allow end users to provide feedback on chat responses. This
captures user sentiment and helps improve response quality.

Consult your organization’s AI policy document for guidance on how to use user feedback for workload improvements. Direct techniques for incorporating user feedback like reinforcement learning through human feedback may not be applicable for all workloads. Workload owners may be best positioned to identify the appropriate feedback incorporation strategy for a given task.

### Implementation steps

- For Amazon Q Business, set up user feedback collection.

Integrate simple feedback options within the application
- Use the `PutFeedback` API action
through AWS SDK for application integration
- Use Amazon Q Business usage trends and query analysis
- Consider storing feedback in Amazon DynamoDB for
scalable, low-latency storage
- Enable conversation logging to get more insights from
user interactions

Configure log delivery (choose between Amazon S3,
CloudWatch Logs, or Amazon Data Firehose)
- Set up filtering if you need to exclude sensitive
information
- Enable logging to start streaming conversation and
feedback data

- For Amazon Bedrock, set up user feedback collection.

Create an Amazon S3 bucket to store user feedback
- Develop a web form or API endpoint to collect user
feedback
- Create an AWS Lambda function to process incoming
feedback
- Set up an Amazon EventBridge rule to run the Lambda
function when new feedback is added to the S3 bucket

- Establish a regular review process.

Schedule periodic reviews of monitoring data, user
feedback, and incident reports
- Create an AWS Step Functions workflow to manage the
feedback processing pipeline
- Consider Amazon Bedrock's large language models to
analyze the feedback
- Consider Quick to create dashboards and
visualizations of the feedback data

- Implement and test improvements.

Identify optimizations in data pipelines, integration
patterns, or model capabilities
- Track KPIs before and after improvements
- Develop and deploy optimizations
- Validate improvements using A/B testing

## Resources

**Related best practices:**

- [OPS04-BP03](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_customer_telemetry.html)

**Related documents:**

- [Guidance
for Capturing and Analyzing Unstructured Customer Feedback on
AWS](https://aws.amazon.com/solutions/guidance/capturing-and-analyzing-unstructured-customer-feedback-on-aws/)
- [Build
an automated insight extraction framework for customer
feedback analysis with Amazon Bedrock and Quick](https://aws.amazon.com/blogs/machine-learning/build-an-automated-insight-extraction-framework-for-customer-feedback-analysis-with-amazon-bedrock-and-amazon-quicksight/)
- [Guidance
for Automated Customer Feedback Analysis with Amazon Bedrock](https://aws.amazon.com/solutions/guidance/automated-customer-feedback-analysis-with-amazon-bedrock/)

**Related examples:**

- [PutFeedback
- Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html)
- [Configure
agent to request information from user to increase accuracy of
function prediction - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-user-input.html)

**Related tools:**

- [Amazon Q Business](https://aws.amazon.com/q/business/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Quick](https://aws.amazon.com/quicksight/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01-bp02.html*

---

# GENOPS02 — Monitor and manage operational health

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# GENOPS02-BP01 Monitor all application layers

Implement comprehensive monitoring and logging across all layers of
your generative AI application to maintain operational health,
provide reliability, and optimize performance. This best practice
aims to provide clear visibility into the application's behavior, from user interactions to core model performance. By
tracking key metrics, organizations can quickly identify and address
issues, enhance user experiences, and make data-driven decisions to
improve their AI systems.

**Desired outcome:** When
implemented, your organization closely monitors the performance of
generative AI workloads.

**Benefits of establishing this best
practice:**

- [Implement
observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Monitor the
performance of your generative AI workload at all layers of the
application, increasing visibility into application operational
state and facilitating the early intervention of operational
issues.
- [Learn
from all operational events and metrics](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Capturing
fine-grained observations enables continuous improvement.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Generative AI applications have several layers. First and foremost
is the application layer, which is the software abstraction above
a foundation model. Then, there is a service layer, an optional
gateway that negotiates prompts and brokers responses back to the
application layer. Depending on the use case, the service layer
may interact with a prompt catalog, a vector data store, or
several guardrails before ultimately interacting with a foundation
model. Simple generative AI workloads may respond back to the
service layer and apply configured guardrails where appropriate
before ultimately responding back at the application layer. More
complex workloads may navigate a knowledge graph, run a prompt
flow, or initiate an agent. The different layers and scenarios for
a generative AI application to traverse require proactive
monitoring and application telemetry at each layer.

Managed services like Amazon Bedrock, Amazon Q Business, and
Amazon OpenSearch Service Serverless facilitate much of this
monitoring on your behalf. These managed services integrate
well with monitoring and logging services like Amazon CloudWatch and AWS CloudTrail. Amazon SageMaker AI Inference
Endpoints can also log to CloudWatch. Evaluate different
logging solutions that best suit your needs, and implement
monitoring at each layer of your custom generative AI
workflow. These considerations should also be applied to
generative business intelligence (BI) solutions Quick Q. Monitor the appropriate Quick Q
metrics to identify operational issues when serving generative
BI insights.

In SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, establish comprehensive observability across
infrastructure, service, application, and model performance
layers using SageMaker AI HyperPod's built-in observability
capabilities and AWS monitoring services.

For EKS-based HyperPod, use the one-click observability
feature that automatically installs Amazon EKS add-ons for
consolidated health and performance data from multiple sources
including NVIDIA DCGM, Kubernetes node exporters, Elastic
Fabric Adapter (EFA), and file systems, all accessible through
unified dashboards in Amazon Managed Grafana with metrics
automatically published to Amazon Managed Service for Prometheus.

Configure CloudWatch Container Insights for enhanced
observability of CPU, GPU, Trainium, EFA, and file system
metrics up to the container level, while implementing deep
health checks and automated node recovery monitoring that
tracks schedulable and unschedulable node status.

For Slurm-based HyperPod, implement comprehensive monitoring
through node exporters for CPU load averages, memory, disk
usage, network traffic, and file system metrics, NVIDIA DCGM
for GPU utilization, temperatures, power usage, and memory
monitoring, and EFA metrics for network performance and error
tracking.

Both systems benefit from SageMaker AI HyperPod's unified
observability solution that reduces troubleshooting time from
days to minutes through pre-built actionable insights,
real-time task performance metric tracking with automated
alerting, and automatic root cause remediation with
customer-defined policies, providing comprehensive visibility
into training job performance, resource utilization, and
system health across operational layers.

### Implementation steps

- Identify your application layers, including:

Application layer
- Service layer
- Foundation model layer
- Additional layers (for example, prompt catalog, vector
data store, or knowledge graph)

- For application layer monitoring:

Enable logs and metrics in Amazon CloudWatch
- For custom metrics, set up for application-specific
events and performance indicators

- For service layer monitoring:

Enable logs and metrics in Amazon CloudWatch
- For request flow analysis, implement tracing with AWS X-Ray or use Amazon Bedrock Agent's tracing feature

- For foundation model layer monitoring:

Use built-in monitoring in Amazon Bedrock or Amazon Q Business
- Configure CloudWatch logging for Amazon SageMaker AI
Inference Endpoints

- For additional layer monitoring:

Enable logs and metrics in your chosen vector database,
such as Amazon OpenSearch Service
- Set up CloudWatch logs and metrics for prompt catalogs
or knowledge graphs

- Configure alerting and dashboards.

Set up CloudWatch alarms for critical metrics and
thresholds
- Create CloudWatch dashboards for key performance
indicators

- Configure security monitoring.

Enable AWS CloudTrail for API activity logging
- Set up Amazon GuardDuty for threat detection

- Continually optimize.

Review and analyze log data to identify improvements
- Adjust monitoring configurations based on changing
application needs and usage patterns

- Consider additional logging solutions:

For log ingestion and transformation, consider Amazon Data Firehose
- For as-needed querying, explore Amazon Athena for logs
stored in Amazon S3

## Resources

Related best practices:

- [OPS08-BP01](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_metrics.html)
- [OPS08-BP02](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.html)
- [OPS08-BP03](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_traces.html)
- [OPS08-BP04](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_alerts.html)
- [OPS08-BP05](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_dashboards.html)

**Related documents:**

- [Using
Amazon CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [Using
Amazon CloudWatch Dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [CloudWatch Logs Insights Query Examples](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.html)
- [Publishing
Custom Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)

**Related examples:**

- [Monitor
the health and performance of Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html)
- [Metrics
for monitoring Amazon SageMaker AI with Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [Monitoring
OpenSearch Serverless with Amazon CloudWatch](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/monitoring-cloudwatch.html)
- [Monitoring
Amazon Q Business and Amazon Q Apps with Amazon CloudWatch](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/monitoring-cloudwatch.html)
- [Monitoring
Amazon Q Developer with Amazon CloudWatch](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/monitoring-cloudwatch.html)
- [Accelerate
Foundation Model Development with One-Click Observability in
Amazon SageMaker AI HyperPod](https://aws.amazon.com/blogs/machine-learning/accelerate-foundation-model-development-with-one-click-observability-in-amazon-sagemaker-hyperpod/)
- [Amazon SageMaker AI HyperPod launches model deployments to accelerate
the generative AI model development lifecycle](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-launches-model-deployments-to-accelerate-the-generative-ai-model-development-lifecycle/)

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html)
- [Amazon Athena](https://aws.amazon.com/athena/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon Q](https://aws.amazon.com/q/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp01.html*

---

# GENOPS02-BP02 Monitor foundation model metrics

It's critical to set up continuous monitoring and alerting for
foundation models for performance, security, and cost-efficiency.
This best practice offers a structured approach to monitor models
that fosters rapid identification and resolution of issues like data
drift, model degradation, and security threats. Adopting this
practice enhances reliability, efficiency, and trust in your
applications, driving better business outcomes and user
satisfaction. It can also help you with regulatory compliance and
optimizes resource utilization.

**Desired outcome:** A robust
monitoring system is in place that provides real-time visibility
into the performance of your foundation models, allows for early
detection of anomalies or degradation, and speeds up response to
incidents. This system integrates with your existing observability
tools and processes, providing a holistic view of your application's
health.

**Benefits of establishing this best
practice:**

- [Implement
observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Monitor
foundation model metrics.
- [Learn
from all operational events and metrics](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Capturing
fine-grained observations enables continuous improvement.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To implement comprehensive monitoring for your foundation model
metrics, consider using cloud-native monitoring solutions that
integrate with your AI services. To achieve better performance and
quick incident response, set warning and error thresholds for the
metrics based on your workload's expected patterns. Additionally,
define and practice incident response playbooks for when these
alerts go off. Configure alarms to monitor specific thresholds and
to send notifications or take actions when values exceed those
thresholds. These metrics can be visualized using graphs in the
console.

For applications using Amazon Bedrock, use Amazon CloudWatch to
monitor crucial metrics such as invocation counts, latency, token
usage, error rates, and throttling events. Set up custom
dashboards to visualize these metrics, and configure alarms to
alert you when predefined thresholds are exceeded.

If you're using Amazon SageMaker AI for hosting models, use
the invocation and resource utilization metrics available in
Amazon CloudWatch, such as invocation counts, latency, and
error rates, as well as GPU and memory utilization. The Model
Monitor feature offers additional metrics to help you monitor
and evaluate the performance of your models in production. You
can establish baselines, schedule monitoring jobs, and set up
alerts to detect deviations from predefined thresholds.

For SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, use the system's comprehensive one-click
observability capabilities that automatically collect and
visualize key metrics across operational layers.

For EKS-based HyperPod, use the integrated Amazon EKS add-on
for SageMaker AI HyperPod observability that consolidates health
and performance data from NVIDIA DCGM, Kubernetes node
exporters, Elastic Fabric Adapter (EFA), and file systems into
unified Amazon Managed Grafana dashboards with metrics
automatically published to Amazon Managed Service for Prometheus.

Configure CloudWatch Container Insights for enhanced
monitoring of CPU, GPU, Trainium, EFA, and file system metrics
up to the container level, while implementing automated
alerting for model invocation latency, concurrent requests,
error rates, and token-level metrics.

For Slurm-based HyperPod, implement comprehensive monitoring
through node exporters for system metrics, NVIDIA DCGM for GPU
health monitoring, and EFA metrics for network performance
tracking, all integrated with the unified observability
solution.

Both systems benefit from SageMaker AI HyperPod's real-time task
performance metric tracking with automated alerting
capabilities, automatic root cause remediation with
customer-defined policies, and inference observability that
captures essential model performance data including invocation
latency, concurrent requests, error rates, and token-level
metrics through standardized Prometheus endpoints.

Additionally, establish incident response playbooks for when
alerts trigger, configure custom thresholds based on
workload-specific patterns, and use a unified dashboard that
reduces troubleshooting time from days to minutes through
pre-built, actionable insights.

To enable automated responses to specific events, consider
implementing Amazon EventBridge. It monitors events from other
AWS services in near real-time. Use it to send event
information when they match rules you define, such as state
change events in a training job you've submitted. Configure
your application to respond automatically to these events.

### Implementation steps

- For Amazon Bedrock, enable model invocation logging.

Choose your desired data output options and log
destination (Amazon S3 or CloudWatch Logs)
- Track key metrics like
`InputTokenCount`,
`OutputTokenCount`, and
`InvocationThrottles`
- Use these metrics to understand model usage and
performance
- If needed, implement additional custom logging in your
application using the CloudWatch
`PutMetricData` API

- For Amazon SageMaker AI, implement Amazon SageMaker AI Model
Monitor.

Establish performance baselines for hosted models
- Include graphs for resource utilization (like memory and
GPU) where applicable
- Set up regular monitoring jobs to evaluate model
performance
- Configure alerts for deviations detected during
monitoring

- Set up a dashboard to visualize key metrics.

Create CloudWatch dashboards for your AI services (like
Amazon Bedrock and SageMaker AI)
- Add widgets for important metrics such as invocations,
latency, token counts, and error rates
- Consider implementing anomaly detection algorithms to
identify unusual patterns in data

- Create alarms for critical thresholds.

Elevated latency in model invocations
- High error rates or throttling events

- Implement EventBridge rules.

Create rules to capture significant events from your AI
services
- Set up appropriate targets for these rules (like SNS
topics or Lambda functions) and automate the responses

- Develop incident response playbooks.

Create playbooks for common scenarios (for example, high
latency or increased error rates)
- Define steps for identifying root causes and
implementing mitigations
- Establish procedures for communication and escalation

- Establish a regular review process

Schedule periodic reviews of dashboards and metrics
- Regularly assess and adjust alarm thresholds
- Conduct retrospective reviews on incidents and
near-misses
- Perform periodic audits of your monitoring coverage

## Resources

**Related best practices:**

- [OPS08-BP01](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_metrics.html)
- [OPS08-BP02](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.html)
- [OPS08-BP04](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_alerts.html)
- [OPS08-BP05](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_workload_observability_create_dashboards)

**Related documents:**

- [Monitor
model invocation using CloudWatch Logs - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [Monitor
the health and performance of Amazon Bedrock - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html)
- [Monitoring
Generative AI applications using Amazon Bedrock and Amazon CloudWatch integration | AWS Cloud Operations & Migrations
Blog](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [AWS Well-Architected Framework: Operational Excellence
Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/welcome.html)
- [Accelerate
Foundation Model Development with One-Click Observability in
Amazon SageMaker AI HyperPod](https://aws.amazon.com/blogs/machine-learning/accelerate-foundation-model-development-with-one-click-observability-in-amazon-sagemaker-hyperpod/)
- [Amazon SageMaker AI HyperPod launches model deployments to accelerate
the generative AI model development lifecycle](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-launches-model-deployments-to-accelerate-the-generative-ai-model-development-lifecycle/)

**Related examples:**

- [SageMaker AI
Model Monitor Example Notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)
- [EventBridge
Rules for SageMaker AI Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/automating-sagemaker-with-eventbridge.html)

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/) (for automated responses)
- [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (for notifications)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp02.html*

---

# GENOPS02-BP03 Implement solutions to mitigate the risk of system overload

There are two primary ways to mitigate the risk of system
overload for generative AI workloads. The first is to scale the
inference serving architecture using advanced auto-scaling
technologies. This is possible using Amazon SageMaker AI
Inference Components, which you can use to host and scale model
independent of the underlying infrastructure. For self-hosted
language models, this is the ideal approach.

The second approach is to rate limit and throttle managed
inference to maintain application stability and performance.
This approach is more applicable to managed inference on Amazon
Bedrock. This practice controls request processing rates to
avoid system overload, which provides consistent application
health and a better user experience. You can increase system
throughput by opting for cross-Region inference or in some cases
by purchasing provisioned model thoughput.

By adopting these measures, you can achieve balanced workload
distribution, reduce service disruption risks, and enhance
application reliability. This approach safeguards against
excessive demand, optimizes resource utilization, and improves
cost efficiency and performance.

**Desired outcome:** After
implementing rate limiting and throttling, your organization can
maintain the stability and performance of their AI applications.

**Benefits of establishing this best
practice:**

- [Safely
automate where possible](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Respond to system load events.
- [Anticipate
failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Maximize operational success by implementing
responses to failure scenarios.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For self-hosted models, adopt SageMaker AI Inference
Components. Inference Components are an extension of
multimodel endpoints, and are meant for hosting and scaling
large-language models dynamically. Inference components treat
models as primary elements, scaling the underlying hardware as
needed based on the availability of CPU and GPU resources, as
well as the full inference load on the provisioned
infrastructure. Inference components are meant for workloads
where you have control over the underlying infrastructure, and
therefore should not be considered for generative AI workloads
hosted on managed infrastructure such as Amazon Q for Business
or Amazon Bedrock.

Implementing rate limiting and throttling is crucial for the
stability of generative AI applications. This practice
controls incoming request rates to reduce the risk of system
overload, helping to provide consistent performance and
availability. It helps protect against traffic spikes, can act
as one of the mitigations to denial-of-service attacks, and
promotes fair usage. Benefits include reliable performance,
enhanced security, optimized resource utilization, and
improved user experience, which align with key principles of
reliability, performance efficiency, security, and cost
optimization.

When designing generative AI systems, consider the limitations
of source systems, and implement appropriate measures. The
level of parallelism achievable may be constrained by the
source system's capacity, necessitating the implementation of
throttling mechanisms and backoff techniques. Amazon Bedrock,
like other AWS services, has default quotas (formerly known as
limits) that apply to your account. These quotas are in place
to help maintain steady service performance and appropriate
usage. Given the potential for occasional disruptions and
errors in source systems, robust error handling and retry
logic should be incorporated into the application
architecture. These measures improve success rates, resiliency
in your application, and user experience.

In SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, establish comprehensive request rate controls
and resource throttling mechanisms that help protect your
cluster from overload conditions while maintaining optimal
training performance.

For EKS-based HyperPod, implement rate limiting through
managed Kubernetes orchestration with resource quotas and
limit ranges to control resource consumption at namespace and
pod levels, avoiding system overload during peak demand.
Configure HyperPod Task Governance with intelligent throttling
mechanisms that automatically manage task queues and resource
allocation rates, verifying that production workloads receive
priority processing while development tasks are throttled
appropriately to avoid cluster saturation.

Use horizontal pod autoscaling with conservative scaling
policies and priority classes to implement request throttling
based on workload criticality, while using node selectors to
distribute load across different instance types and reduce
hotspots. The usage reporting feature provides real-time
visibility into resource consumption patterns, enabling
proactive rate limiting adjustments based on GPU, CPU, and
Neuron Core utilization metrics to maintain optimal cluster
performance under varying load conditions.

For Slurm-based HyperPod, use Slurm's native job submission
throttling and fair share scheduling to avoid system overload
by controlling the rate at which jobs are admitted to the
cluster based on available resources and current system load.
Implement quality of service (QoS) policies and job priority
classes that automatically throttle lower-priority workloads
when system resources approach capacity limits, while
maintaining consistent processing rates for critical training
jobs.

Configure resource allocation policies that dynamically adjust
job submission rates based on cluster health metrics, combined
with HyperPod's auto-resume functionality to handle temporary
overload conditions gracefully without cascading failures.

Both systems benefit from implementing circuit breaker
patterns through SageMaker AI HyperPod Recipes that provide
pre-configured throttling mechanisms and rate limiting
strategies optimized for specific model architectures like
Llama and Mistral, providing sustained performance while
reducing resource exhaustion and system instability during
high-demand periods.

The embedding model has important performance considerations
in your application, regardless of whether it's deployed
locally within the pipeline or accessed as an external
service. Embedding models, as foundational models that operate
on GPUs, have finite processing capacity. For locally-run
models, workload distribution must be carefully managed based
on available GPU capacity. When using external models, avoid
overloading the service with excessive requests. In both
scenarios, the level of parallelism is determined by the
embedding model's capabilities not by the compute resources of
the batch processing system. This highlights the importance of
efficient resource allocation and optimization strategies.

### Implementation steps

- Understand your Amazon Bedrock quotas.

Quotas may apply to various aspects of Amazon Bedrock
usage, such as API request rates, token usage, or
concurrent model invocations
- You can view the current quotas for Amazon Bedrock
through the Service Quotas dashboard in the AWS Management Console
- Default quotas may be updated based on factors such as
regional availability and usage patterns
- Some quotas may be specific to particular models or
model families within Amazon Bedrock
- Some quotas may be adjustable, allowing you to request
an increase through the Service Quotas console
- For quotas that cannot be adjusted through Service Quotas, contact Support for guidance

- Implement throttling mechanisms.

Use Amazon API Gateway for rate limiting to control the
number of requests

- Implement backoff techniques.

Use exponential backoff with jitter to handle transient
errors effectively
- Integrate with AWS SDK for Javascript's built-in retry
mechanisms for seamless error recovery

- Design retry logic.

Implement idempotent operations where possible to
facilitate safe retries
- Use AWS Step Functions for managing complex retry
workflows
- Consider circuit breaker patterns for failing fast in
case of repeated failures

- Implement continuous monitoring and optimization.

Use Amazon CloudWatch observability to monitor system
performance
- Conduct regular load testing and capacity planning

## Resources

**Related best practices:**

- [OPS10-BP02](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_event_response_process_per_alert.html)
- [OPS08-BP04](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_workload_observability_create_alerts.html)

**Related documents:**

- [Quotas
for Amazon Bedrock - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
- [Amazon
SDK Developer Guide - Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html)
- [AWS Prescriptive Guidance - Retry behavior](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)

**Related examples:**

- [Supercharge
your auto scaling for generative AI inference – Introducing
Container Caching in SageMaker AI Inference](https://aws.amazon.com/blogs/machine-learning/supercharge-your-auto-scaling-for-generative-ai-inference-introducing-container-caching-in-sagemaker-inference/)
- [Implementing
Rate Limiting with API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)
- [Using
Step Functions for Retry Logic](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-handling-error-conditions.html)
- [Managing
and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 1](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/)
- [Maximize
Accelerator Utilization for Model Development with New Amazon SageMaker AI HyperPod Task Governance](https://aws.amazon.com/blogs/aws/maximize-accelerator-utilization-for-model-development-with-new-amazon-sagemaker-hyperpod-task-governance/)
- [Introducing
Amazon SageMaker AI HyperPod to train foundation models at
scale](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-to-train-foundation-models-at-scale/)
- [Best
practices for Amazon SageMaker AI HyperPod task governance](https://aws.amazon.com/blogs/machine-learning/best-practices-for-amazon-sagemaker-hyperpod-task-governance/)
- [Get
started with Amazon SageMaker AI HyperPod task governance](https://www.youtube.com/watch?v=_wDhBAPwhoM)
- [Usage
reporting for cost attribution in SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting.html)

**Related tools:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS SDK for Javascript](https://aws.amazon.com/sdk-for-javascript/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp03.html*

---

# GENOPS03 — Observability in workloads

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GENOPS03-BP01 Implement prompt template management

Implement and maintain a versioned prompt template management system
to achieve consistent and optimized performance of language models.
This best practice aims to provide a structured approach to managing
prompt templates, which helps teams systematically version, test,
and optimize prompts. By adhering to this practice, you can achieve
greater predictability in model behavior, enhance traceability of
changes, and improve overall operational efficiency. This leads to
more reliable language model deployments, reduced risks associated
with prompt modifications, and the ability to quickly roll back to
previous versions if needed. Ultimately, this best practice helps
you deliver higher-quality outputs and maintain compliance with
security and governance standards.

**Desired outcome:** You have a
robust, versioned prompt template management system in place. Key
processes involve testing and comparing different prompt variants,
capturing baseline model outputs, and regularly reviewing and
optimizing prompts based on performance metrics.

**Benefits of establishing this best
practice:**
[Safely
automate where possible](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Automate prompt management,
reducing the undifferentiated heavy lifting associated with
traditional prompt management techniques.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implement versioning for your prompt templates. Test and compare
different prompt variants to identify the most effective one, and
use variables for flexibility. Capture baseline metrics of the
model output and validate whether there are deviations from the
expected results. The baseline should be your functional
performance evaluation, which uses your ground truth data. This
evaluation constitutes the set of metrics you should use for
managing your prompt templates. Versioning should include
hyperparameters or ranges where applicable, as these can influence
the output of the model, similar to the prompt contents, and are
paired with the prompt itself during evaluation.

Amazon Bedrock Prompt Management is designed to help you with the
creation and testing of prompts for foundation models. You can use
Bedrock Prompt Management to create, edit, version, and share
prompts across teams. Its components include the prompts
themselves, their variables to be filled at runtime, variants, and
a visual builder interface. This can be integrated into
applications by specifying the prompt during model inference and
supports adding a prompt node to a flow.

Amazon Bedrock Flows is a feature that allows you to create
and manage advanced workflows without writing code. Using the
visual builder interface, you can link various elements including
foundation models, prompts, agents, knowledge bases, and other AWS
services. Flows supports versioning, rollback, and A/B testing.
You can test your flows directly in the AWS Management Console or
using the
[SDK
APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/sdk-general-information-section.html).

### Implementation steps

- Set up Amazon Bedrock Prompt Management.

Create the initial prompt templates by developing a
foundational set of prompt templates tailored to your
use case
- Incorporate variables within prompts to enhance
flexibility and adaptability
- Implement a robust versioning system to track changes
and iterations of prompt templates

- Implement a baseline performance evaluation.

Compile a dataset of ground truth examples to serve as a
benchmark for model evaluation
- Identify and establish performance metrics relevant to
your application
- Conduct preliminary performance assessments to establish
a baseline

- Create and test prompt variants.

Develop several versions of each prompt to explore
different phrasings and structures
- Use Amazon Bedrock Flows to configure A/B testing
workflows for prompt variants
- Analyze the performance of each prompt variant to
determine the most effective options

- Integrate prompts into applications.

Use the Amazon Bedrock SDK to incorporate prompts during
model inference
- Integrate prompt nodes into Amazon Bedrock Flows
where appropriate to streamline application workflows

- Establish a regular review and optimization process.

Plan periodic performance evaluations to assess model
effectiveness
- Review evaluation outcomes to pinpoint areas requiring
enhancement
- Update and version prompts based on evaluation insights
to continually improve performance

- Set up cross-team collaboration.

Share prompts across teams using Amazon Bedrock Prompt
Management
- Establish and disseminate guidelines for prompt creation
and modification to maintain consistency and quality

## Resources

**Related best practices:**

- [OPS05-BP10](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_auto_integ_deploy.html)
- [OPS05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_version_control.html)

**Related documents:**

- [Amazon Bedrock Prompt Template Examples](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-templates-and-examples.html)
- [AWS re:Invent 2023 - Prompt engineering best practices for LLMs on
Amazon Bedrock (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Evaluating
prompts at scale with Prompt Management and Prompt Flows for
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/evaluating-prompts-at-scale-with-prompt-management-and-prompt-flows-for-amazon-bedrock/)

**Related tools:**

- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops03-bp01.html*

---

# GENOPS03-BP02 Enable tracing for agents and RAG workflows

Implement comprehensive tracing for generative AI agents and RAG
workflows to enhance operational excellence and performance
efficiency. This practice offers clear visibility into model
decision-making, which helps you identify inefficiencies, optimize
performance, and debug efficiently. By adopting tracing, customers
achieve more reliable and efficient workflows, which improves model
accuracy, speeds up decision-making, and enhances overall system
performance. This approach supports continuous improvement while
keeping data secure throughout the tracing process.

**Desired outcome:** After
implementing tracing, you have enhanced agent decision-making and
RAG workflows.

**Benefits of establishing this best
practice:**
[Learn
from all operational events and metrics](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Gain insights from
tracing for agents and RAG workflows.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Tracing can be a powerful tool for optimizing the decision-making
process of agents and RAG workflows. To improve your agent's
performance, tracing provides a detailed view of the agent's
step-by-step reasoning process. By examining these steps, you can
identify areas where the agent might be making suboptimal
decisions, taking unnecessary actions, or taking longer than
expected.

To optimize your RAG knowledge base, the structure and content
should be refined to provide relevant information to the agent. By
examining the inputs and outputs at each step, you can refine your
prompt templates to guide the agent towards more effective
decision-making. When the agent produces unexpected results, the
trace can help you understand why those decisions were made and
address the root cause.

Each response from an Amazon Bedrock agent is accompanied by a
trace that details the steps being orchestrated by the agent. The
trace helps you follow the agent's reasoning process that leads it
to the response it gives at that point in the conversation. If you
enable the trace, in the InvokeAgent response,
each chunk in the stream is accompanied by a trace field that maps
to a TracePart object. The
TracePart object contains information about the
agent and sessions, alongside the agent's reasoning process and
results.

To optimize the performance of multiple agents working in parallel
using trace data in Amazon Bedrock. To optimize data transfer
between agents and reduce latency in your multi-agent system using
Amazon Bedrock, consider using the supervisor with routing mode.
This mode allows the supervisor agent to route information
directly to the appropriate collaborator agent, reducing
unnecessary data transfers and overall latency.

Alternatively, considering using Amazon AgentCore, which supports agent tracing by default. AgentCore gives visibility into an agent’s behavior by capturing and visualizing both the traces and spans that capture each step of the agent workflow, including tool invocations and memory. AgentCore supports OpenTelemetry to help integrate agent telemetry data with existing observability systems, including Amazon CloudWatch, Datadog, LangSmith, and Langfuse.

### Implementation steps

- Collect and aggregate trace data.

Implement a system to collect trace data from agents
involved in your parallel processing workflow
- After running an Amazon Bedrock Agent, view the trace in
real-time as your agent performs orchestration
- When making an InvokeAgent request to
the Amazon Bedrock runtime endpoint, set the
enableTrace field to
TRUE. This will include a
trace field in the InvokeAgent
response for each chunk in the stream
- Store this data in a centralized location, such as
Amazon S3 or Amazon CloudWatch Logs, for quick access
and analysis

- Secure trace data.

Implement appropriate access controls to verify that
only authorized personnel can view trace data
- Be mindful of any sensitive information that might be
included in traces and handle it according to your
organization's security policies

- Analyze the trace components.

The trace is structured as a JSON object containing
fields such as agentId,
sessionId, and
trace
- PreProcessingTrace shows how the
agent contextualizes and categorizes user input
- OrchestrationTrace reveals how the
agent interprets input, invokes action groups, and
queries knowledge bases
- PostProcessingTrace demonstrates how
the agent handles the final output and prepares the
response
- FailureTrace indicates reasons for
step failures
- GuardrailTrace shows actions taken by
the Guardrail feature

- Analyze runtimes.

Review the timestamps in the trace data to identify
which agents or steps are taking the longest to complete
- Look for patterns or bottlenecks that might be causing
delays in the overall process

- Examine resource utilization.

Use the trace data to understand how each agent is
utilizing resources such as knowledge bases or action
groups
- Identify overutilization or underutilization of
resources that might be affecting performance

- Optimize agent configurations.

Based on the analysis, adjust the configuration of
individual agents to improve their performance
- This may include fine-tuning prompts, adjusting
knowledge base queries, or modifying action group
structures

- Implement load balancing across agents

Use the insights gained from trace data to distribute
workloads more evenly across agents
- Consider implementing a dynamic load balancing system
that can adjust based on real-time performance metrics

- Optimize data transfer between agents

Use the supervisor with routing mode, which allows the
supervisor agent to route information directly to the
appropriate collaborator agent, reducing unnecessary
data transfers and overall latency
- Use the session state feature to maintain context
between agent interactions, reducing the need to
transfer redundant information
- Where possible, design your multi-agent system to
process tasks concurrently, reducing overall runtime
- Where appropriate, cache frequently accessed data to
reduce repeated transfers between agents
- Deploy your agents in AWS Regions closest to your users
or data sources to minimize network latency

- Optimize your knowledge bases.

Verify that each agent's knowledge base is
well-structured and contains only relevant information
to minimize unnecessary data processing

- Set up performance monitoring.

Use Amazon CloudWatch to create custom metrics based on
the trace data
- Set up alarms to alert you when performance falls below
expected thresholds

- Conduct iterative testing.

After making optimizations, run comprehensive tests to
measure the change in overall system performance
- Use the trace data from these tests to identify further
areas for improvement

- Document and share insights.

Keep a record of optimizations made and their effects on
performance
- Share these insights with your team to improve future
multi-agent system designs

## Resources

**Related best practices:**

- [OPS08-BP03](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_workload_observability_analyze_workload_traces.html)

**Related documents:**

- [Amazon Bedrock AgentCore Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/)
- [Track
agent's step-by-step reasoning process using trace - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
- [Track
each step in your flow by viewing its trace in Amazon Bedrock
- Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html)
- [Create
multi-agent collaboration - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html)

**Related examples:**

- [Introducing Amazon Bedrock AgentCore: Securely deploy and operate AI agents at any scale (preview)](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Optimize
model inference for latency - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Optimize
performance for Amazon Bedrock agents using a single knowledge
base - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-optimize-performance.html)

**Related tools:**

- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [OpenTelemetry](https://opentelemetry.io/)
- [LangFuse](https://langfuse.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops03-bp02.html*

---

# GENOPS04 — Automate lifecycle management

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GENOPS04-BP01 Automate generative AI application lifecycle with infrastructure as code (IaC)

Implementing and managing IaC is crucial for consistent,
version-controlled, and automated infrastructure deployment across
environments. This practice streamlines deployment, reduces errors,
and enhances team collaboration. IaC helps customers achieve
efficiency, reliability, and scalability in infrastructure
management, which allows for rapid iteration, straightforward
rollback, and improved governance and results in secure deployments.

**Desired outcome:** After
implementing the practice of automating the lifecycle management of
generative AI workloads using IaC, customers have version control
infrastructure automated through CI/CD pipelines.

**Benefits of establishing this best
practice:**
[Safely
automate where possible](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Define your entire workload and its
operations (applications, infrastructure, configuration, and
procedures) as code, facilitating infrastructure level change
management, infrastructure version control, and advanced paradigms
such as self-healing infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Automate your application development and migration through stages
using IaC principles. When selecting your tool stack, consider
your team's skills and project requirements. Use tools such as AWS Cloud Development Kit (AWS CDK), AWS CloudFormation, or Terraform
to define and manage the infrastructure resources required for
your application. These resources may include Amazon Bedrock,
Amazon API Gateway, AWS Lambda functions, and AWS Data Pipelines, all of which help you create a reproducible and
version-controlled stack.

Store your IaC templates in a version control system like Git.
This practice facilitates collaboration among team members, allows
for tracking changes over time, and enables rolling back to
previous versions if necessary.

Implement a CI/CD pipeline using AWS CodePipeline, Jenkins, or a
similar tool. This pipeline should initiate on code changes, run
tests on your IaC templates, and automatically deploy
infrastructure changes.

Manage your IaC templates to handle multiple environments such as
development, testing and staging, and production. To maintain
consistency across environments, use the same templates with
different parameters.

For Hyperpod, use AWS CloudFormation, AWS CDK, or Terraform to
define clusters, VPCs, security groups, EKS node groups,
networking policies, and Amazon SageMaker AI resources.

For Amazon EKS, describe your Kubernetes deployments, secrets
management, and ML workflows in YAML or Helm charts, and then
manage those using CI/CD pipelines to automatically provision
and update infrastructure.

For Slurm, automate creation and scaling of compute nodes,
tracker scripts, and cluster configuration using the same IaC
tools.

HyperPod Recipes serve as the cornerstone for implementing
operational task automation by providing pre-built automation
frameworks that reduce the need for manual operational tasks
in distributed training environments. These recipes deliver
IaC templates that automatically provision, configure, and
manage complex training workflows across both EKS and Slurm
orchestrated clusters, directly addressing the core principle
of reducing manual effort and minimizing human error in
operational activities.

Establish practices and controls to help you maintain
compliance of your resources, like using AWS Config to track
resource configurations. Implement Service Catalog for
standardized resource provisioning, and regularly audit your
IaC templates for security best practices and compliance.

Be mindful of the time and cost involved in model training and
customization when automating these activities for your
workload, use historical data to determine when training and
customization might be needed for your workload.

### Implementation steps

- Select your IaC tool stack.

Evaluate AWS CDK, AWS CloudFormation, or Terraform
- Consider team skills and project needs
- Assess learning curve and maintainability

- Define your infrastructure resources.

Include each component, such as Amazon Bedrock, Amazon API Gateway, AWS Lambda, and AWS Data Pipelines
- Create reproducible, version-controlled stacks
- Use modular design for reusability

- Version control your IaC templates.

Use a code repository Git tool
- Implement branching strategy aligned with environments

- Implement a CI/CD pipeline.

Consider AWS CodePipeline or Jenkins for orchestration
- Configure initiation events for code changes
- Set up automated testing for IaC templates
- Enable automatic deployment of changes
- Implement approval gates for production deployments

- Manage multiple environments.

Use the same templates with different parameters for
development, test, and production
- Implement environment-specific security controls

- Establish governance and compliance.

Use AWS Config for tracking resource configurations and
automate remediations
- Implement Service Catalog for standardized
provisioning
- Set up automated compliance checks and reporting

- Regularly audit your IaC templates.

Focus on security best practices
- Conduct periodic third-party security assessments

## Resources

**Related best practices:**

- [OPS05-BP10](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_auto_integ_deploy.html)
- [OPS06-BP03](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_deploy_mgmt_sys.html)
- [OPS06-BP04](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_auto_testing_and_rollback.html)
- [OPS05-BP08](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_multi_env.html)
- [OPS05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_version_control.html)

**Related documents:**

- [Operationalize
generative AI applications on AWS](https://aws.amazon.com/blogs/gametech/operationalize-generative-ai-applications-on-aws-part-ii-architecture-deep-dive/)
- [AWS CloudFormation Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/creating-resources-with-cloudformation.html)
- [AWS re:Invent 2024 - Generative AI in action: From prototype to
production (AIM276)](https://www.youtube.com/watch?v=aFQFiVOh3P0)
- [SageMaker AI
HyperPod Recipes Official Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipes.html)
- [SageMaker AI
HyperPod Recipe Repository Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipe-repository.html)

**Related examples:**

- [Walkthrough:
Building a pipeline for test and production stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/continuous-delivery-codepipeline-basic-walkthrough.html)
- [AWS CDK Examples](https://github.com/aws-samples/aws-cdk-examples)
- [AWS CDK Developer Guide](https://docs.aws.amazon.com/cdk/v2/guide/home.html)
- [Terraform
AWS Provider Examples](https://github.com/terraform-providers/terraform-provider-aws/tree/main/examples)
- [Accelerate
Foundation Model Training and Fine-tuning with New Amazon SageMaker AI HyperPod Recipes](https://aws.amazon.com/blogs/aws/accelerate-foundation-model-training-and-fine-tuning-with-new-amazon-sagemaker-hyperpod-recipes/)
- [Amazon SageMaker AI model endpoint creation with CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html#aws-resource-sagemaker-model--examples)

**Related tools:**

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS CDK](https://aws.amazon.com/cdk/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [AWS Config](https://aws.amazon.com/config/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops04-bp01.html*

---

# GENOPS04-BP02 Implement GenAIOps to optimize the application lifecycle

To optimize generative AI workloads, organizations should implement
[GenAIOps](https://genaiops.ai/), a best
practice that automates the development, deployment, and management
of models. This approach establishes CI/CD pipelines for training,
tuning, and deploying foundation models. GenAIOps enhances
operational efficiency, reduces time-to-market, and enables
consistent, high-quality model performance. It creates a robust,
automated framework that supports the entire generative AI project
lifecycle from development to production deployment. Through
GenAIOps, customers can achieve greater agility, improved model
reliability, and quick adaptation to changing business requirements,
driving innovation and competitive advantage.

**Desired outcome:** After
implementing GenAIOps, organizations can have a robust, automated
framework for managing the entire lifecycle of generative AI
workloads.

**Benefits of establishing this best
practice:**
[Safely
automate where possible](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - automate the lifecycle of your
foundation models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

GenAIOps is a specialized subset of machine learning operations
(MLOps) that focuses on the processes and techniques for managing
and operationalizing foundation models in production environments.
Organizations can harness the power of foundation models while
reducing risks and optimizing their deployments. There are two
categories under GenAIOps: operationalizing foundation model
consumption and operationalizing foundation model training and
tuning. Common concerns across both categories include CI/CD,
prompt management, versioning of artifacts, model upgrades,
evaluation, and monitoring.

For operationalizing applications that consume foundation models,
the model-consuming applications will follow traditional DevOps
processes. Applications are often built using complex
orchestration patterns such as RAG and agents. Operationalizing
RAG applications involves the choice of vector database, indexing
pipelines, and retrieval strategies.

For operationalizing foundation model training and tuning, it is
essential to perform efficient training, tuning, and deployment of
foundation models using automation. Foundation model operations
(FMOps), which is the operationalization of foundation models, and
large language model operations (LLMOps), which is specifically
the operationalization of LLMs, fall under this category. This
involves model selection, continuous tuning and training of
models, experiment tracking, a central model registry, prompt
management and evaluation, and deployment of the models.

Amazon SageMaker AI Pipelines is a serverless workflow orchestration
service specifically designed for MLOps and LLMOps automation. Set
up SageMaker AI Pipelines to build, run, and monitor repeatable
end-to-end ML workflows for LLMs, from data preparation to model
deployment. The service can scale to run tens of thousands of
concurrent ML workflows in production, which is particularly
useful when working with resource-intensive LLMs. Self-managed
MLFlow or SageMaker AI MLFlow is well-suited for tracking
experiments, cataloging the models, approving them, and deploying
them to production.

Amazon Bedrock provides a managed RAG feature called Knowledge
Bases, which automates the indexing and ingestion into various
vector database options and orchestrates the retrieval process.
Amazon Bedrock Agents use the reasoning of foundation models,
APIs, and data to break down user requests, gather relevant
information, and efficiently complete tasks. Amazon Bedrock has
managed features for continued pretraining and finetuning of
foundation models.

### Implementation steps

- For SageMaker AI, implement pipelines.

Use SageMaker AI SDK to add steps which may include data
preparation, model training, model evaluation, and model
deployment
- Use SageMaker AI Processing to run evaluation scripts on the
trained model with SageMaker AI Clarify
- Automate testing with integration and performance tests.
Consider AWS Step Functions to orchestrate them
- Start the pipeline execution
- Use Amazon SageMaker AI Studio to view the pipeline's
progress
- Set up notifications for pipeline status updates using
Amazon CloudWatch Events
- Integrate this into the larger application's CI/CD
pipeline using AWS CodePipeline, AWS CodeBuild, and AWS CodeDeploy with Amazon SageMaker AI Projects

- Enable MLflow experiment tracking.

In Amazon SageMaker AI Studio, configure MLflow tracking
- Use MLflow to log parameters, metrics, and artifacts
during your model training process
- These will be automatically tracked and stored in your
SageMaker AI-managed MLflow server
- Use the MLflow UI in SageMaker AI Studio to analyze metrics
and artifacts to determine the best model iterations
- Register your best models in the MLflow Model Registry

- Use a version control system.

Use a Git compatible repository to manage code and
configurations effectively
- Set up SageMaker AI Model Registry to catalog and version
models

- Set up monitoring and logging.

Monitor real-time FM metrics with Amazon CloudWatch
- Centralize logging with Amazon CloudWatch Logs

- Create a feedback loop for continuous improvement.

Gather user feedback and model performance data
- Automate retraining and model updates based on new data

## Resources

**Related best practices:**

- [OPS05-BP10](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_auto_integ_deploy.html)
- [OPS05-BP07](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_code_quality.html)
- [OPS05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_version_control.html)

**Related documents:**

- [LLM
experimentation at scale using Amazon SageMaker AI Pipelines and
MLflow | AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/llm-experimentation-at-scale-using-amazon-sagemaker-pipelines-and-mlflow/)
- [Achieve
operational excellence with well-architected generative AI
solutions using Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/achieve-operational-excellence-with-well-architected-generative-ai-solutions-using-amazon-bedrock/)
- [MLOps
– Machine Learning Operations– Amazon Web Services](https://aws.amazon.com/sagemaker/mlops/)

**Related examples:**

- [Amazon SageMaker AI MLOps Workshop](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop)
- [AWS MLOps Framework](https://aws.amazon.com/solutions/implementations/aws-mlops-framework/)
- [Amazon SageMaker AI MLOps Project Template](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-sm.html)

**Related tools:**

- [Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker-pipelines/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [AWS CodeBuild](https://aws.amazon.com/codebuild/)
- [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch)
- [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops04-bp02.html*

---

# GENOPS05 — Model customization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GENOPS05-BP01 Learn when to customize models

Prioritize prompt engineering and RAG before model customization to
optimize resources and enhance performance in developing generative
AI solutions. This best practice aims to guide you in making
informed decisions about when and how to customize AI models, which
helps you verify that they achieve the best balance between
efficiency and effectiveness. By starting with prompt engineering
and RAG, you can leverage existing model capabilities to meet their
needs, reducing the time, cost, and complexity associated with model
customization. This approach allows organizations to quickly iterate
on solutions, minimize resource consumption, and focus on achieving
desired outcomes with minimal upfront investment.

**Desired outcome:** You have an
approach to decide when to customize models.

**Benefits of establishing this best
practice:**
[Use
managed services](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Manage the undifferentiated heavy lifting
associated with large-scale, memory-intensive, distributed computing
tasks such as model customization.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider these guidelines when deciding whether to fine-tune,
domain adapt, or pre-train a custom foundation model. Review the
considerations between model performance, resource requirements,
and maintenance costs for each approach.

Start with the least resource-intensive option (prompt
engineering), and progressively move to more advanced methods if
needed. Well-crafted prompts can often achieve the desired results
without modifying the model.

Evaluate RAG to customize the model's behavior by allowing it to
use external knowledge sources through a retrieval mechanism,
which effectively tailors its responses to specific domains or
contexts without retraining the core model itself.

Choose continued pre-training or fine-tuning when:

- You have a
specific task or use case that requires improved performance
- You have the labeled data relevant to your task
- You need the model
to understand domain-specific language (for example, medical or
legal terminology)
- You want to enhance the model's accuracy for
your application

Build a custom foundation model (typically the highest option in
resources and cost) when:

- None of the available pre-trained
models meet your specific requirements
- You have a vast amount of
proprietary data to train on
- You need complete control over the
model architecture and training process.

Amazon Bedrock's built-in tools for model evaluation to assess the
performance improvements after customization. Amazon Bedrock
offers managed RAG, agents, fine-tuning, and continued
pre-training. For greater control, use Amazon SageMaker AI, including
features to build a custom model using HyperPod with distributed
data and model parallelism training capabilities.

### Implementation steps

- Begin with prompt engineering.

Experiment with prompt structures, and test various prompt
formats to identify the most effective approach
- Use Amazon Bedrock's prompt engineering tools to
streamline the process
- Use Amazon SageMaker AI or Amazon Bedrock's evaluation tools
to assess prompt effectiveness

- Evaluate Retrieval-Augmented Generation (RAG) if needed.

Use vector databases such as Amazon OpenSearch Service for
enhanced knowledge retrieval
- Combine RAG with your selected model in Amazon Bedrock, or
consider the managed RAG feature Knowledge Bases
- Measure performance gains and response relevance

- Consider fine-tuning or continued pre-training.

Use Amazon Bedrock managed fine-tuning and pre-training
features
- Prepare labeled data specific to your task or domain
- Monitor improvements after customization

- Build a custom foundation model.

Use Amazon SageMaker AI HyperPod for FM training
- Decide between Slurm or Amazon EKS as your orchestrator
- Use SageMaker AI distributed data parallelism (SMDDP) for
data parallelism
- Use SageMaker AI model parallelism (SMP) for model
parallelism techniques

- Regularly update and retrain your model.

Track model effectiveness over time
- Update models with fresh data as it becomes available
- Use Amazon SageMaker AI Model Monitor for ongoing assessment

- Consider trade-offs in your workload.

Evaluate the cost for each approach
- Balance complexity and efficiency

## Resources

**Related best practices:**

- [OPS04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_identify_kpis.html)

**Related documents:**

- [Amazon Bedrock capabilities to enhance data processing and
retrieval](https://aws.amazon.com/blogs/aws/new-amazon-bedrock-capabilities-enhance-data-processing-and-retrieval/)
- [Customize
models in Amazon Bedrock with your own data using fine-tuning
and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
- [Amazon SageMaker AI HyperPod - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Run
distributed training workloads with Slurm on HyperPod - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-run-jobs-distributed-training-workload.html)
- [SageMaker AI
HyperPod recipe repository - Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-recipe-repository.html)

**Related examples:**

- [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/)
- [Amazon Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)

**Related tools:**

- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops05-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
