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
