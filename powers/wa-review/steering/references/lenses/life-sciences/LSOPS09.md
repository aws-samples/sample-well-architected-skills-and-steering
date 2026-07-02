# LSOPS09 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS09-BP01 Track data ownership and lineage over the life of the project

Data lineage in life sciences projects involves tracking the origin,
movement, and transformation of data throughout its lifecycle. This
process is important because it provides a clear history of how data
has been collected, processed, and used. Maintaining accurate data
lineage improves data integrity, aids in troubleshooting errors, and
supports regulatory adherence. It also allows researchers and
regulators to understand and trust the data's journey from its
source to final analysis, which is critical for validating research
findings and meeting stringent industry standards.

**Desired outcome:** Have a clear,
auditable history of data lineage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use data sharing and management tooling that includes audit
history of access and changes and allows for granular permissions.

### Implementation steps

- Set up an Amazon DataZone or Amazon SageMaker AI Unified Studio
domain and related projects:

- Create a business domain for life sciences data.
- Configure projects and data catalogs.
- Set up user roles and access controls.

- Enable  automatic lineage tracking:

- Use Amazon DataZone or Amazon SageMaker AI Unified Studio
lineage capabilities.
- Connect to data sources (like Amazon S3 or Amazon RDS).
- Use built-in metadata collection.

- Implement governance:

- Use DataZone or SageMaker AI Unified Studio data sharing
workflows.
- Configure approval processes.
- Set up automatic data classification.

## Resources

**Related documents:**

- [Data
lineage in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-data-lineage.html)
- [Best
practice 4.5 – Track data and database changes](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.5-track-data-and-database-changes..html)

**Related tools:**

- [Amazon
DataZone](https://aws.amazon.com/datazone/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops09-bp01.html*

---
