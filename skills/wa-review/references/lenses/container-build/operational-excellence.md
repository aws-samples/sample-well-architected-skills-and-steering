# Operational excellence

**Pages**: 5

---

# Organization

There are no operational excellence best practices for
organization specific to the container build process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/organization.html*

---

# Prepare

CONTAINER_BUILD_OPS_01: How do you manage the lifecycle of your containers
and images?

**Understand the lineage of your container image**

It is important to understand what is built into your
container image. When you start building a new project, at
times it’s easier to use a base image from a verified source,
such as an official Ubuntu image. While these help developers
get up and running faster, often images contain packages and
libraries that are not required to run your application and
take up additional space. Starting with a minimal container
image will save space and speed up the starting of your
container when it’s deployed into production.

Many customers that we speak with take the additional step of
creating parent images. These images form the base for what
all containers in the organization are built on top of. These
parent images are minimal images that put into place
requirements and security controls established by the
organization. For example, the parent image can configure an
internal package source repository that contains curated and
validated library package versions.

Understanding the lineage of your container image helps you efficiently develop, run,
manage, and maintain your containers. It also helps maintain your security posture. You
can find more details in the [Security Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

**Have parity between your deployment environments**

A major benefit of using containers is to provide the ability
for the development team to develop new updates and features
using an identical artifact that runs in production. As much
as possible, development, testing, QA, and production
environments in that it will be eventually deployed should be
as similar as possible. All environments should share best
practices for everything, with the differences between them
being the ability to scale and the data operated upon. Best
practices for development environments differ
between orchestration tools so make sure you are following
recommendations based on your containerized platform of
choice.

**Build the image once and use the same image in all
environments**

Once the new image has been built with the updates in place
for deployment, promote the same image into the next
environment, testing, QA, and production, to provide for
consistency across all environments. This will reduce the
number of changes introduced in each new environment and
provide for more consistent behavior.

**Use a CI/CD build process**

Like with your applications, you should use a CI/CD pipeline
to build and test your images through every stage in your
development process. The CI process usually starts upon a
trigger that is sent from a version control system (usually
git). Whether your application requires compilation or not,
there are several steps to take to build the container.

- Check the code out from the code repository.
- Build the application artifact (executable binary or
language-specific archive).
- Build the container image from the artifact that you just
created.
- Run tests against the built container image.
- Push the container image to the target container registry.

Once built, you will begin continuous deployment where an
automated deployment pipeline takes the recently built
container image, its manifests, and container package (Helm
chart, Kustomization overlay, and so on), and deploys it to
the target environment.

**Multi-stage builds**

Small container images have undeniable performance advantages.
The pull from the registry is faster because less data is
transferred over the network, and the container startup time
is also reduced. This can be achieved by using multi-stage
builds. With this mechanism, you can split the build-phase of
the image from the final image that will be used to run the
application.

```
`FROM debian:10-slim AS builder
# First step: build java runtime module
...

ENV M2_HOME=/opt/maven
ENV MAVEN_HOME=/opt/maven
ENV PATH=${M2_HOME}/bin:${PATH}

COPY ./pom.xml ./pom.xml
COPY src ./src/

ENV MAVEN_OPTS='-Xmx6g'

RUN mvn clean package

# Second step: generate container run image
FROM debian:10-slim

...

COPY --from=builder target/application.jar /opt/app/application.jar

ENV JAVA_HOME=/opt/java
ENV PATH="$PATH:$JAVA_HOME/bin"

EXPOSE 8080

CMD ["java", "-server", "-jar", "application.jar"]`
```

In this example, we start building a container image with the build stage
**builder** that will be referenced in the target image. In the
builder-stage, we generate the complete build environment with all the dependencies (in
this case JDK and Maven) and build the JAR-file containing the application. In the second
step of the build process, there is an additional `FROM` statement that
indicates we start a new build stage. The `COPY` command references the former
builder-stage and copies the JAR-file into the current stage of the build. With this
approach, it is possible to implement reproducible builds with all necessary dependencies
and lightweight target images. However, this build process is more complicated compared to
standard builds and usually takes longer.

**Implement a minimal container image design to achieve your business and
security objectives**

It is important to build into your container image only what
is necessary. Pictures and other static assets should be
stored in a data store, for example Amazon Simple Storage Service (Amazon S3) in AWS, and served through a content
delivery network (CDN). This will achieve a minimal container
image size, which does not only reduce the storage and running
host resource requirements, but it also speeds up the
instantiation of a new container from an image if the image
itself is not cached locally.

**Using package managers to deploy your containerized
applications**

When building a containerized application, the deployable unit
can be not only the container image, but its per-environment
configuration that is deployed alongside with the container
image to the target environment. To achieve this, users can
use packaging tooling such as Helm and Kustomize for
Kubernetes, AWS Copilot for Amazon Elastic Container Service
(Amazon ECS), Docker Swarm for Docker, and more. That means
when building your containerized application, the target
artifact will be a package that contains a reference to the
container image and its common configurations across all
environments. Such configurations can be environment variable,
flags, ports, and other specific configurations. This package
will then be deployed to different target environments with
per-environment customizations. An example of this can be a
Helm chart with an application that references a database
endpoint. The Helm chart will contain all the common
configurations for development, testing, and production
environment, leaving some values to be configured
per-environment such as the database endpoint. Then there will
be different files such as `values-dev.yaml` and a
`values-prod.yaml` that will contain different database
endpoints for the development and production environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/prepare.html*

---

# Operate

CONTAINER_BUILD_OPS_02: How do you know whether your
containerized workload is achieving its business goals?

An important part of operating any workload is understanding
the health of your workload quickly. The sooner an issue can
be identified the better.

To ensure the success of your running container, you must
understand the health of your containerized workload as well
as what your customers are experiencing when they interact
with your application. Identify sources of information within
your workload and use the information to understand the health
of the containerized workload. Identifying where the telemetry
within your workload will come from, determining the proper
logging levels, identifying the thresholds and information
from that telemetry that must be acted upon, and identifying
the action that is required when those thresholds are passed
will reduce risk and impact on your users.

**Implement health checks to determine container state**

Implement container health checks. Health checks are one way to determine the health
of your running container. They enable your orchestration tooling to direct connection
traffic to the container only when it is ready to accept connections, or stop routing
connections to the container if the health checks show that the container is no longer
running as expected. In the latter case, the orchestration tooling will tear down the
misbehaving container and replace it with a new healthy one.

For example, with Amazon ECS you can define health checks as
part of the task definition, and perform load balancer health
checks for your running application.

For Kubernetes and Amazon Elastic Kubernetes Service (Amazon EKS), you can take advantage of features such as liveness
probes to detect deadlock condition, readiness probes to
determine if the pod is prepared to receive requests, and
startup probes to know when the application running in the
container has started. Liveness probes can either be shell
commands or HTTP requests of TCP probes.

**Have your logs available
outside the running container**

Ensure that the logs generated by your running containers are
collected and accessible externally. This will enable you to
use log monitors to gain more insights into the behavior and
functionality of your running container. Your application
should be writing its logs to `STDOUT` and `STDERR` so that a
logging agent can ship the logs to your log monitoring
system.

As with other application workloads, you must understand the
metrics and messages that you have collected from your
workload. Not only must you understand the data emitted by
your containers, but you must also have a standardized log
format to easily evaluate the data with your logging tools.
Logging collector and forwarder tools give you the ability to
standardize your log format across multiple containerized
services.

To enable you and your team to pinpoint where issues may be
occurring, define your log messages to be consistently
structured to enable correlation of logs across multiple
microservices in your central logging system.

This understanding enables you to evolve your workload to
respond to external pressures such as increased traffic or
issues with external APIs that your workload may use in the
course of accomplishing its business goals.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/operate.html*

---

# Evolve

There are no operational excellence best practices for evolve
specific to the container build process.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/evolve.html*

---

# Resources

This section provides companion material for the Container Build Lens with respect to
the operational excellence pillar.

**Blogs and documentation**

- [Health
checks and self-healing with EKS](https://aws.github.io/aws-eks-best-practices/reliability/docs/application/)
- [Implementing
health checks (400 level general guidance)](https://aws.amazon.com/builders-library/implementing-health-checks/)
- [How can I
get my Amazon ECS tasks running using the Amazon EC2 launch type to pass the Application Load Balancer health
check in Amazon ECS?](https://aws.amazon.com/premiumsupport/knowledge-center/troubleshoot-unhealthy-checks-ecs/)
- [How do I
troubleshoot health check failures for Amazon ECS tasks on Fargate?](https://aws.amazon.com/premiumsupport/knowledge-center/ecs-fargate-health-check-failures/)
- [EKS
Windows container logging best practices](https://aws.github.io/aws-eks-best-practices/windows/docs/logging/)
- [Capturing
logs at scale with Fluent Bit and Amazon EKS](https://aws.amazon.com/blogs/containers/capturing-logs-at-scale-with-fluent-bit-and-amazon-eks/)
- [Monitor, troubleshoot, and optimize your containerized applications
infographic](https://d1.awsstatic.com/asset-repository/AWS_CloudWatch_Infographic%20Container%20and%20Anomaly%20DES_8-15-19_FINAL.pdf)

**Partner solutions**

- [Docker
container logging](https://docs.docker.com/config/containers/logging/)
- [Fluent
Bit documentation](https://docs.fluentbit.io/manual/)

**Whitepapers**

[Running
Containerized Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/running-containerized-microservices/introduction.html)

**Training materials**

- [One
observability workshop](https://catalog.workshops.aws/observability/)
- [Kubernetes
health checks](https://www.eksworkshop.com/beginner/070_healthchecks/)
- [Logging
with Amazon OpenSearch Service, Fluent Bit, and OpenSearch
dashboards](https://www.eksworkshop.com/intermediate/230_logging/)
- [Monitoring
using Prometheus and Grafana](https://www.eksworkshop.com/intermediate/240_monitoring/)
- [Tracing
with AWS X-Ray](https://www.eksworkshop.com/intermediate/245_x-ray/)
- [Monitoring
using Amazon Managed Service for Prometheus /
Grafana](https://www.eksworkshop.com/intermediate/246_monitoring_amp_amg/)
- [Monitoring
Amazon ECS clusters and containers](https://ecsworkshop.com/monitoring/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/resources.html*

---
