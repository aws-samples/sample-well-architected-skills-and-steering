# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 3

---

# GAMECOST01 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# GAMECOST01-BP01 Implement attribution of cost per player, game feature, and environment

Cost attribution for game servers is usually simpler to perform than
game backend services because a game server is usually optimized to
be able to host a specific number of concurrent players per instance
which can be amortized across the cost of running the instance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For game backend services, it is recommended to de-couple the
components of your game into distinct features that can be managed
as separate logical or physical resources to make it
straightforward to analyze costs.

For example, although it may seem straightforward to implement a
single monolithic application to host game backend services, this
pattern makes it hard to derive the total cost per player and game
feature over time as you add more features because the compute,
networking, and storage costs of resources are shared across the
features. Consider adopting a serverless architecture for your
game backend services with services such as
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) and AWS Lambda or AWS Fargate for compute,
[Amazon SQS](https://aws.amazon.com/sqs/)
and [Amazon SNS](https://aws.amazon.com/sns/) for messaging, Amazon S3 for object storage, and Amazon DynamoDB for database storage. These services are just a few
examples of products that offer pricing that is usage-based and
primarily driven by request volume so that costs can be visualized
with granularity. Individual resources such as Lambda functions,
Fargate services, DynamoDB tables, and S3 buckets can be
associated with cost allocation tags so that you can attribute the
costs of these services with game feature names that make it
straightforward for you to understand the costs for each of your
services.

It is also recommended to separately manage each of your game
development environments so that you can attribute costs for the
different environments. Typically, game developers will manage
separate environments for development, test, staging and
production environments, as described in the operations pillar of
this games industry lens. Each environment usually has different
scalability, performance, and usage requirements and may be
managed by separate teams. To control costs, organize these
environments so that you can properly monitor and attribute the
costs of each environment.

For more information, refer to the following documentation:

- [Building
a serverless multi-player game that scales](https://aws.amazon.com/blogs/compute/building-a-serverless-multiplayer-game-that-scales/)
- [Standalone
game session servers with a WebSockets-based backend](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_websockets.html)
- [Standalone
game session servers with a serverless backend](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_serverless.html)

### Implementation steps

- De-couple game backend services into distinct features using
serverless or containerized architectures like AWS Lambda,
Amazon API Gateway, and AWS Fargate to enable granular cost
attribution per feature.
- Apply cost allocation tags to individual resources (for
example, Lambda functions, DynamoDB tables, and S3 buckets)
to associate costs with specific game features for better
cost analysis.
- Manage separate environments for development, testing,
staging, and production, organizing and monitoring their
costs independently to align with scalability and usage
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost01-bp01.html*

---

# GAMECOST01-BP02 Discover opportunities for optimization

Game developers and publishers can use AWS FinOps practices to help
optimize their cloud costs and gain better visibility into their
cloud spending. By doing so, game producers can align the average
cost required to maintain infrastructure for the players with the
financial results delivered by the game.

**Level of risk exposed if this best practice
is not established**: Low

## Implementation guidance

AWS offers a ready to use
[solution
guidance for Cloud Financial Management](https://aws.amazon.com/solutions/guidance/cloud-financial-management-on-aws/) to manage and
optimize your expenses for cloud services. This capability
includes granular visibility and cost and usage analysis to
support decision-making for topics such as spend dashboards,
optimization, spend limits, charge back, and anomaly detection and
response. The solution guidance for Cloud Financial Management
includes budget and forecasting features, giving you a defined,
cost-optimized architecture for your workloads so you can select
the right pricing model and attribute resource costs relevant to
your teams. This activates tracking, notification, and cost
optimization techniques across your environment and resources. You
can centrally manage expense information and give critical
stakeholders access as needed for targeted visibility and to
support decision-making.

Another key FinOps tool is the
[Cost
Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html), which provides a centralized view of cost
optimization recommendations and opportunities across your AWS accounts and AWS Regions, so that you can get the most out of your
AWS spend. You can use Cost Optimization Hub to identify, filter,
and aggregate AWS cost optimization recommendations across your
AWS accounts and AWS Regions. It makes recommendations on resource
rightsizing, idle resource deletion, Savings Plans, and Reserved
Instances. With a single dashboard, you avoid having to go to
multiple AWS products to identify cost optimization opportunities.

If your games teams are using shared AWS accounts the
[myApplications
in AWS Management Console Home](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/aws-myApplications.html), can be used to view application
resource costs for individual workloads. This granular view allows
you to identify the specific cost trends within your game
infrastructure, enabling you to make informed decisions about
resource allocation and optimization.

Additionally, regularly reviewing your billing and cost management
data with
[AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) uncovers hidden cost savings opportunities.
This detailed report provides a comprehensive breakdown of your
cloud spending, allowing you to identify areas of overspending,
unutilized resources, and opportunities to take advantage of more
cost-effective services or pricing models.

By embracing FinOps principles and leveraging the tools provided
by AWS, game developers and publishers can make the most efficient
use of their cloud resources, ultimately enhancing their bottom
line and freeing up funds for further game development and
innovation.

### Implementation steps

- Use AWS Cloud Financial Management tools for granular and
detailed visibility, spend dashboards, anomaly detection,
and cost attribution to optimize and track cloud expenses
effectively.
- Use the Cost Optimization Hub to centralize rightsizing,
Savings Plans, and Reserved Instance recommendations across
AWS accounts and Regions.
- Regularly review AWS billing data using Data Exports and
MyApplication on AWS to help analyze workload-specific
costs, uncover savings opportunities, and optimize resource
allocation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost01-bp02.html*

---

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

# GAMECOST03 — Data transfer costs

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# GAMECOST03-BP01 Choose the appropriate type of storage for user generated content to reduce costs

Each type of data generated and stored in your game has unique
characteristics that you should consider when determining the right
storage solution for your workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Use Amazon S3 Object Lifecycle Management to store object data in
the most cost-effective storage class. Amazon S3 provides multiple
[storage
classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) and
[object
lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to make it straightforward to set up
simple and fine-grained policies to automatically transition data
between storage tiers to reduce costs. Instead of simply storing
data in the S3 standard storage class by default, consider setting
up a lifecycle configuration to transition data between tiers
automatically over time, or use S3 Intelligent-Tiering storage
class for unknown or changing access patterns.

Alternatively, S3 Intelligent-Tiering can cost-effectively and
automatically transition data between tiers and is recommended as
a default storage class since it provides cost optimization
without the need to manually setup lifecycle policies, and is now
the best choice for small and short-lived objects. For more
information, see
[Amazon S3 Intelligent-Tiering – Improved Cost Optimizations for
Short-Lived and Small Objects](https://aws.amazon.com/blogs/aws/amazon-s3-intelligent-tiering-further-automating-cost-savings-for-short-lived-and-small-objects/).

Common use cases for Amazon S3 include storage of game assets,
static content, game logs, data lake storage, and backups. For use
cases where file systems are required, such as attaching shared
file systems to workstations during development, consider using
[Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html), which provides different
storage classes and automatically grows and shrinks as you add and
remove files with no need for manage the infrastructure.

[Amazon S3 One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-infreq-data-access)-IA is an ideal storage option for transient
data related to in-game sessions, matchmaking, or other ephemeral
information that can be re-created as needed. That type of game
data does not require redundancy across multiple Availability
Zones (AZs). This lower-cost storage class is well-suited for
records of player actions, game events, and other telemetry data
used for analytics or debugging.

The key cost optimization benefit of using S3 Express One Zone for
such game data is the significant cost savings compared to the
standard S3 storage class, with up to a 20% reduction in storage
costs. This can be particularly advantageous for games with large
volumes of data that do not require the same level of durability
and availability as mission-critical application data. By
leveraging S3 One Zone, game developers and publishers can
optimize their cloud storage costs without compromising the
overall player experience.

### Implementation steps

- Configure Amazon S3 lifecycle policies to transition data
between storage classes or use S3 Intelligent-Tiering as a
default for automatic cost optimization with changing access
patterns.
- Use S3 One Zone-Infrequent Access for transient game session
data, such as telemetry and matchmaking records, to reduce
storage costs by up to 20% while maintaining sufficient
availability.
- For shared file system needs during development, use Amazon EFS to simplify storage management with elastic capacity and
multiple storage classes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost03-bp01.html*

---

# GAMECOST03-BP02 Optimize databases for game backends

Games rely heavily on databases to store a wide range of critical
data, from player profiles and inventories to in-game micro
transactions and progression metrics. Databases also play a crucial
role in managing the social aspects of games, such as creating and
maintaining player groups, parties, and enforcing moderation
policies. As the player base of a game grows, the associated
database costs will inevitably rise to accommodate the increasing
data and usage demands.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

For game backends running on Amazon Aurora, there are several cost
optimization strategies that can be employed. One key
recommendation is to
[auto
scale your read replicas based on usage patterns](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html),
dynamically scaling the number of replicas up or down to handle
fluctuations in traffic. This means that you are paying for the
resources you truly need. Another optimization tactic is to
replace read replicas used for games analytics with DB snapshots
exports to Amazon S3, as the S3 storage service is generally more
affordable than provisioned Aurora database instances. For more
information, see
[Exporting
DB snapshot data to Amazon S3 for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ExportSnapshot.html).

Exploring the use of
[Reserved
DB instances for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithReservedDBInstances.html) for your core database
instances and transitioning to the
[Aurora
Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) configuration can also lead to substantial
long-term cost savings by providing more flexibility and
[granular
control over your resource utilization](https://www.youtube.com/watch?v=ecRje2wFO14).

Similarly, for game backends that use Amazon DynamoDB, employing
the
[DynamoDB
on-demand capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html) can be an effective choice,
especially for new or unpredictable workloads, as it allows you to
pay only for the resources you consume without the need to
over-provision. As your game traffic patterns become more stable
and predictable over time, you can then transition to the
[DynamoDB
provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html), which can offer cost savings
through better capacity planning. Activating auto-scaling on your
DynamoDB tables is another key optimization, allowing the service
to dynamically adjust the provisioned capacity based on
fluctuations in traffic. Test your game's data structure in a
development environment before launch to find and remove
unnecessary
[local
secondary indexes (LSIs)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LSI.html) and
[global
secondary indexes (GSIs)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html). This can lead to substantial cost
savings for game data storage and operations. Removing
[inefficient
Scan operations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html) from your game backend code in favor of
more targeted queries, purchasing
[Amazon DynamoDB reserved capacity](https://aws.amazon.com/dynamodb/reserved-capacity/), and leveraging
[DynamoDB
Streams with AWS Lambda triggers](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html) to process game backend
events can further optimize your DynamoDB costs. For more
information, see
[Best
practices for querying and scanning data in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-query-scan.html).

By implementing these cost optimization strategies for both Amazon Aurora and DynamoDB, game developers and publishers can
significantly reduce their game backend databases spend.

### Implementation steps

- Use Aurora read replica auto-scaling and DB snapshot exports
to Amazon S3 for cost-efficient handling of fluctuating
traffic and analytics needs.
- Optimize DynamoDB costs by starting with on-demand capacity
for new workloads, transitioning to provisioned capacity
with auto-scaling for predictable traffic, and removing
unused LSIs and GSIs.
- Avoid inefficient Scan operations in favor of targeted
queries, use Reserved Instances or Reserved Capacity, and
use DynamoDB Streams with AWS Lambda for event processing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost03-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
