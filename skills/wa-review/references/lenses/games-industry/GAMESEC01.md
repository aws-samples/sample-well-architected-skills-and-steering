# GAMESEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 5

---

# GAMESEC01-BP01 Use roles and federated access, rather than the account root user, to perform actions on your AWS environment

When you first create an AWS account, you begin with an identity
known as the root user, which is accessed using the email address
and password associated with the account. The root user has
complete access to AWS services and resources within that account.
In most cases, you should avoid using the root user for day-to-day
tasks. When root-level access is required, confirm that it's
absolutely necessary and verify that additional logging and
guardrails are in place to track its use.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In an AWS Organizations configuration, each account still has its
own root user, but day-to-day access should instead be managed
through IAM roles and IAM Identity Center users. Create role-based
access tailored to your game's lifecycle stages and teams. For
example, the live operations team might need permissions to manage
in-game events, while developers need access to push updates. When
working with third-party services or partners, use federated
access to enable secure collaboration without exposing sensitive
infrastructure. This approach verifies that each user or partner
has only the access they need while maintaining the security of
your game's infrastructure and player data.

**Customer example**

AnyCompany Games implemented role-based access control when
developing their new game. By using specific IAM roles for their
diverse development teams, they avoid using shared credentials.
This setup allows a dev team to assume a role for core game
systems, while the content team's role is only able to access
asset management services.

### Implementation steps

- Do not use the root user after setting up an account unless
absolutely necessary. Create the account, secure the root
user, and immediately create the required administration IAM
roles and assign that role to federated user.
- Only use the root user when you need to perform
[a
limited number of tasks that are only available to the root
user](https://docs.aws.amazon.com/IAM/latest/UserGuide/root-user-tasks.html). Examples of these tasks include changing your
root user email address and changing your AWS support plan.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp01-use-roles-and-federated-access-rather-than-the-account-root-user-to-perform-actions-on-your-aws-environment.html*

---

# GAMESEC01-BP02 Use AWS Control Tower to quickly set up a multi-account environment on AWS

If you start using AWS with just a single account, you might find
your game studio growing out of it as your game development
process advances. For example, with a single AWS account, you
might begin to reach service limits, or your costs for different
projects and workloads may become more complex. Creating different
accounts for different game titles and environments allows teams
to experiment with new features, bypass service limits, and
maintain security posture and compliance. By implementing a
multi-account strategy in AWS, you can benefit from distributing
service limits across multiple accounts and gain insights into
your AWS costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

It is a common misconception that using multiple AWS accounts will
automatically be more confusing and time consuming. Rather, using
AWS services that are designed to facilitate the governance of
multiple accounts can assist your game studio to spend less time
managing your accounts.

You can use AWS Control Tower is a service to securely provision a
multi-account AWS environment. Control Tower is recommended if you
are building a new AWS environment, starting your journey on AWS,
or are completely new to AWS. During the short setup process , you
can integrate with other AWS services that are involved with
managing accounts and user access, such as AWS Organizations, Service Catalog, and AWS IAM Identity Center.

**Customer example**

AnyCompany Games initially operated from a single AWS account, and
they hit multiple roadblocks when one of their games' development
team reached EC2 service limits during a crucial beta test. At the
same time, their development team for a different game struggled
with resource allocation for their automated testing pipeline. The
situation reached a breaking point when AnyCompany Games couldn't
accurately separate costs between projects, making it difficult to
budget for each game's development.

AnyCompany Games then implemented a multi-account strategy using
AWS Control Tower. They created separate accounts for each game
project, with distinct development, QA, and production
environments. This account level separation isolates each projects
data and assets, so teams working on one game can't access or
modify resources from another. Through AWS Organizations, they
established a centralized billing structure that clearly showed
each game's infrastructure costs and also created
organization-wide access polices.

### Implementation steps

- Use AWS Control tower to set up an automated multi-account
environment.
- Organize accounts based on environments (like development,
QA, and production).
- Use AWS IAM Identity Center and Service Catalog to
centralize user permissions and streamline resource
provisioning across accounts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp02-use-aws-control-tower-to-quickly-set-up-a-multi-account-environment-on-aws.html*

---

# GAMESEC01-BP03 Use least privilege role policies that are tailored to specific job functions

Configuring IAM policies is an essential part of establishing a strong security
foundation. When you set permissions with IAM policies, grant only the permissions required
to perform a task. You do this by defining the actions that can be taken on specific resources
under specific conditions, also known as least-privilege permissions. For example, QA teams
need access to change things in the testing environments but should not have the ability to
modify the production environment.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

You might start with broad permissions, like [managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html),
while you explore the permissions that are required for your workload or use case. As your use
case matures, you can work to reduce the permissions that you grant to work toward least
privilege.

### Implementation steps

- Follow the practice of least privilege permissions for create IAM roles for users
and applications.
- Use AWS-managed policies to quickly provide broad access while identifying the
specific permissions teams or applications need to perform their tasks.
- Studios can also use [IAM
access analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_reduce-permissions-edit-policy.html) to generate custom IAM policies based on
CloudTrail events that identify actions and services used by an IAM entry.
- Regularly review IAM policies and edit overly permissive policies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp03-use-least-privilege-role-policies-that-are-tailored-to-specific-job-functions.html*

---

# GAMESEC01-BP04 Use roles and federated access policies together with account level access policies to grant access to your AWS resources

New AWS users often use IAM policies only when granting access to
others. However, if you are using AWS Organizations, consider how
to use service control policies together with IAM policies to
grant your studio team members and contractors the necessary
levels of access.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

You can create IAM policies to allow or deny access to AWS
services or API actions that work with AWS Identity and Access Management. They can only be applied to IAM identities, such as
users, groups, or roles. For example, an IAM policy might be used
to provide a user read-only access to Amazon S3.

Service control policies (SCPs) are guardrails for your AWS accounts. An SCP doesn't grant permissions, they are used to
restrict actions on AWS services for individual member accounts.
For example, an SCP can deny an AWS account from accessing a
particular Region.

When an action is taken, the relevant IAM policy is evaluated in
combination with the SCPs. Following up on the previous example,
is a role is attempts to run an EC2 instance, IAM indicates is
they are permitted ("Allow" for ec2:RunInstances) and
the SCPs will determine if their choice of Region is valid
("us-east-1" is permitted, but "us-west-1" is
denied by the SCP).

Layering IAM policies and SCPs can verify that anyone who accesses
your AWS resources will only be given the appropriate permissions
that they need. This is especially important to consider if your
AWS accounts and resources span multiple Regions, but not everyone
within your game studio needs to access all of them.

You can tailor IAM policies to grant specific teams specific
permissions for updating things like game configurations, managing
player data, configuring promotional events, and moderating
user-generated content. Meanwhile, you can use SCPs to enforce
organization-wide controls crucial for game operations. These
might include restricting deployment to only approved Regions
where the game operates, helping prevent unauthorized access to
sensitive player data stores, enforcing compliance requirements,
and controlling costs by limiting service usage across development
accounts.

### Implementation steps

- Use IAM policies to manage permissions for individual users,
groups, or roles.
- Use service control policies (SCPs) in AWS Organizations to
enforce account-level permissions.
- Combine IAM policies and SCPs to grant only the required
access for specific users and accounts.

### Resources

- [Policies
and permissions in AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [Service
control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp04.html*

---

# GAMESEC01-BP05 Use a central identity provider

A central identity provider acts as a single source for storing and
managing user credentials, identities, permissions, and
authentication.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use a central identity provider to streamline your user
authentication process, enforce consistent security polices, and
simplify your user management across your AWS accounts and
applications. Having a centralized approach removes the need to
manage user identities and credentials separately, which reduces
the risk of inconsistencies, redundancies, and other security
vulnerabilities. Consolidating user identities and authentication
into one place also allows for better visibility, control, and
auditability for your entire AWS environment.

**Customer example**

AnyCompany Games faced significant challenges with managing
developer access across their rapidly expanding AWS
infrastructure. Their development team grew from 50 to 200 people
across three major titles. Initially, each project team managed
their own AWS access credentials, resulting in inconsistent
security practices, delayed onboarding for new developers, and
occasional security incidents.

The studio implemented AWS IAM Identity Center as their central
identity provider, consolidating user management into a single
system. They connected it with their existing corporate directory,
enabling developers to use their same company credentials for AWS
access. Now developers use their single, existing company login to
gain the AWS access they require to complete their work

### Implementation steps

- Consider using AWS IAM Identity Center as your central
identity provider. This provides consistent access
management across your AWS accounts, provides your employees
with single sign-on authentication, and simplifies user
access auditing to your AWS applications. IAM Identity Center also connects with existing corporate identities from
supported identity providers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec01-bp05.html*

---
