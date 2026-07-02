**Saga**: Automated governance
**Capability**: AG.DEP — Dynamic environment provisioning

---

# [AG.DEP.2] Continuously baseline environments to manage drift

**Category:** FOUNDATIONAL

Baselining environments is a structured process for routinely updating and
standardizing individual environments within the landing zone to match a specified
configured state or *baseline*. Drift management, a part of this process,
involves the identification and resolution of differences between the environment's current
configuration and its desired baseline state.

Regular baselining helps to ensure consistency across
environments at scale, minimizing errors and enhancing
operational efficiency and governance capabilities. The
centralized platform team that manages the landing zone and
environments within require the ability to consistently add
new features, security configuration, performance
improvements, or resolving detected drift issues.

The team must be able to baseline all targeted environments
every time a change is made to the overall landing zone
desired state definition or when a misconfiguration is
detected within the environment.

It is the shared responsibility of the platform team and teams operating workloads to
verify that the correct policies, alerts, and resources are configured properly and
securely. As these teams are both making changes to the same environment, it is important
that all controls and resources managed by the platform team are secured against
unauthorized modifications by other teams operating within the environment. Changes being
made by the platform team to the environment should be communicated to the other teams
to promote a culture of transparency and collaboration.

All deployment, updates, or new features made to the
environments should be made through an infrastructure as code
(IaC) approach, which allows for version control, testing, and
reproducibility of environments. It is also recommended to
have a separate staging environment to test these changes
before they are deployed to the production environments,
further reducing the risk of disruptions or errors.

**Related information:**

- [Customize
your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/customize-landing-zone.html)
- [Types
of Landing Zone Governance Drift](https://docs.aws.amazon.com/controltower/latest/userguide/governance-drift.html)
- [Customize
accounts with Account Factory Customization (AFC)](https://docs.aws.amazon.com/controltower/latest/userguide/af-customization-page.html)
- [Overview
of AWS Control Tower Account Factory for Terraform
(AFT)](https://docs.aws.amazon.com/controltower/latest/userguide/aft-overview.html)
- [Implementing
automatic drift detection in CDK Pipelines using Amazon EventBridge](https://aws.amazon.com/blogs/devops/implementing-automatic-drift-detection-in-cdk-pipelines-using-amazon-eventbridge)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/ag.dep.2-continuously-baseline-environments-to-manage-drift.html*
