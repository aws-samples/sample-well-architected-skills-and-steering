# Reliability

**Pages**: 8

---

## 6 – Design resilience for analytics workload

# Best practice 6.1 – Create an illustration of data flow dependencies

Work with business stakeholders to create a visual illustration of the data pipeline. Identify the systems that interact with each dependency. The key architecture components that are expected to be captured are data acquisition, ingestion, data transformation, data processing, data storage, data protection and governance, and data consumption. All system dependencies need owners. Agree within your organization who owns which dependency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.1-create-an-illustration-of-data-flow-dependencies..html*

---

# Best practice 6.2 – Monitor analytics systems to detect analytics or extract, transform and load (ETL) job failures

Detect extract, transform, and load (ETL) and analytics job failures as soon as possible. Pinpointing where and how the error occurred is critical for notiﬁcations and corrective actions.

## Suggestion 6.2.1– Monitor and track job errors from different levels, including infrastructure, ETL workﬂow, and ETL application code

Failures can occur at all levels of the analytics system. Each task in the analytics workload should be instrumented to provide metrics indicating the health of the task. Monitor the emitted metrics and raise alarms if any components fail. Create dashboards to visualize metrics and govern access to them.

For more details, refer to the following:

- [Visualize data warehouse metrics: Query and visualize Amazon Redshift operational metrics using the Amazon Redshift plugin for Grafana](https://aws.amazon.com/blogs/big-data/query-and-visualize-amazon-redshift-operational-metrics-using-the-amazon-redshift-plugin-for-grafana/)
- [Visualize Amazon EMR metrics: Monitor Amazon EMR on Amazon EKS with Amazon Managed Prometheus and Amazon Managed Grafana](https://aws.amazon.com/blogs/mt/monitoring-amazon-emr-on-eks-with-amazon-managed-prometheus-and-amazon-managed-grafana/)

## Suggestion 6.2.2 – Establish end-to-end monitoring for the complete analytics and ETL pipeline

End-to-end monitoring allows tracking the ﬂow of data as
it passes through the analytics system. In many cases,
data processing might be dependent on application logic,
such as sampling a subset of data from a data stream to
check accuracy. Properly identifying and monitoring the
end-to-end ﬂow of data allows detecting at which step the
analytics and ETL job fails.

## Suggestions 6.2.3 – Determine what data was processed when the job failed

Failures in data processing systems can cause data integrity or data quality issues. Determine what data was being processed at the time of failure and perform quality checks of both the input and output data. If possible, roll-back the committed data and restart your job.

For more details, see AWS Glue: [Overview of Data Quality in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html).

## Suggestions 6.2.4 – Classify the severity of the job failures based on the type of failure and the business impact

Classifying the severity of different job failures helps you prioritize remediation and guide the notiﬁcation requirements to key stakeholders. Classification of jobs can be agreed upon based on importance and the impact the failure has on meeting internal and external SLAs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.2---monitor-analytics-systems-to-detect-analytics-or-etl-job-failures..html*

---

# Best practice 6.3 – Notify stakeholders about analytics or ETL job failures

Analytics and ETL job failures can impact the SLAs for
delivering the data on time for downstream analytics
workloads. Failures might cause data quality or data
integrity issues as well. Notifying all stakeholders about
the job failure as soon as possible is important for
remediation actions needed. Stakeholders may include IT
operations, help desk, data sources, analytics, and
downstream workloads.

For more details, see
AWS Well-Architected:
[Design
your Workload to Withstand Component Failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html)

## Suggestions 6.3.1 – Establish automated notifications to predefined recipients

Use services such Amazon Simple Notification Service
(Amazon SNS) to send automated emails, SMS alerts, or both
in the event of failure. Store the alert logs in an
immutable data store for future reference.

## Suggestions 6.3.2 – Do not include sensitive data in notifications

Automated alerts often include indicators of useful information for troubleshooting the failure. Ensure PII and sensitive information, such as personal, medical, or ﬁnancial information is not shared in failure notiﬁcations.

For more details, see AWS Glue: [Detect and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html).

## Suggestions 6.3.3 – Integrate the analytics job failure notification solution with the enterprise operation management system

Where possible, integrate automated notifications into
existing operations management tools. For example, an
operations support ticket can be automatically filed in the
event of a failure. That same ticket can automatically be
resolved if the analytics system recovers on retry.

## Suggestions 6.3.4 – Notify IT operations and help desk teams of any ETL job failures

Normally, the IT operations team should be the first
contact for production workload failures. The IT
operations team troubleshoots and attempts to recover the
failed job, if possible. It is also helpful to notify the
IT help desk of system failures that have an end user
impact. These can include issues with the data warehouse
used by the business intelligence (BI) analysts.

## Suggestions 6.3.5 – Notify downstream systems of data freshness

Monitor data updates as this gives process and application information when data becomes stale. Stale data can lead to misreporting due to the correct values being stale and not current.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.3---notify-stakeholders-about-analytics-or-etl-job-failures..html*

---

# Best practice 6.4 – Automate the recovery of analytics and ETL job failures

Many factors can cause analytics and ETL jobs to fail. Job
failures can be recovered using automated recovery
solutions, however, others might require manual
intervention. Designing and implementing an automated
recovery solution can help reduce the impact of the job
failures and streamline IT operations.

## Suggestions 6.4.1– Discover recovery procedures that work for multiple failure types

Conﬁgure automatic retries to handle intermittent network disruptions. Conﬁgure managed scaling to ensure that there are sufficient resources available for jobs to complete within speciﬁc time limits.

## Suggestions 6.4.2 – Limit the number of automatic reruns and create log entries for the automatic recovery attempts and results

Track the number of reruns an automated recovery process has attempted. Limit the number of reruns to avoid unnecessary reruns and resources. Track the number of recovery attempts and outcomes to identify failure trends and drive future improvements.

## Suggestion 6.4.3 – Design the job recovery solution based on the delivery SLA

Build systems that can meet SLA requirements even if jobs must be retried or manually recovered. Consider the service-level agreements of the different services that you use, and monitor the performance of your jobs against your organization’s internal SLAs.

## Suggestion 6.4.4 – Consider idempotency when designing ETL jobs

To avoid unexpected outcomes when automatically rerunning pipelines such as duplicated or stale data, enforce idempotency where possible. Idempotent ETL jobs can be rerun with the same result or outcome. Some strategies to achieve this are the overwriting method (for example, Spark overwrite) and the delete-write method (deleting existing data prior to writing it to ensure that there are no duplicates or stale data), although deletion should be applied with caution.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.4-automate-the-recovery-of-analytics-and-etl-job-failures..html*

---

# Best practice 6.5 – Build a disaster recovery (DR) plan for the analytics infrastructure and the data

Discuss with business stakeholders to understand maximum
amount of data loss (RPO) and maximum amount of service loss
(RTO).

## Suggestion 6.5.1 – Confirm the business requirement of the disaster recovery (DR) plan

Agree with the business shareholders what the internal and
external SLAs are for your analytics processes. For
example, not all business reports are business critical so
it’s important that your DR plans are aligned with the
severity of the outage.

## Suggestion 6.5.2 – Design the disaster recovery (DR) solution for each layer of the solution

Review the architecture for your data and analytics pipeline and select the DR pattern that meets your DR requirements, working backwards from the most important information that must be saved in the event of a DR scenario, to the least important.

## Suggestion 6.5.3 – Implement and test your backup solution based on the RPO and RTO

Backup solutions must be implemented to reduce data loss. Test your backup to ensure it is performing correctly by periodically restoring the data and validating the results.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.5---build-a-disaster-recovery-dr-plan-for-the-analytics-infrastructure-and-the-data..html*

---

## 7 – Govern data and metadata changes

# Best practice 7.1 – Build a central Data Catalog to store, share, and track metadata changes

Building a central Data Catalog to store, share, and manage metadata across the organization is an integral part of data governance. This will promote standardization and reuse. Tracing metadata change history in the central Data Catalog helps you manage and control version changes in the metadata. A Data Catalog is often required for auditing and compliance but by incorporating business context to a Data Catalog, it allows users in the organization to discover data assets using business terms rather than technical naming conventions.

## Suggestion 7.1.1 – Changes on the metadata in the Data Catalog should be controlled and versioned

Use the Data Catalog change tracking features. For example, when the schema
changes, AWS Glue Data Catalog will track the version change. You can use AWS Glue to compare
schema versions, if needed. In addition, we recommend a change control process that only
allows those authorized to make schema changes in your Data Catalog. The AWS Glue Schema registry allows you to centrally discover and control data schemas. You can create a schema contract between producers and consumers to improve data consumer awareness to data format changes.

## Suggestion 7.1.2 – Capture and publish business metadata of your data assets

Capturing business metadata and publishing it with metadata assets is essential for data consumers and data stewards alike. Metadata such as regulatory compliance statuses, data classification, and other important data governance characteristics, guides consumers on how to best process the data and informs data governance processes conducted by data stewards. Establishing a business glossary across the organization creates a collection of business terms that can be associated with the data assets. This ensures that business definitions are common across the organization.

For more details, see AWS Data Zone: [Governed Analytics](https://aws.amazon.com/datazone/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-7.1---build-a-central-data-catalog-to-store-share-and-track-metadata-changes..html*

---

# Best practice 7.2 – Monitor for data quality anomalies

Data quality is critical for organizations to accurately measure important business metrices, bad data can impact the accuracy of analytics insights and ML predictions. Monitor data quality and detect data anomalies as early as possible.

For more details, see AWS Glue: [Getting started with AWS Glue Date Quality](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/).

## Suggestion 7.2.1 – Include a data quality check stage in the ETL pipeline as early as possible

A data quality check helps ensure that bad data is
identified and fixed as soon as possible to prevent bad data
from propagating downstream.

## Suggestion 7.2.2 – Understand the nature of your data and determine the types of data anomalies that must be monitored and fixed based on the business requirements

The analytics workload can process various types of data,
such as structured, unstructured, picture, audio, and
video formats. Some data might arrive to the workload
periodically, or some might constantly arrive in real
time. It is pragmatic to assume that data does not always
arrive to the analytics workload in perfect shape, and
only a portion – not the whole set – of data matters to
your workload.

Understand the characteristics of data, and determine what forms of data anomalies you want to remediate. For example, if you expect the data always contains an important attribute like customer ID, you can deﬁne that a datum is abnormal if it doesn’t contain the `customer_id` attribute. Common data anomalies include duplicate data, missing data, incomplete data, incorrect data format, and diﬀerent measurement units.

## Suggestion 7.2.3 – Select an existing data quality solution or develop your own based on the requirements

There are data quality solutions that can only detect single ﬁeld data quality issues. Other solutions can handle complex stateful data quality issues related to multiple ﬁelds.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-7.2---monitor-for-data-quality-anomalies..html*

---

# Best practice 7.3 – Trace data lineage

Have a clear understanding about where your organization’s
data is coming from, how the data is transformed, who and
what systems have access to the data, and how the data is
used, is critical to increasing the business value of data.
To achieve this goal, data lineage should be tracked,
managed, and visualized.

## Suggestion 7.3.1 – Track and control data lineage information

Data lineage information should include where data has
come from, where the data is going, and who has access to
the data. Data changes and the business logic used should
also be tracked in the data lineage.

## Suggestion 7.3.2 – Use visualization tools to investigate data lineage

Data lineage can become complicated when multiple systems
are interacting with each other. Building a data lineage
tool to visualize data lineage can reduce troubleshooting
time and help identify downstream dependencies.

## Suggestion 7.3.3 – Build a data lineage report to satisfy compliance and audit requirements

If some derestriction data lineage is required for
compliance or audit purposes, your organization should
either build a data lineage process using AWS services or
investigate third-party applications.

For more details, refer to the following information:

- AWS data lineage blog**:**
[Build data lineage for data lakes using AWS Glue, Amazon Neptune, and
Spline](https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-7.3---trace-data-lineage..html*

---
