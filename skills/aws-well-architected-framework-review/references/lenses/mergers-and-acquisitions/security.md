# Security

**Pillar**: Security  
**Questions**: 5

---

# MASEC01 — Security

**Pillar**: Security  
**Best Practices**: 5

---

## MASEC01-BP01 Use a centralized identity provider

At any given time, you can have only one directory or one SAML 2.0 identity provider connected to IAM Identity Center. But, you can change the identity source that is connected to a different one.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP02 Use a common authorization approach

Companies may have a very different approach to authorization. Companies need to use a common authorization platform and develop consistent authorization policies for the combined systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP03 Use AWS temporary credentials

You can use the AWS Security Token Service to create and provide trusted users with temporary security credentials that can control access to your AWS resources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP04 Store and use secrets securely

Use AWS Secrets Manager to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. The secret can't be compromised by someone examining your code because the secret no longer exists in the code.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP05 Create a common policy for auditing and rotating credentials

Rotation is the process of periodically updating a secret. When you rotate a secret, you update the credentials in both the secret and the database or service. In Secrets Manager, you can set up automatic rotation for your secrets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

# MASEC02 — Security

**Pillar**: Security  
**Best Practices**: 5

---

## MASEC02-BP01 Use an AWS-defined process to report vulnerabilities

AWS takes security very seriously and investigates all reported vulnerabilities (for more detail, see [AWS Cloud Security](https://aws.amazon.com/security/)).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-2.html*

---

## MASEC02-BP02 Use AWS services with self-service within the existing management console

On AWS, you can automate manual security tasks so you can shift your focus to scaling and innovating your business.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-2.html*

---

## MASEC02-BP03 Use third-party security tools when necessary due to integration with on-premises resources

Amazon Security Lake is a fully-managed security data lake service. You can use Security Lake to automatically centralize security data from AWS and third-party sources into a data lake that's stored in your AWS account. Security Lake helps you analyze security data, so you can get a more complete understanding of your security posture across the entire organization. You can also use Security Lake to improve the protection of your workloads, applications, and data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-2.html*

---

## MASEC02-BP04 Migrate to a common set of tools, including partner tools from marketplace

The AWS Shared Responsibility Model (SRM) makes it easy to understand various choices for protecting unique AWS environment, and [access partner resources](https://aws.amazon.com/partners/featured/security/) that can help you implement end-to-end security quickly and easily.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-2.html*

---

## MASEC02-BP05 Create a common policy for auditing and rotating credentials

For human identities, you should require users to change their passwords periodically and retire access keys in favor of temporary credentials. For machine identities, rely on temporary credentials using IAM roles. For situations where this is not possible, frequent auditing and rotating access keys is necessary.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-2.html*

---

# MASEC03 — Security

**Pillar**: Security  
**Best Practices**: 5

---

## MASEC03-BP01 Standardize root email address (root account email access)

When you first create an AWS account, you begin with a single sign-in identity that has complete access to all AWS services and resources in the account. This identity is called the AWS account root user and is accessed by signing in with the email address and password that you used to create the account. Ensure uninterrupted access to root email after a merger or acquisition.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-3.html*

---

## MASEC03-BP02 Define data access control mechanisms for combined systems

Both organizations need a common set of privacy controls and access to data. AWS is built with comprehensive data protection in the cloud.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-3.html*

---

## MASEC03-BP03 Create a consistent mechanism for data classification and protection (in-transit and at rest)

Before creating any workload, foundational practices that influence security should be in place. For example, data classification provides a way to categorize data based on levels of sensitivity, and encryption protects data by rendering it unintelligible to unauthorized access. These methods are important because they support objectives such as preventing mishandling or complying with regulatory obligations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-3.html*

---

## MASEC03-BP04 Automate data backup process for combined systems

A comprehensive backup strategy is an essential part of an organization’s data protection plan to withstand, recover from, and reduce any impact that might be sustained because of a security event. Create an extensive backup strategy that defines which data must be backed up, how often data must be backed up, and how backup and recovery tasks are monitored.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-3.html*

---

## MASEC03-BP05 Automate responses to data security events

AWS encourages you to use automation to help quickly detect and respond to security events within your AWS environments. In addition to increasing the speed of detection and response, automation also helps you scale your security operations as you expand your workloads running on AWS. Do you have automation process defined on both organizations?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-3.html*

---

# MASEC04 — Security

**Pillar**: Security  
**Best Practices**: 4

---

## MASEC04-BP01 The seller is using AWS services (marketplace) for data governance

Data governance is a framework to build data quality checks, identify lineage (relation) between target and source datasets, and build a data catalog over existing data in data lakes and enterprise data warehouses.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-4.html*

---

## MASEC04-BP02 Document consistent mechanisms for data classification

Ensure organizations are using AWS-supported partner solutions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-4.html*

---

## MASEC04-BP03 Document processes to maintain data integrity within AWS services

Regulatory requirements to maintain the integrity of data are typically implemented as part of a validated application. However, by implementing controls at the AWS service-level, you can facilitate data integrity even for actions performed outside the validated application.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-4.html*

---

## MASEC04-BP04 Understand both the buyer's and seller's compliance needs

AWS supports inheritance of many security standards and compliance certifications, including PCI-DSS, HIPAA/HITECH, FedRAMP, GDPR, FIPS 140-2, and NIST 800-171, which helps you satisfy necessary compliance requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-4.html*

---

# MASEC05 — Security

**Pillar**: Security  
**Best Practices**: 5

---

## MASEC05-BP01 Both organizations have documented network architecture

Network documentation includes written charts, drawings, records, and instructions of networking procedures, layouts, and information on your installed production or development network.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-5.html*

---

## MASEC05-BP02 Define a strategy for overlapping Classless Inter-Domain Routing (CIDR)

In order to plan your prefix summarization and create your routing design, you should understand the IP addressing scheme of the merging or divesting companies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-5.html*

---

## MASEC05-BP03 Define a connectivity model for post-integration or divestiture

The network connectivity layer holds an enterprise’s entire IT ecosystem together. Furthermore, creating the right connectivity model is a critical step toward planning your merger, acquisition, or divestiture.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-5.html*

---

## MASEC05-BP04 Define a strategy for inter-enterprise DNS resolution

DNS is the typical way how users connect to applications and also how various components of an application may communicate with each other.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-5.html*

---

## MASEC05-BP05 Define a security strategy for data flowing between the two enterprises

It is important to establish a secure communication between two enterprises for data transfer.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-5.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
