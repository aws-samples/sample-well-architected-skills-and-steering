# SCREL02 — Foundation

**Pillar**: Reliability  
**Best Practices**: 1

---

# SCREL02-BP01 Integrate shipment tracking solutions, providing real-time visibility through IoT devices and logistics APIs

Integrate comprehensive shipment tracking solutions with core
supply chain systems to create end-to-end visibility across
transportation networks, warehouses, and last-mile delivery
operations. Deploy IoT devices such as GPS trackers, temperature
sensors, and shock monitors to capture real-time condition and
location data from shipments, while establishing API connections
with logistics partners to incorporate their tracking information
into a unified visibility system. Implement geofencing
capabilities to automatically trigger notifications and workflow
actions when shipments enter or exit predefined geographic
boundaries, enabling proactive exception management.

This enhanced visibility infrastructure provides stakeholders with
accurate estimated arrival times, condition monitoring, and
chain-of-custody verification, significantly improving customer
experience while reducing operational uncertainty.

**Desired**
**outcome:** A fully transparent
supply chain where all stakeholders have real-time access to
shipment information, enhancing accountability and responsiveness.

**Benefits of establishing this best
practice:** Improves customer satisfaction, reduces
operational inefficiencies, and enables better decision-making in
case of delays.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

End-to-end visibility requires integrating IoT devices and
logistics APIs into the supply chain. AWS IoT FleetWise can be
used to gather vehicle and shipment data, while dashboards
created with Quick provide stakeholders with
real-time insights. Providing customers with tracking links
further enhances transparency.

### Implementation steps

- **Deploy IoT tracking
devices**: Use AWS IoT FleetWise for collecting
shipment data.
- **Create visualization
dashboards**: Use Quick to display
real-time shipment data.
- **Provide customer
tracking**: Share real-time tracking links with
customers for enhanced transparency.
- **Monitor visibility
systems**: Regularly assess the visibility tools
for accuracy and efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/screl02-bp01.html*

---
