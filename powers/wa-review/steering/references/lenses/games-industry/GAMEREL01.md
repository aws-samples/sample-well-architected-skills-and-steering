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
