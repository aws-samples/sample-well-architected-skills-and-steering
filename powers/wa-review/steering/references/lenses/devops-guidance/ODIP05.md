**Saga**: Observability
**Capability**: O.DIP — Data ingestion and processing

---

# [O.DIP.5] Optimize telemetry data storage and costs

**Category:** RECOMMENDED

Optimize costs associated with storing and processing large
amounts of telemetry data by using techniques like data
filtering and compression. When dealing with non-security
related telemetry data, data sampling can also be an effective
method to reduce costs.

Select cost-effective solutions and consumption-based resources for data storage. Be
strategic about data retention—remove unused or unnecessary data from storage regularly.
Also, be selective about which data sources are ingested and ensure they are required for
effective analysis to avoid unnecessary spend. Always remember that while managing costs
is important, it should not compromise the integrity and completeness of your data,
especially when it comes to security.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF03-BP01
Understand storage characteristics and requirements](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_right_storage_solution_understand_char.html)
- [AWS Well-Architected Sustainability Pillar: SUS04-BP05 Remove
unneeded or redundant data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.dip.5-optimize-telemetry-data-storage-and-costs.html*
