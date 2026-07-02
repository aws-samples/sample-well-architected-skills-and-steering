# SCSEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 3

---

# SCSEC01-BP01 Establish security and governance functions in your CCoE

A robust Cloud Center of Excellence (CCoE) should incorporate
dedicated security and governance functions to implement
consistent implementation of security controls across your supply
chain operations. By embedding these functions within your CCoE,
organizations can establish standardized security practices,
compliance frameworks, and risk management processes that address
the unique challenges of supply chain systems. This approach
enables proactive identification and mitigation of security
vulnerabilities while supporting regulatory compliance across
multi-party supply chain networks. Implementing strong governance
within the CCoE also facilitates clear decision-making authority,
accountability structures, and continuous improvement processes
for supply chain security posture.

**Desired outcome:** A
well-structured CCoE that effectively governs cloud adoption and
security practices across the organization.

**Benefits of establishing this best
practice:** Improved security posture and compliance
adherence through standardized policies and practices.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Establish a cross-functional CCoE team with representatives from
security, compliance, operations, finance, and business units to
drive cloud adoption and governance

The CCoE defines and enforces security policies, standards, and
best practices aligned with financial industry regulations and
your organization's risk posture, while treating the cloud as a
product and application teams as customers to build a culture of
security and compliance into everything.

### Implementation steps

- Assemble a cross-functional CCoE team with representatives
from security, compliance, operations, finance, and
business units, defining clear roles and establishing
regular communication channels.
- Develop comprehensive security policies and standards
aligned with financial industry regulations and your
organization's risk posture, including review processes
for exceptions.
- Design and implement IAM policies enforcing least
privilege access and separation of duties across AWS accounts, with regular access reviews and certification
processes.
- Create self-service resources, training materials, and
consultation services to build a security-first culture
that treats cloud as a product and application teams as
customers.
- Deploy automated policy enforcement through guardrails,
monitoring, and alerting systems to detect violations and
maintain security posture visibility.
- Establish regular governance reviews with continuous
improvement cycles to adapt security practices as cloud
technologies and organizational needs evolve.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec01-bp01.html*

---

# SCSEC01-BP02 Use cloud services to maintain security controls while scaling your supply chain environment

Using cloud security services enables organizations to implement
consistent, automated security controls that scale seamlessly with
dynamic supply chain environments. These services provide built-in
capabilities for threat detection, data protection, identity
management, and compliance monitoring across your entire supply
chain environment.

By integrating cloud security services directly into your
infrastructure as code and CI/CD pipelines, you can make sure
security controls are consistently applied from development
through production while maintaining operational agility.

This approach reduces the operational burden on security teams
while providing enhanced visibility and protection for supply
chain workloads as they scale to meet changing business demands.

**Desired outcome:** Efficient
provisioning of secure, compliance-aligned resources at scale
using AWS native services.

**Benefits**
**of establishing this best
practice:** Streamlined governance and enhanced security
through automated, consistent resource management.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

- Use cloud management and governance services like AWS Control Tower, Service Catalog, and AWS Security Hub CSPM to
provision secure, compliance-aligned resources at scale.
- AWS Control Tower can help set up a secure multi-account
environment following best practices for separation of
duties and least privilege access, while Service Catalog
allows you to create and manage pre-approved, secure IT
service catalogs for your supply chain workloads.

### Implementation steps

- Deploy AWS Control Tower to establish a secure
multi-account environment with guardrails that enforce
separation of duties and least privilege access across
your supply chain infrastructure.
- Create standardized, pre-approved templates in Service Catalog to enable self-service provisioning of secure
supply chain workloads while maintaining governance
controls.
- Implement AWS Security Hub CSPM to gain centralized visibility
into security findings, automate compliance checks, and
continuously monitor security best practices across supply
chain accounts.
- Use AWS Artifact to access and distribute compliance
reports, certifications, and attestations that demonstrate
the security posture of your cloud-based supply chain to
stakeholders and auditors.
- Configure AWS Audit Manager to automatically collect and
organize evidence for regulatory compliance, simplifying
audit preparation and demonstrating adherence to industry
standards.
- Integrate these services with your CI/CD pipelines and
infrastructure as code to make sure security controls
scale automatically with your supply chain workloads and
maintain consistency across environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec01-bp02.html*

---

# SCSEC01-BP03 Practice continuous governance

By establishing a CCoE with cross-functional collaboration, using
cloud governance services, and fostering a culture of continuous
improvement, your organization can effectively address security
and compliance requirements for supply chain workloads in the
cloud.

**Desired outcome:** Adaptive
security policies that evolve with changing business needs and
threat landscapes.

**Benefits of establishing this best
practice:** Increased resilience to emerging threats and
improved compliance through ongoing monitoring and policy updates.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Establish adaptive security policies and procedures that evolve
continuously to align with dynamic business needs, system
modifications, and application updates throughout the
organization's lifecycle.

Continuously monitor and assess your supply chain workloads for
compliance with security policies using automated tools and
processes, while regularly reviewing and updating security
policies and standards based on evolving threats, regulations,
and business needs.

### Implementation steps

- Establish a regular cadence for reviewing and updating
security policies and standards.
- Implement automated compliance checks that run
continuously across your supply chain environment.
- Create a feedback loop between security findings and
policy updates to address emerging threats.
- Develop metrics to measure the effectiveness of security
governance processes.
- Conduct quarterly governance reviews with key stakeholders
from security, operations, and business teams.
- Document and communicate policy changes to all affected
teams and partners.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec01-bp03.html*

---
