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
