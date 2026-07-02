# MIDAOPS01 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# MIDAOPS01-BP01 Implement a process to periodically review compliance requirements relevant to your industrial data infrastructure

Implement a process to periodically review compliance requirements relevant to your
industrial data infrastructure. Regular assessment of compliance requirements is crucial for
manufacturing environments where industrial data is subject to various regulations such as
GDPR, HIPAA, ISO 27001, or industry-specific standards. Establish a systematic review process
to verify ongoing compliance and adapt to changing requirements.

**Desired outcome:** Maintain a clear understanding of
applicable compliance requirements and verify that your industrial data infrastructure remains
compliant through regular assessments and updates. Identify gaps in compliance and implement
necessary changes promptly.

**Benefits of establishing this best practice:** Adopting the
best practice and prescriptive guidance helps you align with industry standards while reducing
the risk of non-compliance penalties and regulatory issue. This enables proactive rather than
reactive compliance management and simplifies auditing processes.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Create a comprehensive compliance review framework for regular assessments,
documentation, and updates to your industrial data infrastructure.

### Implementation steps

- **AWS Config Rule implementation:** Create custom
compliance rules in AWS Config to automatically evaluate your resources against
industry standards. AWS Config maintains a detailed inventory of your AWS resource
configurations and continuously checks for compliance violations.
- **Security Hub CSPM integration:** Enable AWS Security Hub CSPM
with industry-specific security standards (CIS, PCI DSS, HIPAA). Security Hub CSPM
automatically assesses your security status and aggregates alerts across integrated
services.
- **Audit management:** Use AWS Audit Manager to automate
evidence collection and continuously audit your AWS usage. Create assessment templates
mapped to your compliance frameworks and schedule regular assessments.
- **Automated monitoring:** Configure Amazon EventBridge
rules to run Lambda functions for compliance checks. Set up notifications through
Amazon SNS when compliance issues are detected.

## Key AWS services

- [AWS Config](https://aws.amazon.com/config/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/)
- [Amazon Lambda](https://aws.amazon.com/pm/lambda/)

## Resources

**Related documents:**

- [Security Best Practices for Manufacturing OT](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/security-best-practices-for-manufacturing-ot.html)
- [Best practices to respond to security risks across AWS Organizations](https://aws.amazon.com/blogs/mt/best-practices-to-respond-to-security-risks-across-your-aws-organizations/?utm_source=chatgpt.com)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaops01-bp01.html*

---
