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
