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
