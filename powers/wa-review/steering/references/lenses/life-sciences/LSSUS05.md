# LSSUS05 — Sustainability in clinical trials

**Pillar**: Sustainability  
**Best Practices**: 1

---

# LSSUS05-BP01 Design sustainable clinical trial architecture

Implement decentralized clinical trial architectures that minimize
data movement and reduce environmental impact through regional data
processing strategies and edge computing solutions. Design clinical
trial systems that process data closer to trial populations,
reducing network requirements while maintaining regulatory adherence
and data integrity. Use standardized data management services and
smart archiving strategies to optimize resource utilization
throughout the clinical trial lifecycle.

**Desired outcome:** Achieve
significant reduction in data transfer requirements and
environmental impact of clinical trials while improving data
accessibility, patient experience, and operational efficiency
through decentralized architectures and edge computing solutions.

**Common anti-patterns:**

- You centralize your clinical trial data processing without
considering regional or edge processing alternatives.
- You don't implement data filtering and aggregation at collection
points, transferring raw data.
- You use proprietary data formats instead of standardized formats
like FHIR for clinical data.
- You store your clinical trial data in the same storage tier
regardless of access patterns.
- You don't implement automated data archiving strategies aligned
with regulatory retention requirements.
- You don't consider patient travel reduction opportunities
through remote monitoring and virtual visits.

**Benefits of establishing this best
practice:**

- Reduce data transfer costs and energy consumption through edge
processing and regional architectures.
- Improve patient experience and reduce travel-related emissions
through decentralized trial designs.
- Lower operational costs through optimized data management and
automated archiving strategies.
- Enhance data accessibility and analysis capabilities through
standardized data formats.
- Support regulatory adherence through automated retention and
archiving policies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Clinical trials generate vast amounts of data from diverse sources
including electronic health records, patient-reported outcomes,
wearable devices, and medical imaging. Traditional centralized
approaches require significant data movement and processing
resources, contributing to environmental impact while potentially
creating bottlenecks in data analysis. Decentralized clinical
trial architectures address these challenges by processing data
closer to its source and implementing intelligent data management
strategies.

The shift toward decentralized clinical trials is driven by both
sustainability goals and improved patient outcomes. By
implementing edge computing solutions for patient monitoring and
regional data processing strategies, organizations can
significantly reduce data transfer requirements while maintaining
the high standards of data quality and regulatory adherence
required in clinical research. This approach also enables more
inclusive trial designs by reducing patient travel requirements
and supporting remote participation.

### Implementation steps

- Implement decentralized data collection and processing
architecture:

Deploy AWS IoT Greengrass at clinical sites for local
data filtering and aggregation.
- Implement AWS Direct Connect for secure, dedicated
connectivity between clinical sites.
- Configure AWS PrivateLink for secure communication
between decentralized components.

- Establish edge computing solutions for patient monitoring:

Deploy AWS IoT Core for device connectivity and data
ingestion from wearable devices.
- Use AWS IoT Greengrass for local processing of vital
signs and patient-reported outcomes.
- Implement Amazon Kinesis Data Streams for real-time data
processing at the edge.
- Configure AWS Lambda@Edge for lightweight data
transformation and filtering.

- Implement standardized clinical data management:

Use AWS HealthLake for FHIR-based clinical data
management and standardization.
- Implement Amazon S3 with intelligent tiering for
clinical trial data storage.
- Use AWS Glue for data integration and transformation
across different clinical data sources.
- Configure Amazon Redshift for clinical trial data
analytics and reporting.

- Deploy smart data archiving and lifecycle management:

Implement Amazon S3 lifecycle policies for automated
data archiving based on regulatory requirements.
- Use Amazon Glacier for long-term archival of
completed trial data.
- Configure AWS Config for monitoring and automated policy
enforcement.
- Implement AWS CloudTrail for comprehensive audit trails
of data access and modifications.

- Establish monitoring and optimization processes:

Use Amazon CloudWatch to monitor data transfer volumes
and processing efficiency.
- Establish regular reviews of decentralized architecture
performance and optimization opportunities.

## Resources

**Related best practices:**

- [LSSUS03-BP02
Process data closer to source](lssus03-bp02.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)
- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)

**Related documents:**

- [Advance
environmental sustainability in clinical trials using
AWS](https://aws.amazon.com/blogs/machine-learning/advance-environmental-sustainability-in-clinical-trials-using-aws/)
- [Successful
Decentralized Clinical Trials: A True Possibility with AWS in
the Post-Pandemic Era](https://aws.amazon.com/blogs/apn/successful-decentralized-clinical-trials-a-true-possibility-with-aws-in-the-post-pandemic-era/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus05-bp01.html*

---
