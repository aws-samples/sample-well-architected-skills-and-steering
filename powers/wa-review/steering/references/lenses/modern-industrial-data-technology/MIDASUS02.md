# MIDASUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# MIDASUS02-BP01 Actively manage workloads and resource allocation based on production demands

Identify critical and non-critical manufacturing systems, then align computing resources
with actual production schedules and operational requirements to reduce waste while providing
reliability for the essential manufacturing systems.

**Desired outcome:** Cloud resources that efficiently scale with manufacturing operations, prioritizing
time-sensitive shop floor systems while optimizing resource usage for enterprise applications,
resulting in reduced energy consumption, lower costs, and improved environmental
sustainability.

**Benefits of establishing this best practice:**

- Reduced energy consumption and carbon footprint by removing over provisioning of
resources.
- Lower operational costs while maintaining reliability for the production systems.
- Enhanced sustainability reporting metrics with quantifiable improvements in cloud
resource efficiency aligned with manufacturing operations.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Analyze production schedules and system criticality to categorize manufacturing
applications as time-critical (shop floor control, real-time monitoring) and
non-time-critical (reporting functions, data processing) using workload assessment
tools.
- Implement auto scaling mechanisms for all manufacturing systems based on their
specific demand patterns, verifying that enterprise planning and design systems maintain
necessary availability while optimizing resource allocation.
- Use batch processing systems for scheduling background data processing jobs
like quality analysis, production reporting, and maintenance analytics during periods of
lower resource demand.
- Deploy high performance computing (HPC) solutions and run resource-intensive
engineering workloads such as computational fluid dynamics (CFD) and computer aided
engineering (CAE) simulations during off-peak production hours to optimize resource
utilization.

### Implementation steps

- **Assessment and classification:**

Conduct workload assessment of manufacturing applications using AWS Well-Architected Tool
- Document peak usage patterns using Amazon CloudWatch
- Classify applications into real time and batch processing categories

- **Demand pattern mapping:**

Create demand heat maps using Amazon CloudWatch metrics
- Identify off-peak windows for non-time-critical workloads

- **Resource optimization configuration:**

Configure AWS Auto Scaling policies with appropriate thresholds
- Implement scaling plans that align with production schedules
- Define resource constraints to help prevent over-provisioning

- **Workload scheduling implementation:**

Create AWS Batch job configurations for non-critical processing tasks
- Configure AWS ParallelCluster for engineering simulations during off-hours
- Implement prioritization logic for computing resources

- **Monitoring and continuous improvement:**

Deploy CloudWatch dashboards to track resource utilization efficiency
- Establish KPIs using AWS Cost and Usage Reports
- Create sustainability improvement reporting and quarterly review process

## Key AWS services

- AWS Auto Scaling
- Amazon EC2
- AWS Batch
- AWS ParallelCluster
- Amazon CloudWatch
- AWS Cost and Usage Reports

## Resources

- [Step and simple scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html)
- [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
- [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html)
- [Amazon EC2 instance
types](https://aws.amazon.com/ec2/instance-types/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus02-bp01..html*

---
