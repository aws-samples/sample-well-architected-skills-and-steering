# IOTCOST03 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 5

---

## IOTCOST03-BP01 Select services to optimize cost

Understand how services use and charge for messaging, as well as
operating modes that offer cost benefits. Understanding service
billing characteristics can help you identify ways to optimize
messaging, which could result in considerable cost savings at
scale.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- Review your IoT architecture to find communication patterns
and scenarios that could map to service discount features.
- With AWS IoT Core Basic Ingest, you can publish directly to
a rule without messaging charges.
- Use your registry of things only for primarily immutable
data, such as serial Number.
- For your device's shadow, minimize the frequency of reads
and writes to reduce the total metered operation and your
operating costs.

### Resources

- [AWS IoT Rules Engine Basic Ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html)
- [AWS IoT
Pricing](https://calculator.aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST03-BP02 Implement and configure telemetry to reduce data transfer costs

Matching the precision of telemetry data, such as number of
decimal places, to the precision of the required calculation can
help address both the overall message size and the precision of
calculations.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- Reduce string lengths and decimal precision where feasible.
For example, strings sent regularly such as POWER or CHARGE
could be reduced to P or C strings. Similarly, decimal
values such as 21.25 or 71.86 could be reduced to 21 or 72
if the additional precision is not required for the
application. This is common in room temperature readings
where precision beyond is whole number is rarely required.
Across many millions of messages, the savings from removing
a few letters can make a significant difference in message
size and cost.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST03-BP03 Use shadow only for slow changing data

Shadow is used in IoT applications as a persistence mechanism of
device state. The shadow maintains data that remains consistent
across multiple points in time. Device shadow operations can be
billed and metered differently than publish or subscribe
messages. Reducing the shadow update frequency from the device
can reduce the number of billed operations while maintaining an
acceptable level of data freshness.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- Avoid using shadow as a guaranteed-delivery mechanism or for
continuously fluctuating data. As a workload scales up, the
cost of frequent shadow updates could exceed the value of
the data.
- Consider
[MQTT
Last Will and Testament (LWT)](https://docs.aws.amazon.com/iot/latest/developerguide/life-cycle-events.html) as a mitigation for the
risk of loss of device communication instead of using
shadow.
- Use the AWS Pricing Calculator to compare device shadow
interactions versus telemetry messages to understand cost
implications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST03-BP04 Group and tag IoT devices and messages for cost allocation

You can use an IoT billing group to tag devices by categories
related to your IoT application. Create tags that represent
business categories, such as cost centers. Visibility into
devices and messages by category makes cost dimensions easier to
understand and visualize.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- Use
[AWS IoT Core Billing Groups to tag IoT devices](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html) for cost
allocation. Add tracking elements to messages and devices to
help trace source, such as using MQTT5 User Properties to
add product model and serial number.
- Verify that your system can group and organize data by both
technical and business entity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST03-BP05 Implement and configure device messaging to reduce data transfer costs

Charges for different cloud and data transporter providers can
vary based on specifics of message size and frequency. IoT
workloads can cross multiple communication, such as cell
networks, and each layer can have its own metering and pricing
standards.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- Evaluate tradeoffs between message size and number of
messages. Frequency optimization is performed with payload
optimization to both accurately assess the network load and
identify adequate trade-offs between frequency and payload
size.
- For example, your devices might send one message per second.
If you could aggregate those messages on the device and send
five observations in a single message every five seconds,
that could drastically reduce your message count and cost.
- Use MQTT5 and topic aliases to reduce message size and cost
by replacing long topic strings with integers.
- Use the AWS Cost Calculator to compare the cost of using
messaging services like Kinesis and API Gateway to offload
components of your IoT workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---
