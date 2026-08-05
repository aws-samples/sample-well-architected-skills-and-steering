# Operational excellence

**Pages**: 12

---

# Organization

There are no operational practices unique to serverless applications for this best
practice.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/organization.html*

---

# Prepare

There are no operational practices unique to serverless applications for this best
practice.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/prepare.html*

---

# Metrics and alerts

It’s important to understand Amazon CloudWatch metrics and dimensions for every AWS service
you intend to use so that you can put a plan in a place to assess its behavior and add
custom metrics where you see fit.

Amazon CloudWatch provides [automated cross service and per service dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Automatic_Dashboards_Cross_Service.html) to help you understand key
metrics for the AWS services that you use. Use Lambda Powertools for supported languages
to create and capture custom CloudWatch metrics. When Lambda Powertools is not available in your
programming language of choice, use [Amazon CloudWatch Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation.html) (EMF) libraries. EMF logs emitted by Lambda are
processed asynchronously by CloudWatch and do not impact the performance of your Serverless
application.

The following guidelines can be used whether you are creating a dashboard or looking to
formulate a plan for new and existing applications when it comes to metrics:

- **Business metrics**

Business KPIs that will measure your application performance against business
goals and are important to know when something is critically affecting your
overall business, revenue-wise or not.
- Examples: Orders placed, debit or credit card operations, flights
purchased

- **Customer experience metrics**

Customer experience data dictates not only the overall effectiveness of its UI
and UX, but also whether changes or anomalies are affecting customer experience in
a particular section of your application. Often times, these are measured in
percentiles to prevent outliers when trying to understand the impact over time and
how it’s spread across your customer base.
- Examples: Perceived latency, time it takes to add an item to a basket or to
check out, page load times

- **System metrics**

Vendor and application metrics are important to understand the health of your
system, uncover root causes from the metrics above, and gain insight into customer
experience.
- Examples: Percentage of HTTP errors and successes, memory utilization, function
duration, error, or throttling, queue length, stream records length, integration
latency

- **Operational metrics**

Operational metrics are equally important to understand sustainability and
maintenance of a given system. These metrics are also crucial to pinpoint how
stability progressed or degraded over time.
- Examples: Number of tickets (successful and unsuccessful resolutions), number
of times people on-call were paged, availability, CI/CD pipeline stats (successful
and failed deployments, feedback time, cycle and lead time)

CloudWatch Alarms should be configured at both individual and aggregated levels. An
individual-level example is alarming on the *Duration* metric from
Lambda or `IntegrationLatency` from API Gateway when invoked through API, since
different parts of the application likely have different profiles. In this instance, you
can quickly identify a bad deployment that makes a function execute for much longer than
usual.

Aggregate-level examples include alarming, but are not limited to the following
metrics:

- **AWS Lambda**: `Duration`,
`Errors`, `Throttles`, and `ConcurrentExecutions`.
For stream-based invocations, alert on `IteratorAge`. For asynchronous
invocations, alert on `DeadLetterErrors`. When provisioned concurrency is
enabled, use `ProvisionedConcurrencySpilloverInvocations`.
- **Amazon API Gateway**: `IntegrationLatency`,
`Latency`, `5XXError`. For WebSocket API, use
`ClientError`, `IntegrationError` and
`ExecutionError`.
- **Application Load Balancer**: `HTTPCode_ELB_5XX_Count`,
`RejectedConnectionCount`, `HTTPCode_Target_5XX_Count,
UnHealthyHostCount`, `LambdaInternalError`,
`LambdaUserError`.
- **AWS AppSync**: `5XX` and `Latency`.
- **Amazon SQS:**
`ApproximateAgeOfOldestMessage`.
- **Amazon Kinesis Data Streams:**
`ReadProvisionedThroughputExceeded`,
`WriteProvisionedThroughputExceeded`,
`GetRecords.`,`IteratorAgeMilliseconds`,
`PutRecord.Success`, `PutRecords.Success` (if using Kinesis
Producer Library) and `GetRecords.Success`.
- **Amazon SNS**: `NumberOfNotificationsFailed`,
`NumberOfNotificationsFilteredOut-InvalidAttributes`.
- **Amazon SES:**
`Rejects`, `Bounces`, `Complaints`,
`RenderingFailures`.
- **AWS Step Functions:**
`ExecutionThrottled`, `ExecutionsFailed`,
`ExecutionsTimedOut`, `ActivitiesTimedOut`,
`LambdaFunctionsTimedOut`.
- **Amazon EventBridge:**
`FailedInvocations`, `ThrottledRules`.
- **Amazon S3:**
`5xxErrors`, `TotalRequestLatency`.
- **Amazon DynamoDB:**
`ReadThrottleEvents`, `WriteThrottleEvents`,
`SystemErrors`, `ThrottledRequests`, `UserErrors`.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-metrics-and-alerts.html*

---

# Centralized and structured logging

Standardize your application logging to emit operational information about
transactions, correlation identifiers, request identifiers across components, and business
outcomes using structured logging. Unstructured logging using `print` or
`console.log` statements is unfavorable as they are difficult to interpret
and analyze programmatically, hard to add contextual information to, and inconsistent.
Structured logging libraries are advantageous because of configurable logging levels, API
consistency and common output formats, among other things. Use logging utilities from
Lambda Powertools to further simplify and enhance application logging.

JSON is a ubiquitous format which is often used as an output format and supported across
logging services. CloudWatch Logs Insights automatically discovers values in JSON which makes
querying and filtering simple. Judicious event logging from your application provides the
ability to answer arbitrary questions about the state of your workload such as user
behavior, state of your system and anomalous events, among other things. CloudWatch Logs Insights
also facilitates finding Lambda performance data from default log events.

*Figure 8: CloudWatch Logs Insights query to find statistics on cold
starts*

Consistently logging of correlation IDs and passing them to downstream systems allows
tracing and tracking of individual requests or invocations. As your system grows and more
logging is ingested, consider using appropriate logging levels and a sampling mechanism to
log a small percentage of logs in DEBUG mode. Log level configuration should be passed to
downstream systems for consistent tracing in a microservice architecture.

The Lambda Logs API can be used to send Lambda logs to locations other than CloudWatch. A
number of partner solutions provide Lambda layers which use the Lambda Logs API and make
integration with their systems easier. The recommendations and guidance here applies
uniformly regardless of log destination.

The following is an example of a structured logging using JSON as the output:

```
`{
"timestamp":"2019-11-26 18:17:33,774",
"level":"INFO",
"location":"cancel.cancel_booking:45",
"service":"booking",
"lambda_function_name":"test",
"lambda_function_memory_size":"128",
"lambda_function_arn":"arn:aws:lambda:eu-west-1:12345678910:function:test",
"lambda_request_id":"52fdfc07-2182-154f-163f-5f0f9a621d72",
"cold_start": "true",
"message": {
"operation":"update_item",
"details:": {
"Attributes": {
"status":"CANCELLED"
},
"ResponseMetadata": {
"RequestId":"G7S3SCFDEMEINPG6AOC6CL5IDNVV4KQNSO5AEMVJF66Q9ASUAAJG",
"HTTPStatusCode":200,
"HTTPHeaders": {
"server":"Server",
"date":"Thu, 26 Nov 2019 18:17:33 GMT",
"content-type":"application/x-amz-json-1.0",
"content-length":"43",
"connection":"keep-alive",
"x-amzn-requestid":"G7S3SCFDEMEINPG6AOC6CL5IDNVV4KQNSO5AEMVJF66Q9ASUAAJG",
"x-amz-crc32":"1848747586"
},
"RetryAttempts":0
}
}
}
}`
```

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-logging.html*

---

# Distributed tracing

Similar to non-serverless applications, anomalies can occur at larger scale in
distributed systems. Due to the nature of serverless architectures, it’s fundamental to have
distributed tracing.

Making changes to your serverless application entails many of the same principles of
deployment, change, and release management used in traditional workloads. However, there are
subtle changes in how you use existing tools to accomplish these principles.

Active tracing with AWS X-Ray should be enabled to provide distributed tracing
capabilities as well as to enable visual service maps for faster troubleshooting. X-Ray
helps you identify performance degradation and quickly understand anomalies, including
latency distributions.

*Figure 9: AWS X-Ray Service Map visualizing a workload using AWS Lambda,
Amazon DynamoDB and Amazon EventBridge*

Service Maps are helpful to understand integration points that need attention and
resiliency practices. For integration calls, retries, backoffs, and possibly circuit
breakers are necessary to prevent faults from propagating to downstream services.

Another example is networking anomalies. You should not rely on default timeouts and
retry settings. Instead, tune them to fail fast if a socket read/write timeout happens
where the default can be seconds, if not minutes, in certain clients.

X-Ray also provides two powerful features that can improve the efficiency on
identifying anomalies within applications: annotations and subsegments.

*Subsegments* are helpful to understand how application logic is
constructed and what external dependencies it has to talk to.
*Annotations* are key-value pairs with string, number, or Boolean
values that are automatically indexed by AWS X-Ray.

Combined, subsegments and annotations can help you quickly identify performance
statistics on specific operations and business transactions. Examples are a database query
duration, or the durations of a supporting function which parses an image.

*Figure 10: AWS X-Ray Trace with subsegments beginning with
##*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-distributed-tracing.html*

---

# Prototyping

OPS 2: How do you approach application lifecycle management?

Use infrastructure as code to create temporary environments for new features that you
want to prototype, and tear them down as you complete them. You can use dedicated accounts
per team or per developer depending, on the size of the team and the level of automation
within the organization.

Temporary environments allow for higher fidelity when working with managed services,
and increase levels of control to help you gain confidence that your workload integrates and
operates as intended.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-prototyping.html*

---

# Configuration

For configuration management, use environment variables for infrequent changes,
such as logging level and database connection strings. Use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) Parameter Store (SSM) or AWS AppConfig for dynamic
configuration, such as feature toggles. Store sensitive data using AWS Secrets Manager. In
Lambda functions, lookup values by reference from these external systems (SSM, AWS AppConfig,
Secrets Manager) in the function’s global scope outside the handler to reduce API calls. You
can achieve the same goal of reducing API calls to configuration and secrets stores using
Lambda extensions which provide more fine-grained controls and the ability to re-fetch
values. Lambda extensions are powerful and flexible yet bring additional considerations and
challenges including integrations with unit tests and consistent delivery across functions
and runtimes. Lambda Powertools offer similar functionality to retrieve values from various
providers including SSM, AWS AppConfig, Secrets Manager, DynamoDB or custom stores.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-configuration.html*

---

# Testing

Testing is commonly done through unit, integration, and acceptance tests. Developing robust
testing strategies allows you to emulate your serverless application under different loads
and conditions. Unit tests shouldn’t be different from non-serverless applications and,
therefore, can be designed to run locally without any changes. Integration tests shouldn’t
mock services you can’t control, since they might change and provide unexpected results.
These tests are better performed when using real services because they can provide the same
environment a serverless application would use when processing requests in production.
Acceptance or end-to-end tests should be performed without any changes because the primary
goal is to simulate the end users’ actions through the available external interface.
Therefore, there is no unique recommendation to be aware of here. In general, Lambda and
third-party tools that are available in the AWS Marketplace can be used as a test harness in the
context of performance testing. Here are some considerations during performance testing to
be aware of:

Metrics such as invoked maximum memory used and `init` duration are
available in CloudWatch Metrics. For more information, see the [performance pillar](./performance-efficiency.html)section.

If your Lambda function is attached to Amazon Virtual Private Cloud (Amazon VPC), pay attention to the available IP
address space inside your subnet.

Creating modularized code as separate functions outside of the handler enables more
unit-testable functions.

Establishing externalized connection code (such as a connection pool to a relational
database) referenced in the Lambda function’s static constructor or initialization code
(global scope, outside the handler) will ensure that external connection thresholds are
not reached if the Lambda execution environment is reused.

Use a DynamoDB on-demand table unless your performance tests exceed current quotas in your
account.

Take into account any other service quotas that might be used within your serverless
application under performance testing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-testing.html*

---

# Deploying

Use infrastructure as code and version control to enable tracking of changes and
releases. Isolate development and production stages in separate environments. This reduces
errors caused by manual processes and helps increase levels of control to help you gain
confidence that your workload operates as intended.

Use a serverless framework to model, prototype, build, package, and deploy serverless
applications, such as AWS Serverless Application Model or Serverless Framework. With infrastructure as code (IaC)
and a framework, you can add parameters to your serverless application and its
dependencies to ease deployment across isolated stages and across AWS accounts.

Infrastructure frameworks like AWS Cloud Development Kit (AWS CDK) and Terraform play important roles when
managing AWS resources. Serverless-specific tools like AWS SAM and the Serverless
Framework bring unique features to speed day-to-day development and are purpose-built to
minimize the code, test, and deploy loop.

Create separate stages or environments using CI/CD pipelines (for example, Gamma, Dev,
and Prod). A CI/CD pipeline can create the following resources in a beta AWS account:
`OrderAPIBeta`, `OrderServiceBeta`,
`OrderStateMachineBeta`, `OrderBucketBeta`, and
`OrderTableBeta`. Similar, yet separate, resources can be created across
different environments which might reside in separate AWS accounts.

*Figure 11: CI/CD pipeline for multiple accounts*

When deploying to production, favor safe deployments over all-at-once systems as new
changes will gradually shift over time towards the end user in a canary or linear
deployment. Use CodeDeploy hooks (`BeforeAllowTraffic`,
`AfterAllowTraffic`) and alarms to gain more control over deployment validation,
rollback, and any customization you may need for your application.

You can also combine the use of synthetic traffic, custom metrics, and alerts as part
of a rollout deployment. These help you proactively detect errors with new changes that
otherwise would have impacted your customer experience.

*Figure 12: AWS CodeDeploy Lambda deployment and hooks*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/opex-deploying.html*

---

# Evolve

There are no operational practices unique to serverless applications for this best
practice.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/evolve.html*

---

# Key AWS services

Key AWS services for operational excellence include AWS Systems Manager Parameter Store, AWS Serverless Application Model, CloudWatch, AWS CodePipeline, AWS X-Ray, Lambda, and API Gateway.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/key-aws-services.html*

---

# Resources

Refer to the following resources to learn more about our best practices for operational
excellence.

## Documentation and blogs

- [AWS
SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [API Gateway stage variables](https://docs.aws.amazon.com/apigateway/latest/developerguide/stage-variables.html)
- [Lambda environment
variables](https://docs.aws.amazon.com/lambda/latest/dg/env_variables.html)
- [Powertools for AWS Lambda
(Python)](https://docs.powertools.aws.dev/lambda/python/latest/)
- [Powertools for AWS Lambda
(TypeScript)](https://docs.powertools.aws.dev/lambda/typescript/latest/)
- [Powertools for AWS Lambda
(Java)](https://docs.powertools.aws.dev/lambda/java/)
- [Powertools for AWS Lambda
(.NET)](https://docs.powertools.aws.dev/lambda/dotnet/)
- [CloudWatch Embedded Metric
Format library for Python](https://github.com/awslabs/aws-embedded-metrics-python)
- [CloudWatch Embedded Metric
Format library for Node.js](https://github.com/awslabs/aws-embedded-metrics-node/)
- [CloudWatch Embedded Metric
Format library for Java](https://github.com/awslabs/aws-embedded-metrics-java)
- [CloudWatch Embedded Metric
Format library for .NET](https://github.com/awslabs/aws-embedded-metrics-dotnet)
- [Operating Lambda: Logging and custom metrics](https://aws.amazon.com/blogs/compute/operating-lambda-logging-and-custom-metrics/)
- [Operating Lambda:
Using CloudWatch Logs Insights](https://aws.amazon.com/blogs/compute/operating-lambda-using-cloudwatch-logs-insights/)
- [Common CloudWatch Logs
Insights queries](https://github.com/aws-samples/cloudwatch-logs-insights-queries)
- [Using
AWS Lambda extensions to send logs to custom destinations](https://aws.amazon.com/blogs/compute/using-aws-lambda-extensions-to-send-logs-to-custom-destinations/)
- [Building
well-architected serverless applications blog series](https://aws.amazon.com/blogs/compute/building-well-architected-serverless-applications-introduction/)
- [X-Ray latency
distribution](https://aws.amazon.com/blogs/aws/latency-distribution-graph-in-aws-x-ray/)
- [Troubleshooting
Lambda-based applications with X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html)
- [System Manager
(SSM) Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html)
- [AWS
AppConfig integration with Lambda Extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-integration-lambda-extensions.html)
- [AWS
Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [Cache secrets using AWS Lambda extensions](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/cache-secrets-using-aws-lambda-extensions.html)
- [Serverless Application example using CI/CD](https://github.com/awslabs/realworld-serverless-application/wiki/CI-CD)
- [CI/CD for Serverless Applications -
Workshop](https://cicd.serverlessworkshops.io/)
- [Serverless CI/CD for the Enterprise on AWS - Reference Deployment](https://aws.amazon.com/quickstart/architecture/serverless-cicd-for-enterprise/)
- [Using GitHub Actions to deploy serverless applications](https://aws.amazon.com/blogs/compute/using-github-actions-to-deploy-serverless-applications/)
- [Serverless Application example automating Alerts and Dashboard](https://github.com/awslabs/realworld-serverless-application/wiki/Serverless-Operations)
- [AWS service
quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [Stackery:
Multi-Account Best Practices](https://www.stackery.io/blog/multi-account-best-practices/)

## Whitepapers

- [Practicing Continuous Integration/Continuous Delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html)

## Third-party tools

- [Serverless Developer Tools page
including third-party frameworks/tools](https://aws.amazon.com/serverless/developer-tools/)
- [Stelligent: CodePipeline
Dashboard for operational metrics](https://stelligent.com/2017/11/16/codepipeline-dashboard/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/resources.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
