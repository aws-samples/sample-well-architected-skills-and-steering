# ADVPERF04 — Data management design

**Pillar**: Performance Efficiency  
**Best Practices**: 6

---

# ADVPERF04-BP01 Choose a data management strategy that matches your availability, latency, and access requirements

Customers need to have a clear data management strategy for their
advertising workload datastores. The factors to consider are
latency needs, availability needs which will help them chose the
right AWS data service

## Implementation guidance

The following are the most common data stores available in adtech:

- **User data:** Demographic data (age, gender, and
location), behavioral data (browsing history, interests, and purchase history), and
device data (device type, operating system, and browser).
- **Audience data:** Segmentation data (personas and target
audiences) and geo-location data (IP addresses and GPS coordinates).
- **Campaign data:** Ad creative data (like images, videos,
and text), ad placement data (websites, apps, and platforms), and campaign performance
data (impressions, clicks, and conversions)
- **Inventory data:** Publisher data (website or app details
and traffic data) and ad space data (ad sizes, formats, or placements)
- **Pricing and bidding data:** Bid data (bid prices and bid
strategies) and auction data (bid landscape and winning bids).
- **Third-party data:** Data from Data Management Platforms
(DMPs) and data from data exchanges or marketplaces.
- **Analytics and reporting data:** Conversion data (sales,
leads, and actions), attribution data (tracking user journeys), and engagement data
(view-through rates and dwell times)

For latency, consider the following:

- **Low-latency data (real-time or near real-time):** This
data needs to be processed and acted upon within milliseconds to ensure optimal ad
delivery, real-time bidding, and accurate tracking of user interactions.

Bid (bid requests, bid responses, and auction data)
- User (device data, location data, and contextual data)
- Ad impression (ad requests and ad responses)
- Real-time campaign performance (clicks, impressions, and conversions)

- **Medium-latency data (near real-time or batch
processing):** This data can be processed in near real-time (within minutes
or hours) or in batches, as it is used for audience targeting, campaign optimization,
and attribution analysis.

User behavior (browsing history and interests)
- Audience segmentation
- Campaign optimization (performance metrics and engagement data)
- Attribution (user journeys and conversion paths)

- **High-latency data (batch processing or offline):** This
data can be processed in batches or offline, as it is typically used for analysis,
reporting, and long-term decision-making rather than real-time ad delivery or
optimization.

Historical campaign
- Detailed analytics and reporting
- Third-party (from DMPs or data exchanges)
- Ad creative (images and videos)

## Resources

- [Architecture III: Picking the Right Data Store for Your Workload](https://aws.amazon.com/blogs/startups/how-to-pick-the-right-data-store-for-your-workload-1/)
- [Amazon DynamoDB: Ad tech use cases and design patterns](https://aws.amazon.com/blogs/database/amazon-dynamodb-ad-tech-use-cases-and-design-patterns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp01.html*

---

# ADVPERF04-BP02 Consider purpose-built and streaming databases

Purpose-built databases offer low latency and can better meet the
scaling needs of advertising workloads.

## Implementation guidance

Implement low-latency databases with in-memory AWS services
(like [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) or Apache Cassandra) or ISV products specialized
for adtech (like Aerospike).

Implement medium latency data stores with an OLTP database like
[Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/) to implement a multi-Region
availability design.

## Resources

- [Running
Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/)
- [Use
Amazon Aurora Global Database to build resilient multi-Region applications](https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp02.html*

---

# ADVPERF04-BP03 Review your distributed database setup (sharding and replication) for performance, cost, and availability needs

Customers need to consider tradeoffs between performance, cost,
and availability needs, while using features like sharding for
scaling and replication for availability requirements.

## Implementation guidance

Use availability zone affinity in Aerospike to allow client
applications to access Aerospike nodes in the same zone, which
optimizes data transfer across zones.

Distributed databases often support data partitioning or
sharding, which allows you to split your data across multiple
nodes or clusters. This can help distribute the load and optimize cost by reducing the need for high-performance instances or storage
solutions for the entire dataset.

Carefully plan your data replication strategy across
Availability Zones. While replication provides high availability
and durability, replicating data across multiple Availability
Zones can increase costs. Consider replicating only the
essential data or implementing read replicas in different
Availability Zones while keeping the primary node in a single
Availability Zone.

## Key AWS services

- [Amazon RDS](https://aws.amazon.com/rds)

## Resources

- [Architecture
II: Distributed Data Stores](https://aws.amazon.com/blogs/startups/distributed-data-stores-for-mere-mortals/)
- [Building globally distributed MySQL applications using write
forwarding in Amazon Aurora Global Database](https://aws.amazon.com/blogs/database/building-globally-distributed-mysql-applications-using-write-forwarding-in-amazon-aurora-global-database/)
- [Amazon Ads Architecture at Scale - ReInvent 2021](https://www.youtube.com/watch?v=YRbIAmzFxxc)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp03.html*

---

# ADVPERF04-BP04 Enable detailed performance and observability monitoring to help tune queries and refine compute and storage

Provide access to necessary tools and metric granularity for
performance debugging and compute and storage optimization, in
particular because of the low latency requirements for advertising
workloads.

## Implementation guidance

Enable Amazon RDS enhanced monitoring, which provides deeper
visibility into database performance and health. This heightened
visibility helps you diagnose issues faster and optimize
database workloads.

Enable
[Amazon EKS Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html) to provide observability into
cluster health, performance, logs, and billing for container
workloads. This helps you run and optimize Kubernetes
applications efficiently on Amazon EKS while reducing monitoring
costs. The automated dashboards and analytics simplify
troubleshooting.

## Key AWS services

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

## Resources

- [Monitor real-time Amazon RDS OS metrics with flexible granularity
using Enhanced Monitoring](https://aws.amazon.com/blogs/database/monitor-real-time-amazon-rds-os-metrics-with-flexible-granularity-using-enhanced-monitoring/)
- [Optimizing AdTech end-user experiences Using Amazon CloudWatch Internet Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/optimizing-adtech-end-user-experiences-using-amazon-cloudwatch-internet-monitor/)
- [Tuning Amazon RDS for MySQL with Performance
Insights](https://aws.amazon.com/blogs/database/tuning-amazon-rds-for-mysql-with-performance-insights/)
- [Analyze
Amazon Aurora MySQL Workloads with Performance Insights](https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/)
- [Announcing
Amazon CloudWatch Container Insights with Enhanced Observability for Amazon EKS on EC2](https://aws.amazon.com/blogs/mt/new-container-insights-with-enhanced-observability-for-amazon-eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp04.html*

---

# ADVPERF04-BP05 Manage high volume user profile data

The user profile database is typically large, ranging from
100-200 million to 5 billion user profiles and contains a wide
range of data about users' online activities and interactions.
Hence this should be retained for a short time in the range of
30 days -1-year max, to manage data storage costs and data query
latency SLO’s.

## Implementation guidance

Use an in-memory database with a data cache strategy using
Amazon MemoryDB.

Avoid replicating user profile data across multiple Regions due
to high latency and data transfer costs. We recommend storing user profiles
local to the user.

In the event of multi-Region architecture, implement
synchronization between periodically (for example, once or twice a day)
rather than in real-time, as users are unlikely to be in two
locations at once. Advertisers also often use geotargeting, so a
user's profile may only be accessed from the Region the user is
located in for a particular ad campaign.

## Key AWS services

- Amazon MemoryDB

## Resources

- [Observability best practices for Amazon Memory DB for Valke](https://aws.amazon.com/blogs/database/monitor-server-side-latency-for-amazon-memorydb-for-valkey/)y

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp05.html*

---

# ADVPERF04-BP06 Consider AWS Clean Rooms collaboration

AWS Clean Rooms have limits on query result size (for example,
AWS Clean Rooms has a 5GB limit), so consider using
aggregations and filters to reduce result sets.

## Implementation guidance

Large datasets can impact query performance.
Partition data effectively.

A higher number of collaborators in a collaboration channel
impacts processing time. Consider this as one of the
factors for designing the collaboration framework with
collaborators in play.

AWS Clean Rooms offers analysis templates work to support parameterized queries assisting in performance improvement through query reuse. Optimize queries before creating templates.
Consider the choice of cryptographic operations for secure computation, as it adds to processing time.

## Key AWS services

- AWS Clean Rooms

## Resources

- [Guidelines for the C3R encryption client](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-guidelines.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp06.html*

---
