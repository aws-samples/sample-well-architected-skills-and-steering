# MIDASEC09 — Application security

**Pillar**: Security  
**Best Practices**: 3

---

# MIDASEC09-BP01 Apply secure coding practices for applications and data integrations

Implement secure coding guidelines across industrial application development and
integration pipelines to help prevent common vulnerabilities.

**Desired outcome:** Software and data interfaces in industrial
systems are resilient against common attack vectors.

**Benefits of establishing this best practice:** Reduces
injection attacks and vulnerabilities in custom code and enables secure interoperability.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Adopt secure coding checklists (like OWASP), enforce static code analysis, and secure
APIs during development.

### Implementation steps

- Incorporate security requirements into software specifications.
- Use tools like Amazon CodeGuru Reviewer and SonarQube in pipelines.
- Secure APIs with authorization, throttling, and validation.
- Review and test all data transformations and payloads for tampering risks.

## Resources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [What is Amazon CodeGuru Reviewer?](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/what-is-codeguru-reviewer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp01.html*

---

# MIDASEC09-BP02 Perform regular vulnerability scans and penetration tests

Identify and mitigate vulnerabilities in applications and environments by conducting
recurring scans and authorized penetration testing.

**Desired outcome:** Exposed vulnerabilities are proactively
identified and mitigated before exploitation.

**Benefits of establishing this best practice:** Enhances
visibility into system weaknesses and builds resilience against external and internal threats.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use Amazon Inspector and integrate third-party scanning tools for deep and layered
assessments.

### Implementation steps

- Schedule recurring scans using Amazon Inspector across EC2 and container
workloads.
- Perform black-box and white-box pen tests with third-party experts.
- Integrate findings with AWS Security Hub CSPM for centralized visibility.
- Remediate critical vulnerabilities through prioritized CI/CD updates.

## Resources

- [Getting started with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/getting-started.html)
- [Penetration Testing](https://aws.amazon.com/security/penetration-testing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp02.html*

---

# MIDASEC09-BP03 Automate patch management for ICS and connected data infrastructure

Patch known vulnerabilities in a timely manner across industrial control systems (ICS),
gateways, and cloud services by automating patch management processes.

**Desired outcome:** Patches are deployed consistently and
timely, minimizing exposure to known exploits.

**Benefits of establishing this best practice:** Reduces manual
overhead, enhances system stability, and supports compliance with vulnerability remediation
SLAs.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use AWS Systems Manager Patch Manager for cloud-side automation and coordinate closely
with OT vendors for ICS-specific patch cycles.

### Implementation steps

- Inventory all patchable assets across OT and IT systems.
- Use AWS Systems Manager Patch Manager to automate patching for EC2 and managed
nodes.
- Align maintenance windows with production downtime cycles.
- Monitor patch compliance using AWS Config and AWS Systems Manager reports.

## Resources

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)
- [Patch Orchestration with AWS Systems Manager](https://aws.amazon.com/solutions/implementations/patch-orchestration-aws-systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec09-bp03.html*

---
