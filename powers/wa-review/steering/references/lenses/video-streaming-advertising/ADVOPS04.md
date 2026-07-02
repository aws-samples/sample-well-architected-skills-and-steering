# ADVOPS04 — Manage operational processes

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# ADVOPS04-BP01 Implement operational procedures based on data classification and latency requirements

Managing advertising workloads requires different operational
approaches based on data latency needs. This best practice
focuses on establishing specific procedures for handling
low-latency data like bid requests, medium-latency data such as
campaign optimization, and high-latency data including
historical analytics.

## Implementation guidance

For low-latency data (bid data, user profiles, real-time
impressions):

- Implement multi-AZ deployments with automatic failover
mechanisms to facilitate continuous availability
- Configure monitoring with short evaluation periods
appropriate for detecting real-time issues
- Establish dedicated rapid-response procedures for critical
alerts affecting bidding operations
- Implement circuit breakers in API calls to help block
cascading failures during service degradation
- Create runbooks for emergency traffic management during
extreme load conditions
- Configure auto-scaling with aggressive scaling policies to
handle sudden traffic spikes
- Implement local caching strategies to reduce database load
for frequently accessed data
- Set up dedicated dashboards with high-frequency metric
collection for real-time monitoring

For medium-latency data (behavioral data, campaign
optimization):

- Configure batch processing jobs with appropriate completion
targets for campaign optimization
- Implement queue management with automated retry mechanisms
for failed operations
- Set up monitoring with balanced evaluation periods suitable
for near real-time operations
- Create standard incident response procedures with
appropriate escalation paths
- Implement data validation checks with error handling for
data quality issues
- Configure auto-scaling based on processing queue depth and
scheduled campaign activities
- Set up dashboards with appropriate refresh rates for
campaign management operations

For high-latency data (historical data, analytics):

- Schedule batch processing during off-peak hours to minimize
impact on real-time operations
- Implement cost-optimized storage strategies with appropriate
data lifecycle policies
- Configure monitoring with periodic health checks and summary
reporting
- Create standard support procedures with appropriate response
times for non-critical systems
- Implement automated data quality validation with
notification mechanisms
- Configure resource allocation with scheduled scaling based
on known processing windows
- Establish regular performance review processes with trend
analysis

For specialized advertising data types:

- Fraud detection data: Implement optimized processing
pipelines with appropriate monitoring and escalation
procedures designed for the critical nature of fraud
detection
- Content moderation data: Create workflows that balance
automated screening with human review processes, with
appropriate prioritization based on content risk assessment

## Key AWS services

- Amazon CloudWatch
- AWS Systems Manager
- Amazon EventBridge
- Amazon Kinesis Data Streams
- Amazon Managed Service for Apache Flink

## Resources

- [AWS for Advertising & Marketing](https://aws.amazon.com/advertising-marketing/adtech-real-time-bidding/)
- [Architectural patterns for real-time analytics using Amazon Kinesis Data Streams, part 1](https://aws.amazon.com/blogs/big-data/architectural-patterns-for-real-time-analytics-using-amazon-kinesis-data-streams-part-1/)
- [Streaming architecture patterns using a modern data architecture](https://docs.aws.amazon.com/whitepapers/latest/build-modern-data-streaming-analytics-architectures/streaming-analytics-architecture-patterns-using-a-modern-data-architecture.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advops04-bp01.html*

---
