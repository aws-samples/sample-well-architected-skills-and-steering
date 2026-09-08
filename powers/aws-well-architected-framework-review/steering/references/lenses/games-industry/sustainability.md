# Sustainability

**Pillar**: Sustainability  
**Questions**: 2

---

# GAMESUS01 — Data management

**Pillar**: Sustainability  
**Best Practices**: 2

---

# GAMESUS01-BP01 Use storage technologies that fit the patterns adapted to user content, subscriber information, and in-game purchases

You should classify your data by type, retention need and frequency
of access. This enables you to select the most optimized storage
solution for the myriad data types of your game or backend services
produce. Fast changing data should be stored in key-value or
in-memory database services. Transactional data should be store in
relational database services. Large files, game assets, or
user-generated content should be stored in object storage services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Games produce and consume a large variety of data types that
require storage solutions optimized for frequency of access,
latency, and cost. Data stored should be classified using tags to
differentiate data that can be removed or needs to be stored
long-term.

The following services work well for a variety of Games use-cases:

[Amazon Aurora](https://aws.amazon.com/rds/aurora/) (compatible with MySQL and PostgreSQL) offers high
availability, low-latency, and automatic scaling, making it an
excellent choice for handling large amounts of transactional data,
such as player account management and authentication, in-game
economies, leaderboards and player rankings, game state
persistence, event and campaign management, and multi-Region and
high-availability deployment.

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) is a fully managed NoSQL database known for its
low-latency, high throughput, and seamless scalability, which
makes it ideal for handling real-time player data, session
management, inventory, in-game economy, real-time multiplayer game
state, matchmaking, event logging, and scaling for global
audience.

[Amazon DocumentDB](https://aws.amazon.com/documentdb/) (compatible with MongoDB) provides a scalable,
low-latency document-oriented database service, perfect for
storing flexible, semi-structured data, such as inventory system,
player profiles and customization's, game worlds and procedurally
generated content, social and player interactions, analytics and
behavior tracking, and in-game metadata and configurations.

[Amazon ElastiCache](https://aws.amazon.com/elasticache/) supports in-memory caching with Redis or
Memcached, offering rapid data access and reduced response times,
which is critical for real-time multiplayer games where speed and
performance are essential for a smooth user experience.
ElastiCache is utilized in gaming for real-time leaderboards,
session management, caching game metadata, in-game chat and
messaging, matchmaking, real-time analytics and telemetry, and
scaling for high-traffic events.

[Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/?nc=sn&loc=0) can be used to store objects
like game assets, videos, pictures, text log files and more. S3 is
an object storage service offering industry-leading scalability,
data availability, security, and performance.

If it offers multiple storage classes that support frequent and
in-frequent data access, and cost-effective archive storage. For
data that is frequently accessed throughout development, studios
should store objects in
[S3
Standard](https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3) for low latency and high throughput performance.
For data that frequently goes from hot to cold or vice versa,
studios should investigate
[S3
Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/). Intelligent-Tiering monitors the
access patterns of your data and automatically moves data to the
most cost-effective access tier.

For studios that need high throughput, low latency and are ok with
it living in a single Availability Zone use
[S3
Express One Zone.](https://aws.amazon.com/s3/storage-classes/express-one-zone/) This replicates data to a single AZ and
can improve data access speeds compared to S3 standard. For deep
archive needs of historical data Amazon also offers
[Amazon Glacier.](https://aws.amazon.com/s3/storage-classes/glacier/) The Amazon Glacier storage classes are
purpose-built for data archiving, providing you with high
performance, retrieval flexibility, and low cost archive storage
in the cloud.

[Amazon Elastic Block Store](https://aws.amazon.com/ebs/) can be used to store game servers' binaries,
executable files and configurations your game servers or asset
repositories need to function. You should snapshot and delete
unused volumes that are not attached to an EC2 instance. This
alleviates you from storage charges incurred while lowering the
usage of unneeded services and hardware.

### Implementation steps

- Classify game data by type, retention needs, and access
frequency, tagging data to distinguish between short-term
and long-term storage requirements.
- Use Amazon Aurora for transactional data, DynamoDB for
real-time player data, DocumentDB for semi-structured data,
and ElastiCache for low-latency caching of time-critical
game information.
- Store game assets, logs, and user-generated content in
Amazon S3, selecting appropriate storage classes (for
example, Intelligent-Tiering, One Zone, and Glacier) based
on access patterns and archive needs, and use EBS for game
server binaries and configurations with regular snapshot
management.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesus01-bp01.html*

---

# GAMESUS01-BP02 Use lifecycle policies or TTL expiration to delete unnecessary games user data, log files, or deprecated assets

You can use tags and data type to create lifecycle policies or TTL's
to move data to archival storage or remove completely from the
service. This may include temporary configurations, expired archived
content, and historical logs that are no longer needed. Most
services support tagging.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For data stored in S3 you can use lifecycle policies to move the
data to infrequent access and archival tiers of storage. In an S3
Lifecycle configuration, you can define rules to transition
objects from one storage class to another to save on storage
costs. When you don't know the access patterns of your objects, or
if your access patterns are changing over time, you can transition
the objects to the S3 Intelligent-Tiering storage class for
automatic cost savings.

Amazon S3 supports a waterfall model for transitioning between
storage classes, as shown in the following diagram.

You can add transition actions to an S3 Lifecycle configuration to
tell Amazon S3 to delete objects at the end of their lifetime.
When an object reaches the end of its lifetime based on its
lifecycle configuration, Amazon S3 takes an Expiration action
based on which S3 Versioning state the bucket is in:

- **Non-versioned bucket:**
Amazon S3 queues the object for removal and removes it
asynchronously, permanently removing the object.
- **Versioning-enabled bucket:**
If the current object version is not a delete marker, Amazon S3 adds a delete marker with a unique version ID. This makes
the current version noncurrent, and the delete marker the
current version.
- **Versioning-suspended
bucket:** Amazon S3 creates a delete marker with null
as the version ID. This delete marker replaces an object
version with a null version ID in the version hierarchy, which
effectively deletes the object.
- When you add a Lifecycle configuration to a bucket, the
configuration rules apply to both existing objects and objects
that you add later. For example, if you add a Lifecycle
configuration rule today with an expiration action that causes
objects with a specific prefix to expire 30 days after
creation, Amazon S3 will queue for removal existing objects
that are more than 30 days old and that have the specified
prefix.

Time To Live (TTL) for DynamoDB is a cost-effective method for
deleting items that are no longer relevant. TTL allows you to
define a per-item expiration timestamp that indicates when an item
is no longer needed. DynamoDB automatically deletes expired items
within a few days of their expiration time, without consuming
write throughput.

- To use TTL, first enable it on a table and then define a
specific attribute to store the TTL expiration timestamp. The
timestamp must be stored in
[Unix
epoch time format](https://en.wikipedia.org/wiki/Unix_time) at the seconds granularity. Each time
an item is created or updated, you can compute the expiration
time and save it in the TTL attribute.
- Items with valid, expired TTL attributes may be deleted by the
system, typically within a few days of their expiration. You
can still update the expired items that are pending deletion,
including changing or removing their TTL attributes. While
updating an expired item, we recommended that you use a
condition expression to make sure the item has not been
subsequently deleted. Use filter expressions to remove expired
items from
[Scan](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.FilterExpression)
and
[Query](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.FilterExpression.html)
results.
- Deleted items work similarly to those deleted through typical
delete operations. Once deleted, items go into DynamoDB
Streams as service deletions instead of user deletes and are
removed from local secondary indexes and global secondary
indexes just like other delete operations.

With ElastiCache for Redis you can control the freshness of your
cached data by using TTLs or expiration on cached keys. After the
set time has passed, the key is deleted from the cache, and access
to the origin data store is required along with reaching the
updated data.

- Two principles determine the appropriate TTLs to apply and the
types of caching patterns to implement. First, it's important
that you understand the rate of change of the underlying data.
Second, it's important that you evaluate the risk of outdated
data being returned to your application instead of its updated
counterpart.
- With dynamic data that changes often, you might want to apply
lower TTLs that expire the data at a rate of change that
matches that of the primary database. This lowers the risk of
returning outdated data while still providing a buffer to
offload database requests.
- It's also important to recognize that, even if you are only
caching data for minutes or seconds versus longer durations,
appropriately applying TTLs to your cached keys can result in
a performance boost and an overall better player experience
with your game.

### Implementation steps

- Use Amazon S3 Lifecycle policies to transition objects to
infrequent access or archival tiers and configure expiration
actions to delete unnecessary objects based on lifecycle
rules.
- Enable Time to Live (TTL) in DynamoDB tables to
automatically delete expired items without consuming write
throughput, defining the expiration timestamp in Unix epoch
time.
- Set appropriate TTLs for ElastiCache keys based on data
change rates and risk tolerance for outdated data,
facilitating cached data freshness and improved player
experience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesus01-bp02.html*

---

# GAMESUS02 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 2

---

# GAMESUS02-BP01 Select managed services for appropriate compute workloads

Architect your game backend services to use managed services for
event driven or highly variable traffic workloads. Managed services
shift the management of infrastructure to AWS and distributes the
environmental impact across multiple users because of the
multi-tenanted control planes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS services like AWS Lambda, AWS Fargate (Containers), and Amazon
Gamelift (Game server orchestration) can run code, containers, or
orchestrate your game servers without having to manage the
underlying infrastructure. These services automatically scale
based on player demand and you're only charged for the resources
you consume. Because the underlying infrastructure is managed on
your behalf, you are able to focus solely on your games and
backend services' requirements.

You can use [AWS Lambda](https://aws.amazon.com/lambda/) to run code without provisioning or managing
servers. Lambda runs your code on a high-availability compute
infrastructure and performs the administration of the compute
resources, including server and operating system maintenance,
capacity provisioning and automatic scaling, and logging. With
Lambda, you need to supply your code in one of the language
runtimes that Lambda supports. Lambda is useful for processing
game events, player authentication, in-game purchase processing,
and matchmaking requests. Lambda automatically scales based on the
number of events and can handle unexpected spikes in traffic.

[AWS Fargate](https://aws.amazon.com/fargate/?nc=sn&loc=0) is a serverless compute engine for containers that
works with both
[Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (ECS) and
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS). AWS Fargate makes it
straightforward to focus on building your applications by
alleviating the need to provision and manage servers, lets you
specify and pay for resources per application, and improves
security through application isolation by design. Fargate is ideal
for backend services that handle player profiles, state management
and matchmaking.

[Amazon
GameLift](https://aws.amazon.com/gamelift/) is a managed service for deploying, operating, and
scaling dedicated game servers for session-based multiplayer
games. You can deploy your first game server in the cloud in just
minutes, saving up to thousands of engineering hours in upfront
software development and lowering the technical risks that often
cause developers to cut multiplayer features from their designs.

### Implementation steps

- Use AWS Lambda for event-driven workloads like processing
game events, player authentication, in-game purchases, and
matchmaking requests, leveraging its automatic scaling and
serverless management.
- Deploy AWS Fargate with ECS or EKS for backend services such
as player profiles, state management, and matchmaking,
removing server management and improving application
isolation.
- Use Amazon GameLift to deploy and scale dedicated game
servers for session-based multiplayer games, reducing
development time and operational complexity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesus02-bp01.html*

---

# GAMESUS02-BP02 Right-size your compute and deploy GPU performance only where needed

Architect your game servers and backend to efficiently utilize
compute resources. Over-provisioning compute can lead to unnecessary
costs and minimizes the amount of idle or under-utilized resources.
GPU instances should be used to support specific development efforts
like HLOD rebuilds in Unreal, or if you game servers require them by
design. This greatly reduces the environmental impact and costs of
your workloads.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You should optimize your game servers and backend services to use
multiple EC2 instances types and the least number of instances
needed. This increases the number of instances available to meet
your needs during development or for your games launch. You should
also match the instance type to the specific workload you're
deploying. Compute Optimized instances support a wide range of
use-cases including game servers and backend services like
matchmaking. Memory Optimized instances are designed to deliver
fast performance for workloads that process large data sets in
memory. Use GPU instances as required for high performance
requirements, but not for general computing tasks. If able,
architect your services or game servers to run on ARM with
[AWS Graviton instances](https://aws.amazon.com/ec2/graviton/). Graviton is the most performant to
energy efficient instance type available on AWS. They also offer
improved performance and costs when compared to x86 instance
types.

Use the
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify the optimal AWS resource
configurations, such as Amazon Elastic Compute Cloud (EC2)
instance types, Amazon Elastic Block Store (EBS) volume
configurations, task sizes of Amazon Elastic Container Service
(ECS) services on AWS Fargate, commercial software licenses, AWS Lambda function memory sizes, and Amazon Relational Database Service (RDS) DB instance classes, using machine learning to
analyze historical utilization metrics. Compute Optimizer provides
a set of APIs and a console experience to reduce costs and
increase workload performance by recommending the optimal AWS
resources for your AWS workloads.

### Implementation steps

- Match compute resources to specific workloads by using
Compute Optimized instances for game servers, Memory
Optimized instances for large data sets, and GPU instances
only for tasks like HLOD rebuilds or GPU-dependent game
servers.
- Optimize compute utilization by deploying AWS Graviton
instances where possible for energy efficiency, better
performance, and cost savings compared to x86 instances.
- Use AWS Compute Optimizer to analyze historical utilization
and recommend the most efficient configurations for EC2, AWS
ECS, AWS Lambda, and Amazon RDS workloads to reduce costs
and improve performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesus02-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
