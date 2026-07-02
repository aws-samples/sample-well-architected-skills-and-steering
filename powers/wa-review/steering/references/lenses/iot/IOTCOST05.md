# IOTCOST05 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## IOTCOST05-BP01 Balance networking throughput against payload size to optimize efficiency

The specific use case drives the balance between frequency and
payload size. Consider and test different payload optimization
strategies. Additionally, consider trade-offs between
compression and processing overhead.

**Level of risk exposed if this best
practice is not established: Low**

**Prescriptive guidance**

- Shorten values while keeping them legible. If five digits of
precision are sufficient, then you should not use 12 digits
in the payload.
- Use serialization frameworks to compress payloads to smaller
sizes if you do not require IoT rules engine payload
inspection.
- Send data less frequently and aggregate messages together
within the billable increments. For example, sending a
single two KB message every second can be achieved at a
lower IoT message cost by sending two separate two KB
messages every other second.

This approach has tradeoffs that should be considered before
implementation. Adding complexity or delay in your devices may
unexpectedly increase processing costs. A cost optimization
exercise for IoT payloads should only happen after your solution
has been in production and you can use a data-driven approach to
determine the cost impact of changing the way data is sent to
AWS IoT Core.

IOTCOST06: How do you optimize the costs
of storing the current state of your IoT device?

Well-Architected IoT applications have a virtual representation
of the device in the cloud. This virtual representation is
composed of a managed data store or specialized IoT application
data store. In both cases, your end devices must be programmed
in a way that efficiently transmits device state changes to your
IoT application. For example, your device should only send its
full device state if your firmware logic dictates that the full
device state may be out of sync and would be best reconciled by
sending all current settings. As individual state changes occur,
the device should optimize the frequency it transmits those
changes to the cloud.

In AWS IoT, device shadow and registry operations are metered in
one KB increments and billing is per million access and modify
operations. The shadow stores the desired or actual state of
each device and the registry is used to name and manage devices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/managing-demand-and-supplying-resources.html*

---
