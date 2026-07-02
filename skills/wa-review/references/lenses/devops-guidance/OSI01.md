**Saga**: Observability
**Capability**: O.SI — Strategic instrumentation

---

# [O.SI.1] Center observability strategies around business and technical outcomes

**Category:** FOUNDATIONAL

To maximize the impact of observability, it should be closely
aligned with both business and technical goals. This means not
only monitoring system performance, uptime, or error rates but
also understanding how these factors directly or indirectly
influence business outcomes such as revenue, customer
satisfaction, and market growth.

Adopting the ethos that *"Everything fails, all the time"*,
famously stated by Werner Vogels, Amazon Chief Technology Officer, a successful
observability strategy acknowledges this reality and continuously iterates, adapting to
changes in business environments, technical architecture, user behaviors, and customer
needs. It is the shared responsibility of teams, leadership, and stakeholders to establish
relevant performance-related metrics to collect to measure established key performance
indicators (KPIs) and desired business outcomes. Effective KPIs must be based on the desired
business and technical outcomes and be relevant to the system being monitored.

An observability strategy must also identify the metrics,
logs, traces, and events necessary for collection and analysis
and prescribes appropriate tools and processes for gathering
this data. To enhance operational efficiency, the strategy
should propose guidelines for generating actionable alerts and
define escalation procedures. This way, teams can augment
these guidelines to suit their unique needs and contexts.

Use technical KPIs, such as the
[four
golden signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals) (latency, traffic, errors, and
saturation), to provide a set of minimum metrics to focus on
when monitoring user-facing systems. On the business side,
teams and leaders should meet regularly to assess how
technical metrics correlate with business outcomes and adapt
strategies accordingly. There is no one-size-fits-all approach
to defining these
KPIs. Discover
customer and stakeholder requirements and choose the
technical and business metrics and KPIs that best fit your
organization.

For example, one of the most important business-related KPIs for Amazon's e-commerce
segment is *orders per minute*. A dip below the expected
value for this metric could signify issues affecting customer experience or transactions,
which could affect revenue and customer satisfaction. Within Amazon, teams and leaders meet
regularly during weekly business reviews (WBRs) to assess the validity and quality of these
metrics against organizational goals. By continuously assessing metrics against business and
technical strategies, teams can proactively address potential issues before they affect the
bottom line.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF06-BP02 Define a
process to improve workload performance](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_continue_having_appropriate_resource_type_define_process.html)
- [AWS Well-Architected Sustainability Pillar: SUS02-BP02 Align
SLAs with sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html)
- [AWS Well-Architected Reliability Pillar: REL11-BP07 Architect
your product to meet availability targets and uptime service level agreements (SLAs)](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_withstand_component_failures_service_level_agreements.html)
- [Monitoring
and Observability Implementation Priorities](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/implementation-priorities-5.html)
- [AWS Observability Best Practices](https://aws-observability.github.io/observability-best-practices/)
- [Instrumenting
distributed systems for operational visibility](https://aws.amazon.com/builders-library/instrumenting-distributed-systems-for-operational-visibility/?did=ba_card&trk=ba_card)
- [The
Importance of Key Performance Indicators (KPIs) for
Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/)
- [What
is the difference between SLA and KPI?](https://aws.amazon.com/what-is/service-level-agreement/#seo-faq-pairs#sla-kpi)
- [The
Four Golden Signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals)
- [Amazon's
approach to high-availability deployment: Standard
metrics](https://youtu.be/bCgD2bX1LI4?t=2502)
- [The
Amazon Software Development Process: Measure
Everything](https://youtu.be/52SC80SFPOw?t=1922)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.1-center-observability-strategies-around-business-and-technical-outcomes.html*
