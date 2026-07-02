# MLOPS05 — Deployment

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# MLOPS05-BP01 Establish deployment environment metrics

Establish comprehensive monitoring of machine learning operations to
gain visibility into your deployed ML environments. By measuring
metrics such as memory, CPU/GPU usage, disk utilization, endpoint
invocations, and latency, you can provide optimal performance and
improve the reliability of your ML systems.

**Desired outcome:** You gain
real-time visibility into your ML deployment environments through
systematic collection and analysis of performance metrics. You
establish robust monitoring dashboards, alerting systems, and
automated responses to potential issues. This enables you to
proactively address performance bottlenecks, optimize resource
utilization, and maintain reliable ML services while managing costs
effectively.

**Common anti-patterns:**

- Implementing monitoring only after experiencing production
issues.
- Focusing only on basic system metrics while ignoring ML-specific
performance indicators.
- Creating monitoring dashboards without establishing
corresponding alerts.
- Setting static thresholds that don't account for typical usage
patterns.
- Collecting metrics without regular review or actionable response
plans.

**Benefits of establishing this best
practice:**

- Early detection of performance issues before they impact end
users.
- Improved resource optimization and cost efficiency.
- Enhanced ability to scale ML services based on actual usage
patterns.
- Faster troubleshooting and reduced mean time to resolution.
- Data-driven capacity planning and infrastructure decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establishing effective deployment environment metrics requires a
systematic approach to monitoring both infrastructure and
application-specific ML metrics. You need to focus on both
system-level metrics like CPU, memory, and disk usage, as well as
ML-specific metrics such as inference latency, throughput, and
model accuracy. By using AWS services like Amazon CloudWatch, you
can centralize your monitoring approach and gain comprehensive
visibility into your ML operations.

Start by identifying the key performance indicators that matter
most for your specific ML workloads. For inference endpoints,
these typically include latency, throughput, and resource
utilization. For batch processing jobs, focus on processing time,
error rates, and resource efficiency. With these KPIs established,
you can implement automated monitoring and alerting to quickly
identify when your systems deviate from expected performance.

Regular review of your metrics can identify trends and potential
areas for optimization. For example, you might discover that
certain models require more memory than originally allocated, or
that specific types of inference requests consistently take longer
to process. This information guides your infrastructure decisions
and prioritizes optimization efforts.

### Implementation steps

- **Record performance-related
metrics.** Use a monitoring and observability
service like Amazon CloudWatch to record performance-related
metrics. These metrics can include database transactions,
slow queries, I/O latency, HTTP request throughput, service
latency, and other key data. For SageMaker AI endpoints,
collect metrics such as CPUUtilization, MemoryUtilization,
DiskUtilization, and model-specific metrics like
ModelLatency and InvocationsPerInstance.
- **Analyze metrics when events or
incidents occur.** Use monitoring dashboards and
reports to understand and diagnose the impact of an event or
incident. Amazon CloudWatch Dashboards provide insight into
what portions of the workload are not performing as
expected. Correlate metrics, logs, and traces to quickly
identify root causes when issues arise.
- **Establish key performance indicators
(KPIs) to measure workload performance.** Identify
the KPIs that indicate whether the workload is performing as
intended. An API-based ML endpoint might use overall
response latency as an indication of overall performance,
while a batch processing job might track throughput metrics.
For generative AI applications, monitor additional metrics
like token usage, cost per request, prompt engineering
effectiveness, and use
[SageMaker AI
Training Plans](https://aws.amazon.com/sagemaker/pricing/) for cost optimization of large-scale
AI training workloads.
- **Use monitoring to generate
alarm-based notifications.** Monitor metrics for
the defined KPIs and generate alarms automatically when the
measurements are outside expected boundaries. Configure
Amazon CloudWatch Alarms to send notifications using Amazon SNS when thresholds are breached, which provides for timely
responses to potential issues.
- **Review metrics at regular
intervals.** As routine maintenance, or in response
to events or incidents, review what metrics are collected
and identify the metrics that were key in addressing issues.
Identify additional metrics that can identify, address, or
avoid issues. Schedule periodic reviews to keep your
monitoring strategy effective as your ML applications
evolve.
- **Monitor and alarm
proactively.** Use KPIs, combined with monitoring
and alerting systems, to proactively address
performance-related issues. Configure CloudWatch to initiate
automated actions to remediate issues where possible.
Escalate the alarm to those able to respond if an automated
response is not possible. Use anomaly detection to predict
expected KPI values, and generate alerts and automatically
halt or roll back deployments if KPIs are outside of the
expected values.
- **Use Amazon CloudWatch for
comprehensive monitoring.** Use Amazon CloudWatch
metrics for SageMaker AI endpoints to determine the memory,
CPU usage, and disk utilization. Set up CloudWatch
Dashboards to visualize the environment metrics and
establish CloudWatch alarms to initiate a notification
through Amazon SNS (email, SMS, or webHook) to notify on
events occurring in the runtime environment. For model
performance monitoring, implement Amazon SageMaker AI Model
Monitor to detect data drift and quality issues.
- **Use Amazon EventBridge for automated
workflows.** Define an automated workflow using
Amazon EventBridge to respond automatically to events. These
events can include training job status changes, endpoint
status changes, and increasing the compute environment
capacity after it crosses a defined threshold (such as CPU
or disk utilization). Create event rules that run Lambda
functions to scale resources, update configurations, or
notify specific teams based on the event type.
- **Use AWS Application Cost Profiler
for cost allocation.** Implement AWS Application Cost Profiler to report the cost per tenant (model or user).
This assists you in tracking resource usage at a granular
level and enables accurate cost attribution across different
ML models, teams, or business units. Use
[SageMaker AI
Training Plans](https://aws.amazon.com/sagemaker/pricing/) for compute reservation and better
resource planning of high-demand GPU resources. Use these
insights to optimize resource allocation and identify
opportunities for cost savings.
- **Implement SageMaker AI Model Monitor
for data drift detection.** Configure SageMaker AI
Model Monitor to continuously monitor the quality of your
machine learning models in production. Set up automated
quality checks to detect data drift, model drift, and bias
drift in your production workloads. This enables you to
maintain high quality standards and take corrective actions
when models start to deviate from expected behavior.
- **Use AWS X-Ray for distributed
tracing.** Implement AWS X-Ray to trace requests
through your ML application components. This provides
visibility into request flows, latency bottlenecks, and
error points in distributed systems. X-Ray provides an
understanding of the dependencies between components so you
can optimize end-to-end performance of your ML applications.
- **Implement Amazon SageMaker AI Clarify
for bias monitoring.** Use SageMaker AI Clarify to
detect bias in your deployed models. Set up regular
monitoring jobs to track bias metrics and alert when they
exceed acceptable thresholds so that your ML systems
continue to make fair and unbiased predictions in
production.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Metrics
in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [Using
Amzon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
- [DevOps
and AWS](https://aws.amazon.com/devops/?ref=wellarchitected-wp)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops05-bp01.html*

---
