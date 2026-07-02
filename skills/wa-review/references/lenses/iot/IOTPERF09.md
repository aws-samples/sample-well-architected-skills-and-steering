# IOTPERF09 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## IOTPERF09-BP01 Have device inventory in the IoT system that centralizes device configuration and diagnostics

As the number of devices increases, monitor for performance
bottlenecks when all the devices connect to the cloud-side.
These devices could generate a large aggregate amount of data.
To verify that you understand where to improve, gather device
diagnostics to determine the immediate health of a device and
any other devices in its proximity.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTPERF09-BP01-01**
*Deploy an agent to the
device to start capturing the relevant diagnostic
data.*

- For microprocessor-based applications, consider deploying
the AWS Systems Manager Agent (SSM Agent) so that you can
continuously monitor your device's performance metrics.
- There are sample agents provided to use on the device-side
(device or gateway). If device-side diagnostic metrics
cannot be obtained, then it is possible to obtain limited
cloud-side metrics. For example:

TCP connections

Connections
- Local-interface

- Listening TCP/UDP ports

Listening-TCP/UDP-ports
- Interface

- Network statistics

Bytes-in/out
- Packets-in/out
- Network-statistics

- To define and monitor metrics that are unique to your fleet
or use case, use custom metrics, such as number of devices
connected to Wi-Fi gateways, charge levels for batteries, or
number of power cycles for smart plugs.

**Prescriptive guidance
IOTPERF09-BP01-02**
*Measure, evaluate, and
optimize device firmware updates with strategies such as canary
deployment.*

Firmware updates are critical to keep your IoT devices
performant over time, but these updates might not always have
the expected impact. As you deploy firmware updates to your
devices, monitor your KPIs to verify that updates do not have
any unintended impacts to the performance of your hardware
devices or to your IoT applications.

- Deploy new firmware to a limited set of devices, and monitor
the impact on performance before rolling the update out to
the entire fleet. Stop deployment if degradation is
detected.
- Use AWS IoT Jobs to manage over-the-air (OTA) updates and
configure it to deploy to a limited set of devices.
- After the update, evaluate end-to-end performance of the
system using your previously identified KPIs.
- If performance characteristics appear to have been impacted
after the firmware release, use AWS IoT secure tunneling, a
feature of AWS IoT Device Management, to remotely
troubleshoot the device.
- Release additional firmware updates to remediate identified
issues.

### Resources

- [Custom
metrics](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-custom-metrics.html)
- [Using
Continuous Jobs with AWS IoT Device Management](https://aws.amazon.com/blogs/iot/using-continuous-jobs-with-aws-iot-device-management/)
- [Using
Device Jobs for Over-the-Air Updates](https://aws.amazon.com/blogs/iot/using-device-jobs-for-over-the-air-updates/)
- [Introducing Secure Tunneling for AWS IoT Device Management, a new
secure way to troubleshoot IoT devices](https://aws.amazon.com/blogs/iot/introducing-secure-tunneling-for-aws-iot-device-management-a-new-secure-way-to-troubleshoot-iot-devices/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture.html*

---
