# GAMECOST01 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# GAMECOST01-BP01 Implement attribution of cost per player, game feature, and environment

Cost attribution for game servers is usually simpler to perform than
game backend services because a game server is usually optimized to
be able to host a specific number of concurrent players per instance
which can be amortized across the cost of running the instance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For game backend services, it is recommended to de-couple the
components of your game into distinct features that can be managed
as separate logical or physical resources to make it
straightforward to analyze costs.

For example, although it may seem straightforward to implement a
single monolithic application to host game backend services, this
pattern makes it hard to derive the total cost per player and game
feature over time as you add more features because the compute,
networking, and storage costs of resources are shared across the
features. Consider adopting a serverless architecture for your
game backend services with services such as
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) and AWS Lambda or AWS Fargate for compute,
[Amazon SQS](https://aws.amazon.com/sqs/)
and [Amazon SNS](https://aws.amazon.com/sns/) for messaging, Amazon S3 for object storage, and Amazon DynamoDB for database storage. These services are just a few
examples of products that offer pricing that is usage-based and
primarily driven by request volume so that costs can be visualized
with granularity. Individual resources such as Lambda functions,
Fargate services, DynamoDB tables, and S3 buckets can be
associated with cost allocation tags so that you can attribute the
costs of these services with game feature names that make it
straightforward for you to understand the costs for each of your
services.

It is also recommended to separately manage each of your game
development environments so that you can attribute costs for the
different environments. Typically, game developers will manage
separate environments for development, test, staging and
production environments, as described in the operations pillar of
this games industry lens. Each environment usually has different
scalability, performance, and usage requirements and may be
managed by separate teams. To control costs, organize these
environments so that you can properly monitor and attribute the
costs of each environment.

For more information, refer to the following documentation:

- [Building
a serverless multi-player game that scales](https://aws.amazon.com/blogs/compute/building-a-serverless-multiplayer-game-that-scales/)
- [Standalone
game session servers with a WebSockets-based backend](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_websockets.html)
- [Standalone
game session servers with a serverless backend](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift_quickstart_customservers_designbackend_arch_serverless.html)

### Implementation steps

- De-couple game backend services into distinct features using
serverless or containerized architectures like AWS Lambda,
Amazon API Gateway, and AWS Fargate to enable granular cost
attribution per feature.
- Apply cost allocation tags to individual resources (for
example, Lambda functions, DynamoDB tables, and S3 buckets)
to associate costs with specific game features for better
cost analysis.
- Manage separate environments for development, testing,
staging, and production, organizing and monitoring their
costs independently to align with scalability and usage
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost01-bp01.html*

---

# GAMECOST01-BP02 Discover opportunities for optimization

Game developers and publishers can use AWS FinOps practices to help
optimize their cloud costs and gain better visibility into their
cloud spending. By doing so, game producers can align the average
cost required to maintain infrastructure for the players with the
financial results delivered by the game.

**Level of risk exposed if this best practice
is not established**: Low

## Implementation guidance

AWS offers a ready to use
[solution
guidance for Cloud Financial Management](https://aws.amazon.com/solutions/guidance/cloud-financial-management-on-aws/) to manage and
optimize your expenses for cloud services. This capability
includes granular visibility and cost and usage analysis to
support decision-making for topics such as spend dashboards,
optimization, spend limits, charge back, and anomaly detection and
response. The solution guidance for Cloud Financial Management
includes budget and forecasting features, giving you a defined,
cost-optimized architecture for your workloads so you can select
the right pricing model and attribute resource costs relevant to
your teams. This activates tracking, notification, and cost
optimization techniques across your environment and resources. You
can centrally manage expense information and give critical
stakeholders access as needed for targeted visibility and to
support decision-making.

Another key FinOps tool is the
[Cost
Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html), which provides a centralized view of cost
optimization recommendations and opportunities across your AWS accounts and AWS Regions, so that you can get the most out of your
AWS spend. You can use Cost Optimization Hub to identify, filter,
and aggregate AWS cost optimization recommendations across your
AWS accounts and AWS Regions. It makes recommendations on resource
rightsizing, idle resource deletion, Savings Plans, and Reserved
Instances. With a single dashboard, you avoid having to go to
multiple AWS products to identify cost optimization opportunities.

If your games teams are using shared AWS accounts the
[myApplications
in AWS Management Console Home](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/aws-myApplications.html), can be used to view application
resource costs for individual workloads. This granular view allows
you to identify the specific cost trends within your game
infrastructure, enabling you to make informed decisions about
resource allocation and optimization.

Additionally, regularly reviewing your billing and cost management
data with
[AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) uncovers hidden cost savings opportunities.
This detailed report provides a comprehensive breakdown of your
cloud spending, allowing you to identify areas of overspending,
unutilized resources, and opportunities to take advantage of more
cost-effective services or pricing models.

By embracing FinOps principles and leveraging the tools provided
by AWS, game developers and publishers can make the most efficient
use of their cloud resources, ultimately enhancing their bottom
line and freeing up funds for further game development and
innovation.

### Implementation steps

- Use AWS Cloud Financial Management tools for granular and
detailed visibility, spend dashboards, anomaly detection,
and cost attribution to optimize and track cloud expenses
effectively.
- Use the Cost Optimization Hub to centralize rightsizing,
Savings Plans, and Reserved Instance recommendations across
AWS accounts and Regions.
- Regularly review AWS billing data using Data Exports and
MyApplication on AWS to help analyze workload-specific
costs, uncover savings opportunities, and optimize resource
allocation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamecost01-bp02.html*

---
