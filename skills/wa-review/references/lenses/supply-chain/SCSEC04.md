# SCSEC04 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC04-BP01 Implement least privilege access

Least privilege access and separation of duties create critical
security boundaries between different supply chain functions,
helping to prevent a single individual from controlling an entire
process that could compromise data integrity or operational
security.

For organizations with complex supply chains, these principles
form the foundation of a zero-trust security model that protects
sensitive information, maintains regulatory compliance, and
preserves the integrity of supply chain operations.

**Desired outcome:** Minimized risk
of unauthorized access and data breaches through granular access
controls.

**Benefits of establishing this best
practice:** Enhanced security posture and compliance with
regulatory requirements for access control.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Define IAM policies tailored to common supply chain roles such
as supplier, logistics partner, and quality inspector, and use
IAM Access Analyzer to refine permissions and verify strict
adherence to the principle of least privilege across your supply
chain environment. Implement a multi-account strategy with
dedicated Organizational Units for different supply chain
functions, using service control policies to enforce
restrictions on actions within these OUs, and configure custom
rules to monitor and enforce supply chain-specific compliance
requirements.

### Implementation steps

- Design a role-based access control framework with supply
chain-specific roles, mapping each role to precisely
defined permissions that align with job responsibilities
and implementing automated access analyzers to identify
and remove excessive permissions.
- Implement a multi-account architecture with dedicated
Organizational Units for distinct supply chain functions,
using service control policies to enforce boundaries
between operational areas and help prevent unauthorized
actions across account boundaries.
- Configure automated compliance monitoring with custom
rules to detect violations of separation of duties, track
changes to critical supply chain resources, and facilitate
proper implementation of access controls across all
environments.
- Develop standardized, pre-approved resource templates for
common supply chain workloads with embedded security
controls and access constraints that enforce least
privilege by default during provisioning.
- Establish automated workflows for access requests,
approvals, and provisioning that incorporate appropriate
segregation of duties checks and maintain audit trails of
all access changes across the supply chain environment.
- Implement regular access reviews and certification
processes specific to supply chain roles, with automated
detection of toxic combinations of permissions that could
violate separation of duties principles.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec04-bp01.html*

---
