# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 3

---

# MIDAOPS01 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# MIDAOPS01-BP01 Implement a process to periodically review compliance requirements relevant to your industrial data infrastructure

Implement a process to periodically review compliance requirements relevant to your
industrial data infrastructure. Regular assessment of compliance requirements is crucial for
manufacturing environments where industrial data is subject to various regulations such as
GDPR, HIPAA, ISO 27001, or industry-specific standards. Establish a systematic review process
to verify ongoing compliance and adapt to changing requirements.

**Desired outcome:** Maintain a clear understanding of
applicable compliance requirements and verify that your industrial data infrastructure remains
compliant through regular assessments and updates. Identify gaps in compliance and implement
necessary changes promptly.

**Benefits of establishing this best practice:** Adopting the
best practice and prescriptive guidance helps you align with industry standards while reducing
the risk of non-compliance penalties and regulatory issue. This enables proactive rather than
reactive compliance management and simplifies auditing processes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Create a comprehensive compliance review framework for regular assessments,
documentation, and updates to your industrial data infrastructure.

### Implementation steps

- **AWS Config Rule implementation:** Create custom
compliance rules in AWS Config to automatically evaluate your resources against
industry standards. AWS Config maintains a detailed inventory of your AWS resource
configurations and continuously checks for compliance violations.
- **Security Hub CSPM integration:** Enable AWS Security Hub CSPM
with industry-specific security standards (CIS, PCI DSS, HIPAA). Security Hub CSPM
automatically assesses your security status and aggregates alerts across integrated
services.
- **Audit management:** Use AWS Audit Manager to automate
evidence collection and continuously audit your AWS usage. Create assessment templates
mapped to your compliance frameworks and schedule regular assessments.
- **Automated monitoring:** Configure Amazon EventBridge
rules to run Lambda functions for compliance checks. Set up notifications through
Amazon SNS when compliance issues are detected.

## Key AWS services

- [AWS Config](https://aws.amazon.com/config/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/)
- [Amazon Lambda](https://aws.amazon.com/pm/lambda/)

## Resources

**Related documents:**

- [Security Best Practices for Manufacturing OT](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/security-best-practices-for-manufacturing-ot.html)
- [Best practices to respond to security risks across AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-to-respond-to-security-risks-across-your-aws-organizations/?utm_source=chatgpt.com)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaops01-bp01.html*

---

# MIDAOPS02 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# MIDAOPS02-BP01 Use enhanced monitoring and alerting in the cloud and at the edge

Comprehensive observability is crucial for manufacturing teams to proactively monitor the
health and performance of the data infrastructure.

**Desired outcome:** Achieve real-time visibility into the
entire industrial data infrastructure, enabling proactive issue detection, rapid
troubleshooting, and maintenance of optimal system performance across both cloud and edge
environments.

**Benefits of establishing this best practice:** By
implementing this robust observability framework, a manufacturing organization can gain
visibility and insight needed to proactively manage the reliability, performance, and security
of their data-driven operations. The observability tools and practices enable the team to
quickly detect, investigate, and resolve issues before they impact production.

- Enables proactive identification of potential issues before they impact operations
- Reduces mean time to detection (MTTD) and resolution (MTTR)
- Provides comprehensive visibility across the entire data infrastructure
- Facilitates data-driven decision making for system optimization
- Enhances overall system reliability and performance

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Establish a comprehensive monitoring and alerting framework that covers both cloud and
edge components of your industrial data infrastructure.

### Implementation steps

- Use AWS AWS IoT Greengrass to collect and stream operational telemetry data, such as
device health metrics and diagnostic logs, back to the cloud. This allows the
manufacturing team to maintain visibility into the state of edge components, even in
disconnected scenarios.
- Use Amazon CloudWatch to collect and analyze metrics, logs, and events from
across the hybrid edge-cloud architecture. This includes metrics like data ingestion
rates, database performance, and resource utilization. CloudWatch dashboards and
alarms provide visibility into the overall system health, allowing the team to quickly
identify and address issues. Set baseline performance metrics and configure automated
alerting thresholds.
- To enable end-to-end tracing and diagnostics, use AWS X-Ray. X-Ray provides
detailed insights into the performance and dependencies of distributed components,
helping the team rapidly pinpoint the root cause of problems.
- Consider recording all API calls and configuration changes using AWS CloudTrail,
enabling comprehensive auditing and security monitoring of the data infrastructure.

## Key AWS services

- AWS CloudTrail
- Amazon CloudWatch
- AWS AWS IoT Greengrass
- AWS X-Ray

## Resources

**Related documents:**

- [Security Best Practices for Manufacturing OT](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/security-best-practices-for-manufacturing-ot.html)
- [Monitor edge application performance using AWS IoT Greengrass and AWS Distro for
OpenTelemetry](https://aws.amazon.com/blogs/iot/monitor-edge-application-performance-using-aws-iot-greengrass-and-aws-distro-for-opentelemetry/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaops02-bp01.html*

---

# MIDAOPS03 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# MIDAOPS03-BP01 Define meaningful KPIs and metrics

Manufacturing and industrial organizations require comprehensive visibility into the
health and performance of their data-driven operations. Proper definition and monitoring of
KPIs verify that manufacturing processes remain efficient, reliable, and aligned with business
objective.

**Desired outcome:** Establish a comprehensive set of metrics
and KPIs that provide insights into the performance, reliability, and efficiency of your
operations, production, and industrial data workloads. These metrics and KPIs should enable
proactive identification of issues and optimization opportunities.

**Benefits of establishing this best practice:** By adopting
the best practice and prescriptive guidance, your organization gains improved visibility into
manufacturing operations, enabling timely detection of potential production issues, enhanced
operational efficiency, better resource utilization and reduced downtime and maintenance
costs.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Implement industrial workload-specific KPIs monitoring and alerting that aligns with
industry standards like ISA-95 and focuses on critical production metrics.

### Implementation steps

Define industry-specific KPIs applicable for your workload. Examples of common
metrics industrial data workloads:

- System availability and uptime
- Data ingestion rates and latency
- Processing system performance
- Security events and access patterns
- Network connectivity status
- Edge device health status
- Gateway operational status
- Resource utilization (for example, CPU, memory, or storage) for edge gateways and
cloud services

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaops03-bp01.html*

---

# MIDAOPS03-BP02 Implement real-time monitoring and alerting capabilities

Establish comprehensive monitoring of your industrial data infrastructure with automated
alerts to quickly identify and respond to operational issues before they impact manufacturing
processes. Configure appropriate thresholds and notification channels to quickly alert the
right teams about system health, data quality, and performance anomalies.

**Desired outcome:** Your organization has established a clear,
quantifiable understanding of industrial data workload performance through well-defined
metrics and KPIs that align with business objectives and operational requirements.

**Benefits of establishing this best practice:** Monitoring and
alerting capabilities allow the manufacturing team to quickly identify issues or impending
problems that could impact production, quality, or maintenance.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Develop and implement a comprehensive metrics monitoring framework that captures both
technical and business aspects of your industrial data workload.

### Implementation steps

- Use AWS IoT Greengrass for device software to collect, process, and export data
streams, including when devices are offline. It can act as an industrial data gateway
between the shop floor and your AWS environment.
- For pre-built industrial connectors, implement the [AWS Shop Floor Connectivity (SFC)](https://aws.amazon.com/blogs/industries/collecting-data-from-industrial-devices-to-aws-services/) open-source solution either as a
stand-alone application or as an AWS IoT Greengrass component. SFC is a data ingestion
enabler that delivers customizable greenfield and brownfield connectivity solutions.
It addresses limitations and unifies data collection from existing IoT data collection
services, allowing customers to consistently collect data from equipment across
different vendors for use with various AWS services.
- Consider AWS IoT SiteWise to collect data from disparate data sources using OPCUA
and MQTT connectors. AWS IoT SiteWise Monitor provides near real-time dashboard
visualization of your key metrics and can be configured for alerting workflows.
- Use Amazon Managed Grafana to deliver integrated live dashboards for monitoring
your production KPIs, operations, machine status, and alerts. The dashboards can use
Grafana's native data source connectors to visualize data from multiple AWS services,
including AWS IoT SiteWise, Amazon Timestream, Amazon RDS, and Amazon Aurora. This
provides a unified visualization layer for your industrial data, enabling real-time
monitoring and analysis of your manufacturing operations.
- Configure custom Amazon CloudWatch dashboards and alarms to track critical
metrics, such as data ingestion rates and latency resource utilization (like CPU,
memory, and storage) for edge gateways and cloud services, anomalies or deviations in
key operational KPIs, security events and access patterns*.*

## Key AWS services

- Amazon CloudWatch
- Amazon Managed Grafana
- AWS IoT Greengrass
- AWS IoT SiteWise

## Resources

**Related documents:**

- [Collecting data from industrial devices to AWS Services](https://aws.amazon.com/blogs/industries/collecting-data-from-industrial-devices-to-aws-services/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaops03-bp02.html*

---

# MIDAOPS03-BP03 Implement predictive analytics and proactive anomaly detection

Use machine learning capabilities to analyse historical data patterns and identify
potential issues before they impact your industrial operations.

**Desired outcome:** Identifying anomalies early enabling
organizations to take corrective action before problems escalate and disrupt operations.

**Benefits of establishing this best practice:** By
implementing these real-time monitoring, anomaly detection, and centralized observability
capabilities, industrial organizations can understand the health of their data-driven
operations and maintain the reliability, security, and performance required to support their
business objectives.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Develop real-time monitoring and alerting across your industrial data systems to
proactively detect and resolve issues. Use machine learning and predictive analytics to
identify anomalies before they impact operations.

### Implementation steps

- Implement a centralized cloud data store as an enterprise historian using fully
managed AWS services such as AWS IoT SiteWise and Amazon Timestream.
- Configure multi-tier, cloud-optimized services to store time-series data. Use AWS IoT SiteWise or Timestream for hot data and Amazon S3 for cold data.
- Use Amazon SageMaker AI AI to perform advanced AI/ML analyses of cold data for
preventive maintenance, anomaly detection, and predictive quality insights. Use Amazon SageMaker AI Unified Studio as a single data and AI development environment where you can
access and analyse your organization's data using the best tools across many use
cases.
- Use integrated observability tools to provide a centralized view of the overall
system health and performance, such as AWS X-Ray for distributed tracing. AWS X-Ray
allows the team to quickly pinpoint the root cause of issues that span multiple
components of the data infrastructure.
- For centralized observability and diagnostics, organizations can also use AWS CloudTrail to track API calls and configuration changes, providing an audit trail to
understand the provenance of data and the lineage of operational changes.
- For proactive anomaly detection, integrate Amazon GuardDuty to identify
suspicious activity or security threats, and use machine learning models (for example,
through Amazon SageMaker AI AI) to detect unusual patterns in equipment telemetry data.

## Key AWS services

- AWS IoT SiteWise
- Amazon Timestream
- Amazon Simple Storage Service (Amazon S3)
- Amazon SageMaker AI AI
- Amazon GuardDuty
- AWS CloudTrail
- AWS X-Ray

## Resources

**Related documents:**

- [Strategies for modernizing data historians for the manufacturing industry in the AWS Cloud](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-historian-modernization/introduction.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaops03-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
