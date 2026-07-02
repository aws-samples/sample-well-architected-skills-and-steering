# ADVSUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 2

---

# ADVSUS02-BP01 Break down system components to determine which are business critical and compare the trade-offs

When aligning SLAs with sustainability goals for advertising
workloads, break down system components to identify
business-critical elements, and evaluate trade-offs to balance
SLAs with environmental objectives while minimizing waste.

## Implementation guidance

- Categorize workloads by business impact, customer impact,
and latency, monitor performance, and set SLA requirements
accordingly to optimize resource allocation.
- For batch workloads like privacy-enhanced data
collaboration, consider scheduling them to run during
periods when the carbon footprint is lower, such as time of
the day or week when more renewable energy is available or
when demand is lower.
- For time-sensitive and business-critical workloads like
real-time bidding, prioritize meeting SLA requirements, even
if it means running during peak demand periods with a higher
carbon footprint.

## Key AWS services

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) (Automatically scales resources)
- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) (Recommends optimal compute
resources)
- [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) (Schedules starting/stopping
instances)
- [AWS Spot
Instances](https://aws.amazon.com/ec2/spot/) (Discounted spare compute capacity)
- [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) (Energy-efficient ARM processors)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus02-bp01.html*

---

# ADVSUS02-BP02 Identify redundant infrastructure and unnecessary data movement to reduce usage where possible

Identify and eliminate redundant infrastructure components and
unnecessary data movement within your advertising workloads, as
this can help reduce resource usage, lower the overall carbon
footprint, and improve sustainability-related key performance
indicators (KPIs).

## Implementation guidance

- Audit your advertising workload infrastructure to identify
any redundant or underutilized resources, such as idle
instances, oversized instances, or unnecessary data
replication.
- Analyze data movement patterns and network traffic to
identify opportunities for reducing data transfers,
especially over long distances or between regions. Use
Amazon CloudFront to cache and serve ad files closer to
consumers.
- Implement auto scaling and right-sizing mechanisms to
automatically adjust resource allocation based on actual
workload demands, minimizing over-provisioning. For example,
with real-time bidding workloads that use Amazon EKS,
implement a scaling policy that is determined by the number
of bids being served, which optimizes resource usage.
- Consolidate workloads and data storage where possible,
reducing the overall infrastructure footprint and associated
energy consumption. Implement lifecycle policies to remove
old ad file assets that are no longer needed.
- Establish monitoring and reporting processes to track
resource utilization, data movement, and sustainability KPIs
over time, enabling continuous optimization.

## Key AWS services

- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) (Identify optimization opportunities)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) (Visualizes and analyzes cost/usage
data)
- [AWS Config](https://aws.amazon.com/config/) (Monitors and records resource configurations)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) (Cache and serve ad files)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) (Logs API calls and events)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) (Automatically scales resources)
- [AWS Lambda](https://aws.amazon.com/lambda/) (Serverless computing)
- [AWS Data Transfer Cost Estimator](https://calculator.aws/#/createCalculator/DataTransfer) (Estimates data transfer
costs)
- [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) (Remove unneeded ad assets)
- [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/) (Provides architecture best
practices)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus02-bp02.html*

---
