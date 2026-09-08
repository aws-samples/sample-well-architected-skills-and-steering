# Sustainability

**Pillar**: Sustainability  
**Questions**: 5

---

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

# IOTSUS02 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 2

---

## IOTSUS02-BP01 Use the Basic Ingest feature in AWS IoT Core

With the Basic Ingest feature, you can securely send device data
to the AWS services supported by AWS IoT rule actions, without
incurring messaging costs. Basic Ingest optimizes data flow by
removing the publish/subscribe message broker from the ingestion
path, making it more cost-effective and resource-efficient.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

When ingesting data to AWS IoT Core, consider whether to use the
Basic Ingest feature or not. Use this approach if your
application does not require multiple subscribers for the data
being ingested.

For ingestion mechanisms other than Basic Ingest (such as the
Amazon Kinesis family of services), refer to the AWS IoT Lens
for guidance on which service is appropriate for which use case.
At this time, there are no additional sustainability best
practices for these services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-cloud.html*

---

## IOTSUS02-BP02 Choose an appropriate Quality of Service (QoS) level

Higher QoS levels involve additional network overhead for
acknowledgment and retransmission, which can increase power
consumption.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Use MQTT when you have IoT devices or other resource-constrained
environments that need to communicate efficiently and reliably
with a publish-subscribe messaging pattern. MQTT supports
different quality of service (QoS) levels for message delivery.
Consider using lower QoS levels (such as QoS 0) if the
reliability of message delivery is not critical for your use
case to reduce power consumption and network overhead.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/software-and-architecture-cloud.html*

---

# IOTSUS03 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 8

---

## IOTSUS03-BP01 Source sustainable components to help reduce environmental harm and encourage eco-friendly IoT products

Several factors can impact sustainability in various stages of
the design process. These include choices related to materials,
packaging, and product design, which can significantly influence
the carbon footprint of the final product.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance:**

Adopt sustainable practices in the design and manufacturing
layer to reduce the environmental impact of IoT products.
Consider factors that can impact sustainability during various
stages of the design process, such as choices related to
materials, packaging, and product design, which can
significantly influence the carbon footprint of the final
product.

Implement sustainable supply-chain practices, such as sourcing
from suppliers that demonstrate environmentally responsible
practices, using recycled or renewable materials, or selecting
products with lower environmental impact throughout their
lifecycle.

Use products that are certified as Climate Pledge Friendly,
which meet sustainability standards for reducing carbon
emissions and promoting a circular economy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP02 Consider the manufacturing and distribution footprint of your device

Choosing manufacturing facilities with low environmental
impacts, optimizing transportation routes to minimize emissions,
and utilizing energy-efficient manufacturing processes can all
contribute to improved sustainability in the supply-chain.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- Choose manufacturing facilities with low environmental
impacts, such as those that use energy-efficient processes
or renewable energy sources.
- Optimize transportation routes and modes to minimize
emissions from shipping products.
- Use energy-efficient manufacturing processes, such as using
low-temperature solder during the pick-and-place operation
to reduce energy consumption for heating solder on printed
circuit boards (PCBs).
- Design IoT devices and packaging in smaller form factors to
allow for easier and more efficient shipping in large
volumes while consuming fewer raw materials and harmful
chemicals.
- Consider the entire supply chain and make decisions that
contribute to positive environmental outcomes through
thoughtful product design, material selection, and
manufacturing processes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP03 Use benchmarks to help you make a processor choice

Processor and IoT benchmarks can help you assess and narrow down
which processor is appropriate for your use case.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Choose benchmarks that include workloads that closely mimic the
actual workloads IoT devices are expected to handle, such as
sensor data processing, edge filtering, and running
communication protocols.

Look for benchmarks that provide relevant performance metrics
considering the resource constraints of IoT devices, such as low
power operation and real-time processing requirements.

Consider benchmarks that include energy efficiency metrics, such
as Performance per Watt and Thermal Design Power (TDP), to
assess how efficiently CPUs can process workloads while
minimizing energy consumption.

Use benchmarks that include test cases to evaluate the real-time
processing capabilities of CPUs, including latency and
responsiveness, which are important for IoT applications.

Select benchmarks that evaluate the communication and
connectivity performance and efficiency of CPUs, as IoT devices
require communication capabilities to interact with other
devices, cloud services, or data centers.

Consider using benchmarks from the Embedded Microprocessor
Benchmark Consortium (EEMBC), such as the EEMBC IoTMark and
EEMBC ULPBench, which are specifically designed for evaluating
the performance of CPUs in IoT applications and include relevant
metrics aligned with sustainability evaluation criteria.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP04 Optimize your device based on real-world testing

Make the final selection of your device hardware based on
evaluating one or more hardware choices under close-to-actual
operating conditions.  Processors, peripherals, and other
components must be chosen to optimize power draw during runtime
as well as during device idle states.  Other criteria as
discussed throughout this document can be used to make a final
selection based on the results of your testing.

Once the hardware has been finalized, examine whether the
observed performance matches the expected performance.
Profiling of your code on the target hardware under real
workloads can help identify power-hungry sections of the code
and help you optimize them for efficiency. Examining application
and OS use of the device's power saving features and modes may
also be required to achieve optimal efficiency.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

Evaluate one or more hardware choices under close-to-actual
operating conditions to make the final selection of device
hardware.

Choose processors, peripherals, and other components that
optimize power draw during runtime as well as during device idle
states.

Use criteria discussed in the sustainability best practices
document, such as energy efficiency, real-time processing, and
connectivity performance, to make the final hardware selection
based on the results of your testing.

Once the hardware has been finalized, examine whether the
observed performance matches the expected performance by
profiling your code on the target hardware under real workloads.

Identify power-hungry sections of the code through profiling and
optimize them for efficiency.

Examine the application and operating system's use of the
device's power-saving features and modes, and make necessary
adjustments to achieve optimal efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP05 Use sensors with built-in event detection capabilities

Sensor components are the foundation of IoT, bridging the
physical and digital worlds and providing real-time data on
environmental conditions. Sensor components should be designed
to operate with minimal power consumption by optimizing data
transmission. Some sensor components have built-in data
processing capabilities to generate events that are directly
usable by the host device's application. For example, inertial
measurement unit (IMU) sensors can detect fall events by
processing acceleration, orientation, and motion data locally,
and generating an interrupt to the host processor with an alert
when a fall is detected, enabling the host processor to wake up
and process the event while conserving power during regular
operation.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Optimize sensor components to have built-in data processing
capabilities to generate events that are directly usable by the
host device's application, reducing the need for further
processing on the host.

Configure sensor sampling rates to balance between capturing
enough data for accuracy and conserving power to reduce battery
drain, based on the specific use case requirements.

Employ techniques such as adjusting the sampling rate based on
sensor data variability, prioritizing critical data over less
important data, or using event-triggered or adaptive sampling
approaches to reduce unnecessary data collection.

Use sensors that can perform local processing of raw sensor data
using embedded algorithms or machine learning models, and
generate interrupts to the host processor only when specific
events are detected. This allows the host processor to operate
in a low-power mode until an interrupt is received.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP06 Use hardware acceleration for video encoding and decoding

Hardware acceleration for video encoding and decoding is crucial
for sustainability in IoT devices like security cameras and
video doorbells. By offloading intensive video processing to
dedicated hardware accelerators, it can reduce power
consumption, allowing main processors to operate at lower clock
speeds or enter low-power states more frequently. This improved
energy efficiency not only decreases the overall energy
footprint but also enables more compact and resource-efficient
IoT device designs, aligning with sustainable product principles
by minimizing material and resource consumption.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

For IoT devices that require processing and streaming video to
the cloud, such as doorbell or security cameras, use video
encoding to reduce data transmission and file size.

Adopt the H.265 (HEVC or High Efficiency Video Coding) video
encoding standard, which provides better video quality at lower
bit rates compared to H.264 (AVC or Advanced Video Coding),
resulting in reduced bandwidth requirements, lower power
consumption, and lower communication costs during video playback
or transmission.

Choose a microcontroller or microprocessor with dedicated video
encoding hardware acceleration to improve performance and reduce
power consumption in video processing tasks.

Consider system designs that offer a dedicated video encoding
co-processor that runs a single video encoding algorithm,
allowing the host processor to handle other general-purpose
tasks.

With advancements in technology, more efficient video encoding
algorithms may be developed in the future. To extend the
device's lifespan, choose a hardware accelerator with an FPGA or
other updatable logic that can be updated to support more
efficient encoding algorithms as they become available.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP07 Use HSMs to accelerate cryptographic operations and save power

Incorporate secure hardware and hardware security modules (HSMs)
in IoT device designs to improve security, reduce energy
consumption, and enhance sustainability. For example, an HSM
typically performs Elliptic Curve Digital Signature Algorithm
(ECDSA) signature operations several times faster than software
on a general-purpose microcontroller, allowing the host
microcontroller to spend more time in a low-power mode while the
HSM performs complex cryptographic operations.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

Use secure hardware components such as Trusted Platform Modules
(TPMs), hardware security modules (HSMs), secure elements (SEs),
and secure enclaves (SEs) like Arm TrustZone in IoT device
designs to significantly speed up cryptographic operations,
reduce energy consumption, and enhance security.

If the device supports cellular connectivity, use the SIM card
as a secure element instead of a dedicated one to reduce the
overall bill of materials (BOM).

Use device certificates with long expiration dates designed to
be rotated only as needed to maintain the security posture of
the device, as rotating device certificates can be
computationally expensive and requires additional communication
with the cloud.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

## IOTSUS03-BP08 Use low-power location tracking

Employ low-power tracking solutions for IoT for sustainability
and resource efficiency. These solutions extend battery life,
minimizing the need for frequent replacements and associated
electronic waste. They reduce overall energy consumption and
carbon footprints, while enabling reliable operation in remote
or off-grid locations without continuous power sources.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

For GPS-based devices, use chipsets that support assisted-GPS
(A-GPS), which reduces power consumption by offloading some of
the location calculation work to the network.

Consider using location services like AWS IoT Core Device
Location, which leverages cloud-based location solvers such as
Wi-Fi scan, cellular scan, Global Navigation Satellite System
(GNSS) scan, or reverse IP look-up to determine the
geo-coordinates of IoT devices. Using cloud-based location
services can reduce the device power consumption required to
resolve location, as the computationally expensive location
calculations are offloaded to the cloud.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-optimization.html*

---

# IOTSUS04 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 3

---

## IOTSUS04-BP01 Use energy harvesting technologies to power your device

One approach to improve sustainability is to use energy
harvesting technologies to provide some or all of the power
needs of a device, reducing reliance on grid-based power
sources.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Incorporate energy harvesting technologies that can capture
renewable energy sources such as solar energy, thermal energy,
vibration and mechanical energy, radio frequency energy, wind
energy, and piezoelectric energy to power IoT devices. Use
batteries or supercapacitors to store the captured energy,
providing continuous availability of power for the devices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-power-management.html*

---

## IOTSUS04-BP02 Implement tickless operation and low-power modes

Implementing *tickless* operation and making
full use of low power modes available reduces overall power
consumption. Reducing power consumption can, amongst other
things, have impacts to how long a device can be deployed and
the size battery needed to satisfy the business use case. Doing
so improves the overall sustainability of the device.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance**

- Use the tickless operation technique in embedded operating
systems like FreeRTOS to reduce the frequency of system
interrupts or *ticks* while the system is
idle, minimizing power consumption. Use the idle hook
function in the embedded operating system to place the
microcontroller CPU in a low-power mode when the system is
idle.
- For power-critical applications, consider factors such as
the latency and power requirements of entering and exiting
low-power modes, and choose the low-power mode that provides
the best trade-off between power savings and responsiveness.
- Configure the appropriate wake-up sources or events that
will alert the system to exit the low-power mode, further
minimizing power consumption by avoiding unnecessary
wake-ups.
- Implement low-power modes for all project areas. For
example, it is important to implement low-power modes for
the communication stack in a device as well as the sensor
portion of the application.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-power-management.html*

---

## IOTSUS04-BP03 Allow applications or software running on devices to dynamically adjust settings based on requirements and available resources

Implementing dynamic adjustment of hardware settings and power
management techniques on devices is important for
sustainability. It enables energy efficiency, extends device
lifespan, and optimizes resource utilization. By allowing
applications to adapt hardware settings based on requirements
and available resources, and leveraging dynamic power management
techniques, organizations can develop energy-efficient and
long-lasting devices that minimize environmental impact.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

- Enable applications or software on edge devices to make
decisions about changing hardware states, such as CPU
frequency, voltage, or other hardware settings, based on the
specific requirements of the application and the available
resources.
- Implement dynamic power management techniques, where the
device adjusts its power consumption in real-time based on
the available energy.
- Use low-power libraries and APIs provided by
microcontrollers and processors used in IoT devices, as
these offer optimized functions for power management and can
help in the realization of dynamic power management.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/hardware-and-services-power-management.html*

---

# IOTSUS05 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 3

---

## IOTSUS05-BP01 Create detailed documentation

Provide user-friendly documentation or mobile applications that
give a user detailed step-by-step guidance to educate users on
the proper installation and use of devices to avoid errors or
misuse that could necessitate a site visit from a technician,
leading to additional cost and environmental impact

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Educate users on the proper installation and use of IoT devices
through user-friendly documentation or mobile applications that
provide detailed step-by-step guidance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture-user-guidance.html*

---

## IOTSUS05-BP02 Promote responsible disposal, repairability, and transfer of ownership for IoT devices to minimize environmental impact

Implementing responsible disposal, repairability, and transfer
of ownership practices for devices is crucial for
sustainability. It minimizes environmental impact by promoting
recycling, proper disposal of hazardous components, and
adherence to electronic waste regulations.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance**

Implement environmentally responsible practices for disposing of
IoT devices, including recycling electronic components, properly
disposing of batteries, and adhering to local regulations and
guidelines for electronic waste disposal.

Collaborate among IoT device manufacturers, users, and
stakeholders to develop, implement, and improve sustainable and
responsible disposal practices to minimize environmental impact.

Promote repairability and support repair and transfer of
ownership options for IoT devices to extend their lifespan and
reduce waste.

Verify that it is straightforward for users to update, upgrade,
and repair devices back to a working state.

Provide users with detailed instructions on how to perform a
factory reset, wipe data, and dissociate devices from the
current user account before transferring ownership or disposing
of the device.

Provide clear instructions to users on how to properly dispose
of the device at the end of its life, including guidance on
recycling components and isolating any harmful materials.

Consider creating incentives for users to follow proper disposal
and recycling practices for IoT devices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture-user-guidance.html*

---

## IOTSUS05-BP03 Identify when devices in the field can or should be retired

As circumstances change in your deployed solution (sites shut
down, for instance) devices may remain active even though not
needed. To minimize the impact of such cases, unused assets
should be decommissioned.

**Level of risk exposed if this best
practice is not established: Low**

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture-user-guidance.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
