# MIDASEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 6

---

# MIDASEC01-BP01 Create a security Shared Responsibility Model

Define and document a customized Shared Responsibility Model (SRM) that explicitly
separates the security responsibilities between cloud environment, IT, and OT stakeholders.
This provides clarity when managing security across cloud, edge, and on-premises industrial
assets.

**Desired outcome:** Manufacturing stakeholders understand
their distinct responsibilities in securing the infrastructure, data, and workloads across the
IT/OT boundary.

**Benefits of establishing this best practice:** Reduces
ambiguity during audits and incidents, strengthens collaboration across IT/OT, and supports
secure innovation by clarifying boundaries of responsibility.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use the AWS Shared Responsibility Model as a foundation, then extend it to cover the
specific roles and responsibilities across your IT and OT teams.

### Implementation steps

- Review the AWS Shared Responsibility Model and corresponding manufacturing
standards (for example, IEC 62443).
- Identify and document key security ownership across cloud, edge, and on-premises
systems.
- Collaborate with IT, OT, and third-party vendors to define shared controls and
data ownership boundaries.
- Incorporate the SRM into onboarding and compliance training for manufacturing
teams.

## Resources

**Related documents:**

[Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

[AWS Security Foundations](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/security-foundations.html)

[Amazon
IoT](https://aws.amazon.com/iot/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp01.html*

---

# MIDASEC01-BP02 Standardize security baseline and implement role-based access controls

Establish a standardized security configuration across accounts and workloads using AWS Organizations, AWS IAM, and control policies. Implement role-based access controls (RBAC) to
limit access based on job function and responsibility, especially across IT and OT
environments.

**Desired outcome:**Establish consistent security controls
across industrial cloud workloads that help protect both IT systems (MES, ERP) and OT systems
(PLCs, SCADA), reducing exposure to unauthorized access and privilege escalation that could
impact manufacturing operations.

**Benefits of establishing this best practice:**Enables
centralized governance across IT and OT environments, improves auditability of manufacturing
system access, and minimizes risk of misconfigurations through role-based controls aligned
with production requirements.

**Level of risk exposed if this best practice is not
established:** High

## Implementation steps

- Define roles and responsibilities across IT and OT personas (for example,
automation engineers, data scientists, or vendors).
- Create and assign IAM roles and policies aligned to job responsibilities.
- Use AWS IAM Identity Center for central identity management and federated access.
- Apply SCPs to enforce service-level restrictions at the organizational unit (OU)
level.

## Resources

**Related documents:**

- [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp02.html*

---

# MIDASEC01-BP03 Secure machine-to-machine and human-to-machine access

Help protect communication between devices and systems in industrial settings by securing
machine-to-machine (M2M) and human-to-machine (H2M) access using authentication,
authorization, and encryption methods tailored to industrial protocols and devices.

**Desired outcome:** Avoid unauthorized access to industrial
devices and trace actions across automation systems.

**Benefits of establishing this best practice:** Reduces the
scope of impact, improves system integrity, and provides operational visibility for audit and
compliance.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use X.509 certificates for M2M identity, IoT policies for access control, and managed
bastion solutions like AWS Systems Manager Session Manager for H2M.

### Implementation steps

- Provision devices with unique X.509 certificates using AWS IoT Core.
- Define and enforce AWS IoT policies for device communication.
- Use AWS Systems Manager Session Manager for secure remote access to edge and OT
assets.
- Monitor access using AWS CloudTrail and AWS IoT Device Defender.

## Resources

**Related documents:**

[Iot Security Best Practices](https://docs.aws.amazon.com/iot/latest/developerguide/iot-security-best-practices.html)

[Session Manager Userguide](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp03.html*

---

# MIDASEC01-BP04 Automate monitoring and reporting with cloud-ready compliance tools

Automate the collection, evaluation, and reporting of compliance evidence using AWS Cloud
tools. Tailor configurations to meet industry-specific regulatory requirements such as NIST,
CMMC, or ISO and IEC standards for manufacturing.

**Desired outcome:** Ongoing compliance posture monitoring and
reduced manual effort in security and audit processes.

**Benefits of establishing this best practice:** Improves audit
readiness, reduces cost and error in manual compliance efforts, and verifies continuous
governance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish manufacturing compliance baselines by documenting the required controls for
industrial systems and mapping them to technical implementations.

Then, implement automated monitoring that evaluates industrial system configurations,
tracks security control changes, and validates compliance with manufacturing standards.

Use AWS Config, Security Hub CSPM, and Audit Manager, configured specifically for
manufacturing environments, to continuously monitor both IT and OT systems while maintaining
required compliance evidence.

### Implementation steps

- Enable AWS Config across all Regions and accounts.
- Use AWS Security Hub CSPM to aggregate security findings.
- Map controls in AWS Audit Manager to your industry framework.
- Schedule automated compliance report generation and alerting.

## Resources

**Related documents:**

- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/what-is-aws-config.html)
- [What is AWS Security Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [What is AWS Audit Manager?](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp04.html*

---

# MIDASEC01-BP05 Implement incident response playbooks

Develop and test incident response playbooks for common OT/IT scenarios such as device
compromise, unauthorized access, and data exfiltration. Verify your cross-functional
coordination and readiness to minimize downtime and safety risks.

**Desired outcome:** Manufacturing organizations respond to
incidents swiftly with predefined procedures, minimizing production disruption.

**Benefits of establishing this best practice:** Improves MTTD
and MTTR, reduces risk of safety events, and improves regulatory and audit outcomes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS Systems Manager, AWS Lambda, and Amazon EventBridge to automate containment and
response. Simulate scenarios to validate readiness.

### Implementation steps

- Identify critical incident types and build corresponding playbooks.
- Use AWS Systems Manager Automation to orchestrate predefined remediation.
- Run chaos experiments using AWS Fault Injection Service to test response
efficacy.
- Train IT and OT teams on roles and escalation procedures.

## Resources

**Related documents:**

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp05.html*

---

# MIDASEC01-BP06 Establish a communication protocol between IT and OT systems

Define secure communication and data exchange methods between IT and OT environments. Use
edge services to control and monitor flows across the boundary and verify that only authorized
systems interact.

**Desired outcome:** Reduced risk of unintended system access
and data leakage between IT and OT, while enabling secure data-driven operations.

**Benefits of establishing this best practice:** Promotes
security-by-design, improves clarity in responsibility demarcation, and supports long-term
scalability and digital transformation.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Establish secure communication patterns between IT and OT networks by defining allowed
protocols, data flows, and security controls.

Implement edge processing capabilities to manage data exchange, using protocol gateways
for format translation and security enforcement.

Monitor all cross-boundary communications and implement automated alerts for
unauthorized access attempts. This can be achieved using AWS IoT Greengrass and AWS IoT SiteWise for edge management, but the key is maintaining clear security boundaries while
enabling necessary operational data flows.

### Implementation steps

- Use AWS IoT Greengrass to manage and secure data ingestion at the edge.
- Define and monitor edge-to-cloud traffic patterns.
- Use VPC endpoints and private connectivity where needed for isolation.
- Document IT and OT interfaces, protocols, and access policies.

## Resources

**Related documents:**

- [What is AWS IoT Greengrass?](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-aws-iot-greengrass.html)
- [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iotsitewise/latest/userguide/what-is-sitewise.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec01-bp06.html*

---
