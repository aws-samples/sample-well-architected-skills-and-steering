# LSPERF18 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF18-BP01 Perform cross-functional performance reviews between IT and scientists

IT professionals and scientists conduct joint performance reviews to
evaluate system effectiveness. These teams set specific goals that
align technical capabilities with scientific needs. For example,
they might target a 99.9% system uptime while verifying that data
accuracy meets research requirements.

**Desired outcome:** Achieving
specific uptime and performance goals through joint performance
reviews and aligned technical-scientific goal setting.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To effectively implement collaborative performance reviews, bring
together IT professionals and scientists in structured evaluation
sessions that assess system effectiveness from both technical and
scientific perspectives. These cross-functional teams should
establish specific, measurable goals that harmonize technical
capabilities with scientific requirements, such as maintaining
99.9% system uptime while simultaneously verifying that data
accuracy meets rigorous research standards.

Create detailed documentation of these performance standards,
clearly articulating how technical metrics connect to validation
requirements and scientific outcomes.

Develop comprehensive monitoring dashboards that visualize both
technical performance indicators (latency, throughput, resource
utilization) and scientific metrics (data quality, validation
status, experimental reproducibility). This integrated view
enables teams to identify optimization opportunities that don't
compromise scientific integrity.

Implement regular review cycles where technical and scientific
stakeholders jointly analyze performance data, discuss potential
improvements, and make data-driven decisions about system
adjustments.

### Implementation steps

- Schedule reviews using AWS Systems Manager OpsCenter items.
- Track service-level agreements (SLAs) with Amazon CloudWatch
dashboards and custom metrics.
- Document goals in AWS Well-Architected Tool workloads.
- Implement Amazon SageMaker AI Model Monitor for accuracy
checks.
- Use Service Catalog to enforce approved configurations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf18-bp01.html*

---

# LSPERF18-BP02 Document performance standards aligned with validation requirements

Metrics establish clear standards to assess regulatory adherence.
Our approach balances system performance with validation
requirements. Analytics-driven monitoring provides visibility into
status and system performance, enabling teams to make decisions
based on measurements rather than assumptions. This monitoring
approach assits organizations to maintain regulatory adherence while
improving efficiency, creating a framework where performance and
validation work together.

**Desired outcome:** Implement
analytics-driven monitoring that balances system performance with
validation requirements, enabling measurement-based decision-making
to simultaneously maintain regulatory adherence and improve
operational efficiency.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Effective implementation of monitoring requires establishing
clear, measurable standards that precisely define regulatory
adherence expectations for generative AI systems. Organizations
should develop a balanced approach that simultaneously evaluates
technical system performance and validation requirements,
recognizing that these aspects are complementary rather than
competing priorities.

Deploy analytics-driven monitoring solutions that provide
comprehensive visibility into both status and operational metrics
through integrated dashboards accessible to stakeholders. This
dual-perspective monitoring empowers cross-functional teams to
make evidence-based decisions grounded in actual measurements
rather than assumptions, creating a data-driven culture around
audit management.

The monitoring framework should include automated alerts for audit
deviations, regular reporting cycles, and trend analysis
capabilities to identify potential issues before they become
critical.

By implementing this integrated approach, organizations can
maintain strict regulatory adherence while continuously improving
system efficiency, establishing an operational environment where
performance optimization and validation requirements work in
harmony rather than opposition

### Implementation steps

- Configure AWS Config rules to automate monitoring.
- Implement AWS Security Hub CSPM for centralized reporting.
- Deploy Amazon CloudWatch metrics for performance and
validation tracking.
- Use Amazon OpenSearch Service for advanced data analytics.
- Create Amazon EventBridge rules to alert on deviations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf18-bp02.html*

---

# LSPERF18-BP03 Create integrated dashboards showing both performance and metrics

The integrated dashboards combine performance and metrics into clear
visualizations. Teams gain complete system visibility through
real-time data, which enables direct decision-making and reduces
process delays. The system enhances operations while maintaining
scientific integrity and patient safety standards. Teams use this
data to optimize systems while meeting medical and regulatory
requirements.

**Desired outcome:** Deploy
integrated dashboards with real-time visualization of performance
and metrics, providing complete system visibility that enables
immediate decision-making, reducing process delays, and allows teams
to optimize operations while maintaining scientific integrity and
patient safety standards.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To effectively implement integrated monitoring systems, develop
comprehensive dashboards that seamlessly combine technical
performance metrics with audit indicators in clear, actionable
visualizations. These unified interfaces should present real-time
data streams that provide complete system visibility to both
technical and scientific stakeholders, reducing information silos
that typically delay decision-making processes.

Configure the dashboards to display critical performance
parameters (such as response times, throughput, and resource
utilization) alongside relevant metrics (including data quality
indicators, validation status, and regulatory adherence scores).
This integrated approach enables cross-functional teams to make
informed, data-driven decisions without process delays that often
occur when metrics are segregated across different systems.

Implement automated alerting mechanisms that notify appropriate
personnel when metrics approach predefined thresholds, allowing
proactive intervention before issues impact operations. The
monitoring system should maintain comprehensive audit trails that
document both performance optimizations and regulatory adherence,
supporting regulatory requirements while enabling continuous
improvement.

### Implementation steps

- Deploy Amazon CloudWatch dashboards with custom generative
AI performance widgets.
- Integrate AWS Audit Manager metrics for visualization.
- Implement Amazon EventBridge for real-time alerts on
threshold violations.
- Use Quick for interactive data exploration and
analysis.
- Configure AWS Systems Manager for automated remediation
workflows.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf18-bp03.html*

---
