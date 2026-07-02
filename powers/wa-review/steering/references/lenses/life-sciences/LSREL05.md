# LSREL05 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# LSREL05-BP01 Design edge buffering and queuing for laboratory instruments during network disruptions

Implement local data buffering, intelligent queuing, and automatic
retry mechanisms at the edge to verify that data from laboratory
instruments and clinical devices is never lost during network
connectivity issues. Edge infrastructure should provide sufficient
storage capacity, prioritize critical data streams, and
automatically resume transmission with integrity verification when
connectivity is restored.

**Desired outcome:**

- Avoid gaps in data collection from laboratory instruments or
clinical devices in the event of network disruption.
- Data integrity is verified before and after transmission to
detect corruption.
- Experiments and clinical workflows remain valid despite
temporary connectivity issues.

**Common anti-patterns:**

- Relying solely on instrument internal storage without additional
edge buffering capacity.
- Missing integrity verification, allowing corrupted data to
propagate to cloud storage.
- Lack of monitoring for buffer utilization, leading to unexpected
data loss when capacity is exceeded.
- Manual intervention required to resume data transmission after
network recovery.

**Benefits of establishing this best
practice:**

- Avoids invalidation of long-running experiments due to transient
network issues.
- Reduces risk of losing irreplaceable clinical or research data
from one-time procedures.
- Maintains scientific integrity by capturing complete and
accurate data.
- Provides operators with visibility and control during network
disruptions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design edge buffering based on instrument data generation rates,
expected network outage durations, and data criticality. Select
edge compute infrastructure that provides sufficient local storage
capacity and supports automatic retry mechanisms with exponential
backoff. Implement continuous monitoring of buffer utilization
with alerts before capacity thresholds are reached, giving
operators time to take corrective action. Validate buffered data
for integrity before and after transmission to detect corruption
during network disruptions.

### Implementation steps

- Deploy edge compute infrastructure (such as AWS IoT Greengrass, AWS Outposts, or local servers) to provide local
compute, storage, and data management capabilities.
Configure local buffering with retention policies based on
data priority and available storage capacity.
- Configure data transfer mechanisms with built-in retry and
exponential backoff strategies. Use services like AWS
DataSync for large file transfers with automatic integrity
verification, or implement custom retry logic for smaller
payloads.
- Monitor edge storage utilization using Amazon CloudWatch
metrics and create alarms for capacity thresholds to alert
operators before buffers reach maximum capacity.
- For disconnected environments, consider AWS Snowball Edge Edge
devices with local S3-compatible storage and automatic sync
when connectivity is restored.

## Resources

**Related best practices:**

- [LSREL07-BP01 Implement
system-wide data checksums and transfer validation](lsrel07-bp01.html)
- [LSREL11-BP01
Implement monitoring of equipment telemetry to detect
anomalies](lsrel11-bp01.html)

**Related tools:**

- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/)
- [AWS IoT Core](https://aws.amazon.com/iot-core/)
- [AWS DataSync](https://aws.amazon.com/datasync/)
- [AWS Snowball Edge Edge](https://aws.amazon.com/snowball/)
- [AWS Outposts](https://aws.amazon.com/outposts/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel05-bp01.html*

---
