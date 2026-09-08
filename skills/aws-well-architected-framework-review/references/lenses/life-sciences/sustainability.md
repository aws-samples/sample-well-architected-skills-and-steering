# Sustainability

**Pillar**: Sustainability  
**Questions**: 5

---

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

# LSSUS02 — Sustainability metric tracking and reporting

**Pillar**: Sustainability  
**Best Practices**: 1

---

# LSSUS02-BP01 Implement sustainability proxy metrics pipeline for research workloads

Establish comprehensive tagging strategies and normalized metrics to
track and measure sustainability performance across research
workloads. Implement proxy metrics that correlate resource
consumption with research outputs to enable meaningful comparisons
and optimization opportunities. Create sustainability KPIs that
combine resource utilization data with research milestones to drive
continuous improvement in energy efficiency and environmental
impact.

**Desired outcome:** Establish
measurable sustainability metrics that enable data-driven
optimization of research workloads and provide clear visibility into
environmental impact across different research activities and
architectural patterns.

**Common anti-patterns:**

- You don't implement consistent tagging strategies across
research workloads and resources.
- You measure absolute resource consumption without normalizing
for research outputs.
- You don't establish baseline metrics to track sustainability
improvements over time.
- You collect metrics but don't integrate them into research
workflow planning and optimization.
- You don't correlate resource consumption with actual research
deliverables and milestones.
- You rely solely on cost metrics without considering
environmental impact measurements.
- You don't establish regular review cycles to assess and act on
sustainability metrics.

**Benefits of establishing this best
practice:**

- Enable data-driven decisions for optimizing research workload
sustainability.
- Provide clear visibility into environmental impact across
different research activities.
- Support regulatory adherence and sustainability reporting
requirements.
- Align research operations with organizational sustainability
goals and commitments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Sustainability metrics for research workloads require a strategic
approach that balances measurement granularity with practical
implementation. Life sciences organizations must track resource
consumption in ways that correlate with research outputs, enabling
meaningful comparisons across different types of analyses and
computational approaches. This is particularly important given the
diverse nature of life sciences computing, from high-throughput
genomics processing to complex molecular modeling simulations.

Proxy metrics serve as practical indicators of sustainability
performance when direct energy measurements are not feasible. By
normalizing resource consumption against research outputs (such as
vCPU hours per genome processed or GPU hours per molecular
structure analyzed), organizations can identify optimization
opportunities and track improvements over time. Integration with
the AWS Customer Carbon Footprint Tool provides additional context
by correlating proxy metrics with actual carbon footprint data.

### Implementation steps

- Establish comprehensive tagging strategy for research
workloads:

Implement consistent tags for research type (genomics,
proteomics, drug discovery).
- Tag resources by project phase (discovery, validation,
production).
- Include architectural pattern tags (batch processing,
interactive analysis, real-time).
- Use AWS Resource Groups and Tag Editor for centralized
tag management.

- Define and implement normalized sustainability metrics:

Calculate vCPU hours per genome processed for genomics
workloads.
- Track GPU hours per molecular structure analyzed for
computational chemistry.
- Measure storage efficiency through data processed per TB
stored.
- Use Amazon CloudWatch custom metrics to track normalized
performance indicators.

- Create sustainability KPIs aligned with research outputs:

Combine resource utilization metrics with research
milestone achievements.
- Track energy efficiency improvements over time using
baseline comparisons.
- Implement cost-per-research-output metrics for
comprehensive sustainability assessment.
- Use AWS Cost and Usage Reports for detailed resource
consumption analysis.

- Integrate metrics with AWS Customer Carbon Footprint Tool:

Correlate proxy metrics with account and Region-level
carbon footprint data.
- Establish regular reporting cycles for sustainability
performance.
- Create dashboards that combine resource efficiency with
environmental impact.
- Use Quick for sustainability reporting and
visualization.

- Establish continuous monitoring and optimization processes:

Integrate sustainability metrics into research workflow
planning.
- Conduct regular sustainability reviews with research
teams.
- Create feedback loops to incorporate sustainability
learnings into future research planning.

## Resources

**Related best practices:**

- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS01-BP02
Leverage energy efficient hardware and services](lssus01-bp02.html)
- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)

**Related documents:**

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)

**Related examples:**

- [AWS Solutions for Sustainability](https://aws.amazon.com/solutions/sustainability/)

**Related tools:**

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus02-bp01.html*

---

# LSSUS03 — Data management efficiency in data analytics and data lifecycle

**Pillar**: Sustainability  
**Best Practices**: 2

---

# LSSUS03-BP01 Optimize data management for sustainability in life sciences

Implement data management practices that reduce redundant storage,
optimize processing efficiency, and minimize data movement while
maintaining regulatory requirements. Establish centralized data
catalogs and automated lifecycle policies to optimize your storage
tier utilization based on access patterns. Design data architectures
that balance accessibility requirements with energy efficiency
goals.

**Desired outcome:** Achieve
significant reduction in storage footprint and energy consumption
through optimized data lifecycle management, deduplication
strategies, and intelligent storage tiering while maintaining
adherence to life sciences regulatory requirements.

**Common anti-patterns:**

- You store data in the same storage tier regardless of access
patterns or lifecycle requirements.
- You don't implement deduplication strategies for redundant
research datasets.
- You move large datasets frequently between regions or storage
systems without considering energy impact.
- You don't establish data retention policies aligned with
regulatory requirements and business needs.
- You maintain multiple copies of reference datasets across
different research projects.
- You don't use compression techniques for archival and
infrequently accessed data.
- You don't monitor storage utilization and costs to identify
optimization opportunities.

**Benefits of establishing this best
practice:**

- Reduce storage costs through intelligent lifecycle management
and tiering.
- Lower energy consumption of storage systems by using optimal
storage classes.
- Improve data accessibility through centralized cataloging and
metadata management.
- Improve regulatory adherence through automated retention and
archival policies.
- Reduce data transfer costs and energy consumption through
strategic data placement.
- Enable better research collaboration through shared,
deduplicated reference datasets.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Life sciences organizations generate and consume vast amounts of
data across research, clinical, and manufacturing operations.
Effective data management for sustainability requires
understanding data access patterns, regulatory retention
requirements, and the energy implications of different storage
approaches. The key is implementing automated policies that
transition data through appropriate storage tiers while
maintaining accessibility for research and regulatory needs.

Centralized data catalogs play a crucial role in reducing
redundancy and improving data discoverability. By implementing
services like AWS Lake Formation for research data or AWS HealthLake for healthcare data, organizations can remove duplicate
datasets, improve data governance, and reduce overall storage
requirements. This approach is particularly important for
reference datasets, genomic databases, and clinical trial data
that may be accessed across multiple research projects.

### Implementation steps

- Establish centralized data catalogs and governance:

Centralize the management of data by implementing
services such as AWS Lake Formation for research data
cataloging and governance.
- Use data lakes such as AWS HealthLake for healthcare and
clinical data management.
- Create standardized metadata schemas for different data
types.
- Establish data ownership and access control policies.

- Implement intelligent storage lifecycle management:

Configure lifecycle policies to automatically transition
data between storage classes.
- Use Amazon S3 Standard for active research data
requiring frequent access.
- Implement dynamic tiering for data with changing or
unknown access patterns.
- Archive audit and reference data to durable, infrequent
access storage such as Amazon Glacier or S3 Glacier Deep Archive.

- Deploy deduplication and compression strategies:

Implement data deduplication for reference datasets and
genomic databases.
- Use compression algorithms appropriate for different
data types (genomic, imaging, clinical).
- Use service compression features for automated
optimization.
- Create shared reference datasets to remove redundant
storage across projects.

- Optimize data placement and movement:

Analyze data access patterns.
- Implement regional data placement strategies to minimize
transfer costs.
- Use transfer services such as AWS DataSync for efficient
data transfer and synchronization.
- Consider AWS Storage Gateway for hybrid storage
optimization.

- Monitor and continuously optimize storage efficiency:

Use AWS Cost Explorer to track storage costs and
utilization patterns.
- Implement Amazon CloudWatch metrics for storage
efficiency monitoring.
- Set up automated alerts for storage anomalies and
optimization opportunities.
- Conduct regular reviews of data lifecycle policies and
storage class effectiveness.

## Resources

**Related best practices:**

- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)

**Related documents:**

- [Sustainability
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/)

**Related videos:**

- [AWS re:Invent 2024 - Build and optimize a data lake on Amazon S3
(STG323)](https://www.youtube.com/watch?v=SIGpBvmlick)
- [AWS re:Invent 2024 - Data-driven sustainability with AWS
(SUS201)](https://www.youtube.com/watch?v=nA5WqgM7Jt0)
- [Securely
Store, Transform, Query and Analyze Health Data with AWS HealthLake](https://www.youtube.com/watch?v=a5WInyTti74)

**Related examples:**

- [Guidance
for Data Lakes on AWS](https://aws.amazon.com/solutions/guidance/data-lakes-on-aws/)

**Related tools:**

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS HealthLake](https://aws.amazon.com/healthlake/)
- [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
- [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/)
- [AWS DataSync](https://aws.amazon.com/datasync/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus03-bp01.html*

---

# LSSUS03-BP02 Process data closer to source

Optimize data processing locations to minimize network usage and
reduce energy consumption associated with data movement. Implement
edge computing and hybrid architectures that process large datasets
near their generation points, particularly for bandwidth-intensive
applications like genomic sequencing and imaging workflows. Use
managed services that provide optimized resource utilization and
automatic scaling to reduce infrastructure overhead.

**Desired outcome:** Significantly
reduce network bandwidth usage and associated energy consumption by
processing data at optimal locations relative to data sources, while
maintaining processing performance and regulatory requirements.

**Common anti-patterns:**

- You transfer large datasets to centralized processing locations
without considering network and energy costs.
- You don't evaluate edge computing options for
bandwidth-intensive research applications.
- You process data in regions distant from data generation points
without justification.
- You don't consider data sovereignty and regulatory requirements
when choosing processing locations.
- You transfer raw data for processing instead of implementing
preprocessing at the edge.

**Benefits of establishing this best
practice:**

- Reduce network bandwidth costs and energy consumption for large
dataset processing.
- Improve processing performance by reducing network latency for
data-intensive operations.
- Lower infrastructure costs through optimized resource
utilization and managed service adoption.
- Enhance data security and regulatory adherence by minimizing
data movement across network boundaries.
- Enable real-time processing capabilities for time-sensitive
research applications.
- Support hybrid and multi-cloud architectures that optimize for
both performance and sustainability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Life sciences research generates massive datasets that
traditionally require significant network resources to transfer to
centralized processing locations. This approach is particularly
inefficient for applications like genomic sequencing,
cryo-electron microscopy, and high-resolution imaging where raw
data volumes can reach terabytes per experiment. Processing data
closer to its source reduces both network energy consumption and
processing latency while often improving overall system
performance.

Edge computing and hybrid architectures become essential when
dealing with specialized equipment that generates large amounts of
data continuously. For example, cryo-EM facilities, genomic
sequencers, and imaging systems can benefit significantly from
local preprocessing that reduces data volumes before cloud
transfer. AWS services like AWS Outposts enable on-premises
processing with cloud tools, while managed services provide
automatic optimization without requiring dedicated infrastructure
management.

### Implementation steps

- Analyze data generation patterns and processing
requirements:

Map data sources and their typical output volumes and
processing needs.
- Identify bandwidth-intensive workflows that would
benefit from edge processing.
- Assess regulatory requirements for data processing
locations.
- Use and application discovery service to understand
current data flow patterns.

- Implement edge computing solutions for high-volume data
sources:

Deploy edge compute solution such as AWS Outposts for
on-premises processing of large genomic datasets.
- Use AWS Snow Family devices for data processing in
remote or bandwidth-constrained locations.
- Implement IoT edge processing of sensor and instrument
data.
- Consider AWS Wavelength for ultra-low latency processing
requirements.

- Use managed services for optimized data processing:

Use services such as Amazon Kinesis Data Streams for
real-time data processing and analytics.
- Implement AWS Transfer Family for optimized file
transfer and processing workflows.
- Deploy AWS Batch at edge locations for containerized
processing workloads.
- Use Amazon SageMaker AI Edge for machine learning inference
at data sources.

- Optimize data preprocessing and filtering at source
locations:

Implement data compression and filtering before cloud
transfer.
- Use AWS Lambda@Edge for lightweight data processing and
transformation.
- Deploy containerized preprocessing pipelines using
Amazon ECS on AWS Outposts.
- Implement quality control and data validation at source
locations.

- Monitor and optimize data movement and processing
efficiency:

Track data transfer volumes and costs using FinOps tools
such as Cloud Intelligence Dashboards.
- Monitor processing performance and resource utilization
with Amazon CloudWatch.
- Use AWS X-Ray to trace data processing workflows and
identify optimization opportunities.
- Implement automated alerts for unusual data transfer
patterns or processing inefficiencies.

## Resources

**Related best practices:**

- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)
- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)

**Related documents:**

- [Sustainability
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/)
- [AWS Outposts Documentation](https://docs.aws.amazon.com/outposts/)
- [AWS Snow Family Documentation](https://docs.aws.amazon.com/snowball/)
- [Amazon Kinesis Data Streams Documentation](https://docs.aws.amazon.com/kinesis/)
- [AWS Transfer Family Documentation](https://docs.aws.amazon.com/transfer/)
- [Optimizing
data transfers for high throughput life science instruments
using AWS DataSync](https://aws.amazon.com/blogs/storage/optimizing-data-transfers-for-high-throughput-life-science-instruments-using-aws-datasync/)
- [Cloud
at the Edge for Healthcare and Life Sciences](https://d1.awsstatic.com/product-marketing/Outposts/AWS%20HCLS%20eBook.pdf)
- [Genomics
data and transfer storage use cases](https://aws.amazon.com/health/genomics/solutions/data-transfer-and-storage/)

**Related videos:**

- [AWS re:Invent 2024 - AWS wherever you need it: From the cloud to
the edge (HYB201)](https://www.youtube.com/watch?v=_1quMnn2TI0&list=PL2yQDdvlhXf-xkVwHXosPxQh6BdY5LMIc&index=8)

**Related examples:**

- [Guidance
for Optimizing Data Architecture for Sustainability on
AWS](https://aws.amazon.com/solutions/guidance/optimizing-data-architecture-for-sustainability-on-aws/)
- [Building
a GPU-enabled CryoEM workflow on AWS](https://aws.amazon.com/blogs/industries/building-a-gpu-enabled-cryoem-workflow-on-aws/)

**Related tools:**

- [AWS Outposts](https://aws.amazon.com/outposts/)
- [AWS Snow Family](https://aws.amazon.com/snow/)
- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/)
- [AWS Wavelength](https://aws.amazon.com/wavelength/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/)
- [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/)
- [Amazon SageMaker AI Edge](https://aws.amazon.com/sagemaker/edge/)
- [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/)
- [AWS X-Ray](https://aws.amazon.com/xray/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus03-bp02.html*

---

# LSSUS04 — Sustainability in manufacturing environments

**Pillar**: Sustainability  
**Best Practices**: 2

---

# LSSUS04-BP01 Continuously improve the monitoring of resource consumption

Implement comprehensive monitoring systems that track resource
consumption across manufacturing and laboratory equipment to enable
data-driven sustainability improvements. Deploy IoT sensors and
real-time monitoring solutions that provide visibility into energy
usage, material consumption, and operational efficiency patterns.
Establish predictive analytics capabilities that identify
optimization opportunities and support proactive maintenance
strategies.

**Desired outcome:** Achieve
comprehensive visibility into resource consumption patterns across
manufacturing operations, enabling data-driven decisions that reduce
energy usage, minimize waste, and optimize equipment efficiency
while maintaining production quality and regulatory adherence.

**Common anti-patterns:**

- You don't monitor resource consumption at the equipment level,
relying only on facility-wide measurements.
- You use fixed sampling rates for your equipment regardless of
operational patterns.
- You don't implement predictive maintenance based on resource
consumption patterns.
- You don't correlate resource consumption with production output
and quality metrics.
- You don't establish baseline measurements to track
sustainability improvements over time.

**Benefits of establishing this best
practice:**

- Reduce energy consumption through equipment optimization and
predictive maintenance.
- Minimize material waste and improve resource utilization
efficiency.
- Enable predictive maintenance that reduces equipment downtime
and extends asset lifecycles.
- Support regulatory adherence and sustainability reporting
requirements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Manufacturing environments in life sciences require sophisticated
monitoring approaches due to the critical nature of production
processes and strict regulatory requirements. Equipment such as
bioreactors, chromatography systems, and analytical instruments
consume significant resources while requiring precise operational
conditions. Implementing comprehensive monitoring enables
organizations to optimize resource consumption without
compromising product quality or regulatory adherence.

Real-time monitoring with IoT sensors provides granular visibility
into equipment performance and resource consumption patterns. This
data enables predictive analytics that can identify
inefficiencies, predict maintenance needs, and optimize
operational parameters for sustainability. The key is implementing
monitoring systems that balance data collection granularity with
processing efficiency, using adaptive sampling rates that respond
to operational conditions and baseline activity levels.

### Implementation steps

- Deploy IoT sensors for comprehensive equipment monitoring:

Install IoT sensors on critical manufacturing equipment
(bioreactors, HVAC systems, analytical instruments).
- Monitor energy consumption, water usage, compressed air
consumption, and waste generation.
- Use tools like AWS IoT Device Management for centralized
sensor configuration and management.
- Implement solutions such as AWS IoT Greengrass for edge
processing and local data aggregation.

- Establish real-time monitoring and data collection systems:

Use Amazon Kinesis Data Streams for real-time data
ingestion from manufacturing equipment.
- Implement AWS IoT Analytics for processing and analyzing
manufacturing data.
- Store time-series data in Amazon Timestream for
efficient querying and analysis.
- Create real-time dashboards using Quick for
operational visibility.

- Implement adaptive sampling and data efficiency strategies:

Configure dynamic sampling rates based on equipment
operational states.
- Use AWS IoT Rules Engine to filter and route data based
on operational conditions.
- Implement data compression and aggregation at the edge
to reduce network usage.
- Establish baseline activity monitoring to optimize data
collection frequency.

- Deploy predictive analytics for maintenance and
optimization:

Use Amazon SageMaker AI to build predictive models for
equipment maintenance.
- Implement anomaly detection using Amazon Lookout for
Equipment.
- Create predictive analytics for resource consumption
optimization.
- Use AWS Lambda for automated responses to monitoring
alerts and anomalies.

## Resources

**Related best practices:**

- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)
- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)

**Related documents:**

- [AWS IoT Core Documentation](https://docs.aws.amazon.com/iot/)
- [AWS IoT Analytics Documentation](https://docs.aws.amazon.com/iotanalytics/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus04-bp01.html*

---

# LSSUS04-BP02 Use digital twins to optimize resource usage through in silico experimentation

Implement digital twin technologies to create virtual
representations of manufacturing processes that enable in silico
experimentation and optimization without consuming physical
resources. Use these virtual environments to test different
operational scenarios, optimize process parameters, and minimize
resource consumption before implementing changes in physical
systems. Use simulation capabilities to reduce the need for physical
experiments while improving process efficiency and sustainability
outcomes.

**Desired outcome:** Significantly
reduce physical experimentation requirements and resource
consumption by using digital twins for process optimization, while
improving manufacturing efficiency and reducing time-to-market for
process improvements.

**Common anti-patterns:**

- You rely solely on physical experiments for process optimization
without considering digital simulation alternatives.
- You implement process changes without first testing them in
virtual environments.
- You don't use historical data to improve digital twin accuracy
and predictive capabilities.
- You don't validate digital twin predictions against real-world
outcomes to improve model accuracy.

**Benefits of establishing this best
practice:**

- Reduce physical experimentation costs and resource consumption.
- Accelerate process optimization cycles and reduce time-to-market
for improvements.
- Minimize material waste and energy consumption during process
development.
- Enable safe testing of extreme operational scenarios without
risk to physical equipment.
- Improve process understanding and predictive capabilities for
better decision-making.
- Support regulatory submissions with comprehensive simulation
data and analysis.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Digital twins in life sciences manufacturing provide unprecedented
opportunities to optimize processes while minimizing resource
consumption and environmental impact. These virtual
representations enable process development teams to explore
optimization scenarios that would be costly, time-consuming, or
potentially risky to test in physical systems. For example,
chromatography process optimization can involve testing hundreds
of parameter combinations virtually before implementing the most
promising approaches in actual equipment.

The effectiveness of digital twins depends on the quality of
underlying data and models. Life sciences manufacturing processes
often involve complex biochemical interactions that require
sophisticated modeling approaches. However, the investment in
creating accurate digital twins pays dividends through reduced
physical experimentation, faster optimization cycles, and improved
process understanding. Integration with real-time monitoring data
keeps digital twins accurate and provides valuable insights
throughout the manufacturing lifecycle.

### Implementation steps

- Identify and prioritize manufacturing processes for digital
twin development:

Assess processes with high resource consumption or
frequent optimization needs.
- Prioritize critical processes like chromatography,
fermentation, and purification.
- Evaluate data availability and modeling complexity for
each process.
- Use AWS IoT TwinMaker to create digital representations
of manufacturing equipment.

- Develop comprehensive digital twin models:

Create physics-based models using AWS SimSpace Weaver
for complex process simulations.
- Integrate historical process data using Amazon S3 and
AWS Glue for data preparation.
- Use Amazon SageMaker AI to build machine learning models
that enhance digital twin accuracy.
- Implement real-time data integration using AWS IoT Core
and Amazon Kinesis.

- Establish simulated experimentation capabilities:

Create simulation environments for testing different
operational scenarios.
- Implement parameter optimization algorithms using Amazon SageMaker AI.
- Use AWS Batch for running large-scale simulation
experiments.
- Develop automated experiment design and execution
workflows using AWS Step Functions.

- Integrate digital twin insights into manufacturing
operations:

Create dashboards using Quick for
visualizing simulation results.
- Implement automated recommendations based on digital
twin optimization results.
- Use AWS Lambda for real-time process adjustments based
on digital twin predictions.
- Establish feedback loops to continuously improve digital
twin accuracy.

- Validate and continuously improve digital twin performance:

Compare digital twin predictions with actual
manufacturing outcomes.
- Implement continuous learning capabilities using Amazon SageMaker AI.
- Establish regular model updates and validation cycles.

## Resources

**Related best practices:**

- [LSSUS04-BP01
Continuously improve the monitoring of resource
consumption](lssus04-bp01.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)
- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)

**Related documents:**

- [AWS IoT TwinMaker Documentation](https://docs.aws.amazon.com/iot-twinmaker/)
- [AWS SimSpace Weaver Documentation](https://docs.aws.amazon.com/simspaceweaver/)
- [Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/)
- [AWS Step Functions Documentation](https://docs.aws.amazon.com/step-functions/)

**Related examples:**

- [AWS IoT TwinMaker Samples](https://github.com/aws-samples/aws-iot-twinmaker-samples)

**Related tools:**

- [AWS IoT TwinMaker](https://aws.amazon.com/iot-twinmaker/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus04-bp02.html*

---

# LSSUS05 — Sustainability in clinical trials

**Pillar**: Sustainability  
**Best Practices**: 1

---

# LSSUS05-BP01 Design sustainable clinical trial architecture

Implement decentralized clinical trial architectures that minimize
data movement and reduce environmental impact through regional data
processing strategies and edge computing solutions. Design clinical
trial systems that process data closer to trial populations,
reducing network requirements while maintaining regulatory adherence
and data integrity. Use standardized data management services and
smart archiving strategies to optimize resource utilization
throughout the clinical trial lifecycle.

**Desired outcome:** Achieve
significant reduction in data transfer requirements and
environmental impact of clinical trials while improving data
accessibility, patient experience, and operational efficiency
through decentralized architectures and edge computing solutions.

**Common anti-patterns:**

- You centralize your clinical trial data processing without
considering regional or edge processing alternatives.
- You don't implement data filtering and aggregation at collection
points, transferring raw data.
- You use proprietary data formats instead of standardized formats
like FHIR for clinical data.
- You store your clinical trial data in the same storage tier
regardless of access patterns.
- You don't implement automated data archiving strategies aligned
with regulatory retention requirements.
- You don't consider patient travel reduction opportunities
through remote monitoring and virtual visits.

**Benefits of establishing this best
practice:**

- Reduce data transfer costs and energy consumption through edge
processing and regional architectures.
- Improve patient experience and reduce travel-related emissions
through decentralized trial designs.
- Lower operational costs through optimized data management and
automated archiving strategies.
- Enhance data accessibility and analysis capabilities through
standardized data formats.
- Support regulatory adherence through automated retention and
archiving policies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Clinical trials generate vast amounts of data from diverse sources
including electronic health records, patient-reported outcomes,
wearable devices, and medical imaging. Traditional centralized
approaches require significant data movement and processing
resources, contributing to environmental impact while potentially
creating bottlenecks in data analysis. Decentralized clinical
trial architectures address these challenges by processing data
closer to its source and implementing intelligent data management
strategies.

The shift toward decentralized clinical trials is driven by both
sustainability goals and improved patient outcomes. By
implementing edge computing solutions for patient monitoring and
regional data processing strategies, organizations can
significantly reduce data transfer requirements while maintaining
the high standards of data quality and regulatory adherence
required in clinical research. This approach also enables more
inclusive trial designs by reducing patient travel requirements
and supporting remote participation.

### Implementation steps

- Implement decentralized data collection and processing
architecture:

Deploy AWS IoT Greengrass at clinical sites for local
data filtering and aggregation.
- Implement AWS Direct Connect for secure, dedicated
connectivity between clinical sites.
- Configure AWS PrivateLink for secure communication
between decentralized components.

- Establish edge computing solutions for patient monitoring:

Deploy AWS IoT Core for device connectivity and data
ingestion from wearable devices.
- Use AWS IoT Greengrass for local processing of vital
signs and patient-reported outcomes.
- Implement Amazon Kinesis Data Streams for real-time data
processing at the edge.
- Configure AWS Lambda@Edge for lightweight data
transformation and filtering.

- Implement standardized clinical data management:

Use AWS HealthLake for FHIR-based clinical data
management and standardization.
- Implement Amazon S3 with intelligent tiering for
clinical trial data storage.
- Use AWS Glue for data integration and transformation
across different clinical data sources.
- Configure Amazon Redshift for clinical trial data
analytics and reporting.

- Deploy smart data archiving and lifecycle management:

Implement Amazon S3 lifecycle policies for automated
data archiving based on regulatory requirements.
- Use Amazon Glacier for long-term archival of
completed trial data.
- Configure AWS Config for monitoring and automated policy
enforcement.
- Implement AWS CloudTrail for comprehensive audit trails
of data access and modifications.

- Establish monitoring and optimization processes:

Use Amazon CloudWatch to monitor data transfer volumes
and processing efficiency.
- Establish regular reviews of decentralized architecture
performance and optimization opportunities.

## Resources

**Related best practices:**

- [LSSUS03-BP02
Process data closer to source](lssus03-bp02.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)
- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)

**Related documents:**

- [Advance
environmental sustainability in clinical trials using
AWS](https://aws.amazon.com/blogs/machine-learning/advance-environmental-sustainability-in-clinical-trials-using-aws/)
- [Successful
Decentralized Clinical Trials: A True Possibility with AWS in
the Post-Pandemic Era](https://aws.amazon.com/blogs/apn/successful-decentralized-clinical-trials-a-true-possibility-with-aws-in-the-post-pandemic-era/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus05-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
