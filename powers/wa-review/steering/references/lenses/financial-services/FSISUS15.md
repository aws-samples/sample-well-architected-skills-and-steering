**Pillar**: Sustainability

# FSISUS15: What is your testing process for workloads that require floating point precision?

## FSISUS15-BP01 Minimize the bit count while maintaining precision

### Prescriptive guidance

Floating point precision is a way to represent real numbers in a finite binary
format. It stores a number in a fixed-width field with the intent to reduce the memory
bandwidth and storage requirements compared to double-precision arithmetic results.
Although double-precision can sometimes lead to more accurate results, single-precision
calculations can be faster and thus

reduce overall energy consumption for particular workloads. Determine which of your
workloads is suitable for use of floating-point accuracy, performance, and efficiency.
Consider testing with a cluster of instances to see how well it performs at scale.

### Implementation guidance:

- For intensive financial simulations and calculations, test the number of bits
that are required to achieve your floating point precision and consider reducing
number of bits by selecting different floating-point formats, including bfloat16,
that's supported by AWS Graviton.
- Using floating point [Quantization](https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/), you can represent numbers using lower bit-count integers or
floating point numbers without incurring a significant loss in accuracy.
Specifically, you can reduce resource usage by replacing the parameters in your
workload with (1) half-precision (16 bit), (2) bfloat16 (16 bit, but the same
dynamic range as 32 bit), or 8-bit integers instead of the usual single-precision
floating-point (32 bit) values.
- **Service recommendations:** Use the following services
to achieve your goal.

[AWS Batch](https://aws.amazon.com/batch/)
- [AWS Parallel
Cluster](https://aws.amazon.com/hpc/parallelcluster/)
- [Graviton3](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-ec2-c7g-instances-powered-aws-graviton3-processors/)

- Test generative AI models with reduced precision (quantization) to maintain
accuracy while reducing resource consumption.
- Validate generative AI model performance with different floating-point
precisions.
- Use mixed-precision training for generative AI models to optimize resource
usage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus15.html*
