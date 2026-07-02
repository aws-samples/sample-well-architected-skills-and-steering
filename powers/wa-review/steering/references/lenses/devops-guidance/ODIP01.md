**Saga**: Observability
**Capability**: O.DIP — Data ingestion and processing

---

# [O.DIP.1] Aggregate logs and events across workloads

**Category:** FOUNDATIONAL

Logs and events should be aggregated across multiple workloads
to provide a comprehensive view of the entire system. This
enables teams to troubleshoot, identify patterns, and resolve
operational issues.

Implement a log aggregation solution that supports collecting logs from various
sources and provides functions for filtering, searching, visualizing, and alerting. Make
sure the solution provides real-time data collection, supports necessary data sources, and
offers visualization options. The tool should be accessible to application teams, allowing
them to monitor and troubleshoot their system as needed.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL11-BP01 Monitor
all components of the workload to detect failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_monitoring_health.html)
- [Cross-account
cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html)
- [Collect,
analyze, and display Amazon CloudWatch Logs in a single
dashboard with the Centralized Logging on AWS solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-on-aws/welcome.html)
- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)
- [Sending
Logs Directly to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Sending-Logs-Directly-To-S3.html)
- [One
Observability Workshop](https://observability.workshop.aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.1-aggregate-logs-and-events-across-workloads.html*
