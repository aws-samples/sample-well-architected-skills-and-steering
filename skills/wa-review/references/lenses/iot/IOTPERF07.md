# IOTPERF07 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

## IOTPERF07-BP01 Optimize network topology for distributed devices

Carefully design the network topology to minimize latency and
foster efficient data transfer between edge devices and the
cloud. This may involve implementing edge gateways or hubs,
using AWS IoT Greengrass, and optimizing network configurations
based on the geographical distribution and density of devices.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**
IOTPERF07-BP01-01 *Configure
deployed devices to connect to the lowest latency cloud endpoint
of your application's cloud infrastructure.*

To minimize latency and provide optimal performance, configure
edge devices to connect to the nearest edge endpoint of your
application's cloud infrastructure. This can be achieved by
using AWS IoT Core's device data endpoint feature, which allows
devices to connect to the closest AWS IoT Core endpoint based on
their geographic location. By connecting to the nearest cloud
endpoint, data transmission times are reduced, improving
responsiveness and overall application performance, especially
for time-sensitive or latency-critical use cases.

### Resources

- [AWS IoT Coredata plane endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/networking-and-content-delivery.html*

---

## IOTPERF07-BP02 Perform timely connectivity verification for devices

Implement mechanisms to regularly verify and monitor the
connectivity status of IoT and edge devices to quickly detect
connectivity issues. This can be achieved through periodic
heartbeat messages, device shadows, or using AWS IoT Device Management fleet indexing for continuous monitoring and
alerting.

Timely connectivity verification enables proactive
troubleshooting and minimizes potential disruptions in data flow
between edge devices and the cloud. AWS IoT Device Management
fleet indexing can query a group of devices and aggregate
statistics on device records that are based on different
combinations of device attributes, including state,
connectivity, and device violations. With fleet indexing, you
can organize, investigate, and troubleshoot your fleet of
devices.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**
IOTPERF07-BP02-01 *Set up a
heartbeat message publishing routine to analyze connectivity
status and quality.*

Alternatively, to effectively monitor device connectivity,
implement a heartbeat mechanism where devices periodically send
messages containing a monotonically increasing counter and a
timestamp. This approach enables validating message loss by
detecting gaps in the counter sequence and assessing consecutive
message delays by analyzing timestamp differences. The heartbeat
frequency can be adjusted based on the application's
requirements. This mechanism provides visibility into
connectivity status, message integrity, and latency for
individual devices, facilitating proactive issue detection and
remediation. This second approach may be useful for custom
monitoring of devices that require specific polling frequencies.
However, it is important to notice there is a significant
tradeoff associated with this choice in terms of higher
messaging costs when compared to the usage of the optimized AWS IoT Device Management fleet indexing.

### Resources

- [Fleet
indexing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/networking-and-content-delivery.html*

---
