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
