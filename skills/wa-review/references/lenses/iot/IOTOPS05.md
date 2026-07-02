# IOTOPS05 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

## IOTOPS05-BP01 Document how devices join your fleet from manufacturing to provisioning

Document the whole device provisioning process to clearly define
the responsibilities of different actors at different stages.
The end-to-end device provisioning process involves multiple
stages owned by different actors. Documenting the plan and
processes by which devices onboard and join the fleet affords
the appropriate amount of review for potential gaps.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS05-BP01-01** *Document each step (manual and
programmatic) of all the stages for the corresponding actors of
that stage and clearly define the sequence.*

- Identify the steps at each stage and the corresponding
actors.

Device assembly by hardware manufacturer.
- Device registration by service and solution provider.
- Device activation by the end user of the service or
solution provider.

- Clearly define and document the dependencies and specific
steps for each actor from device manufacturer to the end
user.
- Document whether devices can self-provision or are
user-provisioned and how you can make sure that newly
provisioned devices are yours.

**Prescriptive guidance
IOTOPS05-BP01-02** *Assign device metadata to
enable straightforward grouping and classification of devices in
a fleet.*

- The metadata can be used to group the devices in groups to
search and force common actions and behaviors.
- For example, you can assign the following metadata at the
time of manufacturing:

Unique ID
- Manufacturer details
- Model number
- Version or generation
- Manufacturing date

- If a particular model of a device requires a security patch,
then you can easily target the patch to the devices that are
part of the corresponding model number group. Similarly, you
can apply the patches to devices manufactured in a specific
time frame or belonging to a particular version or
generation.
- Along with creating a virtual representation of your device
in the device registry, as part of the operational process,
you must create thing types that encapsulate similar static
attributes that define your IoT devices. A thing type is
analogous to the product classification for a device. The
combination of thing, thing type, and device shadow can act
as your first entry point for storing important metadata
that will be used for IoT operations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS05-BP02 Use programmatic techniques to provision devices at scale

Scaling the onboarding and provisioning of a large device fleet
can be a bottleneck if there is even one manual step per device.
Programmatic techniques define patterns of behavior for
automating the provisioning process such that authenticated and
authorized devices can onboard at any time. This practice
provides a well-documented, reliable, and programmatic
provisioning mechanism that is consistent across all devices
devoid of human errors.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS05-BP02-01** *Embed provisioning claims into
the devices that are mapped to approval authorities recognized
by the provisioning service.*

- Generate a provisioning claim and embed it into the device
at the time of manufacturing.
- AWS IoT Core can generate and securely deliver certificates
and private keys to your devices when they connect to AWS IoT for the first time, using AWS IoT Fleet Provisioning.

**Prescriptive guidance
IOTOPS05-BP02-2** *Use programmatic bootstrapping
mechanisms if you are bringing your own certificates.*

- Determine if you will or won't have device information
beforehand
- If you do not have device information beforehand, use
just-in-time provisioning (JITP).

Enable automatic registration and associate a
provisioning template with the CA certificate used to
sign the device certificate.
- For example, when a device attempts to connect to AWS IoT by using a certificate signed by a registered CA
certificate, AWS IoT loads the template from the
certificate and initiates the JITP workflow.

- If you have device information beforehand, use bulk
registration.

Specify a list of single-thing provisioning template
values that are stored in a file in an S3 bucket.
- Run the start-thing-registration-task command to
register things in bulk. Provide provisioning template,
S3 bucket name, a key name, and a role ARN to the
command.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS05-BP03 Use device level features to enable re-provisioning

A birth or bootstrap certificate is a low-privilege unique
certificate that is associated with each device during the
manufacturing process. The certificate should have a policy to
restrict devices to only allow connecting to specific endpoints
to initiate provisioning process and fetch the final
certificate. Before a device is provisioned, it should be
limited in functionality to help prevent its misuse. Only after
a provisioning process is invoked and approved, should the
device be allowed to operate on the system as designed.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS05-BP03-01** *Use a certificate
bootstrapping process to establish processes for device
assembly, registration, and activation.*

- For example, AWS IoT Core offers a fleet provisioning
interface to devices for upgrading a birth certificate to
long-lived credentials that enable normal runtime
operations.

**Prescriptive guidance
IOTOPS05-BP03-02** *Obtain a list of allowed
devices from the device manufacturer.*

- Check the allow list file to validate that the device has
been fully vetted by the supplier.
- Make sure that the list is encrypted, securely stored, and
can only be accessed by necessary services and users. Even
if the list changes, keep the original list securely stored.
- Make sure that this list is securely transferred from the
manufacturer to you, is encrypted, and is not publicly
accessible.
- Make sure that any bootstrap certificate used is signed by a
certificate authority (CA) you own or trust.

IOTOPS06: How do you implement
observability for your IoT system?

Observability is a crucial part for your IoT application built
to handle device activity at scale. As the main three pillars of
observability are logging, metrics and tracing, there are more
functional parts of the business goals where you actively
troubleshoot and improve the application to mitigate risks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---
