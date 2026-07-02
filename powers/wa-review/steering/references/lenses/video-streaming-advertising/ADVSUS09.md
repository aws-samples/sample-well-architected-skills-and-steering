# ADVSUS09 — Ad intelligence, measurement, and security

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS09-BP01 Optimize fraud detection systems for resource efficiency

Fraud detection systems can perform efficiently and have a reduced carbon impact when using approaches such as intelligent sampling, scheduled analysis, and Regional detection.

## Implementation guidance

- Use energy-efficient processing for continuous fraud
monitoring. If running compute instances, select AWS
Graviton processors.
- Implement intelligent sampling for fraud detection where
appropriate to reduce computational overhead while meeting
business requirements.
- Schedule intensive fraud pattern analysis during
low-carbon periods.
- Use serverless architectures for variable detection
workloads.
- Use efficient data storage patterns for fraud signals and
patterns. Archive data that is not readily needed and
remove data that is no longer required for
compliance/security purposes.
- Use AWS Clean Rooms for measurement analysis across
partners, with the ability to analyze data sets where they
are, with no data movement.
- Implement caching for frequently accessed fraud detection
rules.
- Configure Regional detection systems to minimize data
transfer.

## Key AWS services

- Amazon EC2 with Graviton processors
- AWS Lambda
- Amazon ElastiCache
- AWS Clean Rooms
- Amazon CloudWatch

## Resources

- [Hardware and services](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/hardware-and-services.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus09-bp01.html*

---
