# IOTSEC09 — Security

**Pillar**: Security  
**Best Practices**: 2

---

## IOTSEC09-BP01 Manage and maintain IoT Device software using an automated, monitored, and audited mechanism

Having an automated, monitored, and audited mechanism for
deploying, managing, and maintaining device software in IoT
devices allows for making changes to this device software over
time. The device software installed in each device should be
maintained using a software bill of materials (SBOM). New
features and fixes or updates can be applied to the device
which extend its useful lifetime, address security
vulnerabilities, or enable the device to perform more actions.
Use
[AWS IoT Device Management Software Package Catalog (SPC)](https://docs.aws.amazon.com/iot/latest/developerguide/software-package-catalog.html) to
aid in maintaining device software inventories.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC09-BP01-01** *Use IoT AWS IoT Greengrass and
AWS IoT Greengrass component deployments to update software in IoT edge
devices.*

IoT AWS IoT Greengrass supports a runtime environment in which
concurrent components can be started, stopped, and updated.
Communications is supported between components. This allows for
complex parallel processing of multiple tasks within the device.
IoT AWS IoT Greengrass has extensive support for defining and managing
components and component versions as well as managing the
deployment of those components into fleets of IoT AWS IoT Greengrass
devices.

**Prescriptive guidance
IOTSEC09-BP01-02** *Use IoT Jobs to schedule
and run management and update activities in IoT
devices.*

IoT Jobs allows actions to be carried out in IoT devices based
on both a schedule and the set of devices to which the jobs
apply.

**Prescriptive guidance
IOTSEC09-BP01-03** *Use IoT Secure Tunneling
sparingly to remotely access a device to take some corrective
action.*

IoT Secure Tunneling allows for direct interaction with the
device. However, this should be used only as a last resort since
it implies that a human would be remotely attaching to and
interacting with the device. Using specific remote command and
control mechanisms is preferred to relying on opening up a
secure tunnel through which a human operate would remotely
access a device to perform some action. Remote command and
control allow for much better input/output parameter checking
for the operations being requested.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---

## IOTSEC09-BP02 Manage IoT device configuration using automated and controlled mechanisms

In addition to managing the networking configuration and
firmware or software in the IoT devices, the configuration
settings in the device must also be managed and updated. Like
updating the firmware or software, this should be done using an
automated, monitored, and audited mechanism.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC09-BP02-01** *Use IoT AWS IoT Greengrass and
AWS IoT Greengrass component deployments to update configuration in IoT
devices.*

IoT AWS IoT Greengrass supports a runtime environment in which
concurrent components can be started, stopped, and updated.
Communications is supported between components. This allows for
complex parallel processing of multiple tasks within the device.
IoT AWS IoT Greengrass has extensive support for defining and managing
components and component versions as well as managing the
deployment of those components into fleets of IoT AWS IoT Greengrass
devices. One aspect of component management is the configuration
of the components themselves. This can be used to update
configuration in the IoT devices.

**Prescriptive guidance
IOTSEC09-BP02-02** *Use IoT Jobs to schedule
and run management and update activities in IoT
devices.*

IoT Jobs allows actions to be carried out in IoT devices based
on both a schedule and the set of devices to which the jobs
apply.

**Prescriptive guidance
IOTSEC09-BP02-03** *Use IoT Secure Tunneling
sparingly to remotely access a device to take some corrective
action.*

IoT Secure Tunneling allows for direct interaction with the
device. However, this should be used only as a last resort since
it implies that a human would be remotely attaching to and
interacting with the device. Using specific remote command and
control mechanisms is preferred to relying on opening up a
secure tunnel through which a human operate would remotely
access a device to perform some action. Remote command and
control allow for much better input or output parameter checking
for the operations being requested.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---
