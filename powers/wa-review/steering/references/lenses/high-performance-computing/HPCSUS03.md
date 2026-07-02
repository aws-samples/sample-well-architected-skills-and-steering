# HPCSUS03 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 1

---

## HPCSUS03-BP01 Continually monitor the release of new EC2 instance types

As stated in the performance efficiency Pillar, we recommend
benchmarking your applications with different EC2 instances to
identify which instance type can deliver the best performance
for your HPC workloads. Using efficient Amazon EC2 instances in
HPC workloads is crucial for lower resource usage and
cost-effectiveness.

### Implementation guidance

Continually monitor the release of new instance types and take
advantage of energy efficiency improvements, including those
instance types designed to support specific workloads such as
machine learning training and inference. Independent software
vendors (ISVs) continue to update their supported
architectures. Keep an eye for ISVs that can support the ARM
architecture or accelerators, such as GPUs. Updating your
applications helps you improve the efficiency of your
workload.

## Key AWS services

- [Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/#HPC_Optimize)

## Resources

- [Deep
dive on AWS Graviton2 processor-powered Amazon EC2
instances](https://www.youtube.com/watch?v=NLysl0QvqXU)
- [Deep
dive into AWS Graviton3 and Amazon EC2 C7g
instances](https://www.youtube.com/watch?v=WDKwwFQKfSI&ab_channel=AWSEvents)
- [AWS Graviton4-based Amazon EC2 R8g instances: best price
performance in Amazon EC2](https://aws.amazon.com/blogs/aws/aws-graviton4-based-amazon-ec2-r8g-instances-best-price-performance-in-amazon-ec2)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/hardware-and-services.html*

---
