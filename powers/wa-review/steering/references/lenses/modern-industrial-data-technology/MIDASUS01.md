# MIDASUS01 — Region selection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS01-BP01 Select Regions that offer services required by Manufacturing organizations that maximizes the reduction of your carbon footprint

Choose Regions with lower carbon footprint for your manufacturing workloads while meeting
technical, compliance, and performance requirements.

**Desired outcome:** Manufacturing workloads deployed in regions that minimize carbon footprint while
maintaining operational excellence, compliance requirements, and optimizing for latency to
manufacturing facilities.

**Benefits of establishing this best practice:**

- Reduced environmental impact and energy costs for manufacturing IT operations.
- Enhanced sustainability reporting for regulatory compliance and improved brand
reputation.
- Strategic alignment with carbon reduction goals prepares the organization for
evolving environmental regulations in manufacturing.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Select cloud regions with lower carbon footprint that also satisfy your
manufacturing compliance requirements, data sovereignty needs, and performance
thresholds.
- Deploy manufacturing workloads on energy-efficient computing systems within these
sustainable regions to maximize environmental benefits.
- Configure automatic scaling policies that align with manufacturing production
patterns to verify that computing resources are only active when needed.
- Implement edge processing at manufacturing facilities to reduce data transfer
volumes between factories and cloud regions.
- Use efficient data transfer mechanisms and compression techniques when moving
manufacturing data between regions to minimize network impact.
- Consider hybrid deployment models for manufacturing workloads that must remain
geographically close to production facilities while still benefiting from cloud
sustainability features.

### Implementation steps

- **Carbon footprint assessment:**

Conduct an environmental impact assessment of your current manufacturing
workload deployment using the AWS Customer Carbon Footprint Tool
- Map manufacturing compliance and technical requirements against available
lower-carbon regions
- Create a phased migration plan for manufacturing workloads to greener
regions, prioritizing non-critical applications first

- **Deploy energy-efficient computing:**

Deploy EC2 Graviton instances with Auto Scaling configurations that align
with production schedules and peak processing times
- Configure Amazon EC2 Auto Scaling groups based on manufacturing production
patterns

- **Optimize edge processing:**

Implement AWS IoT Greengrass at manufacturing facilities to optimize edge
processing and reduce unnecessary data transfers
- Configure IoT rules to filter and aggregate manufacturing data at the edge
- Set up AWS DataSync for efficient transfer of required manufacturing data
between regions

- **Implement hybrid solutions:**

Deploy AWS Outposts or AWS Local Zones for manufacturing workloads requiring
low-latency access to production facilities
- Configure AWS Direct Connect for high-throughput, low-latency connectivity
between manufacturing sites and sustainable regions
- Implement Amazon S3 Transfer Acceleration for optimized cross-regional data
movement when required

- **Establish monitoring and governance:**

Create Amazon CloudWatch dashboards to track resource utilization and carbon
metrics across regions
- Establish sustainability KPIs and monitoring dashboards to track carbon
reduction progress
- Implement quarterly reviews to reassess regional deployment decisions based
on sustainability performance metrics

- **Continuous optimization:**

Use AWS Cost Explorer and Sustainability reports to identify further
optimization opportunities
- Regularly review and update regional deployment strategy as cloud provider
sustainability features evolve

## Key AWS services

- AWS Customer Carbon Footprint Tool
- Amazon EC2 Auto Scaling
- AWS Graviton
- AWS DataSync
- AWS IoT Greengrass
- AWS Outposts
- Amazon CloudWatch
- AWS Cost Explorer
- AWS Direct Connect
- AWS Local Zones

## Resources

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Graviton Processors](https://aws.amazon.com/ec2/graviton/)
- [Get started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)
- [AWS DataSync](https://aws.amazon.com/datasync/)
- [AWS Outposts Gives Manufacturers the Power of AWS On Premises](https://d1.awsstatic.com/Solutions/Outposts%20Manufacturing%20Solution%20Brief%20US%20Letter%20AWS%2009.30.20%20FINAL.pdf)
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus01-bp01.html*

---
