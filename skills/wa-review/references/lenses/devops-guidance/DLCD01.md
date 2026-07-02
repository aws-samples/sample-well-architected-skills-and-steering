**Saga**: Development lifecycle
**Capability**: DL.CD — Continuous delivery

---

# [DL.CD.1] Deploy changes to production frequently

**Category:** FOUNDATIONAL

Frequent deployments to production encourages small, rapid, and iterative changes to
the code base. Deploying small and validated changes regularly helps mitigate the risk
associated with each deployment. Frequent deployments not only streamlines the testing and
validation process, but also expedites the feedback loop, leading to quicker resolution of
issues.

Use a pipeline to automate the deployment of validated changes across various
environments, including production. This pipeline should be automatically triggered, such as
by the completion of continuous integration or an updated artifact in an artifact
repository. Once invoked, the pipeline should automatically begin to deploy changes to
non-production environments for further testing and validation. Upon successful validation,
changes can be deployed to the production environment.

When working in a DevOps environment, it is important to distinguish between
*deploying* and *releasing*. Even after deploying
changes to production, these changes might not necessarily be visible or accessible to all
users. By using advanced deployment strategies and employing [feature flags](https://aws.amazon.com/systems-manager/features/appconfig/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&blog-posts-cards.sort-by=item.additionalFields.createdDate&blog-posts-cards.sort-order=desc#Feature_flags), teams can deploy code to production and decide when to release or
rollback specific features in real time, offering more granular control over releasing new
features to end users.

Teams should focus on deploying small changes rather than
bundling multiple changes into a single, large batch
deployment. Accumulating changes complicates testing and
validation, and it becomes challenging to ensure that all
components interact correctly. The practice of deploying small
changes demands discipline and commitment, but it improves
deployment frequency, security, and enhanced collaboration
while ensuring that the code base remains up-to-date and
releasable at all times.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.1-deploy-changes-to-production-frequently.html*
