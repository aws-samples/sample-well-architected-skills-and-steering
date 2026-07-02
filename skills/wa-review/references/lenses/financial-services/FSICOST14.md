**Pillar**: Cost Optimization

# FSICOST14: How do you measure the cost of licensing third-party applications and software?

If you are using third-party software, understand the specific licensing terms of each
third-party vendor.

## FSICOST14-BP01 Consider the cost of licensing third-party applications and software

If you are using third-party software, understand the specific licensing terms of
each third- party vendor. AWS offers both Dedicated Hosts that have pre-installed
virtualization software (Hypervisor) whereas bare metal servers do not have pre-installed
virtualization software.

Choosing the right instance type specific to the licensing terms may reduce your
third-party licensing costs.

Generally, third-party software applications and associated support can provide your
workload with a lower overall cost of ownership than in-house created applications.
Because software vendors have a much broader perspective of customer requirements, their
software can more economically support a wider range of use cases than an in-house
developed solution. A software support agreement reduces your technical debt when new
workload features are needed.

**Licensing**

Evaluate model and API-based generative AI licensing with the same rigor as
traditional third-party software. Assess cost per token, per model family, and concurrency
tier against your workload profiles and expected query volumes. Prefer consumption-based
or hybrid contracts with transparent scaling guardrails and the ability to downshift to
smaller models when latency or accuracy trade-offs are acceptable.

Track licensing renewals and vendor rate changes (for example, third-party LLM
providers or external model APIs) through your Cloud Financial Management tooling to avoid
unplanned cost escalations. For regulated environments, ensure data residency and usage
terms align with your compliance obligations before committing to external generative AI
model providers.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost14.html*
