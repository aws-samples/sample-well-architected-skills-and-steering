# IOTREL08 — Reliability

**Pillar**: Reliability  
**Best Practices**: 4

---

## IOTREL08-BP01 Use a mechanism to deploy and monitor firmware updates

When performing over-the-air (OTA) updates to remote devices'
firmware, make sure that the updates are controlled and
reversible to avoid functional impact of the device to the user,
or the device entering a non-recoverable state. Use tools that
allow you to deploy and track management tasks in your device
fleet.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL08-BP01-01** *Use a cloud-based update
orchestrator to deploy your firmware.*

- You can use AWS IoT Jobs to send remote actions to one or
many devices at once, control the deployment of jobs to your
devices, and track the current and past status of job
executions for each device.
- Using FreeRTOS OTA using AWS IoT Jobs: By using AWS IoT Jobs
for FreeRTOS, you have reliability and security provided out
of the box where OTA update job will send firmware to your
end device over secure MQTT or HTTPS and system reserved
topics are provided to keep track on the status of the job
schedule.
- Using custom IoT jobs with AWS IoT connected devices: By
using AWS IoT Jobs with one or more devices connected to AWS IoT gives you the ability to track the full roll out of the
update.

**Prescriptive guidance
IOTREL08-BP01-02** *Version all of the device
firmware artifacts.*

- Version all of the device firmware using Amazon S3.
- Version the manifest or execution steps for your device
firmware.
- Implement a known-safe default firmware version for your
devices to fall back to in the event of an error.
- Implement an update strategy using cryptographic
code-signing, version checking, and multiple non-volatile
storage partitions, to deploy software images and rollback.
- Version all IoT rules engine configurations in
CloudFormation.
- Version all downstream AWS Cloud resources using
CloudFormation.
- Implement a rollback strategy for reverting cloud side
changes using CloudFormation and other infrastructure as
code tools.

Treating your infrastructure as code on AWS allows you to
automate monitoring and change management for your IoT
application. Make sure that updates can be verified, installed,
or rolled back when necessary.

Devices will need new features over time for better user
experience and the firmware will need to be updated remotely.
Devices should be designed to receive and update their firmware
and the IoT application should be designed to send firmware
updates and monitor the success of such an update send.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

## IOTREL08-BP02 Configure firmware rollback capabilities in devices

Augment hardware with software to hold two versions of firmware
and the ability to switch between them. Devices can rapidly roll
back to older firmware if the new firmware has issues.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL08-BP02-01** *Leverage an RTOS with
functionality to roll back device firmware.*

By combining OTA agents provided by FreeRTOS or using AWS IoT Device SDK, you can create flexibility to hold two versions of
firmware with the hardware that is capable of storing it.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

## IOTREL08-BP03 Implement support for incremental updates to target device groups

It is a good practice to test new firmware on a small group of
devices. Using a smaller group of devices for firmware updates
helps make sure that the firmware as well as the upgrade process
is well tested before the entire fleet is updated.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL08-BP03-01** *Use a cloud orchestrator
in conjunction with device settings augmentation. Cloud services
can help you control and manage jobs in tandem with the devices
running the jobs.*

- The AWS IoT Jobs API provides a granular level of control
from the cloud to the device for carrying out firmware
update incrementally and roll back as needed.
- A job document created as part of AWS IoT job details the
remote operations the device needs to perform. This includes
shutting down rollouts based on timeouts, number of updates
per device among other things. Devices can use this
information to reject or accept firmware updates.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---

## IOTREL08-BP04 Implement dynamic configuration management for devices

Deploying software changes to devices constitutes a high-risk
operation due to the recovery cost associated with remotely
deployed devices. When possible, prefer mechanisms for making
changes using command-and-control channels to reduce the risk
that comes with software deployments and firmware upgrades. This
approach enables you to push some changes to devices while
minimizing the risk of entering fault states that require
on-premises recovery actions. Configuration changes reduce the
amount of bandwidth compared to firmware updates.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL08-BP04-01** *Use cloud tools to command
and control devices. Changing configuration of devices is less
error prone and easier to trace back than updating
firmware.*

- Use Secure Tunneling or Systems Manager to facilitate
patching of the operating system instead of pushing a new
image to be loaded on the device.
- Use Device Shadows to command-and-control devices rather
than sending commands directly to device.
- Use AWS IoT Device Management jobs to rotate expiring device
certificates instead of pushing a new image with updated
certificates.
- [AWS IoT secure tunneling](https://docs.aws.amazon.com/iot/latest/developerguide/secure-tunneling.html)
- [AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)

IOTREL09: How do you perform functional
testing for your IoT solution?

Testing IoT applications and backend services is expensive and
can be a challenge due to the large pool of physical, connected
devices required. Simulation helps test device integration and
IoT backend services, without the need for physical devices. You
can also monitor devices from the simulator or observe how
backend services are processing the data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---
