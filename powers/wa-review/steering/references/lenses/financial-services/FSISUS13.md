**Pillar**: Sustainability

# FSISUS13: Can you complete workloads over more time while not violating your maximum SLA?

How do you avoid load spikes to reduce the provisioned capacity required for your
workload?

Flattening the workload demand curve can help you to reduce the provisioned capacity
for a workload and reduce its environmental impact. In other words, if you can afford to
spread out the load over a longer period of time, rather than having a higher peak in a
shorter span of time, then you lower the overall resource demand for the workload. By doing
so, you lower the overall amount of provisioned capacity, and thus lower overall energy
consumption to meet the workload's demand.

## FSISUS13-BP01 Do not complete a customer transaction in the shortest time when not required by end users

**Prescriptive guidance**

If your workload does not have time-sensitive requirements, consider running them
during times when public demand is lower. This distributes energy consumption to flatten
the resource demand curve. Evaluate your workload requirements to assess if you are able
to make this adjustment.

## FSISUS13-BP02 Introduce jitter to your scheduled tasks

### Prescriptive guidance

- Assess if your scheduled tasks can be distributed to run at random times during
an hour or throughout the day. This minimizes the highs of peak demand load and
spreads it across the day instead. Avoid using the same start minute of scheduled
tasks. Doing so creates high demand for resources at a specific time, which
introduces stress on energy consumption. Staggering job start times avoids load
spikes and creates time-flexible workloads.
- Evaluate whether highly intensive computational workloads such as financial
simulation can be spread over time and run fewer instances to maximize renewable
energy availability. If a grid computing workload is using a third-party scheduler,
prioritize workloads that need to provide calculations for regulators and trading
desks that need information prior to markets opening, so workloads that are not
urgent can be pushed off and worked on at a consistent rate to maximize renewable
energy availability. Additionally, verify that a proper fault tolerance framework is
implemented, as restarting a launch can increase launch time and energy consumption.
- Use [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) achieve your
goal.
- Balance generative AI model response time requirements with energy efficiency.
- Implement cost-aware prompting strategies that may take slightly longer but use
fewer resources.
- Use distributed generative AI inference when time permits to optimize resource
utilization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus13.html*
