# ADVSUS10 — Moderation and brand safety

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS10-BP01 Optimize content moderation systems for sustainable operation

As content grows for organizations, optimizing content moderation systems can benefit sustainability-related key performance indicators (KPIs). Implement or build architectures that include efficient machine learning models, automated scaling, and optimized storage patterns.

## Implementation guidance

- Use efficient machine learning models for content
classification. Use AWS Inferentia chips when possible,
for improved performance per watt.
- Implement batch processing for non-real-time moderation
tasks.
- Configure regional content analysis to minimize data
movement.
- Use caching strategies for frequently accessed moderation
rules.
- Use energy-efficient computing resources, such as AWS
Graviton, for moderation workloads.
- Implement automated scaling based on moderation demand
using auto scaling rules and Amazon CloudWatch metrics.
- Optimize storage patterns for moderation results and audit
trails. For workloads using Amazon S3, use Storage Lens for
insights and recommendations to optimize storage use.

## Key AWS services

- Amazon Rekognition
- AWS Inferentia
- Amazon SageMaker AI
- AWS Auto Scaling
- AWS CloudWatch
- Amazon ElastiCache
- Amazon S3 Storage Lens

## Resources

- [Optimize AI/ML workloads for sustainability: Part 1, identify business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus10-bp01.html*

---
