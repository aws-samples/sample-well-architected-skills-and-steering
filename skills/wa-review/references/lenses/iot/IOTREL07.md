# IOTREL07 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL07-BP01 Store data before processing

Make sure that the data from the devices is stored before
processing. As new requirements and capabilities are added,
stored data can be analyzed to meet the new requirements.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL07-BP01-01** *Use IoT Core Rules Engine
to send data to Firehose to batch and store data on
Amazon S3.*

- IoT Rules Engine can send data to Firehose to
batch and store data on Amazon S3. Intelligent tiering can be enabled in Amazon S3 to
reduce storage costs.
- Understand the latency to access data and choose the Region
to store the data in based on device location.
- If data will be processed in Amazon EC2 instances, consider
using the highly available and low-latency Amazon Elastic Block Store (Amazon EBS).
- NoSQL data can be stored in Amazon DynamoDB, which is a
key-value and document database that delivers single-digit
millisecond performance at scale. IoT Core Rules engine can
write all or part of an MQTT message to a DynamoDB table.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---

## IOTREL07-BP02Implement storage redundancy and failover mechanisms for IoT data persistence

There should be recovery plans for failures in storing and
accessing device data in the cloud. Understand the Recovery
Point Objective (RPO) and Recovery Time Objective (RTO) needed
by your application to access data to be used for analysis.

**Level of risk exposed if this best
practice is not established:** Medium

Prescriptive guidance IOTREL07-BP02-01 *Know how to
monitor and take action on cloud storage failures for IoT
data.*

- AWS Health Dashboard provides notification and
remediation guidance when AWS is experiencing events that
might impact you. Storage and access of data can be modified
based on the notification.
- Use Amazon CloudWatch Logs to trigger on events on writing
and reading data and take appropriate error handling action.

Use AWS IoT rules engine error actions to provision data
storage to other locations if primary storage is
unavailable.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/workload-architecture.html*

---
