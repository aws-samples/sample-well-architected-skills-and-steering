# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 6

---

# IOTCOST01 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

## IOTCOST01-BP01 Use a data lake for raw telemetry data

A *data lake* brings different data sources
together and provides a common management framework for
browsing, viewing, and extracting the sources. An effective data
lake enables IoT cost management by storing data in the right
format for the right use case. With a data lake, storage and
interaction characteristics can be aligned to a specific dataset
format and required interfaces.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- For each telemetry stream, identify key features of
telemetry using the 4Vs of big data—velocity, volume,
veracity, and variety.
- Map each stream into the appropriate storage capability.
- For example, a stream that sends an MQTT message with a JSON
payload every second would be an ideal candidate for being
batched, compressed then stored in Amazon S3.
- For high velocity data streaming, utilize IoT Basic Ingest
and AWS IoT rules to route data to the appropriate storage
service such as Amazon Timestream or Kinesis Data Streams.

### Resources

- [AWS storage types](https://aws.amazon.com/products/storage/)
- [AWS re:Invent 2018: Building with AWS Databases: Match Your
Workload to the Right Database (DAT301)](https://www.youtube.com/watch?v=hwnNbLXN4vA)
- [AWS IoT rule actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST01-BP02 Provide a self-service interface for end users to search, extract, manage, and update IoT data

With flexible cloud computing resources, pay-as-you-go pricing,
and strong identity and encryption controls, your organization
should allow groups to define and share data models in the
format that makes the most sense for them. Self-service
interfaces encourage experimentation and speed up change by
removing barriers for teams to gain access to the data they need
to make decisions.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- Use an architecture that allows various end users to easily
find, obtain, enhance, and share data
- Use a subscriber model, which allows teams to subscribe to
data feeds and receive notification of updates, to reduce
the need for active polling and re-synching with data
sources

### Resources

- [Creating a data lake from a JDBC source in AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-tutorial.html)
- [AWS Data Lake Quick Start](https://aws.amazon.com/quickstart/architecture/data-lake-foundation-with-aws-services/)
- [AWS Data Exchange offers subscriptions to third-party data
sources with notification on updates](https://aws.amazon.com/data-exchange/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST01-BP03 Track and manage the utilization of data sources

Applications and users evolve over time, and IoT solutions can
generate large volumes of data quickly. As your application
matures, it's important for cost management of your IoT workload
to track that data collected is still being used. Consistent
tracking and review of data utilization provides an objective
basis for cost optimization decisions.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- Track access rates and storage trends for your data lake
sources.
- Use automated guidance tools, such as
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and

[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), to identify under-utilized or
resizable components of your workload. AWS Cost explorer has
a forecast feature that predicts how much you will use AWS
services over the forecast time period you selected.
- Use
[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) and

[Cost
Anomaly detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to help prevent surprise bills.

### Resources

- [Monitoring
Amazon S3 metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudwatch-monitoring.html)
- [Find
cost of your S3 buckets using AWS Cost Explorer](https://aws.amazon.com/premiumsupport/knowledge-center/s3-find-bucket-cost/)
- [Forecast
your spend using Cost explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-forecast.html)
- [Best
practices for AWS Budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-best-practices.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST01-BP04 Aggregate data at the edge where possible

Data aggregation is an architectural decision that can have
impacts on data fidelity. Aggregations should be thoroughly
reviewed with engineering and architectural teams before
implementation. If the device can aggregate data before sending
for processing using methods such as combining messages or
removing duplicate or repeating values, that can reduce the
amount of processing, the number of associated resources, and
associated expense.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- A common mechanism includes combining multiple status
updates to a final status, or combining a series of
measurements generated by the device into a single message.
- For example, 10000 of device telemetry data might be
packaged as one 10000 message, two 5000 messages, or ten
separate 1000 messages. Each packaging format has
implications outside of cost such as network traffic (ten
1000 messages will each add their own header messaging as
opposed to a single 10000 message with one header) and the
impact of a lost or delayed message. Optimizing message size
should consider how a lost message impacts the functional or
non-functional characteristics of the system.
- Use [cost
calculators](https://calculator.aws/#/) to model different approaches for message
size and count

IOTCOST02: How do you optimize cost of
raw telemetry data?

Raw telemetry is an original source for analytics but can also
be a major component of cost. Analyze the flow and usage of your
telemetry to identify the right service and handling process
required. Select storage and processing mechanisms that match
the needs of your specific telemetry case.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

# IOTCOST02 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

## IOTCOST02-BP01 Use lifecycle policies to archive your data

When selecting an automated lifecycle policy for data, there are
tradeoffs to consider. For example, do you want to optimize for
speed to market or cost? In some cases, it's best to optimize
for speed rather than investing in upfront cost optimization.
Use your organization's data classification strategies to define
a lifecycle policy to take raw telemetry measurements through
various services. Setting milestones by time sets expectations
and encourages aggregation and production of data over mere
collection.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- Check your organization's data management policy for
requirements on retention, deletion, and encryption, and
align your retention policies and tools with those
guidelines.
- S3 Lifecycle policies or
[S3
Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) can move the data to the most
cost-effective Amazon S3 storage class or Amazon Glacier
for long-term storage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST02-BP02 Evaluate storage characteristics for your use case and align with the right services

Not all data needs to be stored in the same way, and data
storage needs change through a data item's lifecycle. A growing
fleet of devices can exponentially scale its messaging rate and
device operation traffic. This scaling of message volumes can
also mean an increase in storage costs.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- For data at high scale of devices, time, or other
characteristics, consider a data warehouse such as Amazon Redshift or Amazon S3 with Amazon Athena. The data
partitioning and tiering features of AWS storage services
can help reduce storage costs.
- For data at lower scale of time, devices, or other
characteristics, consider Amazon DynamoDB, Amazon OpenSearch Service (OpenSearch Service), or Aurora for short-term
historical data. Use your data lifecycle policies to
optimize what is kept in the short-term storage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

## IOTCOST02-BP03 Store raw archival data on cost effective services

Using the right storage solution for a specific data type will
align costs with usage.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- Use an object store, such as Amazon S3, for raw archival
storage. Object stores are immutable and often more
efficient and cost-effective than block storage, especially
for data which doesn't require editing.
- Avoid costs by using a schema-on-read service, such as
Amazon Athena, to query the data in its native form. Using
Athena can help reduce the need for large-scale storage
arrays or always-on databases to read raw archival data.

IOTCOST03: How do you optimize cost of
interactions between devices and your IoT cloud
solution?

Interactions to and from devices can be a significant driver of
your workload's overall cost. Understanding and optimizing
interactions between devices and cloud solution can be a
significant factor of cost management.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/cost-effective-resources.html*

---

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

# IOTCOST05 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## IOTCOST05-BP01 Balance networking throughput against payload size to optimize efficiency

The specific use case drives the balance between frequency and
payload size. Consider and test different payload optimization
strategies. Additionally, consider trade-offs between
compression and processing overhead.

**Level of risk exposed if this best
practice is not established: Low**

**Prescriptive guidance**

- Shorten values while keeping them legible. If five digits of
precision are sufficient, then you should not use 12 digits
in the payload.
- Use serialization frameworks to compress payloads to smaller
sizes if you do not require IoT rules engine payload
inspection.
- Send data less frequently and aggregate messages together
within the billable increments. For example, sending a
single two KB message every second can be achieved at a
lower IoT message cost by sending two separate two KB
messages every other second.

This approach has tradeoffs that should be considered before
implementation. Adding complexity or delay in your devices may
unexpectedly increase processing costs. A cost optimization
exercise for IoT payloads should only happen after your solution
has been in production and you can use a data-driven approach to
determine the cost impact of changing the way data is sent to
AWS IoT Core.

IOTCOST06: How do you optimize the costs
of storing the current state of your IoT device?

Well-Architected IoT applications have a virtual representation
of the device in the cloud. This virtual representation is
composed of a managed data store or specialized IoT application
data store. In both cases, your end devices must be programmed
in a way that efficiently transmits device state changes to your
IoT application. For example, your device should only send its
full device state if your firmware logic dictates that the full
device state may be out of sync and would be best reconciled by
sending all current settings. As individual state changes occur,
the device should optimize the frequency it transmits those
changes to the cloud.

In AWS IoT, device shadow and registry operations are metered in
one KB increments and billing is per million access and modify
operations. The shadow stores the desired or actual state of
each device and the registry is used to name and manage devices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/managing-demand-and-supplying-resources.html*

---

# IOTCOST06 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## IOTCOST06-BP01 Optimize shadow operations

Cost optimization processes for device shadows and registry
focus on managing how many operations are performed and the size
of each operation. If your operation is cost-sensitive to shadow
and registry operations, explore ways to optimize shadow
operations. For example, for the shadow you could aggregate
several reported fields together into one shadow message update
instead of sending each reported change independently. Grouping
shadow updates together reduces the overall cost of the shadow
by consolidating updates to the service.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance**

- **Use named shadows:**
Separate logical elements, and reduce the size of updates.
- **Aggregate shadow updates:**
Look for opportunities to put several reported fields
together into one shadow message update instead of sending
each reported change independently. Grouping shadow updates
together reduces the overall cost of the shadow by
consolidating updates to the service.
- **Send only what is needed, when it is
needed:** For example, your device should only send
its full device state if your firmware logic dictates that
the full device state may be out of sync and would be best
reconciled by sending all current settings. As individual
state changes occur, the device should optimize the
frequency it transmits those changes to the cloud.
- **Immutable data:** Use the
[AWS IoT device registry](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) device attributes for immutable
data such as a serial number.
- **Minimize the frequency of reads and
writes:** Where possible, limit updates to device's
shadow document to reduce the total metered operations.
- **Choose the right service:**
Avoid using shadows as a guaranteed-delivery mechanism or
for continuously fluctuating data. Consider MQTT Last Will
and Testament (LWT) as a mitigation for the risk of loss of
device communication instead of using shadows.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/managing-demand-and-supplying-resources.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
