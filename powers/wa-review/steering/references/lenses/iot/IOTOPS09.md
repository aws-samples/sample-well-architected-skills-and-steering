# IOTOPS09 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS09-BP01 Run ops metrics analysis across business teams, document learnings and define action items for future firmware deployments

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS09-BP01-01** *Monitor the behavior of
devices as they are updated in the field, and proceed only after
a percentage of devices have upgraded successfully.*

During upgrades, continue to collect all of the Amazon CloudWatch Logs, telemetry, and IoT device job messages and
combine that information with the KPIs used to measure overall
application health and the performance of long-running canaries.

Services like AWS IoT Device Defender are used to track
anomalies in overall device behavior, and to measure deviations
in performance that may indicate an issue in the updated
firmware.

**Prescriptive guidance
IOTOPS09-BP01-02** *Use AWS IoT Device Management
for creating deployment groups of devices and delivering over
the air updates (OTA) to specific device groups.*

Use a combination of grouping IoT devices for deployment and
staggering firmware upgrades over a period of time. In AWS IoT,
thing groups allow you to manage devices by category. Groups can
also contain other groups — allowing you to build hierarchies.
With organizational structure in your IoT application, you can
quickly identify and act on related devices by device group.
Leveraging the thing group allows you to automate the addition
or removal of devices from groups based on your business logic
and the lifecycle of your devices.

**Prescriptive guidance
IOTOPS09-BP01-3** *Use dynamic thing group as a
target for OTA updates.*

Create a continuous job with a dynamic thing group as target
allows you to automatically target devices when they meet the
desired criteria. The criteria can be the connectivity state or
criteria stored in registry or shadow such as software version
or model. If a thing doesn't appear in the dynamic thing group,
it won't receive the job document from the job.

For example, if your device fleet requires a firmware update to
minimize the risk of interruption during the update process, and
you only want to update the firmware on devices with a battery
life greater than 80%. You can create a dynamic thing group
called 80PercentBatteryLife that only includes devices with a
battery life above 80% and use it as the target for your job.
Only devices that meet your battery life criteria will receive
the firmware update. As devices reach the 80% battery life
criteria, they are automatically added to the dynamic thing
group and will receive the firmware update.

IOTOPS10: How do you verify that you are ready to support the
operations of devices in your IoT workload?

Operating IoT workloads at scale is different than testing and
running prototypes. You need to make sure that your team is
prepared and trained to operate a widely distributed IoT data
collection application. IoT workloads require your teams to
learn new skills and competencies to deliver edge-to-cloud
outcomes. Your team needs to be able to pinpoint key operational
thresholds that indicate a high level of readiness.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/evolve.html*

---
