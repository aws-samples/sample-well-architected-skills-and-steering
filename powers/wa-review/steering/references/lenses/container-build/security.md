# Security

**Pages**: 6

---

# Identity and access management

CONTAINER_BUILD_SEC_01: How do you ensure that your container
images are using least privilege identity?

By default, containers provide process isolation. This means that processes running inside of a container are isolated from processes and data
that exist in other containers as well as the container host’s operating system. However, it is important to note that the default behavior is to run
the container using the root user when running a container. When the processes inside the container are running as the root user, not only do they have
full administrative access to containers, they also have the same administrative level access to the container host. Having an application running within
a container through the root user expands the attack surface of the environment. This could provide bad actors with the ability to escalate privilege to
the container host infrastructure if the application is compromised.

There are multiple ways to mitigate this risk. The most straightforward method is to define the `USER` directive in the Dockerfile
used to compile the image:

```
`FROM amazonlinux:2
RUN yum update -y && yum install -y python python-pip wget
RUN groupadd -r dev && useradd -r -g dev dev
USER dev
...`
```

The Dockerfile referenced previously uses a `RUN` command to add the
`dev` user and group to the image and uses the `USER` directive to
ensure that the `dev` user is used when running commands inside of the
container. Therefore, even if the application hosted in this container is compromised, the
attackers would not be able to use the `dev` user within the container
to access other containers or the container host’s operating system.

CONTAINER_BUILD_SEC_02: How do you control access to your build
infrastructure?

**Limit administrator access to build infrastructure (CI pipeline)**

Adding continuous security validation in a build pipeline is a major focus for
organizations moving to a DevSecOps strategy. This helps ensure that security is built
into the application from the beginning of the application’s lifecycle as opposed to
performing security testing only at the end of the development process. However, it is
important to note that securing an organization’s build pipeline should be considered a
high priority as well, as the pipeline typically accesses databases, proprietary code, and
secrets or credentials across dev, test, and prod environments. A compromised build
pipeline could provide a bad actor with access to all of the preceding resources in a
customer environment. As detailed in the security pillar of the AWS Well-Architected
Framework, it is important to follow the best practice of granting the least privileged
access to the container build infrastructure. The least privileged best practice should be
applied to human identities as well as machine identities. An example might be that a
human identity that has access to the container build infrastructure can reach an
application’s source code, secrets, and other sensitive data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/identity-and-access-management.html*

---

# Detective controls

CONTAINER_BUILD_SEC_03: How do you detect and address
vulnerabilities within your container image?

**Ensure that your images are scanned for vulnerabilities**

After images are built, it is important to maintain a regular cadence of scanning those images to ensure no new or existing vulnerabilities have surfaced. There are two basic categories to consider when discussing image scanning: static scanning and dynamic scanning.

Static scanning is performed before the image is deployed. This is important because it allows organizations to detect vulnerabilities in a container image before a container is deployed into an environment. Many registry offerings provide native static image scanning that can scan container images for common vulnerabilities and exposures (CVEs) without having to integrate and maintain a third-party image scanning tool. The scanning process is performed by comparing parent container images, dependencies, and libraries that are used by the container image to known CVEs.

Dynamic container scanning is a process that scans the underlying infrastructure where containers run. It is executed post container deployment, and identifies vulnerabilities that may have been introduced by other software installed on the infrastructure itself. These vulnerabilities can be either modifications to an existing running container, or communication with a container that is exposed externally to other processes or hosts.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/detective-controls.html*

---

# Infrastructure protection

CONTAINER_BUILD_SEC_04: How do you manage your container image
boundaries?

**Minimize attack surface**

In the context of container workloads, infrastructure
protection is often a topic with respect to the container as a
vector to access the underlying compute infrastructure. In any
security context, reducing attack surface is top of mind. This
can be accomplished when designing and building your container
in a variety of ways:

- Run distroless images without a shell or a package manager
to ensure that bad actors cannot make changes to the image
or easily download software packages to aid in their
attack.
- Build open-source libraries from source or scan libraries
for vulnerabilities to ensure awareness of all of the
components of the container image.
- Remove or defang
`setuid`
and
`setgid`
bits from the container image to make sure that these
permissions are not used in privilege escalation attacks.
- Lint your Dockerfile to help identify violations of best
practices for building container images.
- Use a tool such as
[docker-slim](https://github.com/docker-slim/docker-slim)
to analyze existing images and remove unnecessary binaries
not required by the application.
- Ensure that your container is designed to operate with a
read-only root filesystem. This functionality is normally
defined at runtime but it is important to consider this
facet when designing the container itself.

**Understand the lineage of
your container image**

Aside from reducing attack surface, it is also important to understand where your container images are coming from. If not building images from scratch, you should only run images from trusted registries that have been signed with a trusted signature to ensure integrity. Regarding signing images, it is recommended to utilize signed images to ensure that the contents of the container have not been modified before they are deployed.

In general, don’t incorporate images directly from a public repository into your container pipeline. Private registries should be used to allow an organization to maintain complete control and visibility over their container image catalog. If using images originating from public repositories, they should be scanned, signed, and stored in a private registry to ensure that the contents of the image are known and verified against existing security standards.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/infrastructure-protection.html*

---

# Data protection

CONTAINER_BUILD_SEC_05: How do you handle data within your
containerized applications?

**Do not hardcode sensitive data into your container image**

With respect to handling data in the build and design of the
container, it is important that no sensitive information is
stored in the container itself. For example, user credentials
should never be hardcoded into your container image. Instead,
consider using a secret management protocol that is compatible
with the container orchestration system being used to manage
the container workloads.

**Ensure that persistent data
is stored outside of the container**

Also, if your containerized application writes or consumes
persistent data, ensure that data is stored outside of the
container. Since containers are intended to be ephemeral, use
volumes to store persistent data that will remain intact long
after a container’s lifecycle has completed.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/data-protection.html*

---

# Incident response

There are no security best practices for incident response
specific to the container build process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/incident-response.html*

---

# Resources

This section provides companion material for the Container Build Lens with respect to
the security pillar.

**Blogs and documentation**

- [Container
monitoring - Why, how, and what to look out for](https://aws.amazon.com/cloudwatch/container-monitoring/)
- [Amazon ECR container image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)
- [Scanning
Amazon ECR container images with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/enable-disable-scanning-ecr.html)
- [Container
scanning updates in Amazon ECR private registries using
Amazon Inspector](https://aws.amazon.com/blogs/containers/container-scanning-updates-in-amazon-ecr-private-registries-using-amazon-inspector/)
- [Building
end-to-end DevSecOps CI/CD pipeline](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/)
- [Logging
image scan findings from Amazon ECR in CloudWatch using
AWS Lambda](https://aws.amazon.com/blogs/containers/logging-image-scan-findings-from-amazon-ecr-in-cloudwatch-using-an-aws-lambda-function/) function
- [Compliance
as code for Amazon ECS using Open Policy Agent,
Amazon EventBridge, and AWS Lambda](https://aws.amazon.com/blogs/containers/compliance-as-code-for-amazon-ecs-using-open-policy-agent-amazon-eventbridge-and-aws-lambda/)
- [AWS Secrets Manager controller POC: an EKS operator for
automatic rotation of secrets](https://aws.amazon.com/blogs/containers/aws-secrets-manager-controller-poc-an-eks-operator-for-automatic-rotation-of-secrets/)

**Partner solutions**

- [Content
trust in Docker](https://docs.docker.com/engine/security/trust/)
- [Notary
project](https://github.com/notaryproject/notaryproject) - Signature of an OCI artifact
- [Cosign](https://github.com/SigStore/cosign)
- Container signing, verification, and storage in an OCI
registry

**Whitepapers**

- [EKS
best practices (image security)](https://docs.aws.amazon.com/docs.aws.amazon.com/eks/latest/best-practices/image-security.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/resources-1.html*

---
