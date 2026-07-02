**Saga**: Observability
**Capability**: O.CM — Continuous monitoring

---

# [O.CM.5] Detect performance issues using application performance monitoring

**Category:** RECOMMENDED

Application Performance Monitoring (APM) refers to the use of
tools to monitor and manage the ongoing, real-time performance
and availability of systems in production environments. APM
tools help in maintaining the performance of systems by
identifying performance issues early on. This leads to quicker
resolution of issues, improved user experience, and reduced
downtime.

To comprehensively monitor application performance, implement
both Real-User Monitoring (RUM) and Synthetic Monitoring.
These APM tools are recommended detect and diagnose
performance issues in production systems. These APM tools
enable teams to proactively detect and diagnose complex
application performance problems to maintain an expected level
of service.

RUM captures performance metrics based on actual user interactions. Analyze real user
data to understand areas of the system that are frequently used and might benefit from
performance improvements. This data can then be used to identify and debug client-side
issues to optimize end-user experience.

On the other hand, Synthetic Monitoring involves writing
scripts that simulate user interactions, known as canaries, to
continuously monitor endpoints and APIs. Canaries follow the
same routes and perform the same actions as a customer,
allowing for the continuous verification of the customer
experience even in the absence of actual customer traffic. By
using insights from RUM, you can optimize which canaries to
run continuously, ensuring they closely mimic the most common
user paths. This strategy ensures potential issues are
identified before impacting users, offering a seamless user
experience.

Both tools collect metrics on response time, resource
utilization, and other performance-related indicators, forming
a holistic approach to continuous performance monitoring in
production environments.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF01-BP06 Benchmark
existing workloads](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_performing_architecture_benchmark.html)
- [What
is APM (Application Performance Monitoring)?](https://aws.amazon.com/what-is/application-performance-monitoring/)
- [Real-User
Monitoring (RUM) for Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
- [Amazon CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html)
- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.5-detect-performance-issues-using-application-performance-monitoring.html*
