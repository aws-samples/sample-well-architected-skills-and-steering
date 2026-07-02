# Performance efficiency

**Pages**: 5

---

# Selection

CONTAINER_BUILD_PERF_01: How do you reduce the size of your
container image?

**Use small parent
images**

The OS parent image that is used to create the target images
has a huge impact on the final container image size. We can
see huge differences when comparing different base images:

```
`ubuntu:20.04 72.7MB
debian:10-slim 69.3MB
alpine:3.14 5.6MB`
```

We can
use [Alpine](https://hub.docker.com/_/alpine)
to build performant containers, but for certain languages
there are even more optimized run environments we can
leverage. When using statically linked binaries,
[scratch](https://hub.docker.com/_/scratch)
can be an alternative. In the following example, we have a
multi-stage build with a builder image based on Alpine (we
will discuss multi-stage builds later in the document). In the
first stage, the Go programming language application is built
to a statically linked binary, the second stage uses scratch
as base image and run the application built in the first
stage. With this combined approach of a multi-stage build and
using scratch as a base image, we achieve the smallest
possible target image for running our application:

```
`FROM golang:alpine AS builder

....

RUN go build -o /go/bin/myApplication

FROM scratch
COPY --from=builder /go/bin/myApplication /go/bin/myApplication

CMD ["/go/bin/myApplication"]`
```

**Run a single process per
container**

It is highly recommended to limit the number of processes in
each container to one. This approach simplifies the
implementation of
[separations
of concerns](https://www.castsoftware.com/blog/how-to-implement-design-pattern-separation-of-concerns#:~:text=Separation%20of%20concerns%20is%20a,of%20concerns%20is%20about%20order) using simple services. Each container
should only be responsible for a single aspect of the
application that facilitates horizontal scaling of this
particular aspect. If it’s necessary to run more than one
process per container, use a proper process supervisor (like
[supervisord](http://supervisord.org/))
and an init system (like
[tini](https://github.com/krallin/tini)).

**Exclude files with from your
build process**

The `.dockerignore` file
is similar to `.gitignore`
and is used to exclude files that are not necessary for the
build, or are of a sensitive nature. This can be useful if
it’s not possible to restructure the source code directory to
limit the build context. The following example shows a typical
`.dockerignore` file, which excludes files like the compilation
target-directory, JAR-files, and subdirectories.

```
`*
!target/*-runner
!target/*-runner.jar
!target/lib/*
!target/quarkus-app/*`
```

CONTAINER_BUILD_PERF_02: How do you reduce the pull time of your
container image?

**Use a container registry
close to your cluster**

One of the essential factors in the speed of deploying container images from a
registry is locality. The registry should be as close to the cluster as possible, which
means that both the cluster and the registry should be in the same AWS Region. For
multi-region deployments, this means that the CI/CD chain should publish a container image
to multiple Regions. An additional way to optimize the pull time of your container image
is to keep the container image as small as possible. In [Tradeoffs](./tradeoffs.html)
multi-stage builds are discussed in detail to reduce the image size.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/selection.html*

---

# Review

CONTAINER_BUILD_PERF_03: How do you make sure to get consistent
results for your target images?

Using the `latest` tag for
the parent image could potentially lead to issues because the
latest version of the image might include breaking changes
compared to the version that is currently used.

CONTAINER_BUILD_PERF_04: How do you make sure to use updated
versions for parent images?

**Implement a notification
mechanism for updated parent images**

If you’re using a team- or enterprise-wide image, you should
implement a notification mechanism based as part of your CI/CD
chain to distribute the information about a new parent image
to the teams. The teams should build target images with the
new parent images and measure the performance impact of the
changes by running a proper test suite.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/review.html*

---

# Monitoring

CONTAINER_BUILD_PERF_05: How do you make sure you get consistent
performance results over time?

**Implement an automated
performance testing strategy**

System performance can degrade over time. It’s important to
have an automated testing and monitoring system in place to
identify degradation of performance. Every time you build
target images based on new parent images, you should measure
the performance impact of the changes in the parent image.
This also includes the overall build process, because we have
to make sure that a testing and monitoring system covers the
CI/CD chain. Performance metrics and image sizes have to be
collected using services like Amazon CloudWatch and teams must
be alarmed
if [anomalies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
have been detected.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/monitoring.html*

---

# Tradeoffs

CONTAINER_BUILD_PERF_06: How do you optimize the size of your
target image?

**Use caching during
build**

A container image is created using layers. Each statement in a
Dockerfile (like `RUN` or `COPY`) creates a new layer. These
layers are stored in a local image cache and can be reused in
the next build. The cache can be invalidated by changing the
Dockerfile, which means that all subsequent steps to build the
image must be rerun. Naturally, this has a great influence on
the speed the image is built. Thus, the order of the commands
in your Dockerfile can have a dramatic effect on build
performance. In the following example you can see the effect
of the proper ordering of statements in a Dockerfile:

```
`FROM amazonlinux:2
RUN yum update -y
COPY . /app
RUN yum install -y python python-pip wget
CMD [ "app.py" ]`
```

This simple container image uses `amazonlinux` with tag 2 as parent image. In the second step, the Amazon Linux distribution is updated with the latest patches. After that, the Python application is copied into the container image. Next, Python, pip, wget, and additional dependencies required by the application are installed. In the final step, we start the application. The issue with this approach is that each application change results in cache invalidation for all subsequent steps. A small change in the application results in a rerun of the Python installation, which has a negative impact on build time.

An optimized version of the Dockerfile looks like this:

```
`FROM amazonlinux:2
RUN yum update -y && yum install -y python python-pip wget

COPY . /app

CMD [ "app.py" ]`
```

Now the `COPY` statement of the application is located after `yum
install`. The effect of this small adaption is that a change of
the application code results in fewer layer changes. In the
previous version of the file, each application change results
in an invalidation of the layer that installs Python and other
dependencies. This had to be rerun after a code change. One
additional aspect, which is covered in the optimized version
of this Dockerfile, is the number of layers. Each `RUN` command
creates a new layer, by combining layers it is possible to
reduce the images size.

**Use the CPU architecture
with best price to performance ratio**

AWS Graviton-based Amazon EC2 instances deliver up to 40% better price performance over
comparable current generation x86-based instances for a broad spectrum of workloads.
Instead of using one build-server for x86 and ARM in combination with QEMU for CPU
emulation, it might be a more efficient architecture to use at least one build server per
CPU architecture. For example, it is possible to create multi-architecture container
images to support AWS Graviton-based Amazon EC2 instances and x86 using AWS CodeBuild and
AWS CodePipeline. As described in the blog post [Creating multi-architecture Docker images to support Graviton2 using AWS CodeBuild and
AWS CodePipeline](https://aws.amazon.com/blogs/devops/creating-multi-architecture-docker-images-to-support-graviton2-using-aws-codebuild-and-aws-codepipeline/), this approach includes three CodeBuild projects to create an x86
container image, an ARM64 container image, and a manifest list. A manifest list is a list
of image layers that is created by specifying one or more (ideally more than one) image
names. This approach is used to create multi-architecture container images.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/tradeoffs.html*

---

# Resources

This section provides companion material for the Container Build Lens with respect to
the performance efficiency pillar.

**Blogs and documentation**

- [Advanced
Dockerfile: Faster builds and smaller images using
BuildKit](https://www.docker.com/blog/advanced-dockerfiles-faster-builds-and-smaller-images-using-buildkit-and-multistage-builds/) and multistage builds
- [Use
multi-stage builds](https://docs.docker.com/develop/develop-images/multistage-build/)
- [Dockerfile
reference](https://docs.docker.com/engine/reference/builder/)
- [Run
multiple services in a container](https://docs.docker.com/config/containers/multi-service_container/)
- [Best
practices for writing Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

**Partner solutions**

[Dockerfile
best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy)

**Videos**

[Dockerfile
best practices](https://www.youtube.com/watch?v=JofsaZ3H1qM)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/resources-3.html*

---
