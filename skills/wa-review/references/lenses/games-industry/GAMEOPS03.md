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
