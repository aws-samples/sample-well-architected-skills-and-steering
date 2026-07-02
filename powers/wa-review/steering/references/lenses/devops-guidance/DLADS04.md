**Saga**: Development lifecycle
**Capability**: DL.ADS — Advanced deployment strategies

---

# [DL.ADS.4] Implement Incremental Feature Release Techniques

**Category:** RECOMMENDED

Incremental feature releases gradually roll out new features
to users, reducing risk and maintaining system stability.
Techniques include dark launching, two-phase deployments,
feature flags, and canary releases. These techniques enable
safe, controlled, and iterative changes to distributed systems
which reduces risk associated with concurrent updates and
maintaining system stability.

[Dark
launches](https://martinfowler.com/bliki/DarkLaunching.html) allow teams to integrate and test new features
in a live environment, without needing to make them visible to
the entire user base. This approach allows for monitoring and
analyzing the impact and performance of new features under
real-world conditions, while mitigating the risk of widespread
disruptions. Depending on system implementation and team
preferences, dark launches can be implemented using
versioning, A/B testing, canary releases, or most commonly,
using feature flags.

[Feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) allow developers to turn on or off certain
features in their code base without affecting other
functionality. This allows for testing of new features with a
subset of users, limiting potential negative impacts. Feature
flags provide an additional layer of control over the feature
rollout process and can be used for A/B testing, canary
releases, and dark launches.

[Two-phase
deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments#Two-phase_deployment_technique) complement dark launching, focusing
primarily on managing read and write changes in a systematic
and phased manner. Changes should first be prepared to handle
a new update without actively implementing it (Prepare phase),
followed by a second deployment that activates the new changes
(Activate phase). This approach requires careful planning and
coordination, but pays off by prioritizing data integrity and
preventing stale records that could emerge from concurrent
changes.

The specific choice of technique, be it dark launching, two-phase deployments,
feature flags, canary releases, or a combination, depends on your unique needs, the nature
of the changes, the complexity of the system, and the degree of control required over the
release process. Each of these methods offers its own advantages, and their strategic
implementation can significantly enhance the resilience and efficiency of your
deployments.

**Related information:**

- [Amazon CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently)
- [Feature
Flags - AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [My
CI/CD pipeline is my release captain: Multiple inflight
releases](https://aws.amazon.com/builders-library/cicd-pipeline/#Multiple_inflight_releases)
- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- [Using
AWS AppConfig Feature Flags](https://aws.amazon.com/blogs/mt/using-aws-appconfig-feature-flags/)
- [The
Only Guide to Dark Launching You'll Ever Need](https://launchdarkly.com/blog/guide-to-dark-launching/)
- [Deployment
Pipeline Reference Architecture: Dynamic Configuration
Pipeline](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/dynamic-configuration-pipeline/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.4-implement-incremental-feature-release-techniques.html*
