# GAMECOST02 — Cost-effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# GAMECOST02-BP01 Optimize the cost of data transfer across the internet

While AWS primarily charges for outbound (egress) data transfer from
your AWS resources to the internet, game companies can face high
costs related to data transfer through AWS Direct Connect or AWS
Gateway load balancers, which may charge for both inbound (ingress)
and outbound data. Implement solutions that reduce the overall cost
of transferring data from your game's AWS backend to your players,
focusing on minimizing egress charges from your AWS resources as
well as evaluating options to manage ingress and egress fees through
AWS connectivity services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use Amazon CloudFront to reduce the cost of content delivery and
public-facing web applications.

Game content and assets that are stored in the cloud are typically
stored in Amazon S3 and delivered to the game client either
directly from S3 or from web servers hosted in Amazon EC2 that
retrieve the content from Amazon S3 and deliver it to clients. To
reduce the data transfer costs of content downloads, consider
using Amazon CloudFront in front of your cloud storage to deliver
content to users.

Using CloudFront can reduce the cost of data transfer because it
costs less to deliver your content from CloudFront
points-of-presence than directly from Regions, and CloudFront does
not charge origin retrieval fees for AWS-based origins, such as
Amazon EC2 and Amazon S3. If your content is static and does not
change often, you can use CloudFront to cache that data closer to
end-users, which can further reduce costs.

CloudFront also improves the cost efficiency of front-facing
public-facing web applications and services, even if caching is
not used, since the cost of data transfer between your servers and
clients can be reduced by routing traffic through the AWS network.

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/monitoring-using-cloudwatch.html) can be used to monitor your Amazon CloudFront
usage. For use cases where you use multiple content delivery
networks (CDNs),
[Amazon CloudFront Origin Shield](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html) can provide an additional layer of
caching to consolidate and reduce the number of origin requests
from different providers.

To understand your game network traffic, you can enable
[VPC
Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and
[Amazon CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-InternetMonitor.html) to have end-to-end visibility
on player or game backend connections. That approach can identify
the causes for high data transfer cost and perform architectural
changes to optimize data transfer spend.

### Implementation steps

- Use Amazon CloudFront in front of Amazon S3 or EC2-based
content origins to reduce data transfer costs by leveraging
lower-cost delivery from CloudFront points-of-presence and
removing origin retrieval fees.
- Enable VPC Flow Logs and Amazon CloudWatch Internet Monitor
to analyze network traffic and identify architectural
changes to optimize data transfer costs.
- Implement CloudFront Origin Shield to consolidate and reduce
origin requests when using multiple CDNs for additional cost
efficiency.

For more best practices for content delivery, see the
[Content
Delivery for Games whitepaper](https://d1.awsstatic.com/whitepapers/content-delivery-for-games.pdf).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost02-bp01.html*

---

# GAMECOST02-BP02 Optimize the number of game sessions hosted on each game server instance to optimize costs

Optimize the number of game sessions hosted per server instance to
achieve better compute utilization and reduce compute infrastructure
costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To optimize costs, game developers should maximize the number of
game sessions hosted on the same physical or virtual server, also
known as the packing density of their game servers. This is
achieved by increasing the number of game server processes that
can be simultaneously hosted on an instance.

A single game server process should not usually require the use of
the entire resources available on the EC2 instance. This is one of
the most important ways to reduce compute costs for a game and
requires the use of software that can spawn and manage multiple
server processes on the EC2 Instance on separate ports.

For example, Amazon GameLift has a quota on the maximum number of
game server processes per instance, which you should strive to
utilize so that you can reduce hosting costs. For more
information, see
[Amazon
GameLift Servers endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/gamelift.html) for details on the
current quota for maximum game server processes per instance.

As an alternative to deploying game server processes on virtual
machines such as EC2 instances, it is becoming popular for game
developers to run their game servers as container-based
applications using container orchestration solutions. Game
developers can use
[Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) or
[Guidance
for Game Server Hosting Using Agones and Open Match on Amazon EKS](https://aws.amazon.com/solutions/guidance/game-server-hosting-using-agones-and-open-match-on-amazon-eks/). Another option is
[Game
Server Hosting on AWS Fargate](https://aws.amazon.com/blogs/gametech/game-server-hosting-on-aws-fargate/), a serverless compute engine
that works with both ECS and EKS, enabling you to focus on your
game without having to manage the underlying infrastructure.

Container solutions provide job scheduling functionality that can
automatically find an available container instance in the cluster
to host your game server container based on resource requirements
and other placement logic that you specify. However, it is
important to consider how you will manage the scaling and player
placement behavior in a way that doesn't disrupt active player
sessions.

### Implementation steps

- Increase packing density by running multiple game server
processes per EC2 instance using separate ports and process
management software.
- Use Amazon GameLift or container solutions like ECS, EKS, or
AWS Fargate to manage game server processes efficiently and
reduce infrastructure costs.
- Continuously monitor resource utilization to refine packing
density and maintain cost-efficiency without compromising
player experience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost02-bp02.html*

---

# GAMECOST02-BP03 Select the appropriate compute pricing option to reduce costs

Run performance tests of your game server software across a
variety of instance types and compute options to determine which
option is most cost-effective for your game.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

In addition to efficiently utilizing the right EC2 instance types
for your workload, consider which of the available compute pricing
options is most suitable for your cost optimization goals. There
are several pricing options available, including On-Demand
Instances, Spot Instances, Reserved Instances, and Savings Plans.

[Savings Plans](https://aws.amazon.com/savingsplans) (SPs) provide discounts for compute by making usage
commitments and are ideal for scenarios when you cannot forecast
your expected usage for a 1-year or 3-year period. They provide
discounts like Reserved Instances with the flexibility to apply
these discounts across Regions, instance family, operating system,
tenancy. They can also be applied to AWS Fargate, who can be a
game server hosting option for casual games or AWS Lambda who is
used as a great option for turn-based game that do not require
game servers. For more information, see
[Building
a serverless multi-player game that scales](https://aws.amazon.com/blogs/compute/building-a-serverless-multiplayer-game-that-scales/).

Savings Plans are introduced during game launches to save costs
for game servers workloads that are contributing to EC2 instances
spend when the game is released to the audience. Savings Plans can
also be introduced post-launch when game operations team have a
better understanding of the player traffic after the game has been
running in production for an extended period.

Since Savings Plans provide regional flexibility, they are
particularly ideal to optimize game servers spend for games with
unpredictable usage across geographies.

For example, if your daily player usage pattern requires at least
20 servers to support your player base, but periodically requires
up to 40 servers, then consider purchasing Savings Plan
commitments to cover the 20 servers' baseline, because that usage
demand is predictable and consistent, and will result in maximum
utilization of the usage commitment that you have purchased.

Maximize the utilization of Savings Plans and augment them with
other purchase options that provide more flexibility for
unpredictable game server usage spikes, such as on-demand and Spot
Instances to achieve optimal savings.

Spot Instances are ideal for running game servers because they
offer the largest compute discounts, do not require usage
commitments, and they provide flexibility for unpredictable and
spiky workload types. However, Spot Instances can be interrupted,
so they are best suited for game server workloads with short game
session duration or situations where the tolerance for
interruption is higher.

For more information on guidance for running game servers using
Kubernetes on Amazon EKS with EC2 Spot Instances, see
[How
to run massively multiplayer games with EC2 Spot using Aurora
Serverless](https://aws.amazon.com/blogs/compute/how-to-run-massively-multiplayer-games-with-ec2-spot-using-aurora-serverless/).

Use
[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/instance-advisor/) to determine pools with the least chance
of interruption that will deliver maximum savings compared to
on-demand rates.

When using Spot, it is also recommended to run game server
workloads across multiple EC2 instance types and Availability
Zones in an AWS Region to diversify your usage of capacity and
reduce interruption risk.

Consider using Spot Instances in combination with On-Demand
Instances to minimize the impact of potential disruptions to
active game sessions and use capacity optimized allocations
strategy to further reduce the risk of interruption.

Refer to the
[Best
practices for Amazon EC2 Spot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-best-practices.html) for additional best
practices.
[Capacity
Rebalancing in Auto Scaling to replace at-risk Spot
Instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-capacity-rebalancing.html) can be used to proactively monitor and add
additional capacity when Spot Instances are at increased risk of
interruption.

[Amazon
GameLift FleetIQ](https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html) integrates with Spot Instances to optimize
the use of low-cost Spot Instances while reducing the risk of
interruptions. If you are hosting your game using GameLift, review
the GameLift documentation for choosing computing resources. For
more information, see
[Choose
compute resources for a managed fleet](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/gamelift-compute.html).

The following diagram provides an example to illustrate the use of
multiple compute pricing options for game server workloads:

*Hosting game servers with multiple EC2
pricing options*

In the diagram, the player concurrency fluctuates over time which
makes it difficult to manage utilization and achieve cost
optimization. To address this fluctuation, consider adopting a
mixture of different compute pricing options, using Savings Plans
for EC2 to meet the needs of your minimum usage requirements while
relying on EC2 On-Demand and EC2 Spot Instances to meet the needs
of your player demand.

### Implementation steps

- Use Savings Plans for predictable baseline usage, combining
them with Spot and On-Demand Instances for flexibility and
cost optimization during usage spikes.
- Use Spot Instances for game servers with short session
durations or higher interruption tolerance, diversifying
across instance types and Availability Zones to minimize
risk.
- Implement tools like EC2 Spot Instances Advisor, Capacity
Rebalancing, and GameLift FleetIQ to optimize Spot Instance
usage and proactively manage interruptions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost02-bp03.html*

---
