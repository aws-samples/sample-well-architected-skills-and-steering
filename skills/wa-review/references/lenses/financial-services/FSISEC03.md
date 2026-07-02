**Pillar**: Security

# FSISEC03: How do you monitor the use of elevated credentials, such as administrative accounts, and guard against privilege escalation?

IAM policies are powerful and complex, so it's important to
study and understand the permissions that are granted by each
policy. Mitigate privilege escalation and monitor unauthorized
activity in your AWS accounts. With the introduction of
generative AI systems, monitoring elevated credentials extends
to model access, prompt engineering, and AI service
management.

## FSISEC03-BP01 Review IAM policies and permissions

[IAM
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) are powerful and complex, so it's
important to study and understand the permissions that are
granted by each policy.

As part of the tight controls FIs implement around identity
management and broader identity management policies, it is
important to perform periodic reviews of your IAM roles
using
[last accessed
information](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html)
to get a report about the last time that an IAM entity (user
or role) attempted to access a service, and
[delete
roles that are not in use](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html). Before you
delete a role, review its recent service-level activity by
viewing service last accessed data report. Use that
information to refine your policies to allow access to only
the services that are in use. Repeat this process to
generate a report for each type of resource in IAM.

For generative AI services, implement comprehensive IAM
policies that grant least privilege access to foundation
model endpoints while establishing private network
communication, monitoring elevated credential usage in AI
workflows, and implementing permissions boundaries for AI
service roles including attribute-based access controls for
dynamic AI resource management.

## FSISEC03-BP02 Mitigate privilege escalation

Privilege escalation refers to the ability of unauthorized
users gaining access to elevated permissions, often by way of
improperly written code or misconfigurations. Privilege
escalation can result from misusing a number of
non-administrator or non-full access permissions. To help
avoid scenarios like this, pay attention to permissions that
would allow the creation, change and deletion of users, roles,
and policies.

As a way to help prevent privilege escalation, you should use
service control policies (SCPs) to
[block
users in](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception)

[your accounts, except for IAM administrators](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception) or
delegated admins, from performing administrative IAM actions.
Delegation is a common practice for FIs. If you want to safely
delegate permissions management to trusted employees, use
[IAM permissions boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html). IAM permissions
boundaries allow for safe delegation of IAM permissions
management while minimizing escalation of privileges. For
example, developers can safely create IAM roles for Lambda
functions and Amazon EC2 instances without exceeding certain
permissions boundaries defined by your IAM administrators.

## FSISEC03-BP03 Monitor unauthorized activity in your AWS accounts

Use the following guidelines to monitor your AWS account
activity:

- Turn on AWS CloudTrail in each account, and use it in each
supported Region.
- Store AWS CloudTrail log in a centralized logging account
with very restricted access.
- Periodically examine CloudTrail log files. Use Amazon GuardDuty, which provides threat detection by continually
analyzing AWS CloudTrail events, VPC Flow Logs and DNS
logs.
- Enable Amazon GuardDuty in each account, and use it in
each supported Region to automatically detect CloudTrail
management events that can lead to
[IAM privilege escalation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html#privilegeescalation-iam-anomalousbehavior) and other IAM

[finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-iam.html).
- Enable Amazon S3 bucket logging to monitor requests made
to each bucket.
- If you believe there has been unauthorized use of your
account, pay attention to temporary credentials that have
been issued. If temporary credentials have been issued
that you don't recognize,
[disable their permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html).
- [View the last accessed information for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-view-data.html)
through the Management Console, CLI or AWS API.

Administrators can configure roles to require identities to
pass a custom string that identifies the person or application
that is performing actions in AWS when the role is assumed.
This identity information is stored as the
[source
identity](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html#STS-API-source-identity) in AWS CloudTrail. Administrators
can review this activity in CloudTrail, and they can view the
source identity information to determine who or what performed
actions with assumed role sessions.

It is also a good practice to periodically
[review
IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-audit-guide.html#aws-security-audit-review-policy-tips) as well as setting restrictive
user access on a need to know basis. You can
[prevent IAM user and roles from making specified changes](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html#example-scp-restricts-with-exception), through Service Control Policies
(SCPs) and set

[Permissions boundaries for IAM entities](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html).

## Resources

**Related documents:**

- [How
to use trust policies with IAM roles](https://aws.amazon.com/blogs/security/how-to-use-trust-policies-with-iam-roles/)
- [Monitor and Notify on AWS Account Root User
Activity](https://aws.amazon.com/blogs/mt/monitor-and-notify-on-aws-account-root-user-activity/)

**Related videos:**

- [AWS re:Inforce 2022 - Security best practices with AWS IAM](https://www.youtube.com/watch?v=SMjvtxXOXdU)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec03.html*
