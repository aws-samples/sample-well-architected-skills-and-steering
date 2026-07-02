**Pillar**: Cost Optimization

# FSICOST02: Do you apply the Pareto-principle (80/20 rule) to manage, optimize, and plan your cloud usage and spend?

Investing the right amount of effort in a cost optimization strategy up front allows
you to realize the economic benefits of the cloud more readily, by ensuring a consistent
adherence to best practices and avoiding unnecessary over provisioning. CFM is paramount not
only to effectively manage costs, but also to verify that investments are driving expected
business outcomes.

## FSICOST02-BP01 Apply the Pareto-principle 80/20 rule for your CFM efforts

No matter your organization size, pay specific attention to your capacity investment
while developing CFM-related concepts. Here are some examples of CFM activities to apply
the 80/20 rule to create an optimal input and output solution.

- **Cost allocation:** Start with default allocation
opportunities (per AWS account, AWS-generated createdBy tag), then follow up by
tagging all AWS services that support tagging, check overall percentage of cost
allocation. For generative AI workloads, implement specific tags for model selection,
inference costs, and vector store usage. In case you reach 80% cost allocation, check
if equal allocation of the unallocated 20% of costs is acceptable for your
organization (for example, splitting AWS service cost equally between business units
or teams). Before spending time and budget on a third-party solution (for example,
telemetry) ensure that shared resources you aim to allocate are substantial (for
example, over 20% of monthly bill).
- **Cost optimization:** Incorporate implementation of
low-hanging cost optimization recommendations (from Cost Explorer or AWS Trusted Advisor) into daily
activities of your teams. Centralized teams evaluate and book SP and RI quarterly,
decentralized teams perform instance rightsizing and modernization weekly. For
generative AI workloads, analyze and optimize the generative AI pricing model for your
most-used services. Implement cost-aware prompting for frequently used applications.
Optimize cost-informed vector stores for your highest-volume data. Review and refine
cost-informed agents in your most critical automated workflows. CFM practitioners
report it is more efficient to spend 30 minutes per week rather than one day per
month. While implementing cost optimization that requires technical changes, pay
attention to long term benefits, as one-time adjustments can provide reoccurring
savings. Evaluate time and capacity invested into technical adjustments versus cost
saving for at least the next 24 months. These types of calculations help prioritize
activities with the highest impact. Target the top 20% of prompts or flows that drive
~80% of generative AI spend. Apply caching (RAG result caches), prompt trims, and
model downgrades (for example, from large general models to smaller task‑specific
models) on those paths first.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost02.html*
