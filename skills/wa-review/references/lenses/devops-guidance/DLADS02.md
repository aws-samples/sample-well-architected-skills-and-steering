**Saga**: Development lifecycle
**Capability**: DL.ADS — Advanced deployment strategies

---

# [DL.ADS.2] Implement automatic rollbacks for failed deployments

**Category:** FOUNDATIONAL

Implement an automatic rollback strategy to enhance system
reliability and minimize service disruptions. The strategy
should be defined as a proactive measure in case of an
operational event, which prioritizes customer impact
mitigation even before identifying whether the new deployment
is the cause of the issue.

Rollback should be initiated based on alarms linked to key
metrics like fault rates, latency, CPU usage, memory usage,
disk usage, and log errors. Additionally, consider both the
service's overall health and instance-specific
metrics. Incorporate a waiting period after a deployment to
closely monitor the system. This allows time to identify
potential issues that might not be evident immediately,
especially when the system is under low load. Establish
methods to prevent deployments during higher-risk times or
when there are active system issues. This could include
blocking deployments during when high-severity aggregate
alarms are raised or during specific time windows.

The rollback process should include the redeployment of the last successful code
revision, artifact version, or container image, and should employ methods like rolling or
blue/green deployments, or [feature flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) for a swift
rollback with minimal disruption. Consider using the advanced deployment methods introduced
in this capability for more granular control over deployments. Rollback considerations
should not be limited to the latest deployments, but also account for latent changes that
may be the source of current issues. To handle these situations, provide the ability for
developers to select a specific previously deployed release for rollback.

After the rollback, depending on the specific issue being addressed, consider
proactively rolling back other environments that could potentially also be affected, even
if they aren't currently showing any customer impact. Alternatively, if the issue appears to
be environment-specific, wait for the pipeline to roll forward a new release that includes a
bug fix. These operational decisions should be supported by the ability to compare the
changes between the current release and the selected rollback release's deployment
artifacts, including source code changes and changes in library versions.

**Related information:**

- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- [My
CI/CD pipeline is my release captain: Easy and automatic
rollbacks](https://aws.amazon.com/builders-library/cicd-pipeline/#Easy_and_automatic_rollbacks)
- [Automating
safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/?did=ba_card&trk=ba_card)
- [Amazon's
approach to high-availability deployment: Rollback
alarms](https://youtu.be/bCgD2bX1LI4?t=1669)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.2-implement-automatic-rollbacks-for-failed-deployments.html*
