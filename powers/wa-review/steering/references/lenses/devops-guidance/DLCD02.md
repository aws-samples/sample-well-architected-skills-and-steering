**Saga**: Development lifecycle
**Capability**: DL.CD — Continuous delivery

---

# [DL.CD.2] Deploy exclusively from trusted artifact repositories

**Category:** FOUNDATIONAL

All artifacts involved in the delivery process should
originate from a trusted artifact repository. These
repositories contain validated, tested, and integrated
artifacts that have been deemed safe for deployment. By using
trusted artifact repositories, teams can ensure the security
of deployed workloads, maintain quality and security
standards, and promote trust in the delivery pipeline.

The delivery pipeline should be restricted to using only
trusted artifact repositories, which could be enforced through
mechanisms such as allow lists, IP restrictions, or
authentication controls. Additionally, we recommend using
cryptographic signing to validate artifacts and including a
validation stage in the pipeline to verify that the artifacts
meet the necessary standards before deployment. In this way,
the integrity and security of the deployed workloads are
maintained consistently.

**Related information:**

- [Artifact
Repository - AWS CodeArtifact](https://aws.amazon.com/codeartifact/)
- [Fully
Managed Container Registry - Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)
- [Code
Repositories and Artifact Management | AWS Marketplace](https://aws.amazon.com/marketplace/solutions/devops/code-repositories-and-artifact-management?aws-marketplace-cards.sort-by=item.additionalFields.headline&aws-marketplace-cards.sort-order=asc&awsf.aws-marketplace-devops-store-use-cases=*all)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.2-deploy-exclusively-from-trusted-artifact-repositories.html*
