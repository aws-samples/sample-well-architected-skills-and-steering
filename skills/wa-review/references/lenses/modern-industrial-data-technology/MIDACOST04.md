# MIDACOST04 — Forecast resource provisioning

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# MIDACOST04-BP01 Perform an analysis on the historical manufacturing workloads

Make data-driven resource provisioning decisions based on accurate historical usage
patterns in manufacturing environments. This involves analyzing at least one full production
cycle's data, considering seasonal variations, and accounting for planned maintenance windows
in resource forecasting.

**Desired outcome:** Data-driven resource provisioning
decisions based on accurate historical usage patterns in manufacturing environments.

**Common anti-patterns:**

- Using IT-only metrics without considering manufacturing operations data
- Basing forecasts on insufficient historical data (needs at least one full production
cycle)
- Ignoring seasonal production variations in resource planning
- Not differentiating between development, testing, and production environment needs
- Failing to account for planned maintenance windows in resource forecasting
- Using the same forecasting model for both batch and continuous production processes
- Overlooking equipment upgrade cycles in long-term resource planning
- Not considering quality control and compliance requirements in resource forecasting

**Benefits of establishing this best practice:**

- Improved capacity planning
- Reduced overprovisioning
- Better alignment with production patterns
- Optimized resource costs

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before you begin, you will need:

- At least one full production cycle's data
- Historical resource usage patterns across seasons
- Manufacturing schedules and maintenance windows documented

Key decisions needed:

- Forecast horizon based on production cycles
- Resource allocation thresholds for different workload types
- Scaling trigger points aligned with manufacturing needs
- Data retention requirements for compliance

Systematically collect and analyze resource utilization data from manufacturing
systems to identify usage patterns and correlations with production cycles. Use these
insights to create forecasting models that align with actual manufacturing operations,
considering both IT and OT systems for comprehensive resource planning.

### Implementation steps

- Collect historical data on:

Resource utilization
- Production cycles
- Seasonal variations
- Peak usage periods

- Analyze patterns and trends:

Daily/weekly/monthly patterns
- Production correlation
- Seasonal impacts

- Create baseline metrics.
- Develop forecasting models.
- Validate predictions against actual usage.

## Key AWS services

- Quick
- AWS Cost Explorer
- Amazon CloudWatch
- AWS Systems Manager
- Amazon SageMaker AI

## Resources

**Related documents:**

- [Quick](https://docs.aws.amazon.com/quicksight/latest/user/creating-visuals.html)
- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Metrics in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html)
- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/best-practices-for-compute-optimizer.html)
- [Use the
SageMaker AI AI DeepAR forecasting algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/deepar.html)
- [Time Series Forecasts in Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-time-series.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost04-bp01.html*

---
