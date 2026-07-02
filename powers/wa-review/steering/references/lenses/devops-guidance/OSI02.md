**Saga**: Observability
**Capability**: O.SI — Strategic instrumentation

---

# [O.SI.2] Centralize tooling for streamlined system instrumentation and telemetry data interpretation

**Category:** FOUNDATIONAL

Centralized observability platforms are able to offer user-friendly, self-service
capabilities to individual teams that simplify embedding visibility into system components
and their dependencies. These tools streamline the onboarding process and offer
auto-instrumentation capabilities to automate the monitoring of applications.

Adopt an observability platform that provides observability to teams using the
*X as a Service* (XaaS) interaction mode as defined in the [Team Topologies](https://teamtopologies.com/) book by Matthew Skelton and
Manuel Pais. The platform needs to support ingesting the required data sources for effective
monitoring, and provide the desired level of visibility into the system components and their
dependencies.

Onboarding to the platform should be easy for teams, or support auto-instrumentation
to automatically monitor applications for a hands-off experience. This enables the
organization to achieve real-time visibility into system data and improve the ability to
identify and resolve issues quickly.

The observability platform should offer capabilities to follow
requests through the system, the services it interacts with,
the state of the infrastructure that these services run on,
and the impact of each of these on user experience. By
understanding the entire request pathway, teams can identify
where slowdowns or bottlenecks occur, whether this latency is
caused by hardware or dependencies between microservices that
weren't identified during development.

As the observability platform matures, it could begin to offer other capabilities
such as trend analysis, anomaly detection, and automated responses, ultimately aiming to
reduce the mean time to detect ([MTTD](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttd.html)) and the mean time to resolve ([MTTR](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/reducing-mttr.html)) any issues. This can lead to reduced downtime and improved ability to
achieve desired business outcomes.

**Related information:**

- [AWS observability tools](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-observability-tools.html)
- [What
is Amazon CloudWatch Application Insights?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/appinsights-what-is.html)
- [Integrated
observability partners](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/integrated-observability-partners.html)
- [Observability
Access Manager](https://github.com/aws-samples/cloudwatch-obervability-access-manager-terraform)
- [Apache
DevLake](https://devlake.apache.org/)
- [The
Amazon Software Development Process: Self-Service
Tools](https://youtu.be/52SC80SFPOw?t=579)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.2-centralize-tooling-for-streamlined-system-instrumentation-and-telemetry-data-interpretation.html*
