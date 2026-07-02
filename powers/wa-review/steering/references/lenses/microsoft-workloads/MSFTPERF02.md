# MSFTPERF02 — Compute resources

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# MSFTPERF02-BP01 Choose the Amazon EC2 instance families that best fit the Microsoft workload

Amazon EC2 provides different instance family types, addressing
different purposes. For example, General purpose instances, such as
m7i and m7a can be used for most production applications running on
Windows Server. For non-production or less critical environments, t3
burstable instances may also be a fit. Memory optimized instances,
such as r7i, r7a, and x2iedn provide greater ratio of memory to vCPU
and are ideal for memory-intensive workloads, such as Microsoft SQL
Server.

**Desired outcome:** Optimize
performance and cost efficiency by selecting the most appropriate
EC2 instance families that align with your Microsoft workload's
specific compute, memory, and I/O requirements, ensuring optimal
resource utilization while maintaining application performance and
scalability.

**Common anti-patterns:**

- Choosing instance types based solely on cost without considering
performance requirements, leading to under-provisioned resources
that impact application performance and user experience.
- Using the same instance family for all workloads without
evaluating specific requirements, missing opportunities to
optimize performance for memory-intensive applications like SQL
Server or compute-intensive .NET applications.
- Over-provisioning instances with excessive resources "just
in case" without analyzing actual workload patterns,
resulting in unnecessary costs and inefficient resource
utilization.

**Benefits of establishing this best
practice:**

- Optimized performance through instance families specifically
designed for different workload characteristics, ensuring
Microsoft applications receive appropriate compute, memory, and
I/O resources.
- Improved cost efficiency by matching instance capabilities to
actual workload requirements, avoiding over-provisioning while
maintaining performance standards.
- Enhanced scalability and flexibility through understanding of
instance family characteristics, enabling better architectural
decisions for different Microsoft workload components.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Selecting appropriate EC2 instance families for Microsoft
workloads requires understanding both your application
requirements and the characteristics of different instance types.
Begin by analyzing your workload patterns, then match them to
instance families that provide optimal price-performance ratios
for your specific use cases.

### Implementation steps

- Analyze your Microsoft workload requirements including CPU
utilization patterns, memory requirements, storage I/O
needs, and network performance requirements.
- Evaluate different EC2 instance families based on your
workload characteristics:

General purpose (m7i, m7a, m6i) for balanced workloads
- Memory optimized (r7i, r7a, x2iedn) for SQL Server and
memory-intensive applications
- Compute optimized (c7i, c7a) for CPU-intensive .NET
applications
- Burstable (t3, t4g1) for variable or
low-utilization workloads

- Consider processor architecture options including Intel,
AMD, and AWS Graviton processors based on application
compatibility and performance requirements.
- Evaluate instance sizes within families to match vCPU and
memory requirements without over-provisioning resources.
- Test different instance types in non-production environments
to validate performance and cost characteristics.
- Implement monitoring using Amazon CloudWatch and AWS Compute Optimizer to track instance utilization and receive
rightsizing recommendations.
- Establish regular review processes to evaluate instance
performance and adjust selections based on changing workload
patterns.
- Document instance selection criteria and rationale for
different Microsoft workload components to guide future
decisions.

Windows Server OS does not support ARM based
processors. Consider using AWS Graviton based instances can be
used to run
[cross-platform
.NET on Linux](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-graviton.html).

## Resources

**Related documents:**

- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)

**Related tools:**

- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf02-bp01.html*

---

# MSFTPERF02-BP02 Consider the use for EC2 Fast Launch to accelerate launching your Microsoft workload instances

EC2 Fast Launch will speed up the Windows EC2 instance launch
process. When you configure a Windows Server AMI for EC2 Fast
Launch, Amazon EC2 creates a set of pre-provisioned snapshots to use
for faster launching. It completes steps such as Sysprep specialize,
Windows Out of Box Experience (OOBE), and rebooting as required.
Especially useful when you need to scale fast.

**Desired outcome:** Significantly
reduce Windows instance launch times and improve scaling
responsiveness for Microsoft workloads by leveraging EC2 Fast Launch
to pre-provision snapshots and complete initialization steps,
enabling rapid deployment and auto-scaling capabilities for
time-sensitive applications.

**Common anti-patterns:**

- Accepting standard Windows instance launch times without
evaluating Fast Launch benefits, missing opportunities to
improve application availability and user experience during
scaling events.
- Implementing Fast Launch without considering the additional
costs of pre-provisioned snapshots and temporary instances,
potentially increasing expenses without adequate benefit
analysis.
- Using Fast Launch for infrequently launched instances where the
preparation overhead exceeds the benefits, leading to
unnecessary complexity and costs.

**Benefits of establishing this best
practice:**

- Dramatically reduced instance launch times through
pre-provisioned snapshots that eliminate Windows initialization
steps like Sysprep and OOBE during actual instance launches.
- Improved application availability and scaling responsiveness
during traffic spikes or auto-scaling events, enhancing user
experience and system reliability.
- Enhanced disaster recovery capabilities through faster instance
replacement and environment restoration when rapid recovery is
critical for business continuity.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing EC2 Fast Launch requires careful evaluation of your
scaling patterns and cost-benefit analysis. Focus on AMIs that are
frequently launched and where launch time significantly impacts
application performance or user experience.

### Implementation steps

- Identify Windows AMIs that are frequently launched or
require rapid scaling capabilities for your Microsoft
workloads.
- Analyze current instance launch times and scaling patterns
to determine potential benefits of Fast Launch
implementation.
- Configure Fast Launch for selected AMIs through the EC2
console or AWS CLI, specifying the number of pre-provisioned
snapshots to maintain.
- Monitor Fast Launch metrics including launch time
improvements and associated costs for pre-provisioned
resources.
- Evaluate cost-benefit ratio considering snapshot storage
costs, temporary instance costs, and performance
improvements.
- Integrate Fast Launch-enabled AMIs into auto-scaling groups
and deployment processes to maximize scaling responsiveness.
- Establish monitoring and alerting for Fast Launch resource
utilization to optimize the number of pre-provisioned
snapshots.
- Document Fast Launch configuration and regularly review
effectiveness based on actual scaling patterns and
requirements.

## Resources

**Related documents:**

- [Configuring
your Windows AMI for faster launching](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-ami-config-fast-launch.html)
- [Launch
Microsoft Windows Server instances on Amazon EC2 up to 65%
faster than before](https://aws.amazon.com/blogs/modernizing-with-aws/launch-windows-faster-on-ec2/)

**Related tools:**

- [Launch
Microsoft Windows Server instances on Amazon EC2 up to 65%
faster than before](https://aws.amazon.com/blogs/modernizing-with-aws/launch-windows-faster-on-ec2/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf02-bp02.html*

---

# MSFTPERF02-BP03 Consider using Amazon EBS fast snapshot restore

Amazon EBS Fast Snapshot Restore (FSR) offers significant advantages
for Microsoft workloads by eliminating the initialization latency
typically associated with first-use EBS volumes created from
snapshots. This is particularly beneficial for Windows Server
instances and SQL Server deployments where quick recovery time
objectives (RTOs) are crucial. When enabled on selected snapshots in
specific Availability Zones, FSR ensures that EBS volumes created
from these snapshots deliver their full performance immediately
without the need for the traditional initialization process, which
normally requires reading all blocks from S3. For Microsoft
workloads that require rapid failover, disaster recovery, or test
environment provisioning, FSR can dramatically reduce the time
needed to bring systems online.

**Desired outcome:** Achieve
immediate full performance for EBS volumes created from snapshots,
eliminating initialization latency for Microsoft workloads and
enabling rapid disaster recovery, failover scenarios, and test
environment provisioning with predictable performance
characteristics from the moment volumes are attached.

**Common anti-patterns:**

- Accepting standard EBS volume initialization performance without
evaluating FSR benefits for time-critical Microsoft workloads,
missing opportunities to improve recovery times and system
availability.
- Implementing FSR on all snapshots without cost-benefit analysis,
leading to unnecessary expenses for snapshots that don't require
immediate full performance.
- Using FSR without proper planning for Availability Zone
placement, limiting the effectiveness of the feature for
disaster recovery and high availability scenarios.

**Benefits of establishing this best
practice:**

- Eliminated initialization latency providing immediate full
performance for EBS volumes, crucial for rapid disaster recovery
and failover scenarios for Microsoft workloads.
- Improved predictability for recovery time objectives (RTOs) by
removing variable initialization times that can impact business
continuity planning.
- Enhanced operational efficiency for test environment
provisioning and development workflows where rapid volume
availability is essential for productivity.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing EBS fast snapshot restore (FSR) requires strategic
selection of snapshots and Availability Zones based on your
Microsoft workload's recovery and performance requirements. Focus
on critical snapshots used for disaster recovery, production
failover, or frequently accessed test environments.

### Implementation steps

- Identify critical EBS snapshots used for Microsoft workload
disaster recovery, production databases, or frequently
provisioned test environments.
- Analyze recovery time objectives (RTOs) and determine which
workloads would benefit most from immediate volume
performance.
- Enable FSR for selected snapshots in appropriate
Availability Zones based on your deployment architecture.
- Monitor FSR usage and costs to ensure the feature provides
adequate value for the additional expense incurred.
- Integrate FSR-enabled snapshots into disaster recovery
procedures and automated failover processes.
- Test volume creation and performance validation procedures
to confirm FSR effectiveness for your Microsoft workloads.
- Establish policies for FSR lifecycle management including
enabling or disabling based on snapshot age and usage
patterns.
- Document FSR configuration and include in operational
runbooks for disaster recovery and environment provisioning
procedures.

## Resources

**Related documents:**

- [Amazon EBS fast snapshot restore](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html)
- [Instant
performance on Amazon EBS volumes restored from snapshots
using Fast Snapshot Restore](https://www.youtube.com/watch?v=Do4BHPjGDuM)

**Related tools:**

- [Amazon EBS](https://docs.aws.amazon.com/ebs/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf02-bp03.html*

---

# MSFTPERF02-BP04 Consider using Amazon EBS Provisioned Rate for Volume Initialization

Amazon EBS provisioned rate for volume initialization (PRVI) offers
significant advantages for Microsoft workloads by providing
predictable and faster initialization times for new EBS volumes
created from snapshots. This feature is particularly valuable for
Windows Server deployments and SQL Server environments where
consistent and reliable performance during volume initialization is
crucial. By allowing you to specify the initialization rate up to
300 MiB/s, PRVI enables you to control and accelerate the background
process of loading data from S3 to the EBS volume, ensuring your
Microsoft applications can access their data more quickly and
predictably.

**Desired outcome:** Achieve
predictable and accelerated EBS volume initialization for Microsoft
workloads through controlled initialization rates, ensuring
consistent performance during volume creation and reducing the
impact of initialization processes on application availability and
user experience.

**Common anti-patterns:**

- Accepting variable and unpredictable volume initialization times
without considering PRVI benefits, leading to inconsistent
application performance and unpredictable recovery times.
- Implementing PRVI without cost-benefit analysis for specific
workloads, potentially incurring additional costs without
adequate performance improvements for the use case.
- Using PRVI without proper integration into disaster recovery and
scaling procedures, missing opportunities to improve overall
system reliability and predictability.

**Benefits of establishing this best
practice:**

- Predictable initialization performance through controlled
initialization rates that enable reliable capacity planning and
recovery time estimation for Microsoft workloads.
- Improved application availability during scaling events and
disaster recovery scenarios where consistent volume
initialization performance is critical for meeting SLAs.
- Enhanced operational efficiency through reduced variability in
volume provisioning times, enabling more reliable automation and
orchestration of Microsoft workload deployments.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing EBS Provisioned Rate for Volume Initialization
requires careful evaluation of your Microsoft workload's
initialization requirements and cost considerations. Focus on
scenarios where predictable initialization performance is critical
for meeting operational objectives.

### Implementation steps

- Identify Microsoft workloads that require predictable volume
initialization performance, particularly for disaster
recovery and scaling scenarios.
- Analyze current volume initialization patterns and determine
appropriate provisioned rates based on performance
requirements and cost considerations.
- Configure PRVI for relevant EBS volumes with initialization
rates up to 300 MiB/s based on workload needs and budget
constraints.
- Monitor initialization performance and costs to validate the
effectiveness of PRVI implementation for your specific use
cases.
- Integrate PRVI-configured volumes into automated deployment
and disaster recovery procedures to maximize predictability
benefits.
- Establish monitoring and alerting for initialization
performance to ensure PRVI is delivering expected results.
- Document PRVI configuration decisions and include in
operational procedures for volume management and disaster
recovery.
- Regularly review PRVI usage and costs to optimize
configuration based on actual performance requirements and
business value.

## Resources

**Related documents:**

- [Initialize
Amazon EBS volumes](https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html)
- [Accelerate
the transfer of data from an Amazon EBS snapshot to a new EBS
volume](https://aws.amazon.com/blogs/aws/accelerate-the-transfer-of-data-from-an-amazon-ebs-snapshot-to-a-new-ebs-volume/)

**Related tools:**

- [Accelerate
EBS snapshot data transfer](https://aws.amazon.com/blogs/aws/accelerate-the-transfer-of-data-from-an-amazon-ebs-snapshot-to-a-new-ebs-volume/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf02-bp04.html*

---
