# SCSEC12 — Incident response

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC12-BP01 implement comprehensive logging and forensic analysis framework

Implement a robust logging and monitoring framework that captures
detailed audit trails across all supply chain systems,
applications, and partner interactions to enable thorough forensic
analysis of security events. Deploy centralized log management
solutions that aggregate and correlate security data from diverse
sources, providing investigators with comprehensive visibility
into supply chain activities and potential security incidents.
Establish automated analysis capabilities that can quickly process
large volumes of log data to identify patterns, anomalies, and
indicators of compromise across the extended supply chain network.
Maintain appropriate log retention policies and secure storage
mechanisms to make sure forensic evidence remains available and
tamper-proof for compliance and investigation purposes.

**Desired outcome:** Comprehensive
logging and monitoring framework for efficient forensic analysis
of security events.

**Benefits of establishing this best
practice:** Improved ability to investigate and resolve
security incidents, enhancing overall supply chain security.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Implement comprehensive logging from all supply chain systems
and applications into centralized log management solutions,
providing a single source of truth for security and operational
data. Use AWS CloudTrail to record API activity across AWS accounts in the supply chain environment, enabling detailed
auditing of actions and changes across the infrastructure.

### Implementation steps

- Centralize logging from all supply chain systems and
applications into a unified log management solution that
provides comprehensive visibility and search capabilities.
- Configure detailed API activity logging across all AWS accounts and services used in the supply chain environment
to maintain complete audit trails.
- Implement automated log analysis and correlation
capabilities to rapidly identify security incidents and
anomalous activities across the supply chain network.
- Deploy specialized forensic analysis tools that can
visualize and analyze security data to identify root
causes and impact of security incidents.
- Establish appropriate log retention policies and secure
storage mechanisms to make sure forensic evidence remains
available for compliance and investigation requirements.
- Create automated reporting and alerting mechanisms that
notify security teams of potential incidents and provide
initial analysis to accelerate response efforts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec12-bp01.html*

---
