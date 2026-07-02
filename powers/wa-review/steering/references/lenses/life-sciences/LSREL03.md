# LSREL03 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# LSREL03-BP01 Digitize and modernize archival of research data

Replace legacy storage formats such as tapes, optical disks, or
local hard drives with digital storage strategies that provide
redundancy, immutability, and verifiable integrity. Centralized
digital archives keep data accessible, protected from degradation,
and adhere to long-term retention requirements.

**Desired outcome:**

- Research and clinical data remains intact and accessible for
extended periods.
- Immutable archives block tampering or accidental deletion.
- Metadata supports efficient search and retrieval for audits or
scientific review.

**Common anti-patterns:**

- Relying on physical tapes or local servers with no periodic
validation.
- Storing critical data without metadata, making retrieval
inefficient.
- Keeping data in non-standard formats that hinder long-term
usability.

**Benefits of establishing this best
practice:**

- Improved durability and accessibility compared to physical
archives.
- Reduced operational costs and manual overhead of physical
storage.
- Simplified adherence to regulatory audits through traceable,
verifiable archives.
- Supports reproducibility by keeping datasets intact and usable
over decades.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Long-term storage strategies should prioritize immutability and
regulatory alignment. Establish centralized digital archives with
policies that enforce retention and stop premature deletion.
Periodically validate archived datasets with integrity checks and
maintain metadata to verify that datasets are searchable and
contextualized. Migrating legacy media into durable repositories
reduces the risk of data degradation and provides consistent
access across global research teams.

### Implementation steps

- Digitize and migrate legacy media into Amazon S3 with Object
Lock to enforce immutability.
- Use Amazon Glacier Vault Lock to apply retention rules.
- Migrate large historical datasets efficiently with AWS
DataSync.
- Schedule automated integrity checks with Amazon S3 Inventory
and log validation results into AWS Audit Manager for audit
tracking.
- Maintain searchable metadata indexes using Amazon DynamoDB
or Amazon OpenSearch Service to enable rapid dataset
retrieval during audits or scientific reviews.

## Resources

**Related best practices:**

- Data integrity validation for regulatory adherence
- Metadata management and data cataloging
- Lifecycle management policies for long-term research data

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel03-bp01.html*

---

# LSREL03-BP02 Implement tiered storage and recovery strategies

Adopt a tiered approach to storage and retrieval, balancing cost,
durability, and recovery speed. Critical research datasets should be
stored in durable, retrievable formats, while less frequently
accessed archives can be stored in lower-cost, long-term archival
tiers.

**Desired outcome:**

- Cost-effective storage of large volumes of research data.
- Ability to retrieve datasets reliably within regulatory or
operational timelines.
- Long-term durability and reproducibility for clinical trial and
research data.

**Common anti-patterns:**

- Treating each dataset equally, leading to unnecessary costs or
slow recovery.
- Archiving data without defining retrieval timelines or
compliance-related needs.
- Failing to test retrieval procedures, risking failed restores
during audits.

**Benefits of establishing this best
practice:**

- Reduces storage costs without sacrificing durability.
- Provides scalable recovery aligned with business and
compliance-related needs.
- Improved preparation for regulatory audits or re-analysis of
research and clinical data.
- Supports sustainable scaling of data management as volumes grow
exponentially.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Classify datasets by criticality, regulatory requirements, and
access frequency. Assign storage tiers accordingly, with active
datasets kept on performant storage and archival datasets
transitioned to lower-cost tiers. Lifecycle automation reduces
human error and improves adherence to retention schedules.
Recovery workflows must be tested periodically to confirm that
timelines can be met during regulatory audits or scientific
reviews.

### Implementation steps

- Store frequently accessed datasets in Amazon S3 Standard,
then transition infrequently accessed data to Amazon Glacier Flexible Retrieval or enable Amazon S3
Intelligent-Tiering.
- Archive rarely accessed datasets with Amazon Glacier Deep
Archive for the lowest-cost, long-term retention.
- Use S3 Lifecycle Policies to automate transitions across
tiers.
- Implement recovery workflows using AWS Step Functions to
orchestrate retrieval steps, and align with regulatory
timelines and audit needs.

## Resources

**Related best practices:**

- Business continuity planning for research data
- Backup validation and recovery testing
- Risk-based classification of clinical and research datasets

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel03-bp02.html*

---
