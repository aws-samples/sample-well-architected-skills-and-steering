# IOTOPS06 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

## IOTOPS06-BP01 Implement monitoring to capture logs and metrics

Monitoring is an important part of maintaining the reliability,
availability, and performance of your IoT solutions. It is
highly recommended to collect monitoring data from all parts of
your IoT solution to make it easier to debug a multi-point
failure, if one occurs. Create a monitoring plan that answers
the questions such as:

- Which resources to monitor (edge, device connectivity,
remote operations, or device health)?
- Which tools to use?
- Who has to be notified should an incident or event occurs?

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS06-BP01-01** *Use Amazon CloudWatch to
monitor your IoT fleet.*

To support operational insights to your cloud application,
generate dashboards for all metrics collected from IoT Core and
IoT Device Management. These metrics are available through
Amazon CloudWatch Metrics. In addition, CloudWatch Logs contain
information such as total successful messages inbound, messages
outbound, connectivity success, and errors.

**Prescriptive guidance IOTOPS06-BP01-02** *Capture the default metrics emitted by your IoT services and configure alarms for metrics that might indicate business interruption.*

For example, your business deploys a thousand IoT sensors and your operations team wants to be alerted if sensors can no longer connect to the cloud and send telemetry.

- Your IT team administering the AWS account reviews the AWS IoT Core metrics and notes the following metrics to
monitor: `Connect.AuthError`, `Connect.ClientError`, `Connect.ClientIDThrottle`, `Connect.ServerError`, and `Connect.Throttle`.
Activity in these metrics constitutes alerting and
investigation.
- Your IT team uses CloudWatch to configure new alarms on
these metrics when for any period the metrics' SUM of Count
is greater than zero.
- Your IT team configures an Amazon SNS topic to notify their
paging tool when the new CloudWatch alarms changes status.

For more detail, see
[Monitor
AWS IoT alarms and metrics using Amazon CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring-cloudwatch.html)

**Prescriptive guidance
IOTOPS06-BP01-03** *Use unified monitor dashboard
for IoT metrics.*

The unified dashboard in AWS IoT monitor allows identification of potential connectivity and operational problems, reducing the time associated with fleet troubleshooting procedures.
The connectivity metrics dashboard available in the AWS IoT monitor, consolidates frequently used metrics from AWS IoT Core, such as successful connections, inbound or outbound messages published, and connection request authorization failures.
A guided workflow enables AWS IoT Device Management's Fleet Indexing feature and adds widgets for connected device counts, percentage of devices disconnected, and disconnect reasons to the same page.
AWS IoT provides fleet-level and device-level insights driven from the Thing Registry and Device Shadow service through search capabilities such as AWS IoT Fleet Indexing. The ability to search across your fleet eases the operational overhead of diagnosing IoT issues at the device-level or fleet-wide level.

**Prescriptive guidance
IOTOPS06-BP01-04** *Implementing tracing between
all the resources or modules.*

- Visualizing the entire path of requests, from entry to exit
helps quickly identifying where failures or performance
issues occur.
- In addition to Amazon CloudWatch, it's crucial to
instrument to emit trace data. This process can provide
further insights into your workload's behavior and
performance. Integrate X-Ray into your application to gain
insights into its behavior, understand its performance, and
pinpoint bottlenecks. Utilize X-Ray Insights for automatic
trace analysis.

AWS Lambda Powertools is a suite of utilities that helps with
implementing observability best practices without needing to
write additional custom code. Powertools provides three core
utilities:

- *Tracing* provides a
simpler way to send traces from functions to

[AWS X-Ray](https://aws.amazon.com/xray/). It provides visibility into function calls,
interactions with other AWS services, or external HTTP
requests. You can add attributes to traces to allow
filtering based on key information.
- *Logging* provides a custom
logger that outputs structured JSON. It allows you to pass
in strings or more complex objects, and takes care of
serializing the log output.
- *Metrics* simplify
collecting custom metrics from your application, without the
need to make synchronous requests to external systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS06-BP02 Capture and monitor application performance at the edge

Implement tracing and observability methods that provide granular visibility into edge application health, performance, and root cause analysis. By seamlessly connecting the observability strategy for cloud-based applications with those running at the edge, organizations can gain end-to-end visibility and insights for improved application performance.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS06-BP02-01** *Emit device side metrics using
agents.*

- AWS IoT Device Defender Detect can collect, aggregate, and
monitor metrics data generated by AWS IoT devices to
identify devices that exhibit abnormal behavior. Securely
deploy the AWS IoT SDK version two on your AWS IoT connected
devices or device gateways to collect device-side metrics.
- You can use AWS IoT Device Client to publish metrics as it
provides a single agent that covers the features present in
both AWS IoT Device Defender and AWS IoT Device Management.
- Publish device-side metrics to the
[reserved
topic](https://docs.aws.amazon.com/iot/latest/developerguide/reserved-topics.html#reserved-topics-device-defender) in AWS IoT for

[AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/reserved-topics.html#reserved-topics-device-defender) to collect and evaluate.

**Prescriptive guidance
IOTOPS06-BP02-02** *Collect application logs for
tracing capabilities.*

- [AWS Distro
for OpenTelemetry](https://aws.amazon.com/otel/) seamlessly collects and exports
metrics and traces to AWS monitoring services. Distro for
OpenTelemetry Collector is an agent that runs on your
application environment. When it is integrated with AWS IoT Greengrass, this combination extends your observability
capabilities to both edge and cloud applications at scale,
providing consistent and seamless tracing across your
application infrastructure. This integrated approach
delivers real-time visibility into application performance

For more information, see
[Monitor
edge application using AWS IoT Greengrass Monitor edge application performance using AWS IoT Greengrass and AWS Distro for OpenTelemetry](https://aws.amazon.com/blogs/iot/monitor-edge-application-performance-using-aws-iot-greengrass-and-aws-distro-for-opentelemetry/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS06-BP03 Monitor the status of your IoT devices

You need to be able to track the status of your devices. This
includes operational parameters and connectivity. You need to
know whether devices have disconnected intentionally or not.
Monitoring the status of your device fleet is important in
helping troubleshoot device software operation and connectivity
disruptions.

Design a state machine for the device connectivity states, from
initialization and first connection, to frequent communication
(like keep-alive messages) and final state before going offline.
Lifecycle events, such as connection and disconnection, can be
used to observe and analyze device behavior over a period of
time. Additionally, periodic keep-alive messages can track
device connectivity status.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS06-BP03-01** *Subscribe to lifecycle events
and monitor the connections using keep-alive
messages.*

- Capture messages from the IoT message broker whenever a
device connects or disconnects. Being able to tell the
difference between a clean and dirty disconnect is useful in
many scenarios where the devices don't maintain a constant
connection to the broker.
- Based on the use case and device constraints, have the
device send periodic keep-alive messages to AWS IoT Core and
monitor, and analyze the keep-alive messages for anomalies.
- Make sure that the frequency of sending keep-alive messages
is not causing any network storms (perhaps by introducing
some jitter) in the network or causing rate limits.
- Configure your devices to
communicate their status periodically. Implement
Last Will and Testament (LWT) messages and periodic device
keep-alive messages.

**Prescriptive guidance
IOTOPS06-BP03-02** *Implement a well-designed
device connectivity state machine*

- Make sure that the device communicates when it first comes
online and just prior to going offline.
- Implement a wait state for lifecycle events. When a
disconnect message is received, wait a period of time and
verify that the device is still offline before taking
action.
- Specify the interval with which each connection should be
kept open if no messages are received. AWS IoT drops the
connection after that interval unless the device sends a
message or a ping.

**Prescriptive guidance
IOTOPS06-BP03-03** *Use device connection and
disconnection status for anomaly detection.*

- Use connectivity data patterns from devices to detect
anomalous behavior in their communication patterns.

### Resources

- [AWS IoT Now Supports WebSockets, Custom Keepalive Intervals, and Enhanced Console](https://aws.amazon.com/about-aws/whats-new/2016/01/aws-iot-now-supports-websockets-custom-keepalive-intervals-and-enhanced-console/)
- [AWS Solutions Library: Real-Time IoT Device Monitoring with Managed Service for Apache Flink](https://aws.amazon.com/solutions/implementations/real-time-iot-device-monitoring-with-kinesis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS06-BP04 Use device state management services to detect status and connectivity patterns

Edge and cloud-side management services monitor and analyze
parameters, such as device connectivity status and latency, to
help in providing diagnostics and predicting anomalies.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS06-BP04-01** *Monitor device state and
connectivity patterns.*

- Use (or develop as needed) device, gateway, edge, and cloud
management tools that allow monitoring the fleet of devices
- Use logging and monitoring features at all processing
points—device, gateway, edge, and cloud, to get a complete
picture of device connectivity patterns.

### Resources

- [Monitoring
your IoT fleet using CloudWatch](https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/)

- [Building
Observability in IoT applications using AWS Lambda Powertools, AWS X-Ray, Amazon CloudWatch](https://www.youtube.com/watch?v=moRlNXpdhm8)
- [Getting
Aggregate Information of Devices with AWS IoT Device Management Fleet Indexing](https://aws.amazon.com/blogs/iot/getting-aggregate-information-of-devices-with-aws-iot-device-management-fleet-indexing/)
- [AWS IoT Core - Managing thing indexing](https://docs.aws.amazon.com/en_us/iot/latest/developerguide/managing-index.html)
- [Security
monitoring for connected devices across OT, IoT, edge, cloud (TDR222)](https://www.youtube.com/watch?v=-2c83ql5KXg)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---
