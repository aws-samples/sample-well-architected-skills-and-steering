**Saga**: Observability
**Capability**: O.SI — Strategic instrumentation

---

# [O.SI.5] Set and monitor service level objectives against performance standards

**Category:** RECOMMENDED

Teams should define and document Service Level Objectives (SLOs) for every service,
regardless of whether it is directly consumed by external customers or used internally.
SLOs should be accessible and clearly communicate the expected standard of performance and
availability for the service. While Service Level Agreements (SLAs), which define a
contract that must be met for service availability, are typically defined and published
for services that are directly consumed by customers, it is equally important to establish
SLOs for services consumed internally. Such SLOs help ensure performance standards are
met, even in the absence of formal SLAs, and can also act as data points for meeting Key
Performance Indicators (KPIs).

The creation of SLOs should be a collaborative effort
involving both the business and technical teams. The technical
team must provide realistic estimations based on the system's
capabilities and constraints, while the business team ensures
these align with the company's business objectives and
internal standards.

SLOs should be SMART (Specific, Measurable, Achievable,
Relevant, and Time-bound). This means that they should clearly
define what is to be achieved, provide a way to measure the
progress, ensure that the goals can realistically be achieved
given the current resources and capabilities, align with
business objectives, and set a time frame for the achievement
of these goals.

When defining SLOs, rather than using averages, it is
preferable to use percentiles for measurement. Percentiles are
more reliable in detecting outliers and provide a more
accurate representation of the system's performance. For
example, a 99th percentile latency SLO means that 99% of
requests should be faster than a specific threshold, providing
a much more accurate depiction of the service's performance
than an average would.

Teams internally measure and monitor their SLOs to ensure they
are meeting the defined business and technical objectives.
When measuring against a SLO, teams produce Service Level
Indicators (SLIs), which are the actual measurements of the
performance and availability of the service at that point in
time. SLIs are used to evaluate whether the service is meeting
the defined SLOs. By continuously tracking SLIs against the
target SLOs, teams can detect and resolve issues that impact
the performance and availability of their services while
ensuring that they continue to meet both external customer
expectations and internal performance standards.

Continuous improvement and periodic review of SLOs are
required to ensure they remain realistic and aligned with both
the system's capabilities and the business's objectives. Any
changes to the system that could affect its performance should
trigger a review of the associated SLOs.

**Related information:**

- [What
Is SLA (Service Level Agreement)?](https://aws.amazon.com/what-is/service-level-agreement/)
- [What
is the difference between SLA and KPI?](https://aws.amazon.com/what-is/service-level-agreement/#seo-faq-pairs#sla-kpi)
- [AWS Well-Architected Framework - Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
- [Designed-For
Availability for Select AWS Services](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/appendix-a-designed-for-availability-for-select-aws-services.html)
- [Understanding
KPIs ("Golden Signals")](https://aws-observability.github.io/observability-best-practices/guides/operational/business/key-performance-indicators/#10-understanding-kpis-golden-signals)
- [The
Importance of Key Performance Indicators (KPIs) for
Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.5-set-and-monitor-service-level-objectives-against-performance-standards.html*
