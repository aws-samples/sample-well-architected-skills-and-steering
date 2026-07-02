# IOTSUS01 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 4

---

## IOTSUS01-BP01 Eliminate unnecessary modules, libraries, and processes

Verify that the operating system only runs essential processes
that are necessary for the functionality of the IoT device.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Unnecessary libraries, modules, and processes contribute to a
larger device footprint, increase patching requirements, and
create a larger attack surface and more processes for the CPU to
run.

Choose efficient programming languages that satisfy your
business requirements. Programming language choice has an impact
on device requirements as well as active and sleep cycles.
Programming languages vary in areas such as memory management,
typing, and parallelism. It is recommended to design and test
as much as possible prior to making a final decision on
language.

Produce a more efficient and secure IoT device design by
streamlining the operating system and only including essential
processes.

Use projects like Yocto or Buildroot to build custom Linux
images containing only the necessary modules for device
functionality, and build device software like AWS IoT Greengrass
or the AWS IoT Device Client into these custom images using
layers like the meta-aws Yocto layer.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-optimization.html*

---

## IOTSUS01-BP02 Use AWS IoT features to optimize network usage and power consumption

Select AWS IoT service features which can help to optimize
network and power resources.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

Use AWS IoT Device Shadow services, which are virtual representations of
IoT devices in the cloud. Device shadows enable decoupled
bi-directional communication between the device and applications
running in the cloud. Applications can obtain device state from
the shadow rather than the device, reducing traffic between the
device and cloud, and allowing the application to continue
operation even if the device is disconnected intermittently.
When a device comes back online, it can check if there were any
changes requested by the application while it was offline, and
take action as needed. This allows the device to stay offline,
saving power.

Use MQTT retained messages, message expiry, and session expiry
features. Retained messages and Device Shadows both retain data
from a device but have different capabilities and suitability.
MQTT5 message expiry can be used to make sure that devices only
receive time-relevant messages, reducing processing load. The
session expiry feature can be used by MQTT clients to set
application-specific session expiry limits, making sure that the
broker does not need to retain resources beyond what is needed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-optimization.html*

---

## IOTSUS01-BP03 Use a hardware watchdog to restart your device automatically

IoT devices should have a hardware watchdog mechanism, which can
reduce downtime by automatically restarting the device when it
becomes unresponsive. In many cases, restarting the device can
put it in a state where it can be remotely managed, minimizing
the impact of failures and reducing the need for site visits.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Choose processors that include a hardware watchdog and that are
well supported by vendor software solutions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-optimization.html*

---

## IOTSUS01-BP04 Implement resilient and scalable system behavior for clients communicating with the cloud

Clients communicating with the cloud must not only be
functionally correct, but also implement resilient and scalable
system behavior. Implementing such behavior reduces the work
done by each client device and reduces network traffic and doing
so can improve device longevity and total lifetime energy
consumption.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

Support
[exponential
backoff with jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/) when handling connection retries to
cloud endpoints.

Minimize the number of connection attempts when dealing with a
congested network, reducing the work done by each client and
reducing network traffic.

Define a threshold at which point it is more effective to enter
low power modes during a backoff period.

Support MQTTv5 reason codes and use that information to
determine if and when to reconnect.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-optimization.html*

---
