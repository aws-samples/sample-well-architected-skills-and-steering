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
