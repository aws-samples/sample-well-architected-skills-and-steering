# LSPERF05 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF05-BP01 Specialized hardware matching

Deploy purpose-built compute configurations optimized for specific
workload types. Use GPUs for molecular dynamics and AI drug
discovery, high-memory systems (4-8GB RAM per core) for genomics
assembly, and high-IOPS storage architectures for sequencing data
processing.

**Desired outcome:** Implement
specialized computing environments (GPU-accelerated, high-memory,
and high-IOPS storage) that enhance performance and cost-efficiency
across molecular dynamics, AI drug discovery, genomics assembly, and
sequencing data processing workloads.

**Common anti-patterns:**

- Deploying GPU clusters without sufficient memory bandwidth,
creating processing bottlenecks.
- Provisioning high-memory systems with inadequate I/O
capabilities, causing data starvation.
- Selecting hardware solely for compute power while ignoring
interconnect speeds critical for HPC workloads.
- Standardizing on single OS configurations incompatible with
specialized bioinformatics tools.
- Underestimating storage IOPS requirements for high-throughput
sequencing pipelines.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Match purpose-built compute configurations to specific life
science workload types. This provides maximum computational
throughput while avoiding overprovisioning expensive resources.

Accelerate critical healthcare advancements with purpose-built
computational infrastructure. Strategic hardware deployment
removes processing bottlenecks, enabling researchers and
clinicians to achieve breakthrough insights and advance patient
care more rapidly.

Select hardware that can adapt to evolving research requirements.
Life sciences workloads evolve rapidly, requiring infrastructure
that can scale and adapt to new computational methods.

Provide appropriate resource allocation for cross-functional
teams. Consistent compute environments provide scientific
reproducibility and facilitate collaboration between researchers,
clinicians, and data scientists.

### Implementation steps

- Profile and benchmark workloads to establish baselines and
identify consumption patterns.
- Categorize workloads by resource needs and document
performance requirements.
- Deploy specialized hardware with GPUs, high-memory systems,
and high-IOPS storage.
- Monitor utilization, measure metrics, and review hardware
effectiveness regularly.
- Establish standards, approval processes, and refresh
strategies for hardware.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf05-bp01.html*

---

# LSPERF05-BP02 Establish a tiered infrastructure strategy

Implement a layered approach organizing systems by criticality,
optimizing resources, enhancing resilience, and aligning technology
investments with business priorities for more effective
infrastructure management.

**Desired outcome:** A resilient,
cost-effective infrastructure with optimized resource allocation
that aligns with business criticality, enhances scalability, and
provides appropriate protection levels for different system tiers.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish a cohesive cloud-native architecture. This unified
approach creates a seamless computational fabric that uses the
strengths of cloud environments while appearing as a single
resource pool.

Design a strategic resource distribution across cloud services and
regions. This approach provides reliable core services while
enabling elasticity to handle variable computational demands
cost-effectively.

Create unified data access patterns within the cloud environment.
Effective data management reduces duplicated storage costs and
provides computational tasks with access required datasets
regardless of execution location.

Implement workflow tools that can intelligently distribute tasks
across the entire resource pool. Smart orchestration verifies that
workloads run in the optimal environment based on current
conditions and requirements.

Develop comprehensive management practices for the cloud
environment. Unified operations assist the cloud architecture to
function efficiently and meet governance requirements across
deployment contexts.

### Implementation steps

- Assess workloads by analyzing requirements and identifying
cloud-suitable applications.
- Implement cloud bursting with automatic scaling and
efficient data synchronization.
- Deploy data management with consistent access and automated
staging mechanisms.
- Configure orchestration tools with decision rules and
monitoring feedback loops.
- Create unified governance with standardized monitoring,
security, and cost tracking.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf05-bp02.html*

---

# LSPERF05-BP03 Implement a comprehensive system optimization strategy

Establish comprehensive workload profiling, benchmarking, and
monitoring practices covering each computational aspect (compute,
memory, storage, and network), enabling data-driven decisions for
resource allocation and identifying bottlenecks before they impact
research timelines.

**Desired outcome:** Implement
comprehensive workload monitoring across compute, memory, storage,
and network resources to enable data-driven optimization,
proactively identify bottlenecks, and provide efficient resource
allocation for timely research delivery.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a systematic approach to measure each aspect of
computational workload performance. Comprehensive profiling
creates visibility across the entire resource spectrum and
provides baseline metrics for future comparisons.

Execute controlled performance testing to quantify resource
requirements accurately. Structured benchmarking provides
objective data for making architecture decisions and validating
vendor performance claims.

Implement real-time performance tracking to detect emerging issues
before they impact research. Proactive monitoring blockes
unexpected delays in critical research pipelines through early
identification of resource constraints.

Base infrastructure decisions on quantified performance metrics
rather than assumptions. Data-driven allocation deploys resources
where they will have the greatest impact on research outcomes.

Build organizational capabilities around performance optimization
and bottleneck identification. A performance-aware culture
continuously improves computational efficiency across research
activities.

### Implementation steps

- Establish multi-dimensional profiling tools with
standardized metrics for applications.
- Implement benchmark protocols with standardized testing and
comparative analysis.
- Configure monitoring with alerts, trend analysis, and
resource visibility dashboards.
- Establish allocation processes with impact-based priorities
and forecasting models.
- Build capabilities through staff training and cross-team
optimization sharing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf05-bp03.html*

---
