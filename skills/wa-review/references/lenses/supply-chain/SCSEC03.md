# SCSEC03 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC03-BP01 Implement granular access controls

Implementing granular access controls across your supply chain
environment makes sure that users, systems, and third parties have
precisely the level of access required for their specific
functions. By defining and enforcing fine-grained permissions
based on roles, responsibilities, and contextual factors such as
location or time, organizations can significantly reduce the risk
of unauthorized access to sensitive supply chain data and systems.
This approach minimizes the potential exposure surface while
maintaining operational efficiency through automated provisioning
and de-provisioning processes. Regular reviews and continuous
validation of access patterns help identify anomalies and maintain
the principle of least privilege across complex, multi-party
supply chain networks.

**Desired outcome:** Secure and
controlled access for external parties to supply chain systems and
data.

**Benefits**
**of establishing this best
practice:** Reduced risk of unauthorized access and
improved compliance with data protection regulations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

To manage and control access to supply chain systems and data
for partners, vendors, and third parties, you can use various
AWS services to implement robust access controls, monitoring,
and governance mechanisms.

Use AWS Identity and Access Management (IAM) to create and
manage federated identities, roles, and permissions for your
supply chain partners and vendors, while implementing AWS IAM Identity Center to centrally manage access to multiple AWS accounts and cloud applications, including your supply chain
systems.

### Implementation steps

- Implement a centralized identity management system with
federation capabilities to create and manage external
identities, defining granular role-based access policies
that enforce least privilege principles for all
third-party users and systems.
- Deploy a single sign-on solution across your supply chain
environment to streamline authentication while enforcing
consistent security policies including multi-factor
authentication and conditional access controls based on
risk factors.
- Establish secure private connection methods between your
supply chain systems and partner environments, avoiding
direct internet exposure and creating encrypted
communication channels for all third-party interactions.
- Configure comprehensive activity logging and monitoring
across all supply chain systems, with automated alerts for
suspicious behaviors and regular auditing of third-party
access patterns and usage.
- Implement a resource sharing framework that enables
controlled access to specific supply chain resources while
maintaining centralized governance and helping to prevent
unauthorized lateral movement between systems.
- Create automated onboarding and offboarding workflows for
third-party access that include approval gates,
time-limited access, and regular recertification processes
to help prevent access sprawl and facilitate timely
revocation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec03-bp01.html*

---
