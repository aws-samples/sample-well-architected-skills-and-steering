# LSREL02 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# LSREL02-BP01 Build resilient and highly available research solutions

Design research systems using fault-isolated, redundant deployment
patterns that allow continuous access during maintenance or
localized outages. Use highly available configurations where
near-zero downtime is required (for example, ELNs) and
active-passive designs with automated failover for systems with less
stringent latency or availability needs (for example, LIMS).

**Desired outcome:**

- Research systems remain available during maintenance or outages.
- Ongoing experiments and data collection continue without
interruption.
- Researchers have a consistent experience across sites and
geographies.

**Common anti-patterns:**

- Relying on single-instance deployments for critical systems.
- Maintenance performed without phased rollouts or rollback plans.
- Highly available architectures implemented without routine
failover testing.

**Benefits of establishing this best
practice:**

- Protects ongoing experiments from interruption, reducing risk of
wasted samples or time.
- Preserves continuity in multi-day or multi-week lab workflows.
- Provides global research teams access to shared tools without
productivity loss.
- Enhances regulatory readiness by reducing gaps in system
availability records.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When designing research workloads for resiliency, use deployment
topologies that minimize the scope of impact of maintenance and
outage events. Multi-site or multi–AZ deployments allow for
uninterrupted operation when a system component is taken offline.
Automated health checks and intelligent traffic routing directs
users to healthy endpoints, maintaining continuity during upgrades
or failover scenarios. Maintenance windows should be orchestrated
to minimize user disruption, and resilience should be validated
regularly through simulated failovers or planned game days.

### Implementation steps

- Deploy AWS IoT Greengrass for local buffering of instrument
data.
- Deploy LIMS, EHR and ELN solutions across multiple
Availability Zones using Amazon EC2 Auto Scaling for
workload redundancy.
- Place applications behind an Elastic Load Balancer (ALB or
NLB) to support highly available deployment configurations,
or configure Amazon Route 53 DNS failover with health checks
for active-passive failover strategies.
- Use AWS Systems Manager to coordinate upgrades with minimal
disruption. Monitor resilience, health status, and failover
events in Amazon CloudWatch, and validate readiness with
regular failover exercises.

## Resources

**Related best practices:**

- Change management and controlled rollout strategies
- Incident response playbooks for scientific research systems
- Risk-based classification of R&D applications

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp01.html*

---

# LSREL02-BP02 Maintain continuous data availability and integrity

Implement real-time or near-real-time data replication strategies
across Availability Zones or AWS Regions to protect against system
failures or maintenance interruptions. Use warm standby environments
with synchronized datasets to enable quick failover and avoid data
loss or research disruption.

**Desired outcome:**

- Continuous data access during maintenance and outages.
- Minimal risk of data loss or corruption across failure events.
- Trust in the accuracy, completeness, and reproducibility of
research datasets.

**Common anti-patterns:**

- Relying on manual backups without automated validation or
recovery testing.
- Replicating data without maintaining consistency or integrity
verification.
- Treating replication as optional for intermediate or temporary
data sources unless cost/time-effective to reproduce.

**Benefits of establishing this best
practice:**

- Enables uninterrupted access to experimental results and
research datasets.
- Reduces risk of losing critical data from unique or costly
experiments.
- Supports reproducibility and regulatory adherence (like audit
trails and traceability).
- Strengthens collaboration by making shared datasets available
globally.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data availability must be preserved even when system components
undergo maintenance or fail unexpectedly. Structured research
data, such as LIMS transactions, should use multi-zone replication
to maintain availability, while unstructured research datasets
should be replicated across independent storage domains.
Monitoring replication lag and validating dataset consistency are
critical to avoid silent data corruption. Automated recovery
validation and regular restore drills build trust that data can be
recovered accurately and within defined RPO and RTO objectives.

### Implementation steps

- Configure Amazon RDS Multi-AZ deployments for LIMS databases
to achieve transactional durability.
- Use Amazon S3 Cross-Region Replication (CRR) for
uninterrupted access to critical datasets, and protect
large-scale file-based research workloads with Amazon FSx for Lustre combined with snapshot policies managed by AWS Backup.
- Define automated recovery validation policies in AWS Backup
for audit tracking.
- Continuously monitor replication lag and recovery objectives
through Amazon CloudWatch, aligning recovery metrics with
the needs of research workflows.

## Resources

**Related best practices:**

- Data lifecycle management for research datasets
- Data integrity and reproducibility controls
- Governance documentation for GxP-relevant systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp02.html*

---
