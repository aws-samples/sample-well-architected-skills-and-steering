**Saga**: Development lifecycle
**Capability**: DL.EAC — Everything as code

---

# [DL.EAC.7] Automate compute image generation and distribution

**Category:** OPTIONAL

The management of compute images, including containers and machine images, can be
optimized and made more reliable through a code-driven approach. Compute images generally
include a base image, libraries, environment variables, application code, and
configuration files. Similar to other forms of infrastructure as code (IaC), compute
images can be codified, stored in version control systems, tested, and distributed as part
of the development lifecycle.

Establish automated pipelines for building, testing, and distributing compute images.
The build stage creates the image based on its code definition, the
*test* stage validates the functionality and security compliance of
the image, and the *distribution* stage ensures the image is readily
available for teams to use in their environments and workloads. Updates to the images
should be automated, accounting for software patches, security enhancements, and other
modifications.

Given the diverse range of applications and infrastructure
requirements, especially when using managed cloud-based
services, not all organizations or workloads necessitate using
dedicated compute images or codifying them.

**Related information:**

- [Amazon EC2 Image Builder](https://aws.amazon.com/image-builder/)
- [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture)
- [What
is AWS App2Container?](https://docs.aws.amazon.com/app2container/latest/UserGuide/what-is-a2c.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.7-automate-compute-image-generation-and-distribution.html*
