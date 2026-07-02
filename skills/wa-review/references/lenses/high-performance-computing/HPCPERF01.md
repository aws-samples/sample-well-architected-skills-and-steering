# HPCPERF01 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## HPCPERF01-BP01 Evaluate containers or serverless functions

When evaluating compute options, consider containers or
serverless functions for your HPC workload or for parts of your
surrounding workflow.

### Implementation guidance

- Containers are a method of operating system virtualization
that is attractive for many HPC workloads, particularly if
the applications have already been containerized. AWS
services such as AWS Batch, Amazon Elastic Container Service (Amazon ECS), and Amazon Elastic Kubernetes Service (Amazon EKS) help deploy containerized
applications.
- Serverless functions abstract the execution environment.
You can use AWS Lambda to run code without deploying,
running, or maintaining, an instance. Many AWS services
emit events based on activity inside the service, and
often a Lambda function can be initiated off of service
events. For example, a Lambda function can be run after an
object is uploaded to Amazon S3. Many HPC users use Lambda
to automatically run code as part of their workflow.

### Key AWS services

- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)
- [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/)
- [AWS Batch](https://aws.amazon.com/batch/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

### Resources

- [AWS HPC Blog: How to manage HPC jobs using a serverless
API](https://aws.amazon.com/blogs/hpc/how-to-manage-hpc-jobs-using-a-serverless-api/)
- [Bare
metal performance with the AWS Nitro System](https://aws.amazon.com/blogs/hpc/bare-metal-performance-with-the-aws-nitro-system/)
- [Deploying
and running HPC applications on AWS Batch](https://aws.amazon.com/blogs/hpc/deploying-and-running-hpc-applications-on-aws-batch/)
- [How
to manage HPC jobs using a serverless API](https://aws.amazon.com/blogs/hpc/how-to-manage-hpc-jobs-using-a-serverless-api/)
- [What
is AWS ParallelCluster?](https://www.youtube.com/watch?v=gmw7A3kOh60)
- [Performance
Efficiency Pillar: AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html#implementation-steps)

HPCPERF02: How do you select your computing instances?

EC2 instances are virtualized servers and come in different
families and sizes to offer a wide variety of capabilities. Some
instance families target specific workloads, for example,
compute, memory, or GPU intensive workloads. Other instances are
general purpose.

Both the targeted-workload and general-purpose instance families
are useful for HPC applications. Instances of particular
interest to HPC include the HPC Optimized family, the Compute
Optimized family and Accelerated Computing instance types that
are powered by GPUs and FPGAs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute-architecture.html*

---
