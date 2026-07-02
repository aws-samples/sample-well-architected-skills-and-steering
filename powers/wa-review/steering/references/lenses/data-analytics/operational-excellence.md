# Operational excellence

**Pages**: 6

---

## 1 – Monitor the health of the analytics application workload

# Best practice 1.1 – Validate the data quality of source systems before transferring data for analytics

Data quality can have an intrinsic impact on the success or
failure of your organization’s data analytics projects. To
avoid committing significant resources to process potentially
poor-quality data, your organization should understand the
quality of the source data, and monitor the changes to data
quality throughout the data pipeline.

Data source validation can often be performed quickly on a
subset of the latest data range to look for data defects.
Such defects include missing values, anomalous data, or
wrong data types that could fail the analytics job
completion or lead to completion of the job with inaccurate
results.

For more details refer to following document:

- AWS Blog:
[How
to Architect Data Quality on the AWS Cloud](https://aws.amazon.com/blogs/industries/how-to-architect-data-quality-on-the-aws-cloud/)
- AWS Blog: [Getting started with AWS Glue Data Quality from the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/)

## Suggestion 1.1.1 – Implement data quality validation mechanisms

The critical attributes of data quality that should be measured and tracked
through your environment are completeness, accuracy, and uniqueness. Validating and
measuring your data quality using metrics is important to build trust in your data, which
increases data adoption throughout your organization.

For more details, refer to the following information:

- AWS Big Data Blog: [Set up advanced rules to validate quality of multiple datasets with AWS Glue Data
Quality](https://aws.amazon.com/blogs/big-data/set-up-advanced-rules-to-validate-quality-of-multiple-datasets-with-aws-glue-data-quality/)
- AWS Big Data Blog: [Getting started with AWS Glue Data Quality for ETL Pipelines](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-for-etl-pipelines/)
- AWS Big Data Blog: [Set up alerts and orchestrate data quality rules with AWS Glue Data Quality](https://aws.amazon.com/blogs/big-data/set-up-alerts-and-orchestrate-data-quality-rules-with-aws-glue-data-quality/)
- AWS Big Data Blog:
[Enforce
customized data quality rules in AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/enforce-customized-data-quality-rules-in-aws-glue-databrew/).
- AWS Big Data Blog:
[Build
a data quality score card using AWS Glue DataBrew,
Amazon Athena, and Quick](https://aws.amazon.com/blogs/big-data/build-a-data-quality-score-card-using-aws-glue-databrew-amazon-athena-and-amazon-quicksight/).

## Suggestion 1.1.2 – Notify stakeholders and use business logic to determine how to remediate data that is not valid

Alerts and notifications play a crucial role in maintaining data quality because they facilitate prompt and efficient responses to any data quality issues that may arise within a dataset. By establishing and configuring alerts and notifications, you can actively monitor data quality and receive timely alerts when data quality issues are identified. This proactive approach helps mitigate the risk of making decisions based on inaccurate information.

It’s usually more efficient to impute missing values, but in
other cases it’s more efficient to block processing until
the data quality issue can be resolved at source.

## Suggestion 1.1.3 – Score and share the quality of your datasets

To improve the ongoing trust in data quality and adoption
of your organization’s datasets, consider creating a data
quality matrix that can be accessed by the relevant teams
advertising the quality score of your datasets and
potential issues with the data. This information can be
incorporated in your Data Catalog.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-1.1---validate-the-data-quality-of-source-systems-before-transferring-data-for-analytics..html*

---

# Best practice 1.2 – Monitor operational metrics of data processing jobs and the availability of source data

Data processing pipelines often consist of multiple steps that all need to run in sequence to output the desired data sets and meet business deadlines. Monitoring each job in the pipeline is key to ensure operational excellence. The operational metrics of the jobs themselves should be monitored, as well as the availability of source data, and that results are produced.

For example, if your pipeline runs on a fixed schedule, and there is no new source data to process, the pipeline may still appear healthy because it runs without failures. Similarly, if the pipeline runs when new source data becomes available, it can appear healthy when no new source data becomes available if you only alert on failed runs.

## Suggestion 1.2.1 – Alert when new data has not arrived or become available within the expected time

You should monitor the time when new data arrives or becomes available, and alert when too much time has passed since the last occurrence. Even if the jobs in your data processing pipeline runs flawlessly, the quality of the results depend on the quality and availability of the source data.

In a complex data pipeline it can also be necessary to monitor that one stage produces results within an expected time frame as it affects downstream stages.

## Suggestion 1.2.2 – Alert when data processing jobs don’t complete on time or don’t produce results

You should monitor the running time of data processing jobs and alert when too much time has passed since the last completed run. You should also alert if a job does not produce a result. With monitoring and alerts you can discover jobs that fail, and also jobs that fail silently by not producing results.

The expected completion time should be based on the normal running time of the job, with some margin. The margin is needed because the running time of data processing jobs depend on the amount of data they process. Jobs that start as a result of new data becoming available also don’t have a set starting time, which should be factored into the margin.

For very long running jobs it can also be necessary to monitor the start time of jobs, and alert when too much time has passed since the last start. Sometimes it can cause too much delay to wait until the expected completion time before the failure is discovered.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-1.2---monitor-operational-metrics-of-data-processing-jobs-and-the-availability-of-source-data..html*

---

## 2 – Modernize deployment of the analytics jobs and applications

# Best practice 2.1 – Use version control for job and application changes

Version control systems support tracking changes and the
ability to revert to previous versions of an analytics
system should changes cause unintended consequences. Your
team should version control code repositories for both
analytics infrastructure as code (IaC) and analytics
applications logic.

## Suggestion 2.1.1 – Use infrastructure as code and version control systems so that a failed deployment can be rolled back to a previous good state

Follow software development best practices when building
analytics systems. For example, deploy resources using
code templates, such as AWS CloudFormation or Hashicorp
Terraform, so that all deployments occur exactly as
intended. Use version control systems (for example, code
repositories such as GitHub) to hold
current and previous versions of your code templates.
Using these tools, if a new change results in unwanted
outcomes, you can easily roll back to the previous code
template.

For more details, refer to the following information:

- AWS Whitepaper:
[Introduction
to DevOps on AWS](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- AWS Blog:
[Automate
building an integrated analytics solution with AWS
Analytics Automation Toolkit](https://aws.amazon.com/blogs/big-data/automate-building-an-integrated-analytics-solution-with-aws-analytics-automation-toolkit/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.1---use-version-control-for-job-and-application-changes..html*

---

# Best practice 2.2 – Create test data and provision staging environment

Using a known and unchanging dataset for test purposes helps
ensure that when changes are made to the analytics
environment or analytics application code, test results can
be compared to previous versions.

Confirming that the test datasets accurately represent
real-world data allows the analytics workload developer to
confirm the outcomes from the analytics job, as well as
comparing test results to previous versions.

Your organization should use a staging environment for user
access testing. Your organization should create logically separated AWS accounts for your development, test, staging, and production
environments depending upon your development standards.

For more details, refer to the following information:

AWS Whitepaper:
[Establishing
your best practice AWS environment](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)

## Suggestion 2.2.1 – Use a curated dataset to test application logic and performance improvements

Analytics projects that are being developed should use the
same curated dataset to compare results between tests of
different versions of your code. Using the same dataset for
all tests allows demonstrating improvement over time, as
well as making it easier to recognize regressions in your
code.

To help control access to sensitive data, your
organization should use data masking techniques when
restoring development data to non-production environments.
More information on data minimization techniques can be
found in [Security](./security.html).

For more details, refer to the following information:

- AWS Database Blog: [Data Masking using AWS DMS (AWS
Data Migration Service)](https://aws.amazon.com/blogs/database/data-masking-using-aws-dms/)
- Amazon Redshift Data Masking: [Dynamic data masking
(DDM) in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html)

## Suggestion 2.2.2 – Use a random sample of recent data to validate application edge cases and help ensure that regressions have not been introduced

Use a statistically valid random sample of recent data to
confirm that the analytics solution continues to perform
under real-world conditions. Using a sample of recent data
also allows you to recognize whether your dataset
characteristics have shifted, or whether anomalous data
has recently been introduced to your data.

For more information, see the AWS Machine Learning Blog: [Create random and stratified samples of data with Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/create-random-and-stratified-samples-of-data-with-amazon-sagemaker-data-wrangler/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.2---create-test-data-and-provision-staging-environment..html*

---

# Best practice 2.3 – Test and validate analytics jobs and application deployments

Before making changes in production environments, use
standard and repeatable automated tests to validate
performance and accuracy of results.

## Suggestion 2.3.1 – Establish separate staging environments to test changes before going live

Use separate environments, such as development, test, and
production, to allow feature development to be introduced
without disrupting production systems. Test changes for
accuracy and performance before changes are deployed into
the production environment.

## Suggestion 2.3.2 – Automate the deployment and testing when infrastructure and applications changes are introduced

The deployment of data pipelines and data infrastructure changes should be an automated process. When code is checked into version control, a CI/CD process should run tests and apply the changes to the staging environment, and once tested and confirmed correct, it should be deployed to the production environment.

You can use the AWS CodePipeline service to define a CI/CD process.

For more details refer to the following information:

- AWS Perspective Guidance:
[Deploy
an AWS Glue job with an AWS CodePipeline CI/CD
pipeline](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-aws-glue-job-with-an-aws-codepipeline-ci-cd-pipeline.html)
- AWS DevOps Blog:
[How
to unit test and deploy AWS Glue jobs using AWS CodePipeline](https://aws.amazon.com/blogs/devops/how-to-unit-test-and-deploy-aws-glue-jobs-using-aws-codepipeline/)
- AWS DevOps Blog: [10 ways to build applications faster with Amazon CodeWhisperer](https://aws.amazon.com/blogs/devops/10-ways-to-build-applications-faster-with-amazon-codewhisperer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.3---test-and-validate-analytics-jobs-and-application-deployments..html*

---

# Best practice 2.4 – Build standard operating procedures for deployment, test, rollback, and backfill tasks

Standard operating procedures for deployment, test,
rollback, and data backfill tasks allow faster deployments,
reduce the number of errors that reach production. Using a
standard approach also makes remediation easier if a
deployment results in unintended consequences.

## Suggestion 2.4.1 – Document and use standard operating procedures for implementing changes in your analytics workload

Standard operating procedures allow teams to make changes
confidently, thus avoiding repeatable mistakes and reducing
the chance of human error.

## Suggestion 2.4.2 – Use automation to perform changes to underlying analytics infrastructure or application logic

Automated tests can determine when changes have unintended
consequences and can roll back without human intervention.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-2.4---build-standard-operating-procedures-for-deployment-test-rollback-and-backfill-tasks..html*

---
