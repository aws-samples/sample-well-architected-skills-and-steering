# IOTSUS02 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 2

---

## IOTSUS02-BP01 Use the Basic Ingest feature in AWS IoT Core

With the Basic Ingest feature, you can securely send device data
to the AWS services supported by AWS IoT rule actions, without
incurring messaging costs. Basic Ingest optimizes data flow by
removing the publish/subscribe message broker from the ingestion
path, making it more cost-effective and resource-efficient.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

When ingesting data to AWS IoT Core, consider whether to use the
Basic Ingest feature or not. Use this approach if your
application does not require multiple subscribers for the data
being ingested.

For ingestion mechanisms other than Basic Ingest (such as the
Amazon Kinesis family of services), refer to the AWS IoT Lens
for guidance on which service is appropriate for which use case.
At this time, there are no additional sustainability best
practices for these services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-cloud.html*

---

## IOTSUS02-BP02 Choose an appropriate Quality of Service (QoS) level

Higher QoS levels involve additional network overhead for
acknowledgment and retransmission, which can increase power
consumption.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Use MQTT when you have IoT devices or other resource-constrained
environments that need to communicate efficiently and reliably
with a publish-subscribe messaging pattern. MQTT supports
different quality of service (QoS) levels for message delivery.
Consider using lower QoS levels (such as QoS 0) if the
reliability of message delivery is not critical for your use
case to reduce power consumption and network overhead.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-cloud.html*

---
