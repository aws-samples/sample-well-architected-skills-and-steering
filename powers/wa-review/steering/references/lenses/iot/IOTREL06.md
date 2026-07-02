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
