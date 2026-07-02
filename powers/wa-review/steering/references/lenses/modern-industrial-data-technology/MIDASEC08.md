# MIDASEC08 — Application security

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC08-BP01 Align security controls with industry standards

Implement security controls across industrial workloads, and map those controls to
recognized industry standards such as NIST 800-82, ISO/IEC 27001, and IEC 62443.

**Desired outcome:** Security implementations are auditable,
and your organization improves its compliance with applicable industrial regulations.

**Benefits of establishing this best practice:** Streamlines
audit processes, standardizes your security practices, and demonstrates due diligence in
regulated industries.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS Audit Manager and AWS Control Tower to align cloud configurations with
industry-standard security frameworks.

### Implementation steps

- Identify regulatory and industry-specific frameworks applicable to your
workloads.
- Map AWS services and controls to required standards using AWS Audit Manager
frameworks.
- Continuously monitor control adherence using AWS Config and Security Hub CSPM.
- Integrate compliance requirements into the CI/CD process for industrial apps.

## Resources

- [What is AWS Audit Manager?](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)
- [Security standards and controls reference](https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec08-bp01.html*

---

# MIDASEC08-BP02 Conduct regular security awareness programs

Develop training and awareness programs for industrial application teams to reinforce
best practices, policy understanding, and threat awareness.

**Desired outcome:** Engineering and operations staff are
informed about evolving security threats and policies, reducing the risk of human error.

**Benefits of establishing this best practice:** Improves
organizational security culture, reduces social engineering risks, and increases policy
adherence.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Deliver targeted training sessions and simulate threat scenarios relevant to OT and
industrial environments.

### Implementation steps

- Identify key roles that need training (for example, developers, operators, and
integrators).
- Use AWS learning resources or third-party courses tailored to industrial
security.
- Conduct quarterly refresher sessions and phishing simulations.
- Track and report training completion and outcomes to leadership.

## Resources

- [AWS Security Fundamentals (Digital)](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13441/aws-security-fundamentals)
- [NICE Framework Resource Center](https://www.nist.gov/itl/applied-cybersecurity/nice/nice-framework-resource-center)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec08-bp02.html*

---
