**Saga**: Development lifecycle
**Capability**: DL.CD — Continuous delivery

---

# [DL.CD.4] Automate the entire deployment process

**Category:** FOUNDATIONAL

Automate as many stages of the delivery process as possible. Exceptions for
continuous delivery might include optional manual approval gates. Automation reduces the
risk of human error, brings consistency to deployments, and accelerates the delivery
process.

Use the delivery pipeline to automate every stage of deploying changes, from copying
the build artifact to setting up any required configurations. While optional manual approval
gates can exist, all other stages should be automated, maintaining the integrity of the
artifact and reducing the likelihood of errors. Humans should not have access to the target
environments or have the ability to inject code, parameters, configuration, or interfere
with the integrity of the artifact in any way.

Some organizations might still require manual oversight at certain stages as they
evolve their DevOps capabilities. If the organization is early in its DevOps adoption or
operates in a highly regulated environment, there might be a need for manual interventions
or approvals at certain stages. These could be due to governance or regulatory requirements
or simply the need for a human decision at a critical point in the deployment process. Over
time, even for these organizations, the goal should be to have no manual deployment stages
in the deployment of changes.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL08-BP05 Deploy
changes with automation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.html)
- [AWS Well-Architected Security Pillar: SEC11-BP06 Deploy
software programmatically](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_appsec_deploy_software_programmatically.html)
- [What
is Continuous Delivery?](https://aws.amazon.com/devops/continuous-delivery/)
- [Amazon CodeCatalyst](https://codecatalyst.aws/explore)
- [Building
the pipeline](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/building-the-pipeline.html)
- [Going
faster with continuous delivery](https://aws.amazon.com/builders-library/going-faster-with-continuous-delivery/)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture)
- [Deploy
container applications in a multicloud environment using
Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/deploy-container-applications-in-a-multicloud-environment-using-amazon-codecatalyst/)
- [Amazon's
approach to high-availability deployment: Release guidance
lifecycle](https://youtu.be/bCgD2bX1LI4?t=855)
- [Testing
software and systems at Amazon: Continuous integration and
deployment](https://youtu.be/o1sc3cK9bMU?t=1206)
- [The
Amazon Software Development Process: Continuous
Delivery](https://youtu.be/52SC80SFPOw?t=814)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cd.4-automate-the-entire-deployment-process.html*
