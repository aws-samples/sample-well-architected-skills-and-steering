# Security

**Pillar**: Security  
**Questions**: 2

---

# LSSEC01 — Identity and access management

**Pillar**: Security  
**Best Practices**: 3

---

# LSSEC01-BP01 Implement the principle of separation of duties

For users with increased privileges, it is important to distribute
system administration activities, so no one administrator can hide
their activities or control an entire system. Separation of duties
can mitigate risk on critical tasks by requiring separate requesters
and approvers for a task. A common example is the use of an approver
during the
[running
of an automation on AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html). This principle can
be used to implement numerous tasks including controlling access to
your cloud resources. Use roles with limited permissions based on
functional needs when increased privileges are not required.

**Desired outcome:** Administrative
tasks related to GxP data stores require approvals.

**Common anti-patterns:**

- Failure to implement a least privilege administration model.
- Lack of approvals in administration workflows.

**Benefits of establishing this best
practice:** By implementing a least-privilege model and
separating duties, appropriate control over access to GxP related
resources can be demonstrated.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Determine which administrative tasks may have the potential to
impact GxP data integrity. For each of these tasks, separate task
approval from task execution.

Configure roles with least privilege to be used for routine
functions that do not require administrative permissions.

### Implementation steps

- Introduce approval steps into automated administrative
workflows.
- Set required IAM permissions as needed.

## Resources

**Related best practices:**

- [SEC03-BP02
Grant least privilege access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html)

**Related documents:**

- [Run
an automation that requires approvals](https://docs.aws.amazon.com/systems-manager/latest/userguide/running-automations-require-approvals.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssec01-bp01.html*

---

# LSSEC01-BP02 Maintain a history of IAM configurations and changes over time

By logging the IAM policy that was assigned to an IAM user, group,
or role, you can determine the permissions that belonged to a user
at a specific time. For example, you can view whether a user had
permission to modify settings on a specific date in the past.

**Desired outcome:** A complete
history of IAM configurations is maintained and available for
review.

**Benefits of establishing this best
practice:** Provide the ability to view the IAM policy that
was assigned to an IAM user, group, or role over time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Customize AWS Config to record configuration changes to IAM global
resources in your home Region.

### Implementation steps

- Determine a home AWS Region where you want AWS Config to
record and store configuration changes to IAM resources, as
the same IAM data is available in different AWS Regions.
- In your home region, enable recording
by [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/view-manage-resource.html) and enable recording of global resources or
select specific IAM resources.
- Create a service control policy (SCP) to stop recording
being turned off.

## Resources

**Related documents:**

- [How
to Record and Govern Your IAM Resource Configurations Using
AWS Config](https://aws.amazon.com/blogs/security/how-to-record-and-govern-your-iam-resource-configurations-using-aws-config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssec01-bp02.html*

---

# LSSEC01-BP03 Set up alerts for IAM configuration changes and perform audits

Compliance-related access rules should be automated with alerting or
automated risk mitigation actions.

**Desired outcome:** Ability to
mitigate the risk of irregular access configurations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Set up alerts for monitoring activities by users with increased
privileges.

Perform periodic audits of control effectiveness.

### Implementation steps

- [Set
up alerts](https://aws.amazon.com/blogs/security/how-to-receive-alerts-when-your-iam-configuration-changes/) to notify on AWS IAM configuration changes
including when an
[IAM user is created](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-a-notification-when-an-iam-user-is-created.html) or when conflicting permissions are
added to a user or role, such as being able to approve its
own requests on a given workflow.

The added notification can be set up using a combination
of
[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html),
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), and
[Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html).

- Automate permissions management and refinement through
[IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) with security integration workflows
that alert teams to access policy changes. For unused roles,
access keys, or
passwords, [IAM Access Analyzer](https://aws.amazon.com/iam/access-analyzer/) provides quick links in the console
to assist you to delete them. For unused permissions, IAM Access Analyzer reviews your existing policies and
recommends a refined policy that is tailored to your access
activity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssec01-bp03.html*

---

# LSSEC02 — Data privacy

**Pillar**: Security  
**Best Practices**: 1

---

# LSSEC02-BP01 Determine applicable regulatory frameworks and enforce data privacy requirements by implementing controls

Many life sciences organizations fall under data privacy
requirements or regulations which influences data security and
architecture, for example where data may be physically located.

**Desired outcome:** Control
objectives identify the locations and conditions where specific data
is required to be stored and controls are implemented.

**Common anti-patterns:**

- Exporting data from shared data sets.
- Manually obfuscating sensitive fields.

**Benefits of establishing this best
practice:** Clarifies requirements as well as control
automation and audit.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by reviewing data privacy requirements within applicable
regulatory frameworks. To determine applicable regulatory
frameworks, start with local regulations and frameworks for the
country where your sensitive data is generated, hosted, and
processed.

Engage with legal counsel who can assist you to define the scope
of the local regulations, as well as additional regulation
frameworks that may apply to you.

Update documentation of data residency requirements and control
objectives with specific details on which data elements are
subject to allowed or disallowed storage and transmission
locations. For more detail, see SEC01-BP03 Identify and validate
control objectives.

Once the determination of requirements has been made and
documented, technical controls can be put in place to enforce
them. Choose which geographic regions to include in your
environment.

Control objectives should be updated to clearly indicate where
data is expected to be located due to data residency requirements.
Implement controls to keep data within those Regions.

### Implementation steps

- Update control objectives to address data residency
regulatory requirements.
- Separate workloads that have different data residency
requirements.
- Implement controls that enhance your digital sovereignty
governance posture.
- Tag PHI data as sensitive and grant least privilege access
only where required.
- Restrict access by location of resource.
- Implement detective controls that notify security operations
when resources are found in unauthorized locations.
- Implement backups to enable recovery from data corruption
and data deletion.
- Update threat models to cover the accidental or malicious
storage of data in unauthorized locations.

## Resources

**Related documents:**

- [Data
Residency with Hybrid Cloud Services Lens - AWS
Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens)
- [Data
protection in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/data-protection.html)

**Related tools:**

- [AWS DataZone](https://aws.amazon.com/datazone/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssec02-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
