# LSPERF17 — Network and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# LSPERF17-BP01 Measure baseline data transfer performance and evaluate how data sovereignty requirements affect latency

Establish performance baselines by measuring transfer metrics for
data routes and compare against direct paths to understand impact.
Set up ongoing monitoring of transfers to track performance and find
optimization opportunities within regulatory limits. Conduct regular
testing using synthetic data to verify that routes meet both
performance needs and regulatory requirements.

**Desired outcome:** You have a
comprehensive monitoring and optimization system that provides
baseline metrics, validation, and performance analysis for
cross-region data transfers. This enables efficient management of
data transfers while maintaining adherence to regional sovereignty
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establish comprehensive baseline metrics for data transfers across
routes, including latency, throughput, and reliability
measurements. Document performance characteristics of different
transfer paths while maintaining adherence to data sovereignty
requirements. Create comparative analysis frameworks to evaluate
the impact of audit controls on transfer performance.

Implement continuous monitoring of approved data transfer routes
to track performance trends and identify potential bottlenecks.
Set up measurement systems that capture both performance metrics
and regulatory adherence. Establish regular assessment cycles to
evaluate transfer efficiency within regulatory constraints.

Design and implement synthetic testing procedures that simulate
real-world data transfers while maintaining regulatory
requirements. Create test scenarios that reflect various data
types and transfer patterns common in production environments.
Develop testing protocols that validate both performance standards
and regulatory adherence.

Establish systematic processes for identifying optimization
opportunities within adherence boundaries. Create performance
improvement strategies that maintain required data sovereignty
controls. Implement regular review cycles to assess and enhance
transfer efficiency.

### Implementation steps

- Establish comprehensive performance measurement with Amazon CloudWatch for transfer monitoring across routes, VPC Flow
Logs for detailed traffic pattern analysis, and AWS Transit Gateway Network Manager for cross-region connectivity
visibility.
- Implement robust monitoring using AWS Config for continuous
sovereignty rule verification, AWS CloudTrail for complete
audit logging of data transfers, and AWS Security Hub CSPM for
centralized status monitoring.
- Deploy automated testing infrastructure with Amazon CloudWatch Synthetics for transfer route validation, AWS X-Ray for detailed request path tracing across Regions, and
Amazon Route 53 health checks for continuous endpoint
availability monitoring.
- Optimize data transfer capabilities using AWS Global Accelerator for path optimization, AWS Transfer Family for
secure managed file transfers, and AWS Direct Connect for
dedicated high-performance connections supporting critical
transfers.
- Document data sovereignty requirements with approved
transfer routes, audit controls, and verification procedures
for each data classification.
- Establish regular reviews with automated reporting on
transfer patterns, policy adherence, and performance metrics
across regional boundaries.
- Implement automated remediation for common violations and
performance issues.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf17-bp01.html*

---

# LSPERF17-BP02 Implement data classification-based transfer assessment with region-specific regulatory validation

Design test frameworks simulating real clinical and research data
transfers while following data sovereignty routing rules. Test
transfer performance under varying network conditions and data
volumes while maintaining regional adherence. Use modeling to
predict transfer times and resource needs for different sovereignty
scenarios, informing cross-region data sharing decisions.

**Desired outcome:** You have an
automated system for managing cross-Region data transfers that
improves adherence to regional requirements while optimizing
performance. This enables efficient data sharing across global
research locations based on both performance metrics and regulatory
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establish comprehensive data classification systems that align
with regional regulatory requirements and clinical data
sensitivity levels. Create clear mapping between data types and
their corresponding transfer requirements. Implement automated
classification tools that properly handle different data
categories across Regions.

Design and execute testing frameworks that evaluate transfer
performance while maintaining adherence to regional requirements.
Create test scenarios using representative data volumes and types
common in clinical research. Implement monitoring systems that
track both performance metrics and regulatory adherence during
transfers.

Develop region-specific regulatory validation processes that
verify adherence to local data sovereignty requirements. Establish
automated checks that validate transfer paths and data handling
procedures. Create comprehensive audit trails that demonstrate
adherence throughout the transfer lifecycle.

Implement modeling systems that analyze historical transfer data
to predict performance under various scenarios. Create simulation
tools that help evaluate different transfer strategies while
maintaining adherence. Establish regular review cycles to refine
and improve prediction accuracy.

### Implementation steps

- Implement automated data classification with Macie for
sensitive data discovery, S3 Object Tags for appropriate
classification labeling, and IAM policies to enforce
classification-based access controls.
- Establish comprehensive performance monitoring using Amazon CloudWatch metrics for cross-region transfer tracking, VPC
Flow Logs for detailed traffic analysis, and Transit Gateway
for visibility into cross-region transfer routes.
- Deploy robust tools including AWS Config for regional
requirement validation, AWS CloudTrail for detailed transfer
audit logging, and AWS Security Hub CSPM for centralized status
monitoring.
- Create advanced analysis capabilities with Quick
dashboards for transfer performance visualization, Amazon EventBridge for automated event responses, and AWS Systems Manager for coordinated cross-region operations management.
- Document data classification standards with handling
requirements for each sensitivity level and approved
transfer patterns between regions.
- Implement regular audit reporting with metrics on
classification accuracy, transfer policy adherence, and
regional status.
- Establish automated remediation workflows for common
classification and issues.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf17-bp02.html*

---
