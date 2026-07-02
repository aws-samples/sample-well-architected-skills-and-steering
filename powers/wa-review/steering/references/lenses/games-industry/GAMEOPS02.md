# GAMEOPS02 — Account structure

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GAMEOPS02-BP01 Adopt a multi-account strategy to isolate different games and applications into their own accounts

Design an account structure that would guide the infrastructure
deployment to comply to each environment's security, isolation, and
operational needs. Environment isolation by restricting access to it
and permitting only requisite AWS services to be used in them is
essential, with production environments being locked down, while
development and testing environments are lenient to permit
experimentation. Further isolation of major sub-systems in each
environment, and common services that are used by multiple
environments to be hosted and managed out of their own AWS accounts
is highly recommended.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Adopt a multi-account strategy on AWS by isolating the different
environments (like development, test, staging, production, and
shared services) to individual AWS accounts, which reduces the
scope of incidents. Consider AWS Organizations to centrally manage
the hierarchy of your AWS accounts to further simplify operations,
as well as define and apply account-level and organizational
unit-level (OU-level) policies selectively. By designing an
appropriate OU and AWS account structure that is aligned to your
development and productional workflow needs, you can optimize your
costs and enhance scalability.

- **Adopt a multi-account
strategy:** Isolate environments to reduce incident
radius and simplify operations.
- **Use AWS Organizations:**
Manage accounts hierarchically, apply policies, and enable
centralized governance.
- **Plan for Scalability:**
Design fine-grained account structures and implement
cost-saving measures for future growth.

### Implementation steps

A game system deployed in AWS should use multiple accounts that
are logically organized to provide proper isolation, which
reduces the blast radius of issues and simplifies operations as
your game infrastructure scales. AWS accounts that host game
infrastructure are typically grouped into the following logical
environments:

- **Game development
environments** are used by developers for
developing the software and systems for the game.
- **Test or quality assurance (QA)
environments** are used for performing integration
testing, manual QA, and other automated testing that must be
conducted.
- **Staging or pre-production
environments** are used for hosting completed
software so that load and smoke testing can be conducted
prior to launching to production.
- **Live or production
environments** are used for hosting the live
software and infrastructure and serving production traffic
from players.
- **Shared services or tools
environments** provide access to common systems,
software, and tools that are used by many different teams.
For example, a central self-hosted source control repository
and game build farm might be hosted in a shared services
account.
- **Security environments** are
used for consolidating centralized logs and security
technologies that are used by teams that focus on cloud
security.

For game infrastructure on AWS, it is recommended to create
separate accounts for each game environment (development,
testing, staging, and production), as well as accounts for
security, logging, and central shared services.

Typically, smaller game development studios that manage a
limited number of infrastructure resources, usually a few
hundred servers or less, may create one AWS account for each of
these environments (for example, one production account, one
development account, and one staging account). However, as your
game infrastructure or team size grows over time, this
simplified model may not scale well.

When setting up these environments, consider that many AWS
services share resource and
API-level [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) for an entire account within a particular Region.
This must be considered when determining how to logically
organize accounts. AWS accounts only incur cost for consuming
services deployed into them. Therefore, this provides a way to
effectively reduce resource contention and service quotas,
particularly as your game grows and more developers need access
to build and manage resources.

Based on our experience working with larger game development
studios that typically operate thousands of servers with
hundreds of developers accessing resources, we recommend you
design a more fine-grained account structure where individual
applications supporting your game have their own development,
testing, staging, and production accounts. Because it's
difficult and time consuming to re-design your AWS multi-account
strategy after you have launched your game due to the complexity
in planning and migrating live systems, consider your future
scaling needs when determining the right multi-account
structure.

You can use
[AWS Organizations](https://aws.amazon.com/organizations/) to set up a hierarchy and grouping of AWS accounts, and
define [organizational
units](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html) (OUs) to apply common OU-level policies to them
through
[service
control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs). AWS Organizations centrally
manages and governs your environment as you grow and scale your
resources. You can programmatically create new accounts and
allocate resources, group accounts to organize your workflows,
apply policies to accounts or groups for governance,
and simplify billing by using a single payment method for your
accounts. Additionally, Organizations is integrated with other
services so that you can define central configurations, security
mechanisms, audit requirements, and resource sharing across
accounts in your organization.

[AWS Control Tower](https://aws.amazon.com/controltower/) provides a straightforward way to set up
and govern a secure, multi-account environment, called a
*landing zone*. Control Tower creates your
landing zone using AWS Organizations, bringing ongoing account
management and governance as well as implementation best
practices based on AWS's experience working with thousands of
customers as they move to the
cloud. [AWS Config](https://aws.amazon.com/config/) ,
[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), and
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) are services that provide an aggregated or
centralized view of your account's hygiene.

This isolation assists you to set up custom or individual
permissions and guardrails to each game environment. Production
accounts should have the necessary guardrails, access
restrictions, monitoring and alerting, and security tools, while
non-production accounts may not require the same level of
guardrails and permissions. Non-production environments can be
automated to shut down resources after hours and save costs.
Separation of accounts at this level of granularity makes it
straightforward to monitor infrastructure costs for each of the
environments supporting a game.

The following is an example of a multi-account structure for a
game company using AWS Organizations and organizational units
(OUs) to logically group AWS accounts into separate environments
and studios. In this example, OUs are used to group together
accounts based on their environment and then based on the studio
that operates the environment. This demonstrates how you can
create a nested hierarchy to allow separate applications and
games to be deployed into their own accounts within their
environment (depicted as OUs), which can be useful if you
develop and operate multiple games. Refer to the documentation
and whitepapers provided in the resources section of this pillar
to learn about additional strategies that you can consider for
organizing your multi-account strategy.

Based on the discussion above, the sample diagram below assumes
a game studio (Organization) that has a development pipeline
comprised of 4 stages (development, testing, staging, and
production). For a given game (game1), each of the environments
(OU) has individual AWS accounts for game services, dedicated
game servers, social services, and web servers. The resources
that run in each AWS account are relevant to the respective
sub-systems. Typically, every individual game using this kind of
development pipeline would replicate this or a similar structure
for its AWS accounts.

In addition to these game-centric environment OUs, there are
also the shared services OU and security OU. These OUs should be
organization-wide, not for each individual game. That way the
games would consume the shared services for development tools
and data and analytics as in this example. Then, send
application and system logs to the AWS account set up for logs
in the security OU.

Example of account structure for game
environments

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops02-bp01.html*

---

# GAMEOPS02-BP02 Organize infrastructure resources using resource tagging

To effectively manage and track your
[infrastructure
resources](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/tagging.html) in AWS, use proper
[resource
tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) and
[grouping](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html)
to identify each resource's owner, project, application, cost
center, and other data. Tagged resources can be grouped together
using [resource
groups](https://docs.aws.amazon.com/ARG/latest/userguide/welcome.html), which assists with operational support.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define [tagging
policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html). Typical strategies include resource tags for
identifying the resource owner, such as team name or individual
name, the name of the game, application, or project, the studio
name, environment (like development or production), and the role
of the resource (such as database server, web server, dedicated
game server, app server, or cache server). You can add other tags
to assist with business and IT
needs. [AWS Config](https://aws.amazon.com/config/) can also enforce a
[tagging
policy](https://docs.aws.amazon.com/config/latest/developerguide/required-tags.html) at resource creation and update time. Tags and
resource groups are available from the AWS Management Console, the
AWS CLI, and API operations.

### Implementation steps

- Tag resources to identify their owner, project, app, cost
center, and other relevant data.
- Implement tagging policies including tags for owner,
project, studio, environment, and resource role.
- Use AWS Config to enforce tagging policies, and manage tags
through AWS Management Console, CLI, and API.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops02-bp02.html*

---
