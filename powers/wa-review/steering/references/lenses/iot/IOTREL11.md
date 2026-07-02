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
