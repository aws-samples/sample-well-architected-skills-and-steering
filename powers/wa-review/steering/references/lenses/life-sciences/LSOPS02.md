# LSOPS02 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# LSOPS02-BP01 Establish a central control framework

Establishing a central control framework and mapping to applicable
frameworks can simplify processes, avoid duplicate effort, and
reduce operational overheads. The IT quality team can define the
required control objectives, while IT process and tooling experts
can determine the best way to implement the controls.

**Desired outcome:**

- Unified control framework that maps to multiple regulatory
requirements.
- Reduced duplication of efforts across different frameworks.
- Streamlined audit processes with centralized evidence
collection.

**Common anti-patterns:**

- You implement separate controls for each framework.
- You lack clear mapping between control objectives and regulatory
requirements.
- You create duplicate controls that are common across frameworks.

**Benefits of establishing this best
practice:**

- Streamlined reporting through consolidated evidence collection.
- Reduced audit preparation time and resource requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a hierarchical structure with clear accountability that
bridges the gap between high-level objectives and specific
technical implementations. This structure should incorporate
risk-based prioritization to focus resources on the most critical
controls while maintaining comprehensive coverage of requirements.

### Implementation steps

- Inventory the applicable regulatory frameworks and
requirements:

- Use AWS Audit Manager to catalog regulatory requirements
across frameworks and collect evidence of auditing.
- Consider AWS Systems Manager Documents for standardized
documentation.

- Create a unified control catalog with clear mapping to
regulatory requirements:

- Implement AWS Systems Manager Parameter Store for
centralized control definitions.
- Consider Service Catalog for managing approved control
implementations that can be deployed to multiple workloads.

- Establish control ownership and responsibilities across
teams:

- Use AWS Resource Access Manager for sharing control
resources across teams.
- Consider AWS Organizations for defining organizational
control responsibilities.

- Develop standardized templates for control documentation and
evidence collection:

- Store templates in Amazon S3 with appropriate access
controls.
- Consider AWS CloudFormation for templating control
implementation patterns.

- Implement continuous monitoring of control effectiveness:

- Configure AWS Config Rules to verify control implementation.
- Consider AWS Security Hub CSPM for aggregating control status.

## Resources

**Related guides, videos, and
documentation:**

- [Don't
Blame Regulators: How Software Excellence Satisfies
Compliance](https://aws.amazon.com/blogs/enterprise-strategy/stop-blaming-regulations-how-software-excellence-satisfies-compliance/)

**Related examples:**

- [Conformance
Pack Sample Templates for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html)
- [Streamline
compliance management with AWS Config custom rules and
conformance packs](https://aws.amazon.com/blogs/mt/streamline-compliance-management-with-aws-config-custom-rules-and-conformance-packs/)

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [AWS Resource
Access Manager](https://aws.amazon.com/ram/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Config](https://aws.amazon.com/config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops02-bp01.html*

---

# LSOPS02-BP02 Implement regulatory reviews

Incorporate and electronically document formal reviews throughout
the project lifecycle to improve regulatory adherence. This includes
initial framework assessment reviews, design control gates, change
management reviews, pre-submission readiness checks, and periodic
audits to verify ongoing adherence. Document the decisions and
maintain traceability of regulatory requirements implementation
throughout each stage.

**Desired outcome:** A systematic,
documented review process that improves regulatory adherence at
every stage of the project lifecycle, with clear evidence of
requirements verification, issue remediation, and approval decisions
that satisfy regulatory expectations.

**Common anti-patterns:**

- Conducting reviews only at project completion rather than
throughout the lifecycle.
- Treating reviews as checkboxes rather than substantive
evaluations.

**Benefits of establishing this best
practice:**

- Early identification and remediation of audit issues.
- Reduced regulatory submission risks.
- Streamlined audit processes.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish a formal review framework with clearly defined stages
aligned to your development lifecycle. Define specific entry and
exit criteria for each review gate, which explicitly addresses
regulatory requirements. Implement electronic documentation
systems that maintain review histories, decisions, and supporting
evidence.

Regulatory reviews should be integrated into your project
lifecycle rather than treated as separate activities. Map key
decision points in your development process where regulatory
reviews provide maximum value. These typically include initial
planning, design completion, pre-implementation,
post-implementation, and pre-submission phases.

Create standardized templates and checklists for each review type
for consistent evaluation. Involve cross-functional teams
including regulatory affairs, quality assurance, technical
experts, and business stakeholders to provide comprehensive
evaluation from multiple perspectives.

### Implementation steps

- Configure AWS Systems Manager Change Calendar with a
DEFAULT_CLOSED entry to block changes
during regulatory review windows.
- Develop AWS Systems Manager Automation documents to automate
approved changes based on review procedures and findings.
- Implement AWS Audit Manager assessments for periodic audit
verification.

## Resources

**Related examples:**

- [Change
Management for Life Sciences](https://aws.amazon.com/blogs/mt/change-management-for-life-sciences/)
- [Automated
Evidence Collection for Life Sciences continuous compliance
solutions using AWS Audit Manager](https://aws.amazon.com/blogs/mt/automated-evidence-collection-for-life-sciences-continuous-compliance-solutions-using-aws-audit-manager/)

**Related tools:**

- [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html)
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops02-bp02.html*

---
