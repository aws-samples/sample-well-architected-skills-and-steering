**Saga**: Automated governance
**Capability**: AG.DLM — Data lifecycle management

---

# [AG.DLM.8] Improve traceability with data provenance tracking

**Category:** RECOMMENDED

Data provenance tracking records the history of data throughout its lifecycle—its
origins, how and when it was processed, and who was responsible for those processes. This
practice forms a vital part of ensuring data integrity, reliability, and traceability,
providing a clear record of the data's journey from its source to its final form.

The process involves capturing, logging, and storing metadata
that provides valuable insights into the lineage of the data.
Key aspects of metadata include the data's source, any
transformations it underwent (such as aggregation, filtering,
or enrichment), the flow of data across systems and services
(movements), and actors (the systems or individuals
interacting with the data).

Use automated tools and processes to manage data provenance by
automatically capturing and logging metadata, and make it
easily accessible and queryable for review and auditing
purposes. For instance, data cataloging tools can manage data
assets and their provenance information effectively, providing
a systematic way to handle large volumes of data and their
metadata across different stages of the development lifecycle.

In more complex use cases, machine learning (ML) algorithms can be used to uncover
hidden patterns and dependencies among data entities and operations. This technique can
reveal insights that might not be easily detectable with traditional methods.

Regularly review and update the data provenance tracking
process to keep it aligned with evolving data practices,
business requirements, and to maintain regulatory compliance.
Provide training and resources to teams, helping them
understand the importance and practical use of data provenance
information.

Data provenance tracking is particularly recommended for
datasets dealing with sensitive, regulated data or complex
data processing workflows. It also adds significant value in
environments where reproducibility and traceability of data
operations are required, such as in data-driven
decision-making, machine learning model development, and
debugging data issues.

Data provenance tracking is particularly recommended for
datasets dealing with sensitive or regulated data, machine
learning workflows, and complex data processing which may
require debugging.

**Related information:**

- [AWS Glue Data Catalog](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/aws-glue-data-catalog.html)
- [Well-Architected
Data Analytics Lens: Best practice 7.3 – Trace data
lineage](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-7.3---trace-data-lineage..html)
- [Amazon SageMaker AI ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking.html)
- [Blog: Build
data lineage for data lakes using AWS Glue, Amazon Neptune, and Spline](https://aws.amazon.com/blogs/big-data/build-data-lineage-for-data-lakes-using-aws-glue-amazon-neptune-and-spline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dlm.8-improve-traceability-with-data-provenance-tracking.html*
