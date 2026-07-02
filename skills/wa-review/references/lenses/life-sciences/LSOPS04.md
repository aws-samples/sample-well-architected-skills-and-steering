# LSOPS04 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# LSOPS04-BP01 Establish IT quality oversight

It is important to distinguish between IT and product quality. A
dedicated IT quality management team (separate from pharma quality)
should define control objectives and provide quality oversight. They
will act as a liaison to product quality and determine which
additional IT controls are required and which IT records can be used
as evidence of computer systems assurance.

**Desired outcome:**

- Clear separation of IT quality and product quality functions
with defined responsibilities.
- Comprehensive documentation system providing evidence of IT
systems adherence.
- Established processes for qualifying and validating IT systems
supporting GxP-regulated activities.

**Common anti-patterns:**

- Forcing GxP process validation and product quality concepts onto
IT, negatively impacting process efficiency, instead of using IT
industry best practices and quality controls.

**Benefits of establishing this best
practice:**

- Enhanced adherence to GxP regulations through proper IT system
verification.
- Greater process efficiency and delivery cadence.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

An IT quality management team must operate independently while
maintaining strong collaboration with product quality teams. This
team develops frameworks for GxP-relevant system classification,
establishes validation strategies, and implements risk-based IT
system validation approaches. The quality oversight function
focuses on system quality, data integrity and traceability while
using AWS services for audit monitoring, documentation control,
and audit trails. Success depends on balancing regulatory
adherence with operational efficiency through risk-based controls
and clear communication channels.

### Implementation steps

- Create a team structure with clear reporting lines, assign
qualified personnel, and develop the IT quality manual that
defines roles, responsibilities, and core quality processes.
- Create control objectives and SOPs aligned with GxP
requirements, establish validation procedures, and implement
a risk assessment framework with defined quality metrics.
- Implement audit monitoring tools, documentation management
systems, and audit trail mechanisms while establishing
validated testing environments.
- Conduct comprehensive GxP and IT quality procedure training,
establish escalation protocols, and maintain training
records demonstrating staff competency.

## Resources

**Related documents:**

- [Quality
assurance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/quality-assurance.html)
- [Don't
Blame Regulators: How Software Excellence Satisfies
Compliance](https://aws.amazon.com/blogs/enterprise-strategy/stop-blaming-regulations-how-software-excellence-satisfies-compliance/)
- [What
is Code Quality?](https://aws.amazon.com/what-is/code-quality/)

**Related examples:**

- [The
future of quality assurance: Shift-left testing with QyrusAI
and Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/the-future-of-quality-assurance-shift-left-testing-with-qyrusai-and-amazon-bedrock/)
- [Beyond
compute: Shifting vulnerability detection left with Amazon Inspector code security capabilities](https://aws.amazon.com/blogs/security/shifting-vulnerability-detection-left-with-amazon-inspector-code-security-capabilities/)
- [Developing
an Service Catalog self-managed engine for
governance](https://aws.amazon.com/blogs/mt/developing-an-aws-service-catalog-self-managed-engine-for-governance/)

**Related tools:**

- [AWS Config](https://aws.amazon.com/config/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops04-bp01.html*

---

# LSOPS04-BP02 Enforce controls in IT tooling and automation

Implement quality controls and automation in the standard IT
tooling used by the development teams whenever possible to enable
continuous validation.

**Desired outcome:**

- Automated enforcement of quality and regulatory controls within
development workflows.
- Reduced manual oversight burden while maintaining regulatory
adherence.
- Early detection of regulatory issues during the development
process.

**Common anti-patterns:**

- Relying primarily on manual reviews and approvals for
verification.
- Inconsistent application of controls across different teams or
environments.
- Adding audit checks only at the end of development cycles.

**Benefits of establishing this best
practice:**

- Increased development velocity through automated audit
verification.
- Improved quality through consistent application of controls.
- Greater scalability of processes across growing organizations.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Identify key control points in your development and operational
processes where automated verification can replace manual checks.
Implement infrastructure as code templates with pre-validated
configurations, automated testing for regulatory requirements, and
continuous monitoring for drift from approved baselines. These
automated controls should generate appropriate evidence for audit
purposes while remaining transparent to developers.

Consider an automated approach where you translate regulatory
requirements into automated tests and policies. This allows teams
to validate adherence continuously throughout the development
lifecycle rather than as a separate activity. When properly
implemented, automated controls can provide greater assurance than
manual processes while reducing the compliance burden on teams.

### Implementation steps

- Identify key control points in development and operational
workflows:

- Use AWS Glue Data Quality for data pipelines.

- Integrate automated testing into CI/CD pipelines:

- Use AWS CodePipeline with validation gates.
- Use AWS CodeBuild for running automated tests.

- Deploy continuous monitoring solutions for configuration
drift:

- Use AWS Config Rules to detect non-compliant resources.
- Use Amazon EventBridge for automated remediation of issues.

## Resources

**Related documents:**

- [Compliance
and Auditing](https://aws.amazon.com/cloudops/compliance-and-auditing/)

**Related examples:**

- [Measure
performance of AWS Glue Data Quality for ETL pipelines](https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/)

**Related tools:**

- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [AWS CodeBuild](https://aws.amazon.com/codebuild/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops04-bp02.html*

---

# LSOPS04-BP03 Incorporate formal risk management into your IT processes

Risk assessments should be conducted to identify potential
vulnerabilities in electronic systems and data management processes.
It is a crucial component of effective quality management. It
involves proactively identifying, analyzing, and mitigating
potential risks that could impact the quality of products or
services. By integrating risk management into the quality management
process, organizations can improve their overall quality, reduce
costs, and enhance customer satisfaction.

**Desired outcome:**

- Systematic identification and assessment of IT risks across the
organization.
- Risk-based decision making for IT investments and control
implementation.
- Documented evidence of risk assessment and treatment for
regulatory purposes.

**Common anti-patterns:**

- Using generic risk templates without tailoring to specific life
sciences requirements.
- Lacking formal methodology for risk prioritization and
acceptance criteria.

**Benefits of establishing this best
practice:**

- Improved business continuity through proactive risk
identification.
- Greater stakeholder confidence in IT system reliability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implement a formal risk management framework that aligns with
industry standards such as ICH Q9 Quality Risk Management while
using cloud capabilities for automation and real-time monitoring.
Cloud-based tools can identify risks across your infrastructure,
evaluate control effectiveness, and track mitigation activities.
Integrate risk assessments into deployment pipelines, and evaluate
new systems and changes before implementation. Centralized risk
repositories provide visibility across the organization, enabling
consistent risk evaluation and prioritization.

When implementing risk management processes, organizations should
balance comprehensive risk coverage with operational efficiency.
While thorough risk assessment is essential for regulated systems,
excessive documentation can create unnecessary overhead. Focus on
identifying and addressing meaningful risks that could impact
product quality, patient safety, or regulatory adherence. Verify
that your risk management approach accommodates both traditional
and cloud-based architectures to provide consistent coverage
across hybrid environments.

### Implementation steps

- Define a formal risk management methodology aligned with
life sciences requirements:

- Use AWS Audit Manager for creating custom risk assessment
frameworks.
- Use AWS Security Hub CSPM for centralized visibility of security
risks.

- Establish risk assessment templates and scoring criteria for
IT systems:

- Store templates in AWS Systems Manager Documents for
consistent application.
- Consider Service Catalog for standardized risk
assessment processes.

- Conduct baseline risk assessments for GxP-relevant systems:

- Use AWS Config for identifying resource configurations that
may pose risks.
- Consider Amazon Inspector for automated vulnerability
assessments.
- Use AWS IAM Access Analyzer to provide visibility needed to
proactively manage permissions.

- Implement risk mitigation strategies with clear ownership
and timelines:

- Use AWS Systems Manager OpsCenter for tracking risk
remediation activities.
- Consider AWS Organizations for implementing preventive
controls at scale.

- Integrate risk reviews into change management processes:

- Implement AWS Systems Manager Change Manager with risk
assessment gates.
- Consider AWS CodePipeline for automated risk evaluations
during deployments.

- Establish continuous risk monitoring mechanisms:

- Configure Amazon CloudWatch for monitoring risk indicators.
- Consider AWS Security Hub CSPM for aggregating security findings
across services.

## Resources

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)
- [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)
- [AWS Organizations](https://aws.amazon.com/organizations/)
- [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Service Management Connector](https://aws.amazon.com/service-management-connector/)
- [AWS IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops04-bp03.html*

---
