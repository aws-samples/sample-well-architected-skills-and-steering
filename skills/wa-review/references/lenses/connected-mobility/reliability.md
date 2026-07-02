# Reliability

**Pages**: 6

---

# Design principles

In addition to the overall Well-Architected Framework design principles, the following
are the design principles for reliability for connected mobility:

- **Design for failure and resiliency:** It's essential to plan
for resiliency on the vehicle-based telematics unit. Depending on your use case,
resiliency might entail robust retry logic for intermittent connectivity, ability to roll
back firmware updates, ability to fail over to a different networking protocol for
critical message delivery, ability to perform a factory reset.
- **Implement synthetic monitoring:** Simulate the vehicles
behavior by implementing digital clone of the in-vehicle software communicating with the
connected mobility application. The monitoring must share no cloud resources with the
connected mobility backed that is monitoring to being able to assess impairments of the
cloud part.
- **Plan for poor network connectivity:** Vehicles must
tolerate connectivity or backend errors. Connectivity is subject to continuous
interruption given the position of the vehicle, like tunnels, underground parks or remote
locations with low to none signal. Cloud backend applications must tolerate vehicles that
often transition between being connected and disconnected. Availability of connected
services and user experience on disconnection is the core aspect and basic reason of this
platform's existence.
- **Invalidate commands that have passed their usability
threshold:** Connected mobility platforms enable the communication of commands
to the vehicle. The commands are intended to be run on the vehicle at the requested or
configured time, generally in near real time. At times, the state of the vehicle or the
backend system may be such that this communication fails to execute in expected timeframe.
Due to this delay the command may either have been overridden by next command, are no
longer relevant or may be not safe enough to execute. For example, a door unlock command
might not be safe enough or relevant to run after few minutes of delay. Based upon the use
case and the nature of the commands, the backend system should invalidate the commands if
they are stale or passed their usability threshold.
- **Design for idempotent systems:** There can be situations
where the connected mobility system might receive multiple messages that are identical
thus causing an overload. Although the complexity of implementation would be higher,
idempotency reduces the risks of system overload, failure, and reduced availability.
- **Aggregate for simplicity but be prepared to dive deep into logs for
causal analysis:** Connected mobility platforms collect data at high velocity
and volume. Vehicle manufacturers use various mechanisms to aggregate this data for
specific vehicle or fleet over a time. Based upon the use case, a deep dive into the
system and application logs may be needed to troubleshoot issues, determine performance
bottlenecks, execution steps, or to meet compliance regulations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/design-principles-rel.html*

---

# Foundations

CMREL_1: Have you defined your message prioritization policy?

Connected vehicles generate a large amount of data that is sent to the cloud via
messages. It's important to prioritize the message flow and handle different message
severities with different policies.

Connected vehicles generate a large amount of data that must be sent to the cloud via
messages. It's important to prioritize the message flow and handle different severities with
different policies.

**[CMREL_BP1.1] Defining message tier matrix**

The connected mobility solution must classify messages from the vehicle fleet to the
cloud backend in at least two tiers, such as:

- High priority messages
- Low priority messages

These two tiers must be processed using different approaches when it comes to resiliency
as described in the following sections. The tier structure is multidimensional to account
for messages that should be sent as soon as possible or not sent at all (urgency dimension),
and for relevancy. In the urgency dimension are messages that pertain to GPS and ADAS
messages that must be sent, even if they cannot be sent in real time (relevance dimension).
Messages for emergency calls are also in this dimension. Lowest on the priority list (low
urgency and low relevance) include telemetry messages that can be sent in batches on a given
schedule.

**[CMREL_BP1.2] Have a strategy for critical
functions**

Connected mobility should implement critical functions. such as emergency calls in
which messages from the vehicle must be delivered to the cloud no matter what, to overcome
transient failures in the connectivity as well as in the control plane. Those messages
should sit on top of the tier matrix (high relevance, high urgency). In such cases, you
should plan for redundancy for every physical or logical component of in-vehicle as well as
the communication layer with the cloud (such as SIM failure, modem failure, and telco
failure).

Consider building the control plane in multiple Regions and have the vehicles connect to
the first available endpoint for these critical functions.

CMREL_2: How do you ensure that you do not overflow your communication channel
to the cloud?

Messaging from vehicles to the cloud is likely to be unpredictable, generating spikes
that might approach AWS service quotas. If proper measures are not taken, these spikes
could result in message throttling, application impairment, or both.

**[CMREL_BP2.1] Guardrail chatty vehicles**

The connected mobility solution must tolerate anomalies in the message workflows
received from the vehicle fleet. The connected mobility control plane that receives messages
from the vehicle fleet must tolerate spikes in the vehicle's messaging flow throttling low
priority messages down to avoid exceeding service quotas and unwanted cost spikes. If
throttling of low priority messages is not enough to avoid exceeding a service quota,
messages must be classified in more than two tiers and a policy must be implemented to
throttle messages down when appropriate.

**[CMREL_BP2.2] Avoid connection surge to the
cloud**

A vehicle’s side application and firmware must implement a randomized connection to the
backend cloud applications to avoid unnecessary peak traffic. Situations where the entire
fleet attempts the same operation at the same time must be avoided. Traffic generated from
low priority tier messages should be randomized. Navigating the tier structure bottom up,
trade off decision must be taken and implemented whether to randomize the traffic avoiding
connection peaks or increase a service quota (where applicable). The same randomized
behavior must be implemented on the cloud backend for messages that are being sent to the
vehicles.

CMREL_3: Do you have a strategy in case connection certificates are unavailable
or accidentally deleted?

As a best practice, vehicles establish a connection to the backend by exchanging
certificates. The connected mobility control plane must store these certificates with the
highest level of durability, considering that installing new certificates to the client
likely requires the vehicles to be called back at the OEM or auto dealership. Backup
strategy must be built and emergency registration procedure must be available. Be sure to
test both the restore procedure and the emergency procedure with tabletop exercises.

**[CMREL_BP3.1] Implement just-in-time provisioning and
registration**

When using AWS IoT Core to connect vehicles to the AWS Cloud, it’s a best practice to
implement just-in-time provisioning (JITP), just-in-time registration (JITR), or both. In
both cases, certificates are provisioned the first time devices connect to AWS IoT Core by
using a certificate template (JITP) or an AWS Lambda function (JITR). Using JITP and JITR can
help restore a compromised device registry.

**[CMREL_BP3.2] Manual backup of the device
registry**

AWS IoT Core stores information about your devices in the device registry. It also
stores CA certificates, device certificates, and device shadow data. In the event of
hardware or network failures, this data is automatically replicated across Availability
Zones but not across Regions.

AWS IoT Core publishes MQTT events when the device registry is updated. You can use
these messages to back up your registry data and save it somewhere, like a DynamoDB table.
You are responsible for saving certificates that AWS IoT Core creates for you or those you
create yourself.

CMREL_4: How is your connected mobility solution resilient to unintended
access?

Every infrastructure is susceptible to unintended access and threat actors. Connected
mobility is no exception. Your connected mobility solution should implement the security by
design approach to reduce the scope of impact and mitigate and help prevent inadvertent
access. The solution should be resilient to events even if some functions are impaired by
these issues.

**[CMREL_BP4.1] Implementing a layered approach**

An OEM can mitigate the negative impact of unintended access events on connected
vehicles by adopting a layered approach. In vehicle design, physical networks can be
separated by artificial layers. For example, you can create an engine control unit layer, an
in-vehicle communication network layer, and an external interfaces layer. The layer creation
will involve technologies such as gateways, firewalls, message authentication, encryption,
and intrusion detection and prevention systems. During vehicle manufacturing, several
practices can also be considered to identify and mitigate connected vehicle issues and
risks, including:

- Developing over-the-air (OTA) update capabilities for connected vehicle software and
firmware.
- Conducting risk assessment and attack testing.
- Creating domain separation for in-vehicle networks.
Mission- and safety-critical components in a connected vehicle can be separated from
non-critical components, and given limited connectivity to external networks through a
few specific communication channels.

CMREL_5: How do you mitigate the impact of impairments in the connection layer
between vehicles and the AWS Cloud?

Connected mobility is a peculiar scenario in Internet of Things (IoT) given that the
things don’t have a reliable Local Area Network (LAN) to which they are connected. Vehicles
use mobile connectivity which is likely provided by a third party, and vehicles might move
to locations where the mobile connectivity is limited or not available at all.

**[CMREL_BP5.1] Account for telco providers
outages**

Vehicles connect to the cloud control plane leveraging on telematic providers services
(telco), the connected mobility solution must account for failures in this transport layer.
The solution must be able to distinguish if a connection drop has been caused by the
vehicle, the telco, or the control plane in the cloud.

**[CMREL_BP5.2] Implement in-vehicle
functionalities**

Connected mobility application reliability must also encompass the vehicle itself.
Vehicles might be operating in remote locations and deal with intermittent connectivity, or
loss in connectivity, due to a variety of external factors that are out of your connected
mobility application’s control. For example, if an ISP is interrupted for several hours, how
will the vehicle behave and respond to these long periods of potential network outage?
Implement a minimum set of embedded operations on the vehicle to make it more resilient to
the nuances of managing connectivity and communication to AWS control plane.

The vehicle must be able to operate without internet connectivity. You must implement
robust operations in your vehicle firmware and software to provide the basic capabilities.
Store important messages durably offline and, once reconnected, send those messages to the
AWS control plane. Implement exponential retry and back-off logic when connection attempts
fail.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/foundations.html*

---

# Change management

At any OEM, connected mobility landscape is continuously
evolving with new use cases and implementation patterns. On
the vehicle side, the number of sensors collecting data have
been rapidly multiplying. This results in refactoring and
rewrite of some of the processing logic that feeds the vehicle
data platform and enables deriving of insights. Thus, there is
greater need to have streamlined processes that introduce and
manage change in your environment. But based on the use cases,
application, and infrastructure, the run-books and deployment
strategies vary. These changes to the workloads and
environment should be anticipated, monitored, accommodated and
carefully executed for reliability of the connected mobility
platform.

## Monitor workload resources

CMREL_6: Are you monitoring all components of the workloads, including
vehicle-based units?

**[CMREL_BP6.1] Monitor what matters.**

Observability is understanding the working of the system
based on the telemetry that the system emits. A recommended
approach is to implement a Vehicle Network Operations Center
(V-NOC) which is an intelligent observability system that is
aware of the health of the systems running in the vehicle,
the backend systems supporting the platform and the
applications that are user facing. It is essential to
monitor all components of the workloads including
vehicle-based units.

Generally, a Connected Mobility platform has several
integrations with internal and external systems. Any system
change that can impact the interfacing message contracts
needs deep dive impact analysis. Enable the observability on
these integrations for quicker troubleshooting, failure
analysis and performance profiling.

Vehicle based telematic units should have health monitoring
and data transmission mechanism that can relay the state of
systems in near real time when connection is available or
ship buffered logs when connectivity is restored.

**Prescriptive guidance:**

AWS provides native monitoring, logging, alarming, and dashboards with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and tracing through [AWS X-Ray](https://aws.amazon.com/xray/). When deployed together, they provide
the three pillars (metrics, logs, and traces) of an observability solution. AWS services
such as Amazon CloudWatch apply statistical and machine learning algorithms to continually analyze
metrics of systems and applications, determine normal baselines, and surface anomalies
with minimal user intervention. Anomaly detection algorithms account for the seasonality
and trend changes of metrics.

If the preference is for open-source based managed
services [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/)
and [Amazon Managed Grafana](https://aws.amazon.com/grafana/) are two such services providing
additional options for customers to choose from. AWS also
launched [AWS Distro for OpenTelemetry (ADOT)](https://aws-otel.github.io/) - a secure,
production-ready, AWS-supported distribution of the
OpenTelemetry project. Part of the Cloud Native Computing
Foundation, OpenTelemetry provides open-source APIs,
libraries, and agents to collect distributed traces and
metrics for application monitoring. With AWS Distro for
OpenTelemetry, you can instrument your applications just
once to send correlated metrics and traces to multiple AWS
and Partner monitoring solutions.

It is important to be aware of end-to-end functioning of all
endpoints that implement the connected mobility use
cases. This active monitoring can be done with synthetic
transactions which periodically run a number of common tasks
matching actions performed by clients of the workload. You
can also combine the synthetic canary client nodes with AWS X-Ray console to pinpoint which synthetic canaries are
experiencing issues with errors, faults, or throttling rates
for the selected time frame.

In all cases, tool interoperability and extensibility are an
important consideration in observability.

CMREL_7: Are your connected mobility logs from various systems lacking the
correct level of information?

**[CMREL_BP7.1] Log interpretation and context
propagation**

Considering the number of systems and services supporting a
connected mobility setup, it is important to collect logs
into a centralized store. But all log entries are not equal,
in addition the logs may be too verbose or lacking right
level of info that can be used in correlation. A system that
enables the filtering of logs based on prefixes would reduce
the amount of data that is retained and processed for
insights. A processing / transformation engine is needed to
make the logs more usable or to enrich the log entries with
additional information that can be used later for better
correlation.

As connected mobility platforms result in high volume log
generation, a system that simplify the searching, querying
and visualizing of the logs in different ways based on need
is recommended.

An ideal NOC should have capability to create dashboards,
reports, and allow dynamic querying capability. Considering
the mix of systems that are on-board and off-board the log
entries may have sensitive information like location of the
vehicle. Securing the logs
with [encryption
at rest](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/encrypt-log-data-kms.html), auditing and
[masking
sensitive data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) in logs is required for
[compliance
validation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/compliance-validation.html).

**Prescriptive guidance:**

CloudWatch Logs enables you to centralize the logs from all
of connected mobility systems, applications, and AWS
services that you use, in a single, highly scalable service.
You can then easily view them,
[live-tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html),
search them for specific error codes or patterns, filter
them based on specific fields, or archive them securely for
future analysis. CloudWatch Logs enables you to see all of
your logs, regardless of their source, as a single and
consistent flow of events ordered by time.

[CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) enables querying your logs with a
powerful query language, visualizing log data and adding
them to dashboard.

The filtering of the logs can be done using CloudWatch logs
subscription filters that can have four different target
services: [Kinesis
Data Streams, AWS Lambda, Amazon Data Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/SubscriptionFilters.html) and
[Amazon OpenSearch Service](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_OpenSearch_Stream.html)

For a list of AWS services that publish logs to CloudWatch Logs, see the [CloudWatch
documentation.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/aws-services-sending-logs.html)

Some AWS services can directly write logs to other
destinations

Log type

[CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-CWL)

[Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-S3)

[Firehose](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-Firehose)

[CloudFront:
access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html)

✓

[CloudWatch
Evidently evaluation event logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-datastorage.html#CloudWatch-Evidently-datastorage-logformat)

✓

✓

[Amazon ElastiCache (Redis OSS) logs](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Log_Delivery.html)

✓

✓

[AWS Global Accelerator flow logs](https://docs.aws.amazon.com/global-accelerator/latest/dg/monitoring-global-accelerator.flow-logs.html)

✓

[Amazon MSK broker logs](https://docs.aws.amazon.com/msk/latest/developerguide/msk-logging.html)

✓

✓

✓

[Amazon MSK Connect logs](https://docs.aws.amazon.com/msk/latest/developerguide/msk-connect-logging.html)

✓

✓

✓

[AWS Network Firewall logs](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-logging.html)

✓

✓

✓

[Network
Load Balancer access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html)

✓

[Amazon
Route 53 resolver query logs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-query-logs-choosing-target-resource.html)

✓

✓

✓

[EC2
Spot Instance data feed files](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html)

✓

[Amazon Virtual Private Cloud flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-s3.html)

✓

✓

[Amazon VPC Lattice access logs](https://docs.aws.amazon.com/vpc-lattice/latest/ug/monitoring-access-logs.html)

✓

✓

✓

[AWS WAF logs](https://docs.aws.amazon.com/waf/latest/developerguide/logging-destinations.html)

✓

✓

✓

CMREL_8: Is your metric collection aligned with a business outcome?

**[CMREL_BP8.1] Define and calculate metrics (Aggregation)**

Metric collection should always begin with an objective or business outcome.
Defining metrics that are business outcome linked will result in quicker response from the
system and teams supporting it than the generic metrics. As an OEM you are aware of
regular pattern or trend for certain metrics in your system. For example, a critical KPI
could be the number of remote start commands executed on the vehicles across various hours
of the day. Generally, the count is higher in the morning and evenings which changes
across time zones and seasons. With the release of a new version of the services that
process such requests if the traffic has anomaly, it should get reflected on dashboard as
an issue. Aggregations should be available on that metric to determine the severity of the
impact.

**Prescriptive guidance:**

You can create metric filters to match terms in your log events and convert log
data into metrics. When a metric filter matches a term, it increments the metric's count.
For example, on release of a new firmware you can create a metric filter that counts the
number of times the word `ECU_Connected` occurs in your log events. You can
assign units and dimensions to metrics. For example, if you create a metric filter that
counts the number of times the word `ECU_Connected` occurs in your log events,
you can specify a dimension that's called `ECUConnectionCount` to show the
total number of log events that contain the word `ECU_Connected` and filter
data by reported firmware version.

CMREL_9: Does your connected mobility network operations center (NOC) have
the correct level of searchability and interactivity?

**[CMREL_BP9.1] Real-time processing and alarming with notifications
and automated response**

Some OEMs may have existing processes and tools for alarming, trouble tracking and
automated response. For better visibility across the organization, the Vehicle-NOC should
be integrated with these systems. With thousands to millions of vehicles connecting to the
platform the number of data points can be too many so having an intelligent system that
can reduce noise by finding pattern across various issues can boost productivity and
reduce mean time to resolve (MTTR). Typically, such intelligent systems also reduce the
number of repeat notifications for same issue.

**Prescriptive guidance:**

Alerts can be sent to Amazon Simple Notification Service
(Amazon SNS) topics, and then pushed to any number of
subscribers. For example, Amazon SNS can forward alerts to
an email alias or messaging channel so that technical staff
can respond.

When you enable
[anomaly
detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html) for a metric, CloudWatch applies
statistical and machine learning algorithms. These
algorithms continuously analyze metrics of systems and
applications, determine normal baselines, and surface
anomalies with minimal user intervention. In addition,
anomaly detection on metric math is a feature that you can
use to create
[anomaly
detection alarms on the output metric math
expressions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-alarm-on-metric-math-expression.html).

## Design your workload to adapt to changes in demand

CMREL_10: How does your connected mobility workload adapt to vehicle traffic
demand on resources?

**[CMREL_BP10.1] Use automation when obtaining or scaling
resources**

**[CMREL_BP10.2] Scale resources reactively on impairment to
restore workload availability**

**[CMREL_BP10.3] Scale resources proactively to meet demand and avoid
availability impact**

Telemetry traffic from vehicle has patterns that vary based
upon various factors like time of the day, weather condition
during a day, season, geographic location. If the connected
mobility systems are scaling to meet the demand, automating
the process by using managed services will aid in better
control.

When you are automating for scaling it is important to know
the target utilization which generally based upon
observations of historic trends and extrapolating. In a
typical set up for connected mobility this may turn out to
be a complex task due to the typical mix of several
different services.

Another challenge is to monitor your connected mobility
applications / services as the capacity is added or removed
in real time as the demand changes. This will build
confidence to have right level of end user experience as the
workloads change periodically or unpredictably.

**Prescriptive guidance:**

The exact nature of the automation depends upon the type of
services that are supporting the landscape. Managed services
like AWS Lambda, Amazon S3, Amazon CloudFront and others
scale automatically based upon the load condition. There may
be limitations imposed by the Service Quotas which need to
be taken into account.

Self-managed services like Amazon EC2 require careful planning to ensure that the load
distribution meets the requirements for the business function. The automation should
ensure that the instance returns to the state that it is expected to be in to handle the
traffic. Automation is vital to efficient DevOps, and getting your fleets of Amazon EC2
instances to launch, provision software, and self-heal automatically is a key challenge.
[Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/features/) provides
essential features for each of these instance lifecycle automation steps. Use [load
balancers](https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html) to distribute the traffic across the instances and [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-types.html) to provide flexibility in cloud service configuration without impacting
the ECU based client applications.

To make the scaling experience better and simple AWS launched [predictive scaling policies](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/), which uses machine learning to analyze each
resource's historical workload and regularly forecasts the future load for the next two
days. To bring about wider level of control, in 2023, the forecast and scaling were
decoupled so that you could get forecasting which is prescriptive in nature as compared to
forecast and scaling. Predictive scaling can be used for applications where demand changes
rapidly but with a recurring pattern.

Automotive companies generally use the AWS managed services
to reduce the overheads of administrating the infrastructure
and let AWS handle the undifferentiated heavy lifting.
Configuring these managed services
is [Customer's
responsibility](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/the-shared-responsibility-model.html). But considering the varied nature of
these services, configuring them for auto-scaling and with
cohesiveness becomes challenging very quickly. Thus, even in
this case, you need a service that orchestrates the
auto-scaling across the workload. With
[Application
Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html), you can configure automatic scaling for
the various resources beyond Amazon EC2.

**[CMREL_BP10.4] Load and stress test your workload**

Having followed the best practices above it is important to
test if the scaling activities meet the requirements of
connected mobility functions. Stress testing the platform
would reveal the robustness of various connected mobility
functions under extreme load conditions. Some use cases may
deserve higher level of robustness than others due to
various business and compliance reasons. The load testing
frameworks should have the ability to execute various
testing strategies with varied traffic patterns that cover
both the regular business as usual cases and the corner
cases of failure and subsequent recovery. Considering the
agility and cost optimization that AWS cloud computing
provides, setting up of stage environments for load testing
should be less time, money and effort intensive. While load
testing in the stage environment should be done, training
the teams to handle such events in production environment is
also a must-do activity.

**Prescriptive guidance:**

[Distributed
load testing](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) can help load test the applications and
determine the bottlenecks before releasing to production.
The framework can simulate thousands of connected vehicle
applications and generate traffic patterns to uncover
issues. The systems can be tested using simple get requests
or for higher level of customization you can
create [JMeter
scripts](https://jmeter.apache.org/).

[Game
Days](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.gameday.en.html) can simulate a failure or event to test systems,
processes, and team's responses.

## Implement change

CMREL_11: How are you controlling the changes that are deployed?

The number of features and scenarios that are supported by connected mobility
platform have been growing rapidly. It is recommended to control the impact of these
changes while deploying new functions.

**[CMREL_BP11.1] Use runbooks for standard activities such as
deployment**

Vehicles which are connected to the backend are generally
operating in various geographies and time zones. It is
important to plan the change activities at a time that can
cause least disruption to the services. The documentation
should be less verbose and specific to conducting the tasks.
The execution of the steps should be controlled by right
level of authorizations that requires approvals and has
appropriate reason captured. Unauthorized changes can result
in downtime in the connectivity of vehicles to backend.  It
is important to track the changes that were implemented so
that the deployment rollbacks can be analyzed for integrity.

**Prescriptive guidance:**

Runbooks provide an excellent mechanism to communicate the actions that can be
performed with minimum information. The change activities are generally audited and can be
rolled back to the previous version. AWS Config performs compliance checks based on these
rules, and Audit Manager reports the results as compliance check evidence.

**Resources:**

[Using
AWS Config managed rules with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-managed-rules)

[Using
AWS Config custom rules with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-custom-rules)

[Troubleshooting
AWS Config integration with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-rules-troubleshoot)

**[CMREL_BP11.2] Integrate functional and resilience testing as
part of your deployment**

Functional and resilience tests should be part of automated
deployment. If success criteria are not met, the pipeline is
halted or rolled back. These tests are run in a stage
environment and done as part of a deployment pipeline.

**Prescriptive guidance:**

Vehicle owners or the related systems can take different functional paths while
using the connected services. It is important to track such paths and simulate them in
steps using services like [Amazon CloudWatch Synthetic
monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html). As a bonus this also reveals the uptime of the services.

[Chaos
engineering](https://principlesofchaos.org/) with
[AWS Fault Injection Service](https://aws.amazon.com/fis/) can be used to build confidence
in the system's ability to survive certain corner cases. To
execute such tests many of the principles discussed above
are applicable- determining the target state, run
experiments in production and automation.

**Resources:**

**Videos:**

[AWS re:Invent 2022 - Building confidence through chaos
engineering on AWS](https://www.youtube.com/watch?v=tm5GEePP1PY)

**[CMREL_BP11.3] Use a canary or blue/green deployment when
deploying applications in immutable infrastructures**

The operational complexity of the connected mobility
platform builds up with the numerous distributed services
that support various scenarios. Release cycles, patching,
monitoring the changes all result in overhead that is
difficult to manage and error prone. Offboard teams begin to
delay the release of changes to avoid disruptions in
availability of services. A solution to this problem is to
have immutable infrastructure, where infrastructure is not
updated or fixed rather it is replaced.

**Prescriptive guidance:**

[Canary release](https://martinfowler.com/bliki/CanaryRelease.html)
and [Blue/green
deployment](https://martinfowler.com/bliki/BlueGreenDeployment.html) approaches are recommended for deployments into the immutable
infrastructure.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/change-management.html*

---

# Failure management

"Everything fails, all the time"

[Werner Vogels, CTO - Amazon.com](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html)

Connected mobility platforms have been evolving over the years
and the relative pace has been more than any time in past few
decades. There has been an equally growing concern about
vehicle safety with the technology in vehicle, the data
generated and the backend supporting the platform. With the
growing complexity, system failures are highly probable. While
failures are difficult to predict, reliability requires that
the systems are aware of the failures and react accordingly to
avoid impact on availability. Building and deploying robust
systems should be the target state of every automotive
company.

## Back up data

CMREL_12: How do your strategy and mechanisms manage failures to prevent
impact on your workload?

**[CMREL_BP12.1] Identify and back up all data that needs to be
backed up, or reproduce the data from sources**

**[CMREL_BP12.2] Perform data backup automatically**

While there might be *n* data sources that the
connected mobility platforms have to integrate with, not all data is equally important.
It's essential that data entities are classified and criticality determined. This helps
with making right strategic decisions for data recovery based on RPO, that is either
backing up the data or reproduce it. In some of the connected mobility use cases like
emergency-call or breakdown-calls, where compliance is critical the balance has to be
adequate. Classifying data also helps in determining the retention periods for various
data entities, one of the primary drivers for cost optimization.

**Prescriptive guidance:**

Backup capabilities are available with all AWS data sources. Some services
provide additional features such as point-in-time-recovery (PITR), continuous replication
and cross Region copy. With the growing number of services, managing backup configurations
can add to the overhead. Tools such as [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) and [AWS Elastic Data Recovery](https://aws.amazon.com/disaster-recovery/) can boost
the productivity, availability and have a RPO in seconds.

Automotive companies generally have variations hybrid infrastructure setup with
systems running on cloud and on-premises data centers. AWS services such as [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html) or [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) can help in
these deployment modes.

**[CMREL_BP12.3] Secure and encrypt backups**

"Encrypt Everything."

[Werner Vogels, CTO - Amazon.com](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html)

Safeguard the backups just as you secure the vehicle data.
Securing access to the data with right level of permissions
prevents tampering. Encrypt the backups so that the data
cannot be accessed in case of an accidental leak.

**Prescriptive guidance:**

Use AWS Identity and Access Management (IAM) to create
[roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
and
[policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
that have least
[privileged
access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_permissions_least_privileges.html). Use AWS
[managed
policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html) where applicable. As more connected vehicles
are rolled out, the volume of vehicle data that is hosted in
vehicle data lakes keeps growing exponentially. Considering
that S3 is the most popular data store for vehicle data
lakes, following
[the
best practices](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/securing-protecting-managing-data.html) in handling this data is essential.

Ensure the backups are not accidentally deleted as this
could result in vehicle regulatory compliance violations.
[Legal
hold](https://docs.aws.amazon.com/aws-backup/latest/devguide/legalhold.html) is a feature in AWS Backup service that prevents
accidental deletions. Multiple departments/ units within an
organization can have their holds on the backup.

**[CMREL_BP12.4] Perform periodic recovery of the data to verify
backup integrity and processes**

"Hope for the best and be prepared for the worst" - [Maya
Angelou](https://www.womenshistory.org/education-resources/biographies/maya-angelou)

With backups configured, an equal effort is needed in
validating with recovery test whether the backups
meet Recovery Time Objectives (RTO) and Recovery Point
Objectives (RPO). This exercise should be repeated
periodically using well-defined mechanisms to ensure that
the data is recovered within RTO and with expected data loss
as established in RPO.

**Prescriptive guidance:**

Testing the restores build confidence in the system and trains teams to handle the
disaster situations better. There are various features in AWS services that aid in
testing the restores and assess RTO and RPO. Amazon RDS and DynamoDB have allow point-in-time
recovery (PITR). AWS Elastic Disaster Recovery offers continual point-in-time recovery
snapshots of Amazon EBS volumes.

## Use fault isolation

The architecture should ensure that there isn't any single
point of failure. Systems should be resilient enough to
handle the partial or complete failure of the infrastructure
stack. Fault isolated boundaries limit the effect of a
failure within a workload to a limited number of components.
Components outside of the boundary are unaffected by the
failure. Using multiple fault isolated boundaries, you can
limit the impact on your workload.

CMREL_13: How do you ensure that you don't have a single point of failure?

**[CMREL_BP13.1] Deploy the workload to multiple locations**

To ensure high availability and prevent a single point of failure, the services
should be deployed as diverse as required. The system should rely on redundant components
that are decoupled from each other.

**Prescriptive guidance:**

A typical connected mobility set up consists of several
distributed systems which creates an ideal condition to
spread out and isolate.
[Multi-AZ](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/availability-zones.html)
solutions are a must for most of the connected mobility use
cases. Multi-region though ideal but may be cost prohibitive
for wider scope so should be done selectively where
required. A multi-Region approach is common for disaster
recovery strategies to meet recovery objectives when one-off
large-scale events occur.
[AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) can be used to deploy workloads closer to
vehicles for low-latency requirements.

In certain cases, vehicles can communicate with edge
locations rather than the cloud regions. This deployment
pattern is more relevant in case of low latency
requirements. Static content can be delivered to end user
from
[Amazon CloudFront](https://aws.amazon.com/cloudfront/) with millisecond level latency. Other
services that also enable edge computing include
[AWS Global Accelerator](https://aws.amazon.com/global-accelerator/),
[Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html), and Lambda@Edge. Amazon CloudFront can
scale automatically to deliver software with over-the-air
(OTA) updates at scale with high transfer rates.

Evaluate AWS Outposts for your workload. If your workload
requires low latency to your on-premises data center or has
local data processing requirements such as in case of plant
systems. Then run AWS infrastructure and services on
premises using
[AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/failure-management.html*

---

# Key AWS services

Refer to [Appendix A: Designed-For Availability for Select AWS Services](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/appendix-a-designed-for-availability-for-select-aws-services.html) in the Reliability
Pillar whitepaper.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/key-aws-services-rel.html*

---

# Resources

## Change management

**Hands-on labs:**

- [One
Observability Workshop](https://catalog.workshops.aws/observability/en-US)
- [Viewing
Amazon CloudWatch metrics with Amazon Managed Service for Prometheus and Amazon Managed Grafana](https://aws.amazon.com/blogs/mt/viewing-amazon-cloudwatch-metrics-with-amazon-managed-service-for-prometheus-and-amazon-managed-grafana/)

**Reference architecture:**

- [Guidance for Deep Application Observability on AWS](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/deep-application-observability-on-AWS.pdf)

**Videos:**

- [AWS Summit SF 2022 - Full-stack observability and application
monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0)
- [AWS Cloud Operations - How to](https://www.youtube.com/playlist?list=PLhr1KZpdzukdbisTs-Eskg4xsfLFOki1T)
- [Publishing
custom metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [Comprehensive
observability for Amazon EKS](https://aws.amazon.com/blogs/mt/announcing-aws-observability-accelerator-to-configure-comprehensive-observability-for-amazon-eks/)

**Monitoring tools:**

- [AWS Observability Services](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-observability-tools.html)
- [AWS observability repositories](https://github.com/aws-observability)

**Workload load and stress testing tools:**

- [Taurus](https://gettaurus.org/)
- [Apache
JMeter](https://jmeter.apache.org/)

**Blogs:**

- [Ensure
Optimal Application Performance with Distributed Load
Testing on AWS](https://aws.amazon.com/blogs/architecture/ensure-optimal-application-performance-with-distributed-load-testing-on-aws/)

**Guides:**

- [Amazon EC2 Auto Scaling now gives recommendations about activating
predictive scaling policy](https://aws.amazon.com/about-aws/whats-new/2023/01/amazon-ec2-auto-scaling-activating-predictive-scaling-policy/)
- [Step
and simple scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html)
- [Target
tracking scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Scheduled
scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html)
- [AWS services that you can use with Application Auto
Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html)
- [Using
AWS Config managed rules with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-managed-rules)
- [Using
AWS Config custom rules with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-custom-rules)
- [Troubleshooting
AWS Config integration with Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/control-data-sources-config.html#aws-config-rules-troubleshoot)
- [Distributed
Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

**Amazon Builders' Library:**

- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)

## Failure management

**Reference architecture:**

- [Data
Protection Reference Architecture with AWS Backup](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/data-protection-with-aws-backup-ra.pdf?stod_bck4)

**Blogs:**

- [Best
practices for data lake protection with AWS Backup](https://aws.amazon.com/blogs/storage/best-practices-for-data-lake-protection-with-aws-backup/)

**Guides:**

- [Automating
backups with Backup plan](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)
- [Point-in-time
recovery for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.html)
- [Feature
availability by resource](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-resource)
- [Feature
availability by AWS Region](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html#features-by-region)
- [Security
best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [Legal
hold](https://docs.aws.amazon.com/aws-backup/latest/devguide/legalhold.html)
- [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html)
- [Audit
backups and create reports with AWS Backup Audit
Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html)
- [What Is
AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Data
protection in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/data-protection.html)
- [Encryption
for backups in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html)
- [Reliability Pillar: AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)

**Infrastructure map:**

- [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

**Videos:**

- [AWS Summit ANZ 2021 - Everything fails, all the time: Designing
for resilience](https://www.youtube.com/watch?v=wUzSeSfu1XA)

**Whitepapers:**

- [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html)
- [Choose
the right Amazon RDS deployment option: Single-AZ instance,
Multi-AZ instance, or Multi-AZ database cluster](https://aws.amazon.com/blogs/database/choose-the-right-amazon-rds-deployment-option-single-az-instance-multi-az-instance-or-multi-az-database-cluster/)
- [AWS Auto Scaling: How Scaling Plans Work](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html)
- [Implementing
Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/introduction.html)
- [Disaster
Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)

**Workshops:**

- [AWS Well-Architected Reliability Labs](https://wellarchitectedlabs.com/Reliability/)
- [Advanced
Multi-AZ Resilience Patterns](https://catalog.workshops.aws/multi-az-gray-failures/en-US/workshop-overview)
- [Level
200: Testing Backup and Restore of Data](https://wellarchitectedlabs.com/reliability/200_labs/200_testing_backup_and_restore_of_data/)

**AWS Builders' Library:**

- [The
Amazon Builders' Library: How Amazon builds and operates
software](https://aws.amazon.com/builders-library/)

**Books:**

- Robert S. Hammer, *[Patterns for Fault Tolerant Software](https://www.amazon.com/Patterns-Fault-Tolerant-Software-Wiley-ebook/dp/B00DXK33SK/)*
- Andrew Tanenbaum and Marten van Steen, *[Distributed Systems: Principles and Paradigms](https://www.amazon.com/Distributed-Systems-Principles-Paradigms-2nd/dp/0132392275/)*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/resources-rel.html*

---
