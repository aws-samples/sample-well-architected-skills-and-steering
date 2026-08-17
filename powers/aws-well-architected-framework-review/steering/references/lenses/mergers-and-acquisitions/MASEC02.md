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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
