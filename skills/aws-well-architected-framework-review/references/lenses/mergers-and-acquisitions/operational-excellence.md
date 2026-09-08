# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 9

---

# MAOPS01 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 6

---

## MAOPS01-BP01 Workloads from both organizations have identified owners

Strong governance and centralized control over scope of migration workloads facilitates
a successful migration. Wide distribution makes migration more difficult (assuming the
migration scope spans these distributed groups).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-1.html*

---

## MAOPS01-BP02 Processes and procedures have identified owners

Understand who has ownership of the definition of individual processes and procedures,
why those specific process and procedures are used, and why that ownership exists. To better
identify improvement opportunities, understand the reasons that specific processes and
procedures are used.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-1.html*

---

## MAOPS01-BP03 Operations activities have identified owners responsible for their performance

Understand who has responsibility to perform specific activities on defined workloads
and why that responsibility exists. Understanding who has responsibility to perform
activities informs who conducts the activity, validates the result, and provides feedback to
the owner of the activity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-1.html*

---

## MAOPS01-BP04 Create a Cloud Center of Excellence team

Understand the responsibilities of your role and how you contribute to business
outcomes, as this knowledge informs the prioritization of your tasks and why your role is
important. This understanding helps team members recognize needs and respond appropriately.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-1.html*

---

## MAOPS01-BP05 Mechanisms exist to request process additions, changes, and exceptions

You are able to make requests to owners of processes, procedures, and resources. Make
informed decisions to approve requests where they have been deemed viable and appropriate
after an evaluation of benefits and risks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-1.html*

---

## MAOPS01-BP06 Both companies have identified the cloud skills and competencies to enable the resources

Identify gaps between required skills and competencies and what is presently available
in the organization. For existing staff, provide access to training courses of different
types (both classroom-based and online courses). Encourage staff to obtain certification on
cloud competencies to validate their knowledge.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-1.html*

---

# MAOPS02 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

## MAOPS02-BP01 Each company has identified their primary Region

For many services, you can choose an AWS Region that specifies where your resources
are managed. Regions are sets of AWS resources located in the same geographical area. You
don't need to choose a Region for the AWS Management Console or for some services, such as AWS Identity and Access Management.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-2.html*

---

## MAOPS02-BP02 Configure AWS Control Tower, AWS Config, and AWS CloudFormation

AWS Control Tower offers the easiest way to set up and govern a secure, multi-account AWS
environment. It establishes a landing zone that is based on best-practices blueprints, and
it enables governance using guardrails you can choose from a pre-packaged list.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-2.html*

---

## MAOPS02-BP03 Automate infrastructure as code (IaC) using Cloud Formation or Terraform

AWS CloudFormation helps you model, provision, and manage AWS and third-party resources by
treating infrastructure as code.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-2.html*

---

## MAOPS02-BP04 Automate resource compliance using tools like AWS Config

AWS Config is a config tool that helps you assess, audit, and evaluate the configurations
and relationships of your resources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-2.html*

---

# MAOPS03 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS03-BP01 Structure your organization following AWS best practices

A well-architected multi-account strategy helps you innovate faster in AWS, while
helping you meet your security and scalability needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP02 Merge the management accounts of both organizations

Consolidated billing is a feature of AWS Organizations. You can use the management account of
your organization to consolidate and pay for all member accounts. In consolidated billing,
management accounts can also access the billing information, account information, and
account activity of member accounts in their organization. This information may be used for
services such as AWS Cost Explorer, which can help management accounts improve their organization’s
cost performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP03 Determine if it's appropriate to separate management accounts

If there is a use case to keep OUs separate, you can certainly do that with multiple
management accounts. There may be few reasons to keep Organizations separate:

- AWS GovCloud (US) or commercial cloud
- Differing financial needs, including taxation (Europe compared to the US)
- Differing operating scope (Systems Manager)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP04 Merge logging, security, and infrastructure organizations

The approach covered in this pattern is suitable for customers who have multiple
AWS accounts with AWS Organizations and are now encountering challenges when using AWS Control Tower, a
landing zone, or account vending machine services to set up baseline guardrails in their
accounts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP05 Define a backup strategy for each organization

Use AWS Backup to create backup plans that define how to back up your AWS resources.
The rules in the plan include a variety of settings, such as backup frequency, the time
window during which the backup occurs, the AWS Region containing the resources to back up,
and the vault in which to store the backup.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

# MAOPS04 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS04-BP01 Standardize documented operational processes (like CI/CD and deployment)

Organizations incur operational tech debt during mergers and acquisitions.
Organizations should remove manual processes and focus on automation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP02 Retire or consolidate redundant apps and data-stores

Perform technical analysis during mergers and acquisitions. Otherwise, data and systems
can be duplicated, or even potentially orphaned. Both organizations should agree on a
consistent data model, consistent accesses, and compliance needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP03 Have a process in place for customer migration (if necessary)

Customer retention and migration is of utmost importance during mergers and
acquisitions. It is critical to support existing customers with optimal costs and negligible
impact. The AWS ISV Workload Migration Program (WMP) supports software partners that have
a SaaS offering on AWS to drive and deliver workload migrations. Use funding, technical
enablement, and go-to-market support to rapidly migrate customers to your SaaS offering.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP04 Understand third-party integrations and dependencies

It might happen that companies merge or multiple platforms get developed over time and
duplicate some of the same needed subsystems. Being service oriented and consolidating
services reduces the amount of code to be maintained.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

## MAOPS04-BP05 Perform all customizations through configuration, and change them as self-serve or company-controlled feature flags

Customizations that are done with configuration do not require a code recompile or
reload. It is a way to get away from the legacy practice of making hard-coded customizations
per individual customers or segments. Use feature flags that are temporary or permanent.
These flags help during testing or canary release.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-4.html*

---

# MAOPS05 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS05-BP01 Configure AWS resource tags

AWS resources can be tagged for a variety of purposes, from implementing a cost
allocation strategy to supporting automation or authorizing access to AWS resources.
Implementing a tagging strategy can be challenging for some organizations, owing to the
number of stakeholder groups involved and considerations such as data sourcing and tag
governance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP02 Group applications based on tags

A tag is a label that you assign to an AWS resource. A tag consists of a key and a
value, both of which you define. For example, if you have two EC2 instances, you might
assign both a tag key of `Stack`. But the value of `Stack` might be
`Testing` for one and `Production` for the other.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP03 Associate tags with each configured resource (during provisioning)

AWS CloudFormation provides a common language for provisioning all the infrastructure resources
in your AWS environment. For AWS resources using CloudFormation templates, you can use the CloudFormation
Resource Tags property to apply tags to supported resource types upon creation. Managing the
tags as well as the resources with IaC helps create consistency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP04 Set up security based on tags

Organizations have varying needs and obligations to meet regarding the appropriate
handling of data storage and processing. Data classification is an important precursor for
several use cases, such as access control, data retention, data analysis, and compliance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP05 Perform cost allocation based on tags

The AWS-generated tag created by is a tag that AWS defines and applies to supported
AWS resources for cost allocation purposes. User-defined tags are tags that you define,
create, and apply to resources. After you have created and applied the user-defined tags,
you can activate by using the AWS Cost Management Console for cost allocation tracking.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

# MAOPS06 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

## MAOPS06-BP01 The seller has an extensive list of all IP and key innovations (and related documentation)

Use industry domain knowledge, as well as patentable and other relevant code
innovations, to create a platform offering that is truly unique and valuable to customers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-6.html*

---

## MAOPS06-BP02 Document open-source software integrations

Continually evolve your underlying code base to build up capabilities that use
open-source software where appropriate.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-6.html*

---

## MAOPS06-BP03 Hold patents on key platform technologies

Patents are a way to secure your rights to innovative technologies that keep you in a
competitive position.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-6.html*

---

# MAOPS07 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS07-BP01 Document duplicate workloads and features

Keep a centralized list of work that could be epic-level ideas down to more detailed
work for features, bugs, technical debt, and innovative advances.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-7.html*

---

## MAOPS07-BP02 Identify the impact of product features on customers from both companies

A company should be looking beyond the current near-term features going in to
strategically plan out longer term initiatives and how they can be ordered to create a
compelling list of innovations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-7.html*

---

## MAOPS07-BP03 Document a combined-products strategy

Identify products to be retired, maintained, or enhanced. Document customer impact and
migration plan in case of product or workload decommission.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-7.html*

---

## MAOPS07-BP04 Verify that teams understand critical customer requirements

Increased decomposition for engineering tasks corresponds to increased probability of
success. You can properly scope the effort in terms of cost, time, and resources needed, and
define a definition for completion of work.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-7.html*

---

## MAOPS07-BP05 Modify your existing roadmap to incorporate the new organization

Define the new product roadmap that aligns with the combined companies’ goals.
Determine customer impact based on product priorities.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-7.html*

---

# MAOPS08 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

## MAOPS08-BP01 Document mechanisms for both product teams to operate collaboratively

Understanding deal rationale (for example, to acquire new capabilities or to capture
market share). It's important for product teams from both companies to work closely to
achieve the unified organization's goals.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-8.html*

---

## MAOPS08-BP02 Verify that key product teams have a post-integration product strategy in place

Ensure product teams from both companies understand combined product strategy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-8.html*

---

## MAOPS08-BP03 Review, retire, and promote products and roadmaps based on customer focus

Product managers speak to customers regularly. The teams collaborate on the analyzed
findings, and experimentation at scale is performed using well-known mechanisms. Manage data
and cloud-enabled offerings that deliver repeatable value to internal and external customers
as products through their lifecycles.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-8.html*

---

# MAOPS09 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## MAOPS09-BP01 Create a Configuration Management Database (CMDB) or infrastructure repository

Implement automated mechanisms to update data and maintain data accuracy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-9.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
