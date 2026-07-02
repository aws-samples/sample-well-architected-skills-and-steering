**Saga**: Observability
**Capability**: O.SI — Strategic instrumentation

---

# [O.SI.3] Instrument all systems for comprehensive telemetry data collection

**Category:** FOUNDATIONAL

All systems should be fully-instrumented to collect the metrics, logs, events, and
traces necessary for meeting key performance indicators (KPIs), service level objectives,
and logging and monitoring strategies. Teams should integrate instrumentation libraries into
the components of new systems and feature enhancements to capture relevant data points,
while also ensuring that pipelines and associated tools used during build, testing,
deployment, and release of the system are also instrumented to track development lifecycle
metrics and best practices.

Chosen libraries and tools should support the efficient
collection, normalization, and aggregation of telemetry data.
Depending on the workload and existing instrumentation, this
could involve structured log-based metric reporting, or it
might rely on other established methods like using StatsD,
Prometheus exporters, or other monitoring solutions. The
chosen method should align with the workload's specific needs
and the complexity involved in instrumenting the solution.
Strike a balance between thorough monitoring and the amount of
work required to implement and maintain the monitoring
solution, to avoid falling into an anti-pattern of excessive
instrumentation.

Teams might also consider the use of auto-instrumentation tools to simplify the
process of collecting data across their systems with little to no manual intervention,
reducing the risk of human error and inconsistencies. Examples of auto-instrumentation
include embedding instrumentation tools in shared computer images like AMIs or containers
being used, automatically gathering telemetry from the compute runtime, or embedding
instrumentation tools into shared libraries and frameworks.

Regardless of how the team chooses to implement it, instrumentation should be
designed to accommodate the needs of the specific workload and business requirements. This
includes considering factors such as cost, security, data retention, access, compliance, and
governance requirements. All collected data must always be protected using appropriate
security measures, including encryption and least-privilege access controls.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF02-BP03 Collect
compute-related metrics](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_select_compute_collect_metrics.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP01 Monitor
all components for the workload (Generation)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_monitor_resources.html)
- [AWS Well-Architected Cost Optimization Pillar: COST05-BP02
Analyze all components of the workload](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_analyze_all.html)
- [Instrumenting
distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/?did=ba_card&trk=ba_card)
- [AWS Observability Best Practices: Data Types](https://aws-observability.github.io/observability-best-practices)
- [Embedding
metrics within logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html)
- [Application
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html)
- [Container
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)
- [Lambda
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html)
- [Powertools
for AWS Lambda](https://github.com/aws-powertools/powertools-lambda-python)
- [AWS Distro
for OpenTelemetry](https://aws-otel.github.io)
- [Build
an observability solution using managed AWS services and
the OpenTelemetry standard](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/)
- [The
Amazon Software Development Process: Monitor
Everything](https://youtu.be/52SC80SFPOw?t=1548)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.3-instrument-all-systems-for-comprehensive-telemetry-data-collection.html*
