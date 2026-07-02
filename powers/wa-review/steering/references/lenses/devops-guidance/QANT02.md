**Saga**: Quality assurance
**Capability**: QA.NT — Non-functional testing

---

# [QA.NT.2] Validate system reliability with performance testing

**Category:** RECOMMENDED

Performance testing evaluates the responsiveness, throughput, reliability, and
scalability of a system under a specific load. It helps ensure that the application
performs adequately when it is subjected to both expected and peak loads without impacting
user experience. Different performance tests should be run based on the nature of changes
made to the system:

- **Load testing:** Performance tests evaluating the
system's behavior under expected load, such as the typical number of concurrent users
or transactions. Integrate automated load testing into your deployment pipeline,
ensuring every change undergoes validation of system behavior under expected
scenarios.
- **Stress testing:** Performance tests challenging the
system by increasing the load beyond its normal operational capacity. Stress tests
identify the system's breaking points, ensuring that even under extreme conditions,
the system maintains functionality without abrupt crashes. Schedule stress tests after
significant application changes, infrastructure modifications, or periodically—such as
once a month—to prepare for unpredictable spikes in traffic or potential DDoS attacks.
- **Endurance testing:** Performance tests that monitor
system behavior over extended periods of time under a specific load. Endurance tests
help ensure that there are no latent issues, such as slow memory leaks or performance
degradation, which might occur after prolonged operations. Monitor key performance
indicators over time and compare against established benchmarks to identify latent
issues. Schedule endurance tests after significant changes to the system, especially
those that might introduce memory leaks or other long-term issues. Consider running
them periodically—such as quarterly or biannually—to ensure system health over
prolonged operations.

All performance tests should be run against a test
environment mirroring the production setup. Use tailored
performance testing tools for your application's architecture
and deployment environment. Regularly analyze test results
against historical benchmarks and take proactive measures to
counteract performance regressions.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF01-BP07 Load test
your workload](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_performing_architecture_load_test.html)
- [AWS Well-Architected Sustainability Pillar: SUS03-BP03
Optimize areas of code that consume the most time or resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)
- [AWS Well-Architected Reliability Pillar: REL07-BP04 Load test
your workload](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_load_tested_adapt.html)
- [AWS Well-Architected Reliability Pillar: REL12-BP04 Test
scaling and performance requirements](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_test_non_functional.html)
- [Ensure
Optimal Application Performance with Distributed Load
Testing on AWS](https://aws.amazon.com/blogs/architecture/ensure-optimal-application-performance-with-distributed-load-testing-on-aws/)
- [Stress
Testing Tools - AWS Fault Injection Service](https://aws.amazon.com/fis/)
- [Find
Expensive Code – Amazon CodeGuru Profiler](https://aws.amazon.com/codeguru/features/)
- [Load
test your applications in a CI/CD pipeline using CDK
pipelines and AWS Distributed Load Testing Solution](https://aws.amazon.com/blogs/devops/load-test-applications-in-cicd-pipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.2-validate-system-reliability-with-performance-testing.html*
