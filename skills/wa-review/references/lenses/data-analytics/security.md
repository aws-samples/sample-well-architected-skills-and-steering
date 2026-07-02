# Security

**Pages**: 17

---

## 3 – Designing data platforms for governance and compliance

# Best practice 3.1 – Privacy by Design

Privacy by Design is an approach in system engineering that
takes privacy into account throughout the whole engineering
process. It especially focuses on systems or applications
that capture and process personal data.

There is an increased focus on ensuring that personal data
is processed lawfully, fairly, and in a transparent manner
in relation to the data subject. Another concern is that the
data processing is adequate, relevant, and limited in
relation to the purpose for which the information is used.

## Suggestion 3.1.1 – Data minimization

Organizations should only receive, process, and store information that is relevant for the task rather than processing all information when only a portion of the file is required. For example, if a client provided a full extract of all information from their source system containing sensitive personal information, and if a portion of the file is deemed irrelevant in meeting the overall project requirements, the remainder of the file should not be stored or processed.

Data minimization coincides with data access controls in that applying data minimization rules can be implemented using data access controls. A suggestion is to create and maintain a data access matrix aligned with your data classification catalogs. This helps ensure that the correct groups of people have access to the right data. As most compliant frameworks encourage evidence that rules have been applied, a data access matrix can demonstrate to auditors that your organization has gone through the proper thought process to determine who can access what information.

Data minimization can be applied at the point of capture. It can also be applied at the point of access by presenting a restricted data model or implementing role-based access controls (RBAC). For more information on controlling data access, see [4 – Implement data access control](./design-principle-4.html).

Test and user acceptance test (UAT) environments, as well
as training model datasets, must have a restricted dataset
and not contain any personal information. If the structure
of the data model must remain the same as production, then
consider anonymizing or masking information to meet your
data minimization requirements.

It is common practice to create test and development
environments using a backup of production and restore to
the respective development or test environment. If this is
the case, anonymization of personally identifiable
information (PII) and other sensitive information must
occur using inbuilt logic or services such as AWS Glue DataBrew to obfuscate the information.

For more details, refer to the following documentation:

- Amazon Redshift RBAC -
[Amazon Redshift role-based access control](https://docs.aws.amazon.com/redshift/latest/dg/t_Roles.html)s
- AWS Lake Formation RBAC -
[Lake Formation role-based access controls](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-overview.html)
- Amazon Athena RBAC -
[Amazon Athena fine-grained access controls](https://docs.aws.amazon.com/athena/latest/ug/fine-grained-access-to-glue-resources.html)
- AWS Glue DataBrew -
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) Visual Data Preparation

## Suggestion 3.1.2 – Anonymization, pseudonymization, and tokenization

Anonymization, pseudonymization, or tokenisation refers to the method of either rendering data anonymous or encoding data in such a manner that the data is no longer identifiable

### Suggestion 3.1.2.1 – Anonymization

**Anonymization is defined as the process of turning data into a
form that does not identify individuals and where identification is not likely to take
place.**

This results in changing personal data into data that is no longer personal. An
important factor in this process is that the anonymization must be irreversible. The
anonymized value should be supported by the current field data type, have similar
length, and retain some characteristics of the original value. For example, if a Vehicle
Registration Number such as `OU51 SMR` was being anonymized, the result would
look similar to `BB88 9AA`.

Organizations need the ability to anonymize full datasets as well as single records.
Single record anonymization functionality can help deliver right to erasure and meet
data retention requirements. In this case, full batch anonymization is typically used
when obfuscating development and UAT environments.

The function to anonymize information should support the flexibility to anonymize
certain fields, but not all.

Operational databases, reporting databases, and analytical data marts should all be
considered for anonymization, although reports and analytical cubes should never
typically contain PII information regardless.

Audit the reason why information was anonymized, for example, data portability, or
data retention removal. The time, date, and user ID of when and who the anonymization
process has affected should be recorded in an audit table.

For more details, see AWS Big Data Blog: [Anonymize and manage data in your data lake with Amazon Athena and AWS Lake Formation](https://aws.amazon.com/blogs/big-data/anonymize-and-manage-data-in-your-data-lake-with-amazon-athena-and-aws-lake-formation/)

### Suggestion 3.1.2.2 – Pseudonymization

**Pseudonymized data is not the same as anonymized data.**

When data has been pseudonymized, it still retains a level of detail in the target
data that allows tracking back of the data to its original state. With anonymized data,
the level of detail is reduced rendering a reverse compilation impossible.
Pseudonymization is the processing of personal data in such a way that the data can only
be attributed to a specific data subject by using additional information. To
pseudonymize a dataset, the additional information must be kept separately and subject
to technical and organizational measures to ensure non-attribution to an identified or
identifiable person.

In summary, pseudonymized data is a privacy-enhancing technique where directly
identifying data, such as IP addresses and contact information, are held separately and
securely from processed data to ensure non-attribution. Similar to anonymization,
referential integrity must not be affected. Therefore, both of the following are
required: an audit trail of the pseudonymization process, and a pseudonymization
function that supports both single item and batch processing.

For more detail, see [Amazon Redshift Data Masking](https://docs.aws.amazon.com/redshift/latest/dg/t_ddm.html).

### Suggestion 3.1.2.3 – Tokenization

*Tokenization*, when applied to data security, is
the process of substituting a sensitive data element with a non-sensitive equivalent.
This is referred to as a token, which has no extrinsic or exploitable meaning or value.
The token is a reference that maps back to the sensitive data through a tokenization
system. Tokenization is typically used in finance to tokenize the payment account number
(PAN).

For more details, refer to the following information:

- AWS Blog – [AWS Glue DataBrew detection data masking transformations](https://aws.amazon.com/about-aws/whats-new/2021/11/aws-glue-databrew-detection-data-masking-transformations/)
- AWS Blog - [Data Tokenization with Amazon Redshift and Protegrity](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/)

## Suggestion 3.1.3 – Rights of the individual, citizen, or subject

Your organization should consider the process to address
the rights of the individual, citizen, or subject for
their respective regional regulation.

### Suggestion 3.1.3.1 – Subject Access Request (SAR)

This particular right is for an individual to request
information from the data controller, that is, how their
personal data is being processed. If an individual’s
information is being processed, the personal data and
associated metadata must be provided to that individual.

If the individual’s information is stored in a database, then an automated process, such as a stored procedure or User-Defined Function (UDF), should be developed to answer the Subject Access Request (SAR). There will, however, be situations when the individual’s information is stored in Amazon S3. If the information is stored in Amazon S3, the proposed solution to identify which S3 object contains the respective information is to build a lookup table in a database containing the reference number, individual contact details, and the S3 object location. This approach allows your organization to ingest the information into Amazon EMR, infer the schema using Apache Spark, and extract the information required to fulfill the request. Alternatively, your organization must process all S3 objects to identify the information to fulfill the request.

If your regional regulations require that your organization handle a right to data portability request, then the SAR logic can double up to support that as well.

For more details, see Apache Spark Documentation -
[Inferring
the Schema Using Reflection](https://spark.apache.org/docs/2.3.0/sql-programming-guide.html#:~:text=Inferring%20the%20Schema%20Using%20Reflection,-Scala&text=The%20Scala%20interface%20for%20Spark,the%20names%20of%20the%20columns.)

### Suggestion 3.1.3.2 – Right to be forgotten or erasure

Individuals have the right to erasure (the right to be forgotten), where an
individual can request that all of their personal data is erased by the data controller
organization. In some countries, there are instances where the data controller can
refuse to comply with a right to erasure request, such as where the data is used for
financial governance.

The right to erasure does not strictly mean that the individual’s information must
be deleted. Instead, it can be permanently masked so that the personal data is no longer
in the clear and the update is irreversible.

The organization must consider all data repositories when responding to a SAR as an
individual’s information can reside in back up and source system databases. All these
records must have the individual’s information removed or anonymized.

If there are concerns about the impact of database referential integrity being
affected by removing the individual’s information, then you can consider anonymization
of the specific data attributes for the given individual. There are benefits to
anonymization, such as being able to maintain an audit history of what actions have been
performed against the individual by referencing a system ID. The same steps that are
performed in production environments must also be run in UAT, development, OLTP, and
back up repositories.

The schedule of running the procedure in the other environments depends on the
refresh schedules of those other environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.1-privacy-by-design..html*

---

# Best practice 3.2 – Classify and protect data

**How do you classify and protect data
in analytics workload?** Because analytics
workloads ingest data from source systems, the owner of the
source data should define the data classifications. As the
analytics workload owner, you should honor the source data
classifications and implement the corresponding data
protection policies of your organization. Share the data
classifications with the downstream data consumers to permit
them to honor the data classifications in their
organizations and policies as well.

Data classification helps to categorize organizational data
based on sensitivity and criticality, which then helps
determine appropriate protection and retention controls on
that data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.2---classify-and-protect-data..html*

---

# Best practice 3.3 – Understand data classifications and their protection policies

Data classification in your organization is key to
determining how data must be protected while at rest and in
transit. For example, since an analytics workload
necessarily copies and shares data between operations and
systems, we recommend that access be controlled to certain
data classifications. Such a data protection strategy helps
to prevent data loss, theft, and corruption, and helps to
minimize the impact caused by malicious activities or
unintended access.

## Suggestion 3.3.1 – Identify classification levels

Use the
[Data
Classification whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html) to help you identify
different classification levels. Four common levels used
are restricted, confidential, internal, and public,
however, these levels can vary based on the industry and
compliance requirements of your organization.

## Suggestion 3.3.2 – Define access rules

The data owners should define the data access rules based
on the sensitivity and criticality of the data. For
example, with AWS Lake Formation, you can define and
enforce access controls that operate at the table, column,
row, and cell level for all the users that access your
data lake.

For more details, refer to the following information:

- AWS Security Blog:
[How
to scale your authorization needs by using
attribute-based access control with](https://aws.amazon.com/blogs/security/how-to-scale-authorization-needs-using-attribute-based-access-control-with-s3/)
[S3](https://aws.amazon.com/blogs/security/how-to-scale-authorization-needs-using-attribute-based-access-control-with-s3/).
- AWS Big Data Blog:
[Create
a secure data lake by masking, encrypting data, and
enabling fine-grained access with AWS Lake Formation.](https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/)
- AWS Big Data Blog:
[Control
data access and permissions with AWS Lake Formation and
Amazon EMR](https://aws.amazon.com/blogs/big-data/control-data-access-and-permissions-with-aws-lake-formation-and-amazon-emr/).
- AWS Big Data Blog:
[Enforce
column-level authorization with Quick and
AWS Lake](https://aws.amazon.com/blogs/big-data/enforce-column-level-authorization-with-amazon-quicksight-and-aws-lake-formation/)
[Formation](https://aws.amazon.com/blogs/big-data/enforce-column-level-authorization-with-amazon-quicksight-and-aws-lake-formation/).

## Suggestion 3.3.3 – Identify security zone models to isolate data based on classification

Design the security zone models from AWS account levels
down to AWS resource levels. For example, consider
building AWS multi-account models to isolate different
classes of data from AWS account level. Or, you can
consider separating out development and test resources
from production ones from AWS account level or from
resource levels.

For more details, refer to the following information:

- AWS Whitepaper:
[An
Overview of the AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html).
- AWS Whitepaper:
[Organizing
Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html).
- AWS Whitepaper:
[Security
Pillar – AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

## Suggestion 3.3.4 – Identify sensitive information and define protection policies

Discover sensitive data by using custom data identifiers in Amazon Macie or using AWS Glue sensitive data detection. Based on
the sensitivity and criticality of the data, implement data protection policies to prevent
unauthorized access. Due to compliance requirements, data might be masked or deleted after
processing in some cases.

For more details, refer to the following information:

- AWS Blog:
[Introducing
PII data identification and handling using AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/)
- AWS Blog:
[Create
a secure data lake by masking, encrypting data, and
enabling fine-grained access with AWS Lake Formation](https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/)
- AWS Info: [AWS Glue detect and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.3---understand-data-classifications-and-their-protection-policies..html*

---

# Best practice 3.4 – Identify the source data owners and have them set the data classifications

Identify the owners of the source data, like business data owners, and agree what level of protection is required for the data within the analytics platform.

Data classifications follow the data as it moves throughout
the analytics workﬂow to ensure that the data is protected,
and to determine who and what systems are allowed to access
the data. By following the organization’s classification
policies, the analytics workload should be able to
differentiate the data protection implementations for each
class of data. Because each organization has different kinds
of classification, the analytics workload should provide a
strong logical boundary between processing data of different
sensitivity levels. These classifications include
*restricted*,
*confidential*, and
*sensitive*.

## Suggestion 3.4.1 – Assign owners per each dataset

A dataset, or a table in relational database, is a collection of data. A Data Catalog is a collection of metadata that helps centralize share and search information about the data within your platform. In addition to assigned classifications, this capability allows teams to search for data assets and decide whether the data asset is valuable for their analyze or data science workload.

The administrator of the analytics workload should know who are the owners for each dataset, and should assign the dataset ownership in the Data Catalog.

## Suggestion 3.4.2 – Define attestation scope and reviewer as additional scope for sensitive data

As the owner of the analytics workload, you should know
the data owner for each dataset. For example, when a
dataset classified as highly sensitive has permission
issues within the organization, you might have to talk to
the dataset owners and have them resolve the issues.

## Suggestion 3.4.3 – Set expiry for data ownership and attestation, and have owners reconfirm periodically

As businesses change, the data owners and the data
classifications might change as well. Run campaigns
periodically, such as quarterly or yearly, to request each
of the dataset owners to reconfirm that they are still the
right owners, and that the data classifications are still
accurate.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.4---identify-the-source-data-owners-and-have-them-set-the-data-classifications..html*

---

# Best practice 3.5 – Record data classifications into the Data Catalog so that analytics workloads can understand

Allow processes to update the Data Catalog so it can provide
a reliable record of where the data is located and its
precise classification. To protect the data effectively,
analytics systems should know the classifications of the
source data so that the systems can govern the data
according to business needs. For example, if the business
requires that confidential data be encrypted using team-owned
private keys, such as from AWS Key Management Service (AWS KMS), then the analytics workload should be able to
determine which data is classified as confidential by
referencing its data catalog.

## Suggestion 3.5.1 – Use tags to indicate the data classifications

Use a tagging ontology to designate the classiﬁcation of sensitive data in data stores with a data catalog. A tagging ontology allows discoverability of data sensitivity without directly exposing the underlying data.
They also can be used to authorize access in
[tag-based access control (TBAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) schemes.

For more details, refer to the following information:

- AWS Lake Formation Developer Guide:
[What
Is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- AWS Whitepaper: [Tagging
Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- AWS Lake Formation: [Easily manage your data lake at scale using AWS Lake Formation Tag-based access control](https://aws.amazon.com/blogs/big-data/easily-manage-your-data-lake-at-scale-using-tag-based-access-control-in-aws-lake-formation/)

## Suggestion 3.5.2 – Record lineage of data to track changes in the Data Catalog

Data lineage is a relation among data and the processing
systems. For example, the data lineage tells where the
source system of the data has come from, what changes
occurred to the data, and which downstream systems have
access to it. Your organization should be able to
discover, record, and visualize the data lineage from
source to target systems.

For more details, refer to the following information:

- AWS Big Data Blog:
[Metadata
classification, lineage, and discovery using Apache
Atlas on Amazon EMR](https://aws.amazon.com/blogs/big-data/metadata-classification-lineage-and-discovery-using-apache-atlas-on-amazon-emr/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.5---record-data-classifications-into-the-data-catalog-so-that-analytics-workloads-can-understand..html*

---

# Best practice 3.6 – Implement encryption policies

Data encryption is a way of translating data from plaintext
(unencrypted) to ciphertext (encrypted). Encryption is a
critical component of a *defense in
depth* strategy. Therefore, it is highly
recommended that your organization implement a well-designed
encryption and key management system by separating access to
the decryption key from access to your data to provide data
security.

## Suggestion 3.6.1 – Implement encryption policies for data at rest and in transit

Each analytics service provides different types of encryption methods.
Review the viable encryption methods of your solutions and
implement as necessary.

For more details, refer to the following information:

- [AWS Key Management Service (AWS KMS) encryption best practices](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/kms.html)
- AWS Big Data Blog:
[Best
Practices for Securing Amazon EMR](https://aws.amazon.com/blogs/big-data/best-practices-for-securing-amazon-emr/)
- AWS Big Data Blog:
[Encrypt
Your Amazon Redshift Loads with Amazon S3 and AWS KMS](https://aws.amazon.com/blogs/big-data/encrypt-your-amazon-redshift-loads-with-amazon-s3-and-aws-kms/)
- AWS Big Data Blog:
[Encrypt
and Decrypt Amazon Kinesis Records Using AWS KMS](https://aws.amazon.com/blogs/big-data/encrypt-and-decrypt-amazon-kinesis-records-using-aws-kms/)
- AWS Partner Network (APN) Blog:
[Data
Tokenization with Amazon Redshift and Protegrity](https://aws.amazon.com/blogs/apn/data-tokenization-with-amazon-redshift-and-protegrity/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.6---implement-encryption-policies.html*

---

# Best practice 3.7 – Implement data retention policies for each class of data in the analytics workload

The business’s data classification policies determine how
long the analytics workload should retain the data and how
long backups should be kept. These policies help ensure that
every system follows the data security rules and compliance
requirements. The analytics workload should implement data
retention and backup policies according to these data
classification policies. For example, if the policy requires
every system to retain the operational data for five years,
the analytics systems should implement rules to keep the
in-scoped data for five years. More information on data
retention can be found in [Sustainability](./sustainability.html).

## Suggestion 3.7.1 – Create backup requirements and policies based on data classifications

Data backup should be based on business requirements, such
as recovery point objective (RPO), recovery time objective
(RTO), data classifications, and the compliance and audit
requirements.

## Suggestion 3.7.2 – Create data retention requirement policies based on the data classifications

Avoid creating blanket retention policies. Instead,
policies should be tailored to individual data assets
based on their retention requirements.

For more details, refer to the following information:

- AWS Big Data Blog:
[Building
a cost efficient, petabyte-scale lake house with Amazon S3
Lifecycle rules](https://aws.amazon.com/blogs/big-data/part-1-building-a-cost-efficient-petabyte-scale-lake-house-with-amazon-s3-lifecycle-rules-and-amazon-redshift-spectrum/)
[and
Amazon Redshift Spectrum: Part 1](https://aws.amazon.com/blogs/big-data/part-1-building-a-cost-efficient-petabyte-scale-lake-house-with-amazon-s3-lifecycle-rules-and-amazon-redshift-spectrum/)
- AWS Big Data Blog:
[Retaining
data streams up to one year with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/retaining-data-streams-up-to-one-year-with-amazon-kinesis-data-streams/)
- AWS Big Data Blog:
[Retain
more for less with UltraWarm for Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/retain-more-for-less-with-ultrawarm-for-amazon-opensearch-service/)

## Suggestion 3.7.3 – Create data version requirements and policies

Implement a process that captures the data version to
address, based on compliance, security, and operational
requirements.

For more details, refer to the following information:

- AWS Storage Blog:
[Reduce
storage costs with fewer noncurrent versions using
Amazon S3 Lifecycle](https://aws.amazon.com/blogs/storage/reduce-storage-costs-with-fewer-noncurrent-versions-using-amazon-s3-lifecycle/)
- AWS Storage Blog:
[Simplify
your data lifecycle by using object tags with Amazon S3
Lifecycle](https://aws.amazon.com/blogs/storage/simplify-your-data-lifecycle-by-using-object-tags-with-amazon-s3-lifecycle/)
- AWS Database Blog:
[Implementing
version control using Amazon DynamoDB](https://aws.amazon.com/blogs/database/implementing-version-control-using-amazon-dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.7---implement-data-retention-policies-for-each-class-of-data-in-the-analytics-workload..html*

---

# Best practice 3.8 – Enforce downstream systems to honor the data classifications

Since other data-consuming systems will access the data that
the analytics workload shares, the workload should require
the downstream systems to implement the required data
classification policies. For example, if the analytics
workload shares the data that is required to be encrypted
using customer managed private keys in AWS Key Management Service (AWS KMS), then the downstream systems should also
acknowledge and implement such a data protection policy.

This helps to ensure that the data is protected throughout
the data pipelines.

## Suggestion 3.8.1 – Have a centralized, shareable catalog with cross-account access to ensure that data owners manage permissions for downstream systems

Downstream systems can run on independent AWS accounts,
different from the AWS account running the majority of the
analytics workload. Downstream systems should be able to
discover the data, acknowledge the required data
protection policies, and enforce those policies across the
analytics platform.

To allow the downstream systems to use the data from
analytics workload, the analytics workload should provide
cross-account access based on least privileges for each
dataset.

For more details, refer to the following information:

- AWS Big Data Blog: [Cross-account AWS Glue Data Catalog access with Amazon Athena](https://aws.amazon.com/blogs/big-data/cross-account-aws-glue-data-catalog-access-with-amazon-athena/)
- AWS Big Data Blog:
[How
JPMorgan Chase built a data mesh architecture to drive
significant value to](https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/)
[enhance
their enterprise data platform](https://aws.amazon.com/blogs/big-data/how-jpmorgan-chase-built-a-data-mesh-architecture-to-drive-significant-value-to-enhance-their-enterprise-data-platform/)

## Suggestion 3.8.2 – Monitor the downstream systems’ eligibility to access classified data from the analytics workload

Monitor the downstream systems’ eligibility to handle
sensitive data. For example, you do not want development
or test Amazon Redshift clusters to read sensitive data
from the analytics workload. If your organization runs a
program that certifies which systems are eligible to
process various classes of data, periodically verify that
each downstream system’s data processing eligibility
levels are correct and the list of data that it accesses
are appropriate.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-3.8---enforce-downstream-systems-to-honor-the-data-classifications..html*

---

## 4 – Implement data access control

# Best practice 4.1 – Allow data owners to determine which people or systems can access data in analytics and downstream workloads

Data owners are the people that have direct responsibility
for data protection. For instance, the data owners want to
determine which data is publicly accessible, or which data
is restricted access to whom or what systems. The data
owners should be able to provide data access rules, so that
the analytics workload can implement the rules.

## Suggestion 4.1.1 – Identify data owners and assign roles

Data ownership is the management and oversight of an
organization's data assets to help provide business users
with high-quality data that is easily accessible in a
consistent manner. Because the analytics workload
consolidates multiple datasets into a central place, each
dataset is owned by different teams or people. So, it is
important for the analytics workload to identify which
dataset is owned by whom to have the owners control the
data access permissions.

## Suggestion 4.1.2 – Identify permission using a permission matrix for users and roles based on actions performed on the data by users and downstream systems

To aid in identifying and communicating data-access
permissions, an Access Control Matrix is a helpful method
to document which users, roles, or systems have access to
which datasets, and to describe what actions they can
perform. Below is a sample matrix for two users, and two
roles for two schemas with a table in them:

Table 1: Example Access Control Matrix for Users and Roles

**Permissions**

**Read**

**Write**

Schema 1

User1, User2, Role1, Role2

Role1

Schema 1 / Table 1

User1, User2, Role1, Role2

Role2

Schema 2

User1, User2, Role1, Role2

User1, Role1

Schema 2 / Table 2v

User1, User2, Role1, Role2

User2, Role2

The matrix format can help identify the least permissions
that are required by various resources and to avoid
overlaps. An Access Control Matrix should be thought of as
an abstract model of permissions at a given point in time.
Periodically review the actual access permissions against
the permission matrix document to ensure accuracy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.1---allow-data-owners-to-determine-which-people-or-systems-can-access-data-in-analytics-and-downstream-workloads..html*

---

# Best practice 4.2 – Build user identity solutions that uniquely identify people and systems

To control data access effectively, the analytics workload
should be able to uniquely identify the people or systems.
For example, the workload should be able to tell who
accessed to the data by looking at the user identifiers (such
as user names, tags, or IAM role names) with confidence that
the identifier represents only one person or system.

For more details, refer to the following information:

- AWS Big Data Blog:
[Amazon Redshift identity federation with multi-factor
authentication](https://aws.amazon.com/blogs/big-data/amazon-redshift-identity-federation-with-multi-factor-authentication/)
- AWS Big Data Blog:
[Federating
single sign-on access to your Amazon Redshift cluster with
PingIdentity](https://aws.amazon.com/blogs/big-data/federating-single-sign-on-access-to-your-amazon-redshift-cluster-with-pingidentity/)
- AWS Database Blog:
[Get
started with Amazon OpenSearch Service: Use Amazon Cognito for Kibana](https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-use-amazon-cognito-for-kibana-access-control/)
[access
control](https://aws.amazon.com/blogs/database/get-started-with-amazon-elasticsearch-service-use-amazon-cognito-for-kibana-access-control/)
- AWS Partner Network (APN) Blog:
[Implementing
SAML AuthN for Amazon EMR Using Okta and](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/)
[Column-Level
AuthZ with AWS Lake Formation](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/)
- AWS CloudTrail User Guide:
[How
AWS CloudTrail works with IAM](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/security_iam_service-with-iam.html)

## Suggestion 4.2.1 – Centralize workforce identities

It’s a best practice to centralize your workforce
identities, which allows you to federate with AWS Identity and Access Management (IAM) using AWS IAM Identity Center
or another federation
provider. In Amazon Redshift, IAM roles can be mapped to
Amazon Redshift database groups. In Amazon EMR, IAM roles
can be mapped to an Amazon EMR security configuration or an
Apache Ranger Microsoft Active Directory group-based
policy. In AWS Glue, IAM roles can be mapped to AWS AWS Glue Data Catalog resource policies.

AWS analytics services – such as Amazon OpenSearch Service
and Amazon DynamoDB – allow integration with Amazon Cognito for authentication. Amazon Cognito lets you add
user sign-up, sign- in, and access control to your web and
mobile apps. Amazon Cognito scales to millions of users
and supports sign-in with social identity providers, such
as Apple, Facebook, Google, and Amazon, and enterprise
identity providers via SAML 2.0 and OpenID Connect.

For more details, refer to the following information:

- AWS Big Data Blog:
[Federate
Database User Authentication Easily with IAM and Amazon Redshift](https://aws.amazon.com/blogs/big-data/federate-database-user-authentication-easily-with-iam-and-amazon-redshift/)
- WS Big Data Blog:
[Federating
single sign-on access to your Amazon Redshift cluster
with PingIdentity](https://aws.amazon.com/blogs/big-data/federating-single-sign-on-access-to-your-amazon-redshift-cluster-with-pingidentity/)
- Amazon EMR Management Guide:
[Allow
AWS IAM Identity Center for Amazon EMR Studio](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-studio-enable-sso.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.2---build-user-identity-solutions-that-uniquely-identify-people-and-systems..html*

---

# Best practice 4.3 – Implement the required data access authorization models

User authorization determines what actions that a user is
permitted to take on the data or resource. The data owners
should be able to use the authorization methods to protect
their data as needed. For example, if the data owners must
control which users are allowed to view certain columns of
data, the analytics workload should provide column-wise data
access authorization along with user group management for an
effective control.

## Suggestion 4.3.1 – Implement IAM policy-based data access controls

Limit access to sensitive data stores with IAM policies
where possible. Provide systems and people with rotating
short-term credentials via role-based access control
(RBAC).

For more details, see AWS Big Data Blog: [Restrict access to your AWS Glue Data Catalog with resource-level IAM permissions and resource-based policies](https://aws.amazon.com/blogs/big-data/restrict-access-to-your-aws-glue-data-catalog-with-resource-level-iam-permissions-and-resource-based-policies/)

## Suggestion 4.3.2 – Implement dataset-level data access controls

As dataset owners require independent rules of granting
data access, you should build the analytics workloads to
have the dataset owners control the data access per each
dataset level. For example, if the analytics workload
hosts a shared Amazon Redshift cluster, the owners of the
individual table should be able to authorize the table
read and write independently.

For more details, refer to the following information:

- AWS Big Data Blog:
[Validate,
evolve, and control schemas in Amazon MSK and Amazon Kinesis Data](https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/)
[Streams
with AWS Glue Schema Registry](https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/).
- Amazon Redshift:
[Amazon Redshift announces support for Row-Level Security
(RLS)](https://aws.amazon.com/about-aws/whats-new/2022/07/amazon-redshift-row-level-security/)
[Streams
with AWS Glue Schema Registry](https://aws.amazon.com/blogs/big-data/validate-evolve-and-control-schemas-in-amazon-msk-and-amazon-kinesis-data-streams-with-aws-glue-schema-registry/).

## Suggestion 4.3.3 – Implement column-level data access controls

Care should be taken that end users of analytics
applications are not exposed to sensitive data. Downstream
consumers of data should only access the limited view of
data necessary for that analytics purpose. Enforce that
sensitive data is not exposed using column-level
restrictions, for example, mask the sensitive columns to
downstream systems so an accidental exposure is avoided.

For more details, refer to the following information:

- AWS Big Data Blog:
[Allow
fine-grained permissions for Quick authors in
AWS Lake](https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/)
[Formation](https://aws.amazon.com/blogs/big-data/enable-fine-grained-permissions-for-amazon-quicksight-authors-in-aws-lake-formation/)
- Amazon Redshift: [Role-based access controls](https://docs.aws.amazon.com/redshift/latest/dg/t_Roles.html)
- AWS Partner Network (APN) Blog:
[Implementing
SAML AuthN for Amazon EMR Using Okta and](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/)
[Column-Level
AuthZ with AWS Lake Formation](https://aws.amazon.com/blogs/apn/implementing-saml-authn-for-amazon-emr-using-okta-and-column-level-authz-with-aws-lake-formation/)
- AWS Big Data Blog:
[Implementing
Authorization and Auditing using Apache Ranger on Amazon EMR](https://aws.amazon.com/blogs/big-data/implementing-authorization-and-auditing-using-apache-ranger-on-amazon-emr/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.3---implement-the-required-data-access-authorization-models..html*

---

# Best practice 4.4 – Establish an emergency access process to ensure that admin access is managed and used when required

Emergency access allows expedited access to your workload in
the unlikely event of an automated process or pipeline
issue. This will help you rely on least privilege access,
but still provide users the right level of access when they
require it.

## Suggestion 4.4.1 – Ensure that risk analysis is performed on your analytics workload by identifying emergency situations and a procedure to allow emergency access

Identify the potential events that can happen from source
systems, analytics workload, and downstream systems.
Quantify the risk of each event such as likelihood (low,
medium, or high) and the size of the business impact
(small, medium, or large).

For example, after you identified priority risks, discuss
with the source and downstream system owners on how to
allow analytics workload access to the source and
downstream systems to continue the data processing
business.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.4---establish-an-emergency-access-process-to-ensure-that-admin-access-is-managed-and-used-when-required..html*

---

# Best practice 4.5 – Track data and database changes

Data auditing involves monitoring a database to track the
actions of a user or process, and to audit the changes that
have occurred to the data.

## Suggestion 4.5.1 – Database triggering for data auditing

A database trigger is procedural code that is
automatically run in response to certain events on a
particular table or view in a database. Database triggers
can then be used to update an audit table with the changes
that have occurred. The types of information that should
be included in the auditing process include: the original
and updated value of what has been updated, the process or
stored procedure that made the update, and the time and
date the update occurred.

## Suggestion 4.5.2 – Enable advanced auditing

If your database engine supports auditing as a native
feature, you should enable the feature to record and audit
database events such as connections, disconnections,
tables queried, or types of queries issued.

## Suggestion 4.5.3 – AWS Lake Formation time travel queries

Apache Iceberg and Apache Hudi provide a high-performance data lake table format that works just like a SQL table. Iceberg and Hudi make it simple to manage your data lake information and support SQL type analytics. Data that is managed by Iceberg or Hudi is version-controlled, therefore there is a complete history of all data updates. A good example is if you need to know the status of an individual at a certain time, then a time travel query allows you to select a date range to return the value that existed at that time, rather than the current value.

For more details, see [Use the AWS Glue connector to read and write Apache Iceberg tables with ACID transactions and perform time travel](https://aws.amazon.com/blogs/big-data/use-aws-glue-to-read-and-write-apache-iceberg-tables-with-acid-transactions-and-perform-time-travel/).

## Suggestion 4.5.4 – Change Data Capture (CDC)

CDC records `INSERT`s, `UPDATE`s, and `DELETE`s
applied to relational database tables, and makes a log available of which relational
database objects changed, where, and when. These change tables contain columns that
reflect the column structure of the source table you have chosen to track, along with the
metadata required to understand the changes that have been made.

For more details, refer to the following information:

- AWS CloudTrail -
[Secure
Standardized Logging](https://aws.amazon.com/cloudtrail/)
- Amazon RDS Aurora -
[Advanced
Auditing with an Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Auditing.html)
- Amazon RDS Aurora -
[Configuring
an audit log to capture database activities for Amazon RDS](https://aws.amazon.com/blogs/database/configuring-an-audit-log-to-capture-database-activities-for-amazon-rds-for-mysql-and-amazon-aurora-with-mysql-compatibility/)
- AWS Database Migration Service (AWS DMS)
[AWS Database Migration Service](https://aws.amazon.com/dms/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-4.5-track-data-and-database-changes..html*

---

## 5 – Control the access to workload infrastructure

# Best practice 5.1 – Prevent unintended access to the infrastructure

Grant least privilege access to infrastructure to help
prevent inadvertent or unintended access to the
infrastructure. For example, make sure that anonymous users
are not allowed to access to the systems, and that the
systems are deployed into isolated network spaces. Network
boundaries isolate analytics resources and restrict network
access. Network access control lists (NACLs) act as a
firewall for controlling traffic in and out. To reduce the risk
of inadvertent access, define the network boundaries of the
analytics systems and only allow intended access.

## Suggestion 5.1.1 – Ensure that resources in the infrastructure have boundaries

Use infrastructure boundaries for services such as
databases. Place services in their own VPC private subnets
that are configured to allow connections only to needed
analytics systems.

Use
[AWS Identity and Access Management (IAM) Access
Analyzer](https://aws.amazon.com/iam/features/analyze-access/) for all AWS accounts that are centrally
managed through
[AWS Organizations.](https://aws.amazon.com/organizations/) This allows security teams and
administrators to uncover unintended access to resources
from outside their AWS organization within minutes.

You can proactively address whether any resource policies
across any of your accounts violate your security and
governance practices by allowing unintended access.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.1---prevent-unintended-access-to-the-infrastructure..html*

---

# Best practice 5.2 – Implement least privilege policies for source and downstream systems

The principle of least privilege works by giving only enough
access for systems to do the job. Set an expiry on temporary
permissions to ensure that re-authentication occurs
periodically. The system actions on the data should
determine the permission and granting permissions to other
systems should not be permitted.

## Suggestion 5.2.1 – Ensure that permissions are least for the action performed by user/system

Identify the minimum privileges that each user or system
requires, and only allow the permissions that they need.
For example, if a downstream system requests to read an
Amazon Redshift table from an analytics workload, only
give the read permission for the table using Amazon Redshift user privilege controls.

For more details, refer to the following information:

- AWS Security Blog:
[Techniques
for writing least privilege IAM policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/)
- Amazon Redshift Database Developer Guide:
[Managing
database security](https://docs.aws.amazon.com/redshift/latest/dg/r_Database_objects.html)
- AWS Security Blog:
[IAM
Access Analyzer makes it easier to implement least
privilege permissions by](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)
[generating
IAM policies based on access activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/)

## Suggestion 5.2.2 – Implement the two-person rule to prevent accidental or malicious actions

Even if you have implemented the least privilege policies,
someone must have critical permissions for the business,
such as the ability to delete datasets from analytics
workloads.

The two-person rule is a safety mechanism that requires
the presence of two authorized personnel to perform tasks
that are considered important. It has its origins in
military protocol, but the IT security space has also
widely adopted the practice.

By implementing the two-person rule, you can have
additional prevention of accidental or malicious actions
of the people who have critical permissions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.2---implement-least-privilege-policies-for-source-and-downstream-systems..html*

---

# Best practice 5.3 – Monitor the infrastructure changes and the user activities against the infrastructure

As the infrastructure changes over time, you should monitor
what has been changed by whom. This is to ensure that such
changes are deliberate and the infrastructure is still
protected.

## Suggestion 5.3.1 – Monitor the infrastructure changes

You want to know every infrastructure change and want to
know that such changes are deliberate. Monitor the
infrastructure changes using available methods on your
team. For example, you can implement an operation
procedure to review the infrastructure configurations every
quarter of the year. Or, you can use AWS services that
assist you to monitor the infrastructure changes with less
effort.

For more details, refer to the following documentation:

- AWS Config Developer Guide:
[What
Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- Amazon Inspector User Guide:
[What
is Amazon Inspector?](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html)
- Amazon GuardDuty User Guide:
[Amazon S3 protection in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/s3_detection.html)

## Suggestion 5.3.2 – Monitor the user activities against the infrastructure

You want to know who is changing the infrastructure and
when, so that you can see that any given infrastructure
change is performed by an authorized person or system. To
do so, as examples, you can implement an operation
procedure to review the AWS CloudTrail audit logs every
quarter of the year. Or you can implement near real time
trend analysis using AWS services such as Amazon CloudWatch Logs Insights.

For more details, refer to the following information:

- AWS CloudTrail User Guide:
[Monitoring
CloudTrail Log Files with Amazon CloudWatch Logs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.html)
- AWS Management and Governance Blog:
[Analyzing
AWS CloudTrail in Amazon CloudWatch](https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.3---monitor-the-infrastructure-changes-and-the-user-activities-against-the-infrastructure..html*

---

# Best practice 5.4 – Secure the audit logs that record every data or resource access in analytics infrastructure

Logs are an audit trail of events and should be stored in an immutable format for compliance purposes. These logs provide proof of actions
and help in identifying misuse. The logs provide a baseline
for analysis or for an audit when initiating an
investigation. By using a fault-tolerant storage for these
logs, it is possible to recover them even when there is a
failure in the auditing systems. Access permissions to these
logs must be restricted to privileged users. Also log audit
log access to help in identifying unintended access to audit
data.

## Suggestion 5.4.1 – Ensure that auditing is active in analytics services and are delivered to fault-tolerant persistent storage

Review the available audit log features of your analytics
solutions, and configure the solutions to store the audit
logs to fault-tolerant persistent storage. This helps
ensure that you have complete audit logs for security and
compliance purposes.

For more details, refer to the following information:

- AWS Management and Governance Blog:
[AWS CloudTrail Best Practices](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/)
- Amazon Redshift Cluster Management Guide:
[Database
audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html)
- Amazon OpenSearch Service (successor to Amazon OpenSearch Service) Developer Guide:
[Monitoring](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html)
[audit
logs in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html)
- AWS Technical Guide – Build a Secure Enterprise Machine
Learning Platform on AWS:
[Audit
trail](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/audit-trail-management.html)
[management](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/audit-trail-management.html)
- AWS Big Data Blog:
[Build,
secure, and manage data lakes with AWS Lake Formation](https://aws.amazon.com/blogs/big-data/building-securing-and-managing-data-lakes-with-aws-lake-formation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-5.4---secure-the-audit-logs-that-record-every-data-or-resource-access-in-analytics-infrastructure..html*

---
