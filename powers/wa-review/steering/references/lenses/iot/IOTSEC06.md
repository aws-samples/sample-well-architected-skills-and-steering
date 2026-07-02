# IOTSEC06 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC06-BP01 Collect and analyze logs and metrics to capture authorization errors and failures to enable appropriate response

Device logs and metrics can provide your organization with the
insight to be operationally efficient with your IoT workloads by
identifying security events, anomalies, and issues from device
data. Record error-level messages from AWS IoT Core to provide
operational visibility to potential security issues.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC06-BP01-01** *Enable metrics and create
alarms that track authorization and error metrics.*

Observe the trends for these AWS IoT metrics:

- `Connect.AuthError`
- `PublishIn.AuthError`
- `PublishOut.AuthError`
- `Subscribe.AuthError`

Configure CloudWatch alarms for each of the preceding metrics to
alarm based on levels higher than normal for your workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/detective-controls.html*

---

## IOTSEC06-BP02 Send alerts when security events, misconfiguration, and behavior violations are detected

Audit the configuration of your devices and detect and alert
when a device behavior or IoT application processing differs
from the expected behavior. Audit logs provide visibility into
operational data that can indicate potential security issues
active in the device fleet.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC06-BP02-01** *Enable metrics to detect
security events from the data plane.*

Create IoT Device Defender security profiles to generate events
which could indicate security risks. AWS IoT Device Defender
[Ccoud-side
metrics](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/detect-cloud-side-metrics.html) report on device behavior observed by AWS IoT Core. You can detect events based on configured rules. For
example, create a security profile in AWS IoT Device Defender,
that detects unusual device behavior that may be indicative of a
unauthorized access by continuously monitoring activity between
the device and AWS IoT Core. You can specify normal device
behavior for a group of devices by setting up behaviors (rules)
for these metrics. AWS IoT Device Defender monitors and
evaluates each data point reported for these metrics against
user-defined behaviors (rules) and alerts you if behavior
outside the defined rules settings is detected.

**Prescriptive guidance
IOTSEC06-BP02-02** *Enable auditing to check
misconfigurations.*

Audit checks are necessary to determine that devices stay
configured according to best practices throughout their
lifecycle. For instance, it is necessary to audit devices
regularly on basic checks such as logging, use of shared
certificates and unique device identifiers. AWS IoT Device Defender audit checks can help you to continuously audit
security configurations for compliance with security best
practices and your own organizational security policies. Some of
the auditing capabilities that are supported natively are
`LOGGING-DISABLED-CHECK`, `IOT-POLICY-OVERLY-PERMISSIVE-CHECK`,
`DEVICE-CERTIFICATE-SHARED-CHECK`, and
`CONFLICTING-CLIENT-IDS-CHECK`.

**Prescriptive guidance
IOTSEC06-BP02-03** *Facilitate alerting on a
behavior violation.*

Enable alarms or notifications when the device behavior is
anomalous based on configured IoT Device Defender rules. AWS IoT Device Defender Security Profiles can be set up to define limits
for metric values so that alerts are signaled if device behavior
is observed to be outside of these limits.

**Prescriptive guidance
IOTSEC06-BP02-04** *Capture device-side
behavior metrics and alert on device behavior
violations.*

AWS IoT Device Defender can be configured to monitor device-side
metrics which are reported to AWS IoT Device Defender from
messages sent to AWS IoT Core by the device. Additional
configuration and processing may be needed in the device in
order to generate and send these device-side metrics. When
available, these metrics can be used to alert you when behavior
within the device is determined to be outside of normal ranges.
Use AWS IoT Device Defender rules to monitor activity within the
device. Appropriate action can then be taken, such as moving the
device to a maintenance state or performing a remote OTA update
on the device.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/detective-controls.html*

---

## IOTSEC06-BP03 Alert on non-compliant device configurations and remediate using automation

Implement continuous monitoring to track device configurations
and metrics. Regular auditing helps maintain security baselines
and identify necessary updates as technologies evolve and new
threats emerge. For example, cryptographic algorithms once known
to provide secure digital signatures for device certificates can
be weakened by advances in the computing and cryptoanalysis
techniques.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC06-BP03-01** *Verify regular auditing is
enabled for identifying configuration issues.*

Audit checks are necessary to determine that devices stay
configured according to best practices throughout their
lifecycle. For instance, it is necessary to audit devices
regularly on basic checks such as logging, use of shared
certificates and unique device identifiers. AWS IoT Device Defender audit checks can help you to continuously audit
security configurations for compliance with security best
practices and your own organizational security policies. Some of
the auditing capabilities that are supported natively are
`LOGGING-DISABLED-CHECK`,`IOT-POLICY-OVERLY-PERMISSIVE-CHECK`,
`DEVICE-CERTIFICATE-SHARED-CHECK`, and
`CONFLICTING-CLIENT-IDS-CHECK`. A full list of audit features can
be found in
[Audit checks](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/device-defender-audit-checks.html).

**Prescriptive guidance
IOTSEC06-BP03-02** *Use automation to
remediate issues.*

Investigate issues by providing contextual and historical
information about the device such as device metadata, device
statistics, and historical alerts for the device. For example,
you can use AWS IoT Device Defender built-in mitigation actions
to perform mitigation steps on Audit and Detect alarms.
Mitigations can include actions such as adding things to a thing
group, replacing default policy version, and updating a device
certificate. Another possible action is to enable a mitigation
to re-enable logging and publish the finding to Amazon SNS
should the `LOGGING-DISABLED-CHECK` find that logging is not
enabled. Defining the actions taken when an alert is signaled is
done by creating Lambda functions which are invoked through
Amazon SNS when the alert is sent.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/detective-controls.html*

---
