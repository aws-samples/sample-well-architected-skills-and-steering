**Saga**: Automated governance
**Capability**: AG.DLM — Data lifecycle management

---

# [AG.DLM.2] Strengthen security with systematic encryption enforcement

**Category:** FOUNDATIONAL

With continuous delivery, the risk of data breaches that can disrupt the software
delivery process and negatively impact the business increases. To remain agile and rapidly
able to deploy safely, it is necessary to enforce encryption at scale to protect sensitive
data from unauthorized access when it is at rest and in transit.

Infrastructure should be defined as code and expected to change frequently. Resources
being deploy need to be checked for a compliant encryption configuration as part of
deployment process, while continuous scans for unencrypted data and
resource misconfiguration should be automated in the environment. These practices not only
aid in maintaining compliance, but also facilitates seamless and secure data management
across various stages of the development lifecycle.

Automate the process of encryption key creation, distribution,
and rotation to make the use of secure encryption methods
simpler for teams to follow and enable them to focus on their
core tasks without compromising security. Automated governance
guardrails and auto-remediation capabilities should be used to
enforce encryption requirements at scale, ensuring compliance
both during and after deployment.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL09-BP02 Secure and
encrypt backups](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_secured_backups_data.html)
- [AWS Well-Architected Security Pillar: SEC08-BP02 Enforce
encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html)
- [AWS Well-Architected Security Pillar: SEC09-BP02 Enforce
encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html)
- [AWS Well-Architected Security Pillar: SEC09-BP01 Implement
secure key and certificate management](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_key_cert_mgmt.html)
- [Encrypting
Data-at-Rest and -in-Transit](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html)
- [Amazon's
approach to security during development: Encryption](https://youtu.be/NeR7FhHqDGQ?t=1646)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.2-strengthen-security-with-systematic-encryption-enforcement.html*
