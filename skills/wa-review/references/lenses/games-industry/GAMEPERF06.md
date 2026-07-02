# GAMEPERF06 — Data management

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# GAMEPERF06-BP01 Centralize log collection and storage

Implement a centralized log collection and storage solution to gather logs from game server
instances and GameLift.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Use services like Amazon CloudWatch Logs to collect, monitor, and store log data from your game
servers and GameLift instances. CloudWatch Logs provides a scalable and fully managed solution for log
management, facilitating efficient storage and retrieval of log data without impacting game
server performance. If you are running the [CloudWatch Logs agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html), consider the
various install types and configuration options like batch size, buffer duration to minimize
impact to the game server. Consider the game server instances ephemeral and reduce dependency
on localized logging where possible. Establish a centralized policy for implementation of
[Logging best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-best-practices.html).

### Implementation steps

- Use Amazon CloudWatch Logs to collect, monitor, and store log data from game server instances
and GameLift, facilitating centralized and scalable log management.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp01.html*

---

# GAMEPERF06-BP02 Categorize and store game data based on access patterns

Categorize your game data into different types based on their
access patterns and storage requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Common categories
include player data, game saves, persistent world storage, and
analytics data.

### Implementation steps

Use appropriate storage solutions for each data type to optimize
performance and cost-efficiency:

- **Player data:** Use Amazon DynamoDB, a fast and scalable NoSQL database, to store
player profiles, preferences, and progression data. The
low-latency access and automatic scaling capabilities of
DynamoDB provide efficient retrieval and update of player
data.
- **Game saves:** Use Amazon S3
to store game saves and checkpoints. S3 provides high
durability and scalability for storing large amounts of game
save data. Consider using S3 Transfer Acceleration or Amazon CloudFront for faster uploads and downloads of game saves.
- **Persistent world storage:**
For games with persistent world states or shared game data,
consider using Amazon DynamoDB, Amazon ElastiCache or Amazon MemoryDB. ElastiCache and MemoryDB provide in-memory
key-value store while DynamoDB is an SSD backed NoSQL
database. These services provide fast access to stored data,
reducing the time it takes for the game server process to
save game state which improves overall process performance.
- **Analytics data:** Use
Amazon Managed Streaming for Apache Kafka or Kinesis Data Streams
to ingest data streams from your game data producers. Amazon
Managed Service for Apache Flink can be used for real-time
transformation and analysis and sent to Amazon Data Firehose
for processing and delivery into backend data lakes,
warehouses and analytics services.
[Guidance
for Game Analytics Pipeline on AWS](https://aws.amazon.com/solutions/guidance/game-analytics-pipeline-on-aws/) illustrates how
the services work together to provide near real-time and
batch analytics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp02.html*

---

# GAMEPERF06-BP03 Enable efficient log formatting and batching

Configure your game server processes to generate logs in a structured and in a format that
can be parsed, such as JSON.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implement log batching techniques to minimize the frequency of log data transfers from
your game servers to the centralized log storage. Batching logs reduces network overhead and
improves game server performance. Use verbose or debug level logs as an exception and not a
default, as they can incur a performance and cost penalty that should be avoided when
possible.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp03.html*

---

# GAMEPERF06-BP04 Implement log rotation and retention policies

Establish log rotation and retention policies to manage the growth
of log data and optimize storage utilization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Configure your game
servers to automatically rotate logs based on size or time
intervals. Define log retention policies in Amazon CloudWatch Logs
to automatically archive or delete older log data that is no
longer needed for active analysis or troubleshooting.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp04.html*

---

# GAMEPERF06-BP05 Use monitoring and visualization tools

Use monitoring and visualization tools to gain insights into your
game server performance and identify optimization opportunities.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use Amazon CloudWatch to monitor key metrics and set up alarms for
proactive notifications. Utilize tools like Amazon Managed Service for Prometheus and Amazon Managed Grafana to collect,
query, and visualize metrics from your game servers and
infrastructure. Create informative dashboards to track
performance, identify bottlenecks, and make data-driven
optimizations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf06-bp05.html*

---
