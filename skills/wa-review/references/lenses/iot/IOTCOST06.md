# IOTCOST06 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

## IOTCOST06-BP01 Optimize shadow operations

Cost optimization processes for device shadows and registry
focus on managing how many operations are performed and the size
of each operation. If your operation is cost-sensitive to shadow
and registry operations, explore ways to optimize shadow
operations. For example, for the shadow you could aggregate
several reported fields together into one shadow message update
instead of sending each reported change independently. Grouping
shadow updates together reduces the overall cost of the shadow
by consolidating updates to the service.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance**

- **Use named shadows:**
Separate logical elements, and reduce the size of updates.
- **Aggregate shadow updates:**
Look for opportunities to put several reported fields
together into one shadow message update instead of sending
each reported change independently. Grouping shadow updates
together reduces the overall cost of the shadow by
consolidating updates to the service.
- **Send only what is needed, when it is
needed:** For example, your device should only send
its full device state if your firmware logic dictates that
the full device state may be out of sync and would be best
reconciled by sending all current settings. As individual
state changes occur, the device should optimize the
frequency it transmits those changes to the cloud.
- **Immutable data:** Use the
[AWS IoT device registry](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) device attributes for immutable
data such as a serial number.
- **Minimize the frequency of reads and
writes:** Where possible, limit updates to device's
shadow document to reduce the total metered operations.
- **Choose the right service:**
Avoid using shadows as a guaranteed-delivery mechanism or
for continuously fluctuating data. Consider MQTT Last Will
and Testament (LWT) as a mitigation for the risk of loss of
device communication instead of using shadows.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/managing-demand-and-supplying-resources.html*

---
