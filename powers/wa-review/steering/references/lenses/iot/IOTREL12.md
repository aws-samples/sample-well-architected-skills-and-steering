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
