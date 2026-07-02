# IOTSEC08 — Security

**Pillar**: Security  
**Best Practices**: 2

---

## IOTSEC08-BP01 Define an automated and monitored mechanism for deploying, managing, and maintaining networks to which IoT devices are connected

Having an automated and monitored mechanism for deploying
network configuration allows for making changes to this network
configuration depending on conditions. For example, if there is
an issue or event detected in some portion of the network, that
network zone could be isolated/quarantined until the situation
is resolved. Conversely, separate network zones could be
protected from issues or events, at the expense of some
degradation in connectivity for a limited time, if an issue or
event on that network zone is detected.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC08-BP01-01** *Use virtual network
configurations to enable remote management of network
configurations.*

In IIOT environments, enable remote management of network
configuration. By enabling remote management of network
configuration, the network can be adjusted over time to meet the
needs of the solution or situation. Be aware, however, that such
capability also comes with an added risk in that the remote
configuration method itself must be protected. Consider using
Amazon VPC, AWS Virtual Private Network, AWS Direct Connect, and
Amazon Outposts to configure network connectivity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---

## IOTSEC08-BP02 Define an automated and monitored mechanism for deploying, managing, and maintaining network configurations for IoT devices

Having an automated and monitored mechanism for deploying,
managing, and maintaining network configuration in IoT devices
allows for making changes to this network configuration
depending on conditions. For example, if there is an issue or
event in some portion of the network, the network configuration
in the device could be adjusted until the situation is resolved.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC08-BP02-01** *Use IoT Jobs to schedule
and run management and update activities in IoT
devices.*

IoT Jobs allows actions to be carried out in IoT devices based
on both a schedule and the set of devices to which the jobs
apply.

**Prescriptive guidance
IOTSEC08-BP02-02** *Use IoT Secure Tunneling
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

IOTSEC09: What processes are used to
manage and maintain the hardware or software deployed and
configured in your IoT devices?

After initial installation and configuration of the hardware,
firmware, and software into the IoT device, usually at device
manufacturing time, there are often new vulnerabilities
discovered in the hardware, firmware, or software which has been
embedded into those devices. There should be some means of
updating the firmware or software in the devices so that a
vulnerability, if deemed to be serious enough, can be remediated
or mitigated. There are several ways to go about managing and
maintaining the firmware or software which range in their cost
and convenience.

Using an automated, repeatable, and monitored mechanism which
has minimal manual (human) intervention lowers the cost of each
deployment and reduces the potential of human error.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---
