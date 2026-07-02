# HPCCOST02 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## HPCCOST02-BP01 Use the most appropriate instances and resources

Using the appropriate instances and resources for your system is key to cost
management. The technology choice may increase or decrease the overall cost of running an
HPC workload.

### Implementation guidance

- For example, a tightly coupled HPC workload might take ten hours to run on one
instance (X CPU cores), if the same job is run on 10 EC2 instances (10X CPU cores), it
may take 2 hours (performance scaling can be but is typically not linear). The cost
for EC2 will be higher, however the results of the calculation will be available much
quicker. This could reduce the research and development time, and for example reduce
time to market.
- Verify that instances have sufficient physical memory to complete jobs but not
more, as unused memory will not improve compute performance. Depending on the
methodology, increasing the number of nodes per job may distribute the computational
problem and reduce the required memory per node.
- Choose the pricing model best suited for workload duration and criticality, such
as using On Demand for high priority workloads, spot for flexible HPC workloads, and
RI for consistent HPC workloads to help optimize cost.
- Reducing the runtime can also reduce costs for surrounding services, such as
storage, since these resources will not be needed for as long.
- The choice of storage can also impact cost. Many HPC applications read and write
significant amounts of data. If the time to read and write data can be reduced, then
the compute will be needed for less time. There are many different types and
performance settings for storage. Picking the optimum version for your application can
improve efficiency and reduce cost overall.
- For some applications, the cost of licenses exceeds the cost of AWS resources.
It may be worth spending a little more on AWS resources to achieve better
performance and save money overall.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/cost-effective-resources.html*

---
