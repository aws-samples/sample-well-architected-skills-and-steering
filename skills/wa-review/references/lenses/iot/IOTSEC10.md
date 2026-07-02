# IOTSEC10 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC10-BP01 Use encryption to protect IoT data in transit and at rest

For data at rest, the Storage Networking Industry Association
(SNIA) defines storage security as technical controls, which may
include integrity, confidentiality and availability controls
that protect storage resources and data from unauthorized users
and uses. Thus, it is required to protect the confidentiality of
sensitive data, such as the device identity, secrets, or user
data by encrypting it at rest. For data in transit, use a secure
transport mechanism such as TLS to protect the confidentiality
and integrity of data transmitted to and from your devices. Both
MQTT and HTTP communications can be protected using
TLS-protected forms of those protocols.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC10-BP01-01** *Require the use of device
SDKs or client libraries for the device to communicate to
cloud.*

Configure the IoT devices to communicate only over TLS to cloud
endpoints. For example, use AWS IoT Greengrass or Amazon
FreeRTOS SDKs to secure connectivity from your devices to AWS IoT Core over TLS 1.2. The AWS IoT Device SDK also enables the
use of TLS-protected secure communications over TLS 1.2.

**Prescriptive guidance
IOTSEC10-BP01-02** *Encrypt data and secrets
at rest on IoT devices.*

As explained earlier in section IOTSEC02-BP03-03, take advantage
of encryption utilities provided by the host operating system to
encrypt the data stored at rest in the local filesystem. In
addition, take advantage of Secure Elements (SEs) and TPMs.
Trusted execution environments (TEEs) can add storage
protections as well.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-protection.html*

---

## IOTSEC10-BP02 Use data classification strategies to categorize data access based on levels of sensitivity

Data classification and governance is the customer's
responsibility.

- Identify and classify data based on sensitivity collected
throughout your IoT workload and learn their corresponding
business use-case.
- Identify and act on opportunities to stop collecting unused
data, or adjusting data granularity and retention time.
- Consider a defense in depth approach and reduce human access
to device data.

For more information, see
[Manage
data streams on the AWS IoT Greengrass core](https://docs.aws.amazon.com/greengrass/v1/developerguide/stream-manager.html).

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC10-BP02-01** *Implement data
classification strategies for all data stored on devices or in
the cloud, as well as all data sent over the network. Process
data based on the level of sensitivity (for example, highly
classified, or personally identifiable data).*

Before architecting an IoT application, data classification,
governance, and controls must be designed and documented to
reflect how the data can be persisted on the edge or in the
cloud, and how data should be encrypted throughout its
lifecycle. For example, by using AWS IoT Greengrass stream
manager, you can define policies for storage type, size, and
data retention on a per-stream basis. For highly classified
data, you can define a separate data stream.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-protection.html*

---

## IOTSEC10-BP03 Protect your IoT data in compliance with regulatory requirements

Data governance is the rules, processes, and behavior that
affect the way in which data is used, particularly as it regards
openness, participation, accountability, effectiveness, and
coherence. Data governance practices for IoT is important as it
enables protecting classified data and complying with regulatory
obligations. It helps to determine what data needs protection,
or which data needs access control. For more information, see
[AWS Cloud Enterprise Strategy Blog: Using a Cloud Center of
Excellence (CCOE) to Transform the Entire Enterprise](https://aws.amazon.com/blogs/enterprise-strategy/using-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise/).

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC10-BP03-01** *Define specific roles for
personnel responsible for implementing IoT data
governance.*

For example, there might be a need for new roles to monitor
security, from both the functional and policy perspectives, to
control data when it moves from IoT environments to the cloud.

**Prescriptive guidance
IOTSEC10-BP03-02** *Define data governance
policies to monitor compliance with approved
standards.*

For example, you might define a policy that requires security
credentials to never be hardcoded, even on edge devices. Thus,
use only services like AWS Secrets Manager to retrieve secrets
in an encrypted manner.

**Prescriptive guidance
IOTSEC10-BP03-03** *Define clear
responsibilities to drive the IoT data governance
process.*

Multiple administrative roles can exist for a single system. For
instance, you may define roles for users who can replace
defective devices, and separate roles for users who can apply
security patches and upgrade device firmware. Note that roles
and responsibilities might change over the lifecycle of your IoT
systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-protection.html*

---
