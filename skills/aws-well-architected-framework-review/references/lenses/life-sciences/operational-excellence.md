# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 13

---

# LSOPS01 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS01-BP01 Regularly identify and classify applicable regulatory frameworks

Conduct a systematic assessment to identify applicable regulatory
frameworks based on product type assessment, geographic analysis,
data classification, development phase mapping, and risk-based
classification for comprehensive regulatory coverage for your life
sciences workloads. Repeat this process as the project and its
requirements evolve over time.

**Desired outcome:** A comprehensive
regulatory framework map that clearly identifies applicable
regulations, their specific requirements, and how they impact
different aspects of your life sciences project. This enables
informed decision-making and verifies that you don't overlook
regulatory requirements.

**Common anti-patterns:**

- You assume a one-size-fits-all approach to auditing without
accounting for specific regional or other requirements.
- You identify applicable regulatory frameworks as a one-time
activity and assume adherence even as the project evolves.
- You assume the applicable regulatory frameworks have been
identified without regular review to verify.

**Benefits of establishing this best
practice:**

- Provides clear guidance for project stakeholders on regulatory
expectations.
- Identifies required regulatory submissions and approvals.
- Reduces risk of becoming non-compliant over time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

GxP refers to the regulations and guidelines applicable to life
sciences organizations that make food and medical products such as
drugs, medical devices, and medical software applications.
Depending on the location of research and development, governing
bodies may include U.S. Food & Drug Administration
([FDA](https://www.fda.gov/)), European
Medicines Agency
([EMA](https://www.ema.europa.eu/en/homepage)),
or International Council for Harmonisation (ICH) Good Clinical
Practice guideline
([ICH-GCP](https://ich.org/)). In the US,
handling of Personal Health Information (PHI) is governed by
[HIPAA](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html),
in the EU, General Data Protection Regulation
([GDPR](https://gdpr.eu/)). If you are
manufacturing a product, you need to align with Good Manufacturing
Practices
([GMP](https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/norms-and-standards/gmp)).

Review regulations related to your project location and industry.
Consider what type of data you will be handling in your
application, where it is collected, and where it is stored.
Consider if there are data sovereignty or residency requirements
that would determine the Region in which data can be stored or
processed.

### Implementation steps

- Identify relevant regulatory frameworks based on the type of
project and how data is managed, collected, and stored.
- Document the frameworks that apply to your project
and region. Review the resources available from
[AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) to find AWS resources for common
regulatory frameworks.
- Identify requirements that are common across frameworks to
identify necessary checks to satisfy applicable controls.

## Resources

**Related documents:**

- [Don't
Blame Regulators: How Software Excellence Satisfies
Compliance](https://aws.amazon.com/blogs/enterprise-strategy/stop-blaming-regulations-how-software-excellence-satisfies-compliance/)
- [Life
Sciences Compliance in the Cloud](https://aws.amazon.com/health/life-sciences-compliance/)
- [GxP](https://aws.amazon.com/compliance/gxp-part-11-annex-11/)
- [GxP
Systems on AWS](https://d0.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf)

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops01-bp01.html*

---

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

# LSOPS03 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# LSOPS03-BP01 Perform supplier and vendor assessment of each vendor

Establish criteria for the selection and evaluation of suppliers,
and create a plan for the monitoring and re-evaluation of those
suppliers. Assess vendor controls while considering the intended use
of the services and possible risks involved to the system.

**Desired outcome:** Vendors are
established as approved IT suppliers of purchased services.

**Common anti-patterns:**

- Treating AWS as a SaaS provider whose solutions usually directly
support GxP processes, and therefore incorrectly assessing the
risk of using AWS services for to support GxP workloads.
- Asking questions in the supplier questionnaire that are
irrelevant considering the services to be used.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use as much supplier documentation as possible to expedite a
supplier assessment of AWS.

### Implementation steps

- Perform a general market assessment to establish AWS
position in the market and financial stability.
- Collected documentary evidence of the suitability of the AWS
control framework for supporting GxP workload. Establish an
AWS account and download required third-party assessment
reports and certifications from AWS Artifact.
- If there are perceived gaps in the information obtained,
contact your account team to complete a supplier assessment
questionnaire.
- With the downloaded documentary evidence and questionnaire,
perform an analysis and generate a assessment summary with
your conclusions.  Retain this in case of inspection.

## Resources

**Related tools:**

- [AWS Artifact](https://aws.amazon.com/artifact/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops03-bp01.html*

---

# LSOPS03-BP02 Limit available services to improve regulatory adherence

Use infrastructure tooling to allow only services that fit into
required regulatory frameworks.

**Desired outcome:** Only approved
services will be available for use.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Verify components and services used as available to comply with
identified frameworks. Check vendor documentation to confirm that
the products you use are approved at the vendor level.

### Implementation steps

- Identify the available services by referring to
[AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).
- Review audit guides for the available services.
- Setup an AWS Organization to be able to centrally manage
policies and controls.
- Implement service control policies (SCP) limiting access to
only the available services.

## Resources

**Related guides, videos, and
documentation:**

- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
- [What
is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
- [Service
control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Related tools:**

- [AWS Organizations](https://aws.amazon.com/organizations/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops03-bp02.html*

---

# LSOPS03-BP03 Establish clear definitions of responsibilities between you, vendors, and users

A shared responsibility model to clearly delineate responsibilities
between involved parties makes it straightforward to work together.

**Desired outcome:** Have a structure
and expectations in a tool to streamline audits.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Select prepared frameworks when applicable to apply industry
standards.

### Implementation steps

- Review the
[AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) to identify your areas of
responsibility.
- Access
[AWS Artifact](https://aws.amazon.com/artifact/) for audit reports and documentation.
- Deploy AWS Audit Manager framework to create assessment
frameworks aligned with specific life sciences regulations
like FDA, EMA, and ICH-GCP requirements.

## Resources

**Related tools:**

- [AWS Artifact](https://aws.amazon.com/artifact/)
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops03-bp03.html*

---

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

# LSOPS05 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS05-BP01 Enable a configuration management framework

Use a management framework to record resource configurations,
track changes, identify gaps (like defects and issues) and track
resolution of changes.

**Desired outcome:**

- Automated detection of unauthorized or unplanned configuration
changes.
- Centralized visibility into resource dependencies and
relationships.

**Common anti-patterns:**

- Lacking version control for infrastructure configurations.
- Allowing ad-hoc changes without proper documentation or
approval.

**Benefits of establishing this best
practice:**

- Enhanced compliance-alignment through comprehensive
configuration documentation.
- Improved troubleshooting capabilities with complete change
history.
- Faster recovery from incidents through established baseline
restoration.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Build a configuration management system that automatically
discovers and documents resources supporting GxP workloads.
Infrastructure as code enables version control and consistent
deployment, while continuous monitoring detects unauthorized
changes and configuration drift. These capabilities create a
foundation for demonstrating the control required for GxP
adherence while reducing manual overhead.

When implementing resource management for regulated environments,
balance comprehensive tracking with operational efficiency. Focus
on capturing information relevant to regulatory requirements,
including configuration parameters affecting validated
functionality and dependencies between components, while verifying
that your framework accommodates both cloud and on-premises
resources.

### Implementation steps

- Implement automated discovery and inventory management for
IT resources:

- Deploy AWS Config for continuous resource inventory and
configuration tracking.
- Use AWS Systems Manager Inventory for detailed software and
configuration information.

- Establish version-controlled repositories for infrastructure
configurations:

- Use AWS CloudFormation for templated infrastructure
deployment.

- Define formal change management processes for resource
modifications:

- Implement AWS Systems Manager Change Manager for controlled
change processes.
- Consider Service Catalog for standardized resource
provisioning.

- Implement continuous monitoring for configuration drift:

- Configure AWS Config Rules to detect non-compliant
configurations.
- Consider Amazon EventBridge for automated remediation
workflows.

- Create comprehensive system baselines with restoration
capabilities:

- Use AWS Backup for consistent backup and recovery
capabilities.
- Consider AWS Systems Manager Automation for standardized
restoration procedures.

- Document resource relationships and dependencies in a
centralized system:

- Use AWS Resource Groups for logical organization of related
resources.
- Consider AWS Service Management Connector for integration
with existing CMDB systems.

## Resources

**Related examples:**

- [Synchronize
with CMDB](https://docs.aws.amazon.com/en_us/smc/latest/ag/config-sync.html)

**Related tools:**

- [AWS Config](https://aws.amazon.com/config/)
- [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html)
- [AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
- [AWS Service Management Connector](https://aws.amazon.com/service-management-connector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops05-bp01.html*

---

# LSOPS06 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# LSOPS06-BP01 Validate data quality during ingestion

Define data quality measurements and implement checks during
ingestion.

**Desired outcome:** Data is clean
and ready for analysis upon ingestion.

**Benefits of establishing this best
practice:**

- More trusted results.
- Faster output to conclusions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Build data quality checks into data ingestion pipelines.

Plan to isolate erroneous data and have a way to review it as
needed.

### Implementation steps

- Identify expected patterns in received data.
- Build data quality checks in AWS Glue Data Quality.
- Incorporate checks in data pipelines.
- Build processes to catch and isolate erroneous data. Alert
personnel to investigate data errors

## Resources

**Related examples:**

- [Measure
performance of AWS Glue Data Quality for ETL pipelines](https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/)

**Related tools:**

- [AWS Glue](https://aws.amazon.com/glue/)
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops06-bp01.html*

---

# LSOPS06-BP02 Implement data pipeline testing

Create data handling tests including user authentication and
authorization, data collection, and ingestion into later warehouses.
Tests should cover quality in addition to technical requirements.

**Desired outcome:** Data is reliable
and ready for immediate business use. Reports and analytics can be
trusted without manual verification.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Cloud technologies allow for comprehensive test environments that
can replicate entire system architectures and automate complex
test scenarios.

Consider implementing a testing strategy that follows data through
its complete lifecycle, from initial entry through the processing
stages to final storage. Cloud-based environments can replicate
your production architecture, allowing validation of the
integration points and data transformations. Automated testing can
run scenarios that simulate real-world usage patterns, while data
validation tools verify information remains consistent as it moves
through different systems.

When implementing testing, focus on critical data paths that
impact patient safety, product quality, or regulatory adherence.
Consider continuous testing approaches that run core validation
scenarios automatically when changes occur, supplemented by more
comprehensive testing at key milestones.

### Implementation steps

- Map complete data flows across each system component:

- Use AWS X-Ray to trace data paths across distributed
systems.
- Consider AWS AWS Glue Data Catalog for documenting data
structures and relationships.

- Create realistic test environments that replicate production
architecture:

- Implement AWS CloudFormation templates for consistent
environment deployment.
- Consider Service Catalog for standardized test
environment provisioning.

- Develop test scenarios that follow data through complete
processing paths:

- Consider AWS Step Functions for orchestrating complex test
workflows.

- Implement data validation checks at key integration points:

- Use AWS Lambda functions for custom validation logic.
- Consider Amazon EventBridge for coordinating validation
across services.

- Automate testing as part of deployment pipelines:

- Implement AWS CodePipeline for continuous testing
integration:
- Consider AWS CodeBuild for running test suites:

- Monitor data quality metrics throughout test runtime:

- Configure Amazon CloudWatch for tracking data quality
indicators.
- Consider AWS Glue DataBrew for data quality validation.

- Generate comprehensive test reports for regulatory
documentation:

- Store test evidence in Amazon S3 with appropriate retention
policies.
- Consider AWS Systems Manager Automation for standardized
report generation.

## Resources

**Related guides, videos, and
documentation:**

- [How
to test serverless functions and applications](https://docs.aws.amazon.com/lambda/latest/dg/testing-guide.html)
- [OPS05-BP02
Test and validate changes](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_test_val_chg.html)

**Related tools:**

- [AWS X-Ray](https://aws.amazon.com/xray/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops06-bp02.html*

---

# LSOPS07 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# LSOPS07-BP01 Maintain a controlled multi-account environment

Implement standardized account management using templated
environments and automated account provisioning. Establish
organizational guardrails through policies and baseline
configurations. Maintain centralized control over shared services
while providing consistent security across accounts.

**Desired outcome:** Identifiable
resource allocation

**Common anti-patterns:**

- Combining resources into a single account and attempting to
separate it with complex rules.

**Benefits of establishing this best
practice:** Improved security and auditability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement a structured multi-account strategy that separates
workloads based on their regulatory requirements, security needs,
and operational characteristics. Centralized governance mechanisms
can enforce consistent controls across the accounts while allowing
appropriate flexibility for different workload types. Standardized
account provisioning verifies that new environments are created
with baseline controls already in place, while continuous
monitoring verifies ongoing adherence to organizational standards.

When implementing a controlled multi-account environment, balance
centralized governance with workload-specific requirements.
Establish clear guidelines for account structure and
responsibility boundaries, but allow teams appropriate autonomy
within those guardrails. Implement preventive controls for
critical requirements while using detective controls and
remediation for less critical aspects. This approach maintains
appropriate control while enabling innovation and operational
efficiency.

### Implementation steps

- Design a multi-account structure aligned with regulatory
boundaries:

- Implement AWS Organizations for hierarchical account
management.
- Consider AWS Control Tower for standardized account
governance.

- Establish centralized identity and access management:

- Configure AWS IAM Identity Center for centralized user
management.
- Consider AWS IAM Roles for fine-grained permission controls.

- Implement standardized account provisioning processes:

- Use AWS Control Tower Account Factory for consistent account
creation.
- Consider Service Catalog for standardized environment
provisioning.

- Deploy preventive guardrails for critical requirements:

- Configure AWS Organizations Service Control Policies (SCPs)
for preventive controls.
- Consider AWS Control Tower Guardrails for additional
preventive measures.

- Establish baseline configurations across accounts:

- Use AWS CloudFormation StackSets for multi-account resource
deployment.
- Consider AWS Systems Manager for configuration management.

- Implement centralized monitoring and verification:

- Configure AWS Config Aggregators for multi-account
visibility.
- Consider AWS Security Hub CSPM for consolidated security and
monitoring.

## Resources

**Related documents:**

- [Walkthrough:
Automate Account Provisioning in AWS Control Tower by Service
Catalog APIs](https://docs.aws.amazon.com/controltower/latest/userguide/automated-provisioning-walkthrough.html)

**Related examples:**

- [AWS Samples: AWS Control Tower Automate Account Creation](https://github.com/aws-samples/aws-control-tower-automate-account-creation)
- [Automate
account customization using Account Factory Customization in
AWS Control Tower](https://aws.amazon.com/blogs/mt/automate-account-customization-using-account-factory-customization-in-aws-control-tower/)

**Related tools:**

- [AWS Organizations](https://aws.amazon.com/organizations/)
- [AWS Control Tower](https://aws.amazon.com/controltower/)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
- [AWS IAM](https://aws.amazon.com/iam/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Resource
Access Manager](https://aws.amazon.com/ram/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops07-bp01.html*

---

# LSOPS07-BP02 Isolate GxP data from non-GxP data

Take steps to isolate and segment GxP data from non-GxP data. In
conjunction with the recommendations around data discovery and
classification, separate GxP data so the organization can implement
the necessary technical and administrative controls.

**Desired outcome:** Demonstrable
division between GxP and non-GxP data.

**Common anti-patterns:**

- Granting access at a workload level grants access to the data,
GxP and non-GxP.
- Retaining logs that are adjacent to GxP relevant metadata.
- Including GxP data in logs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Incorporate system separation, including table and row-level
access controls.

### Implementation steps

- Foster system separation though architecture design and
deployment.  Create distinct datastores (like Amazon S3 and
Amazon RDS) for GxP data.
- Implement table and row-level access controls through
application logic.
- Apply AWS Lake Formation rules for consistent control to
data sets.
- Produce evidence of verification of access controls.

## Resources

**Related tools:**

- [Amazon RDS](https://aws.amazon.com/rds/)
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [Amazon S3](https://aws.amazon.com/s3/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops07-bp02.html*

---

# LSOPS08 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS08-BP01 Continuously generate and maintain evidence

Use appropriate IT tooling to generate evidence used for regulatory
requirements. Maintain audit trails of the changes, approvals, and
validations. Store the data in an immutable store. Generate reports
as needed from the data. Enable immediate access to evidence during
inspections or audits.

**Desired outcome:** You have a body
of evidence ready for auditors.

**Benefits of establishing this best
practice:** Smoother audit process with less wasted time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start with a clear understanding of what is required, and build
audit readiness practices around those requirements.

### Implementation steps

- Define evidence requirements based on regulatory
obligations:

- Map evidence needs to specific regulations like 21 CFR Part
11, GxP, or HIPAA.
- Consider AWS Audit Manager for creating custom evidence
collection frameworks.

- Implement automated evidence collection mechanisms:

- Configure AWS Config to capture resource configurations and
changes.
- Enable AWS CloudTrail for comprehensive API activity
logging.
- Consider Amazon CloudWatch for operational metrics and logs.

- Establish centralized, secure evidence repositories:

- Use Amazon S3 with appropriate encryption and access
controls.
- Consider S3 Object Lock for immutable evidence storage.
- Implement AWS Backup for evidence protection and retention.

- Create structured evidence organization with metadata:

- Implement Amazon S3 metadata tagging for evidence
classification.
- Consider AWS Glue for cataloging and organizing audit
artifacts.

- Generate reports for audits and inspections:

- Use AWS Audit Manager for automated report generation.
- Consider Quick for audit visualization and
reporting.

- Implement appropriate retention policies for documentation:

- Configure S3 Lifecycle policies for evidence retention.
- Consider AWS Backup for long-term archival of documentation.

## Resources

**Related documents:**

- [Guidance
for Change Management on AWS](https://aws.amazon.com/solutions/guidance/change-management-on-aws/)
- [AWS Systems Manager Change Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html)
- [Logging
AWS Account Management API calls using AWS CloudTrail](https://docs.aws.amazon.com/accounts/latest/reference/monitoring-cloudtrail.html)
- [How
can I secure the files in my Amazon S3 bucket?](https://repost.aws/knowledge-center/secure-s3-resources)

**Related examples:**

- [Streamline
and automate compliance monitoring and reporting with AWS Backup Audit Manager](https://aws.amazon.com/blogs/storage/streamline-and-automate-compliance-monitoring-and-reporting-with-aws-backup-audit-manager/)
- [Leveraging
AWS CloudTrail Insights for Proactive API Monitoring and Cost
Optimization](https://aws.amazon.com/blogs/mt/leveraging-aws-cloudtrail-insights-for-proactive-api-monitoring-and-cost-optimization/)

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Quick](https://aws.amazon.com/quicksight/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops08-bp01.html*

---

# LSOPS09 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS09-BP01 Track data ownership and lineage over the life of the project

Data lineage in life sciences projects involves tracking the origin,
movement, and transformation of data throughout its lifecycle. This
process is important because it provides a clear history of how data
has been collected, processed, and used. Maintaining accurate data
lineage improves data integrity, aids in troubleshooting errors, and
supports regulatory adherence. It also allows researchers and
regulators to understand and trust the data's journey from its
source to final analysis, which is critical for validating research
findings and meeting stringent industry standards.

**Desired outcome:** Have a clear,
auditable history of data lineage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use data sharing and management tooling that includes audit
history of access and changes and allows for granular permissions.

### Implementation steps

- Set up an Amazon DataZone or Amazon SageMaker AI Unified Studio
domain and related projects:

- Create a business domain for life sciences data.
- Configure projects and data catalogs.
- Set up user roles and access controls.

- Enable  automatic lineage tracking:

- Use Amazon DataZone or Amazon SageMaker AI Unified Studio
lineage capabilities.
- Connect to data sources (like Amazon S3 or Amazon RDS).
- Use built-in metadata collection.

- Implement governance:

- Use DataZone or SageMaker AI Unified Studio data sharing
workflows.
- Configure approval processes.
- Set up automatic data classification.

## Resources

**Related documents:**

- [Data
lineage in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-data-lineage.html)
- [Best
practice 4.5 – Track data and database changes](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.5-track-data-and-database-changes..html)

**Related tools:**

- [Amazon
DataZone](https://aws.amazon.com/datazone/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops09-bp01.html*

---

# LSOPS10 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# LSOPS10-BP01 Reproducibility

Build technology products with infrastructure as code so you can
rebuild them if needed. In archive documents, store the structure of
your products. Store data in a format that is simple to archive,
such as Iceberg.

**Desired outcome:** Maintain a
history of changes made in the IT environment and methods to
programmatically create environments when needed.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:** In addition to being ready to close at project
conclusion, this practice eases movement from test to production and
verifies that testing is performed on the exact architecture that
will be deployed. Additionally, it becomes more straightforward to
reproduce the environment in the event that certain components are
needed after project conclusion.

## Implementation guidance

Establish a robust infrastructure as code framework using
industry-standard tools and practices. This foundation fosters
consistent, repeatable deployments while maintaining complete
version control and documentation.

Implement comprehensive documentation practices that automatically
capture infrastructure configurations, dependencies, and changes.
This system should integrate with version control and provide
clear rebuild instructions.

Establish structured change control procedures that maintain
infrastructure stability while enabling necessary updates. This
process should include proper documentation, testing, and approval
workflows.

### Implementation steps

- Create an infrastructure as code foundation:

- Establish version-controlled repository for infrastructure
code and configurations.
- Implement automated CI/CD pipelines for infrastructure
deployment using AWS CodeBuild.
- Create standardized templates for common infrastructure
components. Consider AWS CloudFormation and StackSets.

- Develop a documentation framework:

- Develop comprehensive documentation covering the
infrastructure components.
- Create automated documentation generation for code and
configurations. Consider Amazon Q.

- Implement archive management:

- Implement versioned archive system for infrastructure code.
Amazon S3 Versioning can be used to retain multiple versions
of documents.
- Create automated backup procedures for configuration files
using AWS Backup. Establish a clear tagging system for
archived components.

## Resources

**Related documents::**

- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)

**Related examples:**

- [Generating
documentation with Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-generation.html)

**Related tools:**

- [Amazon Q](https://aws.amazon.com/q/)
- [Amazon S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS CodeBuild](https://aws.amazon.com/codebuild/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) (with drift detection)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops10-bp01.html*

---

# LSOPS10-BP02 Store data in a format that works both for archiving and for active use by retaining related metadata

Select a data format which is queried while the project is ongoing
but archives natively. Iceberg's data format is ideal for life
sciences projects because it stores metadata alongside the data. It
offers advanced data versioning, time travel capabilities, and
schema evolution, essential features for maintaining data lineage
and regulatory adherence while handling large-scale scientific
datasets that frequently change over time.

**Desired outcome:** Have a portable
dataset that contains the data and metadata in a single package

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Verify that the output of data processing results in portable data
formats to allow for simple archiving.

### Implementation steps

- Build standard data pipelines using AWS Glue
- For deep analysis on structured data use Amazon Redshift.
- Build a data lake of the data in Amazon S3 in Iceberg
format.

## Resources

**Related documentsn:**

- [What
is Apache Iceberg?](https://aws.amazon.com/what-is/apache-iceberg/)

**Related examples:**

- [Build
a high-performance quant research platform with Apache
Iceberg](https://aws.amazon.com/blogs/big-data/build-a-high-performance-quant-research-platform-with-apache-iceberg/)

**Related tools:**

- [Modernize
Data Archiving](https://aws.amazon.com/archive/)
- [Amazon S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops10-bp02.html*

---

# LSOPS11 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS11-BP01 Identify clear dataset owners and access history

If you are receiving a dataset, identify who is responsible for data
accuracy and governance and who manages the data lineage during
collection. Depending on the storage method, who is responsible for
securing the data in its different stages?

**Desired outcome:** Have an
automated method of auditing shared data between partners.

**Benefits of establishing this best
practice:** Data can be limited to just what is agreed on.
Secure data can be automatically filtered.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design a collaborative governance framework. Establish unified
governance architecture spanning organizational boundaries. This
foundation enables consistent data policies while respecting each
organization's requirements.

### Implementation steps

- Configure collaborative workflows:

Implement data exchange protocols specific to
organizational relationships.
- Establish shared metadata repositories with
organization-specific views.
- Deploy cross-organizational audit mechanisms.

- Use AWS Clean Rooms to enable granular control and data
sharing without moving data or exposing sensitive
information.

## Resources

**Related documents:**

- [AWS Clean Rooms: Privacy-enhanced collaboration use cases](https://aws.amazon.com/blogs/industries/aws-clean-rooms-privacy-enhanced-collaboration-use-cases/)

**Related examples:**

- [Enable
data collaboration among public health agencies with AWS Clean Rooms – Part 1](https://aws.amazon.com/blogs/big-data/part-1-enable-data-collaboration-among-public-health-agencies-with-aws-clean-rooms/)
- [Automate
AWS Clean Rooms querying and dashboard publishing using AWS Step Functions and Quick – Part 2](https://aws.amazon.com/blogs/big-data/automate-aws-clean-rooms-querying-and-dashboard-publishing-using-aws-step-functions-and-amazon-quicksight-part-2/)

**Related tools:**

- [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops11-bp01.html*

---

# LSOPS12 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS12-BP01 Create a controlled semantic layer

A semantic layer translates complex life sciences data into
understandable business terms, acting as a bridge between raw data
and the scientists who need to use it.

**Desired outcome:** Have a
consistent, well managed semantic layer to allow the data to be
consumed by analysts

**Benefits of establishing this best
practice:** Provides consistency of result definition.
Allows for more straightforward communication with auditors.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use a tool to centralize and implement semantic layer management.

### Implementation steps

- Create an Amazon DataZone or Amazon Sagemaker Unified Studio
domain.
- Use tools to build and manage the semantic layer. Maintain
controlled terminology, business glossaries, and metadata
while verifying that you adhere to regulatory requirements.

## Resources

**Related tools:**

- [Amazon
DataZone](https://aws.amazon.com/datazone/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops12-bp01.html*

---

# LSOPS13 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS13-BP01 Store data in an AI/ML-ready formats

Expectations of what can be done with data are rapidly expanding.
Life sciences projects produce rich data. Work to maximize data
storage to allow for new technologies such as AI/ML.

**Desired outcome:** Be able to pivot
and adapt as there are new technological demands on existing systems
and data.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Use data processing that stores data in adaptable, open standard
formats. This will allow for the greatest flexibility as
technologies progress.

### Implementation steps

- Store data in document formats ingestible by Amazon
Sagemaker and Amazon Bedrock.
- Use AWS Glue to transform data into Iceberg and place in an
Amazon S3 data lake.

## Resources

**Related documents:**

- [Accelerating
Life Sciences Innovation with Agentic AI on AWS](https://aws.amazon.com/blogs/industries/accelerating-life-sciences-innovation-with-agentic-ai-on-aws/)
- [What
is Apache Iceberg?](https://aws.amazon.com/what-is/apache-iceberg/)
- [Building
an End-to-End Data Strategy for Analytics and Generative AI:
Insights from AWS and Workhuman](https://aws.amazon.com/awstv/watch/f4743296958/)

**Related examples:**

- [Use
generative AI on AWS for efficient clinical document
analysis](https://aws.amazon.com/blogs/architecture/use-generative-ai-on-aws-for-efficient-clinical-document-analysis/)
- [Revolutionizing
clinical trials with the power of voice and AI](https://aws.amazon.com/blogs/machine-learning/revolutionizing-clinical-trials-with-the-power-of-voice-and-ai/)

**Related tools:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops13-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
