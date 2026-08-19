# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 19

---

# FSICOST01: Is your cloud team educated on relevant technical and commercial optimization mechanisms?

Due to the size of many financial services enterprise customers, the benefits of
aligning your IT organization with a Cloud Financial Management approach helps you save on
the costs of both infrastructure and operations. To enable this capability, invest in
knowledge building programs, resources, and processes to help become a more cost-efficient
organization.

## FSICOST01-BP01 Evangelize cloud education among all (including non-technical) staff and stakeholders

A company-sponsored cloud training program exists, and is required for all cloud
stakeholders regardless of their seniority or affiliated organization.

A company-sponsored cloud training program exists, and is required for all cloud
stakeholders regardless of their seniority or affiliated organization. For organizations
implementing generative AI workloads, this training should include:

- On-demand courses for teams to learn about cost optimization for both traditional
cloud services and generative AI workloads. This includes model selection strategies,
token optimization, vector store management, and efficient prompt engineering
practices.
- In-person and virtual training from instructors who teach your team in a hands-on
learning environment about cost-effective implementation of generative AI solutions.
For new employees, this should be part of their onboarding training, and should be
mandatory training on a yearly basis for all existing employees and contractors.
- Technical skills and cloud expertise, including generative AI
implementation, to grow your career and business. Encourage specialization in AI/ML
cost optimization paths where available.
- Prompt engineering for cost, response size control, retrieval scope
limiting, embeddings batch sizing, and model A/B testing for price‑performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost01.html*

---

# FSICOST02: Do you apply the Pareto-principle (80/20 rule) to manage, optimize, and plan your cloud usage and spend?

Investing the right amount of effort in a cost optimization strategy up front allows
you to realize the economic benefits of the cloud more readily, by ensuring a consistent
adherence to best practices and avoiding unnecessary over provisioning. CFM is paramount not
only to effectively manage costs, but also to verify that investments are driving expected
business outcomes.

## FSICOST02-BP01 Apply the Pareto-principle 80/20 rule for your CFM efforts

No matter your organization size, pay specific attention to your capacity investment
while developing CFM-related concepts. Here are some examples of CFM activities to apply
the 80/20 rule to create an optimal input and output solution.

- **Cost allocation:** Start with default allocation
opportunities (per AWS account, AWS-generated createdBy tag), then follow up by
tagging all AWS services that support tagging, check overall percentage of cost
allocation. For generative AI workloads, implement specific tags for model selection,
inference costs, and vector store usage. In case you reach 80% cost allocation, check
if equal allocation of the unallocated 20% of costs is acceptable for your
organization (for example, splitting AWS service cost equally between business units
or teams). Before spending time and budget on a third-party solution (for example,
telemetry) ensure that shared resources you aim to allocate are substantial (for
example, over 20% of monthly bill).
- **Cost optimization:** Incorporate implementation of
low-hanging cost optimization recommendations (from Cost Explorer or AWS Trusted Advisor) into daily
activities of your teams. Centralized teams evaluate and book SP and RI quarterly,
decentralized teams perform instance rightsizing and modernization weekly. For
generative AI workloads, analyze and optimize the generative AI pricing model for your
most-used services. Implement cost-aware prompting for frequently used applications.
Optimize cost-informed vector stores for your highest-volume data. Review and refine
cost-informed agents in your most critical automated workflows. CFM practitioners
report it is more efficient to spend 30 minutes per week rather than one day per
month. While implementing cost optimization that requires technical changes, pay
attention to long term benefits, as one-time adjustments can provide reoccurring
savings. Evaluate time and capacity invested into technical adjustments versus cost
saving for at least the next 24 months. These types of calculations help prioritize
activities with the highest impact. Target the top 20% of prompts or flows that drive
~80% of generative AI spend. Apply caching (RAG result caches), prompt trims, and
model downgrades (for example, from large general models to smaller task‑specific
models) on those paths first.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost02.html*

---

# FSICOST03: Do you use automation to drive scale for Cloud Financial Management practices?

Automation can drastically reduce the cost of the CFM. You can provision resources
using auto scaling or using managed services, set budgets to meet, and alerts to inform
users on cost utilization. For generative AI workloads, this includes automated model
scaling, token usage monitoring, and vector store optimization.

## FSICOST03-BP01 Use automation to drive scale for Cloud Financial Management practices

Automation can drastically reduce the cost of the CFM. You can provision resources
using auto scaling or using managed services, set budgets to meet, and alerts to inform
users on cost utilization.

Automating operations reduces the frequency of manual tasks, improves efficiency, and
benefits enterprises by delivering a consistent and reliable experience when deploying,
administering, or operating workloads. You can free up human resources from manual
operational tasks and use them for higher value tasks and innovations, thereby improving
business outcomes. For example, teams can focus on improving prompt engineering or
developing new AI use cases instead of managing infrastructure. Enterprises require a
proven, tested way to manage their workloads in the cloud. That solution must be secure,
fast, and cost effective, with minimum risk and maximum reliability.

Automate token budget enforcement and anomaly alerts: fail‑safe requests that exceed
thresholds; alert when token‑per‑call or cost‑per‑session deviates materially from
baseline.

Schedule off‑peak embedding and fine‑tuning jobs; auto‑pause development endpoints
and ephemeral agents outside working hours.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost03.html*

---

# FSICOST04: How do you promote cost-awareness within your organization?

Awareness of usage at all levels in the organization is key to driving change, as
change in usage drives changes in cost. Consider taking a multi-faceted approach to becoming
aware of your usage and expenditures. Your team must gather data, analyze, and then report.

## FSICOST04-BP01 Promote a culture of transparency on costs

To promote transparency and accountability of costs, it is important to have standard
mechanisms that show or charge back the costs to business units or applications. Companies
use tags to allocate cost to teams, business units, or organizations within an enterprise
and to observe trends. Enforce a tagging taxonomy with tag policies within pipelines that
deploy infrastructure as code (IAC) and govern using SCPs at the organization-level and
configuration across all AWS accounts. For more information on tags, see: [Using
AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).

For generative AI workloads, implement additional tagging for:

- Model inference costs
- Token usage
- Vector store operations
- Knowledge base storage
- Agent workflow execution

Adopt a generative AI cost scorecard per product or use-case team that tracks metrics
such as cost per 1K tokens, average context length, cache hit rates, and percentage of
calls by model tier (for example, gold, silver, and bronze). Visualize this data in
dashboards to drive accountability and promote informed optimization decisions across
engineering and business stakeholders.

In the large organization, some teams are very advanced in cost optimization and they
are aware of cost impacts while other teams are not that mature. Hence, team cooperation,
sharing importance of Cloud Finance Management, Cloud Center of Excellence is extremely
important to promote

a culture of cost optimization. For more information on tags, see [Using
AWS cost](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
[allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost04.html*

---

# FSICOST05: How do you track anomalies in your ongoing costs for AWS services?

Understanding your organization's costs and drivers is critical for managing your cost
and usage effectively, and identifying cost-reduction opportunities. Accurate cost and usage
monitoring allows you to make more informed decisions about where to allocate resources
within your organization.

## FSICOST05-BP01 Be aware of anomalies and periodically review your architecture

Anomalies can drive up cost. Set up AWS Cost Anomaly Detection to detect and alert
on anomalous spend patterns in your deployed AWS services. Cost Anomaly Detection
automatically determines thresholds each day by adjusting for organic growth and seasonal
trends (like usage increases from Sunday to Monday or increased spend at the beginning of
the month) through machine learning models. Financial systems usually integrate with
several other third-party systems, and Cost Anomaly Detection can integrate with these
systems as well.

Extend Cost Anomaly Detection with custom metrics such as `token_in`,
`token_out`, and `embedding_ops`, and route alerts to product or
data owners when cost spikes correspond to new prompt deployments, unexpected
retrieval-augmented generation (RAG) expansion, or fine-tuning jobs running out of
schedule. Combine these alerts with CloudWatch dashboards to correlate generative AI usage
trends with cost anomalies in near real-time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost05.html*

---

# FSICOST06: How do you track your workload usage cycles?

Financial services workload usage can be cyclical and can have usage spikes during
specific days like month-end or quarter-end, or it can be intra-day during specific hours.
AWS provides customers with a number of usage monitoring services that can scale your
operations up and down as demand conditions require. Monitor cost at an application-level,
and a workload-level on a regular basis, and optimize usage of resources and cost.

## FSICOST06-BP01 Monitor your workload usage cycle around times of higher and lower utilization (quarter-end, year-end, weekends, and holidays) to identify ways to reduce your costs

You may have workload usage cycles for week-end or month-end, and quarter-end have
more usage of resources. In some cases, there could be higher usage due to events like the
start of trading hours, holidays shopping, and so on. Monitoring usage and corresponding
events are helpful to optimize cost and architecture. You can choose to shutdown unused
instances, for example Amazon EC2 servers for development, or QA on Friday, and bring them back
up on Monday.

Scale generative AI inference endpoints and vector search infrastructure dynamically
with observed diurnal patterns. Pre-warm minimal capacity only for peak trading or
batch-report windows, then decay to zero or low-cost tiers during off-hours. Automate
these adjustments via scheduled scaling policies or event-driven Lambda functions to
minimize idle inference costs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost06.html*

---

# FSICOST07: Are you using all the available AWS credit and investment programs?

Multiple credit options are available, such as migrations, digital innovation, cloud
economics, and prototyping to activate credits.

## FSICOST07-BP01 Use AWS credit programs such as Migration Acceleration Plan, Digital Innovation, and Activate to save costs and drive cloud adoption

Multiple credit options are available, such as: Migrations, Digital Innovation, Cloud
Economics, Prototyping to Activate credits. Different departments work in silos, and often
the credits earned by the workload in one department need to be publicized for consumption
across the other units. Ensure that the workloads are leveraging these credits across the
organization. Purchasing third- party products or even data from AWS Marketplace. Talk to your
account team to get relevant information on a regular basis for available credit programs.
For example, Activate provides up to $100K in credits for startups.

Extend credit and investment usage to support generative AI adoption programs, such
as proof-of-concepts for foundation-model integration, prompt optimization, or internal
knowledge-base generation. Use MAP and AI/ML investment programs to fund generative AI
proof of concepts on Amazon Bedrock, Amazon SageMaker AI, or Amazon Comprehend, keeping experimentation with
models and vector databases cost-neutral during early exploration. Encourage cross-team
visibility so that AI/ML and analytics units share investment benefits rather than
duplicating spend.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost07.html*

---

# FSICOST08: Are you monitoring usage of Savings Plans regularly?

Capacity planning and usage forecasting is important for managing your commitment
plans. Gain better control of the flexibility of Savings Plan usage and manage costs with
regular monitoring on a regular cadence over quarterly basis, or reviews at regular time
intervals.

## FSICOST08-BP01 Sign up for a compute savings plan for discounts on compute versus on-demand pricing

Financial systems usually have a predicted usage pattern. Sign up for a compute
savings plan, as they offer discounts on compute of up to 72% compared to on-demand
pricing. The most flexible type of Savings Plan applies across the core compute services
(Amazon EC2, AWS Fargate, and AWS Lambda) and across Amazon EC2 instance size, operating system,
tenancy, Availability Zone, and Region. This flexibility accommodates continuously
evolving workloads and avoids unused commitment. Instead of a single monolithic savings
plan, opt for smaller concurrent active Savings Plans, which are additive to reduce commitment
risk, increase discount coverage, and relieve the burden of long-range usage predictions.
Gain better control of the flexibility of Savings Plan usage and manage costs with regular
monitoring on a regular cadence over quarterly basis, or reviews at regular time
intervals.

[Understand how](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-applying.html) Savings Plans can also be shared across all accounts within an AWS
Organization or consolidated billing family.

For steady inference and model-serving workloads, pair Savings Plans with provisioned
throughput or concurrency settings on managed generative AI endpoints (for example, Amazon
Bedrock or Amazon SageMaker AI Endpoint). Avoid over-commitment by separating development or test
environments from production accounts and verify that only sustained production traffic
uses reserved compute capacity. Review plan coverage quarterly as model architectures,
token volumes, and context sizes evolve.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost08.html*

---

# FSICOST09: Are you using the cost advantages of tiered storage?

FSI companies usually have long retention policies for their regulatory and audit
requirements. They usually span multiple years and might even be able to take up to a day or
two to be able to retrieve old data. Understand and use the cost advantages of tiered
storage.

## FSICOST09-BP01 Define data retention policies to select the right storage type for your data lifecycle

FSI companies usually have long retention policies for their regulatory and audit
requirements. They usually span multiple years and might even be able to take up to a day
or two to be able to retrieve old data. Defining data retention policies and corresponding
architecture to transfer data from main storage to archival storage is important. This can
be achieved by transferring data from RDS database to S3 or creating a snapshot and
storing it for better cost efficiencies.

Apply lifecycle policies for Retrieval-Augmented Generation (RAG) artifacts and
generative AI datasets: maintain hot vector indexes (for current-quarter documents or
active knowledge bases) in high-performance vector databases, transition warm data
(historical embeddings or older training data) to object storage such as Amazon S3 Standard–IA,
and archive cold or infrequently accessed corpora (for example, legacy PDFs, or processed
embeddings) in Amazon Glacier or Deep Archive. Automate transitions using S3 Lifecycle policies to
minimize long-term storage costs while preserving retrieval fidelity when needed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost09.html*

---

# FSICOST10: Do you use lower cost Regions to run less data-intensive or time-sensitive workloads?

FSI companies usually have to plan their Disaster Recovery (DR) and also run a cadence
of dry runs for regulatory purposes, and typically opt to setup their DR site in an
alternate AWS Region. Depending on the SLA for latency, data sovereignty and compliance
needs, you could run DR in a less costly Region.

## FSICOST10-BP01 Use less costly Regions for disaster recovery and test platforms

FSI companies usually must plan their Disaster Recovery (DR) and also run a cadence
of dry runs for regulatory purposes, typically opting to set up their DR site in an
alternate AWS Region. Depending on the SLA for latency, data sovereignty, and compliance
needs, you could run DR in a less costly Region. Consider cheaper Regions for
non-production environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost10.html*

---

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

---

# FSICOST12: Are you saving costs by adopting a set of modern microservice architectures?

Financial institutions are moving from monolithic legacy systems such as mainframes
into modern microservices architectures, giving them the flexibility of provisioning
multiple environments to develop features rapidly, instead of waiting for the single
monolith environment to be available, giving them greater agility and faster time-to-market.

## FSICOST12-BP01 Migrate your mainframe and on-premises infrastructure to adopt a cloud-based microservices approach

Financial institutions are moving from monolithic legacy systems such as mainframes
into modern microservices architectures, giving them the flexibility of provisioning
multiple environments to develop features rapidly, instead of waiting for the single
monolith environment to be available, giving them greater agility and faster
time-to-market. Quantifying this gain is important for stakeholder buy-in.

Apply microservice design to generative AI architectures by decomposing large AI
pipelines into modular micro-flows such as *retrieve*,
*reason*, and *act*. This allows each step to
scale and cost-optimize independently — for example, using smaller, lower-cost models for
retrieval or classification, while reserving larger, high-quality models for reasoning or
complex generation tasks. Deploy each flow as a separate containerized or serverless
component (for example, using AWS Lambda, Amazon ECS, or Step Functions) to improve cost
control, maintainability, and fault isolation.

This modular approach aligns generative AI workloads with modern software delivery
practices and enables continuous cost visibility and performance tuning across the AI
lifecycle.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost12.html*

---

# FSICOST13: Do you use cloud services to accommodate consulting or testing of projects?

Some financial services institutions hire contractors during specific months, or for a
project. Procuring a new machine, and ensuring that it is meeting the compliance standards
of a financial services institution can be resource intensive. Using a service like Amazon
WorkSpaces for end-user computing can help with cost-efficient utilization of resources.

## FSICOST13-BP01 Set up pay-as-you-go services when team expands for certain duration

Some financial services institutions hire contractors during specific months, or for
a project. These contractors can work on a project for a short duration, like 6 months to
a year. Procuring a new machine, and ensuring that it is meeting the compliance standards
of a financial services institution can be resource intensive. Using a service like [Amazon WorkSpaces](https://aws.amazon.com/workspaces/faqs/) for end-user computing can
help with cost-efficient utilization of resources. You can create workspaces per your
internal standards, and provision it for a new resource.

**Testing and consulting environments** Extend this
principle to generative AI experimentation by provisioning temporary, cost-capped
environments for proof of concept or consulting engagements. Use ephemeral inference
endpoints (for example, Amazon Bedrock provisioned throughput with automatic teardown) and
time-bounded SageMaker AI Studio domains for data scientists and contractors.

Establish guardrails that enforce token quotas, model tier limits, and usage budgets
per project, keeping generative AI testing compliant and cost-efficient. For partner or
consulting access, apply fine-grained IAM roles and service control policies (SCPs) to
segregate environments and avoid cross-account spend leakage.

Automate cleanup of idle notebooks, vector stores, and test embeddings using
AWS Lambda or Amazon EventBridge rules, verifying that sandbox environments incur zero residual cost
post-engagement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost13.html*

---

# FSICOST14: How do you measure the cost of licensing third-party applications and software?

If you are using third-party software, understand the specific licensing terms of each
third-party vendor.

## FSICOST14-BP01 Consider the cost of licensing third-party applications and software

If you are using third-party software, understand the specific licensing terms of
each third- party vendor. AWS offers both Dedicated Hosts that have pre-installed
virtualization software (Hypervisor) whereas bare metal servers do not have pre-installed
virtualization software.

Choosing the right instance type specific to the licensing terms may reduce your
third-party licensing costs.

Generally, third-party software applications and associated support can provide your
workload with a lower overall cost of ownership than in-house created applications.
Because software vendors have a much broader perspective of customer requirements, their
software can more economically support a wider range of use cases than an in-house
developed solution. A software support agreement reduces your technical debt when new
workload features are needed.

**Licensing**

Evaluate model and API-based generative AI licensing with the same rigor as
traditional third-party software. Assess cost per token, per model family, and concurrency
tier against your workload profiles and expected query volumes. Prefer consumption-based
or hybrid contracts with transparent scaling guardrails and the ability to downshift to
smaller models when latency or accuracy trade-offs are acceptable.

Track licensing renewals and vendor rate changes (for example, third-party LLM
providers or external model APIs) through your Cloud Financial Management tooling to avoid
unplanned cost escalations. For regulated environments, ensure data residency and usage
terms align with your compliance obligations before committing to external generative AI
model providers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost14.html*

---

# FSICOST15: Have you reviewed your ongoing cost structure tradeoffs for your current AWS services lately?

You can optimize cost over time by reviewing new services and implementing them in your
workload. As AWS releases new services and features, it is a best practice to review your
existing architectural decisions to ensure that they remain cost effective.

## FSICOST15-BP01 Monitor and optimize your ongoing costs, ROIs, and tradeoffs against alternative AWS services on a periodic basis to maintain your lowest cost of ownership

Financial services institutions add new human resources periodically, like
contractors, vendors, or FTEs, so it is necessary to maintain a cost-aware culture. There
are also enhancements from AWS on cost-related services. You should conduct periodic
workshops, sessions on effective ways to measure, monitor and optimize cost to spread
awareness of cost optimization to existing resources, as well as new resources on the
team. The frequency of such workshops should be at least once every six months. Every six
months, or during the session, you should recognize cost optimization wins and recognize
individual people driving or contributing to the cost optimization. This drives
cost-optimization culture in a team.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost15.html*

---

# FSICOST16: Are you continuously assessing the ongoing costs and usage of your cloud implementations?

There is a process to examine existing cloud spend, and identify cost optimization
opportunities using manual analysis, or the use of tools (AWS Billing and Cost Management and AWS Cost Management tools, AWS
Partner tools, open-source tools, or DIY tools). As your requirements change, be aggressive
in decommissioning resources, components, and workloads that you no longer require.

## FSICOST16-BP01 Use AWS cost management tools to perform retrospective, audit-based cost optimization on existing cloud workloads

There is a process to examine existing cloud spend, and identify cost optimization
opportunities using manual analysis, or the use of tools (AWS Billing and Cost Management and Cost Management and
Cost Management tools, AWS Partner tools, open-source tools, or DIY tools).

For generative AI workloads, this includes:

- Regular review of model selection and performance against cost
- Token usage optimization
- Vector store and embedding efficiency
- Knowledge base storage optimization
- Agent workflow cost analysis

Cost optimization opportunities are identified, prioritized, and implemented in a
continuous, programmatic manner, verifying that all cloud workloads run as lean as
possible while meeting all functional and non-functional requirements.

**Tools**

Extend cost management by introducing a standard KPI stack for generative AI
workloads, tracked using AWS CFM dashboards or custom Amazon CloudWatch metrics like:

- Cost per 1,000 tokens (input and output)
- Cost per successful user or agent task
- Cache hit percentage (RAG efficiency)
- Average context length and output token size
- Model tier mix ratio (percentage of bronze, silver, and gold routing)

These KPIs provide actionable visibility into generative AI spend patterns,
supporting data-driven optimizations across model selection, prompt engineering, and
caching strategy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost16.html*

---

# FSICOST17: Are you continually reviewing your workload to provide the most cost-effective resources?

There are multiple factors that affect the architecture, for example, new enhancements
related to business requirements, re-architecting your workload to improve efficiency, new
services released by AWS, price changes by AWS, or your team creating an MVP product
with services without considering costs. It is necessary to continually review the
architecture and resources used by your workload.

## FSICOST17-BP01 Assess workload architecture to identify the most cost-effective resources

There are multiple factors that affect the architecture, for example, new
enhancements related to business requirements, re-architecting your workload to improve
efficiency, new services released by AWS, price changes by AWS, or your team creating
an MVP product with services without considering costs. It is necessary to assess the
architecture and resources used by workload, for example, usage of serverless
technologies, managed services to reduce the operational overhead, or AWS Graviton-based
instances that meet your needs. Alternatively, you can refactor your monolithic
application to run as microservices. Most of the FSI systems are API-driven, so splitting
them across a number of diverse services helps procurement, and the right-sizing of
related resources.

**Review**

Continuously re-assess whether managed generative AI services (for example, Amazon
Bedrock or Amazon Q) or self-managed open-model stacks offer the best price-performance and
governance balance for your risk and compliance constraints.

For highly regulated workloads, periodically benchmark in-house fine-tuned models
against Bedrock-hosted foundation models to verify that the chosen deployment pattern
continues to meet cost, latency, and compliance requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost17.html*

---

# FSICOST18: Do you have specific workload modernization or refactoring goals in your cloud strategy?

In traditional financial institutions, databases and core banking solutions are key
cost drivers. Improve your total cost of ownership (TCO) by refactoring your lift and shift
strategies to continue your modernization activities where you can improve performance while
reducing your costs.

## FSICOST18-BP01 Define ambitious modernization strategy to become truly AWS optimized

In traditional financial institutions databases and core banking solutions are key
cost drivers. Improve your Total Cost of Ownership (TCO) by refactoring your lift and
shift strategies to continue your modernization activities where you can improve
performance while reducing your costs.

The Operational Excellence pillar helps you define which workloads are suitable for
refactoring. In the case of core banking systems provided by a vendor, start a dialog with
your vendor to build a roadmap for workload modernization to make them cost-efficient.
Also concentrate

on modernization of workloads that interact with databases and core banking systems
(for example, customer-facing web-pages, and apps). Leverage the AWS service WorkSpaces for
remote diagnostics.

**Modernize**

Replace brittle prompt chains with retrieval-augmented generation (RAG) and
tool-augmented agent frameworks where doing so reduces total cost per task and improves
maintainability.

Retire redundant or shadow knowledge bases accumulated across business units by
consolidating them under centralized governance, providing consistent cost control, data
lineage, and compliance.

Incorporate model lifecycle management into modernization plans. Deprecate outdated
fine-tuned models, transition low-ROI use cases to smaller model tiers, and adopt managed
generative AI orchestration (for example, Bedrock Agents) to reduce operational burden
over time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost18.html*

---

# FSICOST19: Do you use the cloud to drive innovation and operational excellence of your business model to impact both the top and bottom line?

Today, technology and digital solutions are an integral part of FSI operations, however
IT cost is not the biggest block within all expenditures in the profit and loss of FSI
customers (personnel and marketing have greater impacts on cost). Using AWS Cloud
solutions and services to change the way you operate impacts your profitability in the short
and long term.

## FSICOST19-BP01 Use AWS Cloud services to change the way you reduce cost and improve agility in your infrastructure

Today, technology and digital solutions are an integral part of FSI operations,
however IT cost is not the biggest block within all expenditures in the profit and loss of
FSI customers (personnel and marketing have greater impacts on cost). Using AWS cloud
solutions and services to change the way you operate impacts your profitability in the
short and long term. Think big and explore regularly with your AWS Account Management
team to test and launch new use cases and solutions. For example, you may boost your IT
teams' productivity by exploring Amazon Q Developer. With Intelligent Document Processing, you can
automatically process financial or insurance documents using AI and free up capacity on
your service teams.

**Business impact**

Tie generative AI costs directly to measurable business value, for example:

- Cost per reconciled contract
- Cost per KYC file processed
- Cost per approved credit decision
- Cost per customer query resolved through generative AI assistant

Track these KPIs alongside traditional FinOps metrics and prioritize initiatives that
improve the cost-to-value ratio over time. This enables leadership to fund generative AI
programs based on demonstrated ROI, not just innovation potential.

Establish a value per token dashboard that links foundation model spend to tangible
business outcomes (such as hours saved, throughput increased, or accuracy gains),
reinforcing a culture of accountable AI innovation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost19.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
