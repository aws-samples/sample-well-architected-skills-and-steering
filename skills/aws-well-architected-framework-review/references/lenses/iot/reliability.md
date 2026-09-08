# Reliability

**Pillar**: Reliability  
**Questions**: 14

---

# IOTREL01 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL01-BP01 Use NTP to maintain time synchronization on devices

IoT devices need to have a client to keep track of time—either
using Real Time Clock (RTC) or Network Time Protocol (NTP) to
set the RTC on boot. Failure to provide accurate time to an IoT
device could help prevent it from being able to connect to the
cloud.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL01-BP01-01** *Prefer NTP to RTC when NTP
synchronization is available.*

Many computers have an RTC peripheral that helps in keeping
time. Consider that RTC is prone to clock drift of about 1
second a day, which can result in the device going offline
because of certificate invalidity.

**Prescriptive guidance
IOTREL01-BP01-02** *Use Network Time Protocol
for connected applications.*

- Select a safe, reliable NTP pool to use, and a one that
addresses your security design
- Many operating systems include an NTP client to sync with an
NTP server
- If the IoT device is using GNU/Linux, it is likely to
include the NTPD daemon
- You can import an NTP client to your system if using
FreeRTOS
- The device's software needs to include an NTP client and
should wait until it has synchronized with an NTP server
before attempting a connection with AWS IoT Core
- The system should provide a way for a user to set the
device's time so that subsequent connections can succeed
- Use NTP to synchronize RTC on the device to help prevent the
device from deviating from UTC
- Consider the following
[The
NTP Pool for vendors](https://www.pool.ntp.org/en/vendors.html)
- [Chrony](https://chrony.tuxfamily.org/)
is a different implementation of NTP than what NTPD uses and
it is able to synchronize the system clock faster and with
better accuracy than NTPD. Chrony can be set up as a client
and server.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

## IOTREL01-BP02 Provide devices access to NTP servers

An NTP server should be available for clients to use for local
time. NTP servers are required by NTP clients to synchronize
device time and function properly.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL01-BP02-01** *Provide access to NTP
services.*

- ntp.org can be used to synchronize your computer clocks.

- [Amazon
Time Sync Service](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-the-amazon-time-sync-service/): a time synchronization service
delivered over NTP, which uses a fleet of redundant
satellite-connected and atomic clocks in each Region to
deliver a highly accurate reference clock. This is natively
accessible from Amazon EC2 instances and this can be pushed
to edge devices.
- [Chrony](https://chrony.tuxfamily.org/)
is a different implementation of NTP than what NTPD uses and
it is able to synchronize the system clock faster and with
better accuracy than NTPD. Chrony can be set up as a server
and client.

IOTREL02: How do you manage service
quotas and limits for peaks in your IoT workload?

AWS IoT provides a set of soft and hard limits for different
dimensions of usage. AWS IoT outlines the data plane limits on
the IoT limits, see
[AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_iot). Data plane operations (for example, MQTT
Connect, MQTT Publish, and MQTT Subscribe) are the primary
driver of your device connectivity. Therefore, it's important to
review the IoT limits and make sure that your application
adheres to any soft limits related to the data plane, while not
exceeding any hard limits that are imposed by the data plane.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

# IOTREL02 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL02-BP01 Manage service quotas and constraints

For cloud-based workload architectures, there are service quotas (which are also referred to as service limits). These quotas exist to help prevent accidentally provisioning more resources than you need and to limit request rates on API operations so as to protect services from abuse.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTREL02-BP01-01** *Follow the Reliability
Foundations Best Practices defined in the AWS Well-Architected
Framework.*

The most important part of your IoT scaling approach is to make sure that you architect around any hard limits because exceeding limits that are not adjustable results in application errors, such as throttling and client errors. Hard limits are related to throughput on a single IoT connection. Consider restructuring your MQTT topics, or implementing cloud-side logic to aggregate or filter messages before delivering the messages to the interested devices.

Soft limits in AWS IoT traditionally correlate to account-level limits that are independent of a single device. For any account-level limits, you should calculate your IoT usage for a single device and then multiply that usage by the number of devices to determine the base IoT limits that your application will require for your initial product launch. AWS recommends that you have a ramp-up period where your limit increases align closely to your current production peak usage with an additional buffer. To make sure that the IoT application is not under provisioned:

- Consult published AWS IoT CloudWatch metrics for all limits:
[AWS IoT metrics and dimensions](https://docs.aws.amazon.com/iot/latest/developerguide/metrics_dimensions.html)
- Monitor CloudWatch metrics in AWS IoT Core:
[Logging
and Monitoring](https://docs.aws.amazon.com/iot/latest/developerguide/security-logging.html)
- Alert on CloudWatch throttle metrics, which would signal if
you need a limit increase.
- Set alarms for all thresholds in IoT, including MQTT
connect, publish, subscribe, receive, and rule engine
actions.
- Monitoring AWS IoT MQTT Traffic and Automating Quota and
Throttling Notifications
- [Monitoring
your IoT Fleet using CloudWatch](https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/)
- Make sure that you request a limit increase in a timely
fashion, before reaching 100% capacity. See the AWS
documentation on Requesting a quota increase:
[Requesting
a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)

In addition to data plane limits, the AWS IoT service has a
control plane for administrative APIs. The control plane manages
the process of creating and storing IoT policies and principals,
creating the thing in the registry, and associating IoT
principals including certificates and Amazon Cognito federated
identities. Because bootstrapping and device registration is
critical to the overall process, it's important to plan control
plane operations and limits. Control plane API calls are based
on throughput measured in requests per second. Control plane
calls are normally in the order of magnitude of tens of requests
per second. It is important for you to work backward from peak
expected registration usage to determine if any limit increases
for control plane operations are needed. Plan for sustained
ramp-up periods for onboarding devices so that the IoT limit
increases align with regular day-to-day data plane usage.

To protect against a burst in control plane requests, your
architecture should limit the access to these APIs to only
authorized users or internal applications. Implement back-off
and retry logic, and queue inbound requests to control data
rates to these APIs.

IOTREL03: How do you design workloads to
operate efficiently within network bandwidth and storage
constraints?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

# IOTREL03 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL03-BP01 Down sample data to reduce storage requirements and network utilization

Data should be down sampled where possible to reduce storage in
the device and lower transmission costs and reduce network
pressure.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL03-BP01-01** *Use device edge software
capabilities for down sampling.*

- Use compression as a means of down sampling data

Data transmitted to the cloud can be in JSON format, or
in other formats such as Protocol Buffers.

- Using AWS IoT Greengrass for device software to down sample
data.

Applications built using Components can be used on AWS IoT Greengrass to down sample the data before sending it
to the cloud.
- [ETL
with AWS IoT Extract, Transform, Load with AWS IoT Greengrass Solution Accelerator](https://aws.amazon.com/iot/solutions/etl-accelerator/) helps to quickly
set up an edge device with AWS IoT Greengrass to perform
extract, transform, and load (ETL) functions on data
gathered from local devices before being sent to AWS.

IOTREL04: How do you optimize and
control message delivery frequency to IoT devices?

Devices can be restricted in message processing capacity and
messages from the cloud might need to be throttled. The
cloud-side message delivery rate might need to be architected
based on the type of devices that are connected.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

# IOTREL04 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL04-BP01 Target messages to relevant devices

Devices receive information from shadow updates, or from
messages published to topics they subscribe to. Some data are
relevant only to specific devices. In those cases, design your
workload to send messages to relevant devices only, and to
remove any data that is not relevant to those devices.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL04-BP01-01** *Preprocess data to support
the specific needs of the device.*

- Use AWS Lambda to pre-process the data and hone-in
specifically to attributes and variables that are needed by
the device to act upon

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

## IOTREL04-BP02 Implement retry and back off logic to support throttling by device type

Retry and back off logic should be implemented in a controlled
manner so that when you need to alter throttling settings per
device type, you can easily do it. Using data storage of any
chosen kind gives you flexibility on what data to publish down
to the device.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL04-BP02-01** *Use storage mechanisms
that enable retry mechanisms.*

- Using DynamoDB, you can hold data in key value format where
device ID is the key. Retry logic can be applied to only
certain device ID's.
- Using Amazon Relational Database Service, you
have the flexibility to use a variety of database engines.
The retry messages can have new real-time data augmented
with historic data from previous device interactions stored
in Amazon RDS.
- AWS IoT Events provides state machines with built-in timers
to hold back data and retry based on timers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

# IOTREL05 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL05-BP01 Decouple IoT applications from the Connectivity Layer through an Ingestion Layer

In a well-architected IoT application, internal systems are
decoupled from the connectivity layer of the IoT system through
the ingestion layer. The ingestion layer is composed of queues
and streams that enable durable short-term storage while
allowing compute resources to process data independent of the
rate of ingestion.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL05-BP01-01** *Decouple application
consumers using streaming data services.*

To optimize throughput, use AWS IoT rules to route inbound
device data to services such as Amazon Kinesis Data Streams,
Amazon Data Firehose, Amazon Simple Queue Service, or
Amazon Managed Streaming for Apache Kafka before performing any
compute operations. Make sure that all the intermediate
streaming points are provisioned to handle peak capacity. This
approach creates the queueing layer necessary for upstream
applications to process data resiliently.

**Prescriptive guidance
IOTREL05-BP01-02** *Make use of MQTT features
to support reliable delivery of messages.*

AWS IoT Core supports MQTT persistent sessions, which store a
client's subscriptions and messages that haven't been
acknowledged by the client. Messages are stored according to
account limits, and the Persistent session expiry period what
can be adjusted between 1 hour and 7 days. This allows for
clients to publish messages that will be persisted by the AWS IoT Core Broker for up to the account limits and expiry period,
for later processing. Read more about persistent sessions in the
[AWS IoT Core developer guide](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-persistent-sessions).

IOTREL06: How do you facilitate reliable
processing and delivery of IoT messages across your
workload?

Data sent from devices should be processed and stored without
excessive loss. Services that queue and deliver IoT data to
compute and database services should be used to support the
processing of data. IoT devices send lots of data in small sizes
without order, and the cloud application should be able to
handle this.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---

# IOTREL06 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL06-BP01 Dynamically scale cloud resources based on the utilization

The elastic nature of the cloud can be used to increase and
decrease resources on demand. Use the ability to increase and
decrease cloud resources based on data, number of messages, and
size of messages and number of devices.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL06-BP01-01** *Know the mechanisms that
can be used to monitor cloud resource usage and methods to scale
the resources.*

- Use Amazon CloudWatch Logs to trigger based on rate of data
flow to auto-scale cloud resources as needed.
- [Use
AWS IoT Rules engine error actions](https://docs.aws.amazon.com/iot/latest/developerguide/rule-error-handling.html) to provision
additional cloud resources and message retries as needed.
- Examine IoT logs for errors in communicating to resources
and provision resources based on that data.
- Use AWS Lambda to automatically scale your application by
running code in response to each event.
- Use automatic scaling where possible. Kinesis Data Streams
and Amazon DynamoDB are two services that provide automatic
scaling.

**Prescriptive guidance
IOTREL06-BP01-02** *Use MQTT 5 Shared
Subscriptions to effectively load balance MQTT messages across
several subscribers.*

Using *Shared Subscriptions* in
MQTT is an effective way to *load
balance* messages across multiple subscribers in a way
that optimizes resource usage, improves scalability, and
supports more efficient message delivery.

IOTREL07: How do you provision storage
strategies for IoT data in the cloud?

IoT devices send a lot of small messages with no guarantee of
delivery order. This data might not be immediately useful, but
the data volume is typically low enough to economically store
against a future need. It will be beneficial to store the data
so that the data can processed in order. Stored data can be
reprocessed as new requirements are developed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---

# IOTREL07 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL07-BP01 Store data before processing

Make sure that the data from the devices is stored before
processing. As new requirements and capabilities are added,
stored data can be analyzed to meet the new requirements.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL07-BP01-01** *Use IoT Core Rules Engine
to send data to Firehose to batch and store data on
Amazon S3.*

- IoT Rules Engine can send data to Firehose to
batch and store data on Amazon S3. Intelligent tiering can be enabled in Amazon S3 to
reduce storage costs.
- Understand the latency to access data and choose the Region
to store the data in based on device location.
- If data will be processed in Amazon EC2 instances, consider
using the highly available and low-latency Amazon Elastic Block Store (Amazon EBS).
- NoSQL data can be stored in Amazon DynamoDB, which is a
key-value and document database that delivers single-digit
millisecond performance at scale. IoT Core Rules engine can
write all or part of an MQTT message to a DynamoDB table.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---

## IOTREL07-BP02Implement storage redundancy and failover mechanisms for IoT data persistence

There should be recovery plans for failures in storing and
accessing device data in the cloud. Understand the Recovery
Point Objective (RPO) and Recovery Time Objective (RTO) needed
by your application to access data to be used for analysis.

**Level of risk exposed if this best
practice is not established:** Medium

Prescriptive guidance IOTREL07-BP02-01 *Know how to
monitor and take action on cloud storage failures for IoT
data.*

- AWS Health Dashboard provides notification and
remediation guidance when AWS is experiencing events that
might impact you. Storage and access of data can be modified
based on the notification.
- Use Amazon CloudWatch Logs to trigger on events on writing
and reading data and take appropriate error handling action.

Use AWS IoT rules engine error actions to provision data
storage to other locations if primary storage is
unavailable.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---

# IOTREL08 — Reliability

**Pillar**: Reliability  
**Best Practices**: 4

---

## IOTREL08-BP01 Use a mechanism to deploy and monitor firmware updates

When performing over-the-air (OTA) updates to remote devices'
firmware, make sure that the updates are controlled and
reversible to avoid functional impact of the device to the user,
or the device entering a non-recoverable state. Use tools that
allow you to deploy and track management tasks in your device
fleet.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL08-BP01-01** *Use a cloud-based update
orchestrator to deploy your firmware.*

- You can use AWS IoT Jobs to send remote actions to one or
many devices at once, control the deployment of jobs to your
devices, and track the current and past status of job
executions for each device.
- Using FreeRTOS OTA using AWS IoT Jobs: By using AWS IoT Jobs
for FreeRTOS, you have reliability and security provided out
of the box where OTA update job will send firmware to your
end device over secure MQTT or HTTPS and system reserved
topics are provided to keep track on the status of the job
schedule.
- Using custom IoT jobs with AWS IoT connected devices: By
using AWS IoT Jobs with one or more devices connected to AWS IoT gives you the ability to track the full roll out of the
update.

**Prescriptive guidance
IOTREL08-BP01-02** *Version all of the device
firmware artifacts.*

- Version all of the device firmware using Amazon S3.
- Version the manifest or execution steps for your device
firmware.
- Implement a known-safe default firmware version for your
devices to fall back to in the event of an error.
- Implement an update strategy using cryptographic
code-signing, version checking, and multiple non-volatile
storage partitions, to deploy software images and rollback.
- Version all IoT rules engine configurations in
CloudFormation.
- Version all downstream AWS Cloud resources using
CloudFormation.
- Implement a rollback strategy for reverting cloud side
changes using CloudFormation and other infrastructure as
code tools.

Treating your infrastructure as code on AWS allows you to
automate monitoring and change management for your IoT
application. Make sure that updates can be verified, installed,
or rolled back when necessary.

Devices will need new features over time for better user
experience and the firmware will need to be updated remotely.
Devices should be designed to receive and update their firmware
and the IoT application should be designed to send firmware
updates and monitor the success of such an update send.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

## IOTREL08-BP02 Configure firmware rollback capabilities in devices

Augment hardware with software to hold two versions of firmware
and the ability to switch between them. Devices can rapidly roll
back to older firmware if the new firmware has issues.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL08-BP02-01** *Leverage an RTOS with
functionality to roll back device firmware.*

By combining OTA agents provided by FreeRTOS or using AWS IoT Device SDK, you can create flexibility to hold two versions of
firmware with the hardware that is capable of storing it.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

## IOTREL08-BP03 Implement support for incremental updates to target device groups

It is a good practice to test new firmware on a small group of
devices. Using a smaller group of devices for firmware updates
helps make sure that the firmware as well as the upgrade process
is well tested before the entire fleet is updated.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL08-BP03-01** *Use a cloud orchestrator
in conjunction with device settings augmentation. Cloud services
can help you control and manage jobs in tandem with the devices
running the jobs.*

- The AWS IoT Jobs API provides a granular level of control
from the cloud to the device for carrying out firmware
update incrementally and roll back as needed.
- A job document created as part of AWS IoT job details the
remote operations the device needs to perform. This includes
shutting down rollouts based on timeouts, number of updates
per device among other things. Devices can use this
information to reject or accept firmware updates.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

## IOTREL08-BP04 Implement dynamic configuration management for devices

Deploying software changes to devices constitutes a high-risk
operation due to the recovery cost associated with remotely
deployed devices. When possible, prefer mechanisms for making
changes using command-and-control channels to reduce the risk
that comes with software deployments and firmware upgrades. This
approach enables you to push some changes to devices while
minimizing the risk of entering fault states that require
on-premises recovery actions. Configuration changes reduce the
amount of bandwidth compared to firmware updates.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL08-BP04-01** *Use cloud tools to command
and control devices. Changing configuration of devices is less
error prone and easier to trace back than updating
firmware.*

- Use Secure Tunneling or Systems Manager to facilitate
patching of the operating system instead of pushing a new
image to be loaded on the device.
- Use Device Shadows to command-and-control devices rather
than sending commands directly to device.
- Use AWS IoT Device Management jobs to rotate expiring device
certificates instead of pushing a new image with updated
certificates.
- [AWS IoT secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)
- [AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)

IOTREL09: How do you perform functional
testing for your IoT solution?

Testing IoT applications and backend services is expensive and
can be a challenge due to the large pool of physical, connected
devices required. Simulation helps test device integration and
IoT backend services, without the need for physical devices. You
can also monitor devices from the simulator or observe how
backend services are processing the data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

# IOTREL09 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL09-BP01 Implement device simulation to synthesize the entire flow of IoT data

Simulation scenarios can be configured to generate high volumes
of traffic, simulating a large number of IoT devices interacting
with the infrastructure simultaneously. By analyzing metrics
such as message throughput, latency, and error rates during load
testing, users can identify potential bottlenecks and optimize
their infrastructure for reliability and responsiveness.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL09-BP01-01** *To augment your production
device deployments, implement IoT simulations on Amazon Elastic Compute Cloud (Amazon EC2) as device canaries across several AWS Regions.*

- These device canaries are responsible for mirroring several
of your business use cases, such as simulating error
conditions like long-running transactions, sending
telemetry, and implementing control operations. The device
simulation framework must output extensive metrics,
including but not limited to successes, errors, latency, and
device ordering and then transmit all the metrics to your
operations system.
- You must implement a variety of device simulation canaries
that continue to test common device interactions directly
against your production system. Device canaries assist in
narrowing down the potential areas to investigate when
operational metrics are not met. Device canaries can be used
to raise preemptive alarms when the canary metrics fall
below your expected SLA.

**Prescriptive guidance
IOTREL09-BP01-02** *The IoT Device Simulator
simulates diverse scenarios to validate the logic and
functionality of their IoT applications.*

- Launch fleets of virtually connected devices from a
user-defined template and then simulate them to publish data
at regular intervals to AWS IoT
- Simulation scenarios can be utilized to generate synthetic
data for training ML models used in IoT applications. By
simulating different environmental conditions, device
behaviors, and data patterns, users can generate diverse
datasets to train and validate ML algorithms.

For more information see,
[IoT
Device Simulator](https://aws.amazon.com/solutions/implementations/iot-device-simulator/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

# IOTREL10 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL10-BP01 Use cloud service capabilities to handle component failures

An IoT design consists of device software, connectivity and
control services, and analytics services. Test the entire IoT
landscape for resiliency, starting with device firmware, data
flow, the cloud services used, and error handling. Vendors have
services integrated with each other to provide a simplified
integration and fault handling.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTREL10-BP01-01** *Understand and apply the
standard libraries available to manage your device firmware or
software.*

- Devices can be built on
[FreeRTOS](https://aws.amazon.com/freertos/)
which provides connectivity, messaging, power management and
device management libraries that are tested for reliability
and designed for ease of use.
- AWS provides IoT device SDKs and Mobile SDKs, comprised of
open-source libraries, developer guides, sample apps, and
porting guides to help you build IoT solutions with AWS IoT
and your choice of hardware systems.

**Prescriptive guidance
IOTREL10-BP01-02** *Use log levels appropriate
to the lifecycle stage of your workload.*

- AWS IoT logs can be set up per region and per account with
the logging level set to DEBUG during product development
phase to provide insights on data flow and resources used.
This data can be used to improve the IoT system security and
performance.
- [AWS IoT Secure Tunneling](https://aws.amazon.com/blogs/iot/securing-amazon-freertos-devices-at-scale-with-infineon-optiga-trust-x/) can be used to test and debug
devices that are behind a restrictive firewall in the field.

IOTREL11: How do you verify that your
IoT device operates with intermittent connectivity to the
cloud?

IoT solution reliability must also encompass the device itself.
Devices may be deployed in remote locations and deal with
intermittent connectivity, or loss in connectivity, due to a
variety of external factors that are out of your IoT
application's control.

For example, if an ISP is interrupted for several hours, how
will the device behave and respond to these long periods of
potential network outage? Implement a minimum set of embedded
operations on the device to make it more resilient to the
nuances of managing connectivity and communication to AWS IoT Core.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

# IOTREL11 — Reliability

**Pillar**: Reliability  
**Best Practices**: 3

---

## IOTREL11-BP01 Implement device logic to automatically reconnect to the cloud

Your IoT device will likely become disconnected due to
networking issues, power loss, or other unforeseen situations.
This might be true of a single device, or for your entire fleet
of devices. Whether a single device or the entire fleet becomes
disconnected, the following best practices will make sure that
the entire fleet is able to automatically reconnect.

**Level of risk exposed if this best
practice is not established:** Medium

Prescriptive guidance IOTREL11-BP01-01 *Use an
exponential backoff with jitter and retry logic to connect
remote devices to the cloud.*

Consider implementing a retry mechanism for IoT device software.
The retry mechanism should have exponential backoff with a
randomization factor built in to avoid retries from multiple
devices occurring simultaneously. Implementing retry logic with
exponential backoff with jitter allows the IoT devices to more
evenly distribute their traffic and help prevent them from
creating unnecessary peak traffic.

**Prescriptive guidance
IOTREL11-BP01-02** *Use device edge software
and the SDK to use built in exponential backoff
logic.*

- Exponential backoff logic is included in the AWS SDK,
including the AWS IoT Device SDK, and edge software, such as
AWS IoT Greengrass Core and FreeRTOS.
- [AWS SDK handles the exponential backoff](https://docs.aws.amazon.com/general/latest/gr/api-retries.html)
- [AWS IoT Device SDK C: MQTT](https://docs.aws.amazon.com/freertos/latest/lib-ref/c-sdk/mqtt/mqtt_config.html) uses IOT-MQTT-RETRY-MS-CEILING
for setting maximum retry interval limit.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL11-BP02 Design devices to use multiple methods of communication

Devices hardware can be designed to make use of multiple
networking interfaces. Consider a device that provides multiple
network interface types when selecting device hardware according
to the needs of your IoT application.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL11-BP02-01** *Establish alternate
network channels to meet requirements.*

- Have a separate failover network channel to deliver critical
messages to AWS IoT. Failover channels can include Wi-Fi,
cellular networks, or a wireless personal network.
- For low latency workload, use
[AWS Wavelength](https://aws.amazon.com/wavelength/) for 5G devices and
[AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to keep your cloud services closer to the
user.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL11-BP03 Automate alerting for devices that are unable to reconnect

In the event that devices are unable to reconnect, fleet
operators are to be automatically notified to begin
troubleshooting the device and to re-establish device
connectivity.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL11-BP03-01** *Implement logic in the
cloud to notify the device operator if a device has not
connected for an extended period of time.*

- [Lifecycle
events](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html) can be enabled to monitor device lifecycle
events, including connect and disconnect events.
- AWS IoT Fleet Indexing can be used to identify device
connectivity status
- AWS IoT Events can be used to monitor devices remotely.
- Remote monitoring using AWS IoT Events:
[CloudWatch
Metrics connector](https://docs.aws.amazon.com/greengrass/v1/developerguide/cloudwatch-metrics-connector.html)

IOTREL12: How do you verify that
required data is transmitted to the cloud after a device has
been disconnected?

Your IoT device must be able to operate without internet
connectivity. To make sure that required data is not lost when
devices become disconnected from the cloud, they should store
important messages durably offline and, once reconnected, send
those messages to AWS IoT Core. Connection to the cloud can be
intermittent and devices should be designed to handle this.
Choose devices with firmware designed for intermittent cloud
connection and that have the ability to store data on the device
if you cannot afford to lose the data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

# IOTREL12 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL12-BP01 Provide adequate device storage for offline operations

Store important messages durably offline and, once reconnected,
send those messages to the cloud. Device hardware should have
capabilities to store data locally for a finite period to help
prevent loss of information.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL12-BP01-01** *Use the device edge
software capabilities for storing data locally.*

- Design your edge applications according to your device
constraints to store and forward critical data when devices
become disconnected from the cloud.

If your device has sufficient storage available, your
application may implement a local cache of messages
written to disk to make sure that data is not lost when
the device is operating in a disconnected state.
- To make sure that the disk is not accidentally filled
with this persisted data, design your application to
make use of only a set amount of total disk space, and
consider implementing a FIFO overwrite strategy.
- When the device comes back online, a background process
should be implemented to transmit data that was stored
locally to the cloud, emptying the local cache as
messages are successfully published to the cloud.

- If using AWS IoT Greengrass for device software, AWS IoT Greengrass components can help collect, process, and export
data streams, including when devices are offline.

Messages collected on the device are queued and
processed in FIFO order.
- By default, AWS IoT Greengrass Core stores unprocessed
messages destined for AWS Cloud targets in memory.
- Configure AWS IoT Greengrass to cache messages to the
local file system so that they persist across core
restarts.
- AWS IoT Greengrass stream manager makes it easier and
more reliable to transfer high-volume IoT data to the
AWS Cloud.
- [Configure
AWS IoT Greengrass core](https://docs.aws.amazon.com/greengrass/v1/developerguide/gg-core.html)
- [Manage
data streams on AWS IoT Greengrass Core](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-manager.html)
- [AWS IoT Greengrass Developer Guide](https://docs.aws.amazon.com/greengrass/v1/developerguide/what-is-gg.html)
- [Run
Lambda functions on the AWS IoT Greengrass core](https://docs.aws.amazon.com/greengrass/v1/developerguide/lambda-functions.html)
- The ETL with AWS IoT Greengrass solution accelerator
(For more information, see
[Unlock
the value of embedded security IP to build secure IoT
products at scale](https://aws.amazon.com/blogs/iot/unlock-the-value-of-embedded-security-ip-to-build-secure-iot-products-at-scale/))helps to quickly set up an edge
device with AWS IoT Greengrass to perform extract,
transform, and load (ETL) functions on data gathered
from local devices before being sent to AWS.

**Prescriptive guidance
IOTREL12-BP01-02** *Consider using AWS IoT SiteWise for data coming from disparate industrial
equipment.*

AWS IoT SiteWise Edge software collects local equipment data and
sends it to AWS IoT SiteWise in the cloud. You can use SiteWise
Edge gateways to collect data from multiple OPC Unified
Architecture (UA) servers and publish it to AWS IoT SiteWise.
The SiteWise Edge gateway runs on either AWS IoT Greengrass V2
or Siemens Industrial Edge can be used to cache data locally in
the event of intermittent network connectivity. You can
configure the maximum disk buffer size used for caching data. If
the cache size exceeds the maximum disk buffer size, the
connector discards the earliest data from the queue. For more
information, see
[Use
AWS IoT SiteWise Edge gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL12-BP02 Synchronize device states upon connection to the cloud

IoT devices are not always connected to the cloud. Design a
mechanism to synchronize device states every time the device has
access to the cloud. Synchronizing the device state to the cloud
allows the application to get and update device state easily, as
the application doesn't have to wait for the device to come
online.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL12-BP02-01** *Use a digital devices
state representation to synchronize device state using the below
capabilities.*

- AWS provides device shadow capabilities that can be used to
synchronize device state when the device connects to the
cloud. The AWS IoT Device Shadow service maintains a shadow
for each device that you connect to AWS IoT and is supported
by the AWS IoT Device SDK, AWS IoT Greengrass core, and
FreeRTOS.
- [Synchronizing
device shadows](https://docs.aws.amazon.com/iot/latest/developerguide/using-device-shadows.html) - Device SDKs and the AWS IoT Core
take care of synchronizing property values between the
connected device and its device shadow in AWS IoT Core.
- [AWS IoT Greengrass](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) – AWS IoT Greengrass core software
provides local shadow synchronization of devices and these
shadows can be configured to sync with cloud.
- [FreeRTOS](https://docs.aws.amazon.com/greengrass/latest/developerguide/security.html) -
The FreeRTOS device shadow API operations define functions
to create, update, and delete AWS IoT Device Shadow services.

**Prescriptive guidance
IOTREL12-BP02-02** *Use MQTT Persistent
Sessions.*

MQTT's persistent session feature allows a client to retain its
subscriptions, undelivered messages, and other session data
across different connections. If a device (client) disconnects
and later reconnects, it can pick up where it left off without
having to re-subscribe or miss critical messages.

IOTREL13: How do you remotely adjust
message frequency to your IoT devices?

Because IoT is an event-driven workload, your application code
must be resilient to handling known and unknown errors that can
occur as events are permeated through your application. A
well-architected IoT application has the ability to log and
retry errors in data processing. An IoT application will archive
data in its raw format. By archiving data, valid and invalid, an
architecture can more accurately restore data to a given point
in time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

# IOTREL13 — Reliability

**Pillar**: Reliability  
**Best Practices**: 3

---

## IOTREL13-BP01 Configure cloud services to reliably handle message processing

When devices send an unexpected influx of messages, or when your
device fleet grows, it becomes necessary to add error handling
to support the reliable delivery of messages in your IoT
applications.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL13-BP01-01** *Configure error actions
with IoT Rules Engine.*

With the IoT rules engine, an application can enable an IoT
error action. If a problem occurs when invoking an action, the
rules engine will invoke the error action. This allows you to
capture, monitor, alert, and eventually retry messages that
could not be delivered to their primary IoT action. We recommend
that an IoT error action is configured with a different AWS
service from the primary action. Use durable storage for error
actions such as Amazon SQS or Amazon Kinesis.

Beginning with the rules engine, your application logic should
initially process messages from a queue and validate that the
schema of that message is correct. Your application logic should
catch and log any known errors and optionally move those
messages to their own dead-letter queue (DLQ) for further
analysis. Have a catch-all IoT rule that uses Amazon Data Firehose to transfer raw and unformatted messages into
long-term storage in Amazon S3, or Amazon Redshift for data
warehousing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL13-BP02 Send logs directly to the cloud

It is common for device developers to log application errors at
the edge, but that increases the complexity for reliably
troubleshooting device issues, especially as device fleets
increase in size. Storing log files on the device itself then
requires a specialized process to request a device to transmit
logs, which it may not be able to accomplish during failure
states, or to open remote access to the device to access those
logs. Instead, transmit logs as events to the cloud and automate
alerts based on those log events to improve reliability of your
IoT applications.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL13-BP02-01** *Use MQTT to send log
messages to the cloud.*

Regardless of the underlying cause for device failures, if the
device can communicate to your cloud application, it should send
diagnostic information about the hardware failure to AWS IoT Core using a diagnostics topic. If the device loses connectivity
because of the hardware failure, use Fleet Indexing with
connectivity status to track the change in connectivity status.
If the device is offline for extended periods of time, trigger
an alert that the device may require remediation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL13-BP03 Design devices to allow for remote configuration of message publication frequency

Devices may be developed with initial assumptions around how
frequently messages need to be delivered, such as at a rate of
1Hz (1 message per second). When the device is deployed into its
destination environment, whether that is in a smart home
setting, or a remote industrial asset, the network variability
and other challenges may then require the need to alter this
publication frequency. Planning ahead to allow for this type of
configuration to be remotely managed will help with the
reliability aspect of your IoT architecture.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL13-BP03-01** *Use either AWS IoT Jobs or
AWS IoT device shadows to allow for the remote configuration of
message publication frequency.*

AWS IoT Jobs can be used to push remote configuration changes to
devices. AWS IoT device shadows can also be used to maintain
device configuration. AWS IoT device SDKs provide support for
integration with both of these features.

IOTREL14: How do you plan for disaster
recovery in your IoT workloads?

When companies run their core production operations and
cybersecurity functions in the cloud, it is important to design
resilience at the edge & cloud in IoT systems. IoT
implementations must allow for loss of internet connectivity,
local data storage and processing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

# IOTREL14 — Reliability

**Pillar**: Reliability  
**Best Practices**: 3

---

## IOTREL14-BP01 Design server software to initiate communication only with devices that are online

Communication should be server initiated with devices that are
online rather than client-server requests. It enables you to
design client software to accept commands from the server.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance IOTREL14-
BP01-01** *Design client software to accept
commands from the server.*

- FreeRTOS provides pub/sub and shadow library to connected
devices.
- AWS IoT Core provides device shadow capability to persist
device states.
- AWS IoT Device Registry contains a list of devices connected
to AWS IoT Core. AWS IoT Device Registry lets you manage
devices by grouping them.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL14-BP02 Implement multi-Region support for IoT applications and devices

Cloud service providers have the same service in multiple
Regions. You can use this architecture to divert device data to
a Regional endpoint that is in not down. Data consumers should
be enabled in all Regions that consume the diverted device data.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL14-BP02-01** *Architect device software
to reach multiple Regions in case one is not
available.*

- AWS IoT is available in multiple Regions with different
endpoints. If an endpoint is not available, divert device
traffic to a different endpoint.
- AWS IoT configurable endpoints can be used with Amazon Route 53 to divert IoT traffic to a new Regional endpoint.
- AWS IoT Configurable Endpoints:
[Domain
configurations](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable.html)

**Prescriptive guidance
IOTREL14-BP02-02** *Enable device
authentication certificates in multiple Regions.*

- AWS IoT provides devices with authentication certificates to
verify on connection. Deploy the device certificates in the
Regions where the device will connect.
- Setup the cloud side IoT data consumers to accept and
process data in multiple Regions.
- AWS IoT device registration:
[Simplify
IoT device registration and easily move devices between AWS accounts with AWS IoT Core Multi-Account
Registration](https://aws.amazon.com/blogs/iot/simplify-multi-account-device-provisioning-and-certificate-authority-registration-using-aws-iot-core/).

**Prescriptive guidance
IOTREL14-BP02-03** *Use device services in all
Regions the device connects to.*

- AWS IoT Rules Engine diverts device data to use multiple
services. Set up AWS IoT Rules Engine in the respective
Regions to divert traffic to the appropriate services.
- [Rules
for AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

## IOTREL14-BP03 Use edge devices to store and analyze data

Edge storage can provide additional storage for device data.
Data can be stored at the edge during large-scale network events
and streamed later, when network is available.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL14-BP03-01** *Use an edge device as a
connection point to store and analyze data.*

- AWS IoT Greengrass can be used for local processing for
serverless functions, containers, messaging, storage, and
machine learning inference.
- Data can be stored in AWS IoT Greengrass and sent to the
network when it's available.
- [AWS IoT Greengrass features](https://aws.amazon.com/greengrass/features/) and components such a Stream
Manager can be used to help design resilient solutions at
the edge.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/failure-management.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
