# Reliability

**Pages**: 6

---

# Foundations

REL 1: How are you regulating inbound request rates?

## Throttling

In a microservices architecture, API consumers may be in separate teams or even outside
the organization. This creates a vulnerability due to unknown access patterns, as well as
the risk of consumer credentials being compromised. The service API can potentially be
affected if the number of requests exceeds what the processing logic or backend can handle.

Additionally, events that trigger new transactions, such as an update in a database row or
new objects being added to an S3 bucket as part of the API, will trigger additional executions
throughout a Serverless application. Throttling should be enabled at the API level to enforce
access patterns established by a service contract. Defining a request access pattern strategy
is fundamental to establishing how a consumer should use a service, whether that is at the
resource or global level.

Returning the appropriate HTTP status codes within your API (such as a 429 for throttling)
helps consumers plan for throttled access by implementing back-off and retries
accordingly.

For more granular throttling and metering usage, issuing API keys to consumers with usage
plans in addition to global throttling enables API Gateway to enforce quota and access patterns in
unexpected behavior. API keys also simplify the process for administrators to cut off access
if an individual consumer is making suspicious requests.

A common way to capture API keys is through a developer portal. This provides you, as the
service provider, with additional metadata associated with the consumers and requests. You
may capture the application, contact information, and business area or purpose, and store
this data in a durable data store, such as DynamoDB. This gives you additional validation of
your consumers and provides traceability of logging with identities, so that you can contact
consumers for breaking change upgrades or issues.

As discussed in the security pillar, API keys are not a security mechanism to authorize
requests, and, therefore, should only be used with one of the available authorization options
available within API Gateway.

Concurrency controls are sometimes necessary to protect specific workloads against service
failure as they may not scale as rapidly as Lambda. [Concurrency controls](https://docs.aws.amazon.com/lambda/latest/dg/concurrent-executions.html) enable you to
control the allocation of how many concurrent invocations of a particular Lambda function are
set at the individual Lambda function level.

Lambda invocations that exceed the concurrency set of an individual function will be
throttled by the AWS Lambda service and the result will vary depending on their event source.
Synchronous invocations return an HTTP 429 error, Asynchronous invocations will be queued
and retried, while Stream-based event sources will retry up to their record expiration time.

*Figure 18: AWS Lambda concurrency controls*

Controlling concurrency is particularly useful for the following scenarios:

- Sensitive backend or integrated systems that may have scaling limitations: In
situations when your Lambda functions call some legacy or sensitive backend, they may put
too much pressure on the downstream services since functions may scale too fast and
produce many concurrent requests. It is a good idea to limit the concurrency of your
functions so that you can control the amount of requests they produce.
- Protecting against recursive invocations: You may introduce a recursive call of your
Lambda functions accidentally. One of the most common cases is when using S3 - Lambda - S3
pattern reading, and then writing into the same S3 bucket. Limiting concurrency will let
you decrease the implications of such recursive calls and help you detect and fix them
earlier.
- Database Connection Pool restrictions, such as a relational database, which may impose
concurrent limits: Many RDBMS have restrictions on the number of opened connections.
Limiting concurrency of the Lambda functions will allow you to limit the number of opened
connections. If using Amazon RDS databases consider using [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) as a connection pooling mechanism.
- Critical Path Services: Ensure that high priority Lambda functions, such as
authorization, do not run out of concurrency due to runaway invocations from low
priority functions (for example, backend asynchronous processes). Since Lambda
concurrency quotas are applied per account and Region, it's possible for one function to
consume concurrency such that other functions are throttled.
- Ability to disable Lambda function (`concurrency = 0`) in the event of
anomalies: In case of failures, setting concurrency to zero will help you to immediately
stop new invocations of your Lambda functions.
- Limiting desired execution concurrency to protect against Distributed Denial of
Service (DDoS) attacks: Usually the protection against DDoS is done at the API Gateway level,
but it is also a good idea to introduce an additional guard rail on the function level.

Concurrency controls for Lambda functions also limit its ability to scale beyond the
concurrency set and draws from your account reserved concurrency pool. For asynchronous
processing, use Kinesis Data Streams to effectively control concurrency with a single shard as
opposed to Lambda function concurrency control. This gives you the flexibility to increase the
number of shards or the parallelization factor to increase concurrency of your Lambda function.

*Figure 19: Concurrency controls for synchronous and asynchronous
requests*

REL 2: How are you building resiliency into your serverless application?

## Best practices

- Manage transaction, partial, and intermittent failures: Transaction failures might
occur when components are under high load. Partial failures can occur during batch
processing, while intermittent failures might occur due to network or other transient
issues.
- Manage duplicate and unwanted events: Duplicate events can occur when a request is
retried, multiple consumers process the same message from a queue or stream, or when a
request is sent twice at different time intervals with the same parameters. Design your
applications to process multiple identical requests to have the same effect as making a
single request. Events not adhering to your schema should be discarded.
- Orchestrate long-running transactions: Long-running transactions can be processed by
one or multiple components. Favor state machines for long-running transaction instead of
handling them within application code in a single component or multiple synchronous
dependency call chains.
- Consider scaling patterns at burst rates: In addition to your baseline performance,
consider evaluating how your workload handles initial burst rates that may be expected
or unexpected peaks.

## Asynchronous calls and events

Asynchronous calls reduce the latency on HTTP responses. Multiple synchronous calls, as
well as long-running wait cycles, may result in timeouts and *locked* code that prevents retry logic.

Event-driven architectures enable streamlining asynchronous initiations of code, thus
limiting consumer wait cycles. These architectures are commonly implemented asynchronously
using queues, streams, pub/sub, Webhooks, state machines, and event rule managers across
multiple components that perform a business functionality.

User experience is decoupled with asynchronous calls. Instead of blocking the entire
experience until the overall execution is completed, frontend systems receive a reference or
job ID as part of their initial request and they subscribe for real-time changes, or in
legacy systems use an additional API to poll its status. This decoupling allows the frontend
to be more efficient by using event loops, parallel, or concurrency techniques while making
such requests and lazily loading parts of the application when a response is partially or
completely available.

The frontend becomes a key element in asynchronous calls as it becomes more robust with
custom retries and caching. It can halt an in-flight request if no response has been
received within an acceptable SLA, whether it's caused by an anomaly, transient condition,
networking, or degraded environments.

Alternatively, when synchronous calls are necessary, it’s recommended at a minimum to
ensure that the total run time doesn’t exceed the API Gateway or AWS AppSync maximum timeout. Use an
external service (for example, AWS Step Functions) to coordinate business transactions across
multiple services, to control states, and handle error handling that occurs along the
request lifecycle.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/rel-foundations.html*

---

# Change management

There are no operational practices unique to serverless applications for this best
practice.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/change-management.html*

---

# Failure management

Certain parts of a serverless application are dictated by asynchronous calls to various
components in an event-driven fashion, such as by pub/sub and other patterns. When
asynchronous calls fail, they should be captured and retried whenever possible. Otherwise,
data loss can occur, resulting in a degraded customer experience.

Use a dead-letter queue mechanism to retain, investigate, and retry failed
transactions.

- [AWS Lambda](https://aws.amazon.com/lambda/)
allows failed transactions to be sent to a dedicated [Amazon SQS](https://aws.amazon.com/sqs/) dead-letter queue on a per function basis.
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/) and [Amazon DynamoDB Streams](https://aws.amazon.com/dynamodb/) retry the entire batch of items. Repeated errors block processing of
the affected shard until the error is resolved or the items expire.
- Within [AWS Lambda](https://aws.amazon.com/lambda/), you can configure
**Maximum Retry Attempts**, **Maximum
Record Age** and **Destination on Failure** to
respectively control retry while processing data records, and effectively remove
poison-pill messages from the batch by sending its metadata to an [Amazon SQS](https://aws.amazon.com/sqs/) dead-letter queue for further analysis.

AWS SDKs provide back-off and retry mechanisms by default when talking to other AWS
services that are sufficient in most cases. However, [review and tune
them](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-retry-timeout-sdk/) to suit your needs, especially `HTTP keepalive`,
`connection`, and `socket timeouts`. Whenever possible, use Step Functions to
minimize the amount of custom try/catch, back-off, and retry logic within your Serverless
applications. For example, you can use a Step Functions integration to save failed state runs and
their state into a DLQ. For more information on costs trade-offs, see the [cost optimization](./cost-optimization.html) pillar section.

*Figure 20: Step Functions state machine with DLQ step*

Partial failures can occur in non-atomic operations, such as `PutRecords`
(Kinesis) and `BatchWriteItem` (DynamoDB), since they return successful if at least one
record has been ingested successfully. Always inspect the response when using such
operations, and programmatically deal with partial failures. When consuming from Kinesis or
DynamoDB Streams use Lambda error handling controls, such as **maximum record
age**, **maximum retry attempts**, **DLQ on failure**, and **Bisect batch on function
error**, to build additional resiliency into your application. For synchronous
parts that are transaction-based and depend on certain guarantees and requirements, rolling
back failed transactions as described by the [Saga pattern](http://theburningmonk.com/2017/07/applying-the-saga-pattern-with-aws-lambda-and-step-functions/) also can be achieved by using Step Functions state machines, which
will decouple and simplify the logic of your application.

*Figure 21: Step Functions state machine Saga pattern*

Choose the Step Functions type based on your workload. For short-running synchronous and
asynchronous high-volume workloads, use Step Functions - Sync Express. If you need to automate long-running
workflows and want to have additional durability and audit go with Step Functions Standard.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/failure-management.html*

---

# Limits

In addition to what is covered in the Well-Architected Framework, consider reviewing
limits for burst and spiky use cases. For example, API Gateway and Lambda have different limits for
steady and burst request rates. Use scaling layers and asynchronous patterns when possible,
and perform load testing to ensure that your current account limits can sustain your actual
customer demand.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/limits.html*

---

# Key AWS services

Key AWS services for reliability are AWS Marketplace, Trusted Advisor, CloudWatch Logs, CloudWatch, API Gateway,
Lambda, X-Ray, Step Functions, Amazon SQS, and Amazon SNS.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/key-aws-services-2.html*

---

# Resources

Refer to the following resources to learn more about our best practices for reliability.

## Documentation and blogs

- [Quotas in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
- [Quotas in
API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html#api-gateway-limits)
- [Quotas and Limits
in Kinesis Streams](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
- [Service, Account, and Table Quotas
in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html)
- [Quotas in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/limits-overview.html)
- [Getting
started with testing serverless applications](https://aws.amazon.com/blogs/compute/getting-started-with-testing-serverless-applications/)
- [Monitoring Lambda Functions Logs](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-logs.html)
- [Versioning
Lambda](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html)
- [Stages in
API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/stages.html)
- [API Retries in
AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)
- [Step Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-handling-error-conditions.html#using-state-machine-error-conditions-step-4)
- [AWS Lambda and AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-services-lambda.html)
- [Error handling
and automatic retries in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html)
- [Lambda DLQ](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq)
- [Lambda
destinations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations)
- [Step Functions
Wait state](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-wait-state.html)
- [Step Functions Standard
vs. Express Workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)
- [Saga pattern](http://microservices.io/patterns/data/saga.html)
- [Applying Saga pattern with Step Functions](http://theburningmonk.com/2017/07/applying-the-saga-pattern-with-aws-lambda-and-step-functions/)
- [Designing durable serverless apps with DLQs for Amazon SNS, Amazon SQS, AWS Lambda](https://aws.amazon.com/blogs/compute/designing-durable-serverless-apps-with-dlqs-for-amazon-sns-amazon-sqs-aws-lambda/)
- [Troubleshooting
retry and timeout issues with AWS SDK](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-retry-timeout-sdk/)
- [Lambda resiliency controls for stream processing](https://aws.amazon.com/blogs/compute/new-aws-lambda-controls-for-stream-processing-and-asynchronous-invocations/)

## Whitepapers

- [Implementing Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/introduction.html)
- [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/resources-2.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
