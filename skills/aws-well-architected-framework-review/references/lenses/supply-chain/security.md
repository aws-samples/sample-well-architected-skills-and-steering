# Security

**Pillar**: Security  
**Questions**: 14

---

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

# SCSEC02 — Security foundations

**Pillar**: Security  
**Best Practices**: 2

---

# SCSEC02-BP01 Track cloud resources and enforce compliance with automation

Implement automated monitoring systems to continuously track and
inventory all cloud resources throughout your supply chain
environment. Establish compliance guardrails with automated
enforcement mechanisms that validate configurations against
security and regulatory requirements before deployment.

Use automation to regularly audit existing resources, detect drift
from approved configurations, and remediate non-compliant
resources without manual intervention. This approach maintains
consistent governance across your supply chain while reducing the
operational burden of compliance management.

**Desired outcome:** Continuous
compliance tracking and automated remediation across multiple
accounts and regions.

**Benefits of establishing this best
practice:** Real-time detection, automated fixing of
non-compliant configurations, reduced risk of non-compliance and
improved efficiency in managing regulatory requirements.

**Level of risk exposed if this best
practice is not established:** high

## Implementation guidance

Configure AWS Config rules to evaluate resources on a periodic
or real-time basis for continuous compliance monitoring, while
utilizing AWS Config and its proactive mode to automatically
track and remediate resource configurations for continuous
compliance across accounts and regions.

Enable AWS Security Hub CSPM standards and controls to continuously
evaluate if security requirements are met across your supply
chain environments, and Implement automated workflows to route
security findings from AWS Security Hub CSPM to your incident
response and remediation processes.

### Implementation steps

- Deploy AWS Config across the accounts and regions in your
supply chain environment, configuring both periodic and
change-triggered evaluation rules to monitor resource
configurations against compliance standards.
- Activate AWS Config's proactive mode to automatically
remediate non-compliant resources, making sure
configurations consistently meet security requirements
without manual intervention.
- Enable relevant AWS Security Hub CSPM standards (such as CIS
AWS Foundations, AWS Foundational Security Best Practices,
and industry-specific frameworks) to comprehensively
evaluate security posture across your supply chain
accounts.
- Create custom Security Hub CSPM insights that focus
specifically on supply chain-critical resources and
configurations to prioritize security findings relevant to
your business operations.
- Implement automated workflows using EventBridge and Lambda
to route Security Hub CSPM findings to appropriate teams,
ticketing systems, and remediation processes based on
severity and resource type.
- Establish dashboards and regular reporting mechanisms that
provide visibility into compliance status, trends, and
remediation effectiveness across your supply chain
environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec02-bp01.html*

---

# SCSEC02-BP02 Aggregate findings and metrics to maintain centralized visibility

Centralizing security findings and metrics across your distributed
supply chain environment provides comprehensive visibility into
your overall security posture and enables more effective risk
management. By aggregating data from multiple sources, accounts,
and regions into unified dashboards, security teams can quickly
identify patterns, prioritize threats, and coordinate response
efforts across the entire supply chain environment.

This consolidated approach minimizes blind spots that often exist
between different supply chain components and trading partners,
allowing for faster detection of potential security incidents and
compliance issues. Maintaining centralized visibility also
supports more informed decision-making by providing executives and
stakeholders with clear, actionable insights into the security
health of the supply chain network.

**Desired outcome:** Consolidated
view of compliance status across the entire supply chain
infrastructure.

**Benefits**
**of establishing this best
practice:** Enhanced decision-making capabilities and
faster response to compliance issues.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use AWS Config's aggregated view to get a consolidated
compliance picture across multiple AWS accounts and Regions,
while AWS Security Hub CSPM provides a comprehensive view of your
high-priority security alerts and compliance findings from
across AWS accounts.

Integrate compliance data from AWS services into centralized
dashboards and reporting tools for visibility into your overall
supply chain security posture.

### Implementation steps

- Configure AWS Config aggregators to consolidate compliance
data from all supply chain accounts and regions into a
designated security account, providing a unified view of
resource configurations and compliance status.
- Enable AWS Security Hub CSPM in all accounts and establish a
central administrator account to aggregate security
findings, with customized security standards specific to
supply chain operations.
- Implement automated tagging strategies for all resources
to categorize them by supply chain function, allowing for
more granular filtering and analysis of security findings.
- Create custom Amazon CloudWatch dashboards that integrate
metrics from multiple AWS services (Config, Security Hub CSPM,
Amazon GuardDuty, and Amazon Inspector) to visualize
security trends and compliance status across your supply
chain.
- Develop automated reporting workflows using Amazon EventBridge, AWS Lambda, and Quick to generate
and distribute regular security posture summaries to
stakeholders based on their roles and responsibilities.
- Establish integration points between AWS security services
and external SIEM or GRC systems to incorporate supply
chain security data into enterprise-wide risk management
processes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec02-bp02.html*

---

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

# SCSEC07 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC07-BP01 Regularly scan for vulnerabilities, patch your workloads and audit your systems for compliance

Maintaining a proactive vulnerability management program is
critical for identifying and addressing security weaknesses across
supply chain systems. This involves implementing regular scanning
processes to detect vulnerabilities in infrastructure,
applications, and dependencies used throughout the supply chain.
Establishing systematic patching procedures makes sure that
identified vulnerabilities are remediated in a timely manner based
on risk assessment and business impact. Complementing these
activities with regular compliance audits helps verify that
security controls are functioning as intended and meeting
regulatory requirements.

**Desired outcome:** Proactive
identification and remediation of vulnerabilities across supply
chain systems.

**Benefits**
**of establishing this best
practice:** Reduced threat surface and improved
resilience against potential security threats.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Implement automated vulnerability scanning to continuously
assess supply chain-specific workloads, configuring custom
assessment templates for EDI gateways, supplier portals, and
order management systems to prioritize patching based on supply
chain impact and criticality metrics.

Deploy automated patch management to maintain security across
supply chain applications, creating patch baselines specific to
different workload types and coordinating patch deployments with
trading partners to minimize supply chain disruptions.

### Implementation steps

- Implement automated vulnerability scanning to continuously
assess supply chain-specific workloads, configuring custom
assessment templates for EDI gateways, supplier portals,
and order management systems to prioritize patching based
on supply chain impact and criticality metrics.
- Deploy automated patch management to maintain security
across supply chain applications, creating patch baselines
specific to different workload types and coordinating
patch deployments with trading partners to minimize supply
chain disruptions.
- Enable continuous compliance monitoring with custom
controls aligned with supply chain frameworks, tracking
configuration changes to maintain compliance with industry
standards across your supply chain infrastructure.
- Establish a centralized security dashboard to provide
visibility into vulnerability status, patch compliance,
and security posture across all supply chain components
and partner integrations.
- Implement automated remediation workflows that trigger
corrective actions when critical vulnerabilities or
compliance violations are detected in supply chain
systems.
- Create regular reporting mechanisms to communicate
security status to stakeholders and document compliance
with regulatory requirements specific to supply chain
operations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec07-bp01.html*

---

# SCSEC08 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC08-BP01 Implement strong key management in your supply chain systems

Effective encryption key management is fundamental to protecting
sensitive data across supply chain operations. This includes
implementing secure processes for key generation, storage,
rotation, and revocation throughout the key lifecycle.
Organizations should establish clear separation of duties for key
management activities and make sure keys are protected with strong
access controls. Regular auditing of key usage and implementing
automated rotation schedules helps maintain the integrity of
encryption throughout the supply chain environment.

**Desired outcome:** Secure and
controlled management of encryption keys throughout the supply
chain systems, supporting data protection and compliance.

**Benefits**
**of establishing this best
practice:** Enhanced data security, reduced risk of
unauthorized access, and improved compliance through centralized
key management.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Manage encryption keys across different supply chain stages,
creating separate keys for distinct operations (supplier data,
logistics documents, customs documentation) with rotation
policies aligned to compliance requirements. Implement key
policies and access controls that reflect supply chain partner
relationships, using temporary access grants during specific
supply chain events like customs inspections or quality audits.

### Implementation steps

- Manage encryption keys across different supply chain
stages, creating separate keys for distinct operations
(supplier data, logistics documents, customs
documentation) with rotation policies aligned to
compliance requirements.
- Implement key policies and access controls that reflect
supply chain partner relationships, using temporary access
grants during specific supply chain events like customs
inspections or quality audits.
- Enable comprehensive key usage monitoring focused on
supply chain-critical operations, tracking encryption
activities across trade documentation, cross-border data
transfers, and partner data exchanges.
- Configure automated alerts for unusual encryption key
usage patterns that might indicate supply chain process
violations or security incidents.
- Establish a centralized encryption governance framework
that documents key ownership, usage purposes, and access
patterns across the entire supply chain environment.
- Create regular key inventory and access review processes
to make sure encryption controls remain aligned with
evolving supply chain relationships and compliance
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec08-bp01.html*

---

# SCSEC09 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC09-BP01 Implement data classification and protection

A comprehensive data classification framework enables
organizations to identify and appropriately protect different
types of supply chain information. This approach involves
categorizing data based on sensitivity, regulatory requirements,
and business impact to apply proportionate security controls.
Organizations should implement automated discovery and
classification tools to identify sensitive data across diverse
supply chain systems. Protection mechanisms should align with
classification levels, making sure that the most sensitive
information receives the strongest safeguards while maintaining
operational efficiency.

**Desired outcome:** Accurate
classification and appropriate protection of sensitive supply
chain data.

**Benefits**
**of establishing this best
practice:** Improved data protection and compliance with
data privacy regulations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Implement automated data classification using machine learning
and discovery tools to identify and categorize sensitive supply
chain data such as product designs, pricing information, and
logistics data. Apply encryption for sensitive data at rest
across all storage services, facilitating consistent protection
of supply chain information regardless of where it resides.

### Implementation steps

- Implement automated data classification using machine
learning and discovery tools to identify and categorize
sensitive supply chain data such as product designs,
pricing information, and logistics data.
- Apply encryption for sensitive data at rest across all
storage services, facilitating consistent protection of
supply chain information regardless of where it resides.
- Define granular access control policies that enforce least
privilege principles for accessing and managing sensitive
supply chain data across all systems and user roles.
- Manage digital certificates centrally to facilitate secure
encrypted data transmission between supply chain systems,
partners, and service providers.
- Establish data handling procedures that automatically
apply appropriate controls based on data classification,
including retention policies, access restrictions, and
encryption requirements.
- Implement regular data protection audits to verify
classification accuracy and control effectiveness,
adjusting rules and policies as supply chain data
sensitivity evolves.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec09-bp01.html*

---

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

# SCSEC11 — Incident response

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC11-BP01 Develop and implement a comprehensive incident response plan

Establish a comprehensive incident response plan tailored
specifically for supply chain disruptions that clearly defines
roles, responsibilities, and escalation procedures across all
stakeholders including suppliers and logistics partners. Regularly
conduct tabletop exercises and simulations to test the
effectiveness of response protocols under various supply chain
threat scenarios, making sure teams are prepared to act decisively
during actual incidents.

Implement automated detection mechanisms that can quickly identify
potential supply chain security breaches or operational
disruptions, triggering appropriate response workflows. Maintain
secure communication channels and documentation procedures that
enable effective coordination during incidents while preserving
evidence for post-incident analysis and continuous improvement of
security controls.

**Desired outcome:** A
comprehensive and well-tested incident response plan tailored for
supply chain operations.

**Benefits of establishing this best
practice:** Faster response times to security incidents
and minimized impact on supply chain operations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Maintain an up to date incident response plan specifically for
supply chain incidents, with defined roles, communication
procedures, and playbooks that are regularly reviewed and tested
through tabletop exercises. Use AWS Security Hub CSPM to aggregate
security alerts and compliance checks across AWS accounts and
supply chain partners' connected accounts, providing a
centralized view of security posture.

### Implementation steps

- Develop a comprehensive incident response plan
specifically tailored for supply chain operations,
including defined roles, responsibilities, and escalation
procedures for all stakeholders.
- Implement centralized security monitoring and alerting
systems to aggregate findings from multiple sources and
provide unified visibility into supply chain security
posture.
- Establish automated incident detection and response
workflows that can quickly identify and respond to supply
chain-specific security threats and operational
disruptions.
- Configure comprehensive logging and monitoring across all
supply chain infrastructure to enable forensic analysis
and incident investigation capabilities.
- Create secure backup and recovery procedures for critical
supply chain data and systems, with immutable backups
stored in separate secured environments.
- Conduct regular tabletop exercises and incident response
simulations to test and refine response procedures, making
sure all teams are prepared for various supply chain
threat scenarios.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec11-bp01.html*

---

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

# SCSEC13 — Application security

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC13-BP01 Integrate security throughout the software development lifecycle

Incorporate security measures into the earliest stages of the
software development lifecycle (SDLC) to support robust protection
throughout the development process. Develop policies and
procedures for secure coding practices where developers are
trained to follow industry-standard guidelines. Implement security
requirements during the requirements phase, design secure
architectures during the design phase, develop secure code during
implementation, conduct thorough security testing, and maintain
secure deployment and maintenance practices. This comprehensive
approach makes sure that security is not an afterthought but an
integral part of the development process for supply chain
applications.

**Desired outcome:** Security
integrated throughout the SDLC, resulting in more secure supply
chain applications.

**Benefits of establishing this best
practice:** Reduced vulnerabilities in supply chain
applications and lower costs associated with fixing security
issues post-deployment.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Integrate security measures into the earliest stages of the
Software Development Life Cycle (SDLC) to support robust
protection throughout the development process. Develop policies
and procedures for secure coding practices, where developers are
trained to follow industry-standard guidelines for supply
chain-specific requirements including product identification and
tracking, secure data exchange protocols for supplier
communications, and trade partnership security requirements for
cross-border operations.

### Implementation steps

- Define security standards and requirements specific to
supply chain operations during the requirements phase,
including product identification, tracking, and secure
data exchange protocols.
- Design secure architectures during the design phase that
implement chain of custody patterns, secure B2B
integration patterns, and data isolation models for
multi-party supply chain networks.
- Develop secure APIs and Implement digital signature
frameworks during the implementation phase, focusing on
real-time inventory tracking, shipment monitoring, and
electronic proof of delivery.
- Conduct comprehensive security testing including
penetration testing specific to B2B integration points,
security audits on business message flows, and compliance
testing with industry-specific regulations.
- Implement secure deployment practices including key
management for cross-organizational data sharing,
continuous monitoring for supply chain-specific threat
patterns, and incident response procedures for supply
chain disruptions.
- Establish ongoing security maintenance practices including
regular security assessments, vulnerability management,
and security training for development teams working on
supply chain applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec13-bp01.html*

---

# SCSEC14 — Application security

**Pillar**: Security  
**Best Practices**: 1

---

# SCSEC14-BP01 Implement comprehensive code and dependency integrity validation

Maintaining the integrity of application code and dependencies is
critical for helping to prevent supply chain attacks that target
software components. Organizations should implement code signing
to verify authenticity and help prevent tampering with application
components. Automated scanning of dependencies for known
vulnerabilities should be integrated into development workflows to
identify security issues before deployment. Establishing trusted
repositories for approved components and implementing integrity
verification during build and deployment processes creates
multiple layers of protection against compromised software in the
supply chain.

**Desired outcome:** Verified and
secure code and dependencies throughout the supply chain
application lifecycle.

**Benefits of establishing this best
practice:** Reduced risk of compromised applications and
improved overall security of the supply chain environment.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use code signing to verify the authenticity and integrity of
code, involving digitally signing the code with a cryptographic
key to validate it has not been tampered with. Use tools like
AWS CodeArtifact to manage and securely store dependencies,
making sure only approved and verified dependencies are used in
applications, while regularly scanning dependencies for known
vulnerabilities using automated security scanning tools.

### Implementation steps

- Implement code signing processes to digitally sign all
application code and components, supporting authenticity
and helping to prevent tampering throughout the
development and deployment lifecycle.
- Establish secure dependency management using trusted
repositories and automated scanning tools to identify and
remediate vulnerabilities in third-party components before
deployment.
- Implement strict access controls and audit logs in source
control systems to track changes and make sure only
authorized personnel can modify code and dependencies.
- Integrate automated security checks into CI/CD pipelines
to validate code and dependency integrity during build and
deployment processes, helping to prevent compromised
components from reaching production.
- Deploy runtime protection measures and monitoring tools to
detect and respond to unauthorized changes or suspicious
activities in real-time during application execution.
- Establish comprehensive monitoring and logging systems to
maintain visibility into code and dependency integrity
across the entire application lifecycle and supply chain
environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsec14-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
