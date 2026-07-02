# HPCPERF03 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## HPCPERF03-BP01 Optimize your compute environment for your workload

We recommend optimizing your machine image, application-compile
options, instance configuration, and runtime environment when
running your HPC applications.

### Implementation guidance

- A current operating system running a modern kernel is
critical to achieve the best performance and ensuring
access to the most up-to-date libraries. An Amazon Machine
Image (AMI) is a template that contains the software
configuration (operating system, libraries, and
applications) required to launch your instance. You can
select an AMI with the latest version of the operating
system supported by your application. For MPI workloads,
it is also important to use a modern MPI version.
- In addition to choosing an AMI, you can further optimize
your environment by taking advantage of the hardware
features of the underlying processors. There are three
primary methods to consider when optimizing the underlying
hardware:

- Advanced processor features
- Simultaneous multithreading (SMT)
- Processor affinity

HPC applications can benefit from these advanced processor
features (for example, Advanced Vector Extensions) and can
increase their calculation speeds by compiling the software
for the target CPU architecture. The compiler options for
architecture-specific instructions vary by compiler (check the
usage guide for your compiler).

AWS enables Simultaneous multithreading (SMT), commonly
referred to as Hyper-Threading, by default on most of the EC2
instances. Multithreading improves performance for some
applications by allowing two threads to run on the same
physical core. This command will give you the list of the EC2
instances that are offered in a location (or Region) with two
threads per core:

```
`AWS ec2 describe-instance-types --filters
"Name=current-generation,Values=true"
"Name=vcpu-info.default-threads-per-core,Values=2"
--query "InstanceTypes[*].[InstanceType]" --output
text --region us-east-2 | sort`
```

Most HPC applications benefit from disabling multithreading,
and therefore, it tends to be the preferred environment for
HPC applications. Multithreading is easily disabled in Amazon EC2 by
[Specify
CPU options for an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html) for your
instance. Unless an application has been tested with
multithreading enabled, it is recommended that multithreading
be disabled and that processes are launched and individually
pinned to cores when running HPC applications. CPU or
processor affinity allows process pinning to easily happen.

Processor affinity can be controlled in a variety of ways. For
example, it can be configured at the operating system level
(available in both Windows and Linux), set as a compiler flag
within the threading library, or specified as an MPI flag
during execution. The chosen method of controlling processor
affinity depends on your workload and application.

There are many compute options available to optimize a compute
environment. Cloud deployment allows experimentation on every
level from operating system to instance type, to bare-metal
deployments. Because clusters are tuned before deployment,
time spent experimenting with cloud-based clusters is vital to
achieving the desired performance.

### Key AWS services

- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)

### Resources

- [Specify
CPU options for an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html)
- [Processor
state control for Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html)
- [Instance
sizes in the Amazon EC2 Hpc7 family – a different
experience](https://aws.amazon.com/blogs/hpc/instance-sizes-in-the-amazon-ec2-hpc7-family-a-different-experience/)
- [Application
deep-dive into the AWS Graviton3E-based Amazon EC2 Hpc7g
instance](https://aws.amazon.com/blogs/hpc/application-deep-dive-into-the-graviton3e-based-amazon-ec2-hpc7g-instance/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute-architecture.html*

---
