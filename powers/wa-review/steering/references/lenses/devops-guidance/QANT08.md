**Saga**: Quality assurance
**Capability**: QA.NT — Non-functional testing

---

# [QA.NT.8] Practice eco-conscious development with sustainability testing

**Category:** OPTIONAL

Sustainability testing ensures that software products contribute to eco-conscious and
energy-efficient practices that reflect a growing demand for environmentally responsible
development. It is a commitment to ensuring software development not only meets
performance expectations but also contributes positively to the organization's
environmental goals. In specific use cases, such as internet of things (IoT) and smart
devices, software optimizations can directly translate to energy and cost savings while
also improving performance.

Sustainability testing encompasses:

- **Energy efficiency**: Create sustainability tests which
ensure software and infrastructure minimize power consumption. For instance, [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/) are designed
for enhanced energy efficiency. They offer up to 60% less energy consumption for
similar performance compared to other EC2 instances. Write static analysis tests that
focus on improving sustainability by verifying that infrastructure as code (IaC)
templates are configured to use energy efficient infrastructure.
- **Resource optimization:** Sustainable software leverages
hardware resources, such as memory and CPU, without waste. Sustainability tests can
enforce right-sizing when deploying infrastructure. For example, [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) ensures compute resources
align with actual needs, preventing over-provisioning. Similarly, [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) offers actionable insights into resource provisioning based
on actual consumption patterns.
- **Data efficiency:** Sustainability testing can assess
the efficiency of data storage, transfer, and processing operations, ensuring minimal
energy consumption. Tools like the [AWS Customer Carbon
Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) offer insights into the carbon emissions associated with
various AWS services, such as Amazon EC2 and Amazon S3. Teams can use these insights to make
informed optimizations.
- **Lifecycle analysis:** The scope of testing extends
beyond immediate software performance. For instance, the [AWS Customer Carbon
Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) can provide insights into how using AWS services impacts
carbon emissions. This information can be used to compare this usage with traditional
data centers. Metrics from this tool can be used to inform decisions throughout the
software lifecycle, ensuring that environmental impact remains minimal from inception
to decommissioning of resources.

Sustainability testing should use data provided by profiling
applications to measure their energy consumption, CPU usage,
memory footprint, and data transfer volume. Tools such
as [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
and [SusScanner](https://github.com/awslabs/sustainability-scanner)
can be helpful when performing analysis and promotes writing
efficient, clean, and optimized code. Combining this data with
suggestions from AWS Trusted Advisor and AWS Customer Carbon
Footprint Tool can lead to writing tests which can enforce
sustainable development practices.

Sustainability testing is still an emerging quality assurance
practice. This indicator is beneficial for organizations
focusing on environmental impact. We think that by making
sustainability a core part of the software development
process, not only do we contribute to a healthier planet, but
often, we also end up with more efficient and cost-effective
solutions.

**Related information:**

- [AWS Well-Architected Performance Pillar: PERF02-BP04 Determine
the required configuration by right-sizing](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_select_compute_right_sizing.html)
- [AWS Well-Architected Performance Pillar: PERF02-BP06
Continually evaluate compute needs based on metrics](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_select_compute_use_metrics.html)
- [AWS Well-Architected Sustainability Pillar: SUS03-BP03
Optimize areas of code that consume the most time or resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)
- [AWS Well-Architected Sustainability Pillar: SUS06-BP01 Adopt
methods that can rapidly introduce sustainability improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a2.html)
- [AWS Well-Architected Cost Optimization Pillar: COST09-BP03
Supply resources dynamically](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html)
- [Sustainability
Scanner (SusScanner)](https://github.com/awslabs/sustainability-scanner)
- [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html)
- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [Sustainable
Cloud Computing](https://aws.amazon.com/sustainability/)
- [Reducing
carbon by moving to AWS](https://www.aboutamazon.com/news/sustainability/reducing-carbon-by-moving-to-aws)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.8-practice-eco-conscious-development-with-sustainability-testing.html*
