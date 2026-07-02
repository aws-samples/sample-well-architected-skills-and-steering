# LSOPS13 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS13-BP01 Store data in an AI/ML-ready formats

Expectations of what can be done with data are rapidly expanding.
Life sciences projects produce rich data. Work to maximize data
storage to allow for new technologies such as AI/ML.

**Desired outcome:** Be able to pivot
and adapt as there are new technological demands on existing systems
and data.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Use data processing that stores data in adaptable, open standard
formats. This will allow for the greatest flexibility as
technologies progress.

### Implementation steps

- Store data in document formats ingestible by Amazon
Sagemaker and Amazon Bedrock.
- Use AWS Glue to transform data into Iceberg and place in an
Amazon S3 data lake.

## Resources

**Related documents:**

- [Accelerating
Life Sciences Innovation with Agentic AI on AWS](https://aws.amazon.com/blogs/industries/accelerating-life-sciences-innovation-with-agentic-ai-on-aws/)
- [What
is Apache Iceberg?](https://aws.amazon.com/what-is/apache-iceberg/)
- [Building
an End-to-End Data Strategy for Analytics and Generative AI:
Insights from AWS and Workhuman](https://aws.amazon.com/awstv/watch/f4743296958/)

**Related examples:**

- [Use
generative AI on AWS for efficient clinical document
analysis](https://aws.amazon.com/blogs/architecture/use-generative-ai-on-aws-for-efficient-clinical-document-analysis/)
- [Revolutionizing
clinical trials with the power of voice and AI](https://aws.amazon.com/blogs/machine-learning/revolutionizing-clinical-trials-with-the-power-of-voice-and-ai/)

**Related tools:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops13-bp01.html*

---
