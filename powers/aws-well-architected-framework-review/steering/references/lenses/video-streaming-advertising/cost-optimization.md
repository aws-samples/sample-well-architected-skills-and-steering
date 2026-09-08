# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 6

---

# ADVCOST01 — Practice Cloud Financial Management

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# ADVCOST01-BP01 Continually measure costs of different real-time bidding workloads, and adjust resource allocation accordingly

With fluctuations in usage over time, the costs associated with real-time bidding
workloads can vary significantly. Continually monitoring costs is the best way to keep them
under control.

## Implementation guidance

- Set KPIs for each campaign to evaluate cost-to-revenue ratios, as this is key to
measuring value generation.
- Set KPIs for billing metrics (for example, resource costs) as well as campaign
metrics (for example, click-through rate or new subscribers).
- Implement cost allocation tags for resources relevant to campaign tracking.
- Use the Cost and Usage Dashboards Operations Solution (CUDOS) Dashboard as a way
to quickly visualize information about RTB costs and performance.
- Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for one-off visualizations of cost data.
- Generate [Quick](https://aws.amazon.com/quicksight/) dashboards that
are specific to each campaign or that comprise the business as a whole.
- Configure Quick with user-configurable filters to allow users to focus on the data
that matters most to them.
- Configure Quick to email dashboard reports to users on a schedule to automate and
simplify the process.
- Regularly evaluate the data and report findings back to the business.
- As campaigns progress, continually re-evaluate them, and adjust resource
allocation to meet value generation goals.

## Key AWS services

- [Amazon Athena](https://aws.amazon.com/athena/)
- [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)

## Resources

- [Guidance for Deploying a Data Transfer Dashboard for AdTech on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/)
- [Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics
on AWS](https://aws.amazon.com/solutions/guidance/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/)
- [Using CUDOS Dashboard visualizations for AWS Marketplace spend visibility and
optimization](https://aws.amazon.com/blogs/awsmarketplace/using-cudos-dashboard-visualizations-aws-marketplace-spend-visibility-optimization/)
- [Additional dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards/additional)
- [Organizing costs
using AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp01.html*

---

# ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding

While resiliency can increase the cost of workloads, downtime can also be very
expensive. It's important to understand the costs of having a resilient infrastructure
against the costs of not having a resilient infrastructure.

## Implementation guidance

- Quantify the cost of downtime for each campaign based on its expected revenue.

Analyze historical data and projections to estimate the potential revenue
loss due to downtime.
- Consider the impact on customer satisfaction and brand reputation.

- Estimate the cost of applying resiliency measures.

Evaluate the cost of additional resources required for multi-Regional
deployments, backup, and recovery solutions
- Use AWS tools like [AWS Pricing Calculator](https://calculator.aws/#/)
for estimating costs of future resiliency efforts and [Quick](https://aws.amazon.com/quicksight/), [Amazon Athena](https://aws.amazon.com/athena/), AWS Cost and Usage Report, and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for cost analysis
and reporting.

- Compare the cost of downtime with the cost of resiliency measures.

If the potential lost revenue and reputation costs of downtime exceed the
cost of resiliency, favor implementing resiliency measures.
- Consider multi-regional deployments, backup and recovery solutions, and other
resiliency best practices.

By following these steps, you can make informed decisions about implementing
resiliency measures based on a cost-benefit analysis, using AWS tools and services to
optimize your approach and ensure business continuity.

## Key AWS services

- [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources

- [Stage
1: Set objectives](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-1.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp02.html*

---

# ADVCOST02 — Cost-effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# ADVCOST02-BP01 Use ARM processors for faster and more cost-effective bidder nodes

ARM processors can combine lower costs and higher performance, which makes them a great
consideration for cost optimization.

## Implementation guidance

- Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify
the most cost-effective instance types for bidding workloads, and verify that ARM
instances were considered.
- Use [AWS Graviton](https://aws.amazon.com/ec2/graviton/) instances,
which are powered by ARM processors designed by AWS, for your cloud workloads
running in [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/), AWS Lambda,
containers, and various other services.
- Take advantage of the cost savings offered by Graviton instances, which generally
cost less than comparable x86 instances.
- For custom software, recompile it for use on Graviton processors with the
assistance of open-source tools like [sse2neon](https://github.com/DLTcollab/sse2neon) and [Porting Advisor for
Graviton](https://github.com/aws/porting-advisor-for-graviton) for compiled applications.
- For interpreted or JIT languages, they generally run as-is or with minimal
modifications on Graviton processors.
- Conduct performance testing and benchmarking to verify that Graviton instances
meet bidding workload requirements.

## Key AWS services

- [Amazon Cloudwatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

## Resources

- [Use Graviton instances and containers](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-graviton.html)
- [How DeviceAtlas optimized Real-Time Advertising Price/Performance on AWS
Graviton3](https://aws.amazon.com/blogs/industries/how-deviceatlas-optimized-real-time-advertising-price-performance-on-aws-graviton3/)
- [Using
Porting Advisor for Graviton](https://aws.amazon.com/blogs/compute/using-porting-advisor-for-graviton/)
- [AWS Unveils Next Generation AWS-Designed Chips](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp01.html*

---

# ADVCOST02-BP02 Use compression to reduce network traffic and storage costs

Using compression can reduce the amount of data transferred thus reducing network and
storage costs.

## Implementation guidance

- Use GZIP compression before transferring data to [Amazon S3](https://aws.amazon.com/s3) to reduce traffic between Availability Zones and Regions, as well as
traffic to the internet.
- Use snappy compression for [Amazon Kinesis](https://aws.amazon.com/kinesis/) Data Streams to reduce the amount of data stored and transferred.
- Implement HTTP/2 for [Application Load Balancers](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), [Amazon API Gateway](https://aws.amazon.com/api-gateway/) compression, and [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/).
- For databases, consider the following compression techniques to reduce storage
costs:

Column-level compression
- Table-level compression
- Backup compression
- Query result compression
- Index compression

- Implement replication compression to reduce data transfer costs.
- Monitor the impact of compression on CPU utilization, and verify that the
increased CPU costs do not exceed the network transfer costs saved.

## Resources

- [Cost-Optimizing your AWS architectures by utilizing Amazon CloudFront features](https://aws.amazon.com/blogs/networking-and-content-delivery/cost-optimizing-your-aws-architectures-by-utilizing-amazon-cloudfront-features/)
- [Reduce network transfer time with connection compression in Amazon RDS for MySQL and
Amazon RDS for MariaDB](https://aws.amazon.com/blogs/database/reduce-network-transfer-time-with-connection-compression-in-amazon-rds-for-mysql-and-amazon-rds-for-mariadb/)
- [Enable
payload compression for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-enable-compression.html)
- [Custom Amazon MSK
configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html)
- [Processing large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/)
- [What is AWS
Transfer Family?](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp02.html*

---

# ADVCOST02-BP03 Use provisioned resource allocation for campaigns with predictable capacity, and use dynamic allocation for unexpected capacity

Provisioned capacity can provide the lowest cost per hour. However, for unpredictable
workloads dynamic allocation can provide a lower overall cost of ownership.

## Implementation guidance

Provisioned capacity and on-demand capacity are two different pricing models offered
by various AWS services, including [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/), [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), [AWS Lambda](https://aws.amazon.com/lambda/), and [Amazon Athena](https://aws.amazon.com/athena/). The differences between the two models are the
following:

- **Provisioned capacity:** With provisioned capacity, you
reserve and pay for a specific amount of capacity in advance, regardless of whether
you use it or not.

This model is suitable for workloads with predictable and consistent traffic
patterns or when you have a baseline capacity requirement.
- By provisioning capacity, you get dedicated resources and can achieve better
performance and lower costs compared to on-demand capacity for sustained
workloads.
- Examples: DynamoDB provisioned throughput, Kinesis Data Streams provisioned
capacity, Lambda provisioned concurrency, and Athena workgroup capacity.

- **On-demand capacity:** With on-demand capacity, you pay
for the resources you consume on a per-use basis without any upfront commitment or
reservation.

This model is suitable for workloads with unpredictable or bursty traffic
patterns, where you don't have a consistent baseline requirement.
- On-demand capacity provides flexibility and scalability, as you only pay for
what you use, but it can be more expensive for sustained workloads compared to
provisioned capacity.
- Examples: DynamoDB on-demand capacity, Kinesis Data Streams on-demand capacity,
Lambda on-demand concurrency, and Athena on-demand capacity.

- **[Serverless
capacity](https://aws.amazon.com/serverless/):** AWS offers technologies for running code, managing
data, and integrating applications, all without managing servers.

Serverless technologies feature automatic scaling, built-in high
availability, and a pay-for-use billing model to increase agility and optimize
costs.
- These technologies also eliminate infrastructure management tasks like
capacity provisioning and patching, so you can focus on writing code that serves
your customers.
- Examples: Amazon Aurora, Amazon Redshift, Amazon Neptune, Amazon OpenSearch Service, and Amazon
Elasticache.

The choice between provisioned, on-demand, and serverless capacity depends on your
workload characteristics, cost considerations, and performance requirements. Some general
guidelines for making this choice are the following:

- If you have a predictable and consistent workload with a known baseline capacity
requirement, provisioned capacity can provide better performance and cost savings for
sustained usage.
- If your workload is highly variable, unpredictable, or bursty, on-demand or
serverless capacity can offer more flexibility and scalability, but it may be more
expensive for sustained usage.
- For short-term or temporary workloads, on-demand or serverless capacity may be
more cost-effective because you don't have to pay for unused provisioned capacity.
- For long-running or mission-critical workloads with consistent traffic,
provisioned capacity can provide better performance and cost savings.

Analyze your workload patterns, performance requirements, and cost considerations to
determine the most suitable capacity model for your use case. Additionally, many AWS
services offer auto scaling and capacity management features to help optimize resource
allocation and costs based on actual usage patterns.

## Resources

- [Choose the data stream capacity mode](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html)
- [Pricing for Provisioned
Capacity](https://aws.amazon.com/dynamodb/pricing/provisioned/)
- [Configuring provisioned concurrency for a function](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [Serverless on AWS](https://aws.amazon.com/serverless/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp03.html*

---

# ADVCOST02-BP04 Use Spot Instances for cost-effective bidding-as-a-service workloads with flexible fault-tolerance mechanisms

For workloads that can be interrupted, Spot Instances can provide high performance for
a very low cost per hour.

## Implementation guidance

By using Spot Instances and services like Auto Scaling groups and AWS Batch, you can
achieve significant cost savings for your bidding-as-a-service workloads.

- **Spot Instance pricing:** Spot Instances are typically
offered at a substantial discount compared to On-Demand Instance prices. The discount
can range from 10% to 90%, depending on the instance type, region, and current demand.
On average, you can expect to save around 70% on compute costs by using Spot
Instances.
- **Auto scaling with Spot Instances:** By configuring your
Auto Scaling groups to launch Spot Instances, you can benefit from the cost savings
while maintaining the desired level of capacity and availability. Auto Scaling groups
automatically replace interrupted Spot Instances, and your workload can continue
running without disruption.
- **AWS Batch with Spot Instances:** For batch processing
workloads, AWS Batch can use Spot Instances as the compute environment for your jobs.
This can lead to significant cost savings, especially for compute-intensive or
long-running batch jobs. AWS Batch automatically handles job retries and check-pointing,
improving fault tolerance and efficient resource utilization.
- **Cost optimization strategies:**

**Instance right-sizing:** Regularly analyze your
workload's performance and resource utilization to identify the most
cost-effective instance types and sizes. Right-sizing your instances can lead to
substantial cost savings without compromising performance.
- **Spot Instance interruption handling:** Implement
efficient strategies to handle Spot Instance interruptions, such as check-pointing
long-running jobs or gracefully draining and restarting interrupted instances.
This can help minimize wasted compute resources and associated costs.
- **Spot Instance advisors:** Use AWS Spot Instance
advisors or third-party tools to optimize your Spot Instance selection and bidding
strategies. These tools can help you identify the most cost-effective Spot
Instance pools based on historical pricing data and demand patterns.

- **Cost monitoring and optimization:** Continuously
monitor your workload's cost and performance metrics using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), and other monitoring tools. Identify cost optimization
opportunities and implement them regularly to maximize your savings.

By implementing these strategies, you can potentially achieve significant cost
savings while maintaining the scalability and performance of your bidding-as-a-service
workloads.

It's important to note that while Spot Instances offer substantial cost savings, they
are subject to interruptions based on AWS's capacity requirements. Therefore, it's
crucial to implement proper fault tolerance mechanisms and have a strategy to handle
instance interruptions to ensure the reliability and availability of your
bidding-as-a-service workloads.

## Key AWS services

- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)
- [AWS Fargate](https://aws.amazon.com/fargate/)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)

## Resources

- [Guidance for Building a Real Time Bidder for Advertising on AWS](https://aws.amazon.com/solutions/guidance/building-a-real-time-bidder-for-advertising-on-aws/)
- [Beeswax Uses
AWS to Cost-Effectively Process Millions of Bid Requests per Second](https://aws.amazon.com/solutions/case-studies/beeswax-case-study/)
- [AWS Fargate for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)
- [EC2 instance rebalance
recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html)
- [EC2 Fleet and
Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp04.html*

---

# ADVCOST03 — Optimizing communication costs

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# ADVCOST03-BP01 Consider private communication channels between SSP and DSP

Private communication channels can help keep traffic secure while also reducing
internet egress charges.

## Implementation guidance

With [AWS PrivateLink](https://aws.amazon.com/privatelink/), you can
establish secure, private communication channels between your SSPs, DSPs, and other AWS
services or on-premises resources. This approach enhances security, reduces data exposure
risks, and can improve performance for your programmatic advertising workloads, while
simplifying your network architecture and reducing operational overhead. In cases where
PrivateLink cannot be used, then Amazon VPC Peering, AWS Direct Connect, and AWS Global Accelerator can be
considered.

## Resources

- [AWS lowers data processing charges for AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2021/07/aws-lowers-data-processing-charges-aws-privatelink/)
- [Get
started with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp01.html*

---

# ADVCOST03-BP02 When integrating SSPs and DSPs for programmatic advertising, co-locate the platforms

Keeping SSP and DSP components together can keep transactions fast while minimizing
inter-AZ and inter-Region traffic charges.

## Implementation guidance

When integrating SSPs and DSPs for programmatic advertising, use Network Load
Balancer (NLB) to direct traffic from the SSP to the DSP within the same Availability
Zone. This approach can help optimize costs while providing high performance and
availability.

- **Deploy in the same Availability Zone:** Deploy your SSP
and DSP components (such as bidding nodes) within the same Availability Zone based on
expected traffic patterns to minimize cross-AZ data transfer costs and reduce network
latency.
- **Use Network Load Balancer (NLB):** Use Network Load
Balancer (NLB) to distribute traffic from the SSP to the DSP instances within the same
Availability Zone. NLB is cost-effective for TCP traffic and can handle millions of
requests per second.
- **Configure your NLB:** Set the cross-zone-load-balancing
attribute to false, or use the appropriate routing policy to prioritize routing within
the same Availability Zone. This approach routes traffic preferentially to bidder
nodes within the same Availability Zone, reducing cross-AZ data transfer costs.
- **Monitor and optimize:** Regularly monitor your data
transfer costs and traffic patterns across Availability Zones. Adjust your resource
placement and NLB configurations as needed to optimize cost-effectiveness.
- **Use cost optimization tools:** Use AWS Cost Explorer,
AWS Budgets, and AWS Cost Anomaly Detection to monitor and analyze your costs, set budgets, and
receive alerts for potential cost anomalies.
- **Automate and scale:** Use AWS CloudFormation or AWS CDK to
automate the provisioning and management of your SSP and DSP infrastructure, which
helps you scale efficiently and consistently while maintaining cost optimization.

## Resources

- [Guidance for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/)
- [Announcing new AWS Network Load Balancer (NLB) availability and performance
capabilities](https://aws.amazon.com/about-aws/whats-new/2023/10/aws-nlb-availability-performance-capabilities/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp02.html*

---

# ADVCOST03-BP03 Co-locate bidder and database nodes

Keeping bidder and database nodes together can help transactions occur quickly and can
also reduce inter-AZ and inter-Region traffic charges.

## Implementation guidance

To optimize costs when configuring advertising bidder nodes to communicate with
database nodes within the same Availability Zone, consider the following guidance:

- **Resource placement:** Carefully plan the placement of
your bidder nodes and database nodes across Availability Zones. Co-locate bidder nodes
and their corresponding database nodes within the same Availability Zone to minimize
cross-AZ data transfer costs.
- **Database configuration:** If using a managed database
service like Amazon RDS, configure your database instances to use multi-AZ deployment
within the same AWS Region. This separates the primary and standby database
instances into separate Availability Zones, providing high availability while
minimizing cross-AZ data transfer costs for your bidder nodes.
- **Network configuration:** Configure your VPC and subnets
to verify that bidder nodes and database nodes within the same AZ can communicate
efficiently. Use private IP addresses, and avoid public IP addresses or internet
gateways, which can incur additional data transfer costs.
- **Caching and replication:** Implement caching strategies
and read replicas for your database nodes to reduce the amount of data transfer
required between bidder nodes and database nodes. This can further minimize cross-AZ
data transfer costs.
- **Monitoring and optimization:** Regularly monitor your
data transfer costs and traffic patterns across AZs. Adjust your resource placement
and network configurations as needed to optimize cost-effectiveness.
- **Use cost optimization tools:** Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/),
[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), and [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to monitor
and analyze your costs, set budgets, and receive alerts for potential cost anomalies.

## Key AWS services

[Network Load Balancer (NLB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)

## Resources

- [Exploring Data Transfer Costs for AWS Managed Databases](https://aws.amazon.com/blogs/architecture/exploring-data-transfer-costs-for-aws-managed-databases/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp03.html*

---

# ADVCOST04 — Database optimization

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# ADVCOST04-BP01 Consider lower cost storage for older User Profile data

As the 30 most recent days are most relevant, using DynamoDB can prioritize high
performance for the most relevant data (typically within the last 30 days), and archiving to
Amazon S3 can reduce costs for less relevant data.

**For S3 profile data:**

- Enable S3 Intelligent-Tiering on your bucket
- Configure lifecycle policies to transition older data
- Set up monitoring to track access patterns

- **For DynamoDB:**

Implement TTL for old profile records
- Create export jobs to move historical data to S3
- Use S3 Lifecycle policies for long-term archival

**Cost optimization best practices**

- Regularly analyze data access patterns
- Use AWS Cost Explorer to track storage expenses
- Consider object size and retrieval frequency
- Implement tagging for better cost tracking

## Key AWS services

- DynamoDB
- S3
- Intelligent Tiering

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp01.html*

---

# ADVCOST04-BP02 Consider multi-level caching for user profile data

DynamoDB Accelerator provides a powerful, cost-effective solution for caching user profile data by
dramatically reducing read latency and minimizing direct database operations. By creating an
in-memory caching layer, DAX can reduce DynamoDB read capacity unit (RCU) consumption,
translating to significant cost savings for applications with high-frequency profile
lookups. For user profile systems with repetitive access patterns, DAX automatically caches
frequently retrieved items, delivering microsecond-level response times while substantially
lowering infrastructure expenses.

The intelligent caching mechanism avoids redundant database queries, allowing
organizations to optimize their database performance without complex manual caching
implementations, making it an ideal solution for scalable, cost-conscious applications that
require rapid access to user information.

Moreover, the seamless integration of DAX with existing DynamoDB architectures means
minimal code changes are required to achieve these performance and cost benefits, providing
an efficient path to enhanced application responsiveness and reduced operational costs.

- Create a DAX Cluster:

Select the same VPC as DynamoDB table
- Select node type (recommend r5.large for medium workloads)
- Configure cluster size (minimum 3 nodes for high availability)
- Set cache TTL

- Modify application code to support DAX
- Caching strategy implementation:

Configure cache invalidation mechanisms
- Implement write-through or write-behind strategies
- Set appropriate TTL for cached items

- Monitoring and optimization: CloudWatch metrics to track

Cache hit or miss ratio
- Latency
- Consumed read capacity
- Error rates
- Recommended monitoring dashboard

- Performance and cost optimization tuning:

Adjust cluster size based on traffic
- Use reserved instances
- Implement intelligent caching
- Monitor and adjust regularly

## Resources

- [Reduce latency and cost in read-heavy applications using Amazon DynamoDB Accelerator](https://aws.amazon.com/blogs/database/reduce-latency-and-cost-in-read-heavy-applications-using-amazon-dynamodb-accelerator/)

## Key AWS services

- DynamoDB Accelerator
- ElastiCache (Redis OSS)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp02.html*

---

# ADVCOST04-BP03 Store profiles in a single Region and replicate asynchronously

Generally, users will only be in one Region at a time and therefore will only be
updating in one Region. As a result, schedule replication a few times a day with AWS Step Functions
and AWS Lambda to meet the resiliency requirements for data while minimizing high latency and
data transfer costs.

## Implementation guidance

- Develop a Lambda replication function.
- Configure your Step Functions workflow.
- Set up a Amazon CloudWatch event rule for scheduling.
- Implement error handling.
- Configure monitoring.
- Test your replication workflow.

## Key AWS services

- AWS Step Functions
- AWS Lambda

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost04-bp03.html*

---

# ADVCOST05 — Privacy-enhanced collaboration

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# ADVCOST05-BP01 Use cost efficient data types and configurations for collaborative data environments

Use efficient storage formats and streamlined query configurations to reduce unnecessary data scanning, duplication, and transfer costs in collaborative analytics environments.

## Implementation guidance

- Use parquet or columnar formats with partitioning and compress datasets.
- Use standard SQL for lightweight or well-partitioned datasets.
- Avoid unnecessary cross-joins or full table scans.
- Use same-Region AWS Clean Rooms collaborations to minimize inter-Region transfer costs.

## Key AWS services

- AWS Clean Rooms

## Resources

- [Data
formats for AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-formats.html)
- [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.4---partition-your-data-to-avoid-unnecessary-file-reads.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost05-bp01.html*

---

# ADVCOST06 — Data transfer and processing

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# ADVCOST06-BP01 Design fraud detection pipelines to minimize redundant processing and optimize inference costs

Design fraud detection workflows that avoid repeated evaluations by caching known outcomes, filtering threats as early as possible, and running only the necessary inference steps on cost-efficient compute resources.

## Implementation guidance

- Enable AWS Cost Anomaly Detection with thresholds for each adtech microservice.
- Use Spot Instances and Managed Spot Training for SageMaker AI training jobs to identify
malicious ads.
- Cache fraud evaluation results (for example, known creatives, IPs, or device IDs) using DynamoDB
or ElastiCache to avoid reprocessing identical inputs.
- Implement AWS WAF rules for basic bot detection at edge (lowest cost).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost06-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
