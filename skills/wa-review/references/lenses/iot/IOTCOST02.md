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
