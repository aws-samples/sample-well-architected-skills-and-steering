# ADVSUS01 — Region selection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS01-BP01 Distribute data and workloads across Regions when necessary to minimize network usage and latency

When selecting regions to host workloads for sustainability,
distribute data and workloads across multiple Regions to minimize
network usage and latency, prioritising the most sustainable
Regions available that leverage renewable energy sources. The
millisecond latency of programmatic advertising workloads
typically requires ad-servicing architectures be near consuming
workloads. However, there is opportunity to consolidate data
analysis for these workloads into fewer Regions.

## Implementation guidance

- Identify the latency requirements for your workloads, and
determine which AWS Regions can meet those requirements.
- From the eligible regions, select the one with the lowest carbon footprint,
considering factors such as the energy mix (prioritize Regions with 100% renewable
energy).
- Use AWS tools to measure and report your carbon footprint.
- Consolidate infrastructure needs for analytics workloads
(real-time bidding, privacy-enhanced data collaboration, ad
intelligence, and measurement) in fewer AWS Regions with
100% renewable energy.
- Use AWS services designed for energy efficiency, such as
Amazon EBS gp3 volumes, Amazon EC2 Instances with AWS
Graviton processors, and Amazon EC2 Tranium and Inferentia
instances for AI workloads.
- Periodically review and optimize the regional distribution
of workloads as new, more sustainable AWS regions become
available, balancing sustainability goals with performance
requirements.
- Aggregate analytical data in local regions and move the
aggregates to the central reporting region when data needs
to be centralized for business reasons.

## Key AWS services

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/)
- [Amazon EBS volume types](https://aws.amazon.com/ebs/volume-types/)
- [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus01-bp01.html*

---
