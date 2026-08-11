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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
