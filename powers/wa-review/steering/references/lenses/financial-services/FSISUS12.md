**Pillar**: Sustainability

# FSISUS12: What is your process for benchmarking instances for existing workloads?

Maximizing your instance utilization is an effective and quantifiable practice that
helps you meet your sustainability goals. But reaching an ideal utilization state is a
process — it's uncommon for customers to achieve optimal instance utilization on their first
attempt. Define a process to monitor resource utilization over time so you can benchmark
performance and make the necessary adjustments to your workloads.

## FSISUS12-BP01 Set appropriate instance usage goals that reflect your sustainability requirements

**Prescriptive guidance**

- Instance utilization goals differ for every company, but you can use common
metrics that are broadly applied regardless of company size, age, industry, or domain
like carbon emissions and energy consumption.
- You can use these metrics to set goals like an ideal utilization percentage, or a
maximum idle instance threshold.
- It's important to set measurable instance utilization goals that apply within the
context of your business to see and iterate over time.
- Setting appropriate goals provides guidance and justification for every decision
that your organization makes as it collectively works toward a sustainable usage
state.

## FSISUS12-BP02 Track your overall process in achieving your goals

**Prescriptive guidance**

- It's harder to achieve goals if you are not aware of your progress and if you
don't know where you are, you're unable to pivot to make the right changes in reaching
your goal.
- Do this by setting a regular cadence with the appropriate stakeholders to
identify the current state and creating action plans to iterate, if necessary.
- AWS provides tools to help your track your overall progress such as the [AWS
Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) to report on emissions from your AWS usage,
and specifically Amazon EC2, which follows Greenhouse Gas (GHG) Protocol standards.
- You can analyze the changes in your emissions over time and forecast how your
emissions change across your sustainability journey.

## FSISUS12-BP03 Monitor your individual instance performance metrics

### Prescriptive guidance

- Establish a process to monitor individual instances to help you to use two
major optimization approaches:

Using only what you need
- Right-sizing what you do need

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides a unified view
of metrics that you can use to benchmark instance performance. Use both the default
and custom metrics to gather the data you need to make informed decisions.
- For example, you can use the IsIdle default metric for Amazon EMR to identify
clusters for termination. This process helps your organization adopt more optimal
instances types since newer generation instances typically have better
energy-to-performance ratios.
- Run performance tests specific to the processor to better understand your
workloads' needs to help lower your workload's instance count by evaluating whether
workloads are properly fitted to an instance family by performance metrics other
than CPU and reduce unnecessary instances.
- Establish a process to also track supply to demand with [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/). This helps keep your scaling policies
dynamic and relevant to changes to your workload.
- **Implementation guidance:** Hpc 7g instance may be the
obvious contender for a grid computing workload, but network constraints could cause
the need for more instances. Consider switching to C7gn. Do not go after cores, as
memory bandwidth, faster I/O, and higher clock speeds may be more beneficial for
highly intensive financial simulations. For example, on AWS Graviton, since each
vCPU is its own physical core, verify that workloads are running instances beyond
60% CPU to breakage to best assess threshold and limit over provisioning instances.
- **Service recommendations:** Use the following services
to achieve these goals:

[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [Amazon CloudWatch
metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [AWS Graviton Performance Runbook](https://github.com/aws/aws-graviton-getting-started/blob/main/perfrunbook/graviton_perfrunbook.md)

### Generative AI considerations

- Use SageMaker AI AI Inference Recommender to benchmark optimal instance types for
generative AI models.
- Benchmark AWS Trainium instances for energy-efficient generative AI model
training.
- Evaluate EC2 Inferentia instances for sustainable generative AI inference.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus12.html*
