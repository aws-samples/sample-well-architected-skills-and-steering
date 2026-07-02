# IOTREL09 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL09-BP01 Implement device simulation to synthesize the entire flow of IoT data

Simulation scenarios can be configured to generate high volumes
of traffic, simulating a large number of IoT devices interacting
with the infrastructure simultaneously. By analyzing metrics
such as message throughput, latency, and error rates during load
testing, users can identify potential bottlenecks and optimize
their infrastructure for reliability and responsiveness.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL09-BP01-01** *To augment your production
device deployments, implement IoT simulations on Amazon Elastic Compute Cloud (Amazon EC2) as device canaries across several AWS Regions.*

- These device canaries are responsible for mirroring several
of your business use cases, such as simulating error
conditions like long-running transactions, sending
telemetry, and implementing control operations. The device
simulation framework must output extensive metrics,
including but not limited to successes, errors, latency, and
device ordering and then transmit all the metrics to your
operations system.
- You must implement a variety of device simulation canaries
that continue to test common device interactions directly
against your production system. Device canaries assist in
narrowing down the potential areas to investigate when
operational metrics are not met. Device canaries can be used
to raise preemptive alarms when the canary metrics fall
below your expected SLA.

**Prescriptive guidance
IOTREL09-BP01-02** *The IoT Device Simulator
simulates diverse scenarios to validate the logic and
functionality of their IoT applications.*

- Launch fleets of virtually connected devices from a
user-defined template and then simulate them to publish data
at regular intervals to AWS IoT
- Simulation scenarios can be utilized to generate synthetic
data for training ML models used in IoT applications. By
simulating different environmental conditions, device
behaviors, and data patterns, users can generate diverse
datasets to train and validate ML algorithms.

For more information see,
[IoT
Device Simulator](https://aws.amazon.com/solutions/implementations/iot-device-simulator/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/change-management.html*

---
