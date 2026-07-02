**Saga**: Development lifecycle
**Capability**: DL.CI — Continuous integration

---

# [DL.CI.7] Validate the reproducibility of builds

**Category:** OPTIONAL

Every build for a specific version of source code should
ideally be able to generate the same outputs from the same
inputs. The implementation of reproducible builds primarily
involves the creation of an immutable and consistently created
build environment and controlling the inputs for each and
every build.

Between each build, the environment should be destroyed and recreated so that it is
immutable. Use infrastructure as code (IaC) and containerization to help with automating
the creation of the environment in a repeatable and consistent way. Have controls in place
to detect and prevent configuration drift that may alter the build environment
post-creation. All dependencies and software components used to create the environment and
perform the build should be version pinned and recorded.

Any manual intervention during the build can introduce
variability. Every step in the build process needs to be
automated. Factors that can render the build nondeterministic,
such as unrestricted network access and the use of random
generators or timestamps that modify the build artifact, must
be limited.

Verify the reproducibility by establishing processes that
regularly check the reproducibility of the builds. This can
involve triggering builds from the same source code in
different environments and comparing the results. Adopt
mechanisms like binary diffing or checksum comparison to
validate the reproducibility of the build. Set up alarms that
raise alerts when discrepancies occur to provide fast feedback
when there are inconsistencies.

Having reproducible builds is optional and not recommended for
all organizations or workloads. While striving for
reproducibility is encouraged, it may not be achievable in
every context. For example, some builds may depend on specific
environmental parameters or timing elements that make
reproducibility difficult.

**Related information:**

- [Reproducible
builds](https://reproducible-builds.org/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.7-validate-the-reproducibility-of-builds.html*
