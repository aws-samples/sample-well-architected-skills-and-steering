# ADVPERF02 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# ADVPERF02-BP01 Evaluate compute benchmarks and compute options certified by the ISVs if applicable

Evaluate ISV compatibility for running on AWS, and use the right resources based on
published benchmarking results.

## Implementation guidance

Aerospike's ISV product has been observed to be deployed for
high-volume customer adtech workloads due to its speed at scale,
real-time analytics capabilities, and strong data protection.

Databricks is a popular ISV platform used for advertising
workloads due to its capabilities in big data processing,
real-time capabilities and machine learning support. These
facets make it well-suited for the large-scale and fast-changing
needs of advertising analytics and intelligence.

Consider benchmark evaluation for
[Amazon EC2](https://aws.amazon.com/ec2/)
Intel and Graviton instances for Aerospike and Databricks.

## Resources

**Related documentation:**

- [Running
Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/)

**Related partner solutions:**

- [Database comparisons and performance benchmarks (Aerospike)](https://aerospike.com/resources/benchmarks/)
- [Running
operational workloads with Aerospike at petabyte scale in the cloud on 20 nodes](https://aerospike.com/resources/white-papers/running-operational-workloads/)
- Introducing the Well-Architected Data Lakehouse from
Databricks[6 Guiding Principles to Build an Effective Data Lakehouse](https://www.databricks.com/blog/2022/07/14/6-guiding-principles-to-build-an-effective-data-lakehouse.html)
- [Best
Practices for Cost Management on Databricks](https://www.databricks.com/blog/best-practices-cost-management-databricks)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp01.html*

---

# ADVPERF02-BP02 Consider containerization for scalability, low latency, and cost optimization

Adopt containerization as a strategy to operate at scale with low
latency and cost optimization. Evaluate the various options of
running container workloads on AWS.

## Implementation guidance

Consider containerization, which helps improve application
performance and helps scaling needs for adtech workloads, due to
the following benefits:

- **Faster startup times:**
Containers share the host OS kernel and start only the
necessary processes, so they can start almost instantly
compared to a full virtual machine (VM) startup. This makes
scaling up and down faster.
- **Lower resource usage:**
Containers require fewer resources than VMs, as there is no
guest OS overhead. More efficient resource usage leads to cost optimization and the ability to run more container instances per host.
- **Portability across
environments:** Container images can run on any
infrastructure due to standardized runtime without need to
re-optimize for different environments.
- **Scaling and availability:**
Container orchestrators (for example, Amazon EKS) help to
scale containerized apps, provide high availability, and
improve performance under heavy loads.
- **Isolation:** Containers
isolate processes and resources per application, reducing
noisy neighbor issues on multi-tenant hosts for more
predictable performance.
- **Utilization:** Higher
density of containers per host allows full utilization of
available resources, especially with auto scaling.
- **Microservices:**
Decomposing monoliths into containerized microservices
reduces interdependencies and allows independent scaling.

## Key AWS services

- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)

## Resources

- [Leveraging Amazon EKS managed node group with placement group for low latency critical applications](https://aws.amazon.com/blogs/containers/leveraging-amazon-eks-managed-node-group-with-placement-group-for-low-latency-critical-applications/)
- [Amazon ECS vs Amazon EKS: making sense of AWS container services](https://aws.amazon.com/blogs/containers/amazon-ecs-vs-amazon-eks-making-sense-of-aws-container-services/)
- [Under
the hood: Lazy Loading Container Images with Seekable OCI and AWS Fargate](https://aws.amazon.com/blogs/containers/under-the-hood-lazy-loading-container-images-with-seekable-oci-and-aws-fargate/)
- [Optimizing
your Kubernetes compute costs with Karpenter consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp02.html*

---

# ADVPERF02-BP03 Consider using low latency scaling tools like Karpenter to improve startup and scaling time

Integrate observability metrics to initiate scaling of compute
resources. Use open-source frameworks like Karpenter and KEDA,
which provide for low startup latency scaling.

## Implementation guidance

Karpenter (an open-source Amazon tool) for Kubernetes workloads
can help with low-latency scaling and bursty traffic patterns
for adtech workloads.

- **Faster node provisioning:**
Karpenter can provision new nodes in a Kubernetes cluster
much faster than traditional auto scaling methods, as
Karpenter integrates directly with AWS APIs and can use
services like Amazon EC2 Auto Scaling groups for rapid node
provisioning.
- **Node pre-warming:**
Although Karpenter does not support prewarmed node pools like Auto Scaling groups, you can use [pod priority](https://aws.amazon.com/blogs/containers/eliminate-kubernetes-node-scaling-lag-with-pod-priority-and-over-provisioning/) to maintain a pool of
pre-initialized nodes. When new nodes are needed, Karpenter
can quickly provision them from this pre-warmed pool,
further reducing the latency associated with node
provisioning.
- **Horizontal Pod Autoscaling (HPA)
integration:** Karpenter can be configured to work
in tandem with the Kubernetes Horizontal Pod Autoscaler
(HPA). This integration allows Karpenter to provision new
nodes proactively based on the HPA's scaling decisions,
which makes resources available before pods start
experiencing resource constraints.
- **Optimized node selection:**
Karpenter can provision nodes with the appropriate instance
types and resource configurations based on the requirements
of the workloads. This optimization schedules pods on nodes
with sufficient resources, minimizing the need for
rescheduling or resource contention, which can introduce
latency.
- **Parallel node
provisioning:** Karpenter can provision multiple
nodes in parallel, allowing it to rapidly scale out the
cluster when faced with sudden spikes in demand. This
parallelism helps minimize the overall latency associated
with scaling operations.

## Key AWS services

- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)

## Resources

- [Manage
scale-to-zero scenarios with Karpenter and Serverless](https://aws.amazon.com/blogs/containers/manage-scale-to-zero-scenarios-with-karpenter-and-serverless/)
- [Proactive autoscaling of Kubernetes workloads with KEDA using metrics ingested into Amazon Managed Service for Prometheus](https://aws.amazon.com/blogs/mt/proactive-autoscaling-kubernetes-workloads-keda-metrics-ingested-into-aws-amp/)
- [Scalable and Cost-Effective Event-Driven Workloads with KEDA and
Karpenter on Amazon EKS](https://aws.amazon.com/blogs/containers/scalable-and-cost-effective-event-driven-workloads-with-keda-and-karpenter-on-amazon-eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp03.html*

---

# ADVPERF02-BP04 Use a specialized instance family and features

For advertising workloads, consider using a specialized instance
family like compute-optimized for ad serving, storage-optimized
for in-memory database, Trainium-based for machine learning (ML),
and Inferentia-based for ML inferences.

## Implementation guidance

[Amazon EC2](https://aws.amazon.com/ec2/)
provides a

[wide
selection of instance types](https://aws.amazon.com/ec2/instance-types/) optimized to fit different
use cases.

The Amazon EC2 Compute Optimized instance family (C series) is a
great match for compute-intensive workloads such as batch
processing, media encoding, ad serving, bidding, and distributed
analytics.

The Amazon EC2 Storage Optimized instance family (I series) are
next-generation, storage-optimized instances designed to run
applications that require high throughput and real-time latency
access to data on local SSD storage. These instances help
customers running real-time database workloads with Aerospike,
where low latency local NVMe storage is required.

Amazon EC2 Accelerated Computing instances (powered by
[AWS Trainium](https://aws.amazon.com/machine-learning/trainium/)) are purpose built for high performance, deep
learning, and model training, while offering up to 50%
cost-to-train savings over comparable GPU-based instances.

AWS Inferentia accelerators are designed by AWS to deliver high
performance at the lowest cost in Amazon EC2 for your deep
learning (DL) and generative AI inference applications.

AWS Nitro Enclaves enables customers to create isolated compute environments to further help protect and securely process highly sensitive data such as personally identifiable information (PII) and intellectual property data within their Amazon EC2 instances. Nitro Enclaves assist customers to reduce the threat surface area for their most sensitive data processing applications. Enclaves offers an isolated, hardened, and highly constrained environment to host security-critical applications. Nitro Enclaves enables a range of use cases that deal with the processing of highly sensitive data, such as securing private keys, tokenization, and multi-party collaboration. The isolation, cryptographic attestation, and integration with AWS Key Management Service capabilities of Nitro Enclaves are key features that provide customers with a practical approach to setting up multi-party collaboration.

## Resources

- [Choosing
an AWS compute service](https://docs.aws.amazon.com/decision-guides/latest/compute-on-aws-how-to-choose/choosing-aws-compute-service.html)
- [Scaling
distributed training with AWS Trainium and Amazon EKS](https://aws.amazon.com/blogs/machine-learning/scaling-distributed-training-with-aws-trainium-and-amazon-eks/)
- [AWS Inferentia2 builds on AWS Inferentia1 by delivering 4x higher throughput and 10x lower latency](https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/)
- [Introducing Unified ID 2.0 Private Operator Services on AWS Using Nitro Enclaves](https://aws.amazon.com/blogs/industries/introducing-unified-id-2-0-private-operator-services-on-aws-using-nitro-enclaves/)
- [Use AWS Nitro Enclaves to perform computation of multiple sensitive datasets](https://aws.amazon.com/blogs/compute/leveraging-aws-nitro-enclaves-to-perform-computation-of-multiple-sensitive-datasets/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp04.html*

---

# ADVPERF02-BP05 Evaluate ARM architecture for performance considerations by using AWS Graviton

To address the low latency and high throughput needs of advertising workloads, consider
adopting ARM architecture using AWS Graviton for improved performance and cost optimization.

## Implementation guidance

Migrating to AWS Graviton processors can improve performance as
a result of the following:

- **Faster processing:**
Graviton uses 64-bit ARM Neoverse cores that are optimized
for speed and efficiency in cloud workloads. Benchmarks show
Graviton outperforming x86 instances for some workloads.
- **Lower latency:** The ARM
architecture and custom memory subsystem in Graviton reduces
latency for many operations compared to x86. This benefits
real-time and latency-sensitive applications.
- **Improved throughput:** Graviton's support for new
instructions like ARM Neon SIMD improves parallel processing throughput for workloads
like video encoding and transcoding.
- **Enhanced networking:** Up
to 25 Gbps of network bandwidth from the Nitro chip provides
high throughput for network-intensive apps.
- **Burstable performance:** Graviton's TDP and credits system allows workloads to burst performance as needed.
- **Accelerated compression:** Hardware-based compression provided by the Nitro chip speeds up compressed workloads.
- **Caching optimizations:**
Graviton optimizes cache utilization and memory access,
leading to gains for memory bound workloads.

## Key AWS services

- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)

## Resources

- [Optimizing
for performance](https://docs.aws.amazon.com/whitepapers/latest/aws-graviton2-for-isv/optimizing-for-performance.html)
- [Considerations
when transitioning workloads to AWS Graviton based Amazon EC2 instances](https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md)
- [Using
Porting Advisor for Graviton](https://aws.amazon.com/blogs/compute/using-porting-advisor-for-graviton/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf02-bp05.html*

---
