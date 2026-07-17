# Cost optimization

**Pages**: 11

---

# Cost-effective resources

COST 1: How do you optimize your costs?

Serverless architectures are easier to manage in terms of correct resource allocation. Due
to its pay-per-value pricing model and scale based on demand, serverless effectively reduces
the capacity planning effort.

As covered in the operational excellence and performance pillars, optimizing your
serverless application has a direct impact on the value it produces and its cost.

As Lambda proportionally allocates CPU, network, and storage IOPS based on memory, the
faster the initiation, the cheaper and more value your function produces due to 1-ms billing
incremental dimension.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/cost-effective-resources.html*

---

# Matching supply and demand

The AWS serverless architecture is designed to scale based on demand and as such there
are no applicable practices to be followed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/matching-supply-and-demand.html*

---

# Expenditure and usage awareness

As covered in the [AWS
Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), the increased flexibility and agility that the cloud
enables encourages innovation and fast-paced development and deployment. It eliminates the
manual processes and time associated with provisioning on-premises infrastructure, including
identifying hardware specifications, negotiating price quotations, managing purchase orders,
scheduling shipments, and then deploying the resources.

As your serverless architecture grows, the number of Lambda functions, APIs, stages, and
other assets will multiply. Most of these architectures need to be budgeted and forecasted in
terms of costs and resource management, so tagging can help you here. You can allocate costs
from your AWS bill to individual functions and APIs and obtain a granulated view of your
costs and usage per project in AWS Cost Explorer.

A good implementation is to share the same key-value tag for assets that belong to the
project programmatically, and create custom reports based on the tags that you have created.
This feature will help you not only allocate your costs, but also identify which resources
belong to which projects. To gain practical experience on this topic refer to the [Well Architected Labs](https://www.wellarchitectedlabs.com/). You can find many
cost optimization walkthroughs that include tagging as well.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/expenditure-and-usage-awareness.html*

---

# Lambda cost and performance optimization

With Lambda, there are no servers to manage, it scales automatically, and you only pay
for what you use. However, choosing the right memory size settings for a Lambda function is
still an important task. [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) supports Lambda functions and
uses machine-learning to provide memory size recommendations for Lambda functions.

This allows you to reduce costs and increase performance for your Lambda-based
serverless workloads.

These recommendations are available through the Compute Optimizer console, [AWS CLI](https://aws.amazon.com/cli/), [AWS SDK](https://aws.amazon.com/tools/), and the Lambda
console. Compute Optimizer continuously monitors Lambda functions, using historical performance metrics to
improve recommendations over time.

In addition, consider configuring new and existing functions to run on ARM or Graviton
processors. If your functions or dependencies do not require a given processor architecture
(x86, ARM), you might benefit in cost and performance by switching your functions
architecture. We always recommend load testing as results might vary for each use case,
dependency, and runtime. For example, you could create two [versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) of your function: one
for x86 and one for ARM. With the [Alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) feature, you could
distribute a percentage of your traffic to a different processor architecture, and use CloudWatch
Metrics to measure duration and latency efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/cost-and-performance-optimization.html*

---

# Logging ingestion and storage

AWS Lambda uses CloudWatch Logs to store the output of the executions to identify and troubleshoot
problems on executions as well as monitoring the serverless application. These will impact
the cost in the CloudWatch Logs service in two dimensions: ingestion and storage.

Set appropriate logging levels and remove unnecessary logging information to optimize
log ingestion. Use environment variables to control the application logging level and sample
logging in DEBUG mode to ensure you have additional insight when necessary.

Set log retention periods for new and existing CloudWatch Logs groups. For log archival, export
and set cost-effective storage classes that best suit your needs.

If you are using CloudWatch to record metrics in your Lambda Environment consider using the
CloudWatch Embedded Metric Format (EMF) instead of using the CloudWatch PutMetricData API.

EMF enables you to ingest complex high-cardinality application data in the form of logs
and easily generate actionable metrics from them. The embedded metric format is a JSON
specification used to instruct CloudWatch Logs to automatically extract metric values embedded in
structured log events.

In such high-cardinality environments you might observe cost savings by having your
Lambda functions leverage the CloudWatch Embedded Metric Format since with EMF you do not pay the
per request charge of the CloudWatch PutMetricData API. With EMF you are only charged for Data
Ingestion per GB, Data Archival per GB and per Custom Metric.

The metrics created with EMF are created asynchronously by the CloudWatch service. This means
that by using EMF when processing logs might also reduce the execution duration of your
Lambda functions compared to using the PutMetricData API which is a synchronous call.

If you need to have a precise timestamp for each individual metric or you have
dimensions with the same key but different values, at the time of writing you will need to
log separate EMF blobs. This means increased data ingestion and storage per GB CloudWatch cost.

In those cases we recommend to evaluate if the increased log ingestion and storage cost
of EMF will be more expensive versus the benefit of not paying for the per request charge of
the CloudWatch PutMetricData API. Moreover if you need high resolution metrics CloudWatch PutMetricData
API might be a better fit versus EMF.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/logging-ingestion-and-storage.html*

---

# Leverage VPC endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a
connection between your VPC and serverless services like AWS Lambda and AWS Step Functions. You can
use this connection to invoke your Serverless resources without crossing the public
internet.

To establish a private connection between your VPC and serverless resources, you can
create an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, which
enables you to privately access APIs without needing an internet gateway or NAT device
within your architecture.

Leveraging VPC endpoints will most likely contribute to cost savings if you are
leveraging NAT and Internet gateways for the sole purpose of accessing Serverless APIs from
AWS resources that do not have access to the internet. The cost optimisation is achieved
from the fact that interface endpoints are more cost effective VPC structures compared to
NAT and Internet gateways.

The example diagrams below show two different patterns of Lambda functions accessing the
Amazon SNS service. In the first diagram, there are two NAT Gateways in two AZs for high
availability and an Internet Gateway. In the second diagram, there are interface endpoints
in two AZs. The second pattern is more cost effective than the first one because interface
endpoints are more cost effective than using NAT and Internet Gateways combined.

*Figure 34: Lambda function accessing Amazon SNS via NAT and Internet
Gateways*

*Figure 35: Lambda function accessing Amazon SNS via interface
endpoints*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/leverage-vpc-endpoints.html*

---

# DynamoDB on-demand and provisioned capacity

Amazon DynamoDB is a fully managed NoSQL database service with single-digit millisecond
performance at any scale, and is often used for serverless applications. DynamoDB has two
pricing models for read and write throughput: on-demand mode and provisioned mode.

**On-demand mode**

DynamoDB on-demand mode is a serverless throughput option that simplifies database
management and automatically scales to support your most demanding applications. DynamoDB
on-demand lets you create a table without worrying about capacity planning, monitoring
usage, and configuring scaling policies. DynamoDB on-demand mode offers pay-per-request pricing
for read and write requests so that you only pay for what you use. For on-demand mode
tables, you don't need to specify how much read and write throughput you expect your
application to perform.

On-demand mode is the default and recommended throughput option for most DynamoDB
workloads. DynamoDB handles all aspects of throughput management and scaling to support
workloads that can start small and scale to millions of requests per second. You can read
and write to your DynamoDB tables as needed without managing throughput capacity on the table.
For more information, see [DynamoDB on-demand
capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html).

**Provisioned mode**

In provisioned mode, you must specify the number of reads and writes per second that you
require for your application. You'll be charged based on the hourly read and write capacity
you have provisioned, not how much of that provisioned capacity you actually consumed. This
helps you govern your DynamoDB use to stay at or below a defined request rate in order to
obtain cost predictability.

You can choose to use provisioned capacity if you have steady workloads with predictable
growth, and if you can reliably forecast capacity requirements for your application. For
more information, see [DynamoDB
provisioned capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/capacity.html*

---

# AWS Step Functions Express Workflows

When you are creating a workflow with AWS Step Functions you will be given two options for the
type of workflow that you want to create: Standard or Express.

Standard Workflows are ideal for long-running, durable, and auditable workflows.
Standard Workflows can support an execution start rate of over 2K executions per second.
They can run for up to a year and you can retrieve the full execution history using the
[Step Functions
API](https://docs.aws.amazon.com/step-functions/latest/apireference). Standard Workflows employ an exactly-once execution model, where your tasks
and states are never started more than once unless you have specified the **Retry** behavior in your state machine. This makes them suited to
orchestrating non-idempotent actions, such as starting an Amazon EMR cluster or processing
payments. Standard Workflow executions are billed according to the number of state
transitions processed.

Because the Standard Workflows pricing is based on state transitions, try to avoid the
pattern of managing an asynchronous job by using a polling loop and prefer instead to use
Callbacks or the .sync Service integration where possible. Using Callbacks or the .sync
Service integration will most likely reduce the number of state transitions and cost. With
the .sync Service integration in particular, you can have Step Functions wait for a request
to complete before progressing to the next state. This is applicable for integrated services
such as AWS Batch and Amazon ECS.

See diagrams below that describe each scenario:

*Figure 36: Job Poller*

*Figure 37: Wait for Callback*

For example, pausing the workflow until a callback is received from an external
service.

*Figure 38: Using the .sync Service Integration and waiting for a Fargate
task completion*

Express Workflows are ideal for high-volume, event-processing workloads such as IoT
data ingestion, streaming data processing and transformation, and mobile application
backends. Express Workflows can support an execution start rate of over 100K executions per
second. They can run for up to five minutes. Express Workflows can run either synchronously
or asynchronously and employ an at-most-once or at-least-once workflow execution model,
respectively. This means that there is a possibility that an execution might be run more
than once.

Ensure your Express Workflow state machine logic is idempotent and that it will not be
affected adversely by multiple concurrent executions of the same input.

Good examples of using Express Workflows is orchestrating idempotent actions, such as
transforming input data and storing with `PUT` in Amazon DynamoDB. Express Workflow
executions are billed by the number of executions, the duration of execution, and the memory
consumed. There are also cases where combining a Standard and an Express Workflow might
offer a good combination of cost optimization and functionality. An example of a combining
Standard and Express workflows is shown in the diagram below. More specifically, in the
diagram below, the **Approve Order Request** state might be
implemented by integrating with a service like Amazon SQS, and the workflow can be paused while
waiting for a manual approval. This type of state would be good fit for a Standard Workflow.
Whereas for the **Workflow to Update Backend Systems** state
implementation you can start an execution of an Express Workflow to handle backend updates.
Express Workflows can be fast and cost-effective for steps where checkpointing is not
required.

*Figure 39: Express and Standard Workflows combined*

In summary, deciding between Express and Standard Workflows largely depends your use
case. Consider using Express Workflows for a high throughput system, as Express Workflows
will probably be more cost-efficient compared to Standard Workflows for the same level of
throughput. In order to be able to determine which type of workflow is best for you,
consider the differences in execution semantics between Standard and Express Workflows on
top of cost.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/step-functions-workflows.html*

---

# Direct integrations

If your Lambda function is not performing custom logic while integrating with other AWS
services, chances are that it may be unnecessary. API Gateway, AWS AppSync, Step Functions, EventBridge, and Lambda
destinations can directly integrate with a number of services and provide you more value and
less operational overhead. Most public serverless applications provide an API with an
agnostic implementation of the contract provided, as described in [RESTful Microservices](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/restful-microservices.html). An example scenario where a direct integration is a better
fit is ingesting click stream data through a REST API.

*Figure 40: Sending data to Amazon S3 using Firehose*

In this scenario, API Gateway will execute a Lambda function that will simply ingest the
incoming record into Firehose, which subsequently batches records before storing into a S3
bucket. As no additional logic is necessary for this example, we can use an API Gateway service
proxy to directly integrate with Firehose.

*Figure 41: Reducing cost of sending data to Amazon S3 by implementing AWS
service proxy*

With this approach, we remove the cost of using Lambda and unnecessary invocations by
implementing the AWS Service Proxy within API Gateway. A tradeoff when using the AWS Service
Proxy is that a direct integration might introduce some extra complexity if multiple shards
are necessary to meet the ingestion rate. In addition in the case that you need to transform
the messages being sent to Firehose from API Gateway you will need to use [mapping
templates](https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html) at the API Gateway layer. Adding mapping templates might introduce extra
complexity on the debugging and testing side versus using a Lambda function instead. If
latency-sensitive, you can stream data directly to your Firehose by having the correct
credentials at the expense of abstraction, contract, and API features.

*Figure 42: Reducing cost of sending data to Amazon S3 by streaming directly
using the Firehose SDK*

For scenarios where you need to connect with internal resources within your VPC or
on-premises and no custom logic is required, use API Gateway private integration.

*Figure 43: Amazon API Gateway private integration over Lambda in VPC to access
private resources*

With this approach, API Gateway sends each incoming request to an Elastic Load Balancer that
you own in your VPC, which can forward the traffic to any backend, either in the same VPC or
on-premises through an IP address. For REST APIs, Network Load Balancer is supported as a
private integration. For HTTP APIs, both Application Load Balancer and Network Load Balancer are supported. This
approach has both cost and performance benefits as you don’t need an additional hop to send
requests to a private backend with the added benefits of authorization, throttling, and
caching mechanisms. Another scenario is a fan-out pattern where Amazon SNS broadcasts messages to
all of its subscribers. This approach requires additional application logic to filter and
avoid an unnecessary Lambda invocation.

*Figure 44: Amazon SNS without message attribute filtering*

Amazon SNS can filter events based on message attributes and more efficiently deliver the
message to the correct subscriber.

*Figure 45: Amazon SNS with message attribute filtering*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/direct-integrations.html*

---

# Code optimization

As covered in the performance pillar, optimizing your serverless application can
effectively improve the value it produces per execution.

The use of global variables to maintain connections to your data stores or other
services and resources will increase performance and reduce execution time, which also
reduces the cost. Moreover consider connection pooling with [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) for your Lambda functions that interact using SQL
calls with your relational database instance. Please refer to the documentation for the
database engines that are supported and also find more information, at the Serverless
performance pillar section.

An example where the use of managed service features can improve the value per
execution is retrieving and filtering objects from Amazon S3, since fetching large objects from
Amazon S3 requires higher memory for Lambda functions.

*Figure 46: Lambda function retrieving full S3 object*

The previous diagram shows that when retrieving large objects from Amazon S3, we might
increase the memory consumption of the Lambda, increase the execution (so the function can
transform, iterate, or collect required data) and, in some cases, only part of this
information is needed.

This is represented with three columns in red (data not required) and one column in
green (data required). Using Athena SQL queries to gather granular information needed for
your execution reduces the retrieval time and object size upon which to perform
transformations.

*Figure 47: Lambda with Athena object retrieval*

The next diagram shows that by querying Athena to get the specific data, we reduce the
size of the object retrieved and, as an extra benefit, we can reuse that content since Athena
saves its query results in an S3 bucket and invokes the Lambda invocation as the results land
in Amazon S3 asynchronously.

A similar approach could be using S3 Select, which enables applications to retrieve
only a subset of data from an object by using simple SQL expressions. As in the previous
example with Athena, retrieving a smaller object from Amazon S3 reduces execution time and the
memory used by the Lambda function.

*Table: Lambda performance statistics using Amazon S3 vs S3 Select*

*200 seconds*

*95 seconds*

```
`# Download and process all keys

for key in src_keys:

response = s3_client.get_object(Bucket=src_bucket, Key=key)

contents = response['Body'].read()

**for line in contents.split('\n')[:-1]:**

line_count +=1

try:
**data = line.split(',')**
**srcIp = data[0][:8]**

…`
```

```
`# Select IP Address and Keys

for key in src_keys:

response = s3_client.select_object_content

(Bucket=src_bucket, Key=key, expression =

**SELECT SUBSTR(obj._1, 1, 8), obj._2 FROM
s3object as obj)**

contents = response['Body'].read()

for line in contents:

line_count +=1

try:

…`
```

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/code-optimization.html*

---

# Resources

Refer to the following resources to learn more about our best practices for cost
optimization.

## Documentation and blogs

- [CloudWatch Logs
Retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SettingLogRetention.html)
- [Exporting CloudWatch Logs to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3ExportTasksConsole.html)
- [Streaming
CloudWatch Logs to OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_ES_Stream.html)
- [Defining wait
states in Step Functions state machines](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html)
- [Coca-Cola Vending
Pass State Machine Powered by Step Functions](https://aws.amazon.com/blogs/aws/things-go-better-with-step-functions/)
- [Building high throughput genomics batch workflows on AWS](https://aws.amazon.com/blogs/compute/building-high-throughput-genomics-batch-workflows-on-aws-workflow-layer-part-4-of-4/)
- [Simplify
your Pub/Sub Messaging with Amazon SNS Message Filtering](https://aws.amazon.com/blogs/compute/simplify-pubsub-messaging-with-amazon-sns-message-filtering/)
- [S3 Select and Glacier Select](https://aws.amazon.com/blogs/aws/s3-glacier-select/)
- [Lambda Reference
Architecture for MapReduce](https://github.com/awslabs/lambda-refarch-mapreduce)
- [Serverless Application Repository App – Auto-set CloudWatch Logs group retention](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:374852340823:applications~auto-set-log-group-retention)
- [Ten resources every Serverless Architect should know](https://aws.amazon.com/blogs/architecture/ten-things-serverless-architects-should-know/)

## Whitepapers

- [Optimizing Enterprise Economics with Serverless Architectures](https://docs.aws.amazon.com/whitepapers/latest/optimizing-enterprise-economics-with-serverless/optimizing-enterprise-economics-with-serverless.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/resources-4.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
