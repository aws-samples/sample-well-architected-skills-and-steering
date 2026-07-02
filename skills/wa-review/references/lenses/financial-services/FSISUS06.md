**Pillar**: Sustainability

# FSISUS06: How do you monitor and minimize resource usage for financial services workloads?

Monitor and analyze your financial services' usage patterns to minimize resource usage.
Identify services that are not required to be operational at all times or that can be scaled
up and down based on user access patterns.

## FSISUS06-BP01 Actively monitor your FSI resource usage

- Monitor and analyze your financial services' usage patterns to minimize resource
usage.
- Identify services that are not required to always be operational, or that can be
scaled up and down based on user access patterns.
- For example, many consumer-based services can be scaled down or turned off during
off-peak hours.

### Prescriptive guidance

- Remove underutilized software modules and combine these functions into other
software services.
- Minimize the average resource demand required per unit-of-work using automatic
scaling services, serverless transaction processing, or shutting down your resources
when usage patterns permit.
- Use queue-driven architectures, pipeline management, and On-Demand Instance
workers to maximize your utilization for batch processing.
- Implement comprehensive monitoring of generative AI resource consumption using
Amazon CloudWatch.
- Track token lengths of prompts and model responses to measure generative AI
utilization.
- Identify idle time periods to scale down or suspend generative AI inference
endpoints.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus06.html*
