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
