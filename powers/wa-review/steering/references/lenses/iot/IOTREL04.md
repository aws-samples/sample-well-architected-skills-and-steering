# IOTREL04 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL04-BP01 Target messages to relevant devices

Devices receive information from shadow updates, or from
messages published to topics they subscribe to. Some data are
relevant only to specific devices. In those cases, design your
workload to send messages to relevant devices only, and to
remove any data that is not relevant to those devices.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL04-BP01-01** *Preprocess data to support
the specific needs of the device.*

- Use AWS Lambda to pre-process the data and hone-in
specifically to attributes and variables that are needed by
the device to act upon

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

## IOTREL04-BP02 Implement retry and back off logic to support throttling by device type

Retry and back off logic should be implemented in a controlled
manner so that when you need to alter throttling settings per
device type, you can easily do it. Using data storage of any
chosen kind gives you flexibility on what data to publish down
to the device.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL04-BP02-01** *Use storage mechanisms
that enable retry mechanisms.*

- Using DynamoDB, you can hold data in key value format where
device ID is the key. Retry logic can be applied to only
certain device ID's.
- Using Amazon Relational Database Service, you
have the flexibility to use a variety of database engines.
The retry messages can have new real-time data augmented
with historic data from previous device interactions stored
in Amazon RDS.
- AWS IoT Events provides state machines with built-in timers
to hold back data and retry based on timers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---
