# ADVREL09 — Ad measurement and verification

**Pillar**: Reliability  
**Best Practices**: 2

---

# ADVREL09-BP01 Implement redundant ad-verification systems with automated failover mechanisms

Implement redundant ad-verification systems with automated failover capabilities. Use multiple verification providers and automated monitoring for continuous, reliable advertising measurement and validation.

## Implementation guidance

- Deploy multiple third-party verification providers for
cross-validation
- Implement automated failover mechanisms for measurement
systems
- Use data quality checks and anomaly detection
- Maintain backup measurement methodologies
- Configure automated retry mechanisms for failed
measurements
- Implement circuit breakers for degraded third-party
services
- Set up monitoring and alerting for measurement system
health

## Key AWS services

- Amazon CloudWatch
- AWS Lambda
- Amazon EventBridge
- AWS Step Functions
- Amazon DynamoDB

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel09-bp01.html*

---

# ADVREL09-BP02 Establish robust data collection and validation pipelines for measurement accuracy

Build reliable data collection and validation pipelines, emphasizing real-time monitoring, automated reconciliation, and recovery procedures to maintain measurement accuracy in advertising systems.

## Implementation guidance

- Implement data validation at collection points
- Set up real-time data quality monitoring
- Create automated data reconciliation processes
- Configure dead letter queues for failed events
- Implement idempotent processing for measurement events
- Establish clear data freshness SLAs
- Deploy automated data recovery procedures

## Key AWS services

- Amazon Kinesis
- Amazon SQS
- Amazon S3
- AWS Glue
- Amazon EMR

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel09-bp02.html*

---
