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
