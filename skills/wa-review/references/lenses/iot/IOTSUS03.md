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
