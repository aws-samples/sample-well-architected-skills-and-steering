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
