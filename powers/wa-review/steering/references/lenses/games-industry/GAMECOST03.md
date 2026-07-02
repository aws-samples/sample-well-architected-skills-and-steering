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
