**Saga**: Observability
**Capability**: O.DIP — Data ingestion and processing

---

# [O.DIP.6] Standardize telemetry data with common formats

**Category:** RECOMMENDED

Normalize telemetry data using a common format or standard
schema to enhance consistency in data collection and
reporting. This facilitates seamless correlation and analysis
across multiple facets of observability, such as system
performance, user behaviors, and security events, improving
the overall speed and accuracy of detection and response in
any of these areas.

Two notable open-source projects supporting this goal are
OpenTelemetry and the Open Cybersecurity Alliance Schema
Framework (OCSF). OpenTelemetry provides a single set of APIs,
libraries, agents, and collector services to capture
distributed traces and metrics from your application and send
them to any observability platform. OCSF, on the other hand,
is an extensible, vendor-agnostic project designed to simplify
data ingestion and normalization specifically for
cybersecurity events.

Utilize a common telemetry format to streamline these
processes, reduce associated costs of data processing, and
allow teams to focus more on detecting and responding to
actionable events. Guidelines should be established for the
collection and reporting of data, enforcing consistency across
all teams. Adopting and effectively using standard schemas or
frameworks like OpenTelemetry and OCSF can provide
considerable advantages in achieving comprehensive
observability.

**Related information:**

- [OCSF
Schema](https://schema.ocsf.io/)
- [OCSF
GitHub](https://github.com/ocsf)
- [AWS Distro
for OpenTelemetry](https://aws.amazon.com/otel/)
- [OpenTelemetry](https://opentelemetry.io/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.6-standardize-telemetry-data-with-common-formats.html*
