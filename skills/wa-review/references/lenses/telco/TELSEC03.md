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
