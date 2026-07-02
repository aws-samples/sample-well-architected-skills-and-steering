# GAMESUS02 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 2

---

# GAMESUS02-BP01 Select managed services for appropriate compute workloads

Architect your game backend services to use managed services for
event driven or highly variable traffic workloads. Managed services
shift the management of infrastructure to AWS and distributes the
environmental impact across multiple users because of the
multi-tenanted control planes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS services like AWS Lambda, AWS Fargate (Containers), and Amazon
Gamelift (Game server orchestration) can run code, containers, or
orchestrate your game servers without having to manage the
underlying infrastructure. These services automatically scale
based on player demand and you're only charged for the resources
you consume. Because the underlying infrastructure is managed on
your behalf, you are able to focus solely on your games and
backend services' requirements.

You can use [AWS Lambda](https://aws.amazon.com/lambda/) to run code without provisioning or managing
servers. Lambda runs your code on a high-availability compute
infrastructure and performs the administration of the compute
resources, including server and operating system maintenance,
capacity provisioning and automatic scaling, and logging. With
Lambda, you need to supply your code in one of the language
runtimes that Lambda supports. Lambda is useful for processing
game events, player authentication, in-game purchase processing,
and matchmaking requests. Lambda automatically scales based on the
number of events and can handle unexpected spikes in traffic.

[AWS Fargate](https://aws.amazon.com/fargate/?nc=sn&loc=0) is a serverless compute engine for containers that
works with both
[Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (ECS) and
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (EKS). AWS Fargate makes it
straightforward to focus on building your applications by
alleviating the need to provision and manage servers, lets you
specify and pay for resources per application, and improves
security through application isolation by design. Fargate is ideal
for backend services that handle player profiles, state management
and matchmaking.

[Amazon
GameLift](https://aws.amazon.com/gamelift/) is a managed service for deploying, operating, and
scaling dedicated game servers for session-based multiplayer
games. You can deploy your first game server in the cloud in just
minutes, saving up to thousands of engineering hours in upfront
software development and lowering the technical risks that often
cause developers to cut multiplayer features from their designs.

### Implementation steps

- Use AWS Lambda for event-driven workloads like processing
game events, player authentication, in-game purchases, and
matchmaking requests, leveraging its automatic scaling and
serverless management.
- Deploy AWS Fargate with ECS or EKS for backend services such
as player profiles, state management, and matchmaking,
removing server management and improving application
isolation.
- Use Amazon GameLift to deploy and scale dedicated game
servers for session-based multiplayer games, reducing
development time and operational complexity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesus02-bp01.html*

---

# GAMESUS02-BP02 Right-size your compute and deploy GPU performance only where needed

Architect your game servers and backend to efficiently utilize
compute resources. Over-provisioning compute can lead to unnecessary
costs and minimizes the amount of idle or under-utilized resources.
GPU instances should be used to support specific development efforts
like HLOD rebuilds in Unreal, or if you game servers require them by
design. This greatly reduces the environmental impact and costs of
your workloads.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You should optimize your game servers and backend services to use
multiple EC2 instances types and the least number of instances
needed. This increases the number of instances available to meet
your needs during development or for your games launch. You should
also match the instance type to the specific workload you're
deploying. Compute Optimized instances support a wide range of
use-cases including game servers and backend services like
matchmaking. Memory Optimized instances are designed to deliver
fast performance for workloads that process large data sets in
memory. Use GPU instances as required for high performance
requirements, but not for general computing tasks. If able,
architect your services or game servers to run on ARM with
[AWS Graviton instances](https://aws.amazon.com/ec2/graviton/). Graviton is the most performant to
energy efficient instance type available on AWS. They also offer
improved performance and costs when compared to x86 instance
types.

Use the
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify the optimal AWS resource
configurations, such as Amazon Elastic Compute Cloud (EC2)
instance types, Amazon Elastic Block Store (EBS) volume
configurations, task sizes of Amazon Elastic Container Service
(ECS) services on AWS Fargate, commercial software licenses, AWS Lambda function memory sizes, and Amazon Relational Database Service (RDS) DB instance classes, using machine learning to
analyze historical utilization metrics. Compute Optimizer provides
a set of APIs and a console experience to reduce costs and
increase workload performance by recommending the optimal AWS
resources for your AWS workloads.

### Implementation steps

- Match compute resources to specific workloads by using
Compute Optimized instances for game servers, Memory
Optimized instances for large data sets, and GPU instances
only for tasks like HLOD rebuilds or GPU-dependent game
servers.
- Optimize compute utilization by deploying AWS Graviton
instances where possible for energy efficiency, better
performance, and cost savings compared to x86 instances.
- Use AWS Compute Optimizer to analyze historical utilization
and recommend the most efficient configurations for EC2, AWS
ECS, AWS Lambda, and Amazon RDS workloads to reduce costs
and improve performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesus02-bp02.html*

---
