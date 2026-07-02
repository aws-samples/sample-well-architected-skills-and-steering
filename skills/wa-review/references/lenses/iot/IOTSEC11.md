# IOTSEC11 — Security

**Pillar**: Security  
**Best Practices**: 2

---

## IOTSEC11-BP01 Build incident response mechanisms to address security events at scale

There are several formalized incident management methodologies
in common use. The processes involved in monitoring and managing
incident response can be extended to IoT devices. For instance,
AWS IoT Device Management capabilities provide fleet analysis
and activity tracking to identify potential issues, in addition
to mechanisms to enable an effective response.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC11-BP01-01** *Make sure that IoT devices
are searchable by using a device management solution.*

Devices should be grouped by dynamic attributes, such as
connectivity status, firmware version, application status, and
device health.

**Prescriptive guidance
IOTSEC11-BP01-02** *Quarantine any device that
deviates from expected behavior.*

Inspect the device for potential issues in the configurations,
firmware or applications using device logs or metrics. If a risk
or anomaly is detected, the device can be diagnosed remotely
provided that capability exists. For example, Configure AWS IoT
Secure Tunneling to remotely diagnose a fleet of devices.

If remote diagnosis is not sufficient or available, the other
option is to push a security patch, application or firmware
upgrade while the device is quarantined. When sending code to
devices, the best practice is to sign the firmware or software
and to verify the signature at the device prior to applying the
update or code. This allows devices to detect if the code has
been modified in transit. For example, With Code Signing for AWS IoT, you can sign code that you create for IoT devices supported
by Amazon FreeRTOS and AWS IoT device management. In addition,
the signed code can be valid for a limited amount of time to
avoid further manipulation.

**Prescriptive guidance
IOTSEC11-BP01-03** *Over the air (OTA) update
should be configured and staged for deployment activation during
regular maintenance.*

Whether it's a security patch or a firmware update, an update to
a config file on a device, or a factory reset, you need to know
which devices in your fleet have received and processed any of
your updates, either successfully or unsuccessfully. In
addition, a staged rollout is recommended to reduce the scope of
a bad update. Rollouts should be able to be aborted with devices
returning to a failsafe condition on a failed update. For
example, you can use AWS IoT Jobs to roll out OTA updates of
security patches and device configurations in a staged manner
with required rollout and abort configuration settings.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/incident-response.html*

---

## IOTSEC11-BP02 Require timely vulnerability notifications and software updates from your providers

Components in a device bill of materials (BOM), such as secure
elements (SEs) or a trusted platform module (TPM) for key or
certificate storage, can make use of updatable software
components. Some of this software might be contained in the
Board Support Package (BSP) assembled for your device. You can
help to mitigate device-side security issues quickly by knowing
where the security-sensitive software components are within your
device software stack, and by understanding what to expect from
component suppliers with regard to security notifications and
updates.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC11-BP02-01** *Make sure that your IoT
device manufacturer provides security-related notifications to
you, and provides software updates in a timely manner to reduce
the associated risks of operating hardware or software with
known security vulnerabilities.*

Ask your suppliers about their product conformance to the
[Common
Criteria for Information Technology Security Evaluation](https://www.commoncriteriaportal.org/index.cfm).
In addition, use AWS Partner Device Catalog where you can find
devices and hardware to help you explore, build, and go to
market with your IoT solutions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/incident-response.html*

---
