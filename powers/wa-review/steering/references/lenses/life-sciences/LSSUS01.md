# LSSUS01 — Research computing optimization

**Pillar**: Sustainability  
**Best Practices**: 2

---

# LSSUS01-BP01 Design high-performance computing workloads to minimize energy usage

Design research computing workloads to optimize resource utilization
and minimize energy consumption through strategic workload
separation and queue management. Implement compute environments that
align with specific computational demands to maximize hardware
efficiency and reduce idle time. Use multi-queue strategies that
match workload characteristics to appropriate compute resources,
enabling concurrent processing of diverse research tasks while
minimizing environmental impact.

**Desired outcome:** Achieve optimal
resource utilization across research computing infrastructure while
reducing energy consumption and operational costs. Implement
workload-specific compute environments that maximize hardware
efficiency for different types of life sciences analyses.

**Common anti-patterns:**

- You run computational workloads on the same compute environment
regardless of resource requirements.
- You don't implement queue management strategies to optimize
resource allocation.
- You use oversized compute instances for lightweight
computational tasks.
- You don't use spot instances for fault-tolerant research
workloads.
- You run compute resources continuously without considering
actual utilization patterns.
- You don't separate CPU-intensive, GPU-intensive, and
memory-intensive workloads.

**Benefits of establishing this best
practice:**

- Reduce energy consumption and carbon footprint of research
computing operations.
- Lower operational costs through optimized resource utilization
and spot instance usage.
- Enable concurrent processing of diverse research workloads
without resource conflicts.
- Achieve better cost predictability through workload-specific
resource allocation.
- Support regulatory requirements for sustainable research
practices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Research computing workloads in life sciences vary significantly
in their resource requirements, from CPU-intensive sequence
alignment to GPU-accelerated molecular dynamics simulations.
Implementing workload-specific compute environments verifies that
each type of analysis runs on optimally configured resources,
reducing both energy consumption and costs. This approach is
particularly important for life sciences organizations that must
balance research productivity with sustainability goals while
maintaining adherence to regulatory requirements.

Consider the computational characteristics of your research
workloads when designing compute environments. Genomics pipelines
typically require high CPU and memory resources, while protein
structure prediction benefits from GPU acceleration. By separating
these workloads into dedicated environments, you can achieve
better resource utilization and reduce energy waste from oversized
or underutilized compute instances.

### Implementation steps

- Analyze and categorize your research computing workloads by
resource requirements:

Profile CPU, memory, and GPU utilization patterns for
different analysis types.
- Use AWS Compute Optimizer to identify optimal instance
types for each workload category.
- Consider AWS Batch for orchestrating containerized
research workloads.

- Design compute environments aligned with workload
characteristics:

Create CPU-optimized environments for sequence alignment
and variant calling.
- Configure GPU-optimized environments for molecular
dynamics and deep learning.
- Set up memory-optimized environments for genome assembly
and phylogenetic analysis.
- Consider AWS ParallelCluster for HPC workload
management.

- Implement multi-queue strategy for efficient resource
allocation:

Configure high-priority queues for time-sensitive
analyses using on-demand instances.
- Set up spot instance queues for fault-tolerant workloads
like Monte Carlo simulations.
- Use Amazon EC2 Spot Fleet for cost-effective processing
of batch workloads.
- Implement AWS Batch job queues with different compute
environments.

- Enable automated scaling and resource optimization:

Configure auto scaling policies based on queue depth and
resource utilization.
- Use AWS Auto Scaling to automatically adjust compute
capacity.
- Implement scheduled scaling for predictable workload
patterns.
- Monitor resource utilization with Amazon CloudWatch
metrics.

- Establish monitoring and optimization processes:

Track energy efficiency metrics using normalized compute
hours per analysis.
- Monitor cost and utilization patterns with AWS Cost Explorer.
- Set up alerts for underutilized resources using Amazon CloudWatch alarms.
- Regularly review and optimize compute environment
configurations.

## Resources

**Related best practices:**

- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)
- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)

**Related documents:**

- [Accelerating
Life Sciences Research with HPC on AWS](https://pages.awscloud.com/rs/112-TZM-766/images/2018_0517-CMP_Slide-Deck.pdf)
- [Navigating
GPU Challenges: Cost Optimizing AI Workloads on AWS](https://aws.amazon.com/blogs/aws-cloud-financial-management/navigating-gpu-challenges-cost-optimizing-ai-workloads-on-aws/)

**Related videos:**

- [AWS re:Invent 2023 - HPC on AWS for semiconductors and healthcare
life sciences (CMP214)](https://www.youtube.com/watch?v=K-2d-pqe5nU)
- [AWS Summit 2023 - Building sustainable research computing on
AWS](https://www.youtube.com/watch?v=example)

**Related examples:**

- [HPC
Workloads on AWS](https://github.com/aws-samples/aws-hpc-recipes)
- [AWS Batch for Life Sciences](https://github.com/aws-samples/aws-batch-genomics)
- [Genomics
Workflows on AWS](https://github.com/aws-samples/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch)

**Related tools:**

- [AWS Batch](https://aws.amazon.com/batch/)
- [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus01-bp01.html*

---

# LSSUS01-BP02 Use energy efficient hardware and services

Select energy-efficient hardware architectures and managed services
that optimize power consumption while maintaining research computing
performance. Prioritize modern processor architectures and cloud
services that incorporate built-in sustainability optimizations to
reduce the environmental impact of computational workloads.
Implement hardware and service selection strategies that balance
performance requirements with energy efficiency goals.

**Desired outcome:** Achieve
significant energy consumption reduction in research computing
operations while maintaining or improving computational performance.
Implement hardware and service architectures that provide optimal
performance-per-watt ratios for life sciences workloads.

**Common anti-patterns:**

- You default to traditional x86 architectures without evaluating
energy-efficient alternatives.
- You don't consider managed services that provide built-in
sustainability optimizations.
- You don't evaluate the total cost of ownership including energy
consumption.
- You run custom infrastructure instead of using optimized managed
services.
- You don't monitor and measure energy efficiency metrics across
your compute infrastructure.

**Benefits of establishing this best
practice:**

- Reduce energy consumption by up to 60% through modern processor
architectures like AWS Graviton.
- Lower operational costs through improved performance-per-watt
ratios.
- Improve research productivity with automatically optimized
resource allocation.
- Support organizational sustainability goals and regulatory
adherence requirements.
- Benefit from continuous service improvements and optimizations
provided by managed services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Energy-efficient hardware selection is crucial for life sciences
organizations seeking to reduce their environmental impact while
maintaining research computing capabilities. Modern processor
architectures like AWS Graviton processors offer significant
energy efficiency improvements over traditional x86 architectures,
particularly for compute-intensive workloads common in genomics,
proteomics, and molecular modeling. These efficiency gains
compound over time, making hardware selection a critical
sustainability decision.

Managed services provide additional sustainability benefits by
incorporating built-in optimizations that individual organizations
would struggle to implement independently. Services like AWS HealthOmics, AWS HealthLake, and AWS Batch continuously
optimize resource utilization, automatically scale based on
demand, and use the latest energy-efficient infrastructure
improvements. This approach allows research teams to focus on
scientific outcomes while benefiting from ongoing sustainability
improvements.

### Implementation steps

- Evaluate and migrate to energy-efficient processor
architectures:

Assess workload compatibility with AWS Graviton
processors for ARM-based computing.
- Use Amazon EC2 M6g, C6g, and R6g instances for
general-purpose, compute-optimized, and memory-optimized
workloads.
- Benchmark performance and energy consumption for
representative research workloads.
- Consider AWS Graviton3 processors for the latest
efficiency improvements.

- Use managed services with built-in sustainability
optimizations:

Migrate genomics workflows to AWS HealthOmics for
automated resource optimization.
- Use AWS HealthLake for healthcare data processing
with built-in efficiency features.
- Implement AWS Batch for containerized workloads with
automatic scaling and optimization.
- Consider Amazon SageMaker AI for machine learning workloads
with energy-efficient training.

- Optimize service configurations for energy efficiency:

Enable AWS Auto Scaling to automatically adjust capacity
based on demand.
- Configure AWS Lambda for event-driven processing to
minimize idle resource consumption.
- Use Amazon ECS with AWS Fargate for serverless container
execution.
- Implement AWS Step Functions for efficient workflow
orchestration.

- Monitor and measure energy efficiency improvements:

Track performance-per-watt metrics using Amazon CloudWatch custom metrics.
- Monitor cost savings and energy reduction.
- Implement AWS Config rules to adhere to energy
efficiency policies.

- Establish continuous optimization processes:

Regularly review AWS service updates for new energy
efficiency features.
- Conduct periodic assessments of hardware and service
selection decisions.
- Set up automated alerts for suboptimal resource
utilization patterns.
- Create feedback loops to incorporate energy efficiency
learnings into future architecture decisions.

## Resources

**Related best practices:**

- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)

**Related documents:**

- [Improving
Sustainability and Price Performance Using AWS Graviton–Based
Instances with Pinterest](https://aws.amazon.com/solutions/case-studies/pinterest-graviton-case-study/)

**Related videos:**

- [How
to optimize workloads for sustainability using AWS
Graviton-based EC2 instances](https://www.youtube.com/watch?v=pzSvcsduijM&t=804s)

**Related examples:**

- [AWS Graviton Getting Started](https://github.com/aws/aws-graviton-getting-started)
- [AWS HealthOmics Workflows](https://github.com/aws-samples/amazon-omics-tutorials)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus01-bp02.html*

---
