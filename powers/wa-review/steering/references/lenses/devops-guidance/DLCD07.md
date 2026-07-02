**Saga**: Development lifecycle
**Capability**: DL.CD — Continuous delivery

---

# [DL.CD.7] Remove manual approvals to practice continuous deployment

**Category:** OPTIONAL

Fully automate all stages of the deployment process, allowing developers to push new
code into the production environment using fully automated delivery pipelines—with no
manual approval stages required. This is referred to as continuous deployment. Removing
all manual deployment steps reduces potential errors and increases deployment speed. It
allows developers to focus more on coding and less on deployment logistics, improving
efficiency and productivity.

Create fully automated pipelines which perform continuous
integration and continuous deployment. A pipeline should
trigger upon code changes being merged into the main release
branch. This pipeline should perform all necessary quality
assurance tests, build the application, and deploy the new
version to the production environment. Automated governance
capabilities ensure that guardrails are being followed, while
observability functions such as alerts and logs provide
visibility.

This level of automation is a hallmark of mature DevOps
practices. However, it is an optional capability as it is not
always achievable or desired, especially in heavily regulated
industries or in organizations with strict governance
controls.

**Related information:**

- [Continuous
Delivery vs. Continuous Deployment](https://aws.amazon.com/devops/continuous-delivery/)
- [Practicing
Continuous Integration and Continuous Delivery on
AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/implementing-continuous-integration-and-continuous-delivery.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.7-remove-manual-approvals-to-practice-continuous-deployment.html*
