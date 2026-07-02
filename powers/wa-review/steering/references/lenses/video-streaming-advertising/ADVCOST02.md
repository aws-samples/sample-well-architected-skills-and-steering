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
