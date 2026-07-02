# MLSUS01 — Business goal identification

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MLSUS01-BP01 Define the overall environmental impact or benefit

Measure your workload's impact and its contribution to the overall
sustainability goals of the organization. Understand the
environmental footprint of machine learning systems to make informed
decisions about resource allocation and optimization.

**Desired outcome:** You gain a clear
understanding of how your ML workload impacts your organization's
sustainability objectives, including energy consumption, carbon
emissions, and resource utilization. You have established specific
sustainability objectives and success criteria to measure against,
which assists you when optimizing your ML workloads and
demonstrating their environmental value proposition in relation to
their impact.

**Common anti-patterns:**

- Focusing solely on model accuracy without considering
environmental trade-offs.
- Implementing ML systems without measuring their carbon
footprint.
- Overprovisioning resources for ML workloads.
- Unnecessarily retraining models when not required.

**Benefits of establishing this best
practice:**

- Improved alignment between ML initiatives and organizational
sustainability goals.
- Enhanced ability to meet regulatory and reporting requirements.
- Transparent assessment of the sustainability impact of ML
projects.
- Identification of opportunities to optimize ML systems for lower
environmental impact.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Understanding the environmental impact of your ML workloads is
essential for sustainable AI development. ML operations can be
resource-intensive, requiring substantial computing power for
training and inference, which translates to energy consumption and
carbon emissions. By measuring and tracking this impact, you can
make informed decisions about architecture choices, region
selection, and optimization strategies.

The cloud provides significant advantages for sustainable ML
development through its economies of scale and renewable energy
investments. By leveraging AWS's efficiency, you can reduce your
carbon footprint compared to on-premises alternatives. However,
you still need to make conscious decisions about how you design,
deploy, and operate your ML workloads.

Consider the full lifecycle of your ML system, from data
collection and processing to model training, deployment, and
ongoing operations. Each stage has different resource requirements
and environmental impacts. For example, training large models is
typically more computationally intensive than inference, but if
your model serves millions of predictions daily, the inference
stage might have a larger cumulative impact over time.

### Implementation steps

- **Establish sustainability objectives
for ML workloads**. Begin by defining specific
sustainability goals for your ML projects that align with
your organization's broader environmental commitments.
Determine what metrics you'll track (for example, carbon
emissions per training run or energy efficiency per
inference) and set concrete targets for improvement.
- **Assess the environmental impact of
data processing**. Evaluate how much data you're
storing and processing for your ML workloads. Consider
implementing data lifecycle management using
[Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) policies to automatically transition
infrequently accessed data to more efficient storage classes
or archive data that's no longer needed for active training.
- **Measure the impact of model
training**. Calculate the computational resources
and associated carbon emissions of your model training
processes using tools like the
[AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/). Consider factors such
as instance types, training duration, and region selection.
Track these metrics over time to identify trends and
opportunities for improvement.
- **Optimize model training frequency
and approach**. Determine how often retraining is
truly necessary based on model drift monitoring. Implement
incremental training where possible using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to update existing models with new data
rather than retraining from scratch. Use techniques like
transfer learning to leverage pre-trained models and reduce
computational requirements.
- **Assess inference
efficiency**. Evaluate the environmental impact of
your deployed models in production. Consider techniques like
model compression, quantization, and distillation to reduce
the computational requirements of inference while
maintaining acceptable accuracy. Use
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to automatically optimize models for
specific deployment targets.
- **Calculate the net sustainability
value**. Compare the environmental impact of your
ML workload with its benefits, including the sustainability
improvements it enables. For example, if your ML system
optimizes energy usage in manufacturing processes, calculate
the net reduction in emissions to demonstrate its overall
positive impact.
- **Implement ongoing monitoring and
reporting**. Establish a regular cadence for
reviewing sustainability metrics and reporting on progress
toward your goals. Use
[AWS CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor resource utilization and create
dashboards to track your sustainability KPIs over time.
- **For GenAI workloads, consider your
model customization strategy**. When implementing
generative AI solutions, evaluate whether fine-tuning
existing foundation models like
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) models is more environmentally efficient than
training custom models from scratch. Consider prompt
engineering and retrieval-augmented generation (RAG)
approaches that can achieve business goals with lower
computational intensity than full model training.

## Resources

**Related documents:**

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Sustainability Data Initiative](https://sustainability.aboutamazon.com/about/the-climate-pledge)
- [AWS Well-Architected Framework: Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [Corporate
Climate Action - Science Based Targets initiative
(SBTi)](https://sciencebasedtargets.org/)
- [Greenhouse Gas
Protocol](https://ghgprotocol.org/)
- [Optimize
AI/ML workloads for sustainability: Part 1, identify business
goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus01-bp01.html*

---
