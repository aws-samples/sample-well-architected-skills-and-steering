# Cost optimization

**Pages**: 6

---

# Practice cloud financial management

CONTAINER_BUILD_COST_01: How do you design your container
build process to avoid unnecessary cost?

Building a containerized application can result in multiple
images for the same service. Depending on your organization
policy, you might want to keep a subset of your container
images to be used in a case of a rollback scenario. An example
of such a policy might be that you don’t roll back more than
three versions, or more than three months in time. That means,
that not all container images of a specific application should
be kept. Deleting old images can save costs as container
registries charge by size of images stored in the registry.
You can achieve this deletion policy by creating automation
processes, or use service features, for example: Amazon ECR
supports a lifecycle policy that can be used to expire
(delete) images based on rules such as image age, count,
specific tags and more
(see [Examples
of lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html)).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/practice-cloud-financial-management.html*

---

# Expenditure and usage awareness

CONTAINER_BUILD_COST_02: How do you design your container
build process to avoid unnecessary cost?

**Designing efficient
container build process**

Building containers is a process that consumes compute and
storage resources and can lead to unnecessary costs if not
using it properly. The build process consumes resources for
each build, and there are some considerations that have to be
taken for it to be efficient from a cost perspective.

**Application
dependencies**

The container image is usually being built alongside with the application build step. During this build step, all necessary dependencies, libraries, and modules that are being used by the application code are downloaded to the container image.
Using unnecessary dependencies will make the build time longer, and will result in wasting compute resources of the build system.

**Common container image
dependencies**

Some operating system packages are needed for multiple applications in the
organization for a specific runtime (for example, Python and Java). Building a parent
container image that preinstalls all common operating system packages and dependencies for
the specific runtime will result in a more efficient build process. Without this common
image, each individual container image would be installing the same packages, thus wasting
compute and network resources. This practice will also shorten the time for container
images built from a specific runtime, since all of its common operating system packages
and dependencies are already included in the parent container image. As a result, this
will reduce costs for building all other container images that use this parent image.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/expenditure-and-usage-awareness.html*

---

# Cost-effective resources

Container images can affect the overall cost of the system and
workloads. In this section, we’ll describe what has to be done
in order to optimize your container images, and why it is
important from cost perspective.

CONTAINER_BUILD_COST_03: Ensure that your container images
contain only what is relevant for your application to run

Container image size affects several processes related to
running your containerized workload. The following processes
can be affected by having unnecessary large container image
size.

**Containerized application
start-up time**

Container image size affects the time needed for an image to
be pulled from a container registry. Large image sizes
(hundreds, or thousands of MB), can lead to a slow startup
time of the application, which can lead to:

- Waste compute resources while waiting for images to be
pulled.
- Slow scale-out operations.

Container image size also affects the scaling time needed for a containerized application to become ready to receive traffic. This time can translate to a waste of resources. In small-scale replicas of your application, the waste might not be notable, but when dealing with a dynamic autoscaled environment, a 30-second delay between a triggered scale-out event and a container ready to run can result in hundreds of compute minutes wasted per month. To put this delay into an equation, 30 seconds multiplied by 100 pod launches per day, over a period of one month, can result in:

```
`30(sec)*100(launches of pods)*30 (days)=90,000 seconds = 1,500 minutes of compute time that is wasted.`
```

**Storage requirements for
containers**

Consider your instance’s storage requirements depending on
your container image size. The size of your container image
has a direct effect on the instance storage size that the
container will run on. This can result in the need for a
larger storage size for your instances.

Container image size also affects the storage requirements of
the container registry, since the container image will be
stored in the registry. Stored images in Amazon ECR are priced
per GB-month. For current pricing, refer to the
[pricing
page](https://aws.amazon.com/ecr/pricing/).

CONTAINER_BUILD_COST_04: How do you reduce your container
images size?

A container image consists of read-only layers that represent a Dockerfile
instruction. Each instruction creates one additional layer on top of the previous layer.
Running multiple consecutive commands can result in a large container image size, even if
we delete content in the container image itself. An example of that might be installing a
package, and deleting the cached downloaded files that are not needed anymore after
installing the package. The following example shows that we installed
`some-package` and then delete the cached files. Even though we used the
`rm` command to remove the cached file, the container image contains a layer
representing the `rm -rf ...` command, and is still containing a layer with the
actual cached files, resulting in a larger container image.

```
`RUN apt-get install -y some-package
RUN rm -rf /var/lib/apt/lists/*`
```

In order to overcome this, we can concatenate commands, and
use a one-liner approach to install packages and remove the
cached files in a single command:

```
`RUN apt-get install -y some-package && rm -rf /var/lib/apt/lists/*`
```

Reducing image layers can be done with several techniques:

- **Building container images from the
scratch image** - This can result in creating the
minimal container image possible, especially when
containerizing executable applications with minimal
external dependencies from the OS (like Go, Rust, and C).
- **Use lightweight base
images** - For other type of programming
languages that need a runtime environment in the container
image, using parent and base images of lightweight
distributions like Alpine can reduce the image size
significantly. For example: a Python container image based
on Debian parent image is ~330MB in size whereas a Python
container image based on Alpine parent image is ~17MB in
size.
- **Reducing the number of RUN instructions by chaining
commands together** - Installing dependencies and deleting cache in a
single command as shown in the previous command. This practice should only be used
when the consecutive commands relate one to another.
- **Consider using package managers
flags to reduce dependency sizes** - Such as
`no-install-recommends` with `apt-get`.
- **Use multi-stage builds**
- Multi-stage builds let you reduce image sizes by using
build cache from the previous build step and copying only
needed dependencies to the final container image. For
example, see
[docker
docs](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).
- Follow
[Dockerfile
best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy) such as:

Use `COPY` instead of `ADD`.
- Use absolute path when using `WORKDIR`.
- Exclude files from the build process using
`.dockerignore`. Specify exclusion patterns of file,
directories or both (similar to `.gitignore`). This
makes it easy to exclude unnecessary files from `COPY`
or `ADD` commands.

CONTAINER_BUILD_COST_05: How do you design your containerized
application to support automatic scaling and graceful termination?

When designing applications that will be containerized, it is
important to include signal handling within the code and/or
the container itself. Handling signals is a fundamental
practice for writing applications, especially when writing
applications that will run inside a container. The application
should handle system signals and react according to the
application logic. Although this is not directly related to
cost, handling signals is a key element for using cost saving
practices like automatic scaling or using Amazon EC2 Spot
Instances. When a scale-in event, or replacement or
termination of a Spot Instance occurs, the container
orchestrator system or tools will send a `SIGTERM` signal to the
application notifying the application to shut itself down
gracefully. If it fails to do so, the process may end up being
terminated while performing work, which can prohibit the use
of auto scaling or spot in general.

CONTAINER_BUILD_COST_06: How do you design your containerized
application to support multiple CPU architectures?

Different instance families offer different performance for the same amount of
hardware (CPU and memory). An example is using a newer instead of an older generation of
instances, or using instances with different CPU architecture, such as ARM. To use a
different instance architecture, you have to change your build process. Since the default
behavior of the build process is to create a container image that is designed to run on
the architecture of the instance that it was built on, you have to create multiple images
for each CPU architecture. To create multiple images, run the same build process on an x86
instance, and on an ARM-based instance. Use tagging suffixes to differentiate between the
different architectures. You can see an example container image tag when searching images
in your registry (see [aws-node-termination-handler](https://gallery.ecr.aws/aws-ec2/aws-node-termination-handler) and search for container images in the Amazon ECR
public gallery under the **Image tags** tab) and look for the different
*-linux-arm64* and *-linux-amd64* suffixes. Having
different container image tags allows you to schedule and run the x86 version of your
container image on an x86 instance, and the ARM version of your container image on an ARM
instance. You have to make sure that the correct container image version will run on the
correct instance. You can’t run the ARM version of your container image on an x86
instance, and vice versa. The [Docker image manifest v2
schema 2](https://docs.docker.com/registry/spec/manifest-v2-2/), and the [OCI image
index specification](https://github.com/opencontainers/image-spec/blob/main/image-index.md) were created to make it easier to run your container image
on any architecture. This additional specification allows you to create a high-level
manifest that contains a list to other already existing container images. This container
manifest, contains a reference to all the different container images, specifying their
operating system type, architecture, and the digest of the container image that is
referenced. Using the manifest, the container runtime will know which image to pull based
on what architecture the underlying instance uses. An example of different container image
manifests and manifests list, is displayed in the following screenshot from the [Amazon ECR public
gallery](https://gallery.ecr.aws/aws-ec2/aws-node-termination-handler):

*Figure 1. Example of container image manifests and
manifest lists for multi-architecture container images*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/cost-effective-resources.html*

---

# Manage demand and supply resources

CONTAINER_BUILD_COST_07: How do you minimize cost for your
containerized application during startup time?

Longer startup times for containerized applications can result in wasted compute resources.
Shortening startup times can be done on the application-level (code optimization), or on the container level. For example, if the application needs external dependencies to be present in the container, it should be already installed during the build process, or it should be included in the parent image, and not downloaded at startup using an entrypoint script or `DOCKERFILE` commands.

CONTAINER_BUILD_COST_08: What systems are you using to create
your container build process?

Creating any build process requires developing, maintaining, and operating a build system. This can be done by a variety of methods, such as using OSS tooling for job automation, or using self-developed systems that are able to run build scripts for your application. However, running and maintaining this kind of system involves software development costs, operational costs, compute, and storage costs for running the system.
Alternatively you can use build and pipeline services, such as Amazon EC2 Image Builder, AWS CodeBuild, and AWS CodePipeline. Using managed services removes the operational overhead and allows developers to consume pipeline runs and build jobs on a pay-as-you-go basis.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/manage-demand-and-supply-resources.html*

---

# Optimize over time

There are no cost best practices unique to the container build
process for optimize over time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/optimize-over-time.html*

---

# Resources

This section provides companion material for the Container Build Lens with respect to
the cost optimization pillar.

**Blogs and documentation**

- [StopTask
API sending SIGTERM signal](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopTask.html)
- [Termination
of Pods (signals)](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination)
- [Graceful
shutdowns with Amazon ECS](https://aws.amazon.com/blogs/containers/graceful-shutdowns-with-ecs/)

**Partner solutions**

- [Dockerfile
best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Multi
stage builds](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#use-multi-stage-builds)
- [Don’t
install unnecessary packages](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#dont-install-unnecessary-packages)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/resources-4.html*

---
