# ADVREL06 — Architecture capacity

**Pillar**: Reliability  
**Best Practices**: 1

---

# ADVREL06-BP01 Architect defensively against failures

Acknowledge that systems and services occasionally fail, and some
failures will come from external partners and dependencies outside
of your control.

## Implementation guidance

Most advertising systems exist in hybrid configurations, with
services and applications spanning across cloud and on-premise
infrastructure. They use mechanisms across multiple Regions or
data centers to provide high availability, scalability, and
performance.

Understand the characteristics of your application components
and how each component in a hybrid environment may impact your
system as a whole. Be familiar with the complexity of deployment
and operations across different types of environments and how
that complexity can impact overall resilience.

Instead of using internet-based connections, use AWS Direct Connect where possible to provide a consistent network
experience for critical workload networking requirements.
Implement circuit breakers, retries, and fallbacks to gracefully
handle failures from external dependencies, and prevent
cascading failures within your system. Adopt a distributed
architecture with loose coupling and asynchronous communication
patterns to isolate failures and prevent them from propagating
across the entire system.

To validate your resilience strategies and identify potential
weaknesses, regularly conduct chaos engineering experiments by
intentionally injecting controlled failures into your system.

## Key AWS services

- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Availability Zones and Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [Monitoring
and alerting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources

- [Architecting
for Reliability on AWS](https://aws.amazon.com/blogs/architecture/architecting-for-reliability-on-aws/)
- [Implementing
Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
- [Disaster
Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel06-bp01.html*

---
