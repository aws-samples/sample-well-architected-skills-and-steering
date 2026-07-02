**Pillar**: Cost Optimization

# FSICOST11: Do you use cost tradeoffs of various AWS pricing models in your workload design?

Cloud cost is an important part of the design and architecture process and is used in
making trade- offs between quality, performance, security and other non-functional
requirements. Cloud cost is considered when selecting AWS services (using building block
services such as Amazon EC2 versus using managed services such as Amazon ECS).

## FSICOST11-BP01 Identify pricing models and savings plans for your selected AWS services when designing your architecture

Cloud cost is an important part of the design and architecture process and is used in
making trade- offs between quality, performance, security and other non-functional
requirements. Cloud cost

is considered when selecting AWS services (using building block services such as
Amazon Elastic Compute Cloud versus using managed services such as Amazon Elastic Container Service).

Cloud cost is an important part of the design and architecture process and is used in
making trade-offs between quality, performance, security and other non-functional
requirements.

For generative AI workloads, consider the following:

- Model selection based on actual performance requirements against cost
- Inference optimization through batching and caching
- Vector store efficiency and storage optimization
- Prompt engineering for cost efficiency
- Agent workflow cost management

Cloud cost is considered when selecting AWS services (using building block services
such as Amazon EC2 versus using managed services such as Amazon ECS or Amazon Bedrock for generative
AI workloads).

Cost factors that go into the selection of cloud resources based on the level of cost
optimization provided by pricing models or AWS services include: Savings Plans, Reserved
Instances, Amazon EC2 Spot Instances, or Amazon S3 Intelligent-Tiering. Cost trade-offs also include
resource-level decisions based on performance (for example, selecting an XL instead of a
2XL resource size).

Product designs take the pricing structure of AWS services into account (for
example, Elastic Load Balancing charges for elasticity and inter-Availability Zone data transfer charges).
Design activities also include cost estimation for the services being built using the
AWS Pricing Calculator, AWS Price List API, or third-party pricing tools, or they might involve
building and deploying proof of concepts to measure actual costs.

The cost of the new workload is measured on an ongoing basis during the workload's
entire lifecycle, and unexpected cost variances are used to influence future product
changes in the workload. Here are several examples:

- **Pricing trade-offs:** Select foundation or fine-tuned
models based on objective price-performance ratios, running periodic evaluation jobs
that compare accuracy vs cost. Codify model routing rules (for example, gold, silver,
and bronze tiers) to ensure workloads default to cost-efficient models unless premium
accuracy is justified. Implement guardrails to cap maximum context length and enforce
review or approval for gold-tier model usage.
- **Architecture patterns:** Introduce serverless RAG
orchestrators that automatically short-circuit high-confidence cache hits, reducing
duplicate inference calls. Apply response compression or summarization before storage
to cut downstream S3 or vector store costs. Use Amazon Bedrock Guardrails and content
filters to minimize token waste from rejected or repeated outputs.
- **Managed services:** AWS managed services helps reduce
operational overhead to maintain servers, apply patches, and add high availability,
security etc. Plan to use as many managed services as possible to reduce operational
cost.
- **Serverless architecture:** FSI companies often have the
need to set up automation for processing events and workflows for technology
operations. If you use EC2 instances or databases, you are likely not using 100% of
the compute capacity at all times. Many customers only use 10–20% of the available
capacity in their EC2 fleet at any point in time. This average is also affected by
High Availability and Disaster Recovery requirements, which typically result in idle
servers waiting

for traffic from failovers. In serverless models such as AWS Lambda or DynamoDB, you pay
per- request and by duration of time. Additionally, serverless architectures can lower the
overall Total Cost of Ownership (TCO) since many of the networking, security, and DevOps
management tasks are included in the cost of the service.

- **Caching data:** Most of the fintech customers use the
API heavily. So to optimize on time and money, implement caching mechanisms like
caching at the edge or caching data in in-memory cache and so on. This depends on the
type of the APIs and how APIs are designed. In the case of static data, you can cache
at the edge for long-term, and for dynamic content you can cache in in-memory stores
or for a short duration.
- **Right storage selection:** Select the right storage
mechanism to optimize cost across metrics, such as storage, IOPS, and data throughput.
You can use a combination of the Amazon S3 family of products or AWS database products
such as: Amazon Redshift, Amazon RDS, Amazon FSx, Amazon EBS , or Amazon EFS. For more information about
these services, see: [Amazon Storage](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html)
[overview](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html) and
[AWS Database.](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html)
- **Choosing the right instances and usage of Spot
Instances:** Choose the right instances, and choose Spot Instances if
possible to optimize the cost. You can mix and match with Spot Instances and on-demand
capacity. You can use a base amount of capacity with On-Demand Instances, and use Spot
Instances for spikes in demand.
- **CPU architecture:** If your application is not
dependent on a specific CPU architecture like ARM versus x86, you might consider
Graviton-based instances. Many AWS services, including Amazon EC2, Amazon Aurora, Amazon ElastiCache,
Amazon EMR, AWS Lambda, and AWS Fargate, support AWS Graviton-based instances with
significant price performance benefits. For more information, see [Getting started with
Graviton](https://aws.amazon.com/ec2/graviton/getting-started/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost11.html*
