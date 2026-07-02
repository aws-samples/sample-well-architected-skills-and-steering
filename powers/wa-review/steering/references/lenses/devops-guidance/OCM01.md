**Saga**: Observability
**Capability**: O.CM — Continuous monitoring

---

# [O.CM.1] Automate alerts for security and performance issues

**Category:** FOUNDATIONAL

Alerts should automatically notify teams when there are indicators of malicious
activity, compromise, or performance degradation. Effective alerting accelerates incident
response times, enabling teams to quickly address and resolve issues before they can
significantly impact system performance or security. Without automatic alerting, teams can
suffer from delayed response times that can lead to prolonged system downtime or increased
exposure to security threats.

Implement centralized alerting mechanisms to track anomalous behavior across all
systems. Define specific conditions and thresholds that, when breached, will raise alerts.
Verify that the alerts are delivered to the appropriate teams by email, text message, or the
team's preferred notification system. Integrating these alerts into your centralized
incident management systems can also help in the automatic creation of tickets, aiding
faster resolution.

In a more advanced workflow, alerts can be integrated with automated governance
systems to start remediation actions immediately upon detection or to gather additional
insights that will aid investigations.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF07-BP06 Monitor
and alarm proactively](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_monitor_instances_post_launch_proactive.html)
- [AWS Well-Architected Reliability Pillar: REL06-BP03 Send
notifications (Real-time processing and alarming)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_monitor_aws_resources_notification_monitor.html)
- [What
is Anomaly Detection?](https://aws.amazon.com/what-is/anomaly-detection/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [AWS Health Aware](https://github.com/aws-samples/aws-health-aware/)
- [Amazon's
approach to high-availability deployment: Anomaly
detection](https://youtu.be/bCgD2bX1LI4?t=2493)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.cm.1-automate-alerts-for-security-and-performance-issues.html*
