**Saga**: Development lifecycle
**Capability**: DL.CI — Continuous integration

---

# [DL.CI.5] Sequence build actions strategically for prompt feedback

**Category:** RECOMMENDED

By optimizing the sequence of actions or tasks in your
continuous integration pipeline, feedback can be timely,
allowing developers to quickly react and make necessary
changes. This practice reduces the risk of delayed releases
due to late detection of issues.

Initiate long-duration actions earlier and run them in
parallel with other actions, preventing bottlenecks. Tasks
less prone to failure or of lower importance should be
scheduled later to prioritize higher impact tasks. Regularly
reviewing and adjusting action sequences ensures they
effectively identify issues early and provide actionable
feedback.

Strategically sequencing build actions is categorized as
recommended as the foundational focus should first be on
establishing a solid continuous integration pipeline and then
later enhancing it by optimizing the build.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.5-sequence-build-actions-strategically-for-prompt-feedback.html*
