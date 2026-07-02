# Operational excellence

**Pages**: 7

---

# Design principles

There are a number of principles that drive operational
excellence in the cloud. Within healthcare, compliance is often
a key consideration:

- **Develop a hub-and-spoke model for
compliance controls:** Many healthcare customers
are subject to regulatory requirements. Mapping to a central
control framework, such as the National Institute of
Standards and Technology (NIST) or HITRUST, simplifies
mapping to multiple regulations in a hub-and-spoke model.
- **Align software and infrastructure
development with applicable quality frameworks:**
Align development processes and tools with the quality
frameworks that apply to your workload, such as ISO 13485
and ISO 14971.
- **Take advantage of AWS fully managed
services and approved third-party solutions:**
Leverage managed cloud services and third-party solutions
approved by your business criteria to simplify meeting
regulatory requirements and maintaining a strong security
posture. Managed cloud services also simplify the operations
of managing your workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/design-principles.html*

---

# Organization

There are no operational excellence best practices for Organization specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/organization.html*

---

# Prepare

HCL_OPS1. Have you defined a formal risk management program?

**Create and document a risk management program**

Many regulatory frameworks are intended to reduce risk in one
way or another. Organizations usually understand that they
must reduce their risk, but may struggle to determine what the
appropriate risk appetite is and how to manage it. This is
accomplished using a documented risk management program.

In healthcare, the risk management program is designed to
safeguard patient data, as well as the overall organization’s
assets and reputation.  For example, a healthcare provider’s
risk management program also covers clinical quality, which is
critical to reducing potential patient risk.  Healthcare
organizations should create a comprehensive risk management
program that includes all operational, clinical, strategic,
financial, legal, environmental, and any other potential risk
domains.

When designing your risk management program, ask questions
similar to the following:

- Have you defined risk and compliance roles for the cloud?
- Have you created a risk management program for the cloud?
- Have you assessed your workload against regulatory needs?
- Have you performed a security risk assessment?
- Have you created a cloud governance program?
- Have you created a responsibility model?

**Create a risk authority
team**

Creating an effective risk management program for the cloud
should be defined by the appropriate risk authority team.  The
risk authority within the organization (for example, board of
directors, chief risk officers, or business risk officers)
must evaluate the criticality of a business process (and the
underlying workloads that support that process) and specify
the level of availability they require for the process.
Consider the potential impact a disruption may have on the
process, organization, and customers. Weigh the impact against
the cost of operating the workload in a high availability
mode, consequences for business agility, and pace of
innovation. Working backwards from established risk appetites
allows you to define operational priorities and corresponding
cloud architectures that can meet your business objectives.

AWS publishes the [Amazon Web Services: Risk and Compliance whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html) that outlines
the mechanisms used to manage risk on the
AWS side of the shared responsibility model. This whitepaper
also provides tools that customers can use to ensure these
mechanisms are being implemented effectively.

HCL_OPS2. What policies and
procedures has your organization adopted for cloud
governance?

**Create policies and
procedures to govern cloud workloads**

Cloud governance is a set of policies and procedures that
outline, or govern, how an organization manages their cloud
workloads.  A mature governance program requires understanding
the compliance objectives and requirements and establishing a
control environment that meets those objectives and
requirements.  Organizations that host and process healthcare
data can be required to meet specific standards and
regulations, such as HIPAA or General Data
Protection Regulation (GDPR). A mature governance
program can help verify that the necessary controls are
implemented.

As outlined in the
[Amazon Web Services: Risk and Compliance
whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html), AWS customers are responsible for maintaining adequate governance
over their entire IT control environment, regardless of how or
where IT is deployed. Recommended practices include:

- Understanding the required compliance objectives and
requirements (from relevant sources)
- Establishing a control environment that meets those
objectives and requirements
- Understanding the validation required based on the
organization’s risk tolerance and applicable regulatory
requirements
- Verifying the operating effectiveness of their control
environment

Cloud deployments give organizations different options to
apply various types of controls and various verification
methods.

Strong customer compliance and governance on AWS should
include the following:

- Reviewing the
[AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/),
[AWS security documentation](https://docs.aws.amazon.com/security/),
[AWS compliance reports](https://aws.amazon.com/artifact/?nc2=h_ql_prod_se_ar), and other information available
from AWS, together with other customer-specific
documentation. Try to understand as much of the entire IT
environment as possible, and document all compliance
requirements into a comprehensive cloud control framework.
- Designing and implementing control objectives to meet the
enterprise compliance requirements as laid out in the
[AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).
- Identifying and documenting controls owned by outside
parties.
- Verifying that all control objectives are met and all key
controls are designed and working.

Approaching compliance governance this way helps you better
understanding you control environment. It can also delineate
the verification activities that must be performed.

HCL_OPS3. How do you map security
controls to compliance requirements?

**Determine regulatory
frameworks and security controls that are applicable to your
business and your cloud workload**

Organizations that host and process health data must verify
that they are adhering to all applicable regulatory frameworks
and standards. As healthcare organizations evolve and grow,
they may either want, or be required, to adhere to multiple
regulations or certifications. For example, a European
organization may be required to meet GDPR and additional country-specific
regulations in each country it operates in.

**Map applicable frameworks
and controls to AWS controls to align with regulatory
frameworks**

There are two common approaches to addressing multiple
compliance regimes. First, organizations may choose to address
each set of requirements from the beginning and develop
mappings unique to each. Alternatively, organizations can
choose to map to a common security framework, and leverage
published controls mappings from that framework to many
others in a hub-and-spoke model. AWS recommends the latter
approach where possible to avoid duplicating effort.

As an example, here are steps you might take if you use NIST
800-53 as your security framework, and apply it to the HIPAA
Security Rule on AWS:

- Map NIST 800-53 to applicability within the AWS
environment, considering the shared responsibility model
with AWS and any third parties you may work with.
- Use prebuilt AWS compliance checks for NIST or other
frameworks with AWS config conformance packs, as well as
implement any additional custom checks to monitor your AWS
environments. Implement immutable logging to archive
compliance posture over time.
- Use NIST Special Publication 800-66 to map controls from
NIST 800-53 to the HIPAA Security Rule

In other words, create a crosswalk to map your AWS controls to
a common security control framework. Use this crosswalk to
connect controls in your cloud environment to the regulation
standards as required.

Another example is to create a
[responsibility
assignment matrix](https://en.wikipedia.org/wiki/Responsibility_assignment_matrix)
(RACI) that designates roles who are responsible, accountable,
consulted, and informed for regulatory controls. A policy with
a RACI matrix clarifies accountability and helps affirm
that proper actions are taken by designated owners. A
consulted party offers guidance related to the control.
Finally, the informed party is made aware of the situation and
any actions taken. Using RACI matrices can help organizations
properly implement plans and procedures when dealing with
regulatory controls.

HCL_OPS4. How do you educate
employees on access to sensitive data?

**Ensure employees who may
have access to sensitive healthcare data are trained on the
rules and regulations**

Organizations that host or process PHI should ensure that
employees who have access to healthcare data, either
intentionally or accidentally as part of their job function,
are trained on the rules and regulations that govern the
organization. Employees should have knowledge on what to do
when viewing sensitive data. They should know how and where to
host or process that data, and how to protect it. Train
employees on any other regulation-based requirements, such as
breach disclosure. Document all of this in your risk
management program.

**Create and document a
policy and procedure aligned to each control and
safeguard**

Organizations that are hosting and processing sensitive
healthcare data should have a documented policy that aligns
with each control or safeguard in place to secure the data. In
addition, each policy should have an associated procedure
document that outlines how the policy will be implemented.
These policy and procedure documents will help educate
employees on the safeguards used, and can help demonstrate
your compliance posture to your stakeholders. These documents
help create a stronger culture of compliance for your
organization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/prepare.html*

---

# Operate

HCL_OPS5. How do you demonstrate
continuous compliance?

**Partition workloads
involving sensitive data into separate
environments**

Minimize access to sensitive data by isolating workloads to
separate environments requiring additional controls for
access. Segmenting can be done by AWS accounts, VPCs, or Amazon Simple Storage Service buckets. Minimize
using sensitive data in non-production environments.

**Architect and build with
the ability to generate evidence that demonstrate continuous
compliance**

Healthcare organizations must be able to demonstrate their
compliance posture.  Evidence that includes the safeguards
used to protect sensitive healthcare data, as well as the
documented policies and procedures, can all be used to
demonstrate compliance. The cloud services used to architect a
compliant foundation in the cloud, can also be used to gather
the necessary evidence to demonstrate compliance posture. For
example, using infrastructure as code, coupled with a software
development lifecycle, can demonstrate a mature change
management process, which is an important compliance control.
Being able to demonstrate the full scope of a compliance
posture is critical for all stakeholders, whether that is an
organizations leadership, shareholders, customers, and
patients.

There are several key concepts to consider when building out a
continuous compliance posture. While AWS cannot assure
compliance for your environment per the shared responsibility
model, the following approach will make it easier for your
organization to demonstrate compliance on AWS. In general, use
managed services from AWS or third-party solutions, such as
those available in AWS Marketplace, to simplify your approach.

**Identify resources in
the cloud environment**

An accurate representation of your cloud environments is
necessary to demonstrate continuous compliance. Understand
what AWS resources exist and how they interact with each
other. AWS Config will help you identify these resources and
how they are configured. Use distributed tracing solutions,
such as AWS X-Ray, to understand how components of your system
interact, and to map network accessibility between different
resources in your environment.

**Restrict resources and
applications to pre-defined configurations**

Coupling AWS Config with infrastructure as code will allow you
to test application configurations before they are deployed in
your environment. Apply governance to your AWS deployments
using infrastructure as code tools like AWS CloudFormation,
AWS Cloud Development Kit (AWS CDK), Terraform, and Service Catalog. Verify that all configurations are
*secure-by-default* with best practices
around encryption, logging, and least privilege.

**Implement
compliance-as-code for configuration**

For each configuration you specify, test the controls you put
in place. Use AWS Config as the central location to evaluate
configuration changes. Where possible, use AWS Config managed
rules, but also implement custom evaluations with AWS Lambda,
fully capturing environment configuration. Configuration
triggers will also shorten the time to identify AWS resources
that are out of compliance compared to periodic triggers. This
helps you demonstrate your compliance posture by automatically
building and maintaining a list of resources within your AWS
environment. It also allows you to continuously evaluate your
compliance posture against the technical controls identified
by your organization. For example, you can create an AWS Config rule that marks an Amazon S3 bucket as non-compliant if
server-side encryption is not enabled or the Amazon S3 bucket
policy allows unencrypted uploads. AWS provides
[sample
rules bundled into conformance packs](https://docs.aws.amazon.com/config/latest/developerguide/conformancepack-sample-templates.html) that align with
many common regulatory frameworks and best practices, allowing
you to start creating a compliance monitoring solution.

**Centralize security and
compliance findings**

Many customers will use multiple AWS accounts (such as
development, test, and prod, or department-specific accounts).
Configuration management, while important, is not the only set
of technical controls you may require. For example, you may
combine your configuration posture with additional findings,
from third-party solutions or AWS security services like
Amazon GuardDuty. Technical controls and findings should be
grouped together as evidence using a solution such as AWS Security Hub CSPM.

**Map technical controls
to compliance requirements using automation.**

Simplify maintaining a complete view of your compliance
posture by automatically mapping controls and findings to your
internal policies. For example, if you have a compliance
policy around encryption at-rest, you may have individual
controls on the configuration of each AWS resource to verify
encryption is enabled.

AWS Audit Manager helps automate evidence collection from a
variety of sources within AWS, including Security Hub CSPM and
Config. Bundling multiple pieces of evidence together under a
single policy makes it easier to demonstrate compliance with a
specific framework or regulation. You can use Audit Manager’s
prebuilt frameworks, and you can manually specify a list of
controls and policies that are important to your organization.

**Use up-to-date
artifacts.**

The creation of artifacts that document the compliance posture
of a cloud environment should be automated. Use services such
as AWS Config, AWS Audit Manager, and AWS Security Hub CSPM to
automatically collect and report the compliance state of a
cloud environment.

HCL_OPS6. How do you automate
remediation of compliance violations?

There are several key concepts to consider when creating an
automated remediation solution. While your organization is
responsible for compliance for your environment, per the
shared responsibility model, the following approach will make
it easier to demonstrate compliance on AWS. In general, use
managed services either from AWS or a third-party solution,
such as one available in AWS Marketplace, to simplify your
approach.  Similar to the recommendations for demonstrating
continuous compliance, define compliance requirements and
create associated policies and procedures for remediation
before creating the remediation solution.

**Automate remediation
actions for non-compliant resources**

Automate remediation of configurations that are out of
compliance with your technical controls for rapid, consistent
application of your policies. Event-driven architectures
improve remediation times. Not everything can be predicted
ahead of time. Certain remediations may be manual at first,
but investigated when they occur and automated when possible
in future occurrences.

In developing automated remediations, there are several steps
you can follow:

- **Specify controls:** Define the evidence and
configuration you want to track. Use AWS Config and Security Hub CSPM to identify and surface
findings.
- **Identify when configuration changes happen:** Use AWS
services that support event-driven architectures for identification. For example,
AWS Config can monitor resource changes and Amazon EventBridge can serve as an event bus for
additional resource changes.
- **Implement remediation:** Services such as AWS Lambda and
AWS Systems Manager can implement configuration changes.
- **Rerun evaluation:** Verify remediation was implemented
and the environment is back in compliance.

For example, you can create an AWS Config rule that marks an Amazon S3 bucket as non-compliant if the server-side encryption is not enabled.
That rule can invoke a corresponding remediation Lambda function that configures server-side encryption on the bucket, bringing the bucket to a compliant state.
For more information, refer to [Remediating Noncompliant AWS Resources by AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html).
AWS also provides sample AWS Config rules with remediation actions for [Amazon DynamoDB](https://docs.aws.amazon.com/config/latest/developerguide/templateswithremediation.html)
and [Amazon S3](https://docs.aws.amazon.com/config/latest/developerguide/templateswithremediation.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/operate.html*

---

# Evolve

There are no operational excellence best practices for Evolve specific to the Healthcare Industry Lens.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/evolve.html*

---

# Key AWS services

[AWS CloudFormation](https://aws.amazon.com/cloudformation/),
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and
[AWS Config](https://aws.amazon.com/config/) comprise three services that can drive operational
excellence. AWS CloudFormation can be used to create
infrastructure templates based on best practices, and provision
resources in an orderly and repeatable fashion. Amazon CloudWatch can be used for monitoring metrics, collecting logs,
generating alerts, and triggering responses.  AWS Config can
assess, audit, and evaluate the configurations within AWS
environments and trigger remediations when necessary. Following
from the
[Shared
Security Model](https://aws.amazon.com/compliance/shared-responsibility-model/), it is critically important to properly
configure cloud services. Configuration guidance can be
found in the [Architecting
for HIPAA Security and Compliance on Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/introduction.html) whitepaper.

Other services and features that support the three areas of
operational excellence are as follows:

**Prepare:**

- [AWS CDK](https://aws.amazon.com/cdk/)
- [AWS Control Tower](https://aws.amazon.com/controltower)
- [AWS Organizations](https://aws.amazon.com/organizations/)

**Operate:**

- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)
- [Service Catalog](https://aws.amazon.com/servicecatalog/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager)
- [AWS X-Ray](https://aws.amazon.com/xray/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)

**Evolve:**

- [Amazon CodeGuru](https://aws.amazon.com/codeguru/)
- [AWS Network Firewall](https://aws.amazon.com/network-firewall/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [Amazon Detective](https://aws.amazon.com/detective/)
- [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/key-aws-services.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to operational excellence.

**Videos**

- [AWS re:Invent 2021 - Cloud compliance, assurance, and
auditing](https://www.youtube.com/watch?v=pdrYGVgb08Y)
- [Enforce
compliance with AWS Config](https://www.youtube.com/watch?v=X_fznJtSyV8)

**Documentation and blogs**

- [Amazon Web Services: Compliance Resources](https://aws.amazon.com/compliance/resources/)
- [Healthcare
compliance in the cloud](https://aws.amazon.com/health/healthcare-compliance/)
- [Remediate
noncompliant AWS Config rules with AWS Systems Manager
automation runbooks](https://aws.amazon.com/blogs/mt/remediate-noncompliant-aws-config-rules-with-aws-systems-manager-automation-runbooks/)

**Whitepapers**

- Amazon Web Services:
[Risk
and Compliance](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/resources.html*

---
