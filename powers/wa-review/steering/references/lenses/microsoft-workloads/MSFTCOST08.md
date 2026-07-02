# MSFTCOST08 — .NET

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MSFTCOST08-BP01 Refactor to cross-platform .NET and move to Linux

Migrating .NET Framework applications to .NET 8 or later enables
cross-platform deployment, improved security, and better
performance. This modernization allows applications to run on Linux
systems, leverage cloud-native features, and benefit from the latest
optimizations, resulting in more efficient and maintainable systems.

**Desired outcome:** Aim to achieve
reduced licensing costs, improved performance, and enhanced
security. The modernized applications run efficiently on Linux
environments, including AWS Graviton processors, while leveraging
the latest .NET features and cloud-native capabilities. This
transformation results in a more cost-effective, scalable, and
maintainable application portfolio that aligns with modern cloud
architecture principles.

**Common anti-patterns:**

- Continuing to rely on Windows-specific dependencies and COM
components without evaluating modern alternatives, making the
migration to Linux impossible and perpetuating technical debt
and higher operational costs.
- Attempting to run portions of the application on Linux while
keeping critical components on Windows servers, creating a
complex hybrid architecture that increases operational overhead
and negates the cost benefits of the migration while introducing
potential compatibility issues.

**Benefits of establishing this best
practice:**

- Moving to Linux eliminates Windows licensing costs while
enabling the use of cost-effective infrastructure options like
AWS Graviton processors, resulting in significant operational
cost savings and improved performance metrics through modern
.NET optimizations.
- Cross-platform .NET applications can be deployed across diverse
environments using containerization technologies, enabling
efficient CI/CD pipelines, simplified scaling strategies, and
better resource utilization in cloud environments, leading to
improved application reliability and reduced maintenance
overhead.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin with an AWS Transform-assisted assessment to identify
Windows dependencies, then implement an incremental migration
strategy focusing on high-impact components first. Utilize
automated refactoring tools for conversion to cross-platform .NET,
containerize the application, and establish comprehensive testing
protocols to ensure successful deployment on Linux environments
while maintaining application performance and reliability.

### Implementation steps

- Conduct application assessment using AWS Transform to
identify Windows dependencies and migration challenges
- Develop a phased migration plan, prioritizing components for
maximum cost-benefit impact
- Refactor code to cross-platform .NET using AWS Transform's
AI-powered tools and manual adjustments
- Containerize the application and implement a robust testing
strategy for Linux environments
- Deploy the refactored application to Linux servers,
including AWS Graviton instances, and monitor performance

## Resources

**Related documents:**

- [Refactor
to modern .NET and move to Linux](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-refactor-linux.html)

**Related tools:**

- [Modernizing
.NET with AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost08-bp01.net-and-move-to-linux.html*

---

# MSFTCOST08-BP02 Consider serverless architecture for your Microsoft .NET applications

AWS Lambda enables .NET developers to build serverless applications
without managing servers, paying only for actual usage. Using modern
.NET versions, developers can create scalable functions in C# or F#
that run on-demand in the cloud, reducing costs and development
time.

**Desired outcome:** By adopting
serverless architecture with AWS Lambda for .NET applications,
organizations may achieve improved scalability and cost efficiency,
paying only for resources used while eliminating server management
overhead. Using AWS tools like Microservice Extractor may further
simplify the modernization of existing applications.

**Common anti-patterns:**

- Maintaining continuously operational and over-sized servers for
.NET applications instead of leveraging serverless architecture,
resulting in unnecessary costs and underutilized resources.
- Keeping large and monolithic .NET applications intact rather
than breaking them down into microservices or serverless
functions, leading to reduced flexibility and scalability.

**Benefits of establishing this best
practice:**

- Organizations only pay for actual compute resources consumed
during function execution, eliminating costs associated with
idle server capacity and infrastructure management.
- Development teams can focus on code rather than server
maintenance, reducing operational overhead and accelerating
deployment cycles.
- Applications automatically scale based on demand without manual
intervention, ensuring optimal performance during peak loads
while maintaining cost efficiency during low-usage periods.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by identifying suitable .NET applications or components that
can benefit from serverless architecture. Start small by migrating
discrete functions to AWS Lambda using modern .NET versions (Core
or later). Utilize AWS Microservice Extractor for .NET to analyze
and decompose existing monolithic applications into smaller,
manageable services. Implement proper monitoring and logging from
the outset using AWS CloudWatch, and establish clear deployment
pipelines using AWS CI/CD tools. Gradually, expand the serverless
footprint as the team gains experience and confidence with the
architecture.

### Implementation steps

- Install and configure AWS Microservice Extractor for .NET to
analyze existing monolithic applications and identify
potential microservice candidates
- Assess existing .NET applications and identify functions
suitable for serverless migration, prioritizing stateless
operations and event-driven processes
- Set up the AWS Lambda development environment with .NET SDK
and necessary AWS tools (AWS Toolkit for Visual Studio and
AWS CLI)
- Create and test initial Lambda functions using modern .NET
versions, implementing proper error handling and logging
- Configure automated deployment pipelines using AWS CI/CD
services (CodePipeline and CodeBuild) for consistent
function updates
- Monitor function performance and costs using AWS CloudWatch,
and optimize resource allocation based on actual usage
patterns

## Resources

**Related documents:**

- [Consider
serverless .NET](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-serverless.html)

**Related tools:**

*[What
Is AWS Microservice Extractor for .NET?](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost08-bp02.net-applications.html*

---
