# SCPERF05 — Test and monitor performance

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# SCPERF05-BP01 Implement comprehensive monitoring and dashboards for supply chain performance

Building an effective dashboard involves focusing on the key
performance indicators (KPIs) that matter most to your
organization and displaying them in an understandable and visually
appealing way.

**Desired outcome:** Measuring of the
application behavior can help manage it better, just not only the
performance of the application also during vulnerable situations
and to take actions spontaneously.

**Benefits of establishing this best
practice:** Good observability and dashboard to monitor
performance efficiency and continuous improvements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use tools and best practices to gain insights including End-to-end
visibility, alerts and alarms, Anomaly detection, regular review
of metrics and logs, security monitoring, and cost optimization.
Remember, while AWS provides observability tools (Amazon CloudWatch, AWS CloudTrail) to monitor and gain insights, it's the
combination of these tools with best practices that will give you
the most valuable insights about the end-to-end supply chain
systems.

### Implementation steps

- Identify key performance indicators (KPIs) that are most
critical to supply chain operations and business objectives.
- Design and implement comprehensive dashboards using Quick or CloudWatch dashboards to visualize supply
chain performance.
- Configure automated alerts and alarms based on performance
thresholds and anomaly detection to enable proactive
response.
- Implement end-to-end tracing and monitoring across all
supply chain components, from edge devices to cloud
applications.
- Establish regular review processes for performance metrics
and logs to identify trends and optimization opportunities.
- Create role-based dashboard views that provide relevant
insights to different stakeholders across the supply chain
organization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp01.html*

---

# SCPERF05-BP02 Evaluate compliance with performance requirements

When many systems, including third-party systems, are involved in
a workload, it is important to know the behavior of each system
and to monitor who is contributing to performance loss so proper
adjustments can be made.

**Desired outcome**: Optimum
performance that conforms to the system requirements to handle
loads.

**Benefits of establishing this best
practice:** Enhanced visibility into system performance
across complex supply chain networks, improved ability to identify
and resolve performance bottlenecks, better accountability for
third-party system performance, and reduced mean time to
resolution for performance issues.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Monitoring of your workload at multiple levels helps verify that
your resources are performing as expected and you are aware of
deviations. Consider all dimensions of the solution for
monitoring, for example client-side and server-side metrics,
application metrics and infrastructure metrics, technical and
functional metrics.

Provide visibility of data loss in your metrics, for example, by
monitoring for lost messages.

Where possible capture inter-solution and inter-process
communication streams to aid with the reproduction of issues.

### Implementation steps

- Establish performance baselines and SLAs for all supply
chain systems, including third-party integrations.
- Implement comprehensive monitoring across all system
layers, including infrastructure, application, and
business metrics.
- Deploy distributed tracing to track performance across
complex supply chain workflows and identify bottlenecks.
- Create automated performance testing and validation
processes to make sure systems meet established
requirements.
- Implement alerting mechanisms that notify teams when
performance deviates from established baselines or SLA
thresholds.
- Conduct regular performance reviews and optimization
initiatives based on monitoring data and compliance
assessments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp02.html*

---

# SCPERF05-BP03 Integrate performance testing into the release cycle of the supply chain application

Load testing results help you measure how the system behaves while
in high-traffic or heavy loads. Note these measurements to help
you adjust the underlying resources without wasting cost by
over-provisioning.

**Desired outcome:** Properly sized
supply chain applications.

**Benefits of establishing this best
practice:** Cost optimization, resilience, durability,
and improved user experience.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Verify consistency and failure recovery during load tests.
Verify data consistency and recovery during periods of high
load. Making sure that your workload's RTO and RPO is still
valid under the highest load can uncover gaps in your
architecture and operational resilience.

Understand performance of the system under peak load and in
failure scenarios: Include testing of common failure scenarios
in your performance testing suites to understand your workload
behavior in these situations and determine areas for
improvement.

### Implementation steps

- Develop comprehensive performance testing strategies that
simulate realistic supply chain load patterns and peak
usage scenarios.
- Integrate automated performance testing into CI/CD
pipelines to validate performance with every major
release.
- Implement chaos engineering practices to test system
resilience and recovery capabilities under various failure
conditions.
- Create performance test scenarios that include third-party
system integrations and supplier network dependencies.
- Establish performance regression testing to make sure new
releases don't degrade existing system performance.
- Document and analyze performance test results to
continuously improve system architecture and resource
allocation strategies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp03.html*

---
