# HPCCOST01 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## HPCCOST01-BP01 Use the right tools to collect and analyze the data you need.

There are many ways to keep track of costs using the standard
AWS tools, which will vary depending on the chosen architecture.
Please refer to the
[Cost Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

### Implementation guidance

- For HPC applications, it is very common to use tagging.
Resources used for jobs can be tagged with project names,
user ids or any other attributes you choose. Once
resources are tagged with tags activated for cost
allocation, you can generate reports based on the
attributes chosen earlier.
- If a queuing system, such as
[Slurm](https://slurm.schedmd.com/documentation.html)
or
[IBM
Spectrum LSF Suites](https://www.ibm.com/products/hpc-workload-management) is in use, they typically have
ways to log the usage of resources, such as Slurm
Accounting or LSF Analytics. Details vary depending on the
system in use.

## Key AWS services

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Slurm
accounting with AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/slurm-accounting-v3.html)
- [Metrics
in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/practice-cloud-financial-management.html*

---
