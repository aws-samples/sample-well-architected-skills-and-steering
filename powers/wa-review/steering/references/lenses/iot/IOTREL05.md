# IOTREL05 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL05-BP01 Decouple IoT applications from the Connectivity Layer through an Ingestion Layer

In a well-architected IoT application, internal systems are
decoupled from the connectivity layer of the IoT system through
the ingestion layer. The ingestion layer is composed of queues
and streams that enable durable short-term storage while
allowing compute resources to process data independent of the
rate of ingestion.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL05-BP01-01** *Decouple application
consumers using streaming data services.*

To optimize throughput, use AWS IoT rules to route inbound
device data to services such as Amazon Kinesis Data Streams,
Amazon Data Firehose, Amazon Simple Queue Service, or
Amazon Managed Streaming for Apache Kafka before performing any
compute operations. Make sure that all the intermediate
streaming points are provisioned to handle peak capacity. This
approach creates the queueing layer necessary for upstream
applications to process data resiliently.

**Prescriptive guidance
IOTREL05-BP01-02** *Make use of MQTT features
to support reliable delivery of messages.*

AWS IoT Core supports MQTT persistent sessions, which store a
client's subscriptions and messages that haven't been
acknowledged by the client. Messages are stored according to
account limits, and the Persistent session expiry period what
can be adjusted between 1 hour and 7 days. This allows for
clients to publish messages that will be persisted by the AWS IoT Core Broker for up to the account limits and expiry period,
for later processing. Read more about persistent sessions in the
[AWS IoT Core developer guide](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html#mqtt-persistent-sessions).

IOTREL06: How do you facilitate reliable
processing and delivery of IoT messages across your
workload?

Data sent from devices should be processed and stored without
excessive loss. Services that queue and deliver IoT data to
compute and database services should be used to support the
processing of data. IoT devices send lots of data in small sizes
without order, and the cloud application should be able to
handle this.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---
