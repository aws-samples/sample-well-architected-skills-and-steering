# IOTSEC05 — Security

**Pillar**: Security  
**Best Practices**: 1

---

## IOTSEC05-BP01 Perform certificate lifecycle management

Certificate lifecycle includes different phases such as
creation, activation, refresh or rotation, revocation,
deactivation, or expiry. An automated workflow can be put in
place to identify certificates that need attention, along with
remediation actions.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC05-BP01-01** *Document your plan for
managing certificates.*

As explained earlier, X.509 certificates help to authenticate
devices and AWS IoT Core to one another and to set up encrypted
communications between the edge and cloud. Planning the
lifecycle management of device certificates is essential. Enable
auditing and monitoring for compromise or expiration of your
device certificates. Determine how frequently you need to
refresh/rotate device certificates, audit cloud or
device-related configurations and permissions to make sure that
security measures are in place. For example, use AWS IoT Device Defender to monitor the health of the device certificates and
different configurations across your fleet. AWS IoT Device Defender can work in conjunction with AWS IoT Jobs to help
enable refresh/rotation of certificates which are nearing their
expiration.

**Prescriptive guidance
IOTSEC05-BP01-02** *Use certificates signed by
your trusted intermediate CA for on-boarding devices*

As a best practice, the all-root CA keys must be locked and
protected to secure the chain of trust. Device certificates
should be generated using an intermediate CA to sign the device
certificates. Define a process to programmatically manage
intermediate CA certificates as well. For example, enable AWS IoT Device Defender Audit to report on your intermediate CAs
that are revoked but device certificates are still active or if
the CA certificate quality is low. You can thereafter use a
security automation workflow using mitigation actions in AWS IoT Device Defender to resolve the issues.

**Prescriptive guidance
IOTSEC05-BP01-03** *Secure provisioning claims
(just-in-time provisioning or registration) private keys and
disable the certificate in case of misuse and record the event
for further investigation.*

- Monitor provisioning claims for private keys when using just
in time provisioning or just-in-time registration.
- Be sure to monitor usage on the device as well as in AWS IoT Core.
- For example:

Use AWS IoT CloudWatch metrics and logs to monitor for
indications of misuse. If you detect misuse, disable the
provisioning claim certificate so it cannot be used for
device provisioning.
- Use AWS IoT Device Defender to identify security issues
and deviations from best practices.

### Resources

- [Getting started
with AWS IoT Device Defender](https://docs.aws.amazon.com/iot/latest/developerguide/vulnerability-analysis-and-management.html)
- [Just-in-Time
Registration of Device Certificates on AWS IoT](https://aws.amazon.com/blogs/iot/just-in-time-registration-of-device-certificates-on-aws-iot/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/identity-and-access-management.html*

---
