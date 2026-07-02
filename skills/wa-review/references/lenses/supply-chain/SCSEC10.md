# SCSEC10 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC10-BP01 Implement comprehensive data encryption

A holistic encryption strategy is essential for protecting supply
chain data throughout its lifecycle. This includes implementing
strong encryption for data at rest in storage systems, databases,
and backup media across all supply chain environments.
Complementary transport encryption should secure data as it moves
between systems, partners, and geographic locations. Organizations
should select appropriate encryption algorithms and key lengths
based on data sensitivity and regulatory requirements, while
making sure that encryption implementation doesn't significantly
impact system performance or user experience.

**Desired outcome:** Comprehensive
encryption of supply chain data throughout its lifecycle.

**Benefits of establishing this best
practice:** Enhanced data protection and reduced risk of
data breaches or unauthorized access.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Implement a centralized encryption key management strategy with
regular key rotation schedules to protect supply chain data
across all services and integrate with broader encryption
features. Configure server-side encryption for all object
storage containing supply chain data using appropriate key
management options based on sensitivity levels and compliance
requirements.

### Implementation steps

- Implement a centralized encryption key management strategy
with regular key rotation schedules to protect supply
chain data across all services and integrate with broader
encryption features.
- Configure server-side encryption for all object storage
containing supply chain data using appropriate key
management options based on sensitivity levels and
compliance requirements.
- Enable encryption for all relational database instances
that store supply chain information, selecting the
appropriate key management approach based on security
requirements and operational needs.
- Activate encryption for all block storage volumes
supporting supply chain applications to facilitate data
protection at the storage layer regardless of
application-level encryption.
- Establish an encryption governance framework that
documents which encryption methods are applied to
different types of supply chain data and systems based on
classification and risk assessment.
- Implement automated compliance monitoring to verify that
encryption controls remain consistently applied as supply
chain infrastructure evolves and new resources are
provisioned.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec10-bp01.html*

---
