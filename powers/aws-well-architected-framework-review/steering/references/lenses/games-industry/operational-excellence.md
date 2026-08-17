# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 6

---

# GAMEOPS01 — Live operations

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GAMEOPS01-BP01 Use game objectives and business performance metrics to develop your live operations strategy

Consult business stakeholders, such as game producers and publishing
partners, to determine objectives and performance metrics for a
game. This can assist you develop plans for how you will manage the
game, including defining your maintenance windows, software and
infrastructure update schedules, and system reliability and
recoverability goals.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

These metrics can also assist you determine at which stage of your
game's lifecycle you should incorporate a live operation steam
(Live Ops) to monitor game health, collect direct game feedback,
and build streamlined and automated release processes. For
example, a new game might wait until a certain scale is achieved,
measured by active player count, revenue, or another set of
metrics, before setting up a dedicated live operations team. An
established game development studio might already have live
operations experience, perhaps for their other games, so they'd
only need to onboard the new game.

### Implementation steps

- You may define the targets for player concurrency (CCU) and
daily and monthly active users (DAU and MAU) that the game
infrastructure should be capable to effectively support,
your infrastructure budgets, financial targets, and other
performance goals, such as the frequency for release of
content and features to increase player engagement. These
objectives and metrics feed into decisions about the game
design, release management, observability, and support that
is needed for efficient operations.
- Your game might have an objective to release new content
updates at least once each month with no downtime during
release. This information assists you to define your release
deployment strategy and coordinate the scheduling of
required maintenance that may require downtime at other
times throughout the month and contribute towards your
availability SLA.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops01-bp01.html*

---

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

# GAMEOPS03 — Game deployments

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

# GAMEOPS03-BP01 Validate and test your existing core game systems and infrastructure before reusing it in your game

Organizations tend to reuse existing components and source code
from previous games to save on development time and cost. These
legacy components and code may not be subjected to a thorough
review or have detailed integration testing and instead rely on
their past performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

While reuse assists improving
productivity, it can also introduce the risk of reintroducing past
performance and stability issues into a new project. Therefore,
when reusing existing components and source code from previous
games, robust testing should be implemented.

### Implementation steps

- **Identify reused code and
components:** Catalog the source code, libraries,
and components being reused from previous games. Clearly
distinguish between actively maintained and deprecated code
- **Document original behavior and known
issues:** Record the original performance
characteristics, functional limitations, and known bugs or
production incidents associated with the reused components.
- **Perform a thorough code
review:** Conduct a detailed technical review of
the reused components, especially those that had issues in
the past or are poorly documented.
- **Replace or refactor high risk legacy
components:** Prioritize replacing or updating
legacy components that have a history of issues or are no
longer maintainable, rather than relying on workarounds in
production.
- **Conduct integration and
compatibility testing:** Validate the reused
components within the context of the new game's systems.
Verify that they interact properly with new modules, tools,
and APIs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops03-bp01.html*

---

# GAMEOPS03-BP02 Conduct performance engineering before every release (or at least for major releases)

Performance engineering is the process of monitoring multiple key
operational metrics of an app to discover optimization
opportunities that can further improve the application's
performance. This is an iterative process that starts with
testing, followed by optimizing code, its dependencies, associated
processes, its host operating system, and the underlying
infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To conduct a deeper analysis of the app's performance, integrate
an application performance monitoring (APM) or debugging tool in
the app code that can isolate issues and reduce troubleshooting
time by tracking its behavior for anomalies across the flows of
the app. APM tools are also able to identify slow performing
methods and external operations.

[AWS X-Ray](https://aws.amazon.com/xray/) assists developers with their performance engineering
activities, like identifying performance bottlenecks and analyzing
and debugging production errors. You can use X-Ray to understand
how your application and its underlying services are performing
and identify and troubleshoot the root cause of performance issues
and errors. Through numerous rounds of load tests, in which the
application and its infrastructure is gradually loaded with
synthetic player traffic, various system bottlenecks, app errors,
exceptions, OS problems, and other issues are identified that may
have not been found during other QA tests.

For critical events like game launches, content releases,
promotions, and major in-game events, use
[AWS Countdown](https://aws.amazon.com/premiumsupport/aws-countdown-sports/), which provides implementation guidance based on
playbooks built by games experts to verify operational readiness,
mitigate potential risks, and plan for capacity needs. AWS Countdown also has a
[premium
support](https://aws.amazon.com/premiumsupport/aws-countdown/) option that offers enhanced support and options
like engineers to optimize your infrastructure.

### Implementation steps

- Performance engineering involves evaluating and monitoring
key operational metrics to verify that your application's
code, processes, operating system, and infrastructure are
functioning as expected. Pre-production review also assists
to define baseline performance at different levels of
simulated usage.
- Discover and track key metrics like utilization, services,
I/O, processes and such by using system tools such as sar,
top, vmstat, sysstat, netstat, and Performance Monitor.
- Track your application's performance and behavior using APM
tools like AWS X-Ray to isolate issues, identify
bottlenecks, and debug production errors.
- For critical events like game launches, subscribe to AWS
Countdown (IEM) for architectural and operational guidance,
on-demand operational support, and to identify risks and
plan mitigations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops03-bp02.html*

---

# GAMEOPS03-BP03 Load test early and often

Load testing is the process of simulating real-world traffic on a
system to assess its reliability and performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Load testing is
a key factor in developing a performance baseline for your
resources and understanding your system's capacity, which can
guide financial forecasting, architecture design, resource
allocation, automated scaling configurations, and post-launch
pre-scaling activities. Additional benefits include:

- **Optimized infrastructure:**
Resources might be over or under-provisioned. Understanding
the resources needed will result in lower costs and less
infrastructure to manage.
- **Scalability
readiness:** Certain mechanisms and features can
drive users into a game quickly. Knowing when and how to scale
can be the difference between appropriately meeting the
increased demand and losing players. Use load test results to
prepare runbooks with system thresholds, alert points, and
critical alert points at different scaling levels.
- **Higher quality code**: Issues
such as excessive crosstalk between services, unbatched
database calls, inefficient algorithms, memory leaks, and
service degradation issues are sometimes simpler to identify
at scale.
- **Behavior validation:**
Injecting different kinds of failures into your tests can
validate the system's expected behavior or uncover
error-handling issues that need to be corrected.

Ideally, developers should perform load testing at multiple points
throughout the development process, as each can yield different
benefits: Early on, they guide architectural decisions and
refactoring efforts while it's cheaper and straightforward to make
changes. At the end of each sprint or iteration, they validate the
application's performance with the latest features and
functionality.

Prior to deploying to production, large-scale load testing
simulating expected real-world usage patterns confirms the
system's ability to handle the production workload. After the
deployment, periodic load tests monitor the system's performance
and identify changes or bottlenecks that may arise over time.

To simulate player traffic, you need lightweight clients or bots
that emulate the game client flows and transact with the game
backend to simulate real-world player behavior. This data is
generally captured through game play logs and data generated by
human-driven QA tests, as well as through real-world limited scale
alpha or beta tests where real players are invited to play an
early-access build of the game.

It is important to record the system's behavior in an operational
runbook to assist in troubleshooting possible failures in the
future and to retain performance metrics that future load tests
can be compared against. It is also recommended to have human QA
personnel test the game while it is being load tested as they
might discover issues that bots fail to identify and metrics do
not reflect.

[AWS Fault Injection
Service](https://aws.amazon.com/fis/) is a fully managed service for running fault
injection experiments that make it straightforward to improve an
application's performance, observability, and resiliency. Fault
injection experiments are used in chaos engineering, which is the
practice of stressing an application in testing or production
environments by creating disruptive events, such as sudden
increase in CPU or memory consumption, observing how the system
responds, and implementing improvements. Fault injection
experiments assist teams to create the real-world conditions
needed to uncover the hidden bugs, monitoring blind spots, and
performance bottlenecks that are difficult to find in distributed
systems.

### Implementation steps

- Set up a distributed load testing environment using
[Guidance
for Kubernetes-Bases Game Load Testing](https://aws.amazon.com/solutions/guidance/kubernetes-based-game-load-testing-on-aws/).
- Customize and deploy Locust control and worker pods within
the EKS cluster using the provided deployment files,
enabling scalable and manageable load generation.
- Record system behavior and metrics during load testing in an
operational runbook to assist with future troubleshooting
and establish performance baselines.
- Use fault injection experiments to simulate real-world
disruptions and uncover hidden issues in system performance,
observability, and resilience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops03-bp03.html*

---

# GAMEOPS03-BP04 Adopt a deployment strategy that minimizes impact to players

Incorporate a deployment strategy for your game software and
infrastructure that minimizes the amount of downtime that keeps
players out of your game. While certain types of updates might
require installing new updates to the game client, design the game
to minimize or avoid the need for downtime during deployments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

One of the most important steps to consider when developing a game
deployment strategy is to determine how your game infrastructure
will be managed. Manage your game infrastructure using an
infrastructure as code (IaC) tool such
as [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[Terraform by](https://www.terraform.io/)
[Hashicorp](https://www.terraform.io/) to
reduce human errors during environment preparation. Infrastructure
templates can be deployed and tested in automated pipelines, which
creates consistency in the configuration of different game
environments.

There are several deployment strategies that can be used for a
game:

**Rolling substitution**

The primary objective of a rolling substitution for deployment is
to perform the release without shutting down the game and without
impacting players. It is important that the upgrade or changes
that are to be performed are backward compatible and will work
adjacent to the previous versions of the system.

In this deployment, the server instances are incrementally
replaced (substituted or rolled out) by instances running the
updated version. This rolling substitution can be performed in a
few different ways. For example, to implement rolling updates to a
fleet of dedicated game servers, a typical approach involves
creating a new Auto Scaling group of EC2 instances that contain
the new game server build version deployed onto them, and then
gradually routing players into game sessions hosted on this new
fleet of servers. If there is an associated game client update
that is required as a prerequisite to use the new game server
build, then you must include a validation check to verify that
only players that have this new game client update installed are
routed into these game sessions.

Server fleets (for example, EC2 Auto Scaling groups) containing
the old game server build version are only removed from service
after they are drained of active player sessions in a graceful
manner, typically by setting up individualized-server metrics that
allow game operations teams to automate this process.
Alternatively, to reduce the amount of infrastructure and time to
conduct a rolling deployment, an alternative approach can be
performed where existing production instances are removed from
service, updated with the new game server build, and then placed
back into the production fleet. This approach reduces the amount
of infrastructure that is required, but it also increases risk
since the number of available live game servers for players is
reduced as servers are being replaced.

This model can also be used for performing rolling deployments to
backend services such as databases, caches, and application
servers that don't host gameplay. As long as these services are
deployed in a highly-available manner with multiple clustered
instances, then the complexity of deployments to these services
should be less than deployments to dedicated game servers.

**Blue/green deployment**

The primary objective of a blue/green deployment in a game is to
minimize downtime while also allowing safe rollback to the
previous deployment if issues are identified. It is suitable for
deployments where two versions of the game backend are compatible
and can serve players simultaneously.

In the blue/green deployment strategy, two identical environments
(blue and green) are set up. The existing game version is labeled
as blue, while the new game version that is the deployment target
is labeled as green. When the green environment is ready for
migration, you can configure your routing layer to flip the traffic
over to the green environment while keeping the old environment
(blue) available in case failback is needed. In this scenario, the
routing updates might require updating the matchmaking service to
configure it to begin sending game sessions to the new fleet, or
in the case of game backend services, this could be updating DNS
records in Amazon Route 53 for your service
or [shifting
application load balancer weights](https://aws.amazon.com/blogs/aws/new-application-load-balancer-simplifies-deployment-with-weighted-target-groups/) to send traffic to your
new target group.

One of the drawbacks of the blue/green deployment strategy is the
inherent cost of the standby environment due to the additional
infrastructure required while performing the deployment. An option
to mitigate this additional infrastructure cost is to consider
adopting a variant of blue/green deployment where new game
software is deployed onto the same servers that are already
deployed into production. In this scenario, a new green server
process can be started with the new software alongside the
existing blue server process, with the cutover happening between
server processes rather than between separate physical
infrastructure. This approach can also speed up game deployments
across a large amount of infrastructure by removing the need to
wait for new servers to be launched in the cloud. For best
practices on this deployment approach,
see [Blue/Green
Deployments on AWS.](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html)

**Canary deployment**

Canary deployment is useful for game developers, as the strategy
can be applied to release an early alpha or beta build of a game,
or a game feature like a new game mode, map, or challenge to a
restricted or small set of players in-production. Such a
deployment is called a *canary*. The release
may have additional tracking and reporting, so when real players
play that game or feature, their game play telemetry is collected
and analyzed for anomalies and issues.

For new features, the players are not consistently notified about
this, and the game telemetry is the primary source used to
determine if players are experiencing issues and the release
should be rolled-back. At the same time, if no significant issues
are identified, the feature can then be further rolled out to more
players for additional data. If the players are notified, then
they can be asked to provide regular feedback about their
experience. Such test activity would ideally be coordinated by a
live operations team.

As a strategy, canary deployment can also be used for standard
releases to gradually make a new feature available to the players.
A potential advantage over the standard blue/green environment is
that a full-scale second environment is not required. The capacity
of the new scaled-down environment determines how many players are
to be onboarded to the new feature. Before adding more players,
the capacity must be scaled appropriately. Even if this customized
blue/green technique is expected to cost comparatively lesser than
standard blue/green, it is still estimated to incur cost that may
be higher than the rolling substitution technique of canary
deployments.

Run only a single canary on a production environment, and focus it
for its data and feedback. If multiple canaries are deployed, it
complicates troubleshooting and isolating of issues in production
and impairs the quality of the datasets and feedback being
collected.

A variation in the canary is when one or more experiments
(generally UI tests) are run through targeted deployments, where
one set of the game backend servers serve one version of a feature
and another same-sized set serve another version of the same
feature. No additional or special infrastructure is created for
this, and only the chosen pockets of backend servers receive these
updates. The outcome of the experiments is to observe how players
react to each of the versions of the same feature, determine if
there is a consensus of overall like or dislike, and observe if
there are issues identified with its usability or functionality.
Such strategic experiments are also called A/B tests, and the
overall process is called *A/B testing*. On
completion of these experiments, necessary test data is collected
before reverting to the current version of the game backend system
on the servers used for the tests.

**Legacy traditional deployments**

In the traditional style of deployment, during a scheduled
maintenance window the game is shut down and connected players are
dropped or drained before server instances within the game backend
are updated with the latest code builds. This deployment impacts
players each time it is performed, and the players must be
notified ahead of the schedule. As a result, this model causes the
most player impact and should be avoided whenever possible.

After the game update is deployed, the game can be smoke tested
prior to opening the game to the players, who would be waiting for
the game to reopen. This can cause a spike of traffic when players
try to login and play within a short period of time. Therefore, if
the game is not designed to handle such spikes of traffic, you can
choose to gradually allow players back into the game in batches.

Alternatively, you can opt to over-provision the infrastructure to
sustain the opening spike of traffic, and after the game traffic
settles, resources can be scaled down. If necessary, conduct this
type of deployment during off-peak hours when the number of
players is at its lowest. Frequently scheduled maintenance, as
well as extended maintenance, inherently carries a risk of player
attrition and potential loss of revenue. Players also expect
changes after a new release and can lose trust in the game once
returning after a period of downtime.

### Implementation steps

- **Minimize downtime:**
Implement deployment strategies that reduce downtime and
keep players in the game.
- **Infrastructure as code
(IaC):** Use tools like AWS CloudFormation or
Terraform to manage game infrastructure and reduce human
errors.
- **Deployment strategies:**
Use one or a combination of rolling substitution,
blue/green, and canary deployments to provide smooth updates
and reduce player impact.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops03-bp04.html*

---

# GAMEOPS03-BP05 Pre-scale infrastructure required to support peak requirements

Scale infrastructure ahead of large-scale game events to make sure
that you can handle the sudden increase in player demand.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

In addition to new game launches, live games typically run in-game
events, promotions, new content, and season releases as examples
of ways to sustain and improve player engagement. Such activities
experience a high volume of player traffic for the duration of the
event or promotion. The business expects to hit or surpass their
intended targets for the event, and the game infrastructure must
sustain and support them through it.

Prepare your infrastructure ahead of time to be able to support
the anticipated player load that you will experience during large
scale events. To prepare, game operations teams should coordinate
with stakeholders in sales and marketing to estimate the projected
demand that will be generated in an upcoming event by looking at
past player concurrency, engagement metrics, and sales data. If
the event is for a new game launch, game operations teams should
work with these stakeholders to identify realistic projections for
what scale they anticipate. While it may be difficult to predict
how successful a game will become, it is important that everyone
understands what the expectations are for success so that the
infrastructure can be scaled and tested to support those goals.

Many games choose to launch in stages, starting with a soft launch
by opening the game to a small number of players and then
organically scaling the players at every stage, prior to a full
public launch. During the soft launch period, monitor, identify,
track, and resolve issues while refining your projections for the
public launch.

To properly estimate infrastructure requirements, collect data
through load and performance tests run against your game backends
running on production or a production-like staging environment
prior to the game launch. Multiple rounds of these tests should be
run to simulate different conditions of the game and validate that
the backend can withstand the load under most conditions.

To achieve this, developers can write gameplay bots that traverse
various workflows in the game and emulate different conditions.
These tests should inspect the different system layers of the game
backend so that each layer and component is tested and the details
are recorded. Use the data collected from these tests to provision
plan for the game launch.

Single points of failure (SPOF) should be identified and removed
where possible by making the application highly available and
fault tolerant. Use load tests to identify SPOFs by emulating
failures at different upstream and downstream layers and verifying
game and other component behavior.

Along with the necessary estimated infrastructure to be
provisioned for the game launch, in-game event, or promotion
preparations, set up the system to automatically scale on-demand.
Define, configure, and monitor scaling event thresholds to allow
the game backend to scale to sustain a high volume of player
traffic. For variable traffic, pre-provisioning is best because
there may not be enough time to scale-out. Manual scaling might be
required during initial game launches that drive higher than
anticipated demand faster than automated systems can scale
resources.

On AWS, organizations should request higher
[Service Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) for the services that they use in the game backend.
Service Quotas are set up for accounts to safeguard customers from
inadvertently standing up or scaling more infrastructure than
intended. When a game running in an account hits the upper limit
of the configured service quota in that Region, the service
throttles the requests beyond the provisioned quota and burst
provisions. Throttles can cause unintended or unexpected errors
and impair the player experience. Monitor, track, and regularly
review service quota thresholds for the services used by the game
in-production to avoid throttling. When the usage crosses a
tolerable service quota threshold, an increase in the quota can be
requested by raising
an [Support
Case](https://docs.aws.amazon.com/awssupport/latest/user/getting-started.html) from the Console Support Center, after logging in to
the affected account, or using the
[Support
API](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html).

For critical events like game launches, content releases,
promotions, and major in-game events, use
[AWS Countdown](https://aws.amazon.com/premiumsupport/aws-countdown-sports/). Countdown provides implementation guidance based
on playbooks built by Games experts to provide operational
readiness, mitigate potential risks, and plan for capacity
needs. AWS Countdown also has a
[premium
support](https://aws.amazon.com/premiumsupport/aws-countdown/) option that offers enhanced support and options
like engineers to optimize your infrastructure.

If you are launching a game hosted on Amazon GameLift, review
the [pre-launch
checklists](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_launch.html) to prepare.

### Implementation steps

- **Scale infrastructure
ahead:** Prepare infrastructure in advance for
large-scale game events to handle sudden increases in player
demand.
- **Estimate demand:**
Coordinate with sales and marketing to estimate projected
demand using past player data and realistic projections.
- **Load testing and SPOF
removal:** Conduct multiple rounds of load tests to
validate backend capacity, identify single points of
failure, and properly configure automated scaling.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops03-bp05.html*

---

# GAMEOPS05 — Load testing

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GAMEOPS05-BP01 Choose the right stage, architecture, and load testing framework to meet your goals

The approach to load testing a game can vary significantly
depending on many factors, including the stage of the development
process it is performed in, the architecture of the
load-generating system itself, and the choice of load testing
framework. The timing of when it is conducted, whether in the
early phases, during iterative sprints, prior to production
deployment, or post-deployment, will shape the goals and focus of
the testing efforts. Different designs of load-generating
infrastructure have their own pros and cons, and the selection of
the load testing framework greatly influences the capabilities,
ease of use, and integrations available for the testing process.
By thoughtfully aligning these elements, development teams can
tailor the load testing approach to the unique characteristics of
the game, extract the most valuable performance insights, and
provide a smooth experience for their players.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Load testing in different development
stages**

Conducting exploratory load testing early in the development
phases can validate the underlying system architecture. This
assists developers to make informed decisions about the game's
infrastructure, database design, and network topology before
extensive implementation work is done. Load tests identify risks
and create a performance baseline, potentially minimizing the need
for costly rework and technical debt later in the development
lifecycle. They can also foster a shared understanding of the
game's performance requirements among the team, leading to
better collaboration and decision-making. Ultimately, load testing
during the initial phases builds a strong foundation for a
high-performing, scalable, and resilient game, helping enhance the
overall player experience.

At the end of each sprint or iteration, load testing can evaluate
the performance impact of the new features, bug fixes, and other
changes introduced in the latest cycle. This targeted approach
allows development teams to quickly identify regressions or
performance degradations introduced by the latest updates,
enabling them to address these issues before they are propagated
further down the pipeline and maintaining a consistent level of
quality and performance.

Before deploying to production, robust load testing assists
teams validate the system's ability to handle the anticipated
real-world traffic and load conditions. They can uncover
scalability bottlenecks or resource constraints within the
production infrastructure and provide the opportunity to optimize
the game's performance, creating a smooth and responsive user
experience from day one. The insights gained from pre-launch load
testing can mitigate launch-day risks and inform ongoing capacity
planning, which lays the foundation for the game's long-term
sustainability and scalability.

Load testing a game that is already live in production allows
teams to monitor the game's performance and identify performance
regressions or degradations that may occur over time. This enables
them to proactively address issues before they impact the player
experience and negatively affect user retention. Additionally,
load testing in production validates the effectiveness of
performance optimization efforts or infrastructure scaling that
has been implemented. This process provides a high-quality,
responsive, and scalable gaming experience for players even as the
game evolves and matures.

**Load-generating architectures**

The design of the load-generating architecture for game load
testing can take various forms, each with its own set of
advantages and considerations.

At the most basic level, self-managed
[Amazon EC2](https://aws.amazon.com/ec2/)
instances can be provisioned and configured to act as load
generators. With a control node and worker nodes approach, you can
set up multiple load-generating instances, each running their own
test script and overall managed by a single control instance. The
architecture can scale up and generate more load without
increasing complexity by spinning up additional worker nodes, but
this hands-on approach requires teams to handle the provisioning,
configuring, and managing of the underlying infrastructure.

For a more scalable and orchestrated approach, you can use
[Amazon EKS](https://aws.amazon.com/eks/)
Kubernetes clusters to manage and distribute the load testing
workload across a fleet of container-based load agents. Kubernetes
automatic scaling features can be used to handle the scaling of
the load-generating pods, while teams themselves configure and
manage the underlying EC2 instances in the cluster hosting the
pods.

Alternatively, the serverless nature of
[AWS Fargate](https://aws.amazon.com/fargate/) can speed up and simplify the load testing setup by
abstracting away the infrastructure management while still
providing the necessary scalability and flexibility. For hybrid
solutions where an on-premises, load-generating Kubernetes cluster
already exists but additional capacity might be needed,
[EKS
Anywhere](https://aws.amazon.com/eks/eks-anywhere/) can manage both clusters as one from the AWS Management Console.

You can also use
[AWS Lambda](https://aws.amazon.com/lambda/) functions depending on your requirements and goals.
Lambda functions are relatively straightforward to set up and
scale without the need to provision and manage additional
resources. They also allow the creation of more complex and
dynamic test scenarios due to deep integration with other AWS
services. However, Lambda functions do have limits on concurrent
functions and runtime (15 minutes), which may constrain the scale
and length of load testing that can be achieved. Cold start
latencies can also impact the accuracy of the results, and the
resource limitations of Lambda may not be suitable for highly
demanding load testing workloads.

Studios wishing to use a pre-built solution can use
[Distributed
Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html). This solution uses the Amazon ECS on
AWS Fargate to deploy containers that can run simulations of tens
of thousands connected users. You can use this to quickly start
your load testing infrastructure in IAC fashion using AWS CloudFormation.

**Load testing frameworks**

No two load testing frameworks are built the same. Some have
intuitive graphical interfaces for test creation, while others are
entirely command line-based. One tool might be flexible and
performant but require time and effort to configure and manage,
and another might be serverless but limited in the tests it can
create and run. Some enjoy large communities and plenty of
tutorials while being unproven in the field, contrasting sharply
with others that might be battle-tested in production but lack
community support or documentation. Choose the framework that
strikes the right balance for you and your team. Some few popular
options are:

- **[Apache
JMeter](https://jmeter.apache.org/):** Popular Java-based, open-source load
testing framework due to its robust feature set and ease of
use. Its ability to simulate complex user scenarios, wide
range of supported protocols, comprehensive reporting, and
proven track record makes JMeter a reliable choice for load
testing.
- **[Locust](https://locust.io/):**
Modern, distributed load testing framework built on an
event-driven architecture, making it performant while
resource-efficient. Tests are written in Python, allowing
flexible testing scenarios that take advantage of thousands of
powerful third-party libraries, while remaining friendly and
simple to read.
- **[Grafana
K6](https://k6.io/):** Powerful load testing framework that
combines ease of use with advanced capabilities. Its support
for distributed load generation, flexible scripting, and
seamless integration with Grafana for data visualization make
Grafana K6 an attractive choice.
- **[Gatling](https://gatling.io/):**
Open-source load testing framework known for its performance
and scalability. Its Scala-based, domain-specific language
(DSL) allows developers to create concise, maintainable load
testing scripts, and its robust reporting and analysis
capabilities provide detailed insights of the system under
test.

### Implementation steps

- **Load testing stages:**
Conduct load testing at various development stages (early
development, sprints, pre-production, and post-deployment)
to validate system performance and identify issues.
- **Load-generating
architectures:** Choose appropriate load-generating
architectures (EC2, EKS, Fargate, or Lambda) based on
scalability needs, management preferences, and specific test
requirements.
- **Load testing frameworks:**
Select a load testing framework (like JMeter, Locust,
Grafana K6, or Gatling) that balances ease of use,
performance, flexibility, and community support to suit your
team's needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops05-bp01.html*

---

# GAMEOPS06 — Optimize over time

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GAMEOPS06-BP01 Monitor key game metrics to identify player trends and patterns, and use the information to improve the game

In addition to game client system usage, app usage, exceptions,
and crash data, capture game telemetry data that is sent to a game
backend system. This data should represent player activity so that
you can understand how players interact with various features in
the game.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Depending on its implementation, game clients can collect
telemetry data at predefined game features or locations in a game
world. The data is sent to the backend ingestion service for
processing. If the backend service is unreachable, the clients can
store the data locally on the local device until the backend
service is available again. The game designers use this telemetry
data to review how players are playing the game, and if there are
anomalies in the game.

For example, player movements and interactions with items in a map
can be extracted from telemetry data and plotted as a heat map of
activities in-game by players over a set window of time. Such data
assists the game designers identify the need to balance various
elements in the game, such as the power of a weapon, the power of
an in-game character, or the complexity of a map. The raw
telemetry data is generally stored and then processed to extract
analytics that can be visualized by analysts.

The
[Game
AnalyticsPipeline](https://aws.amazon.com/solutions/implementations/game-analytics-pipeline/) solution implementation assists game
developers launch a scalable serverless data pipeline to ingest,
store, and analyze telemetry data generated from games and
services. The solution supports streaming ingestion of data,
allowing users to gain insights from their games and other
applications within minutes.

For custom game telemetry data ingestion, storage, processing and
analytics, AWS also offers a number
of [specialized
services for big data processing and Analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/).

### Implementation steps

- **Capture game telemetry
data:** Collect data on player activity, system
usage, exceptions, and crashes to understand player
interactions and identify issues.
- **Implement telemetry
collection:** Use predefined game features or
locations to collect telemetry data and send it to backend
services, storing locally if the backend is unreachable.
- **Use AWS analytics
solutions:** Use AWS services like the Game
Analytics Pipeline for scalable data ingestion, storage, and
analysis, as well as specialized big data processing and
analytics services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops06-bp01.html*

---

# GAMEOPS06-BP02 Update and adapt the load testing approach as the game changes

Optimizing the load testing approach is a continuous process that
should evolve alongside the game development cycle. As the game
grows in complexity, user base, and feature set, the load testing
strategy must adapt to verify that it accurately simulates
real-world conditions and provides actionable insights.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider
the following:

**Missing or outdated testing
scenarios**

As new functionality is added to a game during the development
process, create and run new load testing scenarios to validate the
performance and scalability of the new features. Similarly,
features and functionality are often refactored to improve
performance, address player feedback, or align with new design
goals, requiring testing scenarios to be continuously updated to
keep pace with the changes and truly test and reflect the state of
the system.

**New load testing frameworks**

Developers might need to change load testing frameworks for a
variety of reasons:

- The initial framework may no longer be able to adequately
simulate the user load or provide the necessary level of
insight into the system's performance
- New game features might require load testing support for new
protocols, APIs, or integration points
- Developers might desire more advanced features as they become
more comfortable with the load testing process
- Preference for frameworks that better align with the team's
technical expertise, programming languages, or existing
toolchains

By carefully evaluating and adapting over time, developers can
align the load testing process with the game's changing
requirements and continue to provide the requisite insights to
optimize and improve the overall user experience.

**Optimizing cost**

The ease and convenience of using managed AWS services can be
highly beneficial, especially in the early stages of development.
These services abstract the underlying infrastructure management,
allowing teams to quickly set up their solution and focus solely
on crafting load testing scenarios and analyzing the results.
However, using managed services can often come at a higher cost
because of the additional value and convenience they provide, like
provisioning, configuring, and maintaining infrastructure, as well
as providing high availability, scaling, and monitoring
capabilities.

As teams mature and grow more comfortable and confident with their
load testing process, there may come a time when self-managing the
infrastructure can provide additional optimization and cost
savings. While this hands-on approach increases the operational
overhead, having direct control over the compute resources,
configurations, scaling behaviors, and resource utilization can
unlock new opportunities for fine tuning and reducing cost. For
example, it might make sense for teams to start their load testing
journey with an AWS Fargate serverless architecture, then move to
self-managing the underlying nodes in an Amazon EKS cluster later.

### Implementation steps

- **Update testing scenarios:**
Continuously create and update load test scenarios to
validate new features and refactored functionalities, and
verify that they reflect the current state of the game.
- **Evaluate load testing
frameworks:** Adapt to new frameworks as needed to
simulate user load, support new protocols, and align with
the team's expertise and toolchains.
- **Optimize costs:** Start
with managed AWS services for ease and convenience, then
consider self-managing infrastructure for cost savings as
the team grows more comfortable with the load testing
process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops06-bp02.html*

---

# GAMESOPS04 — Health monitoring

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GAMESOPS04-BP01 Instrument the game to detect and monitor player-impacting issues

In addition to responding to social media and player reports of
issues, instrument your game with monitoring solutions to detect
and investigate player-impacting issues.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

No amount of testing can identify every issue in a game. Games are
usually launched with known issues that are planned to be
gradually fixed with the next release of the game. Known and
reproducible issues are straightforward to address and fix. To
assist with identifying such issues, game clients should implement
player activity tracking, app logging, and reporting in various
strategic places to assist the backend team identify client-side
issues. The ability to find such issues early assists the game
developers troubleshoot and fix the issue before it becomes
widespread. The data and logs reported by the tracking code should
never include personally identifiable information (PII), and they
should only contain game specific metadata that assist with
debugging.

Implement an observability solution for detecting and responding
to issues such as game crashes or bugs. You can
use [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to create canaries that can monitor
the health of your player-facing backend game services. You can
instrument your backend services with
[AWS X-Ray](https://aws.amazon.com/xray/) to
trace requests across distributed services, and send your custom
logs and metrics
to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/).

Third-party solutions, such as
[Backtrace.io](http://Backtrace.io/) and
[Sentry](https://sentry.io/welcome/), are
popular solutions for error reporting in games. Application
performance monitoring (APM) solutions from partners such
as [New Relic](https://newrelic.com/),
[Splunk](https://www.splunk.com/en_us/devops/application-performance-monitoring.html),
[Datadog](https://www.datadoghq.com/product/apm/),
and [Honeycomb.io](http://Honeycomb.io/)
are also popular.

The game's live operations team and community managers should also
monitor various social networks and channels to check for player
feedback, complaints, and bug reports in addition to the official
support channels. Review and attempt to reproduce every
game-specific complaint, or send them to the QA team for review.
If reproducible, escalate the issue to the game developers for
their troubleshooting and a fix before it impacts the larger
player base.

### Implementation steps

- **Implement monitoring
solutions:** Use monitoring tools to detect
player-impacting issues and respond quickly.
- **Track player activity and
logs:** Instrument game clients to log player
activity and report issues, and verify that no personally
identifiable information (PII) is included.
- **Use third-party and AWS
tools:** Use tools like CloudWatch, X-Ray, and
third-party solutions for error reporting and performance
monitoring, and monitor social media for player feedback and
bug reports.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesops04-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
