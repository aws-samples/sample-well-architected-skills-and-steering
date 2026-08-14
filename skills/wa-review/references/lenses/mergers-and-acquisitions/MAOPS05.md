# MAOPS05 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 5

---

## MAOPS05-BP01 Configure AWS resource tags

AWS resources can be tagged for a variety of purposes, from implementing a cost
allocation strategy to supporting automation or authorizing access to AWS resources.
Implementing a tagging strategy can be challenging for some organizations, owing to the
number of stakeholder groups involved and considerations such as data sourcing and tag
governance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP02 Group applications based on tags

A tag is a label that you assign to an AWS resource. A tag consists of a key and a
value, both of which you define. For example, if you have two EC2 instances, you might
assign both a tag key of `Stack`. But the value of `Stack` might be
`Testing` for one and `Production` for the other.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP03 Associate tags with each configured resource (during provisioning)

AWS CloudFormation provides a common language for provisioning all the infrastructure resources
in your AWS environment. For AWS resources using CloudFormation templates, you can use the CloudFormation
Resource Tags property to apply tags to supported resource types upon creation. Managing the
tags as well as the resources with IaC helps create consistency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP04 Set up security based on tags

Organizations have varying needs and obligations to meet regarding the appropriate
handling of data storage and processing. Data classification is an important precursor for
several use cases, such as access control, data retention, data analysis, and compliance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

## MAOPS05-BP05 Perform cost allocation based on tags

The AWS-generated tag created by is a tag that AWS defines and applies to supported
AWS resources for cost allocation purposes. User-defined tags are tags that you define,
create, and apply to resources. After you have created and applied the user-defined tags,
you can activate by using the AWS Cost Management Console for cost allocation tracking.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/maops-5.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
