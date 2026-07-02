# SCSEC05 — Detection

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC05-BP01 Implement comprehensive monitoring and threat detection

Implement robust monitoring systems that provide real-time
visibility across all supply chain infrastructure, applications,
and data flows to quickly identify anomalous activities and
performance issues. Deploy advanced threat detection capabilities
that use behavioral analysis and pattern recognition to identify
potential security breaches before they impact operations.
Establish centralized logging and alerting mechanisms that
consolidate security events from diverse sources, enabling rapid
investigation and response to emerging threats. This comprehensive
approach facilitates continuous protection of your supply chain
environment while providing the intelligence needed to adapt
security controls as threats evolve.

**Desired outcome:** Real-time
detection and response to security threats across the supply chain
environment.

**Benefits**
**of establishing this best
practice:** Improved threat detection capabilities and
reduced time to respond to security incidents.

**Level of risk exposed if this best
practice is not established:** high

## Implementation guidance

Enable AWS CloudTrail with separate trails for critical supply
chain operations, configuring event selectors for tracking
Amazon S3 operations on supplier data buckets, API calls to
order management systems, and cross-account activities between
logistics partners. Implement Amazon GuardDuty with custom
threat detection for supply chain operations, monitoring for
unusual patterns such as unauthorized access to supplier
portals, suspicious data transfers between trading partners, or
abnormal API calls to inventory systems.

### Implementation steps

- Enable dedicated monitoring trails for critical supply
chain operations, configuring event selectors to track
operations on supplier data storage, API calls to order
management systems, and cross-account activities between
logistics partners.
- Implement threat detection services with custom detection
rules specifically designed for supply chain operations,
focusing on unauthorized access to supplier portals and
suspicious data transfers between trading partners.
- Deploy automated vulnerability scanning for critical
supply chain workloads including EDI gateways, order
processing systems, and inventory management applications.
- Configure centralized logging with appropriate retention
policies to maintain audit trails of all supply chain
activities and security events for compliance and
investigation purposes.
- Establish automated alerting mechanisms with appropriate
severity levels for different types of security events,
making sure the right teams receive timely notifications.
- Regularly review and update monitoring configurations and
detection rules to address emerging threats and changes in
supply chain infrastructure.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec05-bp01.html*

---
