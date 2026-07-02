# IOTCOST04 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## IOTCOST04-BP01 Plan expected usage over time

When architecting to match supply against demand, proactively
plan your expected usage over time, and the limits that you are
most likely to exceed. Factor those limit increases into your
future planning.

**Level of risk exposed if this best
practice is not established:** Low

Prescriptive guidance

Evaluating new AWS features helps you optimize cost by analyzing
how your devices are performing. You can use this analysis to
make changes to how your devices communicate with your IoT.

To optimize the cost of your solution through changes to device
firmware, review the pricing components of AWS services, such as
AWS IoT, determine where you are below billing metering
thresholds for a given service, and then weigh the trade-offs
between cost and performance.

IOTCOST05: How do you optimize payload
size between devices and your IoT system to save
cost?

IoT applications must balance the networking throughput that can
be realized by end devices with the most efficient way that data
should be processed by your IoT application. We recommend that
IoT deployments initially optimize data transfer based on the
device constraints. Begin by sending discrete data events from
the device to the cloud, making minimal use of batching multiple
events in a single message. Later, if necessary, you can use
serialization frameworks to compress the messages prior to
sending it to your IoT system.

From a cost perspective, the MQTT payload size is a critical
cost optimization element for AWS IoT Core. An IoT message is
billed in five KB increments, up to 128 KB. For this reason,
each MQTT payload size should be as close to possible to any
five KB. For example, a payload that is currently sized at 6 KB
is not as cost efficient as a payload that is ten KB because the
overall costs of publishing that message is identical despite
one message being larger than the other.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/managing-demand-and-supplying-resources.html*

---
