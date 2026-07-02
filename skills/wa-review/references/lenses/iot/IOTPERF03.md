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
