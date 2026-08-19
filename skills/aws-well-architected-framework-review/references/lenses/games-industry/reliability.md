# Reliability

**Pillar**: Reliability  
**Questions**: 3

---

# GAMEREL01 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# GAMEREL01-BP01 Distribute game infrastructure across multiple Availability Zones and Regions to improve resiliency

To minimize the impact of localized infrastructure impairments on
your players, you should distribute your infrastructure deployment
uniformly across enough independent locations to be able to
withstand unexpected impairments while still having enough
capacity to meet the needs of your player demand.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When deploying your game infrastructure, it is recommended to
uniformly distribute your capacity across multiple Availability
Zones in a Region so that you can withstand disruptions to one or
more Availability Zones without disrupting the player experience.
Game backend services such as web applications should be load
balanced across multiple Availability Zones or should be built
using managed service such as AWS Lambda and Amazon API Gateway
which provide Regional high availability by design. Similarly,
components that maintain state such as caches, databases, message
queues, and storage solutions should be designed to provide
durable persistence of data across multiple Availability Zones,
which is provided by design in services such as Amazon S3,
DynamoDB, and Amazon SQS, and can be configured in other services.

When designing your game server hosting architecture for
resiliency, deploy your fleets of game servers uniformly across
the Availability Zones within an AWS Region to maximize your
access to available compute capacity in the Region as well as
reduce the impact scope of Availability Zone impairments. For
example, you can
configure [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html) to use the Availability Zones. If an EC2
instance becomes unhealthy, EC2 Auto Scaling can replace the
instance, as well as launch instances into other Availability
Zones if one or more of the Availability Zones becomes
unavailable.

For critical infrastructure, such as authentication, provision a
minimum number of viable instances running across multiple
Availability Zones, and use auto scaling to handle load increases
or fault tolerance if there is an impairment with one of the
Availability Zones.

Deploy your game infrastructure into multiple Regions to maximize
availability. Cross-Regional disaster recovery features like
Aurora global databases and redundant infrastructure that can
become active with a simple DNS change deployed into a secondary
Region can provide service continuity should the primary Region
become impaired. While we encourage this for your game backend
services to achieve high availability, this recommendation is
especially important for your game servers.

For example, in a multiplayer game, your infrastructure capacity
for game servers is likely to outpace the capacity needs for your
other services, since game servers are used to host game sessions
for players. Many games choose to shard players into logical game
Regions (like US west and east). To simplify the player experience
and make it straightforward to use global infrastructure to host
games, consider de-coupling the name of your player-facing game
Regions from the underlying cloud provider Region or data center
location that is physically hosting the game servers, along with
other infrastructure such as Local Zones or your own data centers
that are hosting game server instances supporting that player game
Region.

When designing your matchmaking service, deploy a multi-Region
architecture with separate software deployments across Regions.
Decouple your matchmaking service deployment from the fleets that
host your game server instances so that you can route players to a
game server in Regions regardless of which regional deployment of
your matchmaking service handled the matchmaking request.

Design logic in your matchmaking implementation to favor the game
server Regions that meet your latency and other rules, with the
ability to fallback to routing players to other Regions if your
fleets are low on capacity or there are other regional
infrastructure disruptions.

### Implementation steps

- Distribute game infrastructure uniformly across multiple
Availability Zones to provide high availability and
resilience.
- Deploy game backend services and stateful components using
managed like AWS Lambda, Amazon S3, DynamoDB, and SQS, or
configure load balancing and durability for custom
solutions.
- Implement multi-Region deployments for critical game
services and servers, using disaster recovery solutions like
Aurora global databases and logical player-facing Regions
decoupled from underlying physical locations.

### Resources

- [Static
stability](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/static-stability.html)
- [Best
practices for Amazon GameLift game session queues](https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-best-practices.html)
- [Amazon
GameLift Multi-Region fleets](https://aws.amazon.com/blogs/gametech/amazon-gamelift-is-now-easier-to-manage-fleets-across-regions/)
- [Aurora
Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) for Disaster Recovery

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel01-bp01.html*

---

# GAMEREL02 — Change management

**Pillar**: Reliability  
**Best Practices**: 2

---

# GAMEREL02-BP01 Implement a scaling strategy that incorporates the state of active player game sessions

Implement a solution for automatically scaling your game
infrastructure in a manner that incorporates the stateful nature
of your actively connected player sessions and gracefully handles
scaling activities without disrupting gameplay.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

One of advantages of developing a game in the cloud is the
elasticity that can be achieved by automatically scaling server
infrastructure as needed to meet demand. While stateless or
asynchronous games and backend services can be dynamically scaled
using [Amazon EC2 Auto Scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html),
[EKS
autoscaling](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html), or similar techniques typically adopted for
scalable web applications, game developers typically require a
more customized approach for scaling stateful or synchronous games
to help block disruptions to active player sessions.

### Implementation steps

- For stateful games, generate custom metrics that can be used
to monitor the state of your player sessions and available
game server capacity, which can be reported to Amazon CloudWatch as custom metrics. Exercise features with
application monitoring, such as CloudWatch Synthetics,
checking the game for impairment of functions that simple up
and down health monitoring may not detect.
- Using custom metrics, implement game server scaling
software, for example, as a serverless application using AWS Lambda function or AWS Fargate, to manage the fleet of
dedicated game server instances by using the AWS SDK to make
API calls to update the minimum, maximum, and desired
capacity settings for the
EC2 [Auto
Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroup.html) hosting your game server build.
- Use Amazon GameLift to host your game servers and use
the [out-of-the-box
game server auto scaling capabilities](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-manage-capacity.html) to manage this
scaling process for you.

The automatic scaling capabilities of Amazon GameLift are aware
of active player sessions and can be configured to block the
termination or scale-in of game server instances that are
actively hosting players. For more information,
see [Monitor
Amazon GameLift Servers with Amazon CloudWatch](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel02-bp01.html*

---

# GAMEREL02-BP02 Support the use of multiple EC2 instance types for your game

When hosting your game using EC2 instances, or if you use
containers hosted on EC2 instances in your AWS account, use
multiple instance types in your hosting strategy. By using
multiple instance types, you can increase the number of compute
options that can be used when your game is scaling to add more
servers to support player growth, which improves reliability in
case your preferred instance type is unavailable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When hosting your game using Spot Instances, use multiple instance
types since the availability of Spot Instances fluctuates based on
customer demand.

Test your game on multiple instance types to meet your cost and
performance requirements and determine a prioritized ranking of
instance types. Amazon EC2 Auto Scaling supports using multiple
instance types and sizes as well
as [assigning
weights to each instance type](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html) in your configuration so that
you can implement prioritized ranking of compute options.

When hosting your game using Amazon GameLift managed hosting,
decide what type of instances your game needs and how to run game
server processes on them (using a runtime configuration). When
choosing resources for a fleet, consider several factors,
including game operating system, instance type (the computing
hardware), and whether to use On-Demand Instances, Spot Instances,
or both. Hosting costs with Amazon GameLift primarily depend on
the type of instances you use. For more information,
see [Choose
compute resources for a managed fleet](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-compute.html).

### Implementation steps

- Use multiple EC2 instance types to improve reliability and
scaling options when hosting your game on EC2 or containers.
- Configure Amazon EC2 Auto Scaling or GameLift fleets with
prioritized instance types and weights to optimize cost and
performance.
- Test your game on various instance types to verify that
performance meets requirements and adjust your hosting
strategy
accordingly***.***

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel02-bp02.html*

---

# GAMEREL03 — Failure management

**Pillar**: Reliability  
**Best Practices**: 3

---

# GAMEREL03-BP01 Monitor game server disruptions, and use the data to improve hosting architecture to achieve reliability goals

Monitor game server metrics and the impact of failures or
degradations in performance, such as increased latency under load,
on player behavior over time so that you can adjust your game
server hosting strategy to meet your game's reliability
requirements. Game server infrastructure to be degraded should be
removed from service immediately if it is impacting players or
proactively replaced when there are no active player sessions
hosted on the server.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For scenarios where games are hosted as REST APIs, system
reliability can be managed like traditional web application
architectures, where traffic can be load balanced across multiple
servers in a distributed manner to mitigate the risk of server
failures.

For real-time synchronous gameplay, a game session is usually
hosted on a game server process running on a virtual machine, or
game server instance, since gameplay state needs to be maintained
in a performant manner and replicated to connected game clients.
This implementation means that a player's experience is tightly
coupled to the performance and reliability of the game server
process that hosts their game session. This type of architecture
makes managing the reliability of game servers more complex than
traditional approaches.

To mitigate the impact of a game server failure, configure your
game to continuously perform asynchronous updates of a player's
game state to a highly-available cache or database such
as [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/)
or [Amazon MemoryDB](https://aws.amazon.com/memorydb/). If a server failure occurs, the
player's last saved game state can be fetched from the external
data store, and their session can be restored on a new game server
instance.

However, this approach adds additional cost and complexity to
manage this external state, and may not be suitable for fast-paced
or competitive games where the state changes are so frequent and
happening at such a significant scale that introducing even a
performant in-memory cache data store would result in replication
lag that is too significant to be useful to restore a session
from. For games of this nature, the optimal approach is to accept
the loss of the server and send the player back to a game lobby to
find another session or you can automatically redirect them into
another game session.

Capture as much useful log data about what caused the server
disruption so that you can investigate the issue later. Amazon
GameLift provides guidance
for [debugging
fleet issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html) and provides the ability
to [remotely
access Amazon GameLift fleet instances](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-remote-access.html) .

### Implementation steps

- Monitor game server metrics for performance degradations,
and remove or replace degraded servers as necessary to
maintain reliability.
- Use Amazon ElastiCache or MemoryDB for asynchronous game
state updates to enable session recovery after server
failures when feasible.
- Capture detailed log data on server disruptions for
investigation and debugging, leveraging tools like Amazon
GameLift for fleet monitoring and remote access.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel03-bp01.html*

---

# GAMEREL03-BP02 Implement loose coupling of game features to handle failures with minimal impact to player experience

Decoupling components refers to the concept of designing server
components so that they can operate as independently as possible.
Some aspects of gaming are difficult to decouple since data needs
to be as up to date as possible to provide a good in-game
experience for players. However, many components and gaming tasks
can be decoupled. For example, leaderboards and stats services are
not critical to the gameplay experience, and the reads and writes
to these services can be performed asynchronously from the game.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implement graceful degradation for features in your game that can
be disabled automatically or by an administrator if issues are
detected, as well as configure upstream services that depend on
the feature to be able to gracefully handle the failure. For
example, if specific player data is not properly loading within
your game client, you should consider whether this data is
critical to the gameplay experience. If not, configure the game
client to gracefully handle this failure without disrupting the
experience for the player, optioning to retry fetching this data
later when the player revisits the screen.

Employ logic such as timeouts, retries, and backoff to handle
errors and failures. Timeouts keep systems from hanging for
unreasonably long periods. Retries can provide high availability
of transient and random errors.

Define non-critical components which can be loosely coupled to
critical components. Loose coupling allows systems to be more
resilient since failure in one component does not cascade to
others. When game features do not require stateful connections to
your game servers or backend, you should implement stateless
protocols to scale dynamically and recover from transient
failures. Develop your non-critical components where it can be
loosely coupled with stateless protocols using an HTTP/JSON API.
Implement network calls from the game client to be asynchronous
and non-blocking to minimize the impact to players from
slow-performing game features or other dependent services.

To further improve resiliency through loose coupling, use a
messaging service such as a queuing, streaming, or a topic-based
system between components that can be handled asynchronously. This
model is suitable for an interaction that does not require an
immediate response or where an acknowledgment that a request has
been registered is sufficient. This solution involves one
component that generates events and another that consumes them.
The two components will not integrate through direct
point-to-point interaction but through an intermediate such as a
durable storage or queuing layer. This also assists to improve
system's reliability by preserving messages when processing fails.

Research and select an appropriate messaging mechanism, as various
messaging services have different characteristics, such as
ordering and delivery mechanisms. Design operations to be
idempotent so the chosen message system delivers messages at least
once. As an example, consider a typical game use case where your
game needs to track player playtime, stats, or other relevant data
which can lead to a high write-throughput use case at times of
peak player concurrency.

To implement a reliable architecture, consider whether the use
case requires read-after-write consistency as perceived by the
player. Typically, scenarios such as these are suitable for
asynchronous processing and can be achieved by implementing a
write-queueing pattern where the requests are ingested into a
scalable and durable message queue such as Amazon SQS and can be
inserted into your backend database in batches using a consumer
service, such as a Lambda function. This approach is more reliable
than synchronous communication between multiple distributed
components including the player's game client, your backend web
and application servers, and your internal database system. It
also reduces costs because the backend database does not need to
be scaled to meet peak write throughput since the consumer
processing from the write queue can be used to slow down this
ingestion rate as needed.

### Implementation steps

- Decouple non-critical components like leaderboards and stats
services from critical gameplay features to allow
asynchronous operations and enhance resiliency.
- Implement graceful degradation for non-critical features
with logic for timeouts, retries, and backoff, and verify
that the game client handles failures without disrupting the
player experience.
- Use messaging systems like Amazon SQS for asynchronous
communication between components, enabling scalable,
durable, and reliable processing of high throughput use
cases.

### Resources

- [Build
highly scalable and reliable workloads using microservice
architecture](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-service-architecture.html)
- [Integrating
microservices by using AWS serverless services](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/welcome.html)
- [Understanding
asynchronous messaging for microservices](https://aws.amazon.com/blogs/compute/understanding-asynchronous-messaging-for-microservices/)
- [Introduction
to Scalable Game Development Patterns on AWS](https://d1.awsstatic.com/whitepapers/aws-scalable-gaming-patterns.pdf)
- Implementing
[Graceful
Degradation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html#:~:text=Implementing%20graceful%20degradation%20helps%20minimize%20the%20impact%20of,means%20considering%20potential%20failure%20modes%20during%20dependency%20design.)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel03-bp02.html*

---

# GAMEREL03-BP03 Monitor infrastructure events over time to measure impact on player behavior

Monitor your game server process, game server instance metrics,
and game experience metrics to determine the root cause of issues.
In addition to monitoring CPU and memory, you can also set up
monitoring for network metrics related to network limitations of
EC2 instances to alert you of issues such as exceeding bandwidth,
packets-per-second, or other network-level issues that may
indicate your server resources are under provisioned.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use CloudWatch Synthetics to check critical path application
functionality for player experience, such as being unable to login
or other service impacting issues. For game servers hosted using
Amazon GameLift, consider monitoring
[metrics](https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html)
like:

- GameServerInterruptions and InstanceInterruptions, which can
assist in understanding how limitations in Spot instance
availability are impacting your game servers deployed using
Spot.
- ServerProcessAbnormalTerminations, which can be used to detect
abnormal terminations in your game server processes.

It is recommended to maintain historical metrics data of your game
server reliability. Use this historical data for reporting
purposes and join it with other datasets to uncover potential
trends and assess the impact on player behavior over time that may
be due to game server issues.

Amazon CloudWatch does not retain metrics indefinitely, and
the [storage
resolution of metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) is increased over time, so consider
exporting these metrics to cost-effective long-term storage such
as Amazon S3. You can
configure [CloudWatch
Metric Streams](https://aws.amazon.com/blogs/aws/cloudwatch-metric-streams-send-aws-metrics-to-partners-and-to-your-apps-in-real-time/) to automatically deliver your metrics from
[CloudWatch
Regions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Cross-Account-Methods.html) to your own S3 bucket, where they can be stored
long-term in a storage tier such as S3 Intelligent-Tiering and
eventually archived using Amazon Glacier. By placing your
metrics in Amazon S3, they are readily available to be joined with
other datasets in your data lake for interactive querying
with [Amazon Athena](https://aws.amazon.com/athena/).

### Implementation steps

- Monitor game server, instance, and network metrics,
including bandwidth and packet-per-second limits, using
Amazon CloudWatch and CloudWatch Synthetics for critical
path functionality checks.
- Track GameLift-specific metrics like
*GameServerInterruptions* and
*ServerProcessAbnormalTerminations* to
assess the impact of Spot instance availability and detect
abnormal server terminations.
- Export CloudWatch metrics to Amazon S3 for long-term
storage, use cost-effective tiers like S3
Intelligent-Tiering or Glacier, and analyze trends with
tools like Amazon Athena.

### Resources

- [Amazon EC2 instance-level network performance metrics uncover new
insights](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-ec2-instance-level-network-performance-metrics-uncover-new-insights/)
- [CloudWatch
Metric Streams – Send AWS Metrics to Partners and to Your
Apps in Real Time](https://aws.amazon.com/blogs/aws/cloudwatch-metric-streams-send-aws-metrics-to-partners-and-to-your-apps-in-real-time/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamerel03-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
