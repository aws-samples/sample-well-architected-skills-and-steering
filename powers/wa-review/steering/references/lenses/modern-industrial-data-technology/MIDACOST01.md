# MIDACOST01 — Forecast and optimize

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MIDACOST01-BP01 Implement data-driven cost management using AWS cost tools and manufacturing data

Create reliable cost forecasts by combining AWS usage data with manufacturing schedules
to enhance resource provisioning and budget planning accuracy. This involves analyzing
production patterns, seasonal variations, and historical cloud usage to make informed
decisions about resource allocation and cost optimization.

**Desired outcome:** Develop precise monthly and quarterly cost
forecasts by combining AWS usage data with manufacturing schedules to improve forecast
reliability for resource provisioning and budget planning.

**Common anti-patterns:**

- Relying solely on default AWS cost reports without implementing
manufacturing-specific cost allocation tags
- Making resource provisioning decisions based on short-term usage data
- Failing to account for seasonal production variations when forecasting cloud costs
- Using the same forecasting approach for all types of manufacturing workloads without
considering their unique characteristics
- Neglecting to correlate cloud spending with production output metrics
- Setting static budgets without considering manufacturing cycles and production
schedules
- Making Reserved Instance or Savings Plan commitments without analyzing historical
usage patterns
- Ignoring the impact of planned maintenance windows and product launches on resource
requirements

**Benefits of establishing this Best Practice:**

- Improved budget planning and cost predictability
- Better alignment between IT spending and OT production needs
- Reduced risk of over-provisioning or under-provisioning resources
- Enhanced ability to optimize costs during varying production cycles

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

To systematically analyze and optimize costs:

- Configure AWS Cost Explorer to track resource usage by manufacturing workload
- Set up cost allocation tags that map to specific production lines and processes
- Create monthly reports comparing AWS resource utilization with production output
- Use AWS Budgets to set alerts based on predicted usage thresholds
- Integrate production scheduling data from your MES/ERP systems with AWS cost
management tools
- Review and adjust resource allocation quarterly based on collected metrics

### Implementation steps

- Enable detailed cost and usage reporting for all cloud resources.
- Create cost allocation tags aligned with manufacturing processes.
- Establish a system to collect and analyze production schedule data.
- Implement forecasting models that consider:

Seasonal production variations
- Planned maintenance windows
- New product launches
- Historical resource utilization patterns

- Set up regular review cycles to validate forecasts against actual usage.
- Take advantage of cost saving mechanisms like AWS Savings Plans and Spot Instances.

## Key AWS services

- AWS Cost Explorer
- AWS Budgets
- AWS Supply Chain
- Amazon SageMaker AI Canvas
- AWS Data Exports with Quick

## Resources

**Related documents:**

- [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Managing your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Demand Planning](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand-planning.html)
- [Time Series Forecasts in Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-time-series.html)
- [Cloud Financial
Management with AWS](https://aws.amazon.com/aws-cost-management/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost01-bp01.html*

---

# MIDACOST01-BP02 Configure automated cost monitoring and alerts for manufacturing workloads

Set up a comprehensive alerting system that notifies teams within 24 hours when costs
exceed thresholds, generates cost reports by production line, identifies waste, and maintains
cost visibility across manufacturing operations. This includes setting up progressive alerting
using different severity levels and implementing automated remediation for common cost-related
issues.

**Desired outcome:** Set up a comprehensive alerting system
that:

- Notifies teams within 24 hours when costs exceed defined thresholds
- Generates daily/weekly cost reports by production line
- Identifies resource waste and cost anomalies automatically
- Maintains cost visibility across manufacturing operations

**Common anti-patterns:**

- Setting up generic alerts without considering manufacturing-specific cost patterns
- Creating too many alerts that lead to notification fatigue
- Failing to establish baseline costs before implementing monitoring
- Not differentiating between production and non-production environment alerts
- Sending alerts to a general distribution list instead of specific responsible teams
- Using the same thresholds for different types of manufacturing workloads
- Implementing alerts without defined response procedures
- Focusing only on total cost without considering cost per unit of production
- Not accounting for shift patterns in alert configurations

**Benefits of establishing this Best Practice:**

- Early detection of cost anomalies
- Reduced manual monitoring effort
- Improved cost visibility across teams
- Faster response to cost-related issues

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Before setting up automation, verify that you have:

- Identified key stakeholders who need cost alerts (operations, finance, IT teams)
- Determined cost thresholds for different manufacturing processes
- Mapped your AWS resources to specific production lines or cells
- Established baseline costs for normal operations

Then, implement monitoring systems that:

- Track daily or weekly cost variations against production schedules
- Alert relevant teams when costs deviate your set thresholds (for example, 20%) or more from
baseline
- Generate automated reports showing cost per unit of production
- Monitor resource utilization during different manufacturing shifts

### Implementation steps

- Define cost thresholds or budgets for different manufacturing workload
components.
- Configure automated alerts for:

Budget overruns
- Unusual usage patterns
- Idle resources
- Storage growth rates

- Create automated reports for:

Daily, weekly, or monthly cost trends
- Resource utilization and production output
- Cost per manufacturing line, cell, or product

- Establish escalation procedures for cost-related incidents.

## Key AWS services

- AWS Cost Explorer
- AWS Budgets
- AWS CloudTrail
- AWS CloudWatch
- Amazon Simple Notification Service
- AWS Pricing Calculator
- AWS Lambda

## Resources

**Related documents:**

- [Detecting unusual spend with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)

- [Cost
Optimization with AWS](https://aws.amazon.com/aws-cost-management/cost-optimization/)
- [Logging AWS Cost Management API calls with AWS CloudTrail](https://docs.aws.amazon.com/cost-management/latest/userguide/logging-with-cloudtrail.html)
- [Create a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost01-bp02.html*

---
