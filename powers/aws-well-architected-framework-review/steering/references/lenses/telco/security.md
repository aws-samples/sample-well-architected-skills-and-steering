# Security

**Pillar**: Security  
**Questions**: 5

---

# TELCOSEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 2

---

# TELCOSEC01-BP01 Follow the industry standards and local regulations to host telecom networks in the cloud, demonstrating a security commitment

When operating a telecommunications network in a cloud environment, it is crucial to comply
with relevant industry specifications and local regulatory requirements. This includes adhering
to standards set forth by leading telecom standardization bodies such as the 3rd Generation
Partnership Project (3GPP), which develops technical specifications for mobile networks, and the
European Telecommunications Standards Institute (ETSI), which produces globally applicable
standards for information and communications technologies.

Additionally, the network operations must meet the regulations enforced by authorities like
the Federal Communications Commission (FCC) in the United States and the European Union's
Electronic Communications Code. By aligning with these industry specifications and local laws,
the organization demonstrates a strong commitment to security and building trust with customers.

Adhering to established standards and regulations verifies the cloud-based
telecommunications network functions reliably and safeguards sensitive customer data. This
approach fosters lasting relationships with the customer base through transparent, secure, and
well-regulated operations.

## Implementation guidance

Establish a comprehensive security hardening strategy that protects your AWS
infrastructure through multi-layered defense mechanisms and continuous monitoring. Design a
robust security architecture that encompasses identity management, network segmentation,
encryption protocols, and vulnerability management while maintaining operational efficiency.
Implement centralized logging and monitoring capabilities that provide visibility across the
layers of your infrastructure, enabling rapid detection and response to security incidents.
Create detailed security policies and operational procedures that enforce least privilege
access, automate checks, and maintain audit trails for configuration changes to verify the
integrity and resilience of your cloud environment.

### Implementation steps

- Use Amazon Security Lake for centralized logging.
- Deploy AWS Config for configuration tracking.
- Implement Amazon CloudWatch for monitoring and alerting.
- Enable AWS CloudTrail for API activity logging.
- Configure AWS IAM Identity Center for authentication.
- Set up AWS IAM for role-based access control.
- Deploy AWS Secrets Manager for credential management.
- Enable MFA for privileged accounts.
- Design Amazon VPC architecture for network isolation.
- Configure AWS Transit Gateway for traffic management.
- Implement AWS Network Firewall for traffic filtering.
- Set up security groups and NACLs for micro-segmentation.
- Deploy AWS KMS for key management.
- Configure AWS Certificate Manager for TLS certificates.
- Implement AWS CloudHSM for hardware security modules.
- Enable encryption at rest for data stores.
- Implement AWS Systems Manager for patch management.
- Deploy Amazon Inspector for vulnerability scanning.
- Configure AWS Security Hub CSPM for security posture monitoring.
- Establish automated remediation workflows.

For more detail, see [Enhancing telecom security with
AWS](https://aws.amazon.com/blogs/security/enhancing-telecom-security-with-aws/).

## Resources

**Related documents:**

- [Enhancing telecom security with AWS](https://aws.amazon.com/blogs/security/enhancing-telecom-security-with-aws/)

**Key AWS services:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [AWS IAM](https://aws.amazon.com/iam/)
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec01-bp01.html*

---

# TELCOSEC01-BP02 Encrypt data at-rest and sensitive traffic (control plane, data plane) using secure VPNs and custom encryption keys

Due to regulatory requirements, the CSPs often need to apply
additional encryption to traffic that is not already secured by the underlying transport or
application protocols. Both control plane traffic, such as Diameter signaling, and data plane
traffic, like voice or RTP, require the use of encrypted virtual private networks (VPNs), most
commonly IPsec. It is crucial for CSPs to evaluate their regulatory landscape and establish a
framework to identify and label the traffic and data that needs to be encrypted in transit as
well as at rest, using customer-owned encryption keys.

The data in-use is protected by the
underlying CPU architecture and features like AMD SEV-SNP, Intel TME, and Graviton Memory
Encryption. However, these security measures come with additional costs and limitations, such as
restrictions on packets per second (PPS) per flow (number of IPsec tunnels), PPS per instance
(lack of equal-cost multi-path routing after reaching the largest single-slot capacity),
complexity, and vendor dependencies.

**Desired outcome:**

- Verify sensitive telco network traffic, including control plane and data plane, is
encrypted using secure VPN protocols like IPsec.
- Implement a comprehensive data encryption strategy to protect data in transit and
at rest using customer-managed encryption keys.
- Fulfill regulatory requirements for data protection and secure communications in the
telco industry.
- Maintain the confidentiality and integrity of critical telco network data and signaling
traffic, even when traversing the public cloud infrastructure.
- Provide visibility and control over the encryption keys and algorithms used to secure
the telco workloads.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement a secure, encrypted communication framework for control and data plane traffic
comply with industry standards and regulations. Leverage built-in features for key management,
high availability, and automatic failover. Utilize a centralized key management service to
generate, manage, and rotate encryption keys for securing data in-transit and at-rest across
various systems and services. Verify comprehensive auditing and monitoring of encryption and
key management activities to maintain adherence and provide detailed reporting.

### Implementation steps

- Implement VPN-based encryption for control and data plane traffic:

Configure AWS managed VPN solutions, such as Site-to-Site VPN, to establish secure IPsec
tunnels for control and data plane communications.
- Use the built-in features of these services for automatic key management,
tunnel failover, and high availability.
- Verify the VPN configurations comply with industry standards and regulations
for secure network communications.

- Encrypt data in-transit using custom keys:

Use AWS Key Management Service to generate and manage the encryption keys used to
secure data in-transit.
- Integrate KMS with other AWS services, such as Amazon S3, Amazon EBS, and Amazon RDS, to
transparently encrypt data flowing through these services.
- Implement a key rotation strategy to maintain the cryptographic strength of the
encryption keys over time.

- Encrypt data at rest using custom keys:

Configure AWS services handling telco data, such as Amazon S3, Amazon EBS, and Amazon RDS,
to use customer-managed encryption keys from KMS.
- Verify that sensitive telco data, including logs, metrics, and configuration
files, is encrypted at rest using the custom encryption keys.
- Use KMS key policies to control access and usage of the encryption keys,
aligned with the principle of least privilege.

- Implement key management and rotation:

Establish key management processes and procedures for the creation,
distribution, and rotation of the customer-managed encryption keys.
- Automate key rotation using AWS Lambda functions or AWS Systems Manager, verifying that
keys are updated on a regular basis.
- Integrate the key management processes with the overall security operations and
incident response procedures.

- Maintain audit trails:

Use AWS CloudTrail to create comprehensive audit trails of key management and
data encryption activities.
- Configure AWS Config to continuously monitor the configuration of the encryption
services and report on deviations from the desired state.
- Integrate the encryption and key management data with the organization's
security information and event management (SIEM) system for advanced analytics and
reporting.

## Resources

**Key AWS services:**

- [Site-to-Site VPN](https://aws.amazon.com/vpn/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon EBS](https://aws.amazon.com/ebs/)
- [Amazon RDS](https://aws.amazon.com/rds/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec01-bp02.html*

---

# TELCOSEC02 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 3

---

# TELCOSEC02-BP01 Use secure control plane protocols between the network functions (NF)

The 3rd Generation Partnership Project (3GPP) recommends that telco organizations use
secure control plane protocols between the various network functions (NF) within their 5G core
network architecture. This best practice is crucial for maintaining the confidentiality,
integrity, and availability of the control plane communications, which are essential for the
proper functioning and management of the network.

The control plane is responsible for the exchange of signaling and management information
between network elements, handling critical tasks such as session establishment, mobility
management, and policy enforcement. By implementing secure control plane protocols, telco
organizations can mitigate the risk of unauthorized access, eavesdropping, and tampering of the
control plane traffic, thereby enhancing the overall security and resilience of the network.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement secure communication protocols, such as HTTPS and TLS/DTLS, for control plane
traffic to verify encryption and integrity protection. Use a trusted and secure mechanism
for network function registration and discovery, integrating it with a central registry to
maintain an authorized list of network components. Monitor and analyze the control plane
traffic for anomalies using comprehensive logging and advanced analytics and develop robust
incident response procedures to address security incidents related to the control plane, with
a focus on automated workflows and rapid remediation.

### Implementation steps

Implement secure control plane protocols:

- Verify that the control plane protocols are configured to use secure protocol such
as HTTPs and secure communication channels, such as TLS/DTLS for encryption and
integrity protection.
- Use AWS Certificate Manager to manage and provision the necessary SSL/TLS certificates for
the control plane protocol endpoints.

Secure NF registration and discovery:

- Use a secure NF registration and discovery mechanism, such as the ones defined
in 3GPP TS 29.510, to enable trusted NFs to discover and communicate with each other.
- Integrate the NF registration and discovery process with AWS Cloud Directory or
Service Catalog to maintain a secure and up-to-date registry of authorized network functions.

Control plane traffic monitoring and anomaly detection:

- Implement comprehensive logging and monitoring of the control plane traffic using
Amazon CloudWatch and Amazon OpenSearch Service.
- Configure Amazon GuardDuty to detect and alert on anomalous or suspicious activities
within the control plane protocol communications.
- Use Amazon CloudWatch Logs Insights to perform advanced analysis and forensics on the
control plane traffic logs.

Control plane incident response and remediation:

- Develop and test incident response procedures to address security incidents or
breaches related to the control plane protocols.
- Integrate the control plane security monitoring and incident response capabilities
with the overall security operations and incident management processes.
- Use AWS Lambda, AWS Step Functions, and Amazon SNS to automate the incident response
workflows and facilitate rapid remediation.

## Resources

**Key AWS services:**

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
- [AWS Cloud Directory](https://aws.amazon.com/cloud-directory/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [Amazon OpenSearch Service](https://aws.amazon.com/what-is/elasticsearch/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec02-bp01.html*

---

# TELCOSEC02-BP02 Implement features such as concealed or spoofed subscriber identities for signaling over the interfaces with access network

The 3rd Generation Partnership Project (3GPP) recommends that telco organizations use the
Subscription Concealed Identifier (SUCI) instead of the Subscription Permanent Identifier (SUPI)
on the air interface between the user equipment (UE) and the access network. This best practice
is aimed at enhancing the privacy and security of subscriber identities, as the air interface is
considered the most exposed and vulnerable part of the network.

The SUPI, which includes sensitive subscriber information such as the International Mobile
Subscriber Identity (IMSI), is a unique and permanent identifier associated with each
subscriber. By using the SUCI, a privacy-preserving temporary identifier derived from the SUPI,
telco organizations can block the disclosure of the actual subscriber identity over the air
interface, mitigating the risk of subscriber tracking, profiling, and other privacy-related
attacks.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement a secure mechanism for generating and processing the Subscription Concealed
Identifier (SUCI) instead of the Subscription Permanent Identifier (SUPI) for signaling over
the air interface, maintaining adherence with 3GPP privacy protection schemes. Establish a
secure system for mapping and managing the SUPI-SUCI relationship, with robust encryption and
integrity protection for the air interface communications. Monitor the air interface signaling
for anomalies and develop incident response procedures to address security incidents related
to subscriber identity, prioritizing privacy protection. Verify comprehensive security
governance and adherence with industry standards and regulations for the air interface
security controls.

### Implementation steps

Implement SUCI generation and conversion:

- Configure the UE and the Access and Mobility Management Function (AMF) to generate
and process the SUCI instead of the SUPI for signaling over the air interface.
- Verify that the SUCI is generated using the appropriate privacy protection scheme,
as defined in 3GPP TS 33.501.

Incident response and subscriber identity protection:

- Develop and test incident response procedures to address security incidents or
breaches related to the SUCI signaling over the air interface.
- Use AWS Lambda, AWS Step Functions, and Amazon SNS to automate the incident response workflows
and facilitate rapid remediation.
- Verify that the incident response plan includes steps for investigating,
mitigating, and reporting subscriber identity-related security incidents, while
preserving the privacy of the affected subscribers.

Air interface security governance:

- Establish security governance policies and controls for the management of SUCI
signaling over the air interface.
- Use AWS Config, AWS Security Hub CSPM, and AWS Trusted Advisor to continuously assess the security
posture and verify adherence with industry standards and regulations, such as GDPR.

## Resources

**Key AWS services:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec02-bp02.html*

---

# TELCOSEC02-BP03 Segment and isolate telco network domains and slices

To maintain the security and resilience of a telco network in a cloud environment, segment
and isolate the various domains within the network. The same understanding applies to the
situation where multiple virtual network slices are hosted in a common environment. This
approach assists to mitigate the risk of potential security breaches and minimize the impact of
an incident.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Establish logical isolation by creating distinct network environments for the various
functional domains within the telco network, such as control plane, user plane, management
plane, and signaling plane. Implement robust access controls and monitoring mechanisms to
restrict and govern cross-domain communication. Achieve physical isolation by leveraging
geographically separated infrastructure, if required, and enforce strict access control and
identity management. Facilitate secure connectivity between the isolated network domains
through encrypted and integrity-protected communication channels and manage the necessary
certificates and keys centrally.

### Implementation steps

Logical isolation:

- Identify the distinct functional domains within the telco network, such as control
plane, user plane, management plane and signaling plane.
- Use AWS Virtual Private Cloud (VPC) to create distinct and isolated network
environments for the different functional domains within the telco network, such as
control plane, user plane, management plane, and signaling plane.
- Implement network access controls using AWS security groups and network access
control lists (NACLs) to restrict and monitor cross-domain communications.
- Use AWS VPC Peering to enable secure connectivity between the isolated VPCs,
if required.

Physical isolation:

- Use AWS Availability Zones and Regions to physically separate the network
domains, if needed.
- Use AWS Outposts or AWS Local Zones to deploy dedicated infrastructure for specific
network domains, maintaining physical isolation.
- Integrate AWS Identity and Access Management to enforce strict access control and identity
management for personnel and systems interacting with the isolated domains.

Secure connectivity:

- Establish secure communication using AWS Direct Connect or Site-to-Site VPN for interconnecting the
isolated network domains.
- Use AWS Certificate Manager to manage and renew SSL/TLS certificates for secure
communication.

## Resources

**Key AWS services:**

- [AWS VPC](https://aws.amazon.com/vpc/)
- [AWS
Security Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)
- [AWS
Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [AWS Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [AWS Outposts](https://aws.amazon.com/outposts/)
- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [Site-to-Site VPN](https://aws.amazon.com/vpn/)
- [AWS Private Link](https://aws.amazon.com/privatelink/)
- [AWS
PrivateSubnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec02-bp03.html*

---

# TELCOSEC03 — External interface security

**Pillar**: Security  
**Best Practices**: 1

---

# TELCOSEC03-BP01 Secure the APIs used to expose telco network functionality

In modern telco networks, the Network Exposure Function (NEF) for 5G networks and the
Service Capability Exposure Function (SCEF) for 4G networks provide APIs to expose network
capabilities and services to external applications and partners. These APIs serve as the gateway
for accessing sensitive network resources and data, making it crucial to implement robust
security measures to protect them.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement strong authentication mechanisms and enforce role-based access control to
authorize API access based on client permissions and privileges. Manage user identities and
generate secure JSON web tokens. Verify API communication is encrypted using HTTPS/TLS
protocols and leverage web application firewalls to enforce and monitor security. Implement
API rate limiting and throttling to block potential denial-of-service attacks. Perform input
validation and sanitization on API requests and integrate comprehensive logging and monitoring
to detect and respond to suspicious API activity. Manage API versioning and deprecation to
verify clients use the latest secure versions and regularly assess API security through
automated testing and vulnerability management.

### Implementation steps

- API traffic encryption:

Verify API communication is encrypted using HTTPS/TLS protocols with AWS Certificate Manager
to manage SSL/TLS certificates.
- Leverage AWS WAF (Web Application Firewall) to enforce SSL/TLS adherence and
monitor TLS cipher suite usage.

- API rate limiting and throttling:

Implement API rate limiting and throttling using Amazon API Gateway's built-in
throttling capabilities.
- Configure API Gateway to enforce rate limits and block potential denial-of-service
(DoS) attacks.

- API input validation and sanitization:

Utilize AWS Lambda functions as API backends to perform input validation and
sanitization using libraries like express-validator or Joi.
- Integrate Amazon API Gateway with AWS WAF to apply custom security rules for input
validation and protection against common web application vulnerabilities.

- API logging and monitoring:

Enable comprehensive logging of API requests and responses using Amazon CloudWatch Logs.
- Set up Amazon CloudWatch alarms and Amazon SNS notifications to alert on suspicious API
activity.

- API versioning and deprecation:

USe Amazon API Gateway's versioning capabilities to manage multiple versions of the
NEF and SCEF APIs.
- Implement version-specific access controls using AWS IAM policies to verify
clients use the latest secure API versions.
- Utilize Amazon API Gateway's stage management features to deprecate older API versions
and provide clear migration guidelines.

- API security assessments:

Perform API security assessments using AWS Security Hub CSPM, which aggregates findings
from various AWS security services.
- Address identified vulnerabilities using AWS Systems Manager for patch management and
AWS Lambda for rapid remediation.

## Resources

**Key AWS services:**

- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec03-bp01.html*

---

# TELCOSEC04 — Data Protection

**Pillar**: Security  
**Best Practices**: 1

---

# TELCOSEC04-BP01 Enable encryption for CPNI and PII information at rest and in transit and access restriction

It is recommended that telecommunications organizations implement comprehensive
encryption measures for both customer proprietary network information (CPNI) and personally
identifiable information (PII) at rest and in transit to verify robust data protection and
regulatory adherence. Organizations should use industry-standard encryption algorithms
(such as AES-256) for data at rest, implement TLS/SSL protocols for data in transit, and
establish secure key management practices.

This implementation should include
encryption where applicable, strong access controls with multi-factor authentication, and
regular security audits to verify encryption effectiveness. The organization must verify
that third-party vendors handling CPNI or PII adhere to the same encryption standards and
maintain detailed documentation of encryption practices.

Furthermore, establish comprehensive employee
training programs to verify proper handling of encrypted data, and
incident response plans should be developed specifically for potential breaches of encrypted
information. This recommendation is critical for avoiding potential data breaches,
maintaining regulatory adherence, protecting against financial penalties, and preserving
customer trust. Conduct regular reviews and updates of encryption protocols to
address emerging security threats and maintain the effectiveness of data protection
measures.

**Desired outcome:**

- Verify that customer proprietary network information (CPNI) and personally identifiable
information (PII) data is encrypted at rest and in transit, providing a robust layer of
protection for sensitive customer data.
- Implement strict access controls and least-privilege permissions to limit access to
CPNI and PII data, reducing the risk of unauthorized access or data breaches.
- Demonstrate adherence with industry regulations and customer data privacy requirements,
such as FCC CPNI rules and GDPR, by effectively securing the handling of sensitive
information.
- Provide visibility and auditability of access and usage of CPNI and PII data through
comprehensive logging and monitoring.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance:

Implement robust data protection measures by encrypting customer CPNI and PII data at
rest and in transit. Use customer-controlled encryption keys and secure communication
protocols like TLS. Enforce strict access controls based on the principle of least privilege,
with multi-factor authentication. Enable comprehensive logging and monitoring to track access
and usage activities, integrating the logs into a centralized security framework. Establish
clear data handling policies and procedures and conduct regular audits to verify the
effectiveness of the data protection controls and verify ongoing adherence with industry
regulations and customer privacy requirements.

### Implementation steps

- Encrypt CPNI and PII data at rest:

Use AWS Key Management Service (KMS) to generate and manage customer-controlled encryption
keys for protecting data at rest.
- Configure AWS services handling CPNI and PII data, such as Amazon S3, Amazon RDS, and
Amazon EBS, to use the customer-managed encryption keys from KMS.
- Implement a key rotation strategy to verify the cryptographic strength of the
encryption keys is maintained over time.

- Encrypt CPNI and PII data in transit:

Require the use of secure communication protocols, such as TLS 1.2 or 1.3, for
data transfers involving CPNI and PII information.
- Utilize AWS Certificate Manager to provision, manage, and renew the SSL/TLS certificates used
for encrypting in-transit data.
- Enforce the use of secure protocols and certificate validation across network
connections, including those between internal telco network functions and external
interfaces.

- Implement access controls and least privilege:

Define granular IAM policies to restrict access to CPNI and PII data based on
the principle of least privilege.
- Leverage AWS Identity and Access Management to create roles and policies that limit access to CPNI
and PII data to only the authorized personnel and systems.
- Implement multi-factor authentication (MFA) for users and systems accessing CPNI
and PII data, adding an extra layer of security.

- Enable comprehensive logging and monitoring:

Configure AWS CloudTrail to create detailed audit trails of access and usage activities
related to CPNI and PII data.
- Integrate the CloudTrail logs with Amazon CloudWatch and Amazon OpenSearch Service for centralized security
monitoring and analysis.
- Set up Amazon CloudWatch alarms to trigger alerts for suspicious or unauthorized access
attempts to CPNI and PII data.

- Establish data governance processes:

Develop and enforce data handling policies and procedures aligned with industry
regulations and customer data privacy requirements.
- Integrate the encryption, access control, and logging mechanisms into the
organization's overall security framework.
- Conduct regular audits and assessments to verify the effectiveness of the data
protection controls and verify ongoing adherence.

## Resources

**Key AWS services:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
- [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon OpenSearch Service](https://aws.amazon.com/what-is/elasticsearch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec04-bp01.html*

---

# TELSEC03 — External interface security

**Pillar**: Security  
**Best Practices**: 2

---

# TELSEC03-BP02 Deploy signaling firewall on the roaming and interconnecting interfaces with other telco networks

The Global System for Mobile Communications Association (GSMA) recommends deploying
signaling firewalls on the roaming and interconnecting interfaces with other telco networks.
This best practice is aimed at protecting the telco network from potential signaling-based
attacks and maintaining the overall security and integrity of the network.

The signaling firewall acts as a gatekeeper, monitoring and filtering the signaling
traffic exchanged between the telco network and its roaming partners or interconnected
networks. By implementing a signaling firewall, organizations can effectively mitigate the
risk of unauthorized access, signaling storms, and other signaling-related security threats,
thereby enhancing the resilience and reliability of the network.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Catalog and understand the network topology and signaling traffic across each
identified interface. Deploy a signaling firewall solution capable of deep packet
inspection, protocol validation, and anomaly detection, aligned with the organization's
security policies. Integrate the signaling firewall with comprehensive logging,
monitoring, and centralized security analysis capabilities. Configure the firewall to
inspect and filter signaling traffic, implementing protocol-specific rules to detect and
block unauthorized or malicious activities. Establish robust monitoring and incident
response procedures, integrating the firewall logs with advanced security analytics
tools. Regularly review and update the signaling firewall's configuration, rulesets, and
software versions to maintain effectiveness against evolving threats, leveraging
automated maintenance and validation processes.

### Implementation steps

- Identify roaming and interconnection interfaces:

Catalog the roaming and interconnection interfaces within the
telco network, including the protocols and signaling traffic
exchanged.
- Understand the network topology and the flow of signaling traffic
across the identified interfaces.

- Deploy signaling firewall solution:

Select a signaling firewall solution that is compatible with the
identified protocols and interfaces within the telco network.
- Configure the signaling firewall to align with the organization's
security policies and best practices.

- Integrate signaling firewall with AWS services:

Integrate the signaling firewall with Amazon CloudWatch for comprehensive
logging and monitoring of signaling traffic and security events.
- Utilize AWS Security Hub CSPM to centralize the security findings from the
signaling firewall and other security services, enabling holistic
security analysis and incident response.

- Signaling traffic inspection and filtering:

Configure the signaling firewall to inspect incoming and outgoing
signaling traffic, validating the integrity and authenticity of the
signaling messages.
- Implement signaling protocol-specific rules and policies to
detect and block unauthorized or malicious signaling activities,
such as signaling storms, fraud attempts, and network element
impersonation.
- Regularly update the signaling firewall's rulesets and signatures
to address evolving signaling-based threats and vulnerabilities.

- Signaling firewall monitoring and incident response:

Establish robust monitoring and alerting mechanisms to detect and
respond to anomalies or security incidents related to the signaling
traffic.
- Integrate the signaling firewall logs with Amazon CloudWatch and Amazon OpenSearch Service
for advanced security analysis and threat hunting.
- Develop and test incident response procedures to mitigate the
impact of signaling-based attacks or network disruptions.

- Signaling firewall maintenance and updates:

Regularly review and update the signaling firewall's
configuration, rulesets, and software versions to verify it remains
effective against the latest security threats.
- Leverage AWS Systems Manager for automated patching and updates of the
signaling firewall infrastructure.
- Conduct periodic testing and validation of the signaling
firewall's functionality and security posture.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telsec03-bp02.html*

---

# TELSEC03-BP03 Perform regular penetration testing on each of the protocols implemented on the signaling layer

Perform regular penetration testing on each of the protocols implemented on the signaling
layer of their network. This best practice is crucial for identifying and addressing
vulnerabilities that could be exploited by malicious actors to compromise the security and
integrity of the telco network.

The signaling layer is responsible for the exchange of control and management information
between network elements, making it a critical attack surface. Penetration testing on the
signaling layer protocols assists organizations to uncover potential weaknesses, such as
improper protocol implementation, cryptographic flaws, or insecure configurations, which could
lead to unauthorized access, data breaches, or service disruptions.

By conducting regular and comprehensive penetration testing, telco organizations can
proactively identify and mitigate risks, maintaining the overall resilience and security of
their signaling infrastructure.

## Implementation guidance

Maintain a comprehensive inventory of implemented signaling layer protocols, including
their versions and implementation details. Define the scope and objectives of a penetration
testing exercise focused on the identified signaling protocols, developing a detailed testing
plan aligned with security policies and regulatory requirements. Conduct thorough testing of
the signaling protocols, verifying the proper implementation of security controls, and
identifying vulnerabilities or misconfigurations. Prioritize the discovered vulnerabilities
based on their risk and potential impact, and develop and execute remediation plans to address
them, leveraging automated patch management and security update deployment processes.

### Implementation steps

- Signaling layer protocol inventory:

Identify the signaling layer protocols implemented within the telco network,
such as Diameter, SS7, SIP, and GTP.
- Maintain a comprehensive inventory of the signaling protocols, including their
versions and implementation details.

- Penetration testing scoping and planning:

Define the scope and objectives of the penetration testing exercise, focusing
on the identified signaling layer protocols.
- Verify the penetration testing activities are aligned with the organization's
security policies and regulatory requirements.

- Use AWS security services for penetration testing:

Utilize AWS Security Hub CSPM to centralize the findings and recommendations from the
penetration testing activities.
- Leverage AWS Systems Manager for efficient and secure deployment of the penetration
testing tools and environments.

- Comprehensive signaling protocol testing:

Conduct thorough testing of the identified signaling layer protocols, including
fuzzing, protocol-specific vulnerability scanning, and exploitation attempts.
- Verify the proper implementation of security controls, such as encryption,
authentication, and authorization, within the signaling protocols.
- Identify and document vulnerabilities or misconfigurations that could be
exploited to compromise the signaling layer.

- Remediation and vulnerability management:

Prioritize the identified vulnerabilities based on their risk and potential
impact on the telco network.
- Develop and execute remediation plans to address the discovered
vulnerabilities, including software updates, configuration changes, and the
implementation of additional security controls.
- Use AWS Systems Manager for efficient patch management and deployment of security
updates across the signaling layer infrastructure.

## Resources

**Key AWS services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telsec03-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
