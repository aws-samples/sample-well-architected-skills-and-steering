# LSOPS06 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# LSOPS06-BP01 Validate data quality during ingestion

Define data quality measurements and implement checks during
ingestion.

**Desired outcome:** Data is clean
and ready for analysis upon ingestion.

**Benefits of establishing this best
practice:**

- More trusted results.
- Faster output to conclusions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Build data quality checks into data ingestion pipelines.

Plan to isolate erroneous data and have a way to review it as
needed.

### Implementation steps

- Identify expected patterns in received data.
- Build data quality checks in AWS Glue Data Quality.
- Incorporate checks in data pipelines.
- Build processes to catch and isolate erroneous data. Alert
personnel to investigate data errors

## Resources

**Related examples:**

- [Measure
performance of AWS Glue Data Quality for ETL pipelines](https://aws.amazon.com/blogs/big-data/measure-performance-of-aws-glue-data-quality-for-etl-pipelines/)

**Related tools:**

- [AWS Glue](https://aws.amazon.com/glue/)
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops06-bp01.html*

---

# LSOPS06-BP02 Implement data pipeline testing

Create data handling tests including user authentication and
authorization, data collection, and ingestion into later warehouses.
Tests should cover quality in addition to technical requirements.

**Desired outcome:** Data is reliable
and ready for immediate business use. Reports and analytics can be
trusted without manual verification.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Cloud technologies allow for comprehensive test environments that
can replicate entire system architectures and automate complex
test scenarios.

Consider implementing a testing strategy that follows data through
its complete lifecycle, from initial entry through the processing
stages to final storage. Cloud-based environments can replicate
your production architecture, allowing validation of the
integration points and data transformations. Automated testing can
run scenarios that simulate real-world usage patterns, while data
validation tools verify information remains consistent as it moves
through different systems.

When implementing testing, focus on critical data paths that
impact patient safety, product quality, or regulatory adherence.
Consider continuous testing approaches that run core validation
scenarios automatically when changes occur, supplemented by more
comprehensive testing at key milestones.

### Implementation steps

- Map complete data flows across each system component:

- Use AWS X-Ray to trace data paths across distributed
systems.
- Consider AWS AWS Glue Data Catalog for documenting data
structures and relationships.

- Create realistic test environments that replicate production
architecture:

- Implement AWS CloudFormation templates for consistent
environment deployment.
- Consider Service Catalog for standardized test
environment provisioning.

- Develop test scenarios that follow data through complete
processing paths:

- Consider AWS Step Functions for orchestrating complex test
workflows.

- Implement data validation checks at key integration points:

- Use AWS Lambda functions for custom validation logic.
- Consider Amazon EventBridge for coordinating validation
across services.

- Automate testing as part of deployment pipelines:

- Implement AWS CodePipeline for continuous testing
integration:
- Consider AWS CodeBuild for running test suites:

- Monitor data quality metrics throughout test runtime:

- Configure Amazon CloudWatch for tracking data quality
indicators.
- Consider AWS Glue DataBrew for data quality validation.

- Generate comprehensive test reports for regulatory
documentation:

- Store test evidence in Amazon S3 with appropriate retention
policies.
- Consider AWS Systems Manager Automation for standardized
report generation.

## Resources

**Related guides, videos, and
documentation:**

- [How
to test serverless functions and applications](https://docs.aws.amazon.com/lambda/latest/dg/testing-guide.html)
- [OPS05-BP02
Test and validate changes](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_test_val_chg.html)

**Related tools:**

- [AWS X-Ray](https://aws.amazon.com/xray/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops06-bp02.html*

---
