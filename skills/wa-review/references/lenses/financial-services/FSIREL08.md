**Pillar**: Reliability

# FSIREL08: How do you monitor your resources to understand your workloads health?

High availability for applications requires the ability to detect failures and
recover quickly. Workloads must be configured to emit the relevant telemetry to detect
failures, so that operational processes can capture and react to these events.

## FSIREL08-BP01 Use a single pane of glass for monitoring

Amazon CloudWatch provides robust monitoring, allowing you to organize the data to
escalate detected issues as quickly as possible. Without adequate processes in place,
you may miss leading indicators of problems. A single pane of glass and standardizing
cloud monitoring standards across your organization can help avoid information silos
and simplify the analysis of monitoring data. Combining monitoring of AWS system
metrics and workload logs enables analysts to cross-reference signals and log
information across dependent systems. Frequently, issues surface in invoking systems,
and IT professionals spend time parsing logs on the invoking systems instead of on the
dependent systems where the error originated. Consider embedding metrics in logs with
[Embedded Metric
Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html), which allows you to quickly dive from the single pane of glass
to the most granular entity of your workload. More information on building efficient
dashboards for operational visibility can be found in the [The Amazon
Builders' Library](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/).

## FSIREL08-BP02 Alert on the absence of an event

The absence of monitoring data can indicate an underlying issue. Implement
controls that alert on missed reporting intervals. Treat missing data as a security
breach, and raise alarms appropriately.

## FSIREL08-BP03 Identify metrics and validate alerts through load testing

Workloads must be load-tested regularly to validate scaling and resilience.
Identify key metrics (for both components that auto scale with demand and for static
resources such as relational databases) that correlate with capacity constraints and
customer outages during these load tests.

As part of your load-testing, validate these metrics and associated alerts,
ensuring that alerts are issued as expected. Perform load tests in lower environments
to identify indicators for alerting and automated remediation. Validation of your
indicators and alerts through load testing minimize your Mean Time to Detection
(MTTD), giving your recovery mechanisms more time to respond and increasing the
workload's availability.

## FSIREL08-BP04 Use distributed tracing tools for service-oriented architectures

As systems become more distributed with the implementation of microservices
architectures, the challenge of identifying performance bottlenecks increase. Use
workload performance monitoring tools such as AWS X-Ray to trace and provide
telemetry across multiple systems and on a transaction-by-transaction basis. Adopt
tools like AWS X-Ray and [Open Telemetry](https://aws.amazon.com/otel/)
as integrated tools that provide tracing and data as transactions span across multiple
services.

## FSIREL08-BP05 Monitor AI model performance and drift

Continuous monitoring should track key performance
indicators against established baselines, with automated
alerts for significant deviations and configurable
thresholds with escalation procedures. Establish regular
cadences for model evaluation using production data,
comparing predictions against actual outcomes. Implement
comprehensive logging systems that capture input data
characteristics, prediction outputs, and environmental
factors to facilitate root cause analysis when performance
issues arise. For regulated applications, consider deploying
parallel inference systems where both current and candidate
models run simultaneously to compare outputs before
deployment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel08.html*
