# IOTOPS08 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS08-BP01 Use static and dynamic device attributes to identify devices with anomalous behavior

Anomalies in fleet operations might only surface when analyzing
metrics that aggregate across the boundaries of your static and
dynamic groups or attributes. For example, devices that are
running firmware version 2.0.10 and currently have a battery
level over 50%. Static and dynamic groups allow for identifying
and pinpointing devices in unique ways to monitor, analyze, and
take corrective actions on device behavior.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS08-BP01-01** *Pinpoint devices with unusual
communication patterns.*

- Use a combination of static and dynamic groups of devices to
perform fleet indexing to group devices and identify
behavioral patterns—connectivity status, and message
transmission.
- Use lifecycle events, device connectivity, and data
transmission patterns to detect anomalies and pinpoint
unusual behavior using techniques such as statistical
anomaly detection (for large fleet of devices).
- Once abnormal behavior has been identified, move rogue and
abnormal devices into a different group so that remedial
policies can be assigned and implemented on them.

### Resources

- [AWS IoT Core - Authorization](https://docs.aws.amazon.com/iot/latest/developerguide/iot-authorization.html)
- [AWS IoT - Device Defender](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/what-is-device-defender.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/operate.html*

---
