**Pillar**: Performance Efficiency

# FSIPERF06: How do you evaluate compliance with performance requirements?

Here are several methods for doing so:

- Monitoring of your workload at multiple levels helps verify
that your resources are performing as expected and you are
aware of deviations.
- Consider all dimensions of the solution for monitoring, for
example client-side and server-side metrics, application
metrics and infrastructure metrics, technical and functional
metrics.
- Monitor for failure rates and alert when they are above
expected values.
- Identify KPIs and create threshold alerts for them and
determine what actions to take (like autoscaling) when
thresholds are breached - this allows you to observe the
overall health of your system and identify
[non-binary,
or grey, failure states](https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/gray-failures.html).
- Provide visibility of data loss in your metrics, for example
by monitoring for lost messages.
- Where possible capture inter-solution and inter-process
communication streams to aid with the reproduction of
issues.

## FSIPERF06-BP01 Use Application Performance Monitoring (APM) tools

Use APM tools to provide your organization the capability to verify that application
performance meets its defined requirements. AWS offers features and services to monitor
and subsequently right-size the cloud services that you need to meet performance
requirements.

For example, you can monitor and set alarms on latency and error rates for each user
request using Amazon CloudWatch metrics and alarms, or on your downstream dependencies, or on the
success and failure of key operations. Amazon CloudWatch Synthetics can be used to create
*canaries*, configurable scripts that run on a schedule, or to
monitor your endpoints, and APIs.

The required level of monitoring generates huge amounts of data, which can be
challenging for operation teams to store, analyze, and visualize, so make use of services
including Amazon Managed Service for Prometheus to monitor and alert on containers, Amazon Managed Grafana to visualize metrics and
logs, and the wide range of features found in Amazon CloudWatch, to provide the appropriate tools
for monitoring your systems without the overhead of managing additional infrastructure.
Teams need training to update their skills and processes and take full advantage of this
new fidelity of insight.

## FSIPERF06-BP02 Integrate performance testing into the release cycle

Rather than considering performance testing to be a separate part of the workload
release cycle, integrate performance testing into your release process and CI/CD tooling.
This allows you to record and evaluate performance metrics across releases, being aware of
and taking action when metrics change as early as possible.

## FSIPERF06-BP03 Verify consistency and failure recovery during load tests

You must verify data consistency and recovery during periods of high load. Ensuring
that your workload's RTO and RPO is still valid under the highest load can uncover gaps in
your architecture and operational resilience.

## FSIPERF06-BP04 Understand performance of the system under peak load and in failure scenarios

Include testing of common failure scenarios in your performance testing suites to
understand your workload behaviour in these situations and determine areas for
improvement.

Extend the range of performance testing scenarios to cover testing at loads beyond
current peak loads, and testing the scaling processes themselves of the application to
understand how the environment behaves under increasing load.

Under common or anticipated failure scenarios, workloads should exhibit predictable
failure patterns with performance degrading gracefully using techniques such as [fail-open behavior,](https://www.wellarchitectedlabs.com/reliability/300_labs/300_health_checks_and_dependencies/4_fail_open/) and the transformation of [hard dependencies into soft dependencies.](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html)

## FSIPERF06-BP05 Include dependencies in your load tests

Financial institutions need to map resources they need to continuously deliver their
important business services. These resources are your people, processes, technology,
facilities, and information, including third-party service providers. This mapping allows
the identification of operational dependencies, vulnerabilities, and threats.
Incorporating the dependencies of your workload (such as on financial messaging providers)
as part of your performance tests enables you to demonstrate the overall resiliency of
your workload.

## FSIPERF06-BP06 Collect and analyze generative AI performance metrics

For financial services workloads using generative AI,
implement comprehensive monitoring of model performance,
including response latency, accuracy metrics, and token usage.
Set up monitoring specifically for regulatory adherence
concerns, such as bias detection and unexpected outputs that
might impact financial decisions or customer interactions.

**Implementation steps:**

- Configure CloudWatch metrics for AI services like Amazon
Bedrock or Amazon SageMaker AI endpoints.
- Implement trace frameworks like OpenLLMetry to capture model
performance metrics.
- Establish alert thresholds specific to AI components in
financial workloads.
- Create dashboards that visualize AI model performance
alongside other application metrics.
- Set up automated remediation actions for common performance
issues.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf06.html*
