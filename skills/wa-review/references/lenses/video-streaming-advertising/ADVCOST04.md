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
