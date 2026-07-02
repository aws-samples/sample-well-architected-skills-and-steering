**Pillar**: Sustainability

# FSISUS09: How do you optimize areas of your code that use the most resources?

Analyze and optimize your code's efficiency to improve resource utilization.

## FSISUS09-BP01 Monitor and optimize areas of code that are the most compute resource-intensive

### Prescriptive guidance

- Use [CodeGuru](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) and [Amazon Q Developer](https://aws.amazon.com/q/developer/) to optimize your code's efficiency.
- If possible, choose the most efficient OS and programming languages to run your
code.
- Remove unnecessary code such as modules that perform sorting or formatting.
- Optimize generative AI model inference code using efficient model
architectures.
- Implement model distillation to create smaller, task-specific generative AI
models.
- Use specialized instances like EC2 Inferentia for generative AI workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus09.html*
