# HNSEC03 — Detection

**Pillar**: Security  
**Best Practices**: 2

---

# HNSEC03-BP01 Implement network traffic monitoring and threat detection

Monitor and implement an immediate response process that detects and
reacts to any suspicious or malicious activity. Continuously
monitoring workloads helps to identify security incidents faster. At
a minimum, the metadata of logs should be captured for hybrid
network connections with private connections.

**Desired outcome:** Detect
suspicious or unauthorized activity and improve security posture by
capturing and analyzing network traffic logs.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables early detection and response to security incidents
- Provides visibility into hybrid network activity
- Helps with forensic analysis and compliance reporting
- Reduces risk of undetected malicious activity

## Implementation guidance

- Enable flow logs on all relevant networks using services such
as VPC Flow Logs and Transit Gateway Flow Logs
- Enable continuous threat detection across network traffic and
accounts. For example, you can achieve this with Amazon GuardDuty.
- Review findings regularly and establish automated or manual
incident response processes.
- Store and analyze logs in a central location for correlation
and investigation.

## Resources

- [Logging
IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec03-bp01.html*

---

# HNSEC03-BP02 Set up central logging and analytics

Establishing a centralized logging and analytics system is crucial
for comprehensive visibility, security monitoring, and operational
efficiency across both on-premises and cloud infrastructures. A
central logging solution enables organizations to collect, store,
analyze, and respond to events occurring throughout their
distributed network environments.

**Desired outcome:** Achieve
comprehensive visibility and efficient analysis across all
networking environments for rapid detection and troubleshooting.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Centralizes monitoring and log management
- Streamlines threat detection and operational insights
- Supports compliance and audit requirements
- Simplifies troubleshooting across hybrid environments

## Implementation guidance

- Aggregate logs from on-premises and cloud environments to a
centralized analytics platform.
- Implement dashboards and alerting for key performance and
security events.

## Resources

- [Centralized
Logging with
OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)
- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [Central
Logging and Analytics in Hybrid Environments](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/central-logging-and-analytics-in-hybrid-environments.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec03-bp02.html*

---
