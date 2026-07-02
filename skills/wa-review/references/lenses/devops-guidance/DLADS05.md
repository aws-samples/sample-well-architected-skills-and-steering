**Saga**: Development lifecycle
**Capability**: DL.ADS — Advanced deployment strategies

---

# [DL.ADS.5] Ensure backwards compatibility for data store and schema changes

**Category:** RECOMMENDED

Backwards compatibility in data stores and schemas ensures
that as changes are made, previous versions of the system
continue to operate as expected. This requires careful
planning, thorough testing, and detailed monitoring. As
modifications, additions, or deletions are made to data
structures and schemas, these changes should be designed to
coexist with previous data structures, allowing both old and
new versions to operate concurrently. Maintaining backwards
compatibility helps to avoid breaking changes that could
disrupt continuous integration and delivery pipelines.

One way to achieve backwards compatibility is by implementing
versioning in your data schemas. With this method, new changes
are incorporated into a new version, while older versions
remain functional for existing applications.
[Feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) can also be used to conceal new alterations until
they're fully ready, facilitating testing and phased rollout
of updates without affecting existing users.

To ensure the safe implementation of these changes, they
should be thoroughly tested in a non-production
environment. Testing typically involves three stages to detect
potential issues: initially, the change is deployed to a
fraction of the servers to verify coexistence of software
versions; next, the deployment is completed across all
servers; and finally, a rollback deployment is initiated. If
no errors or unexpected behavior occur during these stages,
the test is considered successful.

In scenarios involving changes that require coordination between different
microservices, it is important to maintain consistency in the order of deployments across
environments. For example, in serialization contexts, readers are typically deployed
before writers during roll-forward, while writers precede readers during rollbacks.

**Related information:**

- [Ensuring
rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/)
- [Using
Amazon RDS Blue/Green Deployments for database
updates](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/blue-green-deployments.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.5-ensure-backwards-compatibility-for-data-store-and-schema-changes.html*
