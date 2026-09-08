# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 9

---

# IOTPERF01 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## IOTPERF01-BP01 Optimize for device hardware resources utilization

When designing IoT solutions, it's crucial to consider the
limited hardware resources available on edge devices, such as
processing power, memory, and battery life. Optimizing resource
utilization can significantly improve performance, efficiency,
and overall device longevity. AWS offers several services and
tools to help architects and developers optimize their solutions
for device hardware constraints.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTPERF01-BP01-01**
*Apply efficient runtimes
and code language for embedded devices.*

When making architectural decisions, thoroughly evaluate the
hardware capabilities of the target devices, and select
appropriate AWS services and configurations to optimize resource
utilization. This approach can lead to improved performance,
extended battery life, and cost savings by reducing cloud
processing and data transfer requirements. Some key tools to
consider in your device components are:

- **AWS IoT Device Client
SDK**: Provides lightweight, optimized libraries
for various programming languages. These libraries enable
efficient communication with AWS IoT Core and other AWS
services, minimizing resource consumption on edge devices.
For optimal performance, select based on your device
constraints, prioritizing lower-level languages for
battery-powered or resource-limited deployments:

**Embedded C SDK**: Best
for highly constrained devices with minimal RAM
(256KB+). Offers lowest memory footprint and power
consumption.
- **C++ SDK**: Balances
performance with developer productivity for embedded
Linux applications and gateways.
- **Python, JavaScript, or Java
SDKs**: Choose only when device resources
permit, as they trade performance for ease of
development, in general.

- **FreeRTOS:** A real-time
operating system for microcontrollers that is designed to be
resource-efficient and highly configurable. It allows
developers to tailor the OS to specific hardware
requirements, reducing the overall footprint.
- For more complex scenarios, AWS IoT Greengrass is an open
source edge runtime and cloud service that helps you build,
deploy, and manage device software. It manages devices to
act locally on the data they generate, run predictions based
on machine learning models, filter and aggregate device
data, and only transmit necessary information to the cloud.
By processing data locally, AWS IoT Greengrass minimizes
network latency and optimizes resource utilization,
particularly for time-sensitive or bandwidth-constrained
applications.

**Prescriptive guidance
IOTPERF01-BP01-02** *Leverage edge gateways as hubs to bridge
communications with the cloud.*

Edge gateways act as intermediaries, aggregating data from
multiple devices, performing local processing and filtering, and
intelligently managing communication with the cloud. This
approach offloads workloads from the cloud and reduces network
traffic and latency. By implementing edge gateways with AWS IoT Greengrass, you can deploy AWS Lambda functions, machine
learning models, and other application components directly on
these gateways, enabling real-time processing and
decision-making at the edge. This architecture not only enhances
performance but also improves resilience by allowing continued
operation during intermittent cloud connectivity, maintaining
data integrity, and minimizing potential disruptions.

### Resources

- [AWS IoT Device SDKs, Mobile SDKs, and AWS IoT Device
Client](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sdks.html)
- [AWS IoT Greengrass GitHub](https://github.com/aws-greengrass)
- [FreeRTOS
GitHub](https://github.com/FreeRTOS)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/architecture-selection.html*

---

# IOTPERF02 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

## IOTPERF02-BP01 Implement comprehensive monitoring solutions to collect performance data from your IoT devices

It is important to establish performance baselines and key
performance indicators (KPIs) specific to your IoT devices and
application requirements. These metrics may include device CPU
and memory utilization, network bandwidth consumption, battery
life, and embedded software-level metrics such as data
throughput and latency. Additionally, depending on the
programming language used, other memory metrics to consider are
heap usage or garbage collection frequency (Java), memory leak
detection and dynamic memory allocation ratio (C/C++), and
memory pool utilization (Python).

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTPERF02-BP01-01** *Analyze device metrics and compare to a
standard baseline.*

Collecting historical performance data from your devices helps
you understand regular behavior for your deployments and
potentially detect anomalies by using machine learning
strategies and tools. Use AWS IoT Device Defender to audit
device configurations, monitor device metrics, and detect
deviations from expected behavior. Additionally, services like
Amazon CloudWatch can be integrated to collect and analyze
device performance metrics, set alarms, and run automated
actions based on predefined thresholds.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/compute-and-hardware.html*

---

## IOTPERF02-BP02 Evaluate the runtime performance of your application

Application performance in production can be different from what
you observe in a controlled test environment. Actively analyzing
the performance of your application based on device health,
network latency, and payload size provides insight on how to
obtain performance improvements. By using different types of
metrics, the health of each device in a multi-device setting can
be obtained.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance IOTPERF02-BP02-1** *Analyze connection patterns, sensor data
and set up a device security profile to detect
anomalies.*

- Measuring changes in connection patterns of devices might
indicate some devices having a jittery network connection.
- Comparing device-side timestamps from multiple devices to
arrival times on the cloud-side might indicate local network
latency or additional hops in device path.

### Resources

- [Configure
AWS IoT logging](https://docs.aws.amazon.com/iot/latest/developerguide/configure-logging.html)
- [Gather system health telemetry data from AWS IoT Greengrass core
devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/telemetry.html)
- [AWS IoT Device Defender Detect](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-detect.html)
- [How to detect anomalies in device metrics and improve your
security posture using AWS IoT Device Defender](https://aws.amazon.com/blogs/iot/how-to-detect-anomalies-in-device-metrics-and-improve-your-security-posture-using-aws-iot-device-defender-custom-metrics/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/compute-and-hardware.html*

---

# IOTPERF03 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## IOTPERF03-BP01 Add timestamps to each published message

Timestamps (ideally in UTC time) help in determining delays that
might occur during the transmission of a message from the device
to the application. Timestamps can be associated with the
message and to fields contained in the message. If a timestamp
is included, the sent timestamp is recorded on the cloud-side
along with the sensor or event data.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTPERF03-BP01-01** *Add timestamps on the server side.*

- If the devices lack the capability to add timestamps to the
messages, consider using server-side features to enrich the
messages with timestamps that correspond to receiving the
message.
- For example, AWS IoT Rules SQL language provides a
`timestamp()` function to generate a timestamp when the
message is received.
- When using AWS IoT Greengrass:

Use AWS IoT Greengrass stream manager to batch timestamped
messages during connectivity interruptions while
preserving message sequence integrity
- Consider local AWS Lambda functions to process and
enrich messages with timestamps closer to the source,
minimizing latency between event occurrence and
timestamp application

**Prescriptive guidance
IOTPERF03-BP01-02** *Have a reliable time source on the
device.*

- Without a reliable time source, the timestamp can only be
used relative to the specific device. For example:

Devices should use the Network Time Protocol (NTP) to
obtain a reliable time when connected.
- Real-time clock (RTC) devices can be used to maintain an
accurate time while the device lacks network
connectivity.

- Depending on the application, timestamps can be added at the
message level or at the single payload field level. Delta
encoding can be used to reduce the size of the message when
multiple timestamps are included. Choosing the right
approach is a trade-off between accuracy, energy efficiency,
and payload size.

### Resources

- [AWS IoT Rules Developer Guide – timestamp() function](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html#iot-function-timestamp)
- [The Implementation of Timestamp, Bitmap and RAKE Algorithm on Data Compression and Data Transmission from IoT to
Cloud](https://ieeexplore.ieee.org/document/8528698)
- [Delta
encoding](https://en.wikipedia.org/wiki/Delta_encoding)

IOTPERF04: Is there a mechanism for
payload filtering or stream prioritization?

Firmware updates are critical, and filtering messages at the
edge might subject the devices to unnecessary load. This
result could be counterproductive from a power and memory
consumption perspective. Sending only messages that the device
makes use of reduces the load on the resources and supports
better performances.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-management.html*

---

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

# IOTPERF05 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

## IOTPERF05-BP01 Identify the ingestion mechanisms that best fit your use case

Identify which data ingestion method best fits with your use
case to obtain the best performance and operational complexity
tradeoff. Multiple mechanisms might be needed. This method
provides the optimal ingestion path for the data generated by
your devices to obtain the best trade-offs between performance
and cost.

**Level of risk exposed if this best
practice is not established: Low**

**Prescriptive guidance
IOTPERF05-BP01-01**
*Evaluate ingestion
mechanism for telemetry data.*

- Determine if the communication pattern is unidirectional
(device to backend) or bi-directional. For example:

HTTPS should be considered over MQTT when your device is
acting as an aggregator. Use multiple threads and
multiple HTTP connections to maximize the throughput for
high delay networks as HTTP calls are synchronous.

- Consider the APIs provided by the destination for your data
and adopt them if you can securely access them. For example:

AWS IoT SiteWise provides an HTTP API to ingest
operational data from industrial applications which
needs to be stored for a limited period and processed as
a time series with hierarchical aggregation
capabilities.
- Real-time video (for example, video surveillance
cameras) has specific characteristics that makes it more
suitable to ingest in a dedicated service, such as
Amazon Kinesis Video Streams.

- Consider the need for data to be buffered locally while the
device is disconnected and the transmission resumed as soon
as the connection is re-established. For example:

AWS IoT Greengrass stream manager provides a managed
stream service with local persistence, local processing
pipelines, and exporters to Amazon Kinesis Data Streams,
AWS IoT SiteWise, and Amazon S3.

- Consider the latency, throughput, and ordering
characteristics of the data you want to ingest. For example:

For applications with a high ingestion rate
(high-frequency sensor data) and where message ordering
is important, Amazon Kinesis Data Streams provides
stream-oriented processing capabilities and the ability
to act as temporary storage.
- For applications that do not have any real time
requirements (such as logging, large images) and when
the devices have the possibility to store data locally,
uploading data directly to Amazon S3 can be both
performant and cost efficient.

### Resources

- [Device
communication protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)
- [AWS IoT SiteWise adds support for 10 new industrial protocols
with Domatica EasyEdge integration](https://aws.amazon.com/blogs/iot/aws-iot-sitewise-adds-support-for-10-new-industrial-protocols-with-domatica-easyedge-integration/)
- [Amazon Kinesis Video Streams system requirements](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/system-requirements.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-management.html*

---

## IOTPERF05-BP02 Optimize data sent from devices to backend services

Optimizing the amount of data sent by the devices at the edge
allows the backend to better meet the processing targets set by
the business. Detailed data generated at the edge might have
little value for your application in its raw form.

**Level of risk exposed if this best
practice is not established: Medium**

**Prescriptive guidance
IOTPERF05-BP02-01**
*Aggregate or compress
data at the edge.*

Aggregate data points at the edge before sending them to the
cloud, such as performing statistical aggregation, frequency
histograms, signal processing to reduce payload size and
consequently the load of the data transmission.

### Resources

- [Use
AWS IoT SiteWise Edge gateways](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways-ggv2.html)
- [Cost-effectively ingest IoT data directly into Amazon S3 using AWS IoT Greengrass](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.html)

IOTPERF06: How do you efficiently make
sure stored data is usable by business?

You may have multiple databases in your IoT application, each
selected for attributes such as the write frequency of data to
the database, the read frequency of data from the database,
and how the data is structured and queried. Consider some of
these other criteria when selecting a database offering:

- Volume of data and retention period
- Intrinsic data organization and structure
- Users and applications consuming the data (either raw or
processed) and their geographical location and dispersion
- Advanced analytics needs, such as machine learning or
real-time visualizations
- Data synchronization across other teams, organizations,
and business units
- Security of the data at the row, table, and database
levels
- Interactions with other related data-driven events such as
enterprise applications, drill-through dashboards, or
systems of interaction

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-management.html*

---

# IOTPERF06 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## IOTPERF06-BP01 Store data in different tiers following formats, access patterns and methods

AWS has several database offerings that support IoT solutions.
For structured data, you should use Amazon Aurora, a highly
scalable relational interface to organizational data. For
semi-structured data that requires low latency for queries and
will be used by multiple consumers, use Amazon DynamoDB, a fully
managed, multi-Region database that provides consistent
single-digit millisecond latency and offers built-in security,
backup and restore, and in-memory caching.

AWS also provides specific data storage solutions for industrial
use cases with AWS IoT SiteWise. For equipment data, three tiers
are available:

- A hot storage tier optimized for real-time applications
- A warm storage tier optimized for analytical workloads
- A cold storage tier using Amazon Simple Storage Service
(Amazon S3) for operational data applications with high
latency tolerance

SiteWise helps you to reduce storage cost by keeping recent data
in the hot storage tier for at least 30 days and moving
historical data to a cost-optimized warm storage tier based upon
user-defined data retention policies.

Use Amazon SageMaker AI AI to build, train, and deploy machine
learning models based on your IoT data, in the cloud, and on the
edge using AWS IoT services, such as machine learning inference
in AWS IoT Greengrass.

Consider storing your raw formatted time series data in a data
warehouse solution such as Amazon Redshift. Unformatted data can
be imported to Amazon Redshift using Amazon S3 and Amazon Data
Firehose. By archiving unformatted data in a scalable, managed
data storage solution, you can begin to gain business insights,
explore your data, and identify trends and patterns over time.

In addition to storing and leveraging the historical trends of
your IoT data, you should have a system that stores the current
state of the device and provides the ability to query against
the current state of all of your devices. This supports internal
analytics and customer facing views into your IoT data.

The AWS IoT Device Shadow service is an effective mechanism to
store a virtual representation of your device in the cloud. AWS IoT Device Shadow service is best suited for managing the
current state of each device.

In addition, for internal teams that need to query against the
shadow for operational needs, use the managed capabilities of
fleet indexing, which provides a searchable index incorporating
your IoT registry and shadow metadata. If there is a need to
provide index-based searching or filtering capability to a large
number of external users, such as for a consumer application,
dynamically archive the shadow state using a combination of the
IoT rules engine, Amazon Data Firehose, and Amazon OpenSearch Service to store your data in a format that allows fine grained
query access for external users.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTPERF06-BP01-01**
*Create automated
mechanisms to transition data from tiers to implement
lifecycles.*

In an IoT solution, data often follows a lifecycle, transitioning from real-time ingestion to historical storage and archiving. To efficiently verify that stored data is utilizable throughout its lifecycle, it's crucial to implement automated mechanisms that transition data across different storage tiers based on predefined rules and policies.

For example, you can use AWS IoT rules and AWS Lambda functions to automatically route incoming real-time data to Amazon DynamoDB or Amazon Timestream for low-latency access and processing. As the data ages, you can initiate automated processes to transition it to Amazon S3 or Amazon Glacier for cost-effective, long-term archival storage.

Additionally, you can implement data retention policies and lifecycle management rules within your data storage solutions. For instance, in Amazon DynamoDB, you can configure Time to Live (TTL) settings to automatically expire and remove data after a specified period, improving the efficiency of storage utilization and reducing costs.

By creating automated mechanisms to transition data across different storage tiers, you can optimize storage costs, make data accessible based on its lifecycle stage, and maintain data integrity and availability for various analytical and operational use cases throughout the data lifespan.

### Resources

- [Managing
the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Backing
up and restoring Timestream tables: How it works](https://docs.aws.amazon.com/timestream/latest/developerguide/backups-how-it-works.html)
- [RetentionProperties](https://docs.aws.amazon.com/timestream/latest/developerguide/API_RetentionProperties.html)
- [Manage
data storage in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-storage.html)
- [Configure
storage settings in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-storage.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-management.html*

---

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

# IOTPERF08 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

## IOTPERF08-BP01 Load test your IoT applications

Applications can be complex and have multiple dependencies.
Testing the application under load helps identify problems
before going into production. Load testing your IoT applications
verifies that you understand the cloud-side performance
characteristics and failure modes of your IoT architecture.
Testing helps you understand how your application architecture
operates under load, identify performance bottlenecks, and apply
mitigating strategies prior to releasing changes to your
production systems.

**Prescriptive guidance
IOTPERF08-BP01-01**
*Simulate the real device
behavior.*

- A device simulator should implement the device behavior as
closely as possible. Test not only message publishing, but
also connections, reconnections, subscriptions, enrollment,
and other contextual events such as constrained network
bandwidth. Start testing at a lower load, and progressively
increase to 100%. Additionally, consider exercising the
workload beyond the traditional expected load by performing
stress tests.

Start the load test at a low percent of your estimated
total device fleet (for example, 10%).
- Evaluate the performance of your application using
operational dashboards created to measure end-to-end
delivery of device telemetry data and automated device
commands.
- Make any necessary changes to the application
architecture to achieve desired performance goals.
- Iterate these steps increasing the load until you get to
100%.
- For further workload development, consider performing
stress tests beyond usual load expected

### Resources

- [IoT
Device Simulator](https://aws.amazon.com/solutions/implementations/iot-device-simulator/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture.html*

---

## IOTPERF08-BP02 Monitor and manage your IoT service quotas using available tools and metrics

Be aware of the adjustable and unadjustable quotas of the AWS
service, and continuously monitor the key performance indicators
so that you can anticipate when actions must be taken to request
increases in the service quotas and re-evaluate your
architecture. Verify that your application operates within the
quotas of the services that you are building on to provide the
optimal performance to your users.

Monitoring keeps you aware of which service quotas you might be
reaching so that you can change your application to cope with
the unadjustable quotas or to request the increase of an
adjustable quota with sufficient lead time.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTPERF08-BP02-01**
*Be aware of the service
quotas of the different IoT services.*

- Pay attention to which limits are adjustable quotas and
which are unadjustable quotas as they require different
approaches. For example:

An unadjustable *quota*, such a
control plane request rate, requires changes in the
application behavior to avoid the event repeating too
often. Workarounds for unadjustable quotas might require
different design decisions, such as using multiple
accounts. It's good to know the unadjustable and
adjustable quotas in advance so that you can make these
design decisions as early as possible in the development
process.
- *Adjustable quotas* should be
monitored to anticipate the need for additional capacity
and provide sufficient notice so that a request for a
limit increase can be made well ahead of time. For
example:

For AWS IoT Core, alert on `RulesMessageThrottles`,
`Connect.ClientIDThrottle`, `Connect.Throttle`,
`PublishIn.Throttle`, `Subscribe.Throttle`,
`Unsubscribe.Throttle`.
- For AWS IoT Device Management, monitor active
continuous jobs, and active snapshot jobs in Service Quotas

### Resources

- [AWS IoT Core endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html)
- [AWS IoT Device Defender endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_defender.html)
- [AWS IoT Device Management endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html)
- [AWS IoT Greengrass V2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html)
- [AWS IoT SiteWise endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-sitewise.html)

IOTPERF09: How do you maintain
visibility over the distributed infrastructure
deployed?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
