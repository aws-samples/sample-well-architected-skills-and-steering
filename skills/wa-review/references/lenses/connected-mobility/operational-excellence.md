# Operational excellence

**Pages**: 7

---

# Design principles

The following are design principles for operational excellence
in the cloud:

- Based on the workload and your business objectives, identify connected mobility key
performance indicators (KPIs). The connected mobility KPIs should be linked to metrics
from all layers: business, application, data, security, and infrastructure. Once
identified, use the connected mobility KPIs to work backwards and identify operational
KPIs.
- Implement end-to-end observability and a single pane view of the connected mobility
workload status from vehicle to the cloud and full stack of the application: Proactively
monitor end user experience in-vehicle.
- Develop a testing framework to simulate production-like conditions: Site
Reliability Engineering (SRE) team are responsible for reliability of the application
amidst frequent updates from development teams. The SRE team works closely with the
development team to create new features and stabilize production systems. One of the
challenges faced by the SRE team is to simulate the vehicle while trying to test or debug
a connected mobility feature or a production issue. Develop a virtual vehicle in the cloud
that has capability to simulate various real-world conditions including load and Mobile
Network Operator (MNO) failures.
- Implement mechanisms to improve developer productivity enabling reduction in Time
to Market (TTM), which is the time it takes to take connected mobility features from
concept to launching it in the industry. Develop deployment templates and provide a
developer portal to quickly spin up new development and lab environments.
- Implement a multi-stakeholder runbook to effectively respond to production events.
Connected mobility is a complex system with multiple stakeholders from end users to Mobile
Network Operators, cloud hyperscalers, downstream data consumers, and OEMs. To reduce the
Mean Time to Restore (MTTR), a runbook should be developed for all critical events.
Eventually, automate runbooks to streamline operational processes, reduce human error, and
improve efficiency, leading to faster incident resolution and enhanced operational
excellence.

## Definitions

**Observability:** Observability allows users to understand a
system's state from its external output and take (corrective) action. Observable systems
yield meaningful, actionable data to their operators, allowing them to achieve favorable
outcomes (faster incident response, increased developer productivity) and less toil and
downtime.

Best practices implementing observability include:

- **Monitor what matters:** Start with the connected
mobility business key performance indicators (KPIs) and work backwards to the application
and infrastructure metrics.
- **Collect telemetry from all layers:** Connected mobility
has dependencies and interactions with vehicles, Mobile Network Operators, cloud
providers, internet service providers, AWS Partners, and other components—both within
and outside your control—that can impact your business outcomes. It is important that you
have a holistic view of your entire workload.
- **Propagate context:** Collect logs, metrics, and traces,
and propagate transaction IDs, which helps to perform correlation, analysis, anomaly
detection, dashboarding, and alarms.

**Leading versus lagging indicators:** Leading indicators are
metrics that are used to measure future performance. For example, customer satisfaction and
connected mobility feature usage metrics can be used to predict renewal rates, as a happy and
engaged customer is more likely to renew the paid subscription. Similarly, quality metrics of
the feature releases can be a leading indicator to predict the failure rate of the
system.

Lagging indicators are metrics used to measure past performance for example connected
mobility subscription renewal rates, Mean Time Between Failures (MTBF), and remote command
latency. Lagging indicators provide valuable feedback on the effectiveness of past decisions
and help identify areas for improvement. Both leading and lagging indicators are important for
managing and measuring operational efficiency of connected mobility workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/design-principles-ops.html*

---

# Organization

There are no best practices specific to this area for connected mobility.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/organization.html*

---

# Prepare

CMOPS_1: How do you define the meaningful monitoring KPIs and metrics of your
connected mobility platform?

Connected mobility platforms handle millions of vehicles and end users, and billions
of messages being generated. The scale and distributed nature of connected mobility
platforms create unique challenges for monitoring. Defining the critical KPIs and metrics is
a key step of your monitoring strategy, and should include end user mobile applications,
vehicles, mobile cellular networks, and cloud infrastructure. Consider starting with the
benefits that the connected mobility platform provides to its end users and work backwards
to identify KPIs and metrics, which are leading and lagging indicators of success.

**[CMOPS_BP1.1] Define end-to-end KPIs and metrics for a
connected mobility platform.**

Collecting key metrics, logs, and trace information from all parts of your connected
mobility platform will give you end to end visibility across the solution. It can decrease
the Mean Time to Detect (MTTD), Mean Time to Repair (MTTR), and Mean Time to Restore Service
(MTRS) by allowing you to detect issues quickly, and troubleshoot and debug with precision.
It can also help you recognizing trends before critical issues occur.

Define KPIs that include business, application, and
infrastructure across the solution. Start this process by
creating a working team that includes stakeholders from
various teams including business teams. Start by defining
business KPIs, and then supporting KPIs for the application
and infrastructure. These KPIs should be mapped to the metrics
collected from tools such as
[AWS CloudWatch](https://aws.amazon.com/cloudwatch/), which helps to observe resources in AWS,
on-premises, and in other clouds. Some sample KPIs are as
follows:

**Business KPIs:**

- Metrics from end user mobile app including the number of remote commands issued,
errors running remote commands, remote command latency, errors from user portals, and
errors from infotainment systems.
- Mobile network Quality of Service (QoS) metrics such as
packet loss, latency, jitter, and interference.
- Vehicle health indicators such as diagnostic codes,
battery health, fuel efficiency, and repair and
maintenance data.
- Vehicle security metrics such as the number of
unauthorized requests to high-risk ECUs and vehicle
disconnected duration metric.

**Application KPIs:**

- Number of transaction failures, application errors, and
number of retries for key services.
- Response times to and from vehicle, and latency across the
application and in critical functions.
- Health checks for critical features and functions of the
application.
- Database metrics such as query response times, number of
connections, and IOPS metrics.

**Infrastructure KPIs:**

- Usage metrics that include CPU, Memory, Storage, and
Network for critical connected mobility infrastructure.
These metrics play a crucial role in proactive
infrastructure management, optimizing resource allocation,
and enhancing the overall user experience of Connected
Mobility.
- Service quota metrics to enable proactive service quota management and avoid
downtime due to reaching a service quota. Effective quota management prevents connected
mobility service disruption.
- Security metrics including unpatched instances, security
vulnerabilities, security events, and non-compliant
resources. These metrics help assessing security status,
make informed decisions, and prioritize actions to
mitigate risks.
- Cloud specific metrics for key services. As an example, [AWS Lambda](https://aws.amazon.com/lambda/) is commonly used as part of connected mobility
implementations on AWS. Key Lambda metrics include number of invocations, number of
errors, number of retries, number of invocations that were throttled, and duration of
function processing. These metrics play a vital role in preventing and addressing
various issues that can affect the reliability and performance of your connected mobility
platform.

CMOPS_2: How do you observe the health of your connected mobility platform and
proactively identify anomalies?

The connected mobility platform includes the vehicle edge, connectivity, cloud-based
infrastructure and applications, enables various services like fleet management, remote
diagnostics, and predictive maintenance. Implementing observability enables insights about
end-to-end system health, availability, performance, and scalability, which in turn helps
reduces the time to restore the service after a disruption.

By monitoring metrics such as response times, resource utilization, and error rates, the
customer can identify potential bottlenecks or issues that may impact the overall
performance of the system. This allows for proactive measures to be taken, such as scaling
up resources or optimizing the platform's architecture, to provide uninterrupted service
delivery.

Monitoring the health of edge devices is crucial because these devices form the backbone
of connected mobility. Edge devices, such as vehicle telematics units or sensors, collect
and transmit data to the cloud for analysis and are typically used for decision-making. By
continuously monitoring their health, you can detect any anomalies, performance degradation,
or malfunctions in real-time and provide timely interventions.

Observability of connected mobility platforms requires that the data from all the
subsystems and microservices are aggregated in a data lake, there is a capability to
correlate the records, and dive deep to identify the root cause of the issue.

**[CMOPS_BP2.1] Implement an observability data lake that aggregates
telemetry from all connected mobility components.**

Validate that all components of the connected mobility platform are able to send the
telemetry data (logs, traces, and metrics) to the observability data lake. Implement
transaction correlation IDs in those records to trace the transaction across multiple
services.

To investigate intermittent errors in a set of vehicles, it requires a capability to
activate debug level logging inside the vehicle. These logs can help the operations team to
replay transactions in a test environment and also debug the root cause of the errors in
production. As the data loggers will generate a lot of data, this capability should be
enabled only during an event. Implement a log and trace framework, based on the standard
defined by the [AUTOSAR 4 DLT](https://www.autosar.org/fileadmin/standards/R22-11/CP/AUTOSAR_SWS_DiagnosticLogAndTrace.pdf). The end user also should be able to enable this through a
diagnostic app in the infotainment screen to assist the troubleshooting with the service
engineer.

The logs can then be transferred to the cloud using [AWS IoT Core](https://aws.amazon.com/iot-core/) where the AWS IoT rules engine can be used to upload
in-vehicle log records to Amazon CloudWatch. You can also upload the log records using [Amazon S3](https://aws.amazon.com/s3/) pre-signed URLs if the MQTT publish payload is
more than 256 MB. The connected mobility platform should have a capability to import these
logs into vehicle simulators in the cloud to replay these transactions in non-production
environments

Implement an observability data pipeline to orchestrate and automate data processing
workflows, ensuring seamless ingestion and transformation of observability data.

**[CMOPS_BP2.2] Set up real-time monitoring and alerting
capabilities to detect anomalies promptly.**

Use Amazon CloudWatch to store logs and to monitor key metrics such as vehicle status,
telemetry, or network connectivity. Use [AWS Glue](https://aws.amazon.com/glue/) to transform and analyze the log data using services like [Amazon Athena](https://aws.amazon.com/athena/) or [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/). Implement custom log analysis solutions or use [AWS Partner Network](https://aws.amazon.com/partners/) offerings for advanced log analytics.
When predefined thresholds or anomalies are detected, CloudWatch Alarms can cause notifications
via [Amazon Simple Notification Service](https://aws.amazon.com/sns/) (Amazon SNS) or perform automated
actions using [AWS Lambda](https://aws.amazon.com/lambda/) functions.

Implement AWS Lambda functions to process and analyze streaming data from the edge
devices in near real-time, triggering alerts or notifications based on predefined
thresholds. By leveraging Lambda, you can apply custom logic or machine learning models to
the incoming observability data, enabling real-time anomaly detection and triggering alerts
or notifications based on specific conditions.

Perform synthetic transaction monitoring that simulates the typical end user journey.
The synthetic transaction agents should be deployed in various geographical locations, which
periodically sends test transactions to the connected mobility services deployed in the
cloud. Implement a vehicle health monitoring agent solution as per [AUTOSAR](https://www.autosar.org/fileadmin/standards/R21-11/FO/AUTOSAR_EXP_SystemHealthMonitoring.pdf) to monitor the vehicle to cloud communication. If the monitoring detects
any issues, such as a breach in a performance threshold or any error, it will alert the
operations team.

**[CMOPS_BP2.3] Implement predictive analytics and proactive
operations.**

To improve operations and detection of patterns in the cloud, predictive analytics
and proactive operations play a significant role in avoiding costly downtimes. By using
predictive analytics, historical data is analyzed to identify patterns and trends that can
predict potential component failures. This enables proactive maintenance scheduling,
reducing the risk of unexpected downtime. Machine learning (ML) models can be trained on
historical data, allowing for accurate predictions. Applying predictive analytics algorithms
helps generate insights and optimize maintenance planning.

For the application stack in the cloud, use an ML service like [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/) to detect abnormal operating patterns to identify
operational issues. You can extend predictive capability by developing ML algorithms using a
service like [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) and leveraging an
observability data lake. This insight can be used by the solution to automatically recommend
remedial actions and runbooks to restore the service

In a connected mobility platform, the most challenging aspect is debugging vehicle to
cloud communications. Following best practices can help you debug the in-vehicle connected
vehicle components remotely.

**[CMOPS_BP2.4] Implement robust remote diagnostic capabilities.**

To troubleshoot, robust remote diagnostic capabilities are essential. This entails
developing comprehensive diagnostic algorithms that can accurately identify potential
issues. Real-time data collected from in-vehicle system is continuously analyzed to detect
anomalies and raise timely alerts. By leveraging advanced ML techniques and cloud-based
analytics platforms, the diagnostic accuracy can be improved, enabling efficient
identification of problems.

Use services such as AWS IoT Core for near real-time diagnostic data ingestion and
processing. Use serverless functions such as AWS Lambda to develop diagnostic algorithms that can
analyze the events in real-time. This enables the diagnosis of complex patterns and the
generation of actionable insights.

**[CMOPS_BP2.5] Provide remote access for troubleshooting
purposes.**

Authorized support personnel can remotely access in-vehicle systems, which expedites the
troubleshooting process. However, it's crucial to implement secure communication protocols
to protect data privacy and prevent unauthorized access. Utilizing end user consent and
virtual private networks (VPNs) or encrypted remote access tools helps establish a secure
connection. Regularly auditing and updating access permissions further enhances security
while preventing unauthorized access. Follow the security best practices (CMSEC_6) for the
remote troubleshooting.

CMOPS_3: Have you set up a validation environment that has feature equality
with production environment of the connected mobility platform?

**[CMOPS_BP3.1] Validate the system in a non-production
environment that has feature equality with production.**

The connected mobility platform requires additional validation to incorporate
variability of network connectivity, external systems, in-vehicle components, model years of
vehicles and diverse environments that the vehicles are operated.

Use digital twin concepts to create a vehicle simulator to introduce common failure
scenarios and test subsystem behavior. Modularizing the digital twin model enables
additional subsystems to be added in the future. Leverage vehicle observability data
collected over time to generate machine learning models and perform predictive testing.
Create curated test dataset to test application logic, regression, and performance. Use
simulation tools (such as virtual ECUs) to test for scenarios throughout the
application/sub-system development lifecycle and to validate subsystem behavior.

Perform real world tests for connectivity (with different
hardware and network equipment/environment), security,
navigation, entertainment, data collection and analytics. Such
tests should be performed with hardware-in-loop using modular
test benches.

CMOPS_4: How do you do agile development of the connected mobility platform,
with a focus on minimizing disruptions?

**[CMOPS_BP4.1] Leverage microservices architecture for connected
mobility platform.**

The microservices architecture streamlines the development, deployment, scaling, and
maintenance of the entire connected mobility platform. For example, the remote commands
microservice, which is responsible for sending lock, unlock, and remote start commands to
the vehicle, can be independently scaled and deployed. This operation can be performed
separately from the vehicle diagnostic microservices, which send periodic vehicle diagnostic
reports to the end user. This architecture also enables each microservice to have different
disaster recovery (DR) strategies based on their individual recovery time objective (RTO)
and recovery point objective (RPO).

**[CMOPS_BP4.2] Implement API-first architecture to facilitate
the exchange of data and services while developing connected mobility platform.**

API operations help in agile development and faster feature-to-market in the context
of connected mobility software, it provides clear guidelines, enable modular development,
and support collaboration with external stakeholders. For example, automotive Original
Equipment Manufacturers (OEMs) deploy developer portals to crowdsource app development on
the connected mobility platform. These portals give secure access to the connected vehicle
platform through public API operations. Connected vehicle API operations could also be used
to securely share connected vehicle data to authorized repairers for compliance with Right
to Repair regulations. The API-first approach also helps to easily extend the platform to
support multiple model years of vehicles with backward compatibility as longs the API
contracts are maintained. It also reduces the impact of changes and reduces time to market
for new features without causing disruption to the connected mobility platform.

**[CMOPS_BP4.3] Implement DevOps automation.**

Incorporate DevOps automation to improve productivity, enhance developer experience,
and improve quality of the connected mobility feature releases. Implement a self-service
developer portal which provisions pattern-based software templates with preapproved
resources and configurations requiring limited manual intervention. Create connected
mobility platform templates in the developer portal that include opinionated pre-built
modules for observability and other connected mobility best practices baked in. Adopt
Continuous Integration/Continuous Deployment (CI/CD) pipelines to automate the testing and
deployment of the software updates, ensuring rapid and error-free releases. Automate
testing, to simulate scenarios and real-world conditions, helps validate the connected
mobility platform for safety and performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/prepare.html*

---

# Operate

CMOPS_5: How do you respond to an incident within your connected mobility
platform?

Responding to disruptions is an important aspect of operating your connected mobility platform as it impacts end user's ability to access critical features of their vehicle, may impact company revenue, and could erode customer trust. Understanding the scope of an outage, including which functions are affected, allows for timely and accurate communication with your customers and key business stakeholders, and minimizing your Mean Time to Repair (MTTR), and Mean Time to Restore Service (MTRS).

**[CMOPS_BP5.1] Determine the scope and impact of the incident to your
connected mobility platform.**

The connected mobility platform includes many functions, and understanding which functions
are affected, and the scale of impact is an important step to guide your response. An
example of a critical function is the ability for customers to use remote commands. Start by
analyzing your end-to-end monitoring dashboards for your connected mobility platform, review
reported incidents to your Service Desk, and determine the cause of the disruption. If it is
related to an AWS service event, find out if it is impacting a Region, or localized impact
to a specific Availability Zone. You can use the [Health Dashboard](https://health.aws.amazon.com/health/status) to get more detailed
information on AWS service specific events.

Reference your incident management playbook to investigate the appropriate process to initiate.
The runbook should guide your teams on communicating the disruption to your customers, include step by step instructions on
how to investigate the incident, remediation options, and how to validate recovery.

**[CMOPS_BP5.2] Communicate with customers about the incident in a
timely fashion.**

Connected mobility disruptions require effective communication for the safety of the users
and brand protection. The notification should be event driven and multi-channel, example
notify affected customers immediately through the customer's mobile app via push
notifications, SMS messages, and email about the issue. Provide clear and accurate
information about the problem, its cause, and the expected resolution time. Establish a
dedicated line for inbound customer queries. Communicate on the regular basis on progress.

**[CMOPS_BP5.3] Recover the application using runbooks and
automation.**

After identifying the issue, refer to the designated runbook for application recovery.
Following the runbook instructions, you might need to shift to an alternate Availability
Zone (AZ) if an AZ failed, or move to another Region in the case of a Region-wide failure.
For example, if a crucial business component, with low RTO and RPO requirements, experiences
a disruption, it is essential to refer to the disaster recovery runbook to facilitate the
transition of your application.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/operate.html*

---

# Evolve

There are no best practices specific to this area for connected mobility.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/evolve.html*

---

# Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS IoT Core](https://aws.amazon.com/iot-core/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon Athena](https://aws.amazon.com/athena/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/)
- [Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/key-aws-services-ops.html*

---

# Resources

**Documentation and blogs:**

- [How to get started with the new disconnected duration metric in AWS IoT Device Defender](https://aws.amazon.com/blogs/iot/how-to-get-started-with-the-new-disconnected-duration-metric-in-aws-iot-device-defender/)
- [Building an Automotive Embedded Linux Image for Edge and Cloud Using Arm-based Graviton
Instances, Yocto Project, and SOAFEE](https://aws.amazon.com/blogs/industries/building-an-automotive-embedded-linux-image-for-edge-using-arm-graviton-yocto-project-soafee/)
- [Using Digital Twins to Drive Electric Vehicle Battery Insights with MHP and
AWS](https://aws.amazon.com/blogs/apn/using-digital-twins-to-drive-electric-vehicle-battery-insights-with-mhp-and-aws/)
- [Build an observability solution using managed AWS services and the OpenTelemetry
standard](https://aws.amazon.com/blogs/mt/build-an-observability-solution-using-managed-aws-services-and-the-opentelemetry-standard/)
- [Monitoring your IoT fleet using CloudWatch](https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/)
- [Monitoring AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [What is Site Reliability Engineering (SRE)?](https://aws.amazon.com/what-is/sre/)
- [What is
observability? (AWS Observability Best Practices)](https://aws-observability.github.io/observability-best-practices/)
- [AUTOSAR_SWS_DiagnosticLogAndTrace](https://www.autosar.org/fileadmin/standards/R22-11/CP/AUTOSAR_SWS_DiagnosticLogAndTrace.pdf) (PDF)
- [AUTOSAR_EXP_SystemHealthMonitoring](https://www.autosar.org/fileadmin/standards/R21-11/FO/AUTOSAR_EXP_SystemHealthMonitoring.pdf) (PDF)
- [Diagnostic Log and Trace
daemon](https://github.com/COVESA/dlt-daemon#overview) (GitHub)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/resources-ops.html*

---
