# LSPERF03 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF03-BP01 Workload-specific performance analysis

Conduct systematic analysis of workload characteristics to identify
distinct performance requirements and optimization opportunities.
Profile computational patterns, data access behaviors, and resource
utilization across different workflow stages to guide targeted
optimization efforts, allocating resources on empirical performance
needs rather than assumptions.

**Desired outcome:** Implement
systematic workload profiling to identify optimization opportunities
and guide resource allocation based on empirical performance data.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To optimize genomics or life sciences workloads effectively, begin
with systematic analysis using AWS observability tools. Deploy
Amazon CloudWatch with custom metrics and dashboards to establish
baseline performance across your architecture. Configure detailed
monitoring through CloudWatch Container Insights for containerized
workloads or CloudWatch agent for EC2 instances to capture CPU,
memory, disk, and network utilization patterns.

Profile computational patterns by implementing AWS X-Ray tracing
to understand request flows and component interactions throughout
your application stack. For ML-based workloads, use Amazon SageMaker AI Profiler to analyze model training and inference
performance characteristics. These tools help identify
computational bottlenecks and guide decisions about instance
types, model optimization techniques, or architectural changes
that could improve performance.

Analyze data access behaviors using CloudWatch metrics for
services like Amazon S3, Amazon DynamoDB, and Amazon RDS.
Implement S3 Storage Lens to gain visibility into object storage
patterns and optimize data placement strategies. For database
workloads, use RDS Performance Insights or DynamoDB CloudWatch
metrics to identify query patterns that might benefit from
indexing or caching strategies with Amazon ElastiCache.

Map resource utilization across different workflow stages by
correlating metrics from multiple sources in CloudWatch
dashboards. This correlation helps identify how resource
requirements fluctuate throughout your workload lifecycle and
where targeted optimizations would deliver the greatest impact.
Use AWS Cost Explorer, cost allocation tags, and CloudWatch
dashboards together to understand the cost implications of
different resource allocation strategies.

Implement a data-driven optimization approach using AWS Compute Optimizer for right-sizing recommendations and AWS Well-Architected Tool to evaluate your architecture against best
practices. Test optimization hypotheses using A/B testing
methodologies with AWS AppConfig before full deployment. Document
findings and optimization decisions in AWS Systems Manager
documents to build organizational knowledge around performance
optimization practices specific to your Genomics or Lifesciences
workloads.

### Implementation steps

- Deploy CloudWatch dashboards for workload monitoring.
- Use SageMaker AI Profiler to analyze model performance.
- Implement X-Ray tracing for request flow analysis.
- Create S3 Storage Lens dashboards for data patterns.
- Optimize with AWS Compute Optimizer recommendations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf03-bp01.html*

---

# LSPERF03-BP02 Environment isolation by workload type

Implement clear separation between research and clinical
environments based on their fundamentally different requirements.
Establish a dedicated infrastructure for computationally-intensive
research pipelines with burst capacity for parallel processing,
while maintaining separate, highly-available environments for
clinical applications where consistency and reliability are
paramount.

**Desired outcome:** Create distinct
infrastructure environments optimized for the unique requirements of
research computing and clinical applications.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing clear separation between research and clinical
environments is essential for organizations working with
generative AI in healthcare and life sciences. Begin by
establishing distinct AWS accounts for each environment using AWS Organizations with service control policies (SCPs) that enforce
appropriate guardrails. This separation creates natural boundaries
for access controls, resource allocation, and regulatory
requirements while still enabling cross-account data sharing when
necessary through services like AWS RAM.

For research environments, prioritize flexibility and
computational power by implementing Amazon SageMaker AI with its
comprehensive ML development capabilities. Configure auto scaling
compute resources using Amazon EC2 Auto Scaling groups with
GPU-accelerated instances like P4d or G5g to support
computationally intensive workloads. Implement AWS Batch for
efficiently managing parallel processing jobs with spot instances
to optimize costs during model training and experimentation
phases. This approach provides researchers with the burst capacity
needed for iterative development while maintaining cost
efficiency.

For clinical environments, focus on high availability and
consistency by deploying infrastructure across multiple
Availability Zones using AWS CloudFormation or AWS CDK with
immutable patterns. Implement Amazon RDS multi-AZ deployments for
database reliability and Amazon ElastiCache for consistent
performance. Configure detailed monitoring with Amazon CloudWatch
and AWS X-Ray for predictable performance characteristics critical
for clinical applications. Implement AWS Config rules to enforce
configuration adherence with regulatory requirements like HIPAA or
GxP.

Establish controlled pathways for promoting validated models from
research to clinical environments using AWS CodePipeline with
approval gates and validation tests. Store model artifacts in
Amazon S3 with versioning enabled and implement AWS Lambda
functions to validate model metadata before clinical deployment.
Use Service Catalog to create standardized, pre-approved
deployment patterns that clinical teams can use without
compromising governance requirements.

### Implementation steps

- Create account separation using AWS Organizations.
- Deploy research workloads on SageMaker AI with GPU instances.
- Build clinical systems with Multi-AZ RDS deployments.
- Implement CodePipeline for controlled model promotion.
- Configure CloudWatch dashboards for environment monitoring.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf03-bp02.html*

---

# LSPERF03-BP03 Tailored service configuration by use case

Customize infrastructure and service configurations to align with
the specific requirements of each workload category. Fine-tune
compute, storage, and networking parameters for research
environments to maximize throughput and processing efficiency, while
configuring clinical environments with emphasis on consistent
performance, redundancy, and predictable behavior under each
condition.

**Desired outcome:** Implement
tailored infrastructure configurations that precisely match the
unique requirements of research and clinical workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Customizing infrastructure and service configurations for
different workload categories is essential for optimizing both
performance and cost efficiency in generative AI deployments.
Begin by conducting a detailed workload assessment using AWS Well-Architected Tool with the
[Generative
AI Lens](https://github.com/aws-samples/sample-well-architected-custom-lens/blob/main/generative-ai-lens/generative-ai-lens.json) to identify the specific requirements and
characteristics of each workload category. This assessment
establishes clear performance targets, reliability requirements,
and cost constraints that will guide your configuration decisions.

For research environments focused on model development and
experimentation, prioritize compute flexibility and processing
efficiency. Configure Amazon EC2 instances with the latest
generation of accelerators like AWS Trainium for training
workloads. Implement Amazon FSx for Lustre configured with high
throughput capabilities to support efficient data processing
during training. Use Amazon SageMaker AI with managed spot training
to reduce costs for non-time-sensitive workloads while maintaining
the ability to scale compute resources during intensive
experimentation phases.

For clinical or production environments where consistent
performance is critical, implement multi-AZ deployments across
infrastructure components using AWS CloudFormation or AWS CDK.
Configure Amazon RDS with multi-AZ deployments and provisioned
IOPS for consistent database performance. Implement Amazon ElastiCache with reserved nodes to provide stable, predictable
caching performance. Deploy inference endpoints using Amazon SageMaker AI with auto scaling configured based on predictable
traffic patterns rather than reactive scaling, providing
consistent latency even during traffic variations.

Tailor networking configurations to each environment's specific
needs using advanced VPC features. For research environments,
implement AWS Transit Gateway with increased bandwidth allocations
to support large data transfers. For clinical environments,
implement AWS Global Accelerator to provide consistent network
performance and AWS Shield Advanced for enhanced protection
against availability-impacting events.

Implement comprehensive monitoring tailored to each environment
using Amazon CloudWatch with custom metrics and dashboards. For
research environments, focus monitoring on resource utilization
and throughput metrics. For clinical environments, prioritize
monitoring of latency percentiles, error rates, and availability
metrics with automated alerting through Amazon SNS when
performance deviates from established baselines.

### Implementation steps

- Assess workloads using AWS Well-Architected Tool.
- Deploy research models on SageMaker AI with spot instances.
- Configure clinical systems with Multi-AZ architecture.
- Implement FSx for Lustre for high-throughput processing.
- Create CloudWatch dashboards for environment monitoring.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf03-bp03.html*

---
