# Performance efficiency

**Pillar**: Performance Efficiency  
**Pages**: 1

---

# Performance efficiency

The [Performance Efficiency
Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html) addresses best practices for managing production environments. This document
does not cover the design and management of non-production environments and processes, such as
continuous integration or delivery. The Well-Architected Performance Efficiency Pillar provides
an overview of design principles, best practices, and questions. If relevant, you can find
guidance on implementation in the [Performance Efficiency
Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html).

The Performance Efficiency Pillar focuses on the efficient use of computing resources to
meet requirements, and how to maintain efficiency as demand changes and technologies evolve.
Following these design principles can help you achieve and maintain efficient workloads in the
cloud.

Design principles

- **Democratise advanced technologies:** Make advanced technology
implementation easier for your team by delegating certain tasks like the undifferentiated
work to your cloud vendor. Rather than asking your IT team to learn about hosting and
running a new technology, consider consuming the technology as a service. For example, NoSQL
databases, media transcoding, and machine learning are all technologies that require
specialised expertise. Learn and develop these expertise with [AWS Skill Builder](https://skillbuilder.aws/). In the cloud, these
technologies become services that your team can consume, allowing your team to focus on
product development rather than resource provisioning and management.
- **Go global in minutes:** Deploying your workload in multiple
AWS Regions around the world allows you to provide lower latency and a better experience
for your customers at minimal cost.
- **Use serverless architectures:** Serverless architectures
remove the need for you to run and maintain physical servers for traditional compute
activities. For example, serverless storage services can act as static websites (removing
the need for web servers) and event services can host code. This removes the operational
burden of managing physical servers, and can lower transactional costs because managed
services operate at cloud scale.
- **Experiment more often:** With virtual and automatable
resources, you can quickly carry out comparative testing using different types of instances,
storage, or configurations.
- **Consider mechanical sympathy:** Use the technology approach
that aligns best with your goals. For example, consider data access patterns when you select
database or storage approaches.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/maori-data-lens/performance-efficiency.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
