# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 4

---

# MSFTPERF01 — Cloud resource selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# MSFTPERF01-BP01 Consider AWS Elastic Beanstalk for running traditional Windows servers hosting your Microsoft application

In scenarios where the traditional virtual machine approach is a
requirement, evaluate the EC2 instance families that better address
your Microsoft workload needs. Using data-driven decisions for
architectural considerations, you can also opt for Elastic Beanstalk
to reduce the operational overhead on managing the EC2 instances and
surrounding infrastructure resources, such as Elastic Load Balancing, and Auto Scaling Groups.

**Desired outcome:** Optimize
performance efficiency for traditional Microsoft applications by
leveraging AWS Elastic Beanstalk to reduce operational overhead
while maintaining the familiar Windows Server environment, enabling
faster deployments, automated scaling, and simplified infrastructure
management without sacrificing application performance or
functionality.

**Common anti-patterns:**

- Managing EC2 instances manually for Microsoft applications
without leveraging platform services, leading to increased
operational complexity, slower deployment cycles, and higher
maintenance overhead for load balancing and scaling
configurations.
- Choosing inappropriate EC2 instance families for Microsoft
workloads without considering performance requirements,
resulting in either over-provisioned resources that waste costs
or under-provisioned instances that impact application
performance.
- Implementing traditional deployment approaches without
considering managed platform services, missing opportunities to
improve deployment speed, reliability, and operational
efficiency through automation and best practices.

**Benefits of establishing this best
practice:**

- Reduced operational overhead through automated infrastructure
management, including load balancing, auto scaling, and health
monitoring, allowing teams to focus on application development
rather than infrastructure maintenance.
- Improved deployment efficiency and reliability through AWS Elastic Beanstalk's automated deployment processes, version
management, and rollback capabilities that streamline
application updates and reduce deployment risks.
- Enhanced performance optimization through automatic scaling
capabilities and integrated monitoring that ensures Microsoft
applications maintain optimal performance during varying load
conditions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing AWS Elastic Beanstalk for Microsoft applications
requires understanding your application requirements and
configuring the platform appropriately for Windows workloads.
Begin by assessing your current application architecture and
deployment processes, then configure Elastic Beanstalk with the
appropriate instance types and platform settings to optimize
performance while reducing operational complexity.

### Implementation steps

- Assess your Microsoft application requirements including
runtime dependencies, performance needs, and scaling
patterns to determine appropriate Elastic Beanstalk
configuration.
- Choose the appropriate AWS Elastic Beanstalk platform
version that supports your .NET Framework or .NET Core
application requirements.
- Select optimal EC2 instance families based on your
application's compute, memory, and I/O requirements,
considering options like m7i, r7i, or c7i instances.
- Configure AWS Elastic Beanstalk environment settings
including auto scaling policies, load balancer
configuration, and health check parameters.
- Set up application deployment processes using AWS Elastic Beanstalk deployment methods such as rolling deployments or
blue/green deployments.
- Implement monitoring and logging integration with Amazon CloudWatch to track application performance and
infrastructure metrics.
- Configure environment variables and application settings
through AWS Elastic Beanstalk configuration options to
maintain environment-specific configurations.
- Establish backup and disaster recovery procedures using AWS Elastic Beanstalk's configuration management and version
control capabilities.

## Resources

**Related documents:**

- [Using
Elastic Beanstalk with .NET](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net)
- [Seamless
Production Deployment with Elastic Beanstalk](https://aws.amazon.com/blogs/dotnet/seamless-production-deployment-with-elastic-beanstalk/)

**Related tools:**

- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf01-bp01.html*

---

# MSFTPERF01-BP02 Consider Amazon managed container orchestrator services to run containers on AWS

Amazon Elastic Kubernetes Service (EKS), Amazon Elastic Container Service (ECS), and AWS Fargate support both Linux and Windows
containers. Either running cross-platform .NET on Linux or .NET
Framework on Windows, you can run your Microsoft
container-compatible workload taking advantage of the benefits of
the managed service, improving performance efficiency.

**Desired outcome:** Achieve improved
performance efficiency and operational simplicity for Microsoft
workloads by leveraging managed container orchestration services
that provide automated scaling, resource optimization, and reduced
infrastructure management overhead while supporting both Windows and
Linux container deployments.

**Common anti-patterns:**

- Running containerized Microsoft applications on self-managed
container platforms without leveraging AWS managed services,
increasing operational complexity and missing optimization
opportunities.
- Choosing container orchestration without considering workload
characteristics, leading to over-engineered solutions for simple
applications or under-powered platforms for complex distributed
systems.
- Implementing containers without proper resource allocation and
scaling policies, resulting in performance issues or resource
waste.
- Microsoft workloads on self-managed container orchestration
platforms may limit the availability of AWS services and
features that are designed to simplify the deployment and
management of these workloads.

**Benefits of establishing this best
practice:**

- Enhanced scalability and resource utilization through managed
container orchestration that automatically optimizes resource
allocation and scaling based on workload demands.
- Reduced operational overhead through AWS-managed control planes,
automated updates, and integrated monitoring capabilities.
- Improved deployment flexibility supporting both Windows and
Linux containers for different Microsoft workload components.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing managed container orchestration for Microsoft
workloads requires careful evaluation of your application
architecture and container requirements. Choose the appropriate
service based on your complexity needs and operational
preferences, then configure for optimal performance and
efficiency.

### Implementation steps

- Assess your Microsoft applications for containerization
readiness and determine Windows versus Linux container
requirements.
- Choose between EKS, ECS, or Fargate based on complexity,
control requirements, and operational preferences.
- Configure container resource allocation, scaling policies,
and networking for optimal performance.
- Implement container image optimization and security scanning
processes.
- Set up monitoring and logging integration with Amazon CloudWatch Container Insights.
- Establish CI/CD pipelines for automated container deployment
and updates.

## Resources

**Related documents:**

- [Windows
in Kubernetes](https://kubernetes.io/docs/concepts/windows/)
- [Deploy
Windows nodes on EKS clusters](https://docs.aws.amazon.com/eks/latest/userguide/windows-support.html)
- [Launching
an Amazon ECS Windows container instance](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_window-container_instance.html)
- [Windows
Containers Isolation Modes](https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container)
- [Windows
containers on AWS](https://aws.amazon.com/blogs/containers/tag/windows/)

**Related tools:**

- [Amazon Elastic Kubernetes Service Documentation](https://docs.aws.amazon.com/eks/)
- [Amazon Elastic Container Service Documentation](https://docs.aws.amazon.com/ecs/)
- [Simplify
compute management with AWS Fargate](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf01-bp02.html*

---

# MSFTPERF01-BP03 Run serverless Microsoft applications on AWS Lambda

Use cases such as event-driven, like message processing and API
routes, application-based function, like packaging and entire
cross-platform ASP.NET runtime, file processing, mobile backend,
cloud automation, and similar are usually suitable for running on
AWS Lambda.

**Desired outcome:** Achieve optimal
performance efficiency and cost optimization for suitable Microsoft
workloads by leveraging AWS Lambda's serverless architecture,
eliminating infrastructure management overhead while providing
automatic scaling, high availability, and pay-per-execution pricing
for event-driven and function-based applications.

**Common anti-patterns:**

- Running long-running or stateful Microsoft applications on
Lambda without considering execution time limits and stateless
requirements, leading to performance issues or architectural
mismatches.
- Implementing serverless solutions for workloads that require
persistent connections or complex state management, missing the
benefits of serverless while introducing unnecessary complexity.
- Choosing Lambda without evaluating cold start impacts on
performance-sensitive applications, potentially affecting user
experience for latency-critical workloads.

**Benefits of establishing this best
practice:**

- Eliminated infrastructure management overhead through fully
managed serverless execution environment that automatically
handles scaling, patching, and availability.
- Optimized cost efficiency through pay-per-execution pricing
model that eliminates costs for idle resources and automatically
scales to zero when not in use.
- Enhanced performance for event-driven workloads through
automatic scaling and optimized execution environment designed
for short-lived, stateless functions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing serverless Microsoft applications on AWS Lambda
requires careful evaluation of application architecture and
suitability for serverless patterns. Focus on event-driven,
stateless workloads and optimize for Lambda's execution model to
achieve maximum performance efficiency.

### Implementation steps

- Identify Microsoft workload components suitable for
serverless architecture including event-driven functions,
API endpoints, and batch processing tasks.
- Refactor applications to follow serverless patterns with
stateless, event-driven design principles.
- Configure Lambda functions with appropriate runtime, memory
allocation, and timeout settings for optimal performance.
- Implement efficient cold start optimization techniques
including provisioned concurrency for latency-sensitive
functions.
- Set up event sources and triggers using services like API Gateway, S3, SQS, or EventBridge.
- Configure monitoring and observability using CloudWatch,
X-Ray, and Lambda Insights for performance tracking.

## Resources

**Related documents:**

- [Building
.NET applications on AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-csharp.html)

**Related tools:**

- [AWS Lambda](https://docs.aws.amazon.com/lambda/)
- [AWS .NET Development Blog](https://aws.amazon.com/blogs/compute/category/devops/aws-net-development/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf01-bp03.html*

---

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

# MSFTPERF03 — Storage solutions

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# MSFTPERF03-BP01 Consider Amazon EBS gp3 volumes for general workloads

Amazon EBS's newest and most cost-effective SSD option, General
Purpose SSD (gp3) volumes, strikes an optimal balance between price
and performance for a wide range of applications. A key advantage of
gp3 volumes is the ability to adjust performance independently of
storage capacity, allowing users to meet specific performance
requirements without unnecessarily increasing block storage.
Moreover, gp3 volumes offer significant cost savings, with prices
20% lower per GiB compared to their predecessor, General Purpose SSD
(gp2) volumes.

**Desired outcome:** Optimize storage
performance and cost efficiency for Microsoft workloads by
leveraging gp3 volumes that provide independent scaling of IOPS and
throughput from storage capacity, enabling right-sized storage
configurations that meet performance requirements while minimizing
costs.

**Common anti-patterns:**

- Continuing to use gp2 volumes without evaluating gp3 benefits,
missing opportunities for cost savings and performance
optimization through independent IOPS and throughput scaling.
- Over-provisioning storage capacity to meet IOPS requirements
when using gp2 volumes, leading to unnecessary storage costs
that could be avoided with gp3's independent performance
scaling.
- Choosing high-performance storage options like io1/io2 for
workloads that could be adequately served by gp3 with
appropriate IOPS configuration, resulting in unnecessary costs.

**Benefits of establishing this best
practice:**

- Significant cost savings through 20% lower per-GiB pricing
compared to gp2 volumes while maintaining or improving
performance characteristics for Microsoft workloads.
- Enhanced flexibility through independent scaling of IOPS and
throughput from storage capacity, enabling optimal resource
allocation without over-provisioning storage.
- Improved performance predictability through consistent baseline
performance and the ability to provision additional IOPS and
throughput as needed for specific workload requirements.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing gp3 volumes for Microsoft workloads requires
understanding your storage performance requirements and migrating
from existing volume types where appropriate. Focus on workloads
that can benefit from independent IOPS and throughput scaling
while achieving cost savings.

### Implementation steps

- Analyze current storage performance requirements for
Microsoft workloads including IOPS, throughput, and capacity
needs.
- Identify existing gp2 volumes and other storage types that
could benefit from migration to gp3 for cost and performance
optimization.
- Plan gp3 volume configurations with appropriate baseline
performance and additional provisioned IOPS or throughput
based on workload requirements.
- Test gp3 performance in non-production environments to
validate performance characteristics for your specific
Microsoft applications.
- Implement migration procedures for existing volumes using
EBS volume modification or snapshot-based migration
approaches.
- Monitor storage performance and costs after migration to
validate expected benefits and optimize configurations as
needed.
- Establish policies for new volume provisioning that default
to gp3 unless specific requirements dictate alternative
storage types.
- Document gp3 configuration standards and include in storage
provisioning procedures for consistent implementation across
environments.

## Resources

**Related documents:**

- [General
Purpose SSD (gp3) volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html#gp3-ebs-volume-type)

**Related tools:**

- [Migrate
Amazon EBS volumes from gp2 to gp3](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp01.html*

---

# MSFTPERF03-BP02 Consider Amazon EBS io2 Block Express volumes for high-intense I/O workloads

Amazon EBS io2 Block Express volumes are based on an updated storage
server architecture. They are designed to handle high I/O
requirements for applications running on Nitro System-based
instances. These volumes offer improved durability and lower
latency. As a result, they are suitable for resource-intensive
applications that require consistent performance, such as certain
database systems (For example, Oracle, SAP HANA, and Microsoft SQL
Server) and SAS Analytics.

**Desired outcome:** Achieve maximum
I/O performance and lowest latency for demanding Microsoft
workloads, particularly SQL Server databases and other I/O-intensive
applications, through io2 Block Express volumes that provide
consistent high-performance storage with enhanced durability and
reliability.

**Common anti-patterns:**

- Using general-purpose storage for high-performance Microsoft SQL
Server databases without evaluating io2 Block Express benefits,
potentially limiting application performance and user
experience.
- Implementing io2 Block Express for workloads that don't require
extreme I/O performance, leading to unnecessary costs without
proportional performance benefits.
- Choosing io2 Block Express without ensuring compatibility with
Nitro System-based instances, missing the full performance
potential of the storage technology.

**Benefits of establishing this best
practice:**

- Maximum I/O performance through io2 Block Express architecture
designed specifically for high-intensity workloads, enabling
optimal performance for demanding Microsoft applications.
- Enhanced reliability and durability through improved storage
architecture that provides consistent performance and reduced
latency for mission-critical workloads.
- Improved application responsiveness for I/O-intensive Microsoft
workloads including SQL Server databases, analytics
applications, and high-performance computing scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing io2 Block Express volumes requires careful evaluation
of I/O requirements and cost considerations. Focus on workloads
that genuinely require extreme I/O performance and can justify the
additional costs through improved application performance and
business outcomes.

### Implementation steps

- Identify Microsoft workloads with high I/O requirements that
would benefit from io2 Block Express performance
characteristics, particularly SQL Server databases and
analytics applications.
- Analyze current I/O patterns including IOPS requirements,
throughput needs, and latency sensitivity to determine if
io2 Block Express is appropriate.
- Ensure compatibility with Nitro System-based instances that
can fully utilize io2 Block Express performance
capabilities.
- Configure io2 Block Express volumes with appropriate IOPS
provisioning based on workload requirements and performance
testing results.
- Implement performance testing in non-production environments
to validate expected performance improvements and cost
justification.
- Monitor storage performance metrics including IOPS
utilization, throughput, and latency to ensure optimal
configuration and utilization.
- Establish cost monitoring and optimization procedures to
ensure io2 Block Express usage remains cost-effective for
the performance benefits provided.
- Document io2 Block Express configuration standards and use
cases for consistent implementation across high-performance
Microsoft workloads.

## Resources

**Related documents:**

- [Provisioned
IOPS SSD (io2 Block Express) volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html#io2-block-express)
- [Best
practices for Amazon RDS for SQL Server with Amazon EBS io2
Block Express volumes up to 64 TiB](https://aws.amazon.com/blogs/database/best-practices-for-amazon-rds-for-sql-server-with-amazon-ebs-io2-block-express-volumes-up-to-64-tib/)

**Related tools:**

- [io2
Block Express considerations](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html#io2-bx-considerations)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp02.html*

---

# MSFTPERF03-BP03 Consider Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is a managed service that
provides file storage using Microsoft Windows file system
technology. It supports Windows file system features and uses the
Server Message Block (SMB) protocol for network file access, making
it compatible with various Windows-based enterprise workloads and
applications. The service offers integration with other AWS services
and performance optimized for enterprise applications, aiming to
provide low-latency file storage. FSx for Windows File Server is
designed for Windows workloads that require shared file storage,
such as File Servers, Application Server configuration stores, and
even Microsoft SQL Server databases.

**Desired outcome:** Achieve
high-performance, fully managed Windows file storage that seamlessly
integrates with Microsoft workloads, providing native Windows file
system features, SMB protocol support, and optimized performance
while reducing operational overhead through AWS-managed
infrastructure.

**Common anti-patterns:**

- Implementing self-managed Windows file servers on EC2 without
evaluating FSx benefits, missing opportunities to reduce
operational overhead and improve performance through managed
services.
- Using general-purpose storage solutions for Windows workloads
that require specific Windows file system features, potentially
limiting functionality and performance.
- Choosing FSx configurations without proper performance analysis,
leading to either over-provisioned resources that increase costs
or under-provisioned storage that impacts application
performance.

**Benefits of establishing this best
practice:**

- Reduced operational overhead through fully managed Windows file
storage that eliminates the need to manage file server
infrastructure, patching, and maintenance tasks.
- Enhanced performance and reliability through AWS-managed
infrastructure optimized for Windows workloads with built-in
high availability and backup capabilities.
- Native Windows integration providing full compatibility with
Windows file system features, Active Directory integration, and
SMB protocol support for seamless application integration.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing Amazon FSx for Windows File Server requires
understanding your file storage requirements and migration
planning from existing file server infrastructure. Focus on
workloads that require Windows-native file system features and can
benefit from managed service advantages.

### Implementation steps

- Assess current Windows file storage requirements including
capacity, performance, and feature needs for your Microsoft
workloads.
- Evaluate existing file server infrastructure and identify
workloads suitable for migration to FSx for Windows File Server.
- Choose appropriate FSx deployment options including
Single-AZ or Multi-AZ configurations based on availability
and performance requirements.
- Configure FSx file systems with appropriate storage
capacity, throughput, and IOPS settings based on workload
analysis and performance testing.
- Plan migration procedures for existing file shares and data,
including user access permissions and Active Directory
integration.
- Implement backup and disaster recovery strategies using
FSx's built-in backup capabilities and cross-region
replication options.
- Monitor file system performance and utilization using
CloudWatch metrics to optimize configuration and identify
scaling needs.
- Establish operational procedures for FSx management
including access control, monitoring, and capacity planning
for ongoing operations.

## Resources

**Related documents:**

- [What
is Amazon FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
- [Optimizing
Amazon FSx for Windows File Server performance with new
metrics](https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/)

**Related tools:**

- [Amazon FSx performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp03.html*

---

# MSFTPERF03-BP04 Consider Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed AWS service that
provides scalable, high-performance file storage based on the
widely-used NetApp ONTAP file system. It combines the familiar
features and capabilities of NetApp systems with the benefits of a
cloud-managed service. This service offers fast, flexible shared
file storage accessible from Linux, Windows, and macOS instances,
both in AWS and on-premises. FSx for ONTAP provides high-performance
SSD storage with very low latencies and also HDD storage. Amazon FSx for NetApp ONTAP offers robust file storage capabilities, including
support for petabyte-scale datasets in a single namespace and high
throughput of up to tens of GBps per file system.

**Desired outcome:** Achieve
enterprise-grade, high-performance file storage for Microsoft
workloads through FSx for ONTAP, providing multi-protocol
access, advanced data management features, and cost optimization
capabilities while maintaining compatibility with existing NetApp
environments and Microsoft applications.

**Common anti-patterns:**

- Using basic file storage solutions for enterprise Microsoft
workloads without evaluating FSx for ONTAP's advanced features,
missing opportunities for performance optimization and data
management capabilities.
- Implementing FSx for ONTAP without leveraging its multi-protocol
capabilities, limiting the potential for workload consolidation
and simplified architecture.
- Choosing FSx for ONTAP configurations without considering data
tiering and compression features, potentially missing
significant cost optimization opportunities.

**Benefits of establishing this best
practice:**

- Superior performance and scalability through NetApp ONTAP
technology providing high throughput, low latency, and support
for petabyte-scale datasets in a single namespace.
- Advanced data management capabilities including automatic
tiering, compression, deduplication, and snapshot technologies
that optimize both performance and costs.
- Multi-protocol flexibility supporting NFS, SMB, iSCSI, and NVMe
protocols, enabling consolidation of diverse Microsoft workload
storage requirements on a single platform.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing Amazon FSx for NetApp ONTAP requires understanding
your enterprise storage requirements and planning for advanced
data management features. Focus on workloads that can benefit from
multi-protocol access, advanced data services, and cost
optimization through data efficiency features.

### Implementation steps

- Assess enterprise storage requirements for Microsoft
workloads including performance, capacity, protocol needs,
and data management requirements.
- Evaluate existing NetApp environments and plan migration
strategies to leverage familiar ONTAP features in the cloud.
- Configure FSx for ONTAP file systems with appropriate
performance tiers, capacity planning, and multi-protocol
access based on workload requirements.
- Implement data efficiency features including compression,
deduplication, and automatic tiering to optimize storage
costs and performance.
- Configure multi-protocol access (SMB, NFS, iSCSI) to support
diverse Microsoft workload requirements and enable workload
consolidation.
- Establish backup and disaster recovery procedures using
ONTAP's snapshot and replication capabilities for data
protection.
- Monitor storage performance, utilization, and cost
optimization through CloudWatch metrics and ONTAP management
tools.
- Implement ongoing data management policies including
tiering, retention, and capacity planning to maintain
optimal performance and costs.

## Resources

**Related documents:**

- [What
is Amazon FSx for NetApp ONTAP?](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
- [Managing
storage on Windows servers with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/managing-storage-on-windows-servers-with-amazon-fsx-for-netapp-ontap/)
- [Best
practice configuration of Amazon FSx for NetApp ONTAP for
Microsoft SQL Server workloads](https://aws.amazon.com/blogs/storage/best-practice-configuration-of-amazon-fsx-for-netapp-ontap-for-microsoft-sql-server-workloads/)
- [AWS Guidance: Best Practices for running MSSQL workloads on FSx for ONTAP](https://repost.aws/articles/AROwbUp134QbGhtrPPEYeuog/aws-guidance-best-practices-for-running-mssql-workloads-on-fsx-for-netapp-ontap)

**Related tools:**

- [Amazon FSx for NetApp ONTAP performance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp04.html*

---

# MSFTPERF03-BP05 Leverage instance store temporary block storage for EC2 instances

An instance store is a form of temporary block-level storage for EC2
instances, provided by disks physically attached to the host
computer. It is well-suited for storing frequently changing data
such as buffers, caches, and scratch data, as well as temporary data
replicated across multiple instances like in a load-balanced web
server pool, and Microsoft SQL Server TempDB data. The capacity and
number of instance store volumes available vary depending on the
instance type and size, with some instance types not offering
instance stores at all.

**Desired outcome:** Maximize I/O
performance for temporary and cache data in Microsoft workloads by
leveraging instance store volumes that provide the highest possible
storage performance through direct attachment to the host computer,
particularly beneficial for SQL Server TempDB, application caches,
and high-performance computing scenarios.

**Common anti-patterns:**

- Using EBS volumes for temporary data and caches when instance
store volumes are available, missing opportunities for maximum
I/O performance and potentially increasing storage costs.
- Storing persistent or critical data on instance store volumes
without understanding their temporary nature, risking data loss
during instance stops or failures.
- Choosing instance types without instance store when workloads
could benefit from high-performance temporary storage, limiting
application performance potential.

**Benefits of establishing this best
practice:**

- Maximum I/O performance through direct-attached storage that
provides the highest possible throughput and lowest latency for
temporary data operations.
- Cost optimization by using included instance store volumes for
appropriate use cases instead of provisioning additional EBS
volumes for temporary storage needs.
- Enhanced application performance for Microsoft workloads that
heavily utilize temporary storage, such as SQL Server TempDB
operations and application-level caching.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing instance store volumes requires careful planning to
ensure appropriate use cases and data management practices. Focus
on temporary, cache, and scratch data that can benefit from
maximum I/O performance while ensuring critical data remains on
persistent storage.

### Implementation steps

- Identify Microsoft workload components that generate
temporary data, caches, or scratch files that could benefit
from high-performance instance store volumes.
- Evaluate EC2 instance families that include instance store
volumes and assess their capacity and performance
characteristics for your workload requirements.
- Plan data placement strategies to ensure only appropriate
temporary data is stored on instance store volumes while
maintaining persistent data on EBS.
- Configure applications to utilize instance store volumes for
SQL Server TempDB, application caches, temporary files, and
other high-I/O temporary data.
- Implement data management procedures that account for the
temporary nature of instance store volumes, including
startup initialization and data replication strategies.
- Monitor instance store utilization and performance to
validate expected benefits and optimize usage patterns for
maximum efficiency.
- Establish operational procedures for instance lifecycle
management that properly handle instance store data during
maintenance and scaling operations.
- Document instance store usage patterns and include in
application deployment and disaster recovery procedures.

## Resources

**Related documents:**

- [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Make
instance store volume available for use on an EC2
instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/making-instance-stores-available-on-your-instances.html)

**Related tools:**

- [Instance
store volumes limits for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp05.html*

---

# MSFTPERF04 — Performance measurement

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MSFTPERF04-BP01 Use historical data to evaluate performance

Effective assessment of Microsoft workload performance requires
comprehensive data collection across key system components: compute,
memory, storage, and networking. This approach aligns with the
Well-Architected Framework's Performance Excellence guidelines,
specifically the best practice PERF02-BP03, which focuses on
gathering compute-related metrics. By monitoring these critical
areas, organizations can identify suboptimal performance and
implement timely corrective measures. This holistic monitoring
strategy enables proactive management of Microsoft workloads,
ensuring they meet performance expectations and allowing for swift
intervention when performance falls below desired thresholds.

**Desired outcome:** Establish
comprehensive performance data collection and analysis capabilities
for Microsoft workloads that enable data-driven optimization
decisions, proactive issue identification, and continuous
performance improvement through historical trend analysis and
performance pattern recognition.

**Common anti-patterns:**

- Collecting performance data without systematic analysis or
historical comparison, missing opportunities to identify
performance trends and optimization opportunities over time.
- Monitoring only basic system metrics without collecting
Microsoft-specific performance indicators, limiting visibility
into application-level performance issues and optimization
potential.
- Implementing reactive performance monitoring that only triggers
during incidents, rather than proactive analysis that can
prevent performance degradation before it impacts users.

**Benefits of establishing this best
practice:**

- Data-driven optimization decisions through comprehensive
historical performance analysis that identifies trends,
patterns, and optimization opportunities across Microsoft
workload components.
- Proactive issue identification and prevention through continuous
monitoring and analysis that can detect performance degradation
before it impacts business operations.
- Improved capacity planning and resource allocation through
historical data analysis that enables accurate forecasting of
future performance and scaling requirements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing comprehensive performance data collection and
analysis requires establishing systematic monitoring across all
Microsoft workload components and creating processes for regular
performance evaluation and optimization.

### Implementation steps

- Identify key performance metrics for Microsoft workload
components including compute, memory, storage, and network
performance indicators.
- Configure comprehensive monitoring using Amazon CloudWatch,
Performance Counters, and application-specific monitoring
tools to collect historical performance data.
- Establish data retention policies that maintain sufficient
historical data for trend analysis and performance
comparison over time.
- Implement automated data analysis and reporting processes
that regularly evaluate performance trends and identify
optimization opportunities.
- Create performance dashboards and visualization tools that
enable easy analysis of historical performance data and
trend identification.
- Establish regular performance review processes that analyze
historical data to identify patterns, anomalies, and
optimization opportunities.
- Document performance baselines and thresholds based on
historical analysis to enable effective anomaly detection
and alerting.
- Integrate historical performance analysis into capacity
planning and architectural decision-making processes for
continuous improvement.

## Resources

**Related documents:**

- [Monitoring
Windows services with Amazon CloudWatch](https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/)
- [How
do I use the CloudWatch agent on a Windows Server to view
metrics for Performance Monitor?](https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows)
- [How
to monitor Windows and Linux servers and get internal
performance metrics](https://aws.amazon.com/blogs/compute/how-to-monitor-windows-and-linux-servers-and-get-internal-performance-metrics/)
- [Run
ADOTCollector on AWS Windows Ec2 Host](https://aws-otel.github.io/docs/setup/build-collector-on-windows)

**Related tools:**

- [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)
- [OpenTelemetry](https://opentelemetry.io/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf04-bp01.html*

---

# MSFTPERF04-BP02 Define baseline performance requirements

Microsoft workloads vary in their performance needs, making
historical data analysis crucial for establishing baseline
performance metrics. This approach allows organizations to detect
and quantify performance fluctuations effectively. By implementing
targeted alerts, IT teams can quickly identify anomalies, such as
unexpected CPU usage spikes, changes in storage throughput,
increased memory consumption, or more intricate performance issues.
The collected monitoring data serves a dual purpose: it not only
helps in detecting problems, but also provides valuable insights for
ongoing performance optimization.

**Desired outcome:** Establish clear,
measurable performance baselines for Microsoft workloads that enable
effective anomaly detection, performance optimization, and capacity
planning while providing objective criteria for evaluating system
health and performance improvements over time.

**Common anti-patterns:**

- Operating Microsoft workloads without defined performance
baselines, making it difficult to identify when performance
degrades or to measure the effectiveness of optimization
efforts.
- Setting performance baselines based on assumptions rather than
actual historical data analysis, leading to inappropriate
thresholds that generate false alerts or miss genuine
performance issues.
- Creating static baselines that does not account for normal
performance variations or business cycles, resulting in alert
fatigue or missed performance degradation during expected usage
patterns.

**Benefits of establishing this best
practice:**

- Effective anomaly detection through well-defined baselines that
enable accurate identification of performance deviations and
potential issues before they impact business operations.
- Improved performance optimization through objective measurement
criteria that enable evaluation of optimization efforts and
identification of areas requiring attention.
- Enhanced capacity planning and resource allocation through
baseline-driven analysis that supports data-driven decisions
about scaling and infrastructure investments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing performance baselines requires systematic analysis of
historical performance data and establishment of meaningful
thresholds that account for normal variations while detecting
genuine performance issues.

### Implementation steps

- Collect sufficient historical performance data across all
Microsoft workload components to establish statistically
meaningful baselines.
- Analyze performance patterns including daily, weekly, and
seasonal variations to understand normal performance
fluctuations.
- Define performance baseline metrics for key indicators
including CPU utilization, memory consumption, storage I/O,
network throughput, and application response times.
- Establish performance thresholds and alert criteria based on
statistical analysis of historical data and business
requirements.
- Configure monitoring and alerting systems to detect
deviations from established baselines and notify appropriate
teams of performance anomalies.
- Implement regular baseline review and adjustment processes
to account for changing workload patterns and business
requirements.
- Document baseline definitions, measurement criteria, and
alert thresholds for consistent application across
environments and teams.
- Integrate baseline monitoring into operational procedures
and incident response processes to enable rapid performance
issue identification and resolution.

## Resources

**Related documents:**

- [Using
CloudWatch outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Best
practices for monitoring Microsoft SQL Server on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-ec2-best-practices/monitoring.html)
- [Windows
Server - Power and performance tuning](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/hardware/power/power-performance-tuning)
- [Select
the right instance type for Windows workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/right-size-selection.html)
- [FSx for Windows File Server performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
- [Windows
container memory requirements](https://docs.aws.amazon.com/eks/latest/best-practices/windows-oom.html#_windows_container_memory_requirements)

**Related tools:**

- [Amazon CloudWatch](https://docs.aws.amazon.com/cloudwatch/)
- [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf04-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
