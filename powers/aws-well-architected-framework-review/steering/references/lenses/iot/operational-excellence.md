# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 10

---

# IOTOPS01 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## IOTOPS01-BP01 Conduct an OT and IT cybersecurity risk assessment using a common framework

When taking advantage of IT technologies in OT environments, it
is important to conduct a cybersecurity risk assessment using
frameworks to fully understand and proactively manage risks (for
example, ISA/IEC 62443).
Companies with maturing OT and IT convergence display common
patterns.

**Level of risk exposed if this best practice is not established:** Medium

**Prescriptive guidance IOTOPS01-BP01-01:** *Conduct a cyber-security risk assessment so that the risks, gaps and vulnerabilities are fully understood and can be proactively managed. Create and maintain an up-to-date threat model.*

- Proactively managing risks, gaps, and vulnerabilities
between OT and IT
- Up to date threat modeling capabilities for both OT and IT
- Define the system being assessed
- Identify threats, vulnerabilities and consequences of
unintended access or behavior
- Rank the discovered risks
- Develop a risk mitigation strategy

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/organization.html*

---

## IOTOPS01-BP02 Evaluate if OT and IT teams use separate policies and controls to manage cybersecurity risks or if they use the same policy

The ongoing maturity and adoption of cloud within IT and now
within OT creates a more common environment. A comprehensive
enterprise and OT security policy will encompass risks across
the entirety of the business. This allows for OT risks such as
safety to be recognized and addressed within IT. Conversely,
this allows for IT risks such as bots and ransomware to be
addressed within OT. While policies might converge, mitigation
strategies will still differ in many cases.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive
guidance IOTOPS01-BP02-01**

- OT and IT maintaining separate risk policies.
- The degree of isolation for process control and safety
networks.
- Interconnectedness of OT and IT systems and networks.
- Security risks that were applicable to either IT or OT might
now apply to both.
- Singular security control policy that governs both OT and
IT.
- Different mitigation strategies as appropriate for OT and
for IT. For example, the speed of patching is often
different between OT and IT by design.
- The use of holistic approaches to manage OT and IT risk.

### Resources

- [How
to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
- [AWS Threat Modeling workshop](https://maturitymodel.security.aws.dev/en/3.-efficient/threat-modeling/)
- [Assessing
OT and IIoT cybersecurity risk](https://aws.amazon.com/blogs/iot/assessing-ot-and-iiot-cybersecurity-risk/)
- [Guidance
on using ISA/IEC 62443 for IIoT projects](https://aws.amazon.com/blogs/iot/guidance-on-using-isa-iec-62443-for-iiot-projects/)

IOTOPS02: Is there a central cloud
center of excellence (CCoE) with equivalent representation
from OT and IT in industrial organizations?

Given the historical nature of the separation of IT and OT,
organizations might still operate in silos. An indication of
converging maturity is how well those teams are working across
divisions or have even removed silos altogether. Meaningful
OT/IT convergence requires focused and organized effort, which
a CCoE can facilitate. A CCoE is a multi-disciplinary team of
passionate OT and IT subject matter experts (SMEs) who act as
change agents to accelerate IIoT adoption by standardizing and
evangelizing best practices, developing repeatable patterns to
scale implementation, driving governance, and providing
thought leadership. The CCoE can start small with 3-5 members,
cross-trained in both IT and OT aspects and can scale as
needed. For a CCoE to be successful, it requires executive
sponsorship and ability to act autonomously. The CCoE can
focus on making incremental improvements instead of a big-bang
approach. A prioritization framework is used to identify pilot
use cases starting with low-risk, high value, and low effort
use cases with measurable success metrics. After the pilot use
cases are deployed and business value demonstrated, this
activity continues cyclically to implement the pipeline of
prioritized use cases.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/organization.html*

---

# IOTOPS02 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS02-BP01 Consolidate resources into centers of excellence to bring focus to new or transforming enterprises

You can consider creating CCoEs around security to consolidate
experts from around the company. Such focused areas are a
central point of technical authority and accelerates decision
making.

**Level of risk exposed if this best practice is not established:** Low****

**Prescriptive guidance IOTOPS02-BP01-01**

- Consolidating resources into centers of excellence.
- Security experts consolidated from around the company into a
singular organization.
- Defining security focus areas based on risk priorities.
- Having a central point of security authority.
- OT and IT teams operating uniformly.
- Well understood and applied incident response decision
rights in OT.
- Availability is vital in OT. Systems must run in order to
produce and manufacture product. Downtime equals lost
revenue.
- Security defenses are often designed to wrap around OT zones
while restricting the conduits between them.

### Resources

- [AWS Blogs: 7 Pitfalls to Avoid When Building a CCOE](https://aws.amazon.com/blogs/enterprise-strategy/7-pitfalls-to-avoid-when-building-a-ccoe/)
- [AWS Blogs: Using a CCOE to Transform the Entire
Enterprise](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/)
- [Managing
Organizational Transformation for successful OT/IT
convergence](https://aws.amazon.com/blogs/iot/managing-organizational-transformation-for-successful-ot-it-convergence/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/organization.html*

---

# IOTOPS03 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## IOTOPS03-BP01 Use static and dynamic device hierarchies to support fleet operations

Using a software registry, devices can be categorized into
static groups based on their fixed attributes (such as version
or manufacturer) and into dynamic groups based on their
changing attributes (such as battery percentage or firmware
version). Operationalizing devices in groups can help you
manage, control, and search for devices more efficiently.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS03-BP01-01** *Manage several devices at
once by categorizing them into static groups and hierarchy of
groups.*

- Build a hierarchy of static groups for efficient
categorization and indexing of your devices.
- Use provisioning templates to assign devices to static
groups as they are provisioned for the first time.
- For example, categorize all sensors of a car under a car
group and all the cars under a vehicle group. Child groups
inherit policies and permissions attached to their
respective parent groups.

**Prescriptive guidance
IOTOPS03-BP01-02** *Build a device index to
efficiently search for devices, and aggregate registry data,
runtime data, and device connectivity data.*

- Use a fleet indexing service from AWS IoT Core to index
device and group data.
- Use a device index to search registry metadata, stateful
metadata, and device connectivity status metadata.
- Use a group index to search for groups based on group name,
description, attributes, and all parent group names.
- For example, if you want to send over-the-air (OTA) updates
only to devices that are sufficiently charged, then define a
dynamic group for devices with more than 90% battery.
Devices will dynamically be added to or removed from the
group as their battery percentage crosses the threshold.
Send OTA updates to all things under this dynamic group

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS03-BP02 Use index and search services to enable rapid identification of target devices

A large IoT deployment can have millions of sensors sending
data to the cloud. A separate indexing and search service can
make it straightforward to index and organize the device data,
and search for devices by attributes. Ingesting device data to
a search service, for example, Amazon OpenSearch Service, makes it straightforward to use powerful
search, visualization, and analytics capabilities of OpenSearch Service
to organize and search for devices. You can ingest your device
data and the state to OpenSearch Service seamlessly.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS03-BP02-01** *Use an indexed data store to
get, update, or delete device state.*

- Use messaging topics to enable applications and things to
get, update, or delete the state information for a Thing
(Thing Shadow).
- Ingest the shadow data to Firehose through the
AWS IoT Core rules engine.
- Ingest the data from Firehose to Amazon OpenSearch Service through built-in
destination options for OpenSearch Service.
- Configure search and visualizations on the data directly or
through the OpenSearch Dashboards console.
- In AWS, you can create an AWS IoT thing for each physical
device in the device registry of AWS IoT Core. By creating a
thing in the registry, you can associate metadata to
devices, group devices, and configure security permissions
for devices. An AWS IoT thing should be used to store static
data in the thing registry while storing dynamic device data
in the thing's associated device shadow. A device's shadow
is a JSON document that is used to store and retrieve state
information for a device.

### Resources

- [AWS IoT Core - Fleet indexing serviceAWS IoT Core - Fleet
indexing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html)
- [AWS IoT Core - AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [The
Internet of Things on AWS – Official Blog: Archive AWS IoT Device Shadow services in Amazon OpenSearch Service](https://aws.amazon.com/blogs/iot/archive-aws-iot-device-shadows-in-amazon-elasticsearch-service/)
- [Analyze
device-generated data with AWS IoT and Amazon OpenSearch Service](https://aws.amazon.com/blogs/mobile/analyze-device-generated-data-with-aws-iot-and-amazon-elasticsearch-service/)

IOTOPS04: How do you verify that newly
provisioned devices have the required operational prerequisites?

Logical security for IoT and data centers is similar in that
both involve predominantly machine-to-machine authentication.
However, they differ in that IoT devices are frequently
deployed to environments that cannot be assumed to be
physically secure. IoT applications also commonly require
sensitive data to traverse the internet. Due to these
considerations, it is vital for you to have an architecture
that determines how devices will securely gain an identity,
continuously prove their identity, be seeded with the
appropriate level of metadata, be organized and categorized
for monitoring, and enabled with the right set of permissions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

# IOTOPS04 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS04-BP01 The device management processes should be automated, data-driven, and based on previous, current, and expected device behavior

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS04-BP01-01** *Defining how devices are
provisioned must include how the devices are manufactured and
how they are registered for both greenfield and brownfield fleet
of devices.*

- In AWS IoT, you can use multiple features to provision your
individual device identities signed by your CA to the cloud.
This path involves provisioning devices with identities and
then using just-in-time-provisioning (JITP),
just-in-time-registration (JITR), fleet provisioning or
Multi-Account Registration to securely register your device
certificates to the cloud. Using AWS services including
Route 53, Amazon API Gateway, Lambda, and DynamoDB, will
create a simple API interface to extend the provisioning
process with device bootstrapping.
- IoT applications must support incremental rollout and
rollback strategies. By having this as part of the
operational efficiency plan, you will be equipped to launch
a fault-tolerant, efficient IoT application.

### Resources

- [Device
Manufacturing and Provisioning with X.509 Certificates in AWS IoT Core](https://docs.aws.amazon.com/pdfs/whitepapers/latest/device-manufacturing-provisioning/device-manufacturing-provisioning.pdf#device-manufacturing-provisioning)
- [How
to automate onboarding of IoT devices to AWS IoT Core at scale with Fleet Provisioning](https://aws.amazon.com/blogs/iot/how-to-automate-onboarding-of-iot-devices-to-aws-iot-core-at-scale-with-fleet-provisioning/)

IOTOPS05: How do you govern device fleet
provisioning process?

IoT solutions can scale to millions of devices and this requires
device fleets to be well planned from the perspectives of
provisioning processes and metadata organization. Maintain a
full chain of security controls over who or what processes can
trigger device provisioning to decrease the likelihood of
inviting unintended (or rogue) devices into your fleet.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

# IOTOPS05 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

## IOTOPS05-BP01 Document how devices join your fleet from manufacturing to provisioning

Document the whole device provisioning process to clearly define
the responsibilities of different actors at different stages.
The end-to-end device provisioning process involves multiple
stages owned by different actors. Documenting the plan and
processes by which devices onboard and join the fleet affords
the appropriate amount of review for potential gaps.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS05-BP01-01** *Document each step (manual and
programmatic) of all the stages for the corresponding actors of
that stage and clearly define the sequence.*

- Identify the steps at each stage and the corresponding
actors.

Device assembly by hardware manufacturer.
- Device registration by service and solution provider.
- Device activation by the end user of the service or
solution provider.

- Clearly define and document the dependencies and specific
steps for each actor from device manufacturer to the end
user.
- Document whether devices can self-provision or are
user-provisioned and how you can make sure that newly
provisioned devices are yours.

**Prescriptive guidance
IOTOPS05-BP01-02** *Assign device metadata to
enable straightforward grouping and classification of devices in
a fleet.*

- The metadata can be used to group the devices in groups to
search and force common actions and behaviors.
- For example, you can assign the following metadata at the
time of manufacturing:

Unique ID
- Manufacturer details
- Model number
- Version or generation
- Manufacturing date

- If a particular model of a device requires a security patch,
then you can easily target the patch to the devices that are
part of the corresponding model number group. Similarly, you
can apply the patches to devices manufactured in a specific
time frame or belonging to a particular version or
generation.
- Along with creating a virtual representation of your device
in the device registry, as part of the operational process,
you must create thing types that encapsulate similar static
attributes that define your IoT devices. A thing type is
analogous to the product classification for a device. The
combination of thing, thing type, and device shadow can act
as your first entry point for storing important metadata
that will be used for IoT operations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS05-BP02 Use programmatic techniques to provision devices at scale

Scaling the onboarding and provisioning of a large device fleet
can be a bottleneck if there is even one manual step per device.
Programmatic techniques define patterns of behavior for
automating the provisioning process such that authenticated and
authorized devices can onboard at any time. This practice
provides a well-documented, reliable, and programmatic
provisioning mechanism that is consistent across all devices
devoid of human errors.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS05-BP02-01** *Embed provisioning claims into
the devices that are mapped to approval authorities recognized
by the provisioning service.*

- Generate a provisioning claim and embed it into the device
at the time of manufacturing.
- AWS IoT Core can generate and securely deliver certificates
and private keys to your devices when they connect to AWS IoT for the first time, using AWS IoT Fleet Provisioning.

**Prescriptive guidance
IOTOPS05-BP02-2** *Use programmatic bootstrapping
mechanisms if you are bringing your own certificates.*

- Determine if you will or won't have device information
beforehand
- If you do not have device information beforehand, use
just-in-time provisioning (JITP).

Enable automatic registration and associate a
provisioning template with the CA certificate used to
sign the device certificate.
- For example, when a device attempts to connect to AWS IoT by using a certificate signed by a registered CA
certificate, AWS IoT loads the template from the
certificate and initiates the JITP workflow.

- If you have device information beforehand, use bulk
registration.

Specify a list of single-thing provisioning template
values that are stored in a file in an S3 bucket.
- Run the start-thing-registration-task command to
register things in bulk. Provide provisioning template,
S3 bucket name, a key name, and a role ARN to the
command.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS05-BP03 Use device level features to enable re-provisioning

A birth or bootstrap certificate is a low-privilege unique
certificate that is associated with each device during the
manufacturing process. The certificate should have a policy to
restrict devices to only allow connecting to specific endpoints
to initiate provisioning process and fetch the final
certificate. Before a device is provisioned, it should be
limited in functionality to help prevent its misuse. Only after
a provisioning process is invoked and approved, should the
device be allowed to operate on the system as designed.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS05-BP03-01** *Use a certificate
bootstrapping process to establish processes for device
assembly, registration, and activation.*

- For example, AWS IoT Core offers a fleet provisioning
interface to devices for upgrading a birth certificate to
long-lived credentials that enable normal runtime
operations.

**Prescriptive guidance
IOTOPS05-BP03-02** *Obtain a list of allowed
devices from the device manufacturer.*

- Check the allow list file to validate that the device has
been fully vetted by the supplier.
- Make sure that the list is encrypted, securely stored, and
can only be accessed by necessary services and users. Even
if the list changes, keep the original list securely stored.
- Make sure that this list is securely transferred from the
manufacturer to you, is encrypted, and is not publicly
accessible.
- Make sure that any bootstrap certificate used is signed by a
certificate authority (CA) you own or trust.

IOTOPS06: How do you implement
observability for your IoT system?

Observability is a crucial part for your IoT application built
to handle device activity at scale. As the main three pillars of
observability are logging, metrics and tracing, there are more
functional parts of the business goals where you actively
troubleshoot and improve the application to mitigate risks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

# IOTOPS06 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

## IOTOPS06-BP01 Implement monitoring to capture logs and metrics

Monitoring is an important part of maintaining the reliability,
availability, and performance of your IoT solutions. It is
highly recommended to collect monitoring data from all parts of
your IoT solution to make it easier to debug a multi-point
failure, if one occurs. Create a monitoring plan that answers
the questions such as:

- Which resources to monitor (edge, device connectivity,
remote operations, or device health)?
- Which tools to use?
- Who has to be notified should an incident or event occurs?

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS06-BP01-01** *Use Amazon CloudWatch to
monitor your IoT fleet.*

To support operational insights to your cloud application,
generate dashboards for all metrics collected from IoT Core and
IoT Device Management. These metrics are available through
Amazon CloudWatch Metrics. In addition, CloudWatch Logs contain
information such as total successful messages inbound, messages
outbound, connectivity success, and errors.

**Prescriptive guidance IOTOPS06-BP01-02** *Capture the default metrics emitted by your IoT services and configure alarms for metrics that might indicate business interruption.*

For example, your business deploys a thousand IoT sensors and your operations team wants to be alerted if sensors can no longer connect to the cloud and send telemetry.

- Your IT team administering the AWS account reviews the AWS IoT Core metrics and notes the following metrics to
monitor: `Connect.AuthError`, `Connect.ClientError`, `Connect.ClientIDThrottle`, `Connect.ServerError`, and `Connect.Throttle`.
Activity in these metrics constitutes alerting and
investigation.
- Your IT team uses CloudWatch to configure new alarms on
these metrics when for any period the metrics' SUM of Count
is greater than zero.
- Your IT team configures an Amazon SNS topic to notify their
paging tool when the new CloudWatch alarms changes status.

For more detail, see
[Monitor
AWS IoT alarms and metrics using Amazon CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring-cloudwatch.html)

**Prescriptive guidance
IOTOPS06-BP01-03** *Use unified monitor dashboard
for IoT metrics.*

The unified dashboard in AWS IoT monitor allows identification of potential connectivity and operational problems, reducing the time associated with fleet troubleshooting procedures.
The connectivity metrics dashboard available in the AWS IoT monitor, consolidates frequently used metrics from AWS IoT Core, such as successful connections, inbound or outbound messages published, and connection request authorization failures.
A guided workflow enables AWS IoT Device Management's Fleet Indexing feature and adds widgets for connected device counts, percentage of devices disconnected, and disconnect reasons to the same page.
AWS IoT provides fleet-level and device-level insights driven from the Thing Registry and Device Shadow service through search capabilities such as AWS IoT Fleet Indexing. The ability to search across your fleet eases the operational overhead of diagnosing IoT issues at the device-level or fleet-wide level.

**Prescriptive guidance
IOTOPS06-BP01-04** *Implementing tracing between
all the resources or modules.*

- Visualizing the entire path of requests, from entry to exit
helps quickly identifying where failures or performance
issues occur.
- In addition to Amazon CloudWatch, it's crucial to
instrument to emit trace data. This process can provide
further insights into your workload's behavior and
performance. Integrate X-Ray into your application to gain
insights into its behavior, understand its performance, and
pinpoint bottlenecks. Utilize X-Ray Insights for automatic
trace analysis.

AWS Lambda Powertools is a suite of utilities that helps with
implementing observability best practices without needing to
write additional custom code. Powertools provides three core
utilities:

- *Tracing* provides a
simpler way to send traces from functions to

[AWS X-Ray](https://aws.amazon.com/xray/). It provides visibility into function calls,
interactions with other AWS services, or external HTTP
requests. You can add attributes to traces to allow
filtering based on key information.
- *Logging* provides a custom
logger that outputs structured JSON. It allows you to pass
in strings or more complex objects, and takes care of
serializing the log output.
- *Metrics* simplify
collecting custom metrics from your application, without the
need to make synchronous requests to external systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS06-BP02 Capture and monitor application performance at the edge

Implement tracing and observability methods that provide granular visibility into edge application health, performance, and root cause analysis. By seamlessly connecting the observability strategy for cloud-based applications with those running at the edge, organizations can gain end-to-end visibility and insights for improved application performance.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS06-BP02-01** *Emit device side metrics using
agents.*

- AWS IoT Device Defender Detect can collect, aggregate, and
monitor metrics data generated by AWS IoT devices to
identify devices that exhibit abnormal behavior. Securely
deploy the AWS IoT SDK version two on your AWS IoT connected
devices or device gateways to collect device-side metrics.
- You can use AWS IoT Device Client to publish metrics as it
provides a single agent that covers the features present in
both AWS IoT Device Defender and AWS IoT Device Management.
- Publish device-side metrics to the
[reserved
topic](https://docs.aws.amazon.com/iot/latest/developerguide/reserved-topics.html#reserved-topics-device-defender) in AWS IoT for

[AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/reserved-topics.html#reserved-topics-device-defender) to collect and evaluate.

**Prescriptive guidance
IOTOPS06-BP02-02** *Collect application logs for
tracing capabilities.*

- [AWS Distro
for OpenTelemetry](https://aws.amazon.com/otel/) seamlessly collects and exports
metrics and traces to AWS monitoring services. Distro for
OpenTelemetry Collector is an agent that runs on your
application environment. When it is integrated with AWS IoT Greengrass, this combination extends your observability
capabilities to both edge and cloud applications at scale,
providing consistent and seamless tracing across your
application infrastructure. This integrated approach
delivers real-time visibility into application performance

For more information, see
[Monitor
edge application using AWS IoT Greengrass Monitor edge application performance using AWS IoT Greengrass and AWS Distro for OpenTelemetry](https://aws.amazon.com/blogs/iot/monitor-edge-application-performance-using-aws-iot-greengrass-and-aws-distro-for-opentelemetry/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS06-BP03 Monitor the status of your IoT devices

You need to be able to track the status of your devices. This
includes operational parameters and connectivity. You need to
know whether devices have disconnected intentionally or not.
Monitoring the status of your device fleet is important in
helping troubleshoot device software operation and connectivity
disruptions.

Design a state machine for the device connectivity states, from
initialization and first connection, to frequent communication
(like keep-alive messages) and final state before going offline.
Lifecycle events, such as connection and disconnection, can be
used to observe and analyze device behavior over a period of
time. Additionally, periodic keep-alive messages can track
device connectivity status.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS06-BP03-01** *Subscribe to lifecycle events
and monitor the connections using keep-alive
messages.*

- Capture messages from the IoT message broker whenever a
device connects or disconnects. Being able to tell the
difference between a clean and dirty disconnect is useful in
many scenarios where the devices don't maintain a constant
connection to the broker.
- Based on the use case and device constraints, have the
device send periodic keep-alive messages to AWS IoT Core and
monitor, and analyze the keep-alive messages for anomalies.
- Make sure that the frequency of sending keep-alive messages
is not causing any network storms (perhaps by introducing
some jitter) in the network or causing rate limits.
- Configure your devices to
communicate their status periodically. Implement
Last Will and Testament (LWT) messages and periodic device
keep-alive messages.

**Prescriptive guidance
IOTOPS06-BP03-02** *Implement a well-designed
device connectivity state machine*

- Make sure that the device communicates when it first comes
online and just prior to going offline.
- Implement a wait state for lifecycle events. When a
disconnect message is received, wait a period of time and
verify that the device is still offline before taking
action.
- Specify the interval with which each connection should be
kept open if no messages are received. AWS IoT drops the
connection after that interval unless the device sends a
message or a ping.

**Prescriptive guidance
IOTOPS06-BP03-03** *Use device connection and
disconnection status for anomaly detection.*

- Use connectivity data patterns from devices to detect
anomalous behavior in their communication patterns.

### Resources

- [AWS IoT Now Supports WebSockets, Custom Keepalive Intervals, and Enhanced Console](https://aws.amazon.com/about-aws/whats-new/2016/01/aws-iot-now-supports-websockets-custom-keepalive-intervals-and-enhanced-console/)
- [AWS Solutions Library: Real-Time IoT Device Monitoring with Managed Service for Apache Flink](https://aws.amazon.com/solutions/implementations/real-time-iot-device-monitoring-with-kinesis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS06-BP04 Use device state management services to detect status and connectivity patterns

Edge and cloud-side management services monitor and analyze
parameters, such as device connectivity status and latency, to
help in providing diagnostics and predicting anomalies.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS06-BP04-01** *Monitor device state and
connectivity patterns.*

- Use (or develop as needed) device, gateway, edge, and cloud
management tools that allow monitoring the fleet of devices
- Use logging and monitoring features at all processing
points—device, gateway, edge, and cloud, to get a complete
picture of device connectivity patterns.

### Resources

- [Monitoring
your IoT fleet using CloudWatch](https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/)

- [Building
Observability in IoT applications using AWS Lambda Powertools, AWS X-Ray, Amazon CloudWatch](https://www.youtube.com/watch?v=moRlNXpdhm8)
- [Getting
Aggregate Information of Devices with AWS IoT Device Management Fleet Indexing](https://aws.amazon.com/blogs/iot/getting-aggregate-information-of-devices-with-aws-iot-device-management-fleet-indexing/)
- [AWS IoT Core - Managing thing indexing](https://docs.aws.amazon.com/en_us/iot/latest/developerguide/managing-index.html)
- [Security
monitoring for connected devices across OT, IoT, edge, cloud (TDR222)](https://www.youtube.com/watch?v=-2c83ql5KXg)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

# IOTOPS07 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## IOTOPS07-BP01 Enable appropriate responses to events

Key operational data elements are those data points that convey
some notion of operational health of your application by
classifying events. Detecting operational events early can
uncover unforeseen risks in your application and give your
operations team a head start to help prevent or reduce business
interruption. By defining a minimum set of logs, metrics, and
alarms, your operations team can provide a faster incident
response which reduces risks of business disruption.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS07-BP01-01** *Configure logging to capture
and store at least error-level events.*

- Use AWS IoT service logging options to capture error events
in Amazon CloudWatch Logs
- Your devices create telemetry or diagnostic messages that
are not stored in the registry or the device's shadow.
Instead, these messages are delivered to AWS IoT using a
number of MQTT topics. To make this data actionable, use the
AWS IoT rules engine to route error messages to your
automated remediation process and add diagnostic information
to IoT messages. The rules engine inspects the status of a
message and if it is an error, it starts the Step Function
workflow to remediate the device based off the error message
detail payload.

**Prescriptive guidance
IOTOPS07-BP01-02** *Create a dashboard for your
responders to use in investigations of operational events to
rapidly pinpoint the period of time when errors are
logged.*

- Group clusters of error events into buckets of time to
quickly identify when surges of errors were captured.
- Drill down into clusters of errors to identify any patterns
to signal for triage response.

**Prescriptive guidance
IOTOPS07-BP01-03** *Configure an automated
monitoring and alerting tool to detect common symptoms and
warnings of operational issues.*

- For example, configure AWS IoT Device Defender to run a
daily audit on at least the high and critical checks.
- Configure an Amazon SNS topic to notify a team email list,
paging tool, or operations channel when AWS IoT Device Defender
reports non-compliant resources in an audit.

For more information, see [AWS IoT Device Defender Audit](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/operate.html*

---

## IOTOPS07-BP02 Use data-driven auditing metrics to detect if any of your IoT devices might have been broadly accessed

Monitor and detect the abnormal usage patterns and possible
misuse of devices and automate the quarantine steps.
Programmatic methods to detect and quarantine devices from
interacting with cloud resources enable teams to operate a fleet
in a scalable way while minimizing a dependency on active human
monitoring.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS07-BP02-01** *Use monitoring and logging
services to detect anomalous behavior. Once you detect the
compromised device, run programmatic actions to quarantine
it.*

- Disable the certificate for further investigation and revoke
the certificate to help prevent the device from any future
use.
- Use AWS IoT CloudWatch metrics and logs to monitor for
indications of misuse. If you detect misuse, quarantine the
device so it does not impact the rest of the system.
- Use AWS IoT Device Defender to identify security issues and
deviations from best practices

IOTOPS08: How do you segment your device
operations in your IoT application?

You need to segment your device fleet to pinpoint operational
challenges and direct incident response to the appropriate
responder. Device fleet segmentation enables you to identify
conditions under which devices operate sub optimally and
minimize response time to security events.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/operate.html*

---

# IOTOPS08 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS08-BP01 Use static and dynamic device attributes to identify devices with anomalous behavior

Anomalies in fleet operations might only surface when analyzing
metrics that aggregate across the boundaries of your static and
dynamic groups or attributes. For example, devices that are
running firmware version 2.0.10 and currently have a battery
level over 50%. Static and dynamic groups allow for identifying
and pinpointing devices in unique ways to monitor, analyze, and
take corrective actions on device behavior.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS08-BP01-01** *Pinpoint devices with unusual
communication patterns.*

- Use a combination of static and dynamic groups of devices to
perform fleet indexing to group devices and identify
behavioral patterns—connectivity status, and message
transmission.
- Use lifecycle events, device connectivity, and data
transmission patterns to detect anomalies and pinpoint
unusual behavior using techniques such as statistical
anomaly detection (for large fleet of devices).
- Once abnormal behavior has been identified, move rogue and
abnormal devices into a different group so that remedial
policies can be assigned and implemented on them.

### Resources

- [AWS IoT Core - Authorization](https://docs.aws.amazon.com/iot/latest/developerguide/iot-authorization.html)
- [AWS IoT - Device Defender](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/operate.html*

---

# IOTOPS09 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS09-BP01 Run ops metrics analysis across business teams, document learnings and define action items for future firmware deployments

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS09-BP01-01** *Monitor the behavior of
devices as they are updated in the field, and proceed only after
a percentage of devices have upgraded successfully.*

During upgrades, continue to collect all of the Amazon CloudWatch Logs, telemetry, and IoT device job messages and
combine that information with the KPIs used to measure overall
application health and the performance of long-running canaries.

Services like AWS IoT Device Defender are used to track
anomalies in overall device behavior, and to measure deviations
in performance that may indicate an issue in the updated
firmware.

**Prescriptive guidance
IOTOPS09-BP01-02** *Use AWS IoT Device Management
for creating deployment groups of devices and delivering over
the air updates (OTA) to specific device groups.*

Use a combination of grouping IoT devices for deployment and
staggering firmware upgrades over a period of time. In AWS IoT,
thing groups allow you to manage devices by category. Groups can
also contain other groups — allowing you to build hierarchies.
With organizational structure in your IoT application, you can
quickly identify and act on related devices by device group.
Leveraging the thing group allows you to automate the addition
or removal of devices from groups based on your business logic
and the lifecycle of your devices.

**Prescriptive guidance
IOTOPS09-BP01-3** *Use dynamic thing group as a
target for OTA updates.*

Create a continuous job with a dynamic thing group as target
allows you to automatically target devices when they meet the
desired criteria. The criteria can be the connectivity state or
criteria stored in registry or shadow such as software version
or model. If a thing doesn't appear in the dynamic thing group,
it won't receive the job document from the job.

For example, if your device fleet requires a firmware update to
minimize the risk of interruption during the update process, and
you only want to update the firmware on devices with a battery
life greater than 80%. You can create a dynamic thing group
called 80PercentBatteryLife that only includes devices with a
battery life above 80% and use it as the target for your job.
Only devices that meet your battery life criteria will receive
the firmware update. As devices reach the 80% battery life
criteria, they are automatically added to the dynamic thing
group and will receive the firmware update.

IOTOPS10: How do you verify that you are ready to support the
operations of devices in your IoT workload?

Operating IoT workloads at scale is different than testing and
running prototypes. You need to make sure that your team is
prepared and trained to operate a widely distributed IoT data
collection application. IoT workloads require your teams to
learn new skills and competencies to deliver edge-to-cloud
outcomes. Your team needs to be able to pinpoint key operational
thresholds that indicate a high level of readiness.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/evolve.html*

---

# IOTOPS10 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS10-BP01 Train team members supporting your IoT workloads on the lifecycle of IoT applications and your business objectives

Key team members responsible for IoT workloads are trained on
major IoT lifecycle events: onboarding, command and control,
security, data ingestion, integration, and analytics services.
Team members should be able to identify key operational metrics
and know how to apply incident response measures. Training team
members on the basics of IoT lifecycles and how these align with
business objectives provides actionable context on failure
scenarios, mitigation strategies, and defining lasting processes
that effectively contribute to fewer operational events and less
severe impact during events.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS10-BP01-01** *Build IoT operational
expertise by having team members and architects' complete
reviews of common IoT architectural patterns, best practices,
and educational courses.*

- Introduce new team members to IoT lifecycles with onboarding
checklists that include at least one educational course.
- Introduce new team members with onboarding checklists that
include a step to review, validate, and submit updates to
your IoT application architecture documentation and
operational monitoring plan.

**Prescriptive guidance
IOTOPS10-BP01-02** *Author runbooks for each
component of the architecture and train team members on their
use.*

Include guidance for a response procedure for remote devices
that are no longer online. Apply recovery commands for
troubleshooting remote devices that are faulty but still online.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/evolve.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
