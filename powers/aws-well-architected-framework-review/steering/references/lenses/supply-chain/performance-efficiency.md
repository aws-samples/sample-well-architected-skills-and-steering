# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 5

---

# SCPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# SCPERF01-BP01 Use internal and external risk to determine performance requirements

External regulatory or supplier systems, as well as internal risk
requirements, are often a good place to start for performance
requirements. For certain systems, regulators release sector-wide
guidance and data residency rules and regulators require that
system have the capability to deliver on the operational
resilience and the performance targets they have set for
themselves.

**Desired**
**outcome:** You can achieve best
end-user performance irrespective of the data residency rules due
to the regulatory requirements.

**Benefits of establishing this best
practice:** Low latency, best end-user experience, and
low risk of violating data regulations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

External regulatory or supplier systems, as well as internal
risk requirements, are often a good place to start for
performance requirements. For certain systems, regulators
release sector-wide guidance and data residency rules and
regulators require that system have the capability to deliver on
the operational resilience and the performance targets they have
set for themselves. If the systems update the supplier database
or connected to their network to pull data, the performance
targets should be taken into consideration.

### Implementation steps

- Identify all relevant regulatory requirements and data
residency rules that apply to your supply chain systems.
- Analyze supplier system performance requirements and
integration points that may impact overall system
performance.
- Establish performance baselines based on regulatory
guidance and internal risk assessments.
- Define performance targets that balance compliance
requirements with operational efficiency.
- Implement monitoring and alerting systems to track
performance against established targets.
- Regularly review and update performance requirements as
regulations and business needs evolve.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf01-bp01.html*

---

# SCPERF01-BP02 Factor in rate of increase in load, traffic, and scale-out intervals

Identify the upper bounds of the peak load against a system, as
well as the amount of time needed to reach peak load. Load tests
often overlook the rate of increase in traffic and create tests
that scale up too quickly or too slowly.

**Desired**
**outcome:** You mimic the traffic
and load situation of the system and see how the user experience
in such situations, this will help to fine-tune the underlying
resources of the architecture to achieve better results.

**Benefits of establishing this best
practice:** System resiliency prediction, and system
behavior during peak hours/loads.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Identify the upper bounds of the peak load against a system, as
well as the amount of time needed to reach peak load. Load tests
often overlook the rate of increase in traffic and create tests
that scale up too quickly or too slowly. If the load test ramps
up too quickly, the system may not be able to add capacity
rapidly enough to meet the demand, which degrades performance
and introduces errors. Load tests need to be run periodically
and with every major release of the system or when new systems
or architecture is introduced in the supply chain eco-system.

### Implementation steps

- Analyze historical traffic patterns to identify peak load
periods and growth rates specific to supply chain
operations.
- Design load tests that accurately simulate realistic
traffic ramp-up patterns based on actual usage scenarios.
- Establish automated scaling policies that can respond
appropriately to gradual and sudden load increases.
- Implement comprehensive monitoring during load tests to
identify performance bottlenecks and capacity constraints.
- Create regular load testing schedules that coincide with
major system releases and supply chain system
integrations.
- Document and analyze load test results to continuously
improve system performance and scaling capabilities.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf01-bp02.html*

---

# SCPERF02 — Compute selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# SCPERF02-BP01 Use serverless compute to run tasks

Choosing the correct compute power for the workload provides
smooth performance of the application, not only for the end users
also for the solution developer community to maintain the software
stacks across various infrastructures.

**Desired outcome:** Smooth
performance that elastic in nature with low upkeep.

**Benefits of establishing this best
practice:** Improved user experience, maintenance of
software stack, and scalability.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Some supply chain services computing workloads, like supplier
data visibility, are typically loosely coupled and can benefit
from event-driven architectures using the scaling capacity of
AWS serverless compute options like AWS Lambda and AWS Fargate,
combined with messaging services including Amazon SQS and Amazon EventBridge to decouple components. These serverless solutions
minimize the overhead of capacity management, automatically
scaling in or out to meet demands. Where scale is the primary
factor, AWS serverless container compute engine AWS Fargate, can
be used with both Amazon Elastic Container Service (Amazon ECS)
and Amazon Elastic Kubernetes Service (Amazon EKS), removing the
overhead of managing and provisioning compute resources.

### Implementation steps

- Identify supply chain workloads that are suitable for
serverless architectures, focusing on event-driven and
loosely coupled processes.
- Implement AWS Lambda functions for lightweight,
short-duration tasks such as data processing and API
integrations.
- Deploy AWS Fargate for containerized workloads that
require more control over the runtime environment while
maintaining serverless benefits.
- Integrate messaging services like Amazon SQS and Amazon EventBridge to decouple components and enable asynchronous
processing.
- Configure auto-scaling policies to automatically adjust
compute resources based on demand patterns and workload
requirements.
- Monitor performance metrics and optimize function
configurations to facilitate efficient resource
utilization and cost-effectiveness.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp01.html*

---

# SCPERF02-BP02 Use machine learning capabilities for supply chain applications

AWS Supply Chain unifies data and provides machine
learning--powered actionable insights, built-in contextual
collaboration, and demand planning.

**Desired**
**outcome:** High requirement
workloads can be made easier using machine learning capabilities.
Certain pre-built algorithms can reused to fit your workflow which
can save time for building the right solutions.

**Benefits of establishing this best
practice:** Agility, performance, and re-usability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use
[AWS Supply Chain](https://aws.amazon.com/aws-supply-chain/) to reduce the heavy lifting of the
workloads, which involves deep machine learning skills and
time-consuming algorithm development activities.

### Implementation steps

- Evaluate existing supply chain processes to identify
opportunities where machine learning can provide value and
improve efficiency.
- Implement AWS Supply Chain to use pre-built machine
learning models for demand forecasting and supply
planning.
- Integrate machine learning capabilities with existing
supply chain systems to enhance decision-making and
automation.
- Train teams on machine learning tools and best practices
to maximize the value of AI-powered supply chain
solutions.
- Monitor machine learning model performance and
continuously refine algorithms based on actual business
outcomes.
- Expand machine learning usage to additional supply chain
use cases as capabilities and confidence grow.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp02.html*

---

# SCPERF02-BP03 Use edge compute capabilities for supply chain applications

AWS offers a robust suite of edge computing solutions that extend
cloud capabilities closer to end users, devices, and on-premises
locations. At the core of AWS's edge computing strategy are two
main services: AWS Outposts and AWS Local Zones.

**Desired**
**outcome:** These edge compute
capabilities enable a single-digit millisecond latency for
applications like supply chain which needs real-time edge data to
perform machine learning inferences and action autonomously
without pushing the decision making at the cloud.

**Benefits of establishing this best
practice:** Agility, performance, and low latency.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

AWS offers a robust suite of edge computing solutions that
extend cloud capabilities closer to end users, devices, and
on-premises locations. At the core of AWS's edge computing
strategy are two main services: AWS Outposts and AWS Local
Zones. AWS Outposts brings native AWS services, infrastructure,
and operating models to virtually any datacenter or on-premises
facility. It's ideal for workloads requiring low latency access
to on-premises systems, local data processing, or data residency
requirements. AWS Local Zones are infrastructure deployments
that place compute, storage, database, and other AWS services
closer to large population and industry centers. Local Zones act
as an extension of an AWS Region, connected through
high-bandwidth, secure connections.

### Implementation steps

- Assess supply chain operations to identify use cases that
require low-latency processing or local data residency.
- Deploy AWS Outposts for on-premises workloads that need
AWS services with local data processing capabilities.
- Implement AWS Local Zones for applications requiring
ultra-low latency access to end users or manufacturing
facilities.
- Configure AWS IoT Greengrass for edge devices to enable
local data processing and autonomous decision-making
capabilities.
- Establish secure connectivity between edge locations and
central cloud infrastructure to maintain data
synchronization.
- Monitor edge computing performance and optimize resource
allocation to facilitate efficient operation across
distributed locations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp03.html*

---

# SCPERF03 — Database and storage selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# SCPERF03-BP01 Select your database architecture based on workload

Purpose-built data storage for your workloads can help increase
the performance efficiency of the overall system, as well to be
more resilient in case of failures.

**Desired outcome:** Purpose-built
data storage. Increased performance efficiency of the overall
system.

**Benefits of establishing this best
practice:** Scalability, resilience, and end user
performance improvement.

**Level of risk exposed if this best
practice is not established:** High.

## Implementation guidance

Select database options that align with your performance
requirements, using different database technologies for
different purposes, such as Amazon Timestream time-series
database for storing ticking market data, rather than a
one-size-fits-all use of traditional relational databases. Also,
Amazon RDS is a straightforward relational database service
optimized for total cost of ownership. It is simple to set up,
operate, and scale with demand. Amazon RDS automates the
undifferentiated database management tasks, such as
provisioning, configuring, backups, and patching.

### Implementation steps

- Analyze supply chain data access patterns and performance
requirements to determine optimal database architectures.
- Implement purpose-built databases for specific use cases,
such as time-series databases for IoT sensor data and
document databases for product catalogs.
- Configure Amazon RDS for transactional supply chain data
that requires ACID compliance and complex queries.
- Deploy NoSQL databases like Amazon DynamoDB for
high-throughput, low-latency applications such as
inventory tracking.
- Establish database performance monitoring and optimization
processes to maintain continued efficiency as data volumes
grow.
- Implement automated backup and disaster recovery
strategies to maintain data availability and business
continuity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf03-bp01.html*

---

# SCPERF03-BP02 Select your storage architecture based on workload

Data lineage is important in the world of producers and consumers
of the data. This lineage can be verified and validated when it is
tracked from the source system to the destination systems. As a
result, well-organized data leads to better understanding.

**Desired outcome:** Well-organized
data with improved understanding.

**Benefits of establishing this best
practice:** Data lineage, scalability, resilience, and
re-usability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS Supply Chian needs a data lake with AI/ML models for supply
chains to understand, extract, and transform disparate,
incompatible data into a unified data model. The data lake can
ingest your data from various data sources, including your
existing ERP systems, such as SAP S/4HANA, and supply chain
management systems. To add data from variable sources such as
EDI 856, some applications use AI/ML and natural language
processing (NLP) to associate data from source systems to the
unified data model. EDI 850 and 860 messages are transformed
directly with predefined but customizable transformation
recipes.

### Implementation steps

- Design a data lake architecture using Amazon S3 to store
diverse supply chain data from multiple sources and
formats.
- Implement data ingestion pipelines using AWS Glue to
extract, transform, and load data from ERP systems and
supply chain applications.
- Configure AI/ML models to process and standardize
disparate data formats, including EDI messages and
unstructured documents.
- Establish data lineage tracking mechanisms to maintain
visibility into data flow from source systems to
destination applications.
- Implement data governance policies and access controls to
maintain data quality and security across the storage
architecture.
- Create automated data validation and quality monitoring
processes to maintain data integrity throughout the supply
chain environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf03-bp02.html*

---

# SCPERF03-BP03 Use cache memory to help improve the performance

Cache memory provides improved latency of the application when
accessed outside of the solution-hosted Regions.

**Desired outcome:** Low latency of
the application when accessed outside of designated Regions.

**Benefits of establishing this best
practice:** Better throughput, low latency, reduced power
consumption, improved reliability, and increased scalability.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

While considering using the cache memory for your supply chain
solutions, you can architect the solution to use caching
services to improve performance. Store frequently used data in
memory or bring the data closer to consumers. Many AWS services
offer features for caching or dedicated services including
Amazon ElastiCache, and Amazon File Cache. For example,
frequently accessed inventory data should be stored in cache
memory, with time-to-live (TTL) settings configured to align
with the data's update frequency and usage patterns. In this
case, data caching solutions (Redis Cache or MemoryDB) are
important to quickly access last available data with low latency
(200 milliseconds or less) interval.

### Implementation steps

- Identify frequently accessed supply chain data that would
benefit from caching, such as inventory levels, product
information, and pricing data.
- Implement Amazon ElastiCache with Redis or Memcached to
cache frequently accessed data and reduce database load.
- Configure appropriate TTL settings for cached data based
on update frequency and business requirements for data
freshness.
- Deploy Amazon CloudFront for caching static content and
API responses to improve global access performance.
- Implement cache invalidation strategies to maintain data
consistency when underlying data changes.
- Monitor cache performance metrics and optimize cache
configurations to maximize hit rates and minimize latency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf03-bp03.html*

---

# SCPERF04 — Network architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# SCPERF04-BP01 Use performance requirements to drive the selection of network components and architecture

Bring the hosted solution closer to your users' Region to provide
a better user experience and make the data safer while hosted or
in transit.

**Desired outcome:** Better user
experience and safer data while at rest or in transit.

**Benefits of establishing this best
practice:** Secured data while hosted or in-transit, and
low latency by using Amazon backbone network and infrastructure.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use AWS Direct Connect to provide the shortest and most reliable
path to AWS resources for components hosted outside of AWS. Use
Amazon CloudFront to cache static content closer to use cases,
and AWS Global Accelerator to route connections to the closest
possible source, using the AWS backbone network and bringing
your solutions closer to industries, users, and data. When using
multiple AWS Regions, use Route 53 latency-based routing to
serve requests from the AWS Region with the lowest latency.

### Implementation steps

- Analyze network performance requirements and identify
optimal AWS regions based on user and supplier locations.
- Implement AWS Direct Connect for dedicated, high-bandwidth
connections between on-premises supply chain systems and
AWS.
- Deploy Amazon CloudFront to cache frequently accessed
content and reduce latency for global supply chain users.
- Configure AWS Global Accelerator to optimize network paths
and improve application performance for distributed supply
chain operations.
- Implement Route 53 latency-based routing to automatically
direct traffic to the best-performing AWS region.
- Monitor network performance metrics and optimize routing
configurations to maintain optimal user experience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf04-bp01.html*

---

# SCPERF05 — Test and monitor performance

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# SCPERF05-BP01 Implement comprehensive monitoring and dashboards for supply chain performance

Building an effective dashboard involves focusing on the key
performance indicators (KPIs) that matter most to your
organization and displaying them in an understandable and visually
appealing way.

**Desired outcome:** Measuring of the
application behavior can help manage it better, just not only the
performance of the application also during vulnerable situations
and to take actions spontaneously.

**Benefits of establishing this best
practice:** Good observability and dashboard to monitor
performance efficiency and continuous improvements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use tools and best practices to gain insights including End-to-end
visibility, alerts and alarms, Anomaly detection, regular review
of metrics and logs, security monitoring, and cost optimization.
Remember, while AWS provides observability tools (Amazon CloudWatch, AWS CloudTrail) to monitor and gain insights, it's the
combination of these tools with best practices that will give you
the most valuable insights about the end-to-end supply chain
systems.

### Implementation steps

- Identify key performance indicators (KPIs) that are most
critical to supply chain operations and business objectives.
- Design and implement comprehensive dashboards using Quick or CloudWatch dashboards to visualize supply
chain performance.
- Configure automated alerts and alarms based on performance
thresholds and anomaly detection to enable proactive
response.
- Implement end-to-end tracing and monitoring across all
supply chain components, from edge devices to cloud
applications.
- Establish regular review processes for performance metrics
and logs to identify trends and optimization opportunities.
- Create role-based dashboard views that provide relevant
insights to different stakeholders across the supply chain
organization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp01.html*

---

# SCPERF05-BP02 Evaluate compliance with performance requirements

When many systems, including third-party systems, are involved in
a workload, it is important to know the behavior of each system
and to monitor who is contributing to performance loss so proper
adjustments can be made.

**Desired outcome**: Optimum
performance that conforms to the system requirements to handle
loads.

**Benefits of establishing this best
practice:** Enhanced visibility into system performance
across complex supply chain networks, improved ability to identify
and resolve performance bottlenecks, better accountability for
third-party system performance, and reduced mean time to
resolution for performance issues.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Monitoring of your workload at multiple levels helps verify that
your resources are performing as expected and you are aware of
deviations. Consider all dimensions of the solution for
monitoring, for example client-side and server-side metrics,
application metrics and infrastructure metrics, technical and
functional metrics.

Provide visibility of data loss in your metrics, for example, by
monitoring for lost messages.

Where possible capture inter-solution and inter-process
communication streams to aid with the reproduction of issues.

### Implementation steps

- Establish performance baselines and SLAs for all supply
chain systems, including third-party integrations.
- Implement comprehensive monitoring across all system
layers, including infrastructure, application, and
business metrics.
- Deploy distributed tracing to track performance across
complex supply chain workflows and identify bottlenecks.
- Create automated performance testing and validation
processes to make sure systems meet established
requirements.
- Implement alerting mechanisms that notify teams when
performance deviates from established baselines or SLA
thresholds.
- Conduct regular performance reviews and optimization
initiatives based on monitoring data and compliance
assessments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp02.html*

---

# SCPERF05-BP03 Integrate performance testing into the release cycle of the supply chain application

Load testing results help you measure how the system behaves while
in high-traffic or heavy loads. Note these measurements to help
you adjust the underlying resources without wasting cost by
over-provisioning.

**Desired outcome:** Properly sized
supply chain applications.

**Benefits of establishing this best
practice:** Cost optimization, resilience, durability,
and improved user experience.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Verify consistency and failure recovery during load tests.
Verify data consistency and recovery during periods of high
load. Making sure that your workload's RTO and RPO is still
valid under the highest load can uncover gaps in your
architecture and operational resilience.

Understand performance of the system under peak load and in
failure scenarios: Include testing of common failure scenarios
in your performance testing suites to understand your workload
behavior in these situations and determine areas for
improvement.

### Implementation steps

- Develop comprehensive performance testing strategies that
simulate realistic supply chain load patterns and peak
usage scenarios.
- Integrate automated performance testing into CI/CD
pipelines to validate performance with every major
release.
- Implement chaos engineering practices to test system
resilience and recovery capabilities under various failure
conditions.
- Create performance test scenarios that include third-party
system integrations and supplier network dependencies.
- Establish performance regression testing to make sure new
releases don't degrade existing system performance.
- Document and analyze performance test results to
continuously improve system architecture and resource
allocation strategies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf05-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
