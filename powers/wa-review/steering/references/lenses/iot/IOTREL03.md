# IOTREL03 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL03-BP01 Down sample data to reduce storage requirements and network utilization

Data should be down sampled where possible to reduce storage in
the device and lower transmission costs and reduce network
pressure.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL03-BP01-01** *Use device edge software
capabilities for down sampling.*

- Use compression as a means of down sampling data

Data transmitted to the cloud can be in JSON format, or
in other formats such as Protocol Buffers.

- Using AWS IoT Greengrass for device software to down sample
data.

Applications built using Components can be used on AWS IoT Greengrass to down sample the data before sending it
to the cloud.
- [ETL
with AWS IoT Extract, Transform, Load with AWS IoT Greengrass Solution Accelerator](https://aws.amazon.com/iot/solutions/etl-accelerator/) helps to quickly
set up an edge device with AWS IoT Greengrass to perform
extract, transform, and load (ETL) functions on data
gathered from local devices before being sent to AWS.

IOTREL04: How do you optimize and
control message delivery frequency to IoT devices?

Devices can be restricted in message processing capacity and
messages from the cloud might need to be throttled. The
cloud-side message delivery rate might need to be architected
based on the type of devices that are connected.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---
