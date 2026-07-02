# IOTPERF04 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## IOTPERF04-BP01 Have mechanisms to prioritize specific payload types

One strategy to address payload stream prioritization is to
create multiple queues or data streams to separate and channel
different payload types. For example, you could have dedicated
queues or streams for real-time sensor data, firmware updates,
and configuration messages. You can use this separation to apply
different prioritization policies and processing rules based on
the payload type's criticality and performance requirements.

Additionally, use protocol-level features such as Quality of
Service (QoS) in MQTT to provide reliable and prioritized
message delivery. By setting different QoS levels for different
payload types, you can prioritize the delivery of critical
messages over non-critical ones and transmit high-priority data
reliably and with minimal latency.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTPERF04-BP01-01**
*Create multiple queues
or data streams on the application side to channel different
payload types.*

When working with publisher-subscriber type architectures,
make sure to structure topics in the message broker following
a scope and verb approach. With this strategy, you can
subscribe to messages for a given scope (for example, a
device) or refine the subscription on a given scope and verb.

**Prescriptive guidance
IOTPERF04-BP01-02**
*Choose the right
Quality of Service (QoS) for publishing the
messages.*

- QoS 0 should be the default choice for all telemetry data
that can cope with message loss and where data freshness
is more important than reliability.
- QoS 1 provides reliable message transmission at the
expense of increased latency, ordered ingestion in case of
retries, and local memory consumption. It requires a local
buffer for all unacknowledged messages.
- QoS 2 provides once and only once delivery of messages but
increases the latency.

### Resources

- [Designing
MQTT Topics for AWS IoT Core](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.html)
- [OASIS
MQTT Version 5.0 QoS Specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901103)

IOTPERF05: How do you optimize
telemetry data ingestion?

IoT solutions drive rich analytics capabilities across vast
areas of crucial enterprise functions, such as operations,
customer care, finance, sales, and marketing. At the same
time, they can be used as efficient exit points for edge
gateways. Careful consideration must be given to architecting
highly efficient IoT implementations where data and analytics
are pushed to the cloud by devices and where machine learning
algorithms are pulled down to the device gateways from the
cloud.

Individual devices can be constrained by the throughput
supported over a given network. The frequency at which data is
exchanged must be balanced with the transport layer and the
ability of the device to optionally store, aggregate, and then
send data to the cloud. Send data from devices to the cloud at
timed intervals that align to the time required by backend
applications to process and take action on the data. For
example, if you need to see data at a one-second increment,
your device must send data at a more frequent time interval
than one second. Conversely, if your application only reads
data at an hourly rate, you can make a trade-off in
performance by aggregating data points at the edge and sending
the data every half hour.

The speed at which enterprise applications, business, and
operations need to gain visibility into IoT telemetry data
determines the most efficient point to process IoT data. In
network constrained environments where the hardware is not
limited, use edge solutions such as AWS IoT Greengrass to
operate and process data offline from the cloud. In cases
where both the network and hardware are constrained, look for
opportunities to compress message payloads by using binary
formatting and grouping similar messages together into a
single request.

For visualizations, several AWS services can be used. Amazon
Managed Service for Apache Flink can process streaming data in
real-time using SQL. Additionally, Quick provides
business intelligence dashboards for IoT data visualization
with minimal setup. AWS IoT SiteWise offers purpose-built
visualization tools for industrial equipment data. For
operational monitoring, Amazon Managed Grafana enables
time-series data visualization with pre-built IoT dashboards,
while Amazon CloudWatch Dashboards can display IoT metrics and
alarms.

Evaluating and optimizing your IoT application for its
specific needs, whether telemetry data ingestion or
controlling devices in the field, improves your outcomes in
balancing performance and reliability within your hardware and
network constraints. Separating the way that your application
handles data collected through sensors or device probes from
command-and-control flows helps achieve more reliable
performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-management.html*

---
