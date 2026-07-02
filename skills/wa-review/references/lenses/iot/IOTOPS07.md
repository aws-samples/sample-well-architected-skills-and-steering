# IOTOPS07 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## IOTOPS07-BP01 Enable appropriate responses to events

Key operational data elements are those data points that convey
some notion of operational health of your application by
classifying events. Detecting operational events early can
uncover unforeseen risks in your application and give your
operations team a head start to help prevent or reduce business
interruption. By defining a minimum set of logs, metrics, and
alarms, your operations team can provide a faster incident
response which reduces risks of business disruption.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS07-BP01-01** *Configure logging to capture
and store at least error-level events.*

- Use AWS IoT service logging options to capture error events
in Amazon CloudWatch Logs
- Your devices create telemetry or diagnostic messages that
are not stored in the registry or the device's shadow.
Instead, these messages are delivered to AWS IoT using a
number of MQTT topics. To make this data actionable, use the
AWS IoT rules engine to route error messages to your
automated remediation process and add diagnostic information
to IoT messages. The rules engine inspects the status of a
message and if it is an error, it starts the Step Function
workflow to remediate the device based off the error message
detail payload.

**Prescriptive guidance
IOTOPS07-BP01-02** *Create a dashboard for your
responders to use in investigations of operational events to
rapidly pinpoint the period of time when errors are
logged.*

- Group clusters of error events into buckets of time to
quickly identify when surges of errors were captured.
- Drill down into clusters of errors to identify any patterns
to signal for triage response.

**Prescriptive guidance
IOTOPS07-BP01-03** *Configure an automated
monitoring and alerting tool to detect common symptoms and
warnings of operational issues.*

- For example, configure AWS IoT Device Defender to run a
daily audit on at least the high and critical checks.
- Configure an Amazon SNS topic to notify a team email list,
paging tool, or operations channel when AWS IoT Device Defender
reports non-compliant resources in an audit.

For more information, see [AWS IoT Device Defender Audit](https://docs.aws.amazon.com/iot/latest/developerguide/device-defender-audit.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/operate.html*

---

## IOTOPS07-BP02 Use data-driven auditing metrics to detect if any of your IoT devices might have been broadly accessed

Monitor and detect the abnormal usage patterns and possible
misuse of devices and automate the quarantine steps.
Programmatic methods to detect and quarantine devices from
interacting with cloud resources enable teams to operate a fleet
in a scalable way while minimizing a dependency on active human
monitoring.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS07-BP02-01** *Use monitoring and logging
services to detect anomalous behavior. Once you detect the
compromised device, run programmatic actions to quarantine
it.*

- Disable the certificate for further investigation and revoke
the certificate to help prevent the device from any future
use.
- Use AWS IoT CloudWatch metrics and logs to monitor for
indications of misuse. If you detect misuse, quarantine the
device so it does not impact the rest of the system.
- Use AWS IoT Device Defender to identify security issues and
deviations from best practices

IOTOPS08: How do you segment your device
operations in your IoT application?

You need to segment your device fleet to pinpoint operational
challenges and direct incident response to the appropriate
responder. Device fleet segmentation enables you to identify
conditions under which devices operate sub optimally and
minimize response time to security events.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/operate.html*

---
