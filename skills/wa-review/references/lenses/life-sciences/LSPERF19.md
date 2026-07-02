# LSPERF19 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF19-BP01 Implement infrastructure as code for consistent test environments

Use infrastructure as code (IaC) to deploy consistent, repeatable
test environments that accurately mirror production. By codifying
your infrastructure, you reduce configuration drift between test and
production environments, This approach enables teams to rapidly
provision test environments on demand, run comprehensive load tests
against scientific workflows, and tear down resources when testing
concludes.

**Desired outcome:** Implement
infrastructure as code (IaC) to deploy consistent, repeatable test
environments that mirror production, reducing configuration drift
and enabling on-demand provisioning for comprehensive scientific
workflow load testing with efficient resource management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing IaC provides a foundation for creating consistent,
repeatable test environments that precisely mirror production
configurations for generative AI systems. By codifying
infrastructure specifications, organizations can reduce
configuration drift between testing and production environments
and verify that performance evaluations and validation tests
accurately reflect real-world conditions. This approach enables
development and scientific teams to rapidly provision complete
test environments on demand through automated processes,
significantly reducing setup time and reducing manual
configuration errors.

Teams can execute comprehensive load tests against scientific
workflows in these environments, gathering performance metrics
that reliably predict production behavior while maintaining strict
validation controls. The ephemeral nature of IaC-provisioned
environments allows organizations to tear down resources
immediately after testing concludes, optimizing cost efficiency
without sacrificing testing rigor.

Implement version control for infrastructure code to maintain
historical records of environment configurations, supporting audit
requirements and enabling rollback capabilities when needed.

### Implementation steps

- Use AWS CloudFormation to codify your generative AI
infrastructure stack.
- Implement AWS Config to detect and avoid configuration
drift.
- Deploy Service Catalog to standardize environment
provisioning.
- Integrate Distributed Load Testing on AWS for scientific
workflow validation.
- Configure Amazon EventBridge to automate resource cleanup
after testing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf19-bp01.html*

---

# LSPERF19-BP02 Establish comprehensive performance metrics and evidence collection

Establish measurable performance metrics specific to scientific
workflows before load testing. Capture traditional indicators
alongside domain-specific measurements for research and clinical
data processing. Implement automated evidence collection to create
audit trails, inform optimization decisions, and verify system
reliability. Centralize test results to enable trend analysis and
detect regressions across cycles.

**Desired outcome:** Implement a
comprehensive scientific workflow performance measurement framework
that establishes metrics before testing, captures domain-specific
indicators, automates evidence collection, and centralizes results
for trend analysis and regression detection.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Effective performance testing for generative AI systems requires
establishing comprehensive, measurable metrics specifically
tailored to scientific workflows before initiating load testing
activities. Organizations should develop a balanced measurement
framework that captures traditional technical indicators (such as
latency, throughput, and resource utilization) alongside
domain-specific scientific measurements that reflect research
quality and clinical data processing integrity.

Implement automated evidence collection mechanisms that
systematically document test results, creating detailed audit
trails that satisfy regulatory requirements while simultaneously
providing valuable data for optimization decisions. These
automated systems should capture performance data at regular
intervals during testing, correlating system behaviors with
specific workloads to identify optimization opportunities and
potential bottlenecks.

Centralize test results in a structured repository that enables
sophisticated trend analysis across multiple test cycles,
facilitating the early detection of performance regressions that
might impact scientific outcomes.

Configure dashboards to visualize both point-in-time performance
and longitudinal trends, making complex performance data
accessible to both technical and scientific stakeholders.

### Implementation steps

- Define metrics in Amazon CloudWatch using custom dimensions
for scientific workflows.
- Deploy AWS X-Ray traces to capture both technical and
domain-specific indicators.
- Implement AWS Audit Manager for automated evidence
collection.
- Use Amazon S3 and Amazon Athena to centralize and query
performance test results.
- Create Quick dashboards for trend analysis
across test cycles.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf19-bp02.html*

---

# LSPERF19-BP03 Schedule regular performance tests with production-representative data loads

Institute a cadence of regular performance tests using simulated
research and clinical data that accurately represents production
workloads in terms of volume, variety, and velocity. These scheduled
tests should be integrated into your development pipeline to
identify performance bottlenecks early, before they impact
production operations. Vary test scenarios to account for both
typical daily operations and peak usage patterns, such as
end-of-month processing or seasonal research activities. Complement
scheduled tests with on-demand testing triggered by significant
system changes. This proactive approach to performance validation
verifies that scientific and clinical users consistently experience
responsive systems that meet their demanding computational
requirements.

**Desired outcome:** By implementing
a comprehensive performance testing framework, scientific and
clinical users experience consistently responsive systems that meet
their computational requirements, with zero production incidents
caused by performance bottlenecks.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing effective performance testing for generative AI
systems requires establishing a consistent cadence of regular
evaluations using carefully constructed datasets that accurately
represent production workloads. Organizations should develop
simulated research and clinical data that mirrors actual usage
patterns in terms of volume, variety, and velocity
characteristics, verifying that test results provide meaningful
insights about real-world performance. Integrate these scheduled
performance tests directly into development pipelines as automated
gates, enabling early identification of potential bottlenecks
before they can impact production operations or scientific
outcomes.

Design a comprehensive testing strategy that incorporates diverse
scenarios reflecting both typical daily operations and anticipated
peak usage patterns, such as end-of-month processing surges or
seasonal research activities that might stress system resources.
Complement the regular testing schedule with targeted, on-demand
evaluations triggered by significant system changes, including
infrastructure updates, algorithm modifications, or data pipeline
adjustments.

This proactive, multi-faceted approach to performance validation
creates a robust quality framework so that scientific and clinical
users consistently experience responsive systems capable of
meeting their demanding computational requirements.

### Implementation steps

- Deploy AWS DevOps tools like AWS CodePipeline with Amazon CloudWatch Synthetics for automated testing cycles.
- Use Amazon SageMaker AI Experiments to track model performance
across different test scenarios.
- Implement AWS Step Functions to orchestrate complex testing
workflows with varying loads.
- Configure Amazon EventBridge to trigger on-demand tests when
detecting significant system changes.
- Use Quick dashboards to visualize performance
trends across testing cycles.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf19-bp03.html*

---
