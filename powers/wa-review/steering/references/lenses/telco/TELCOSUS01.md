# TELCOSUS01 — Energy optimization

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS01-BP01 Implement energy-efficient infrastructure for telco networks

When designing telco network infrastructure for sustainability, focus on optimizing
compute resources, implementing intelligent scaling, and leveraging edge computing to reduce
energy consumption. Start by analyzing your current network functions deployment patterns -
including virtual network functions (VNFs), cloud-based network functions (CNFs), and support
systems like business support systems (BSS) and operations support systems (OSS).

**Desired outcome:** Achieve reduction in energy consumption across
telco network operations through optimized infrastructure deployment, intelligent auto scaling,
and efficient resource utilization while maintaining service availability and meeting service
requirements.

**Benefits of establishing this practice:**

- Reduced energy costs through efficient
resource utilization.
- Progress toward net-zero emissions
commitments and Science Based Targets.
- Meeting government mandates for
carbon reduction in telecommunications.
- Improved performance through right-sized
infrastructure.
- Automated scaling reduces manual
intervention and human error.

**Level of risk exposed if this best practice is not established:**
Low

## Implementation guidance

For compute optimization, use AWS Compute Optimizer to analyze your EC2 instances running telco
workloads and receive recommendations for rightsizing. Deploy your network functions on AWS
Graviton-based instances which provide up to 60% better energy efficiency compared to
comparable x86-based instances. For containerized network functions, use Amazon ECS with
AWS Fargate Spot or Amazon EKS with Karpenter to automatically optimize container placement and
reduce idle capacity.

Implement edge computing strategies using AWS Outposts, AWS Local Zones, or AWS Wavelength to
process data closer to Radio Access Network (RAN) sites and end users. This reduces backhaul
traffic and core network energy consumption. For 5G deployments, use AWS Wavelength to embed
compute and storage at the network edge within telecommunications providers' datacenters.

Configure AWS Auto Scaling with predictive scaling policies based on historical traffic patterns
typical in telco networks (peak hours, special events, seasonal variations). Use Amazon CloudWatch to
monitor metrics like CPU utilization, network throughput, and custom metrics from your network
functions to trigger scaling actions.

### Implementation steps

- Deploy AWS Compute Optimizer and analyze recommendations for EC2 instances running telco workloads.
Generate reports to identify over-provisioned instances and potential savings.
- Implement tagging strategy for telco resources using tags like Environment,
NetworkFunction, TrafficPattern to enable granular monitoring and optimization.
- Configure AWS Systems Manager to automatically stop non-production telco workloads during
off-hours and weekends using Maintenance Windows and Automation documents.
- Deploy Amazon CloudWatch Container Insights for ECS/EKS clusters running containerized
network functions to identify idle containers and optimization opportunities.
- Set up AWS Auto Scaling with target tracking policies for core network functions, using
metrics like requests per second or concurrent sessions typical in telco workloads.
- Implement AWS Lambda for event-driven telco functions like billing notifications,
network alerts, and configuration updates to reduce idle compute.
- Use AWS Cost and Usage Reports with hourly granularity to correlate resource
usage with network traffic patterns and identify optimization windows.

## Resources

**Key AWS services:**

- [EC2](https://aws.amazon.com/ec2/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [EKS](https://aws.amazon.com/pm/eks/)
- [ECS](https://aws.amazon.com/ecs/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus01-bp01.html*

---
