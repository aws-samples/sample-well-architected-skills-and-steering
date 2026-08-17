# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 6

---

# ADVPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# ADVPERF01-BP01 Design geographical affinity architecture with external entities (DSPs and SSPs)

Design for the least-network path, but keep regulatory needs in
consideration. Use the AWS backbone network to improve latency.

## Implementation guidance

Implement Amazon Route 53 (fail-over and geolocation routing) to
route traffic to the target load balancers and compute workloads
in the closest Region to the origination of intake requests.
This architecture may help align with specific compliance and residency needs. Consult with legal counsel for guidance tailored to your specific use case and jurisdiction.

Implement AWS PrivateLink on the same Region between
external entities (like DSPs and SSPs) where both parties are on
AWS.

For privacy-enhanced collaboration using AWS Clean Rooms, it is recommended to have collaborators in the same Region as the clean room to avoid latency with cross-Region data transfer.

## Key AWS services

- [Amazon Route 53 (R53)](https://aws.amazon.com/route53/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)
- [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)

## Resources

- [Disaster
Recovery Solutions with AWS managed services, Part 3: Multi-Site Active/Passive](https://aws.amazon.com/blogs/architecture/disaster-recovery-solutions-with-aws-managed-services-part-3-multi-site-active-passive/)
- [How
Storygize and Sharethrough are using AWS PrivateLink to reduce costs and increase revenue](https://aws.amazon.com/blogs/industries/how-storygize-and-sharethrough-are-using-aws-privatelink-to-reduce-costs-and-increase-revenue/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp01.html*

---

# ADVPERF01-BP02 Use appropriate scaling to handle burst traffic with cost considerations

Consider start-up latency and scaling needs to handle burst
traffic for networking, compute, and storage resources.

## Implementation guidance

Network Load Balancer (NLB) and Application Load Balancer (ALB)
scaling parameters depend upon the following parameters:

- Overall number of long-lived connections
- New TCP/TLS connections per second expected
- Data transfer in GB per second expected

NLB scaling needs are driven by elastic network interface at the
Availability Zone level, whereas ALB scales across Availability
Zones.

Consider Load balancer Capacity Unit (LCU) reservation, which
you can use to proactively set a minimum capacity for your load
balancer. This capability complements the load balancer's
existing ability to auto scale based on your traffic pattern.
Implement load balancers with target groups (like Auto Scaling
groups).

For container workloads running on Amazon EKS, implement EKS
Auto Scaling:

- Set up horizontal scaling and node scaling using either
Cluster Autoscaler or Karpenter
- Set up pod scaling using horizontal pod scaling

Integrate with default Kubernetes metrics (like CPU and memory)
or extensive metrics (inputs like queue lengths, CPU usage, and
business metrics) using
[Kubernetes Event-driven
Autoscaling (KEDA)](https://keda.sh/).

For databases like Amazon Aurora, enable storage auto scaling,
which is a managed solution for storage expansion.

## Key AWS services

- [Amazon
Network Load Balancer (NLB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Amazon Elastic
Load Balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/)
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/)

## Resources

- [Auto
Scaling benefits for application architecture](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html)
- [Load
Balancer Capacity Unit Reservation for Application and Network Load Balancers](https://aws.amazon.com/about-aws/whats-new/2024/11/load-balancer-capacity-unit-reservation-application-balancers/)
- [Autoscaling
Amazon EKS services based on custom Prometheus metrics using CloudWatch Container Insights](https://aws.amazon.com/blogs/containers/autoscaling-amazon-eks-services-based-on-custom-prometheus-metrics-using-cloudwatch-container-insights/)
- [Autoscaling
Amazon ECS services based on custom metrics with Application Auto Scaling](https://aws.amazon.com/blogs/containers/autoscaling-amazon-ecs-services-based-on-custom-metrics-with-application-auto-scaling/)
- [How
ktown4u built a custom auto scaling architecture using an Amazon Aurora mixed-configuration cluster to respond to sudden traffic spikes](https://aws.amazon.com/blogs/database/how-ktown4u-built-a-custom-auto-scaling-architecture-using-an-amazon-aurora-mixed-configuration-cluster-to-respond-to-sudden-traffic-spikes/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp02.html*

---

# ADVPERF01-BP03 Design for low latency with appropriate compute, storage, and network considerations

Use features from AWS compute, storage, and network services that
cater to low latency advertising workload needs.

## Implementation guidance

Consider the following guidance for compute, storage, and
network:

**Compute**

- Use
[compute-optimized](https://aws.amazon.com/ec2/instance-types/)
instances. Use benchmarking based on parameters like CPU,
memory, launch time, and burst performance to choose the
appropriate instance type.
- Cluster
your [EC2
instances](https://aws.amazon.com/ec2/) into

[placement
groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) for ad serving components for the lowest
possible latency between instances.

**Storage**

- Implement instance-attached SSD
[Amazon EBS](https://aws.amazon.com/ebs/) volumes for lowest latency storage.
- Implement provisioned IOPS SSDs if you have an IOPS-intensive workload.
- Implement
[Amazon EFS](https://aws.amazon.com/efs/) for shared file storage with burst capability.
- Implement
[Elasticache
Redis](https://aws.amazon.com/elasticache/) or Memcached to cache frequently accessed data.

**Networking**

- Implement enhanced networking for higher I/O and packet per
second performance.
- Implement [VPC
endpoints](https://aws.amazon.com/vpc/) to access AWS services within the network.

## Resources

- [Leveraging
Amazon EKS managed node group with placement group for low latency critical applications](https://aws.amazon.com/blogs/containers/leveraging-amazon-eks-managed-node-group-with-placement-group-for-low-latency-critical-applications)
- [New Amazon EC2 Instances (C7gd, M7gd, and R7gd) Powered by AWS Graviton3 Processor with Local NVMe-based SSD Storage](https://aws.amazon.com/blogs/aws/new-amazon-ec2-instances-c7gd-m7gd-and-r7gd-powered-by-aws-graviton3-processor-with-local-nvme-based-ssd-storage/)
- [Enhanced
Networking](https://docs.aws.amazon.com/pdfs/AWSEC2/latest/UserGuide/ec2-ug.pdf#enhanced-networking)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp03.html*

---

# ADVPERF01-BP04 Evaluate AI/ML-based architecture for optimization (like contextual advertising or scaling algorithms on event context)

Use AWS services to implement a low latency, high throughput
inference and MLOps framework.

## Implementation guidance

- Implement low-latency, high-throughput model inference using
[Amazon ECS](https://aws.amazon.com/ecs/),

[Amazon EKS](https://aws.amazon.com/eks/), and

[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/).
- Implement an ML pipeline using Amazon SageMaker AI to build,
train, and deploy machine learning models. Additionally, use
Sage Maker for predictive scaling of compute based on
learning from past event data.

## Resources

**Related documentation:**

- [Guidance
for Machine Learning for Near Real-Time Advertising on AWS](https://aws.amazon.com/solutions/guidance/machine-learning-for-near-real-time-advertising-on-aws/?did=sl_card&trk=sl_card)
- [Guidance
for Low-Latency High-Throughput Model Inference Using Amazon ECS](https://aws.amazon.com/solutions/guidance/low-latency-high-throughput-model-inference-using-amazon-ecs/)

**Related videos:**

- [AWS re: Invent 2020: Distributed machine learning for digital video and TV ad serving](https://www.youtube.com/watch?v=u3q-P1PQig8&t=60s)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp04.html*

---

# ADVPERF01-BP05 Evaluate the choice of open source-based software (self-managed) against using a fully-managed service

Open source-based software is widely used by customers for
advertising workloads. Carefully evaluate the factors for adoption
of self-managed and managed services.

## Implementation guidance

Adtech customers need to decide between self-managed and fully-managed services for container, databases, and analytics services in their workloads.

Evaluate the effect of both choices on performance of your workload from operational effort, infrastructure cost, customizability, high availability, and time to market. Create benchmarks for performance using both options if needed, and choose the option that meets your performance requirements.

## Key AWS services

- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)

## Resources

- [Migrating
from self-managed Kubernetes to Amazon EKS? Here are some key considerations](https://aws.amazon.com/blogs/containers/migrating-from-self-managed-kubernetes-to-amazon-eks-here-are-some-key-considerations/)
- [How
to choose the right Amazon MSK cluster type for you](https://aws.amazon.com/blogs/big-data/how-to-choose-the-right-amazon-msk-cluster-type-for-you/)
- [Motivations
for migration to Amazon DynamoDB](https://aws.amazon.com/blogs/database/motivations-for-migration-to-amazon-dynamodb/)
- [Processing
large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/)
- [Build
an end-to-end MLOps pipeline using Amazon SageMaker AI Pipelines, GitHub, and GitHub Actions](https://aws.amazon.com/blogs/machine-learning/build-an-end-to-end-mlops-pipeline-using-amazon-sagemaker-pipelines-github-and-github-actions/)
- [Choosing
an AWS database service](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp05.html*

---

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

# ADVPERF03 — Data storage selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# ADVPERF03-BP01 Choose appropriate block storage options to power your advertising workload

Block storage is crucial for data storage in the cloud. Customers
need to choose the appropriate block storage service based on
different types of workloads, as well as their requirements for
storage performance and stability.

## Implementation guidance

[Amazon EBS](https://aws.amazon.com/ebs/) provides persistent block-level storage
volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances. In the advertising industry, Amazon EBS can be
used to store databases, such as MySQL or PostgreSQL, that power ad servers, bid management
systems, and other critical components. Amazon EBS volumes can be easily scaled and optimized for
different workload patterns, which provides high performance and reliability.

- **Volume types:** Choose the
appropriate EBS volume type based on your workload. For
general-purpose workloads, use GP3 volumes. For
high-performance needs, consider IO2 volumes. If you need
high performance, you'll need to use
[EC2
Instance Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html?utm_source=simpleaws&utm_medium=referral&utm_campaign=amazon-ebs-basics-and-best-practices). It's ephemeral block storage with a
much higher performance than EBS.
- **EBS-optimized instances:** Use Amazon EBS-optimized Amazon EC2
instances to provide dedicated throughput between your instances and Amazon EBS volumes. For
example, use Amazon EBS-optimized Amazon EC2 instances and provisioned IOPS volumes for real-time
bidding or ad serving. workloads.
- **Encryption:** Enable encryption by default for all Amazon EBS
volumes to meet security and compliance requirements.
- **Snapshot management:** Regularly create and manage Amazon EBS
snapshots for backup and disaster recovery. Use AWS Data Lifecycle Manager to automate
snapshot management.
- **Performance monitoring:**
Use Amazon CloudWatch metrics to monitor and optimize EBS
health and performance.
- **Scaling:** Leverage Amazon EBS Elastic Volumes to increase the
size of Amazon EBS volumes dynamically without disrupting your applications.

## Resources

- [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [Amazon EBS volume performance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-performance.html)
- [Monitoring
tools for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-overview.html)
- [Automate
backups with Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)
- [What
is Amazon Elastic Block Store?](https://docs.aws.amazon.com/ebs/latest/userguide/work-with-ebs-encr.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp01.html*

---

# ADVPERF03-BP02 Use object storage to store and analyze raw data from ad servers, DSPs, and DMP

Object storage can be used to store massive amounts of data while
balancing cost and performance. Customers can use object storage
services to build data lakes and analyze this data to uncover
valuable insights and achieve business goals.

## Implementation guidance

[Amazon S3](https://aws.amazon.com/s3/) is a highly scalable and durable object
storage service that can store and protect any amount of data for a range of use cases. It
is ideal for storing and serving static content, such as images, videos, and other media
assets used in advertising campaigns. Amazon S3 also supports data lakes, which you can use to
store and analyze vast amounts of raw data from various sources, including ad servers,
demand-side platforms (DSPs), and data management platforms (DMPs).

- **[Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/):** A powerful storage class for
performance-critical applications, including advertising model training. Its low
latency, high throughput, and cost efficiency makes it an ideal choice for real-time ad
placement, machine learning for ad personalization, and interactive analytics.
- **Data partitioning:** Use
multiple prefixes to partition your data, which distributes
the load and improves performance. For example, instead of
storing all objects under a single prefix, use multiple
prefixes like `s3://bucket-name/prefix1/` and
`s3://bucket-name/prefix2/`.
- **Data transfer:** Use Amazon S3 Transfer Acceleration to speed up data transfers over
long distances, improving the performance of data ingestion
and distribution processes.
- **Monitoring and auditing:**
Use AWS CloudTrail and Amazon CloudWatch to monitor S3
access and performance metrics.
- **Storage tiering and
class:** Each object in Amazon S3 has a
[storage
class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) associated with it. Choosing a storage class
designed for your use case lets you optimize storage costs,
performance, and availability for your objects. Use the S3
Intelligent-Tiering storage class, which is designed to
optimize storage costs by automatically moving data to the
most cost-effective access tier when access patterns change,
without operational overhead or impact on performance. S3
Intelligent-Tiering monitors access patterns and
automatically moves objects that have not been accessed to
lower-cost access tier.

## Resources

- [Getting
started with S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-getting-started.html)
- [Setting
an S3 Lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)
- [Protecting
data with server-side encryption](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)
- [Monitoring
metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudwatch-monitoring.html)
- [Manage
Amazon S3 storage costs granularly and at scale using S3 Intelligent-Tiering](https://aws.amazon.com/blogs/storage/manage-amazon-s3-storage-costs-granularly-and-at-scale-using-s3-intelligent-tiering/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp02.html*

---

# ADVPERF03-BP03 Use a cloud file system to store shared data between applications

File storage services (such as Amazon EFS) provide a simple way to
set up and scale file systems and are widely used for big data and
analytics workloads, media processing workflows, and content
management scenarios. They are well-suited for distributed
workloads and applications that need to share files across
multiple EC2 instances.

## Implementation guidance

[Amazon EFS](https://aws.amazon.com/efs/)
is a scalable and fully managed cloud file system that provides
a simple, serverless way to share file data across AWS Cloud
services and on-premises resources. In the advertising industry,
Amazon EFS can be used to store and share log files,
configuration files, and other data that needs to be accessed
concurrently by multiple applications or instances. This is
particularly useful for log processing and analysis pipelines,
where data needs to be shared across multiple stages.

- **[Performance
modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes):** Amazon EFS offers both General
Purpose and Max I/O performance modes.
- **[Throughput
modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes):** Choosing the correct throughput mode for your file system
depends on your workload's performance requirements.
- **Cost optimization:** Use Amazon EFS lifecycle policies to
automatically move infrequently accessed files to the [EFS Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/) storage class,
reducing stor
- **High availability:** Create Amazon EFS mount targets in all
availability zones to provide high availability and low latency access to your file
system.
- age costs.

## Resources

- [Encrypting
data in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)
- [Create an Amazon EFS
file system and mount it on an Amazon EC2 instance using the AWS CLI](https://docs.aws.amazon.com/efs/latest/ug/wt1-getting-started.html)
- [Mounting
considerations for Linux](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-general.html)
- [Managing
automatic backups of Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/automatic-backups.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp03.html*

---

# ADVPERF04 — Data management design

**Pillar**: Performance Efficiency  
**Best Practices**: 6

---

# ADVPERF04-BP01 Choose a data management strategy that matches your availability, latency, and access requirements

Customers need to have a clear data management strategy for their
advertising workload datastores. The factors to consider are
latency needs, availability needs which will help them chose the
right AWS data service

## Implementation guidance

The following are the most common data stores available in adtech:

- **User data:** Demographic data (age, gender, and
location), behavioral data (browsing history, interests, and purchase history), and
device data (device type, operating system, and browser).
- **Audience data:** Segmentation data (personas and target
audiences) and geo-location data (IP addresses and GPS coordinates).
- **Campaign data:** Ad creative data (like images, videos,
and text), ad placement data (websites, apps, and platforms), and campaign performance
data (impressions, clicks, and conversions)
- **Inventory data:** Publisher data (website or app details
and traffic data) and ad space data (ad sizes, formats, or placements)
- **Pricing and bidding data:** Bid data (bid prices and bid
strategies) and auction data (bid landscape and winning bids).
- **Third-party data:** Data from Data Management Platforms
(DMPs) and data from data exchanges or marketplaces.
- **Analytics and reporting data:** Conversion data (sales,
leads, and actions), attribution data (tracking user journeys), and engagement data
(view-through rates and dwell times)

For latency, consider the following:

- **Low-latency data (real-time or near real-time):** This
data needs to be processed and acted upon within milliseconds to ensure optimal ad
delivery, real-time bidding, and accurate tracking of user interactions.

Bid (bid requests, bid responses, and auction data)
- User (device data, location data, and contextual data)
- Ad impression (ad requests and ad responses)
- Real-time campaign performance (clicks, impressions, and conversions)

- **Medium-latency data (near real-time or batch
processing):** This data can be processed in near real-time (within minutes
or hours) or in batches, as it is used for audience targeting, campaign optimization,
and attribution analysis.

User behavior (browsing history and interests)
- Audience segmentation
- Campaign optimization (performance metrics and engagement data)
- Attribution (user journeys and conversion paths)

- **High-latency data (batch processing or offline):** This
data can be processed in batches or offline, as it is typically used for analysis,
reporting, and long-term decision-making rather than real-time ad delivery or
optimization.

Historical campaign
- Detailed analytics and reporting
- Third-party (from DMPs or data exchanges)
- Ad creative (images and videos)

## Resources

- [Architecture III: Picking the Right Data Store for Your Workload](https://aws.amazon.com/blogs/startups/how-to-pick-the-right-data-store-for-your-workload-1/)
- [Amazon DynamoDB: Ad tech use cases and design patterns](https://aws.amazon.com/blogs/database/amazon-dynamodb-ad-tech-use-cases-and-design-patterns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp01.html*

---

# ADVPERF04-BP02 Consider purpose-built and streaming databases

Purpose-built databases offer low latency and can better meet the
scaling needs of advertising workloads.

## Implementation guidance

Implement low-latency databases with in-memory AWS services
(like [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) or Apache Cassandra) or ISV products specialized
for adtech (like Aerospike).

Implement medium latency data stores with an OLTP database like
[Amazon Aurora Global Database](https://aws.amazon.com/rds/aurora/global-database/) to implement a multi-Region
availability design.

## Resources

- [Running
Ad Tech Workloads on AWS with Aerospike at Petabyte Scale](https://aws.amazon.com/blogs/industries/running-ad-tech-workloads-on-aws-with-aerospike-at-petabyte-scale/)
- [Use
Amazon Aurora Global Database to build resilient multi-Region applications](https://aws.amazon.com/blogs/database/use-amazon-aurora-global-database-to-build-resilient-multi-region-applications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp02.html*

---

# ADVPERF04-BP03 Review your distributed database setup (sharding and replication) for performance, cost, and availability needs

Customers need to consider tradeoffs between performance, cost,
and availability needs, while using features like sharding for
scaling and replication for availability requirements.

## Implementation guidance

Use availability zone affinity in Aerospike to allow client
applications to access Aerospike nodes in the same zone, which
optimizes data transfer across zones.

Distributed databases often support data partitioning or
sharding, which allows you to split your data across multiple
nodes or clusters. This can help distribute the load and optimize cost by reducing the need for high-performance instances or storage
solutions for the entire dataset.

Carefully plan your data replication strategy across
Availability Zones. While replication provides high availability
and durability, replicating data across multiple Availability
Zones can increase costs. Consider replicating only the
essential data or implementing read replicas in different
Availability Zones while keeping the primary node in a single
Availability Zone.

## Key AWS services

- [Amazon RDS](https://aws.amazon.com/rds)

## Resources

- [Architecture
II: Distributed Data Stores](https://aws.amazon.com/blogs/startups/distributed-data-stores-for-mere-mortals/)
- [Building globally distributed MySQL applications using write
forwarding in Amazon Aurora Global Database](https://aws.amazon.com/blogs/database/building-globally-distributed-mysql-applications-using-write-forwarding-in-amazon-aurora-global-database/)
- [Amazon Ads Architecture at Scale - ReInvent 2021](https://www.youtube.com/watch?v=YRbIAmzFxxc)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp03.html*

---

# ADVPERF04-BP04 Enable detailed performance and observability monitoring to help tune queries and refine compute and storage

Provide access to necessary tools and metric granularity for
performance debugging and compute and storage optimization, in
particular because of the low latency requirements for advertising
workloads.

## Implementation guidance

Enable Amazon RDS enhanced monitoring, which provides deeper
visibility into database performance and health. This heightened
visibility helps you diagnose issues faster and optimize
database workloads.

Enable
[Amazon EKS Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-EKS.html) to provide observability into
cluster health, performance, logs, and billing for container
workloads. This helps you run and optimize Kubernetes
applications efficiently on Amazon EKS while reducing monitoring
costs. The automated dashboards and analytics simplify
troubleshooting.

## Key AWS services

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

## Resources

- [Monitor real-time Amazon RDS OS metrics with flexible granularity
using Enhanced Monitoring](https://aws.amazon.com/blogs/database/monitor-real-time-amazon-rds-os-metrics-with-flexible-granularity-using-enhanced-monitoring/)
- [Optimizing AdTech end-user experiences Using Amazon CloudWatch Internet Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/optimizing-adtech-end-user-experiences-using-amazon-cloudwatch-internet-monitor/)
- [Tuning Amazon RDS for MySQL with Performance
Insights](https://aws.amazon.com/blogs/database/tuning-amazon-rds-for-mysql-with-performance-insights/)
- [Analyze
Amazon Aurora MySQL Workloads with Performance Insights](https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/)
- [Announcing
Amazon CloudWatch Container Insights with Enhanced Observability for Amazon EKS on EC2](https://aws.amazon.com/blogs/mt/new-container-insights-with-enhanced-observability-for-amazon-eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp04.html*

---

# ADVPERF04-BP05 Manage high volume user profile data

The user profile database is typically large, ranging from
100-200 million to 5 billion user profiles and contains a wide
range of data about users' online activities and interactions.
Hence this should be retained for a short time in the range of
30 days -1-year max, to manage data storage costs and data query
latency SLO’s.

## Implementation guidance

Use an in-memory database with a data cache strategy using
Amazon MemoryDB.

Avoid replicating user profile data across multiple Regions due
to high latency and data transfer costs. We recommend storing user profiles
local to the user.

In the event of multi-Region architecture, implement
synchronization between periodically (for example, once or twice a day)
rather than in real-time, as users are unlikely to be in two
locations at once. Advertisers also often use geotargeting, so a
user's profile may only be accessed from the Region the user is
located in for a particular ad campaign.

## Key AWS services

- Amazon MemoryDB

## Resources

- [Observability best practices for Amazon Memory DB for Valke](https://aws.amazon.com/blogs/database/monitor-server-side-latency-for-amazon-memorydb-for-valkey/)y

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp05.html*

---

# ADVPERF04-BP06 Consider AWS Clean Rooms collaboration

AWS Clean Rooms have limits on query result size (for example,
AWS Clean Rooms has a 5GB limit), so consider using
aggregations and filters to reduce result sets.

## Implementation guidance

Large datasets can impact query performance.
Partition data effectively.

A higher number of collaborators in a collaboration channel
impacts processing time. Consider this as one of the
factors for designing the collaboration framework with
collaborators in play.

AWS Clean Rooms offers analysis templates work to support parameterized queries assisting in performance improvement through query reuse. Optimize queries before creating templates.
Consider the choice of cryptographic operations for secure computation, as it adds to processing time.

## Key AWS services

- AWS Clean Rooms

## Resources

- [Guidelines for the C3R encryption client](https://docs.aws.amazon.com/clean-rooms/latest/userguide/crypto-computing-guidelines.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf04-bp06.html*

---

# ADVPERF05 — Networking and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance

A private network not only enhances the overall stability and
security of your system, but it also improves the latency and user experience
for advertising customers.

## Implementation guidance

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish private connections between your
VPC and AWS services, such as Amazon S3, Amazon DynamoDB, or
Amazon ElastiCache. This approach enhances security by avoiding
the public internet and improves performance by reducing network
hops and latency.

## Resources

- [Access
AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html)
- [Simplify
private connectivity to Amazon DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/)
- [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html)
- [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp01.html*

---

# ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration to reduce latency and improve user experience

Edge services can accelerate requests for static content as well
as improve the response time for dynamic requests. By using the
advantages of the cloud backbone network, it can maximize the
efficiency and stability of access after requests enter the cloud.

## Implementation guidance

If your advertising workload involves serving static content,
such as images or videos, use
[Amazon CloudFront](https://aws.amazon.com/cloudfront/) to cache and deliver your content from edge
locations around the world. Amazon CloudFront reduces latency
and improves user experience for your global audience by serving
content from the nearest edge location.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Regional Edge Caches (RECs)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Points of Presence (POPs)
- [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/)

## Resources

- [Use
an Amazon CloudFront distribution to serve a static website](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/getting-started-cloudfront-overview.html)
- [Ways
to use CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html)
- [CloudFront
configuration best practices](https://docs.aws.amazon.com/whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.html)
- [Speeding
up your website with Amazon CloudFront](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html)
- [Customize
at the edge with Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp02.html*

---

# ADVPERF05-BP03 Use load balancers to improve high availability and load distribution in your workload

Use the load balancing service provided by AWS to enhance the high
availability of applications. In the event of disruptions that cause targets to become unhealthy, load balancers can automatically exclude unhealthy targets from traffic routing.

## Implementation guidance

Elastic Load Balancing (ELB) employs various load balancing
algorithms, such as round-robin, least outstanding requests, or
IP hash, to distribute traffic evenly across healthy targets,
which optimizes resource utilization and prevents overloading of
individual targets. It supports content-based routing, which
routes traffic based on the content of the request, such as the
URL path or headers, efficiently handling different types of
requests. ELB can offload SSL/TLS decryption and encryption from
your targets, reducing the computational overhead on your
application servers and improving overall performance.

## Key AWS services

- [Amazon Elastic
Load balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/)
- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)

## Resources

- [What's
the Difference Between Application, Network, and Gateway Load Balancing?](https://aws.amazon.com/compare/the-difference-between-the-difference-between-application-network-and-gateway-load-balancing/)
- [Monitor
your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)
- [ELB
Best Practices Guides](https://aws.github.io/aws-elb-best-practices/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp03.html*

---

# ADVPERF05-BP04 Provide dedicated network connection between your on-premises environment and AWS to offer high bandwidth and low latency

Use dedicated network connections to provide stable and high-speed
data communication between the on-premises data center and the AWS Cloud. This model is also applicable for connections between
multiple Regions, providing efficient and secure data
communication while effectively avoiding public network noise.

## Implementation guidance

For workloads that require high throughput or have strict
compliance requirements, consider implementing
[AWS Direct Connect](https://aws.amazon.com/directconnect/). AWS Direct Connect provides a dedicated
network connection between your on-premises environment and AWS,
offering high bandwidth, low latency, and enhanced security by
bypassing the public internet.

## Key AWS services

- [AWS PrivateLink](https://aws.amazon.com/privatelink/)

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)
- [Compliance
validation for AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/DirectConnect-compliance.html)
- [Using
the AWS Direct Connect Resiliency Toolkit to get started](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp04.html*

---

# ADVPERF06 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# ADVPERF06-BP01 Adopt a chipset-agnostic workload design for best availability of cloud resources and cost

Implement an x86 chip-agnostic design for workloads to optimize
the compute price of your advertising workload.

## Implementation guidance

Adtech customers that use Amazon EC2 Spot Instances may have found that Spot Instance costs
have swung between a preference towards AMD and Intel. As a result, implement a
chipset-agnostic design, and make your design configuration-based for seamless adoption and
to get the best compute price.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp01.html*

---

# ADVPERF06-BP02 Optimize your intake request format (like HTTP/2 or HTTP/3) for faster processing

Use optimization in next generation networking protocols to
address low latency needs for advertising workloads.

## Implementation guidance

Implement HTTP/2 protocol, which offers features like
multiplexing (multiple requests and responses are sent over the
same TCP connection), header compression, and binary protocol.
These features improve latency and throughput.

AWS services do support HTTP/2 and HTTP/3 protocols for gains in
performance efficiency.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

## Resources

- [New
– HTTP/3 Support for Amazon CloudFront](https://aws.amazon.com/blogs/aws/new-http-3-support-for-amazon-cloudfront/)
- [Application Load Balancers enables gRPC workloads with end to end HTTP/2 support](https://aws.amazon.com/about-aws/whats-new/2020/10/application-load-balancers-enable-grpc-workloads-end-to-end-http-2-support/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
