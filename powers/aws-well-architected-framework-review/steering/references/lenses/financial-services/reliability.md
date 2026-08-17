# Reliability

**Pillar**: Reliability  
**Questions**: 10

---

# FSIREL01: Have you planned for events that impact your software development infrastructure and challenge your recovery plans?

Financial services institutions are increasingly relying on continuous integration
(CI) and deployment (CD) pipelines to accelerate development and deployment. Often the
only way to change production systems is through the pipeline to ensure that quality
controls, security guard rails, and standards are maintained as part of the change
management process.

## FSIREL01-BP01 Treat your CI/CD tools as critical workload components for recovery

If key elements of an SDLC environment, such as the CI/CD
pipeline, are impacted, you might not be able to commit new
code, change configurations, pull containers, or upload
application artifacts, which can result in an outage of your
workload. Understand the entire dependencies of your SDLC and
plan for disruption of the critical components that the SDLC
relies on. Consider replicating your SDLC environment and
supporting services in another Region, which allows you to
continually replicate source code, application, and container
repositories. Based on the criticality of your workload, you
should understand how your components interact with both the
data plan and the control plan to understand what failures
would cause service disruptions to your workload.

## FSIREL01-BP02 Implement AI model versioning and rollback strategies

Financial services institutions must establish formal AI model
versioning and rollback capabilities to maintain operational
resilience. Implement immutable model registries that preserve
all model artifacts, training data characteristics,
hyperparameters, and performance metrics for each version.
Develop clear versioning conventions that include major and
minor designations based on the significance of model changes.
Establish automated deployment pipelines with built-in
validation gates and rollback triggers based on predefined
performance thresholds. Create comprehensive rollback
procedures that include not just technical reversion steps but
also business impact assessments, customer communication
templates, and regulatory notification processes where
required. Test rollback capabilities regularly as part of
disaster recovery exercises.

## FSIREL01-BP03 Add specialized AI system testing and validation to software testing methodology

Effective AI system testing and validation requires a
multi-layered approach beyond traditional software testing
methodologies. Establish separate development, testing, and
production environments with appropriate data separation and
access controls. Implement comprehensive testing regimes including
unit tests for individual components, integration tests for system
interactions, and holistic validation with representative data,
prompt and response testing, and human-in-the-loop evaluations
that provide qualitative checks for grounding, tone, and policy
compliance. For critical financial applications, conduct
adversarial testing to identify potential vulnerabilities and edge
cases. Validation should include fairness and bias assessments,
particularly for consumer-facing applications where regulatory
adherence is essential. Document all testing procedures, results,
and remediation actions to support audit requirements and
regulatory examinations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel01.html*

---

# FSIREL02: Are you practicing continuous resilience to ensure that your services meet regulatory availability and recovery requirements?

Your workload, and the environment in which it operates, is
constantly changing. To keep pace, resiliency practices should
not be considered a one-time effort. Make resilience a regular
part of your feature delivery and operational cadence
throughout a workload's lifetime. To this end, resiliency
testing should be part of your CI/CD testing pipelines.

Furthermore, you should establish a resiliency review on a
regular interval to validate that changes have not impacted
the application's resiliency posture. In addition to this, the
rise of generative AI have added a recommended pattern to
allow
[cross-region
inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) or
[provisioned
throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) to facilitate more reliable calls to
generative AI models.

## FSIREL02-BP01 Practice regular resilience testing

Resilience is not a one-time effort. Resilience should be
part of your day-to-day operations and practiced
continuously. Perform chaos engineering experiments and
scenario testing like
[Fault
Injection Service](https://aws.amazon.com/fis/) or Cross-Region connectivity faults
regularly to increase your team's understanding of how your
workload behaves in adverse conditions such as excessive
load, slow or failed network links, or a combination of
adverse conditions. Continuous testing for resilience helps
you to anticipate, observe, and respond to faults, as well
as find blind spots that you didn't know existed. By
practicing continuous resilience testing and
[chaos
engineering](https://aws.amazon.com/blogs/architecture/chaos-testing-with-aws-fault-injection-simulator-and-aws-codepipeline/), your teams can improve observability and
gain confidence in their ability to quickly detect and
recover from incidents as recovery procedures are practiced
and improved.

## FSIREL02-BP02 Implement an operational readiness review process

To capture learnings from previous incidents and minimize reoccurrence across
teams, implement an [operational readiness review
process](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) within your organization. As part of your incident
analysis process, identify key questions that, if asked prior to the incident, may
have prevented the incident from occurring. Maintain a list of these key questions so
that, as new features are released, your developers can refer back to the list and
make sure that they don't repeat the same mistakes that have disrupted other
workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel02.html*

---

# FSIREL03: How are your business and regulatory requirements driving the resilience of your workload?

## FSIREL03-BP01 Use business criticality to drive recovery objectives

Financial institutions scrutinize their most critical functions where a disruption
to the function could cause harm to consumers, policy holders, participants, or
industry integrity. This harm could mean that customers are unable to quickly recover
(for example, when a firm is unable to put a client back into the correct financial
position after a disruption or if they exceed the allowed disruption time). Resilience
requirements should guide the development and operation of workloads that deliver or
support these functions. Resilience requirements should be written to verify that the
workload implementing the requirements is able to meet impact tolerances. In capturing
resilience requirements, financial institutions must also consider any regulatory
requirements concerning resilience.

The resilience of a workload should be defined by the business sponsoring the
workload and is usually presented as RTO and RPOs plus a service-level objective
(SLO). The criticality of a workload should therefore drive the investment for
automated recovery of the workload. Example SLOs and mappings to resilience tiers are
shown in Table 1 and 2.

*Table 1 – Example resilience tiering for
SLO*

Availability SLO
Resilience tier
Acceptable downtime per year

99.99%
Platinum - Tier 1
52.60 minutes

99.90%
Gold - Tier 2
8.77 hours

98%
Silver - Tier 3
7.31 days

*Table 2 – Example resilience tiering for RTO and RPO*

Tier
Max RTO
Max RPO
Criteria
Cost

Platinum - Tier 1
15 minutes
30 seconds
Mission-critical workloads
$$$

Gold - Tier 2
15 minutes – 8 hours
2 hours
Important, but not mission-critical workloads
$$

Silver - Tier 3
6 hours – a few days
24 hours
Noncritical workloads
$

## FSIREL03-BP02 Apply fine grained workload resilience requirements

It's common to initially think of a workload's availability as a single target for
the workload as a whole. However, upon closer inspection, we frequently find that
certain functions of a workload have different availability requirements. For example,
some systems might prioritize the ability to receive and store new data ahead of
retrieving existing data. Other systems prioritize real-time operations over
operations that change a system's configuration or environment. The Well-Architected
reliability pillar outlines a few of the ways that you can decompose a single workload
into constituent parts-per-function and evaluate the availability requirements for
each. The benefit of decomposing is to focus efforts on availability according to the
specific needs of and the value delivered by the individual function, rather than
engineering the whole system to the strictest requirement.

Developing a system to the highest levels of availability can be expensive. Being
able to address the resilience of individual workload functions can allow you to
justify the investment based on the value of the function. With the functions measured
by their criticality, you can also make informed trade-offs such as degrading the
performance of less critical functions to maintain performance of the workload's most
critical functions.

## FSIREL03-BP03 Use past examples of market volatility in determining peak loads

In financial services workloads, even ones that do not directly provide services
for traders such as settlement and clearing, market volatility creates peak demand
requirements with a long-tail. The peak volume of an extreme event is much higher than
one would expect to model a normal distribution, and thus typical p95 and p99 metrics
are insufficient for estimating peak load. Determine if the workloads have
dependencies on market volatility, and adjust load testing scenarios based on
historical peaks, allowing you to determine how the workload performs in unexpected
situations. It is common that financial services workloads are subject to dramatic
increases in demand. The scaling response to the increase in demand must keep up with
the change in demand. For example, automatic scaling can take several minutes for a
workload to be ready to receive traffic, and may exceed the ability to respond to
customer requests in the expected timeframe, resulting in missed SLAs. For mission
critical workloads, consider concepts like [static
stability](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) and [graceful degradation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html) so that the workload continues to perform within
acceptable limits, even under extreme load.

## FSIREL03-BP04 Model failures to identify resilience requirements

Resilience requirements, like other system requirements, can
be tested and should be documented in response to a business
need. A resilience requirement must be met by the workload
in order

to achieve the RTO, RPO, and availability objective of the
business function the workload supports. The resilience
requirement does this by defining a control, which must be
designed and implemented to mitigate the impact of a failure
somewhere within the workload, with the

workload's dependencies, or in the workload's environment.

Use modeling techniques (for example, failure modes and
effects analysis (FMEA)), combined with Operational Readiness
Reviews (ORR), to anticipate the scenarios that could
disrupt the workload's ability to meet its objectives.
Create resilience requirements to mitigate any harm
anticipated by the failure modeling analysis.

As failures are modeled, implement appropriate tooling to
detect these failures in the future. Create runbooks for
documentation on resolving failures to minimize impact.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel03.html*

---

# FSIREL04: Does the resilience and the architecture of your workload reflect the business requirements and resilience tier?

Understanding how AWS services can impact your workload's availability is an
important step in determining the resilience of your architecture.

## FSIREL04-BP01 Use best practices to implement highly resilient critical workloads

Financial services institutions must be compliant with regulatory frameworks that
define policies towards the resilience and operational excellence of their mission
critical or core workloads. Workloads designated by regulators and financial
institutions as critical are therefore subject to greater scrutiny from regulators
because financial services institutions must demonstrate that they can recover
operations within reasonable recovery times and with little or no data loss.

To achieve these targets, you must mitigate scenarios that may disrupt your system
by anticipating the scenarios, being able to monitor for their occurrence, and having
pre-arranged responses in place. Adopting processes like ORRs, predictive monitoring
with leading indicators, and consistent deployments are just some of the best
practices that can be used to mitigate common scenarios. Additional workload design
patterns for resilient systems can be found in the [The Amazon Builders' Library](https://aws.amazon.com/builders-library/?cards-body.sort-by=item.additionalFields.sortDate&cards-body.sort-order=desc&awsf.filter-content-category=*all&awsf.filter-content-type=*all&awsf.filter-content-level=*all).

## FSIREL04-BP02 Provide external dependency accessibility from failover environments

FSI workloads often rely on many external service integrations with partner firms
or online services from other departments in the same firm. While your workload may be
able to resume service in a different failover environment, confirm that the system is
able to operate with its dependencies from the failover environment. Make your
dependencies accessible from the failover environment, and verify that the workload is
able to function despite any changes in network attributes, such as latency.

Tightly coupled dependencies may need to be failed over in advance of your
workload's failover. This slows down the recovery of your workload as it waits for its
dependencies to become available. Coordinate your disaster recovery failover to
expedite this process and bring down the recovery time to within acceptable
ranges.

## FSIREL04-BP03 Decouple your dependencies

Design your workload so that it is able to function despite impairment to dependencies, like external
service integrations with partner firms, as well as services from other departments in the
same firm. Decouple your workload from its
dependencies so that it has static stability and continues functioning, or at least
fails gracefully, even when its dependencies are impaired. Workload code should be
reviewed and tested with the consideration that any API call to an external dependency
may time out with no response, or return an unexpected error. Use chaos engineering to
perform experiments where the workload's functionality is observed during simulation
dependency disruption.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel04.html*

---

# FSIREL05: Is the resilience of the architecture addressing challenges for distributed workloads across AWS and an external entity?

## FSIREL05-BP01 Evaluate the resilience of cross-cloud application architectures

Understand the characteristics of your application components and how each component that is consumed across clouds may impact your system as a whole. Use failure mode and effects analysis (FMEA) to consider the severity and plausibility of possible failure modes, including application-level failures and service provider failures based on the provider's service event history. Consider if the added complexity of deployment across different types of environments adds to or reduces overall resilience.

## FSIREL05-BP02 Address hybrid resiliency

Use Direct Connect to provide a consistent network experience rather than
internet-based connections. Achieve highly resilient network connections between
Amazon Virtual Private Cloud (Amazon VPC) and your on-premises infrastructure by using multiple redundant
Direct Connect connections. Use AWS Direct Connect Resiliency Toolkit to help you choose
the right resiliency model. The AWS Direct Connect Failover Testing feature allows you to
test the resiliency of your AWS Direct Connect connection by disabling the Border Gateway
Protocol session between your on-premises networks and AWS.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel05.html*

---

# FSIREL06: To mitigate operational risks, can your workload owners detect, locate, and recover from gray failures?

Failures, such as loss of network connectivity, is often considered in a binary
nature where the connectivity is functioning normally or not functioning at all. However
there are non-binary failures called *gray failures*, which are
defined by the characteristic of differential observability, meaning that different
entities observe the failure differently. Gray failures can be subtle and difficult to
detect. An example of a gray failure with network connectivity is a 40% packet loss of
all TCP packets over a network link. Another example is intermittent failure on one or
more servers behind a load balancer where some requests fail, but not enough to initiate
the load balancer's health check. Overall service health metrics may be based on
aggregate metrics, such as average response time from the load balancer, which may
obscure localized failures.

## FSIREL06-BP01 Monitor indicators aside from system metrics that can signal client impairment

Capture data that measures the experience of your workload's clients to understand
when anomalies are affecting the customer experience with a workload function. Such
measures are often collected as percentiles to prevent outliers when trying to
understand the impact over time and how it's spread across your workload's clients.
Examples of such metrics may be the 99th percentile of latency from the load balancer,
a deviation in the number of requests being received over time, or the number of
unsuccessful responses returned to the client. Highly visible workload owners should
also have a means to monitor sudden increases in inbound customer support requests,
and complaints on social media channels. Have a way for users to send feedback
directly from within the service, or adjacent channels that can be monitored by
service owners in near real-time.

## FSIREL06-BP02 Have a way to find outliers hiding in aggregate metrics

Wherever system dashboards and monitors are reporting on aggregate results across
a fleet of resources, be sure that system operators can also break out metrics and
find outliers. Use tools like [Amazon CloudWatch Contributor
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) and [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to be able to ask
questions like: "Who are the top 10 clients with high error rates?" And: "Do those top
10 clients share a common root cause?"

## FSIREL06-BP03 Use anomaly detection to detect unusual changes in user engagement metrics

FSI workload owners should monitor for anomalies in metric data such as the
number of user requests that receive a timely and successful response, and user
session dropout rates (the number of users that began a multi-step process, such as a
payment flow, but didn't finish). With Amazon CloudWatch you can enable anomaly detection on
various metrics, which continually analyzes the metrics, determines normal baselines, and
surfaces anomalies that can in turn be used to initiate a CloudWatch alarm.

## FSIREL06-BP04 Have a way to manually route away during failure

There may be a need to fail away from a primary system to its secondary, either
because a system that depends on your workload needs to failover, or due to an
unexpected, undetected impact to your primary system. In such cases you may need to
manually override the status of health checks and route traffic away from the sources
of a gray failure. You can use services such as [Route 53 Application Recovery
Controller](https://aws.amazon.com/route53/application-recovery-controller/) and its feature [zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) with routing
controls. Also consider having a way to manually control and override the responses
from each health check target, providing you with full control when a workload is
considered unhealthy and initiated to route around the faulty resources.

## FSIREL06-BP05 Establish baselines for expected network traffic

To understand conditions of high or unexpected network traffic, you must
establish a steady state of metrics for the expected data flows between your workload
and its users as well as between the components within your workload. This baseline
should initiate an operational response when a workload is suddenly seeing abnormal
traffic throughput that exceeds the expected steady state ranges. Understanding the
steady state is key in creating the knowledge of normal communication patterns between
and within the workload components. Knowing which network communications patterns are
outside of normal ranges helps operations teams troubleshoot and isolate impacted
components.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel06.html*

---

# FSIREL07: How do you monitor your resilience objectives to achieve your strategic objectives and business plan?

## FSIREL07-BP01 Monitor and validate your RPO

RPO is the maximum amount of data loss allowed as the result of a system failure
expressed in units of time. Online Transaction Processing (OLTP) systems within
financial services institutions typically leverage continuous data replication to a
failover environment, where the RPO is a function of the latency of the data
replication. AWS database services such as Amazon RDS and Amazon DynamoDB offer continuous data
replication and also provide replication latency metrics that can be continuously
monitored. RPO can be further verified by continuously adding synthetic records into
the transaction stream and validating that each synthetic record was received,
processed, and replicated within the RPO target limit. Furthermore CloudWatch alarms should
be configured to alert whenever replication delays are routinely exceeding the system
RPO limits.

## FSIREL07-BP02 Monitor and validate your RTO

RTO is often defined as the maximum amount of time allowed for a system to resume
its normal operations after a failure. RTO is measured and validated by testing system
recovery processes and directly measuring the time it takes to recover. To be able to
provide audit evidence for proof of DR and recovery exercises, you have to understand
your workload's dependency chains to prove that if any of its dependencies fail, your
service can stay within the boundary of the defined RTO.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel07.html*

---

# FSIREL08: How do you monitor your resources to understand your workloads health?

High availability for applications requires the ability to detect failures and
recover quickly. Workloads must be configured to emit the relevant telemetry to detect
failures, so that operational processes can capture and react to these events.

## FSIREL08-BP01 Use a single pane of glass for monitoring

Amazon CloudWatch provides robust monitoring, allowing you to organize the data to
escalate detected issues as quickly as possible. Without adequate processes in place,
you may miss leading indicators of problems. A single pane of glass and standardizing
cloud monitoring standards across your organization can help avoid information silos
and simplify the analysis of monitoring data. Combining monitoring of AWS system
metrics and workload logs enables analysts to cross-reference signals and log
information across dependent systems. Frequently, issues surface in invoking systems,
and IT professionals spend time parsing logs on the invoking systems instead of on the
dependent systems where the error originated. Consider embedding metrics in logs with
[Embedded Metric
Format (EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.html), which allows you to quickly dive from the single pane of glass
to the most granular entity of your workload. More information on building efficient
dashboards for operational visibility can be found in the [The Amazon
Builders' Library](https://aws.amazon.com/builders-library/building-dashboards-for-operational-visibility/).

## FSIREL08-BP02 Alert on the absence of an event

The absence of monitoring data can indicate an underlying issue. Implement
controls that alert on missed reporting intervals. Treat missing data as a security
breach, and raise alarms appropriately.

## FSIREL08-BP03 Identify metrics and validate alerts through load testing

Workloads must be load-tested regularly to validate scaling and resilience.
Identify key metrics (for both components that auto scale with demand and for static
resources such as relational databases) that correlate with capacity constraints and
customer outages during these load tests.

As part of your load-testing, validate these metrics and associated alerts,
ensuring that alerts are issued as expected. Perform load tests in lower environments
to identify indicators for alerting and automated remediation. Validation of your
indicators and alerts through load testing minimize your Mean Time to Detection
(MTTD), giving your recovery mechanisms more time to respond and increasing the
workload's availability.

## FSIREL08-BP04 Use distributed tracing tools for service-oriented architectures

As systems become more distributed with the implementation of microservices
architectures, the challenge of identifying performance bottlenecks increase. Use
workload performance monitoring tools such as AWS X-Ray to trace and provide
telemetry across multiple systems and on a transaction-by-transaction basis. Adopt
tools like AWS X-Ray and [Open Telemetry](https://aws.amazon.com/otel/)
as integrated tools that provide tracing and data as transactions span across multiple
services.

## FSIREL08-BP05 Monitor AI model performance and drift

Continuous monitoring should track key performance
indicators against established baselines, with automated
alerts for significant deviations and configurable
thresholds with escalation procedures. Establish regular
cadences for model evaluation using production data,
comparing predictions against actual outcomes. Implement
comprehensive logging systems that capture input data
characteristics, prediction outputs, and environmental
factors to facilitate root cause analysis when performance
issues arise. For regulated applications, consider deploying
parallel inference systems where both current and candidate
models run simultaneously to compare outputs before
deployment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel08.html*

---

# FSIREL09: How are you backing up data in the cloud?

Not all backups are created equal, and not all have equal value. Ensure that the
data you're backing up, and the way in which it is stored, is commensurate with the
value of the data backup.

## FSIREL09-BP01 Implement a backup strategy

A comprehensive backup strategy is an essential part of an organization's data
protection plan to withstand, recover from, and reduce any impact that might be
sustained due to a security event. You should create an extensive backup strategy that
defines which data must be backed up, how often data must be backed up, and monitoring
of backup and recovery tasks. It is equally important to highlight which data should
not be backed up; your backup strategy should balance the cost of implementing a
backup strategy and the cost of backup retention with the value of the backups. If
data is non-essential or could be reconstructed from other sources, make it clear to
teams that not everything has to be backed up.

## FSIREL09-BP02 Maintain backups in a secondary Region

When you develop a comprehensive strategy for backing up and restoring data,
consider backing up your data into another AWS Region allowing you to recover
quickly in the case of a disaster recovery scenario. For those applications with
criticality, requiring them to operate in multiple Regions makes sure that you replicate
your backups from the primary to the secondary Region. Copying backups between Regions
can be done using custom tooling or the original features of various AWS services
such as [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html).
Alternatively, management of backups between Regions, including the management of
encryption keys for cross-Region replication, can be automated and performed using
[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel09.html*

---

# FSIREL10: How are backups retained?

## FSIREL10-BP01 Understand requirements for data backup and retention

An important task of determining the resilience requirements of a workload is to
identify data backup and retention needs. Financial institutions may have standards
for backup and retention of data in their systems, which may be informed by regulatory
requirements. Financial services customers must understand the requirements that apply
to the workloads that are running in their environments.

## FSIREL10-BP02 Back up logs as part of the backup strategy

In addition to the backup of workload data and databases, the system logs may
also fall under regulatory requirements. Include the AWS CloudTrail, CloudWatch Logs, workload, and
system logs in the log backup plan. In AWS, customers use Amazon S3, Amazon Glacier, Amazon EBS
snapshots, and Amazon RDS snapshots for backups of AWS services, and AWS Storage Gateway for
on-premises backup to AWS. The AWS Backup service centralizes the management of the
backups across the AWS environment by creating [tag-based policies to manage the backups](https://aws.amazon.com/blogs/storage/use-aws-backup-and-ci-cd-tools-to-automate-centralized-backup-across-aws-services/).

## FSIREL10-BP03 Incorporate anti-ransomware backups into your backup strategy

In addition to the normal backup cycle, short-lived anti-ransomware backups need
to be inserted into the backup cycle. Define a frequency and retention time on how
long these ransomware backups should be held that aligns with your corporate security
strategy. While a Regional copy of the data is sufficient for most cases, you can
consider replicating backups with AWS Backup into another Region and AWS account. For
a more detailed discussion around preventing ransomware, see [Protecting resources](https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/protecting-resources.html).

## FSIREL10-BP04 Create lifecycle policies for backups

Based on regulatory requirements, create lifecycle policies to retain and purge
data in AWS. You can use a lifecycle policy in Amazon S3 to allow for the automation of
migration of data to the most appropriate storage tier. AWS Backup allows for the
management of retention of data across the environment through tag-based policies.
AWS Backup also provides you with a [Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) mechanism to
help prevent changes to backup lifecycles, as well as help prevent manual deletion of backups,
helping you to align with your compliance requirements.

## FSIREL10-BP05 Use Glacier Vault Lock and S3 Object Lock for WORM storage

Financial institutions often need to retain records for many years in write-once
indelible storage. FSIs can use Glacier Vault Lock and S3 Object Lock mode to store
data using a write-once-read-many (WORM) model. Amazon S3 Object Lock has been assessed by
Cohasset Associates for use in environments that are subject to SEC 17a-4, CFTC, and
FINRA regulations. The Amazon S3 Object Lock mode applied to an object stops users
from modifying that object. To track which objects have S3 Object Lock, you can refer
to an Amazon S3 inventory report that includes the status of objects. Amazon S3 Object Lock
helps you adhere to regulatory requirements that require WORM storage, or add another layer
of protection against object changes and deletion. For more information about how Amazon S3
Object Lock relates to these regulations, see the [Cohasset Associates Compliance Assessment for Amazon S3 whitepaper](https://d1.awsstatic.com/r2018/b/S3-Object-Lock/Amazon-S3-Compliance-Assessment.pdf). AWS also
has partners that specialize in legal hold search and archive solutions that are
compatible with AWS, and often built on top of AWS WORM features. Refer to the
[AWS Partners
website](https://aws.amazon.com/partners/work-with-partners/) for information.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel10.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
