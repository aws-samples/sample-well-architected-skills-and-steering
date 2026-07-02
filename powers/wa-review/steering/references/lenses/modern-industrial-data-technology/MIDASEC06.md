# MIDASEC06 — Data protection

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC06-BP01 Use secure data exchange protocols

Use secure and standardized protocols for sharing industrial data internally and
externally, helping protect integrity and confidentiality.

**Desired outcome:** Data is transmitted securely across
different systems and organizations without unauthorized interception or tampering.

**Benefits of establishing this best practice:** Helps prevent
data breaches, supports secure collaboration, and aligns with industry data exchange
standards.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use MQTT over TLS, HTTPS, or OPC-UA with encryption and certificate-based
authentication.

### Implementation steps

- Configure IoT and gateway devices to communicate over secure protocols.
- Enforce TLS 1.2 or higher for all data-in-transit.
- Implement endpoint authentication using certificates or tokens.
- Monitor traffic for anomalies using AWS IoT Device Defender.

## Resources

- [AWS IoT Core protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)
- [What is AWS IoT Device Defender?](https://docs.aws.amazon.com/iot-device-defender/latest/ug/what-is.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp01.html*

---

# MIDASEC06-BP02 Establish clear data ownership and sharing agreements

Define clear ownership responsibilities and data sharing rules to guide access and usage
across internal teams and partner organizations.

**Desired outcome:** Data is shared responsibly, with clarity
around who controls, accesses, and governs its lifecycle.

**Benefits of establishing this best practice:** Improves
accountability, supports regulatory compliance, and fosters trusted partnerships in the
industrial environment.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Document data ownership roles and access conditions as part of your data governance
framework and reinforce with access controls.

### Implementation steps

- Identify and document data owners across all domains.
- Define acceptable use policies and access controls for each dataset.
- Use AWS Lake Formation and IAM policies to enforce agreements.
- Review agreements regularly to align with evolving compliance needs.

## Resources

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec06-bp02.html*

---
