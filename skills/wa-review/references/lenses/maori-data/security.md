# Security

**Pillar**: Security  
**Pages**: 4

---

# MD_SEC 1: How is Māori data protected?

Systems designed to capture, store, or process Māori data should follow the same best
practice as any other cloud solution in that they should be designed, built, and operated with
security in mind. The Security Pillar of the Well-Architected Framework provides in-depth,
best practice guidance for architecting secure workloads. The [Data protection](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-dataprot.html) best
practice area in the Security Pillar provides best practices relating to data classification,
protecting data at rest, and protecting data in transit. Data protection is just one aspect of
securing your cloud architectures. Security should be applied at all layers through multiple
controls using a defence-in-depth approach. In addition to the best practices contained in the
Security Pillar, the following considerations may also apply:

- **MD_SEC01-BP01: Design storage systems to handle data with different
Māori data classifications.** If the data is considered tapu and that is
feedback you have received from your customers, then it may be appropriate to apply
additional controls and procedures. These may be required to support specific tikanga
related to the handling of certain data. You may choose to store certain data separately
from other data with different security requirements for access and processing. It is
possible, for example, to store data in separate virtual private clouds (VPC), separate
databases, or separate object storage buckets. This separation of datasets means you can
apply independent security controls, such as different access permissions, different
logging and auditing levels, and different backup approaches.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-1-how-is-māori-data-protected.html*

---

# MD_SEC 2: How do you design workload security for long-term safety?

Certain Māori data may need to be available for generations to come. Consult with Māori
customers and advisers about what data retention policies they recommend according to the
different types of data. These data retention policies can be revisited in the future too.
Regardless of how long you are intending to store this data, all data needs to be properly
secured for the protection of taonga (treasure) for generations to come.

Ransomware is a good example to consider. If you have one copy of your data and you are
subject to a ransomware attack, you may not be able to recover your data. Consider how many
backup copies may be required to protect yourself from this scenario. Design appropriate
access controls to minimise the chance of accidental or malicious deletion or corruption of
back-ups. While it may seem redundant, it's important to store backups across multiple
different types of storage and in multiple different locations. With this strategy, there's
always an available backup, no matter the circumstances. Where irreplaceable digital taonga is
identified, it is important to consider offline replication in addition to the appropriate
data protection and resilience controls.

- **MD_SEC02-BP01: Understand data protection options available through
your provider to protect data at the level of control your customer wants.**
Customers control how they configure their environments and secure their content,
including whether they encrypt their content (at rest and in transit), and what other
security features and tools they use and how they use them. AWS does not change customer
configuration settings, as these settings are determined and controlled by the customer.
AWS customers have the ability to design their security architecture to meet
their compliance needs. AWS provides the customer autonomy to decide when and how
security measures are implemented in the cloud, in accordance with each customer's
business needs. When choosing which option is best, you should understand the risks you
are trying to mitigate, take into account both the benefits and costs of each solution,
and choose a solution that meets your requirements. Choose a cloud provider that offers
contractual restrictions on their access to your data and operational restrictions. AWS,
for example, is one of those cloud providers who offers both.
- **MD_SEC02-BP02: Understand what encryption options are available to
protect your data at rest and in transit.** Encryption of data at rest is a
recommended best practice for protecting your data from unauthorised access. AWS
provides several options for data encryption. One option is to have AWS create and
manage encryption keys for you through the AWS Key Management Service. Many AWS services integrate with
AWS KMS to enable encryption of your data. Another option is to create your own encryption
keys within AWS KMS. This provides you with more control over your keys. This includes
control over the key material, the rotation policy, and the permissions that define who
can use or manage the key. AWS KMS is designed so that no one, not even an AWS employee,
can retrieve your plaintext KMS keys from the service.
- **MD_SEC02-BP03: Make informed decisions about where data is
stored**. Māori users of your system may prefer their data to be stored in New
Zealand. AWS allows customers to control where their data is stored and processed, and
your content won't be replicated or moved outside of your chosen AWS Region except as
agreed by you. For customers in Aotearoa New Zealand, the options for storing data within
New Zealand include the Auckland AWS Local Zone, an AWS Outpost, or the upcoming AWS
Auckland region. Every commercial AWS region is designed, built, and operated in the
same way and incorporates the same levels of security. When choosing an AWS
infrastructure for your workload, take into account the possible trade-offs that may
exist. For example, an AWS Region has a larger selection of AWS services and higher
resiliency than an AWS Outpost. However, an AWS Outpost may provide more flexibility
as to the location where the infrastructure can be placed. There are also costs and budget
considerations to take into account. Some other considerations related to the location of
data include:

Do you need to make a distinction between where data is processed and where it is
stored? For example, the data could be stored in a database in New Zealand but
processed on an EC2 instance in another region (of your choice) as part of an analytics job.
Alternatively, it could be captured using a web application running on servers in
Sydney and then saved to a database located in New Zealand.
- Do you need to duplicate data across locations to meet your customer requirements?
For example, a data archiving solution could send backups to another AWS Region for
resiliency and security reasons. An application like a digital archive solution could
make use of Amazon CloudFront for content distribution to help reduce latency for end users
when accessing the content. This would require copies of data to be stored at CloudFront
edge locations, while the primary data is stored in the origin storage service such as
Amazon S3 or a database.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-2-how-do-you-design-workload-security-for-long-term-safety.html*

---

# MD_SEC 3: How can you identify and classify Māori data?

Organisations may wish to understand what Māori data they hold and have a method to
classify Māori data to protect it with security controls and practices. Once the data has been
classified and appropriate metadata is captured, you can govern and use that data in
appropriate ways.

- **MD_SEC03-BP01: Develop an understanding of what Māori data
is**. Create an easy-to-understand definition of Māori data for your
organisation. Having a definition of Māori data can help determine what additional
considerations are relevant to your organisation or application. Piloting this and testing
this with your customers facilitates a mutually-agreed upon definition, which is
implementable for your organisation.
- **MD_SEC03-BP02: Incorporate Māori data classification into your data
governance framework**. If you already have a data classification framework
within your organisation, you may wish to expand this to include a Māori data
classification approach. A classification framework can help you determine what is Māori
data, outline where and how the classification should be recorded, and define the security
and access controls that are required for that data classification. For example, what
additional data access controls may be required if the data is classified as tapu or noa?
- **MD_SEC03-BP03: Record Māori data classifications as metadata and
make it easily discoverable**. Use approaches such as metadata tagging and data
cataloguing to store and manage your classification metadata. Tools such as business data
catalogues should make it easier for your organisation to search for and discover datasets
that contain Māori data in your organisation. In addition, you can add tags which record
the purpose for which consent of that data was given. This may allow for easier review of
consent and data access policies and up-to-date consent practices.
- **MD_SEC03-BP04: Leverage technologies and techniques to help identify
and classify existing Māori data**. Your organisation may already capture and
store Māori data. Consider using available tools and techniques to review and classify
your existing data. Once identified and classified, update your metadata and business data
catalogues. This may involve assessing data across databases, object stores, file servers,
document management systems, communication systems (like email), and analytics platforms.
For example, search your AWS Glue Data Catalog table columns for terms like *iwi*
or *hapū* or Māori organisation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-3-how-can-you-identify-and-classify-māori-data.html*

---

# MD_SEC 4: How do you maintain privacy of personal Māori data?

It is important that personal data is collected and processed lawfully, fairly, and
transparently in relation to a person. When designing, building, and operating workloads that
may capture, store, and process Māori personal data, privacy should be taken into account
throughout the entire process. The application of privacy principles should align with your
organisation's privacy framework and be guided by applicable privacy regulation such as the
New Zealand Privacy Act 2020. For further information on how you are applying AWS services
in conjunction with the New Zealand Privacy Act 2020, see [Using AWS in the Context of the New Zealand Privacy Considerations](https://d1.awsstatic.com/whitepapers/compliance/Using_AWS_in_the_context_of_New_Zealand_Privacy_Considerations.pdf).

- **MD_SEC04-BP01: Use tools and techniques to adequately de-identify
data.** This helps protect individual's privacy when producing data sets that
may be shared or published. There are many techniques within data and analytics domains to
help de-identify data. These include obfuscation (obscuring sensitive data), tokenisation
(where a sensitive piece of data is replaced by a non-sensitive token where the token can
map back to the original data), and anonymisation (such as removing sensitive data
completely).
- **MD_SEC04-BP02: Honour the consent you've received when using data
for internal analytics**. If your organisation asked for consent when
collecting data, that data should be used only for the purposes that you have received
consent for. If your organisation asked for consent and did not receive it, exclude this
data from analytics and AI/ML uses.
- **MD_SEC04-BP03: Honour the consent you've received when sharing
data**. Only share data with third parties if you have obtained requisite
consent in accordance with applicable laws such as the New Zealand Privacy Act. Consider
creating mechanisms to exclude that data from any data sharing processes if you have not
obtained the required consents.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/md_sec-4-how-do-you-maintain-privacy-of-personal-māori-data.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
