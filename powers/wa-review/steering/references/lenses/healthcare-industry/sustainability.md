# Sustainability

**Pages**: 7

---

# Region selection

HCL_SUS1. How do you identify targets
for sustainability improvement?

**Prioritize targets for
improvement by reviewing your workloads against the
[sustainability
principles](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/best-practices-for-sustainability-in-the-cloud.html)**

Migrating workloads from on-premises data centers to the cloud
can reduce the workload’s carbon footprint by 88%. Regular
review of cloud architecture for optimization opportunities can
reduce carbon footprints as well.  Both mean that healthcare
workload migrations can deliver the benefits of the cloud and
simultaneously improve sustainability.  The
[Sustainability
pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html) contains a
number of
[best
practices for sustainability in the cloud](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/best-practices-for-sustainability-in-the-cloud.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/region-selection.html*

---

# User behavior patterns

HCL_SUS2. How do you match workload
infrastructure to user behavior patterns?

**Scale infrastructure to
continually match user demand and performance
requirements**

Many healthcare workloads are life-critical, and have steady
demand 24 x 7. However, other workloads (such as those
supporting ambulatory care delivery or revenue cycle workflows)
exhibit cyclical utilization patterns with peak demand during
business hours.
[Minimize
the amount of hardware used](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-the-minimum-amount-of-hardware-to-meet-your-needs.html) by scaling workloads down
during periods of low demand.

Legacy solutions may use statically provisioned
infrastructure, with redundancy for high availability. Consider
cloud-native ways to meet business requirements with an elastic,
efficient architecture and disaster recovery strategy (like a
pilot light architecture rather than active-active).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/user-behavior-patterns.html*

---

# Software and architecture patterns

HCL_SUS3. Does your organization
monitor workload activity and remove or refactor components
that are no longer necessary?

**Analyze demand on workloads
to identify components that can be removed or refactored. Then,
engage component owners and stakeholders to redesign clinical
workflows, and decrease workload infrastructure**

Some healthcare delivery systems and large independent software
vendors (ISV) have sprawling IT footprints with numerous siloed
systems. Identifying and
[removing
or refactoring components](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/remove-or-refactor-workload-components-with-low-or-no-use.html) with little or no use can
simplify workflows, decrease cost, and improve sustainability.
Cloud archives can minimize the cost of retaining data from
retired components.

HCL_SUS4. How do you optimize the
impact of and applications and the equipment that run
them?

**Evaluate the overall impact
of applications, devices, and equipment**

As documented in the
[Sustainability
pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html), it is
recommended to
[optimize
impact on customer devices and equipment](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/optimize-impact-on-customer-devices-and-equipment.html).  For example,
as new features are released for a healthcare application, build
those features as backward compatible, minimizing the need for
new hardware.  Additionally, evaluate the potential impact of
new or upgraded hardware requirements to minimize the overall
impact when architecting new workloads or features.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/software-and-architecture-patterns.html*

---

# Measure results

HCL_SUS5. How does your organization
measure the effectiveness of sustainability
efforts?

**Quantify and report results
to drive continuous improvement processes**

The healthcare vertical extensively uses metrics and measures to
quantify care quality, effectiveness, and patient experience.
Adding metrics to quantify sustainability improvement can better
align business interests with sustainability goals. Further,
analysis of such reporting can help identify repeatable
processes for achieving sustainability improvements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/measure-results.html*

---

# Data patterns

HCL_SUS6. How does your organization
remove unneeded or redundant health data?

**Automate data retention
processes that retain the minimum amount of health data required
to meet regulatory and business requirements**

Regulatory requirements may impose data retention periods on
healthcare providers and ISVs.  However, it is common for health
data to be retained in perpetuity, well beyond its useful life.
Begin by reviewing and classifying data in line with your
business and regulatory requirements, such as how long health
data records must be retained.  Review data assets with
consideration of regulatory compliance, care delivery needs, and
secondary use goals.  Optimize storage costs and environmental
impact by taking advantage of storage classes within cloud
services and aligning with access patters. Remove
[unneeded
or redundant data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/remove-unneeded-or-redundant-data.html).  Use automated lifecycle policies
wherever possible to automate the deletion or archival of
unnecessary data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/data-patterns.html*

---

# Key AWS services

There are a number of key AWS features that support sustainability in the cloud.
The following services and features are an important part of the sustainability journey:

**Workload management:**

- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/)
- [AWS Customer
Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Data Exchange](https://aws.amazon.com/data-exchange/sustainability/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/key-aws-services-5.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to sustainability.

**Documentation and blogs**

- [Introduction
of the Sustainability Pillar for the AWS Well-Architected
Framework](https://aws.amazon.com/blogs/aws/sustainability-pillar-well-architected-framework/)
- [Reducing carbon by moving to
AWS](https://www.aboutamazon.com/news/sustainability/reducing-carbon-by-moving-to-aws)
- [AWS and sustainability in the cloud](https://sustainability.aboutamazon.com/environment/the-cloud?energyType=true)
- [AWS enables sustainability solutions](https://aws.amazon.com/sustainability/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/resources-5.html*

---
