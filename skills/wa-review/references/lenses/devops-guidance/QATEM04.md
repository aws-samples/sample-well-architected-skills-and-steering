**Saga**: Quality assurance
**Capability**: QA.TEM — Test environment management

---

# [QA.TEM.4] Implement a unified test data repository for enhanced test efficiency

**Category:** RECOMMENDED

Test data refers to specific input datasets designed for
testing purposes to simulate real-world scenarios.
Centralizing test datasets in a unified storage location, such
as a data lake or source code repository, ensures they are
stored, normalized, and managed effectively.

Test data might be stored differently depending on your specific use case. It can be
stored centrally for a single team who maintains multiple microservices or related
products, or centrally governed for multiple teams to source test data from. By
centralizing, teams can reuse the same test data across different test cases, minimizing
the time and effort spent preparing test data for usage.

Create a centralized, version-controlled system to store test
datasets, such as a data lake or source code
repository. Ensure the data in this central repository is
sanitized and approved for non-production environments. When
test environments are set up and test cases are run, use
delivery pipelines and automated tools to source test data
directly from this centralized source.

Outdated test datasets can result in ineffective tests and inaccurate results.
Regularly maintain the centralized test data source by updating it either periodically or
when there are changes in systems data schemas, features, functions, or dependencies.
Treat the test data as a shared resource with contracts in place to prevent disrupting
other teams or systems. Document any changes made to test data and notify any dependent
teams of these changes. Maintaining up-to-date test data allows for more effective issue
identification and resolution, leading to higher-quality software.

We recommend automating the update process where feasible using data pipelines, for
example, by pulling recent production data and obfuscating it as changes are made. Protect
sensitive data by implementing a data obfuscation plan that transforms sensitive
production data into similar, but non-sensitive, test data. Use obfuscation techniques,
such as masking, encrypting, or tokenizing, to sanitize the production data prior to it
being used in non-production environments. This approach helps uphold data privacy and
mitigates potential security risks during testing.

**Related information:**

- [AWS Well-Architected Sustainability Pillar: SUS04-BP06 Use
shared file systems or storage to access common data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a7.html)
- [AWS Well-Architected Sustainability Pillar: SUS04-BP07
Minimize data movement across networks](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a8.html)
- [AWS Well-Architected Cost Optimization Pillar: COST08-BP02
Select components to optimize data transfer cost](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized_components.html)
- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)
- [Identifying
and handling personally identifiable information
(PII)](https://docs.aws.amazon.com/databrew/latest/dg/personal-information-protection.html)
- [Data
Obfuscation](https://www.imperva.com/learn/data-security/data-obfuscation/)
- [Data
Masking using AWS DMS (AWS Data Migration Service)](https://aws.amazon.com/blogs/database/data-masking-using-aws-dms/)
- [Data
Lake Governance - AWS Lake Formation](https://aws.amazon.com/lake-formation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.tem.4-implement-a-unified-test-data-repository-for-enhanced-test-efficiency.html*
