# GAMEPERF02 — Region selection

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GAMEPERF02-BP01 Select a home Region that is near your players

For an initial game launch, you should determine where to deploy
infrastructure based on discussions with your business
stakeholders, such as publishing teams who determine where the
game is expected to be made available to players, and where they
are focusing their pre-launch marketing and advertising efforts.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Your business stakeholders should also have mechanisms to
stimulate demand to gain a better understanding of player
reception and viability. For example, these teams will have
mechanisms such as game pre-orders, marketing events and
campaigns, public email lists for players to register interest
before launch, and other approaches to establish relevant signals
to determine where the game will likely have the most players at
launch. The game may also use a regional roll out strategy that
includes play test and soft-launch phases to determine regional
player demand.

[Select
a home Region](https://aws.amazon.com/about-aws/global-infrastructure/) that is near your player base and your
developers and has the AWS services and features you need to host
your game. The home RSegion will be where the game backend
services will run, and it may also run game servers. Evaluate a
home Region based on services supported, connectivity to edge
locations, proximity to failover Regions, and number of
Availability Zones. If you are using a Local Zone, consider the
parent Region is sometimes located in a different geographic area.
As an example: Santiago, Chile Local Zone us-east-1-scl-1a has N.
Virginia us-east-1 as its parent Region even though it is
geographically closer to Sao Paulo sa-east-1.

### Implementation steps

- Identify deployment Regions based on player demand signals
from pre-launch activities like pre-orders, marketing
campaigns, and interest registrations.
- Choose a home Region close to the primary player base and
developers, making sure it supports required AWS services,
edge locations, and failover Regions.
- Evaluate Local Zones carefully, considering that the parent
Region may differ geographically from the location of the
Local Zone.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf02-bp01.html*

---

# GAMEPERF02-BP02 Design an approach that supports placing latency-sensitive game infrastructure close to players to improve performance

Separate placement for latency sensitive infrastructure like game
servers minimizes the impact of long network routes. Repeatable
deployments can make it simple to maintain multiple locations that
are more performant for your players. Ping is a common metric that
is surfaced in game UI and low ping can be a differentiating
capability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When first launching a game, you may not yet have enough
information about your player base to adequately know where best
to deploy infrastructure closest to the players that are most
interested in playing your game. This is a common challenge, and
you should prepare for this scenario by designing an architecture
that allows you to rapidly adjust your hosting placement strategy
to deploy servers where they are needed closer to players. It is
typical for game developers to regularly assess their game
infrastructure deployment as a recurring post-launch analysis to
incrementally invest in improvements over time with an iterative
approach.

A best practice is to use infrastructure-as-code templates, such
as AWS CloudFormation or Terraform by Hashicorp, for the
configuration of your infrastructure such as VPCs, subnet
configurations, and dependencies required to launch critical game
services so that you can refer to these templates, quickly
customize them if needed, and deploy them into locations where
additional infrastructure is needed to support your players.

You should also make sure you understand how your current
deployment strategy could be evolved to allow future expansion.
IaC templates are repeatable but are not a substitute for network
planning.
[IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
manages your VPCs. Subnet sizing, Availability Zone selection, and
IP inventory and cross-account Availability Zone alignment. The
network is important to consider and can be disruptive to players
when changed. Game servers deployed across multiple geographic
locations will connect to your game backend, which is more common
to be hosted in a single or multiple home Regions which can
require additional configuration to support private connectivity.
These considerations should be continuously evaluated over time so
that you can make changes to your game hosting strategy as your
game's requirements evolve or your player requirements change.

When determining how many game hosting locations to use for your
game, consider the following factors:

- **Quality of player experience
improvement:** How much of a player experience
improvement can you introduce by adding additional game
hosting locations? What is the incremental performance gain
that you can achieve by doing so? How will you measure this
performance improvement?
- **Which player populations to
prioritize:** How many players can you improve the
experience for if you add additional game hosting locations?
Which player populations, or geographic locations, will you
prioritize?
- **Downstream impacts of
change:** If you change your game hosting strategy,
how will this influence your matchmaking wait times for
players? Can the match sizes, skill balance or number of
players in the player pool accommodate a game hosting location
strategy change? Supporting more locations can potentially
fragment the player pool and add increased cost and
complexity.

Each of these considerations should be evaluated as you determine
where you add or remove game hosting locations. For example, you
may choose to prioritize improving the experience for players in
geographic locations with the least performant gameplay
experience, or for players who express the most vocal public
feedback. You may also choose to factor the player monetization
into your priorities, for example by focusing attention on
improving the experience for players in geographic locations that
generate a significant source of revenue for your game or have the
potential to generate incremental revenue if you introduce
performance improvements.

In addition to hosting infrastructure in AWS Regions, you can use
[Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), which are an extension of an AWS Region, to host
your game servers and other latency sensitive applications such as
voice chat servers closer to your players. You might also choose
to run game development infrastructure in Local Zones to improve
the experience for your game development teams. For example, you
can use Local Zones to address use cases such as hosting replicas
of your self-managed source control servers closer to your game
developers, and to offer game development virtual workstations and
content storage to users using Amazon EC2 instances, EBS volumes,
and Amazon FSx file systems deployed into one or more Local Zones
near your development studios without requiring you to host the
infrastructure on-premises.

[Outposts](https://aws.amazon.com/outposts/)
are a good choice when Regions or Local Zones are not available in
the same geographic area. Connectivity from your data center to
AWS should be considered to enable game server to backend system
reliability. AWS Outposts and Outpost Servers are purpose-built to
run AWS in your datacenter using the same services and APIs to
help create a consistent deployment model wherever you run your
game. Multiple racks can be combined into a logical Outpost, and
the infrastructure can be shared across AWS accounts. The hardware
lifecycle is managed by AWS and the lead time can be as short as 3
months.

If you are building games using containers and want the flexibility
to adopt a hybrid deployment architecture using open-source
software that can be deployed on your own on-premise
infrastructure, you can use
[ECS
Anywhere](https://aws.amazon.com/ecs/anywhere/), or
[EKS
Anywhere](https://aws.amazon.com/eks/eks-anywhere/) as an alternative to AWS Outposts or Local Zones.
If you host with Amazon GameLift;
[Amazon
GameLift Anywhere can be used to run your server build on local
hardware](https://aws.amazon.com/blogs/gametech/hybrid-game-server-hosting-with-amazon-gamelift-anywhere/) which can speed up your development process,
enabling you to use Local Zones or register your own metal as part
of the your fleet.

### Implementation steps

- Use infrastructure-as-code tools like AWS CloudFormation or
Terraform for repeatable deployments, enabling quick
customization and scaling of game hosting locations based on
player needs.
- Evaluate player experience improvements, player population
priorities, and downstream impacts such as matchmaking times
when adding or removing game hosting locations.
- Use AWS Local Zones, Outposts, or hybrid options like ECS
Anywhere, EKS Anywhere, or GameLift Anywhere to optimize
latency-sensitive infrastructure and support diverse
deployment needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf02-bp02.html*

---
