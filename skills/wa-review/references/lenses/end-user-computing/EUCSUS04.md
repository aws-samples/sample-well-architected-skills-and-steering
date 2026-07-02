# EUCSUS04 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS04-BP01 Implement a scaling methodology in WorkSpaces Applications

Scaling policies improve resource utilization and cost
management for application streaming workloads.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Either fleet type (On-Demand or Always-On) requires a
methodology to verify that the appropriate number of instances
are available when users initiate a connection.

A combination of step scaling, scheduled scaling, or target
tracking scaling is recommended to match each fleet usage. To
avoid extra consumption of instances, monitor your fleet usage
and modify your scaling policies accordingly. The following
resources describe in further detail the differences between
the types of scaling and how to configure them to align with
the pattern of usage for the applications being delivered.
Keep in mind that the fleet type choice is only available
during the fleet creation process.

- [WorkSpaces Applications Fleet Types](https://docs.aws.amazon.com/appstream2/latest/developerguide/fleet-type.html)
- [Fleet Auto Scaling for Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/autoscaling.html)
- [Scaling Your Desktop Application Streams with Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/compute/scaling-your-desktop-application-streams-with-amazon-appstream-2-0/)
- [Scale your Amazon WorkSpaces Applications fleets](https://aws.amazon.com/blogs/desktop-and-application-streaming/scale-your-amazon-appstream-2-0-fleets/)
- [Monitoring Amazon WorkSpaces Applications Resources](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus04-bp01.html*

---
