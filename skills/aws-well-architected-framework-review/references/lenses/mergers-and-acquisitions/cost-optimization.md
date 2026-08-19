# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 3

---

# MACOST01 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 6

---

## MACOST01-BP01 Perform pricing model analysis for the combined entities

Analyze each component of the workload. Determine if the component and resources should be running for extended periods (for commitment discounts) or dynamic and short-running (for Spot or On-Demand Instances). Perform an analysis on the workload using the recommendations feature in AWS Cost Explorer.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-1.html*

---

## MACOST01-BP02 Optimize accounts through various means, such as EC2 instance types, Savings Plans, and Amazon S3 lifecycle

Use AWS Trusted Advisor to examine current cost savings and possible additional savings.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-1.html*

---

## MACOST01-BP03 Discover and realize additional cost savings

Explore means for additional cost savings, and use AWS Cost Explorer to evaluate costs. Choose an optimized savings plan for the combined entity, and work with AWS teams to use Reserve Instances or Savings Plans across companies if possible.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-1.html*

---

## MACOST01-BP04 Migrate to Regions based on cost

Resource pricing can be different in each Region. Factoring in Region cost verifies that you are paying the lowest overall price for a workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-1.html*

---

## MACOST01-BP05 Use managed services for lower TCO

Understand how proper use of managed services can lower TCO.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-1.html*

---

## MACOST01-BP06 Select third-party agreements with cost efficient terms

Cost-efficient agreements and terms scale the cost of these services with the benefits they provide. Select agreements and pricing that scale when they provide additional benefits to your organization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-1.html*

---

# MACOST02 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

## MACOST02-BP01 Configure billing and cost management tools across both organizations

Configure AWS Cost Explorer and AWS Budgets in line with your organization policies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-2.html*

---

## MACOST02-BP02 Combine both organizations information to cost and usage

To roll your new AMS-managed AWS account bill into a payment for an existing AWS Organizations management account, set up consolidated billing, and link the accounts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-2.html*

---

## MACOST02-BP03 Allocate costs based on workload metrics

Organize the workload's costs by metrics or business outcomes to measure workload cost efficiency. Implement a process to analyze the AWS Cost and Usage Report with Amazon Athena, which can provide insight and chargeback capability.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-2.html*

---

## MACOST02-BP04 Configure a bill or chargeback strategy using custom usage tags

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-2.html*

---

# MACOST03 — Cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 5

---

## MACOST03-BP01 Perform data transfer modeling

Gather organization requirements, and perform data transfer modeling of the workload and each of its components. This identifies the lowest cost point for its current data transfer requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html*

---

## MACOST03-BP02 Select components to optimize data transfer cost

All components are selected, and architecture is designed to reduce data transfer costs. This includes using components such as wide-area-network (WAN) optimization and multi-Availability Zone (AZ) configurations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html*

---

## MACOST03-BP03 Implement services to reduce data transfer costs

Implement services to reduce data transfer. For example, using a content delivery network (CDN) such as Amazon CloudFront to deliver content to users, caching layers using Amazon ElastiCache, or using AWS Direct Connect instead of VPN for connectivity to AWS.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html*

---

## MACOST03-BP04 Delete redundant data stores using policies

Manage the lifecycle of all your data, and automatically enforce deletion timelines to minimize the total storage requirements of your workload.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html*

---

## MACOST03-BP05 Analyze data integration pattern of the combined organizations

Data is a combined organizational asset. Collect, store, organize, and process valuable data, and make it available in a secure way to the people and applications that need it.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/macost-3.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
