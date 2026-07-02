# SCSEC06 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC06-BP01 Implement network segmentation and isolation to reduce risks across supply chain phases

Network segmentation creates security boundaries between different
stages of your supply chain, limiting the potential impact of
security breaches. By implementing logical separation between
procurement, manufacturing, distribution, and other supply chain
functions, organizations can help prevent lateral movement of
threats and apply specific security controls appropriate to each
segment. This approach enables more granular access control,
improved monitoring, and enhanced protection of sensitive assets
across the supply chain environment. Effective segmentation should
be based on business functions, data sensitivity, and regulatory
requirements.

**Desired outcome:** Segmented and
secure supply chain stages with appropriate access controls and
monitoring.

**Benefits**
**of establishing this best
practice:** Reduced risk of cross-stage contamination and
improved overall supply chain security.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Isolate procurement systems within dedicated network segments
and implement least privilege access controls for procurement
staff, while making sure all sensitive procurement data is
encrypted both at rest and in transit. Isolate manufacturing
systems into separate network zones with stringent access
control lists, and establish secure private connectivity
channels between manufacturing processes and supply chain
partners.

### Implementation steps

- Isolate procurement systems within dedicated network
segments and implement least privilege access controls for
procurement staff, while making sure all sensitive
procurement data is encrypted both at rest and in transit.
- Separate manufacturing systems into separate network zones
with stringent access control lists, and establish secure
private connectivity channels between manufacturing
processes and supply chain partners.
- Deploy web application protection to shield distribution
applications from common web-based exploits and
vulnerabilities.
- Implement comprehensive monitoring and threat detection
across all distribution systems to identify unauthorized
access attempts and behavioral anomalies.
- Establish consistent security tagging and classification
schemes across all supply chain stages to enable automated
security policy enforcement and compliance verification.
- Regularly conduct security assessments and penetration
testing for each supply chain stage to identify and
remediate vulnerabilities before they can be exploited.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec06-bp01.html*

---
