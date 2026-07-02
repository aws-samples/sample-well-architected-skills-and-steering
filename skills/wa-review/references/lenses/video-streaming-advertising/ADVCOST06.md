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
