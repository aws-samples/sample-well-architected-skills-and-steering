**Saga**: Development lifecycle
**Capability**: DL.LD — Local development

---

# [DL.LD.8] Generate mock datasets for local development

**Category:** OPTIONAL

Mock datasets are synthetic or modified datasets that
developers can use during the development process, eliminating
the need to interact with real, sensitive production
data. Using mock datasets ensures tests are thorough and
realistic, without compromising security.

Use data generating tools to create mock datasets. These tools
can range from random data generators to more advanced methods
like generative AI. Generative AI can be used to generate
synthetic datasets that can be used to test applications and
is especially useful for generating data that is not often
included in testing datasets, such as defects or edge cases.

If using real-world data is necessary for local development, ensure it is obfuscated.
Methods such as masking, encrypting, or tokenizing production datasets can transform real
datasets into mock datasets that are safe for local development. It might be useful to
store already prepared mock datasets that can be shared between teams or systems to
perform testing with. This approach creates a realistic local testing environment without
risking developers handling actual production data.

**Related information:**

- [Testing
software and systems at Amazon: Developer
environment](https://youtu.be/o1sc3cK9bMU?t=1017)
- [Generate
test data using an AWS Glue job and Python](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/generate-test-data-using-an-aws-glue-job-and-python.html)
- [Foundation
Model API Service - Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [What
is Generative AI?](https://aws.amazon.com/what-is/generative-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ld.8-generate-mock-datasets-for-local-development.html*
