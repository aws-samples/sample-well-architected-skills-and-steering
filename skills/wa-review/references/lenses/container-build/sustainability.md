# Sustainability

**Pages**: 7

---

# Region selection

The Region selection best practice focuses on where you will implement your workloads
based on both your business requirements and sustainability goals. There are no
sustainability practices unique to the container build process for Region selection. Refer
to the [Region
selection](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/region-selection.html) best practice from the sustainability pillar of the Well-Architected
Framework for more information.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/region-selection.html*

---

# User behavior patterns

There are no sustainability practices unique to the container build process for user
behavior patterns. Refer to the [user
behavior patterns](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/user-behavior-patterns.html) best practice from the sustainability pillar of the
Well-Architected Framework for more information.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/user-behavior-patterns.html*

---

# Software and architecture patterns

CONTAINER_BUILD_SUSTAINABILITY_01: How do you design
your containerized application in a way that reduces the use of the underlying
resources?

When designing containerized application, you should keep your
build manifests up-to-date and aligned with your application
needs. A containerized application image starts from a
Dockerfile. The Dockerfile includes all commands required to
include the configuration and dependencies for the
containerized application. If there are some dependencies that
are no longer required, removing them from the Dockerfile can:

- Reduce the time that it takes to build the container
image. This affects host resource consumption by the build
process.
- Reduce the container image size and therefore reduce the
time it takes for this image to be pulled to an instance.
This affects host resources usage for running and storing
the container images.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/software-and-architecture-patterns.html*

---

# Data patterns

There are no sustainability practices unique to the container build process for the
data patterns best practice, see the [data
patterns](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/data-patterns.html) best practice from the sustainability pillar of the Well-Architected
Framework for more information.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/data-patterns.html*

---

# Hardware patterns

CONTAINER_BUILD_SUSTAINABILITY_02: How do you
support your containerized application to run on energy-efficient hardware?

To be able to [use instance types with the least environmental impact](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/use-instance-types-with-the-least-impact.html) (from the Sustainability
Pillar whitepaper), you have to ensure your containerized application is able to run on a
variety of instance types and architectures. This can be done by creating images that
support multi-architecture as described in the [Cost Optimization Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html). For example, you can use a build service
that supports multi-architecture build servers and combine them to a multi-architecture
image using the CI pipeline (see Graviton workshop as an [example](https://graviton2-workshop.workshop.aws/en/amazoncontainers.html)
of using AWS CodeBuild, and AWS CodePipeline alongside Graviton and Amazon EKS). You can also use tools
that generate multi-architecture images from a single Dockerfile, such as [Docker Buildx.](https://docs.docker.com/desktop/multi-arch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/hardware-patterns.html*

---

# Development and deployment process

Look for opportunities to reduce your sustainability impact by
making changes to your development, test, and deployment
practices.

CONTAINER_BUILD_SUSTAINABILITY_03: How do you design
your build tooling and services to improve efficiency of the underlying
resources?

**Use dynamically created
build servers for building your containerized
workload**

Using dynamically created build servers (such as
[AWS CodeBuild](https://aws.amazon.com/codebuild/)), ensures that while building your
containerized images, the needed infrastructure is being
provisioned when the build process starts, and being
terminated as soon as the build process ends.

**Use pre-defined or built
runtimes to reduce your build time, and reuse needed
dependencies for the build process**

When building different types of containerized applications,
using common and standardized runtimes for the build process
reduces the operational management of creating and maintaining
custom images. Also, by using the specific type of runtime for
your build server, it verifies that no common dependency is
being downloaded and configured as part of the build process.
All relevant dependencies are being incorporated into the
different runtimes of your build servers, and are being used
many times by different build processes for different
applications. An example of
[multiple
build runtimes](https://docs.aws.amazon.com/codebuild/latest/userguide/runtime-versions.html) can be found in the AWS CodeBuild
documentation.

**Update your parent and base
image regularly**

Update your base and parent images to the latest versions, as
sometimes there is a performance improvement that is
introduced in newer versions. These improvements are
translated into a sustainability improvement as it affects the
resource consumption of the underlying infrastructure, and as
a result improves the overall efficiency.

**Delete unused or obsolete
container images**

As described in the [Cost Optimization Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html), create mechanisms to verify that unused or
obsolete container images are deleted. This can be achieved, for example, by registry
[lifecycle
policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html), as exists in [Amazon ECR.](https://aws.amazon.com/ecr/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/development-and-deployment-process.html*

---

# Resources

This section provides companion material for the Container Build Lens with respect to
the sustainability pillar.

**Blogs and documentation**

General sustainability documentation:

- [Ask an Expert - Sustainability](https://aws.amazon.com/blogs/architecture/ask-an-expert-sustainability/)
- [AWS Sustainability](https://aws.amazon.com/sustainability/)

AWS sustainable documentation:

- [Understand
resiliency patterns and trade-offs to architect
efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/)
- [Optimizing
your AWS infrastructure for sustainability, part I:
Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
- [Automated
cleanup of unused images in Amazon ECR](https://aws.amazon.com/blogs/compute/automated-cleanup-of-unused-images-in-amazon-ecr/)

**Videos**

- [AWS re:Invent 2021 - Architecting for sustainability](https://www.youtube.com/watch?v=3-Zq2W1-odU)
- [AWS re:Invent 2021 - Behind the Scenes: AWS and sustainability| AWS Events](https://www.youtube.com/watch?v=sTurbjuHV6o)

**Training materials**

[Graviton
workshop](https://graviton2-workshop.workshop.aws/en/amazoncontainers.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/resources-5.html*

---
