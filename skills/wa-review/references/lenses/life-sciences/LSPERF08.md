# LSPERF08 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF08-BP01 Implement holistic system performance monitoring beyond traditional latency metrics

Implement a multi-layered latency monitoring system tracking the
entire clinical workflow times, not just system metrics. Capture
95th and 99th percentiles. Set medical SLAs (stroke imaging

- Deploy workflow monitoring across entire clinical process
with persistent identifiers.
- Define performance indicators with statistical tracking and
baseline measurements.
- Create performance standards with thresholds for critical
workflows.
- Implement monitoring for healthcare-specific protocols and
interfaces.
- Deploy progressive alerting for transactions approaching
clinical thresholds.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf08-bp01.html*

---

# LSPERF08-BP02 Track resource utilization with clinical context

Track compute metrics tied to clinical workflows and patient volumes
for predictive capacity planning. Monitor specialized clinical
accelerators like GPUs for imaging. Analyze resource usage patterns
by department and procedure to optimize allocation while providing
emergency capacity. Implement context-aware anomaly detection that
distinguishes normal clinical activity spikes from true issues, with
alerts weighted by clinical importance.

**Desired outcome:** Implement
comprehensive clinical-aware resource monitoring that provides
predictive insights, optimizes capacity allocation based on workflow
patterns, and delivers intelligent alerting prioritized by patient
care impact.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish relationships between infrastructure performance and
specific healthcare workflows. Correlation analysis reveals how
technical resource consumption directly relates to patient care
activities.

Implement specialized tracking for purpose-built healthcare
computing hardware. Targeted monitoring optimizes utilization of
clinical-specific accelerators critical for advanced medical
applications.

Develop detailed understanding of resource utilization across
different healthcare dimensions. Multidimensional analysis enables
optimized resource allocation aligned with actual clinical
operations.

Implement intelligent monitoring that understands expected
clinical activity patterns. Context-aware anomaly detection blocks
false alarms while verifying that real issues receive prompt
attention.

Develop notification systems that prioritize based on patient care
impact. Clinical weighting provides attention to the most critical
healthcare services when resource constraints occur.

### Implementation steps

- Implement contextual monitoring with clinical workflow
identifiers.
- Deploy specialized hardware tracking for imaging and genomic
workflows.
- Create resource consumption models by department and
procedure type.
- Configure pattern recognition for normal clinical activity
variations.
- Implement priority alerting based on clinical criticality
and patient impact.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf08-bp02.html*

---

# LSPERF08-BP03 Implement clinical system monitoring with workflow validation and impact analysis

Implement synthetic transactions simulating clinical workflows while
monitoring data integrity throughout your infrastructure. Regularly
test recovery capabilities against clinical RTOs. Develop dashboards
that translate technical metrics into patient impact metrics with
proper prioritization and regulatory adherence. Document historical
performance data to demonstrate system reliability and support
continuous improvement efforts.

**Desired outcome:** Establish a
monitoring framework with synthetic clinical workflow testing,
recovery validation, patient-impact dashboards, and historical
performance tracking to improve system reliability and regulatory
adherence.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Deploy automated testing that simulates real healthcare user
activities. Synthetic transactions verify functionality from a
clinical perspective rather than just confirming technical
availability.

Deploy specialized tracking for healthcare data as it moves
through systems. Data pipeline monitoring improves clinical
information integrity beyond basic system performance metrics.

Implement regular testing of failover systems for patient-critical
applications to verify that they consistently meet established
recovery time objectives (RTOs) and recovery point objectives
(RPOs). Deploy automated recovery verification processes that
validate systems will function as expected during actual incidents
affecting clinical care, confirming that recovery objectives are
not just theoretically defined but practically achievable under
real-world conditions

Develop dashboards that translate technical issues into clinical
care implications. Patient impact visualization assists with
appropriate response prioritization based on actual healthcare
effects.

Establish comprehensive historical performance tracking that
satisfies healthcare regulations. Compliance-focused data
retention verifies that your monitoring data fulfills regulatory
requirements for clinical systems.

### Implementation steps

- Configure healthcare simulations mimicking clinical
workflows and calculations.
- Implement verification for clinical data completeness and
integrity.
- Deploy scheduled failover testing aligned with clinical
requirements.
- Create dashboards showing patient impact and diagnostic
delays.
- Deploy secure archives for performance metrics and
reporting.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf08-bp03.html*

---
