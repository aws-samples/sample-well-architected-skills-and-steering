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
