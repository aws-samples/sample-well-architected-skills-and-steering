# Security

**Pages**: 4

---

# Address security and privacy risks

The privacy requirements of government services can be extremely
strict. Take a balanced approach to managing risk by implementing
appropriate privacy and security measures, and by understanding
the real impact of the system on the people, communities, and
businesses affected. Support a security culture where security
measures are frictionless for service operations, and do not place
additional burden on users. This includes responsible, accountable
and auditable stewardship of government data and systems.

**Questions to ask:**

- How can you demonstrate and monitor for security in your
system or service?
- How can you demonstrate compliance to and stewardship of
privacy for all data and systems?
- What are the jurisdictional requirements around identity,
including identity frameworks, data sharing legislation,
privacy impact assessments, and so on?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/address-security-and-privacy-risks.html*

---

# Verifying privacy-by-design

GL-SEC-01: What privacy
practices have you adopted relating to the use of
data?

- **Elevate encryption beyond the basics:** Cloud
technologies make it simpler and cost effective to encrypt data. Government
jurisdictions have specific compliance and data classification requirements. For
example, they might have hardware or software certification requirements, or require
that cryptographic controls be managed independently of the cloud service provider’s
managed encryption services.

**Improvement plan** – Leverage encryption to
protect data at transport and at rest. See the AWS Digital Sovereignty Pledge and
guidance.

- **Document how privacy and end user control has been
considered:** The possibilities for a personalized government service
delivery must be balanced with maintaining end user control and privacy to maintain
public trust. Government services should be designed to be as private as
possible. Architects can link to data in place, use verifiable claims and credentials
where possible, to maintain strong privacy controls and minimize any requirement to
create new copies of data. Validate that sensitive data is protected, removed, or
obfuscated to limit exposure. Use detection controls so that the operations team knows
where sensitive data exists in the service. Access to data should require users and
systems to demonstrate a strong security posture assessment, enforced with fine-grained
authorization rules and multiple authentication controls.

**Improvement plan** – Encourage the organization
to consider privacy in the design and management of the service.

- **Give end users appropriate control:** To help alleviate
privacy concerns, provide end users as much control over their experience as possible.
This control can include the ability to dial up or down the helpfulness of the service,
for example, the level of prompting, proactive delivery, or other forms of
personalization. Be transparent about data storage, use, transmission, and access.
Modern technologies must allow for continuous and informed consent mechanisms where
users can be involved in the decision to share their data. Make it simple for end users
to understand what has been shared, with whom, and for what purpose. Enable them to
revoke consent at will, and verify that access to the data is immediately restricted.

**Improvement plan** – Encourage the organization
to consider personal agency in the design and management of the service.

- **Minimize data copies where avoidable:** In some
circumstances, the ability to link to existing data might not be possible. Make use of
aggregated data, synthetic data, or both. Use techniques such as verifiable claims or
confidential computing to verify that the service can be operated with similar data to
what is expected, while minimizing the risk of exposure or re-identification of
personally identifiable information (PII).

**Improvement plan** – Identify ways to use data
that leverages verifiable claims, credentials, anonymization, and APIs for
consideration by the organization.

- **Enforcing exposure consequences:** Verify that vendor
contracts inherit these obligations, and use legal and contractual means to prohibit the
sharing, reuse, or storing of the data for any purpose other than delivering the
government service.

**Improvement plan** – Support the organization to
assess exposure consequences.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/ensuring-privacy-by-design.html*

---

# Shifting to a real time security model

When security is compliance-led or reactive, it can miss opportunities to be proactive
in real time.

GL-SEC-02: How do you handle
real time responsiveness to security (including national
security) threats?

- **Do threat modelling and scenario planning**to assess and
inform business continuity planning, including an incident response plan within your
ecosystem, taking into consideration critical infrastructure, outside interference,
disaster preparedness, and national resilience.

**Improvement plan** – Use scenario planning, and
conduct an AWS security audit to help identify areas to improve.

- **Test and document how security threats are detected and disrupted
in real time**, including the escalation plan and mechanisms to relevant
security and intelligence agencies for that jurisdiction.

**Improvement plan** – Run threat scenarios with
the organization to identify and document how threats are detected and disrupted in
real time with clear lines of accountability. Provide AWS guidance and tools, such
as AWS Shield Advanced, and consider an AWS security workshop.

- **Document the critical infrastructure
considerations**, as this is of particular
importance for national critical infrastructure.

**Improvement plan** – Support the organization to
identify critical dependencies and likely impacts of service disruption.

Note
The operational excellence pillar addresses
agile operating models which support this
outcome.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/shifting-to-a-real-time-security-model.html*

---

# Resources

- [AWS Shield Advanced
Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary-capabilities.html)
- [AWS Digital
Sovereignty Pledge](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/)
- [Security, Identity, and Compliance on
AWS](https://aws.amazon.com/products/security/)
- [AWS Risk and
Compliance whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html)
- [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)
- [Why AWS Data
Exchange?](https://aws.amazon.com/data-exchange/why-aws-data-exchange/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/resources-1.html*

---
