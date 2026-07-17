# Performance efficiency

**Pages**: 11

---

# Amazon API Gateway

To build RESTful APIs, use REST APIs from Amazon API Gateway. REST APIs are intended for APIs that
require API proxy functionality and API management features in a single solution.

Amazon API Gateway Edge-optimized APIs provide a fully managed Amazon CloudFront distribution to optimize
access for geographically dispersed consumers. API requests are routed to the nearest CloudFront
Point of Presence (POP), which typically improves connection time.

*Figure 22: Edge-optimized API Gateway deployment*

The API Gateway Regional endpoint doesn’t provide a CloudFront distribution, and enables HTTP2 by
default, which helps reduce overall latency when requests originate from the same Region.
Regional endpoints also allow you to associate your own Amazon CloudFront distribution or an existing
CDN.

*Figure 23: Regional Endpoint API Gateway deployment*

This table can help you decide whether to deploy an Edge-optimized API or Regional API
Endpoint:

**Edge-optimized API**

**Regional API Endpoint**

API is accessed across Regions. Includes API Gateway-managed CloudFront distribution.
X

API is accessed within same Region. Least request latency when API is accessed
from the same Region as API is deployed.

X

Ability to associate own CloudFront distribution.

X

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/amazon-api-gateway.html*

---

# AWS Lambda

Provisioned concurrency initializes a requested number of execution environments so that
they are prepared to respond immediately to your function's invocations. To enable your
function to scale without fluctuations in latency, use provisioned concurrency. By
allocating provisioned concurrency before an increase in invocations, you can ensure that
all requests are served by initialized instances with very low latency. AWS Lambda also
integrates with [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/). You can
configure Application Auto Scaling to manage provisioned concurrency on a schedule or based
on utilization. Use scheduled scaling to increase provisioned concurrency in anticipation of
peak traffic.

*Figure 24: Provisioned concurrency initializes a requested number of
execution environments to respond immediately to function's
invocations*

To optimize latency, you can customize the initialization behavior for functions that use
provisioned concurrency. You can run initialization code for provisioned concurrency
instances without impacting latency, because the initialization code runs at allocation
time. Configure Amazon VPC access to your Lambda functions only when necessary. Set up a NAT
gateway if your VPC-enabled Lambda function needs access to the Internet. Be sure to check
both the Security Group and network Access Control List (ACL) to allow outbound requests
from your Lambda function. As covered in the AWS Well-Architected Framework, configure your
NAT gateway, or NAT instances across multiple Availability Zones for high availability and
performance. This decision tree can help you decide when to deploy your Lambda function in a
VPC.

*Figure 25: Decision tree for deploying a AWS Lambda function in an
Amazon VPC*

For Lambda functions in VPC, avoid DNS resolution of public host names for underlying
resources in your VPC. For example, if your Lambda function accesses an Amazon RDS DB instance in
your VPC, launch the instance with the no-publicly-accessible option.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/aws-lambda.html*

---

# AWS Step Functions

AWS Step Functions offers both Standard or Express Workflow types. Standard Workflows are ideal
for long-running, durable, and auditable workflows. Express Workflows are ideal for
high-volume, event-processing workloads such as IoT data ingestion, streaming data
processing and transformation, and mobile application backends. A Standard Workflow has a
maximum duration of 1 year, compared to 5 minutes for an Express Workflow. Both Standard and
Express Workflows support execution history logging to Amazon CloudWatch Logs. Publishing logs doesn't
block or slow down executions, allowing you to select the log level required for the
workflow. When inspecting a workflow consider using [Amazon CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to
interactively search and analyze your workflow log data. Using the [GetExecutionHistory](https://docs.aws.amazon.com/step-functions/latest/apireference/API_GetExecutionHistory.html) API to explore the execution history for Standard Workflows
may save you from writing code. AWS Step Functions state transitions are throttled using a token
bucket scheme. Estimate the state transitions expected and match to quotas for bucket size
and refill rates. Trade off between Standard Workflow with throttling, or Express Workflow
with unlimited bucket size and refill rate.

An Express Workflow can start either synchronously or asynchronously. Select a synchronous
invocation when you can wait for the result and prefer to develop applications without the
need to develop additional code to handle errors, retries, or execute parallel tasks.
Synchronous Express execution API calls do not contribute to the existing account capacity
limits. Step Functions will provide capacity on demand and will automatically scale with
sustained workloads. Surges in workloads may be throttled until capacity is available. A
Synchronous Express Workflow can be invoked from Amazon API Gateway, AWS Lambda, or by using the
[StartSyncExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html) API call.

Invoke an Asynchronous Express Workflow if you don’t require an immediate response
output such as messaging services, or data processing that other services don’t depend on.
An Asynchronous Express Workflow returns a confirmation the workflow has started, and you
poll Amazon CloudWatch Logs for the result. An Asynchronous Express Workflow can be started in response
to an event, by a nested workflow in Step Functions, or by using the [StartExecution](https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html) API call.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/aws-step-functions.html*

---

# Amazon API Gateway

Amazon API Gateway and
AWS AppSync caching can be enabled to improve performance for applicable operations. DAX can
improve read responses significantly as well as Global and Local Secondary Indexes to prevent
DynamoDB full table scan operations. These details and resources were described in the Mobile
Backend scenario.

API Gateway content encoding allows API clients to request the payload to be compressed
before being sent back in the response to an API request. This reduces the number of bytes
that are sent from API Gateway to API clients and decreases the time it takes to transfer the
data. You can enable content encoding in the API definition, and you can also set the
minimum response size that triggers compression. By default, APIs do not have content
encoding support enabled.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/amazon-api-gateway-2.html*

---

# AWS Lambda

Set your AWS Lambda function timeout a few seconds higher than the
average execution to account for any transient issues in downstream services used in the
communication path. This also applies when working with Step Functions activities, tasks, and
Amazon SQS message visibility. Choosing a default memory setting and timeout in AWS Lambda may have an
undesired effect in performance, cost, and operational procedures.

Setting the timeout much higher than the average execution may cause functions to
execute for longer upon code malfunction, resulting in higher costs and possibly reaching
concurrency limits depending on how such functions are invoked. Setting a timeout that
equals one successful function execution may trigger a serverless application to abruptly
halt an execution if a transient networking issue or abnormality in downstream services
occur. Setting a timeout without performing load testing and, more importantly, without
considering upstream services, may result in errors whenever any part reaches its timeout
first.

Follow [best
practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html) for working with Lambda functions such as container reuse, minimizing
deployment package size to its runtime necessities, and minimizing the complexity of your
dependencies including frameworks that may not be optimized for fast startup. The latency
99th percentile (P99) should always be taken into account, as one may not impact the
application SLA agreed to with other teams.

AWS Lambda Extensions count towards the deployment package size limit of your function.
They also can impact the performance of your function because they share function resources
such as CPU, memory, and storage. Account for the additional resources used when adding
Lambda extensions through [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) or [functions deployed as container images](https://aws.amazon.com/blogs/compute/working-with-lambda-layers-and-extensions-in-container-images/). If your extension performs
compute-intensive operations, you may see your function's execution duration
increase.

Serverless applications may begin modeling monolithic applications, represented by a
single AWS Lambda function performing multiple tasks. Serverless applications may adopt this
monolithic approach as an easier way to get started, or developers may follow existing
development practices and paradigms, or simple applications may grow more complex over time.
As you optimize your serverless application, this monolithic approach may be less performant
due to the bundle of dependencies for everything that is not used on every execution path.
Consider breaking down your serverless application into microservices and remove unused
dependencies from these discrete functions. You will also gain performance in adapting new
features and opting for code optimized for the function use-case or integration.

Take advantage of Amazon API Gateway native routing functionality instead of using the routing of
web frameworks, which are well suited for web servers. Web frameworks inside the Lambda
function increases the size of the deployment package.

*Figure 26: Amazon API Gateway simplified routing architecture*

After a Lambda function has executed, AWS Lambda maintains the execution context for some
arbitrary time in anticipation of another Lambda function invocation. That allows you to use
the global scope for one-off expensive operations, for example establishing a database
connection or any initialization logic. In subsequent invocations, you can verify whether it’s
still valid and reuse the existing connection.

Consider connection pooling with [Amazon RDS
Proxy](https://aws.amazon.com/rds/proxy/) for your Lambda functions that interact using SQL calls with your database
instance. Amazon RDS Proxy handles the connection pooling necessary for scaling simultaneous
connections created by concurrent AWS Lambda functions. This allows for reuse of existing
connections, rather than creating new connections for every function invocation.

*Figure 27: Amazon RDS Proxy allows you to efficiently scale to many more
connections from your serverless application*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/aws-lambda-2.html*

---

# AWS Step Functions

AWS Step Functions monitor the Amazon CloudWatch metric [ExecutionThrottled](https://docs.aws.amazon.com/step-functions/latest/dg/procedure-cw-metrics.html#cloudwatch-step-functions-execution-metrics) which reports throttling on state transition, the number of
`StateEntered` events, and retries that have been throttled. Use this metric to
determine if a quota increase for a Standard Workflow is required.

If an Express Workflow execution runs for more than the 5-minute maximum, it will fail
with a `States.Timeout` error and emit a `ExecutionsTimedOut` CloudWatch
metric. Make use of [timeouts](https://docs.aws.amazon.com/step-functions/latest/dg/sfn-stuck-execution.html) in your task to
avoid an execution stuck waiting for a response. Specify a reasonable
`TimeoutSeconds` when you create the task. If you are receiving `States.Timeout`
errors, consider breaking the workflow into multiple workflow executions, revising your task
code or creating a Standard Workflow.

## Asynchronous Transactions

Because your customers expect more modern and interactive user
interfaces, you can no longer sustain complex workflows using synchronous transactions. The
more service interaction you need, the more you end up chaining calls that may end up
increasing the risk on service stability as well as response time.

Modern UI frameworks, such
as Angular.js, VueJS, and React, asynchronous transactions, and cloud native workflows provide
a sustainable approach to meet customer demand, as well as helping you decouple components and
focus on process and business domains instead.

These asynchronous transactions (or often times
described as an event-driven architecture) kick off downstream subsequent choreographed events
in the cloud instead of constraining clients to lock-and-wait (I/O blocking) for a response.
Asynchronous workflows handle a variety of use cases including, but not limited to: data
Ingestion, ETL operations, and order or request fulfillment.

In these use-cases, data is
processed as it arrives, and is retrieved as it changes. We outline best practices for two
common asynchronous workflows where you can learn a few optimization patterns for integration
and async processing.

## Serverless Data Processing

In a serverless data processing workflow, data is ingested from
clients into Kinesis (using the Kinesis agent, SDK, or API), and arrives in Amazon S3.

New objects kick
off a Lambda function that is automatically executed. This function is commonly used to
transform or partition data for further processing and possibly stored in other destinations
such as DynamoDB, or another S3 bucket where data is in its final format.

As you may have
different transformations for different data types, we recommend granularly splitting the
transformations into different Lambda functions for optimal performance. With this approach,
you have the flexibility to run data transformation in parallel and gain speed as well as
cost.

*Figure 28: Asynchronous data ingestion*

Firehose offers native [data transformations](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html)
that can be used as an alternative to Lambda, where no additional logic is necessary for
transforming records in Apache Log or System logs to CSV, JSON, JSON to Parquet, or
ORC.

A Kinesis data stream is a set of [shards](https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html#shard), each shard contains a
sequence of data records. Lambda reads records from the data stream and invokes your
function [synchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-sync.html) with an event that contains stream records. Lambda reads records
in batches and invokes your function to process records from the batch. Each batch
contains records from a single shard or data stream.

To minimize latency and maximize read throughput of processing data from a Kinesis data
stream, build your consumer with the [enhanced fan-out](https://docs.aws.amazon.com/kinesis/latest/dev/enhanced-consumers.html) feature. This
throughput is dedicated, which means that consumers that use enhanced fan-out don't have
to contend with other consumers that are receiving data from the stream.

Avoid invoking your function with a small number of records. You can configure the
event source to buffer records for up to five minutes by configuring a [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html#API_CreateEventSourceMapping_RequestSyntax)
*batch window* (`MaximumBatchingWindowInSeconds`). Lambda continues to
read records from the stream until it has gathered a full batch, or until the batch window
expires.

Configure the [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html#API_CreateEventSourceMapping_RequestSyntax)
*batch size* (`BatchSize`) to control the maximum number of records that can
be sent to your function with each invoke. A larger batch size can often more efficiently
absorb the invoke overhead across a larger set of records, increasing your throughput. Avoid
stalled shards by configuring the event source mapping to retry with a smaller batch size,
limit the number of retries, or discard records that are too old. To retain discarded events,
configure the event source mapping to send details about failed batches to an Amazon SQS queue or Amazon SNS
topic.

Increase your Kinesis stream processing throughput using the [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateEventSourceMapping.html#API_CreateEventSourceMapping_RequestSyntax) `ParallelizationFactor` setting to increase concurrency by
processing multiple batches from each shard in parallel. Lambda can process up to 10 batches in
each shard simultaneously keeping in-order processing at the partition-key level. Increase the
number of shards to directly increase the number of maximum concurrent Lambda function
invocations.

Use the Lambda emitted [IteratorAge](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#events-kinesis-metrics)
metric to estimate the latency between when a record is added and when the function
processes it.

## Serverless Event Submission with Status Updates

Suppose you have an ecommerce site and a customer submits an
order that kicks off an inventory deduction and shipment process; or an enterprise application
that submits a large query that may take minutes to respond.

The processes required to complete this common transaction may require multiple service
calls that may take a couple of minutes to complete. Within those calls, you want to
safeguard against potential failures by adding retries and exponential backoffs, However,
that can cause a less than ideal user experience for whoever is waiting for the
transaction to complete.

For long and complex workflows similar
to this, you can integrate API Gateway or AWS AppSync with Step Functions that upon new authorized
requests will start this business workflow. Step Functions responds immediately with an
execution ID to the caller (Mobile App, SDK, web service).

For legacy systems, you can use the execution ID to poll Step Functions for the business workflow
status via another REST API. With WebSockets, whether you’re using REST or GraphQL, you
can receive business workflow status in real-time by providing updates in every step of
the workflow.

*Figure 29: Asynchronous workflow with Step Functions state
machines*

Another common scenario is integrating API Gateway directly with Amazon SQS or Kinesis as a scaling layer.
A Lambda function would only be necessary if additional business information or a custom
request ID format is expected from the caller.

*Figure 30: Asynchronous workflow using a queue as a scaling
layer*

In this second example, Amazon SQS serves multiple purposes:

- Storing the request record durably is important because the client can confidently
proceed throughout the workflow knowing that the request will eventually be processed.
- Upon a burst of events that may temporarily overwhelm the backend, the request can be
polled for processing when resources become available.

Compared to the first example without a queue, Step Functions Standard Workflow is storing
the data durably without the need for a queue or state-tracking data sources. In both
examples, the best practice is to pursue an asynchronous workflow after the client submits the
request and avoiding the resulting response as blocking code if completion can take several
minutes.

With WebSockets, AWS AppSync provides this capability out of the box with GraphQL
subscriptions. With subscriptions, an authorized client could listen for data mutations
they’re interested in. This is ideal for data that is streaming, or that may yield more
than a single response.

With AWS AppSync, as status updates change in DynamoDB, clients can automatically subscribe and
receive updates as they occur and it’s the perfect pattern for when data drives the user
interface. With AWS AppSync you power your application with the right data, from one or more
data sources with a single network request using GraphQL. GraphQL works at the application
layer and provides a type system for defining schemas. These schemas serve as
specifications to define how operations should be performed on the data and how the data
should be structured when retrieved.

*Figure 31: Asynchronous updates via WebSockets with AWS AppSync and
GraphQL*

Web Hooks can be implemented with Amazon SNS Topic HTTP subscriptions. Consumers can host an
HTTP endpoint that Amazon SNS will call back through a POST method upon an event (for example,
a data file arriving in Amazon S3). This pattern is ideal when the clients are configurable,
such as another microservice, which could host an endpoint. Alternatively, [Step Functions supports callbacks](https://docs.aws.amazon.com/step-functions/latest/dg/callback-task-sample-sqs.html) where a state machine will block until it receives
a response for a given task.

*Figure 32: Asynchronous notification via Webhook with Amazon SNS*

Lastly, polling could be costly from both a cost- and resource-perspective due to multiple
clients constantly polling an API for status. If polling is the only option due to
environment constraints, it’s a best practice to establish SLAs with the clients to limit
the number of empty polls.

*Figure 33: Client polling for updates on transaction recently
made*

For example, if a large data warehouse query takes an average of two minutes for a
response, the client should poll the API after two minutes with exponential backoff if the
data is not available. There are two common patterns to ensure that clients aren’t polling
more frequently than expected: Throttling and Timestamp, for when is safe to poll
again.

For timestamps, the system being polled can return an extra field with a timestamp or
time period showing when it is safe for the consumer to poll once again. This approach
follows an optimistic scenario where the consumer will respect and use this wisely, and in
the event of abuse you can also employ throttling for a more complete
implementation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/aws-step-functions-2.html*

---

# Review

There are no performance efficiency practices unique to serverless applications for this
best practice.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/review.html*

---

# Monitoring

Monitor the Amazon CloudWatch AWS Lambda performance and concurrency metrics to understand
performance details about a single invocation and the number of instances processing events
across a function.

See the [AWS
Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) whitepaper for best practices in the monitoring area for
performance efficiency that apply to serverless applications.

View the AWS Compute Optimizer identified recommendations for AWS Lambda function memory sizes. AWS Compute Optimizer
uses machine learning to analyze historical utilization metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/monitoring.html*

---

# Tradeoffs

Configuring AWS Lambda-provisioned concurrency incurs charges to your AWS account.
Consider the functions you need to scale without fluctuations in latency. You can configure
provisioned concurrency on a version of a function, or on an alias.

See the [AWS
Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) whitepaper for best practices in the tradeoffs area for
performance efficiency that apply to serverless applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/tradeoffs.html*

---

# Key AWS services

Key AWS Services for performance efficiency are Amazon DynamoDB Accelerator, Amazon API Gateway,
AWS Step Functions, Amazon VPC, NAT gateway and AWS Lambda.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/key-aws-services-3.html*

---

# Resources

Refer to the following resources to learn more about our best practices for performance
efficiency.

## Documentation and blogs

- [Operating Lambda:
Performance optimization – Part 1](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)
- [Operating Lambda:
Performance optimization – Part 2](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-2/)
- [Operating Lambda:
Performance optimization – Part 3](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-3/)
- [Using
Amazon RDS Proxy with AWS Lambda](https://aws.amazon.com/blogs/compute/using-amazon-rds-proxy-with-aws-lambda/)
- [Understanding
Container Reuse in AWS Lambda](https://aws.amazon.com/blogs/compute/container-reuse-in-lambda/)
- [New for AWS Lambda – Predictable start-up times with Provisioned Concurrency](https://aws.amazon.com/blogs/compute/new-for-aws-lambda-predictable-start-up-times-with-provisioned-concurrency/)
- [Introducing AWS Lambda Extensions](https://aws.amazon.com/blogs/compute/introducing-aws-lambda-extensions-in-preview/)
- [Best
practices for organizing larger serverless applications](https://aws.amazon.com/blogs/compute/best-practices-for-organizing-larger-serverless-applications/)
- [Caching data and configuration settings with AWS Lambda extensions](https://aws.amazon.com/blogs/compute/caching-data-and-configuration-settings-with-aws-lambda-extensions/)
- [Best Practices
When Using Athena with AWS Glue](https://docs.aws.amazon.com/athena/latest/ug/glue-best-practices.html)
- [Analyzing
log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [Serverless Patterns Collection](https://serverlessland.com/patterns)
- [AWS Lambda Power
Tuning](https://github.com/alexcasalboni/aws-lambda-power-tuning)
- [Caching Best Practices](https://aws.amazon.com/caching/best-practices/)

## Developer guides

- [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Best practices for
working with AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)
- [Configuring a
Lambda function to access resources in a VPC](https://docs.aws.amazon.com/lambda/latest/dg/configuration-vpc.html)
- [Using Lambda extensions
- Impact on performance and resources](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html#using-extensions-reg)
- [Using AWS Lambda with
Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)
- [Managing concurrency for a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html#configuration-concurrency-provisioned)
- [AWS Lambda FAQs](https://aws.amazon.com/lambda/faqs/)
- [Choosing between HTTP APIs and REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vs-rest.html)
- [Enabling API caching to
enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)
- [Read/Write Capacity Mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html)
- [Using
Global Secondary Indexes in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)
- [In-Memory
Acceleration with DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)
- [Standard vs. Express
Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)
- [Using AWS Step Functions with
other services](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-service-integrations.html)
- [What Is
Amazon Kinesis Data Streams?](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [AppSync Data
sources and resolvers](https://docs.aws.amazon.com/appsync/latest/devguide/tutorials.html)
- [Optimizing cold
start performance for AWS Lambda](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/lambda-optimize-starttime.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/resources-3.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
