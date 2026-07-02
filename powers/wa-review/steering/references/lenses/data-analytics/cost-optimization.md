# Cost optimization

**Pages**: 11

---

## 11 – Choose cost-effective compute and storage solutions based on workload usage patterns

# Best practice 11.1 – Decouple storage from compute

It’s common for data assets to grow exponentially year over
year. However, your compute needs might not grow at the same
rate. Decoupling storage from compute allows you to manage
the cost of storage and compute separately, and implement
different cost optimization features to minimize cost.

## Suggestion 11.1.1 – Use services that decouple compute from storage

Services that allow independent scaling of storage and compute allow for greater flexibility when handling workloads. This means when your workload is compute intensive you do not need to deploy a large storage array to meet the compute power for running your workload.

## Suggestion 11.1.2 – Use Amazon Redshift RA3 instances types

Amazon Redshift RA3 instance types support the ability to
decouple the compute and storage. This allows your Amazon Redshift storage to scale independently from your compute
resources, which improves cost efficiencies for your data
warehousing workloads.

## Suggestion 11.1.3 – Use a decoupled ﬁle system for Big Data workloads

The EMR file system (EMRFS) is an implementation of HDFS
that all Amazon EMR clusters use for reading and writing
regular files from Amazon EMR directly to Amazon S3. By
using EMRFS, your organization is only charged for the
storage used, rather than paying for overprovisioned and
underutilized HDFS EBS storage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-11.1---decouple-storage-from-compute..html*

---

# Best practice 11.2 – Plan and provision capacity for predictable workload usage

For well-defined workloads, planning capacity ahead based on
average usage pattern helps improve resource utilization and
avoid over provisioning. For a spiky workload, set up
automatic scaling to meet user and workload demand.

## Suggestion 11.2.1 – Choose the right instance type based on workload pattern and growth ratio

Consider resource needs, such as CPU, memory, and
networking that meet the performance requirements of your
workload. Choose the right instance type and avoid
overprovisioning. An optimized EC2 instance runs your
workloads with optimal performance and infrastructure
cost. For example, choose the smaller instance if your
growth ratio is low as this allows more granular
incremental change.

## Suggestion 11.2.2 – Choose the right sizing based on average or medium workload usage

Right sizing is the process of matching instance types and
sizes to your workload performance and capacity
requirements at the lowest possible cost. It’s also the
process of looking at deployed instances and identifying
opportunities to downsize without compromising capacity or
other requirements that will result in lower costs.

## Suggestion 11.2.3 – Use automatic scaling capability to meet the peak demand instead of over provisioning

Analytics services can scale dynamically to meet demand. Then, after the demand has dropped below a certain threshold, the service will remove the resources that are no longer needed. The automatic scaling of serverless services enables applications to handle sudden traffic spikes without capacity planning, reducing costs and improving availability.

There are a number of services that can automatically scale, and other services that you need to configure the scaling for. For example, AWS services like Amazon EMR, AWS Glue, and Amazon Kinesis can auto-scale seamlessly in response to usage spikes and remove resources without any configuration.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-11.2---plan-and-provision-capacity-for-predictable-workload-usage..html*

---

# Best practice 11.3 – Use on-demand instances or serverless capacity for unpredictable workload usage

Serverless services typically only charge for the compute used, or the use of other measures like data processed, but only when there is a workload actively using the service. In contrast, allocating infrastructure yourself often means paying for idle resources.

## Suggestion 11.3.1 – Use Amazon Athena for ad hoc SQL workloads

Amazon Athena is a serverless query service that makes it
easy to analyze data directly in Amazon S3 using standard
SQL. With Amazon Athena, you only pay for the queries that
you run. You are charged based on the amount of data
scanned per query.

## Suggestion 11.3.2 – Use AWS Glue or Amazon EMR Serverless instead of Amazon EMR on EC2 for infrequent ETL jobs

AWS Glue is a fully managed ETL (extract, transform, and
load) service that makes it simple and cost-effective to
categorize your data, clean it, enrich it, and move it
reliably between various data stores and data streams.
With AWS Glue jobs, you pay only for the resources used
during the ETL process. In contrast, Amazon EMR on EC2 is
typically used for frequently running jobs requiring
semipersistent data storage.

Amazon EMR Serverless provides a highly cost-effective way to run EMR clusters and data pipelines on an infrequent or intermittent basis. Unlike provisioned clusters that incur hourly charges even when idle, Serverless allows you to spin up a cluster on-demand when a job is submitted, and tear it down automatically once the job completes. This means you only pay for the actual time the cluster is running to process your workload, optimizing costs for infrequent ETL, data processing, or when-necessary analysis jobs.

## Suggestion 11.3.3 – Use serverless resources for unpredictable or spiky workloads

Use serverless analytics services, such as Amazon Redshift Serverless, Amazon EMR, Amazon Athena, Amazon Quick Serverless, and Amazon Managed Streaming for Apache Kafka (Amazon MSK) Serverless, to perform analytical queries, processing and streaming, with pay-as-you-go pricing. This helps remove the cost associated with idle resources.

You can also use serverless resources for development and testing needs.

For more details, see [AWS serverless data analytics pipeline reference architecture](https://aws.amazon.com/blogs/big-data/aws-serverless-data-analytics-pipeline-reference-architecture/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-11.3---use-on-demand-instance-capacity-for-unpredictable-workload-usage..html*

---

## 12 – Build financial accountability models for data and workload usage

# Best practice 12.1 – Measure data storage and processing costs per user of the workload

Data analytics workloads have recurring stable costs and
per-use costs, for example, a weekly reporting job with
relatively static data storage fees or periodic
unpredictable processing runtime fees. Your organization
should establish a financial attribution mechanism that
captures data storage and workload usage when analytics
systems are run. Using this approach, your end users
(business unit, team, or individual) can be notified of their
consumption at regular intervals.

## Suggestion 12.1.1 – Use tagging or other attribution methods to identify workload and data storage ownership

Collaboration between business, IT, and finance team to
agree on cost allocation, cost ownership, cost charging,
and budget management. Create budget tracking policy for
storage and workload using tagging. Agree on the
governance approach to implement policy (that is, central
and decentralize), billing allocation, charge back, and
budget reporting.

For more details, refer to the following information:

- AWS Cloud Financial Management Blog: Cost
[Tagging
and Reporting with AWS Organizations](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/)
- AWS Billing and Cost Management and Cost Management User Guide:
[Reporting
your budget metrics with budget reports](https://docs.aws.amazon.com/cost-management/latest/userguide/reporting-cost-budget.html),
[Configuring
AWS Budgets actions](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-controls.html) and
[Creating
an Amazon SNS topic for budget notifications](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-sns-policy.html)

## Suggestion 12.1.2 – Implement cost-visibility and internal bill-back method to aggregate your teams' use of analytics resources

Notify teams of their analytics usage costs periodically. Build dashboards that provide teams visibility into how their work impacts costs to the business using a self-service approach.

You can view and optimize your costs through the AWS Cost and Usage Report and the Cost and Usage Dashboards Operations Solution (CUDOS) reports.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-12.1---measure-data-storage-and-processing-costs-per-user-of-the-workload..html*

---

# Best practice 12.2 – Build local or build centralized data analytics platforms

Teams can establish their own data analytics resources that support their analytical needs locally, rather than extracting information and transferring it to a central location. Decide when teams benefit from building local analytics resources, balancing required agility and team skillset with the need for a centralized analytics platform.

## Suggestion 12.2.1 – Perform regular reviews of analytics operations to determine if the business can benefit from teams managing their own infrastructure

Teams may prefer to own and manage their own infrastructure, as this allows for more flexibility and agility in system design with fewer dependencies. Individual ownership also provides clear cost visibility. In other cases, a shared processing system can be more efficient, where teams send data requests to a central provider. Tracking request volume by team enables cost attribution. A centralized team managing infrastructure benefits multiple groups through increased resource utilization and concentrated expertise. Centralized data repositories make enriching data simpler and provide a single access point. Organizations find centralized analytics helps meet compliance and governance needs.

In summary, there are trade-offs between decentralized team-owned infrastructure providing more flexibility compared to centralized shared infrastructure increasing utilization and governance. Teams and centralized providers can also coordinate, with centralized systems handling some processing and team systems providing customization. The best approach depends on the specific organizational needs and structure.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-12.2-build-local-or-centralized-data-analytics-platforms.html*

---

# Best practice 12.3 – Restrict and record resource allocation permissions using AWS Identity and Access Management (IAM)

To better control costs, create distinct IAM roles that authorize users to provision certain resources. This ensures that only permitted individuals can provision the resources they are allowed to, preventing unauthorized and unnecessary spending.

## Suggestion 12.3.1 – Create a cost governance framework that uses specialized IAM roles, rather than individual users, to provision costly infrastructure

Restrict the authorization to launch costly resources to
specific IAM roles. For example, certain instances types
can only be provisioned by certain teams to reduce
unnecessary expenditure.

## Suggestion 12.3.2 – Track AWS CloudTrail logs to determine overall usage-per-user and role

Track the usage across users and roles to get a clear understanding of resource
usage. As part of your cost-allocation governance, automatically process the AWS CloudTrail logs so
that cost allocation is properly attributed to the relevant department.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-12.3---restrict-and-record-resource-allocation-permissions-using-aws-identity-and-access-management-iam..html*

---

## 13 – Manage cost over time

# Best practice 13.1 – Remove unused data and infrastructure

Delete data that is out of its retention period, or not
needed anymore. Delete intermediate-processed data that can
be removed without business impacts. If the output of
analytics jobs is not used by anyone, consider removing such
jobs so that you don't waste resources.

## Suggestion 13.1.1 – Track data freshness

In many cases, maintaining a metadata repository for
tracking data movement will be worthwhile. This is not
only to instill confidence in the quality of the data, but
also to identify infrequently updated data, and unused
data.

## Suggestion 13.1.2 – Delete data that is out of its retention period

Data that is past its retention period should be deleted
to reduce unnecessary storage costs. Identify data through
the metadata catalog that is outside its retention period.
To reduce human effort, automate the data removal process.
If data is stored in Amazon S3, use Amazon S3 Lifecycle
configurations to expire data automatically.

## Suggestion 13.1.3 – Delete intermediate-processed data that can be removed without business impacts

Many steps in analytics processes create intermediate or
temporary datasets. Ensure that intermediate datasets are
removed if they have no further business value.

## Suggestion 13.1.4 – Remove unused analytics jobs that consume infrastructure resources but no one uses the job results

Periodically review the ownership, source, and downstream
consumers of all analytics infrastructure resources. If
downstream consumers no longer need the analytics job,
stop the job from running and remove unneeded resources.

## Suggestion 13.1.5 – Use the lowest acceptable frequency for data processing

Data processing requirements must be considered in the business context. There is no value in processing data faster than it is consumed or delivered. For example, in a sales analytics workload, it might not be necessary to perform analytics on each transaction as it arrives. In some cases, only hourly reports are needed by business management. Batch processing the transactions is more eﬃcient and can reduce unnecessary infrastructure costs between batch processing jobs.

## Suggestion 13.1.6 – Compress data to reduce cost

Data compression can significantly reduce storage and query costs. Columnar data formats like Apache Parquet stores data in columns rather than rows, allowing similar data to be stored contiguously. Using Parquet over CSV format can reduce storage costs significantly. Since services like Amazon Redshift Spectrum and Amazon Athena charge for bytes scanned, compressing data lowers the overall cost of using those services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-13.1-remove-unused-data-and-infrastructure..html*

---

# Best practice 13.2 – Continuously evaluate your provisioned resources and identify overprovisioned workloads

Workload resource utilization can change over time,
especially with the growth of data or after process
optimization has occurred. Your organization should review
resource usage patterns and determine if you require the
same infrastructure footprint to meet your business goals.

## Suggestion 13.2.1 – Evaluate whether compute resources can be downsized

Investigate your resource utilization by inspecting the
metrics provided by Amazon CloudWatch. Evaluate whether
the resources can be downsized to one-level smaller within
the same instance class. For example, reduce Amazon EMR
cluster nodes from m5.16xlarge to m5.12xlarge, or the
number of instances that make up the cluster.

## Suggestion 13.2.2 – Move infrequently used data out of a data warehouse into a data lake

Data that is infrequently used can be moved from the data
warehouse into the data lake. From there, the data can be
queried in place or joined with data in the warehouse. Use
services such as Amazon Redshift Spectrum to query and
join data in the Amazon S3 data lake, or Amazon Athena to
query data at rest in Amazon S3.

## Suggestion 13.2.3 – Merge low utilization infrastructure resources

If you have several workloads that all have
low-utilization resources, determine if you can combine
those workloads to run on shared infrastructure. In many
cases, using a pooled resource model for analytics
workloads will save on infrastructure costs.

## Suggestion 13.2.4 – Move infrequently accessed data into low-cost storage tiers

When designing a data lake or data analytics project,
consider required access patterns, transaction
concurrency, and acceptable transaction latency. These
will inﬂuence where data is stored. It is equally
important to consider how often data will be accessed.
Have a data lifecycle plan to migrate data tiers from
hotter storage to colder, less-expensive storage, while
still meeting all business objectives.

Transitioning between storage tiers is achieved using
Amazon S3 Lifecycle policies. These automatically
transition objects into another tier with lower cost, and
will even delete expired data. Amazon S3
Intelligent-Tiering will analyze the data access patterns
and automatically move objects between tiers.

## Suggestion 13.2.5 – Move to serverless when you don't need always-on infrastructure

For analytics workloads that have intermittent or unpredictable usage patterns, moving to AWS serverless can provide significant cost savings compared to provisioned servers. AWS serverless analytics services like Amazon Athena, EMR Serverless, and Amazon Redshift Serverless are great options that provide on-demand access without having to provision always-on resources. These services automatically start up when needed and shut down when not in use so you don't have to pay for idle capacity.

For example, with Amazon Redshift Serverless, you pay for compute only when the data warehouse is in use. By using Amazon Redshift Serverless for tasks such as loading data and leveraging Amazon Redshift data sharing, you can scale down your main cluster and still maintain the same performance for end users.

For more detail, refer to the following:

- [Easy analytics and cost optimization with Amazon Redshift Serverless](https://aws.amazon.com/blogs/big-data/easy-analytics-and-cost-optimization-with-amazon-redshift-serverless/)
- [Amazon EMR Serverless cost estimator](https://aws.amazon.com/blogs/big-data/amazon-emr-serverless-cost-estimator/)
- [Run queries 3x faster with up to 70% cost savings on the latest Amazon Athena engine](https://aws.amazon.com/blogs/big-data/run-queries-3x-faster-with-up-to-70-cost-savings-on-the-latest-amazon-athena-engine/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-13.2---reduce-overprovisioning-infrastructure..html*

---

# Best practice 13.3 – Evaluate and adopt new cost-effective solutions

As AWS releases new services and features, it’s a best
practice to review your existing architectural decisions to
ensure that they remain cost effective. If a new or updated
service can support the same workload but in a much cheaper
way, consider implementing the change to reduce cost.

## Suggestion 13.3.1 – Set Service Quotas to control resource usage

Some AWS services allow setting Service Quotas per
account. Service Quotas should be established to prevent
runaway infrastructure deployment by accident. Ensure that
Service Quotas are set high enough to cover the expected
peak usage.

## Suggestion 13.3.2 – Pause and resume resources if the workload is not always required

Use automation to pause and resume resources when the
resource is unneeded. For example, stop development and
test Amazon RDS instances that are not used after working
hours.

## Suggestion 13.3.3 – Switch to a new service or take advantage of new features that can reduce cost

AWS consistently adds new capabilities to enable your
organization to leverage the latest technologies to
experiment and innovate more quickly. Your organization
should review new service releases frequently to
understand the price and performance, and determine if
such features can improve cost reduction.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-13.3---evaluate-and-adopt-new-cost-effective-solutions..html*

---

## 14 – Use optimal pricing models based on infrastructure usage patterns

# Best practice 14.1 – Evaluate the infrastructure usage patterns and choose your payment options accordingly

On-demand resources provide immense ﬂexibility with
pay-as-you-go payment models across multiple scenarios and
scales. Alternately, Reserved Instances provide significant
cost saving for workloads that have steady resource
utilization and serverless options for unpredictable demand. Perform regular workload resource usage
analysis. Choose the best pricing model to ensure that you
don’t miss cost optimization opportunities and maximize your
discounts.

## Suggestion 14.1.1 – Evaluate available payment options of the infrastructure resources of your choice

Review the pricing page for specific AWS services. Each
service will list the billing metrics, such as runtime or
gigabytes processed, as well as any discount options for
dedicated usage. In addition, many AWS analytics services
offer discounted payment terms, Reserved Instances, or
Savings Plans, in exchange for a specific usage commitment.
Almost all AWS services offer the payment for usage on
demand, meaning you only pay for what you use.

## Suggestion 14.1.2 – For steady, permanent workloads, obtain Reserved Instances or Savings Plans price discounts instead of paying On-Demand Instance pricing

Reserved Instances give you the option to reserve some AWS
resources for a one- or a three-year term. In turn, you
will receive a significant discount compared with the
On-Demand Instance pricing. Workloads that have consistent
long-term usage are good candidates for the Reserved
Instance payment option.

## Suggestion 14.1.3 – Use either on-demand, spot or serverless resources during development and in pre-production environments

Development and pre-production environments frequently change and often do not require 100% availability. Use on-demand instances with start and stop resources, or serverless resources in cases where workload utilization is unpredictable, frequently changes, or is only used for portions of the day. You can use spot instances for fault-tolerant and flexible big data analytics applications. Spot instances are available at up to a 90% discount compared to on-demand prices. Spot instances are not suitable for workloads that are inflexible, stateful, fault-intolerant, or tightly coupled between instance nodes.

For more detail, refer to the following:

- [Optimize Cost by Automating the Start or Stop of Resources in Non-Production Environments Spot Instance Best Practices](https://aws.amazon.com/blogs/architecture/optimize-cost-by-automating-the-start-stop-of-resources-in-non-production-environments/)
- [Optimizing Amazon EC2 Spot Instances with Spot Placement Scores](https://aws.amazon.com/blogs/compute/optimizing-amazon-ec2-spot-instances-with-spot-placement-scores/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-14.1---evaluate-the-infrastructure-usage-patterns-and-choose-your-payment-options-accordingly..html*

---

# Best practice 14.2 – Consult with your finance team and determine optimal payment models

If you use reserved-capacity pricing options, you can reduce
the infrastructure cost without modifying your workload
architectures. Collaborate with your finance team on the
planning and use of purchase discounts.

Make informed decisions regarding various cost factors.
These include the amount of capacity to reserve, the reserve
term length, and the choice of upfront payments for their
corresponding discount rates. The finance team should assist
your team in determining the best long-term and
reserved-capacity pricing options. This is because these
options affect your IT budget plans, such as which month is
the right moment to pay an upfront charge.

## Suggestion 14.2.1 – Consolidate the infrastructure usage to maximize the coverage of reserved capacity price options

Reserved Instances and Savings Plan purchases apply
automatically to the resources that will receive the
largest discount benefit. To maximize your discount
utilization, consolidate resources in accounts within an
AWS Organization structure. Allow the purchase commitments
to apply to other AWS accounts within your organization if
they are unused in the account for which they are
purchased.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-14.2---consult-with-your-finance-team-and-determine-optimal-payment-models..html*

---
