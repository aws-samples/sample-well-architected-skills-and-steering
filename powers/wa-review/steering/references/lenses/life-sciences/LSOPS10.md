# LSOPS10 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# LSOPS10-BP01 Reproducibility

Build technology products with infrastructure as code so you can
rebuild them if needed. In archive documents, store the structure of
your products. Store data in a format that is simple to archive,
such as Iceberg.

**Desired outcome:** Maintain a
history of changes made in the IT environment and methods to
programmatically create environments when needed.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:** In addition to being ready to close at project
conclusion, this practice eases movement from test to production and
verifies that testing is performed on the exact architecture that
will be deployed. Additionally, it becomes more straightforward to
reproduce the environment in the event that certain components are
needed after project conclusion.

## Implementation guidance

Establish a robust infrastructure as code framework using
industry-standard tools and practices. This foundation fosters
consistent, repeatable deployments while maintaining complete
version control and documentation.

Implement comprehensive documentation practices that automatically
capture infrastructure configurations, dependencies, and changes.
This system should integrate with version control and provide
clear rebuild instructions.

Establish structured change control procedures that maintain
infrastructure stability while enabling necessary updates. This
process should include proper documentation, testing, and approval
workflows.

### Implementation steps

- Create an infrastructure as code foundation:

- Establish version-controlled repository for infrastructure
code and configurations.
- Implement automated CI/CD pipelines for infrastructure
deployment using AWS CodeBuild.
- Create standardized templates for common infrastructure
components. Consider AWS CloudFormation and StackSets.

- Develop a documentation framework:

- Develop comprehensive documentation covering the
infrastructure components.
- Create automated documentation generation for code and
configurations. Consider Amazon Q.

- Implement archive management:

- Implement versioned archive system for infrastructure code.
Amazon S3 Versioning can be used to retain multiple versions
of documents.
- Create automated backup procedures for configuration files
using AWS Backup. Establish a clear tagging system for
archived components.

## Resources

**Related documents::**

- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)

**Related examples:**

- [Generating
documentation with Amazon Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-generation.html)

**Related tools:**

- [Amazon Q](https://aws.amazon.com/q/)
- [Amazon S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS CodeBuild](https://aws.amazon.com/codebuild/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) (with drift detection)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops10-bp01.html*

---

# LSOPS10-BP02 Store data in a format that works both for archiving and for active use by retaining related metadata

Select a data format which is queried while the project is ongoing
but archives natively. Iceberg's data format is ideal for life
sciences projects because it stores metadata alongside the data. It
offers advanced data versioning, time travel capabilities, and
schema evolution, essential features for maintaining data lineage
and regulatory adherence while handling large-scale scientific
datasets that frequently change over time.

**Desired outcome:** Have a portable
dataset that contains the data and metadata in a single package

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Verify that the output of data processing results in portable data
formats to allow for simple archiving.

### Implementation steps

- Build standard data pipelines using AWS Glue
- For deep analysis on structured data use Amazon Redshift.
- Build a data lake of the data in Amazon S3 in Iceberg
format.

## Resources

**Related documentsn:**

- [What
is Apache Iceberg?](https://aws.amazon.com/what-is/apache-iceberg/)

**Related examples:**

- [Build
a high-performance quant research platform with Apache
Iceberg](https://aws.amazon.com/blogs/big-data/build-a-high-performance-quant-research-platform-with-apache-iceberg/)

**Related tools:**

- [Modernize
Data Archiving](https://aws.amazon.com/archive/)
- [Amazon S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops10-bp02.html*

---
