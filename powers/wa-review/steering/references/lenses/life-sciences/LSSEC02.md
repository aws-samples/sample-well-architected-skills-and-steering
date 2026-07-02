# LSSEC02 — Data privacy

**Pillar**: Security  
**Best Practices**: 1

---

# LSSEC02-BP01 Determine applicable regulatory frameworks and enforce data privacy requirements by implementing controls

Many life sciences organizations fall under data privacy
requirements or regulations which influences data security and
architecture, for example where data may be physically located.

**Desired outcome:** Control
objectives identify the locations and conditions where specific data
is required to be stored and controls are implemented.

**Common anti-patterns:**

- Exporting data from shared data sets.
- Manually obfuscating sensitive fields.

**Benefits of establishing this best
practice:** Clarifies requirements as well as control
automation and audit.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by reviewing data privacy requirements within applicable
regulatory frameworks. To determine applicable regulatory
frameworks, start with local regulations and frameworks for the
country where your sensitive data is generated, hosted, and
processed.

Engage with legal counsel who can assist you to define the scope
of the local regulations, as well as additional regulation
frameworks that may apply to you.

Update documentation of data residency requirements and control
objectives with specific details on which data elements are
subject to allowed or disallowed storage and transmission
locations. For more detail, see SEC01-BP03 Identify and validate
control objectives.

Once the determination of requirements has been made and
documented, technical controls can be put in place to enforce
them. Choose which geographic regions to include in your
environment.

Control objectives should be updated to clearly indicate where
data is expected to be located due to data residency requirements.
Implement controls to keep data within those Regions.

### Implementation steps

- Update control objectives to address data residency
regulatory requirements.
- Separate workloads that have different data residency
requirements.
- Implement controls that enhance your digital sovereignty
governance posture.
- Tag PHI data as sensitive and grant least privilege access
only where required.
- Restrict access by location of resource.
- Implement detective controls that notify security operations
when resources are found in unauthorized locations.
- Implement backups to enable recovery from data corruption
and data deletion.
- Update threat models to cover the accidental or malicious
storage of data in unauthorized locations.

## Resources

**Related documents:**

- [Data
Residency with Hybrid Cloud Services Lens - AWS
Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens)
- [Data
protection in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/data-protection.html)

**Related tools:**

- [AWS DataZone](https://aws.amazon.com/datazone/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssec02-bp01.html*

---
