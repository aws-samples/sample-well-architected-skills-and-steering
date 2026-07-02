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
