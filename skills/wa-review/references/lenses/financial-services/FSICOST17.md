**Pillar**: Cost Optimization

# FSICOST17: Are you continually reviewing your workload to provide the most cost-effective resources?

There are multiple factors that affect the architecture, for example, new enhancements
related to business requirements, re-architecting your workload to improve efficiency, new
services released by AWS, price changes by AWS, or your team creating an MVP product
with services without considering costs. It is necessary to continually review the
architecture and resources used by your workload.

## FSICOST17-BP01 Assess workload architecture to identify the most cost-effective resources

There are multiple factors that affect the architecture, for example, new
enhancements related to business requirements, re-architecting your workload to improve
efficiency, new services released by AWS, price changes by AWS, or your team creating
an MVP product with services without considering costs. It is necessary to assess the
architecture and resources used by workload, for example, usage of serverless
technologies, managed services to reduce the operational overhead, or AWS Graviton-based
instances that meet your needs. Alternatively, you can refactor your monolithic
application to run as microservices. Most of the FSI systems are API-driven, so splitting
them across a number of diverse services helps procurement, and the right-sizing of
related resources.

**Review**

Continuously re-assess whether managed generative AI services (for example, Amazon
Bedrock or Amazon Q) or self-managed open-model stacks offer the best price-performance and
governance balance for your risk and compliance constraints.

For highly regulated workloads, periodically benchmark in-house fine-tuned models
against Bedrock-hosted foundation models to verify that the chosen deployment pattern
continues to meet cost, latency, and compliance requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost17.html*
