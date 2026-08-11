# MAOPS03 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS03-BP01 Structure your organization following AWS best practices

A well-architected multi-account strategy helps you innovate faster in AWS, while
helping you meet your security and scalability needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP02 Merge the management accounts of both organizations

Consolidated billing is a feature of AWS Organizations. You can use the management account of
your organization to consolidate and pay for all member accounts. In consolidated billing,
management accounts can also access the billing information, account information, and
account activity of member accounts in their organization. This information may be used for
services such as AWS Cost Explorer, which can help management accounts improve their organization’s
cost performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP03 Determine if it's appropriate to separate management accounts

If there is a use case to keep OUs separate, you can certainly do that with multiple
management accounts. There may be few reasons to keep Organizations separate:

- AWS GovCloud (US) or commercial cloud
- Differing financial needs, including taxation (Europe compared to the US)
- Differing operating scope (Systems Manager)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP04 Merge logging, security, and infrastructure organizations

The approach covered in this pattern is suitable for customers who have multiple
AWS accounts with AWS Organizations and are now encountering challenges when using AWS Control Tower, a
landing zone, or account vending machine services to set up baseline guardrails in their
accounts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

## MAOPS03-BP05 Define a backup strategy for each organization

Use AWS Backup to create backup plans that define how to back up your AWS resources.
The rules in the plan include a variety of settings, such as backup frequency, the time
window during which the backup occurs, the AWS Region containing the resources to back up,
and the vault in which to store the backup.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-3.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
