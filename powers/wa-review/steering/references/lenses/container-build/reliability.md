# Reliability

**Pages**: 5

---

# Foundations

CONTAINER_BUILD_REL_01: How do you limit the amount of CPU and
memory a container consumes?

**Use RAM and CPU limits**

By default, a running container will use the full RAM and CPU
of the host system. This can lead to performance bottlenecks
on the host and put your workload in a degraded state.

Setting RAM and CPU limits on your running container will
improve the availability of the host system and the workload.
In Amazon ECS, update the CPU and memory parameters in the
task definition to limit the CPU and RAM a container will
consume.

```
`{
"containerDefinitions": [
{
"command": ["/bin/sh -c 'echo HELLO WORLD! >> /usr/share/nginx/html/index.html'"],
"entrypoint": ["sh", "-c"],
"image": "nginx:1.20.1-alpine",
"name": "hello-world",
"portMapping": [
{
"containerPort": 80,
"hostPort": 80,
"protocol": "tcp"
}
]
}
],
"CPU": "256",
"memory": "512",
"executionRoleArn": "arn:aws:iam::012345678910:role/ecsTaskExecutionRole",
"family": "fargate-task-definition",
"networkMode": "awsvpc",
"runtimePlatform": {"operatingSystemFamily": "LINUX" },
"requiresCompatibilities": [ "FARGATE" ]
}`
```

If you are going to run your container workload on Amazon EKS,
update the CPU and memory values in the resources section of
your YAML file. The requests and limits keys are used to
define how much memory and CPU a specific container will
consume when running.

```
`---
apiVersion: apps/v1
kind: Deployment
metadata:
name: frontend
labels:
app: web
spec:
replicas: 1
selector:
matchLabels:
app: web
template:
metadata:
labels:
app: web
spec:
containers:
- name: app
ports:
- containerPort: 80
image: nginx:1.20.1-alpine
resources:
requests:
memory: "64Mi"
CPU: "250m"
limits:
memory: "128Mi"
CPU: "500m"`
```

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/foundations.html*

---

# Workload architecture

CONTAINER_BUILD_REL_02: How do you handle persistent data in a
container application?

**Use volumes to persist
data**

There are times when workloads have to store data across multiple containers. For example, an image-processing application that saves images for processing. Given the ephemeral nature of a container workload, data on the container will be lost once the container is restarted and longer exists.

Use mounted volumes, whether block or network file system (NFS), to persist file data for an application. Mounted volumes allow for file data sharing among multiple running containers. In addition, mounted volumes should be used to persist logs or configuration files.

For persisting data, use external database such as Amazon Relational Database Service (Amazon RDS), Amazon DynamoDB, or Amazon Aurora. Use a database system that provides performance, high-availability, and scalability to your container application when persisting data.

CONTAINER_BUILD_REL_03: How do you automate building and
testing of containers?

**Create local testing
processes**

When building a containerized application, you want to be able
to test your application as early as possible. That means that
you have to think about how developers will be able to test
their containerized application locally. First you will have
to decide whether the container build for local testing will
run on the developer’s machine or in a remote machine, because
this will have an impact on the tooling that developers use on
their machines. Second, you will have to provide a local
deployment mechanism. For this, you can use single containers
that run as part of an automation script or deploy the
containers locally using a local version of your target
orchestrator. This can be also part of the testing section of
your local build-script. With this approach, you can deploy
necessary infrastructure components like databases in a
lightweight fashion in order to test your application with the
real infrastructure instead of mocked APIs. One example might
be a Docker Compose manifest to deploy multiple containers in
a single command. For Kubernetes, use minikube to deploy the
containerized application and all of its objects (such as
Deployment, ConfigMaps, and Secrets).

**Design your testing
environments to support your container build
pipeline**

When building a containerized application, it can be easily
deployed throughout multiple environments. In order to
validate that your application is running properly, you will
have to test your containerized applications. With the
container’s ecosystem, you can have multiple manifests for all
of the applications in an environment, and you can easily
provision a ready-to-use environment with all dependent
services already deployed in it. This process of temporary, or
ephemeral testing environments, can be achieved in lower
effort given the ease of reproducing fully configured
environments that are based on containers. Whether you’re
using the GitOps methodology for a Kubernetes based
application, or a centralized deployment configuration, you
should try to create reproducible environments to support
testing of your containerized application.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/workload-architecture.html*

---

# Change management

CONTAINER_BUILD_REL_04: How do I cascade updates to a parent or
base image?

**Create a standardized parent
image**

Based on a lean parent image, a team- or enterprise-wide image
can be created that provides optimizations to all teams. This
could also be multiple parent images depending on the
containerized application frameworks and languages. An
organization could potentially start with a lean image
containing company-specific configurations, and teams can add
additional software that is necessary to run the different
applications. This could be, for example, a Java Runtime
Edition (JRE) or a specific Python version. One disadvantage
of this solution is that if a parent image is changed, all
images that use it - directly or indirectly - must also be
recreated.

**Use an image hierarchy
approach**

Try to maintain an image hierarchy in your container image
strategy. A hierarchy or layered approach to container images
helps with maintenance, cascading of updates to base images,
and allows for the reuse of container images. In addition, it
helps maintain the security posture of the broader
organization by using the same images that have the security
controls image managed by a central team. Operations like
patching of a parent image should trigger a rebuild with
changes to child images. As a best practice, separate images
into the following categories:

- Intermediate base image
- Application server
- Application source code or binary

The intermediate base image is a small and lightweight base OS image. See the
following example of a base image, which is the Docker Hub's official public alpine image.
Note
Before using images
from a public repository, take steps to review the image for
security vulnerabilities.

`FROM alpine:3.13`

The application server image is a specific image of the platform application to run
the developer's code but does not contain the application's binary code itself. See the
following example of an application server image, which is Docker Hub's official NGINX
image. It contains the base image of `alpine:1.13` and the NGINX platform
application. The following Dockerfile is built using `docker build -t
nginx:1.20.1-alpine`.

```
`FROM alpine:3.13
...
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off"]`
```

Lastly, the application binary created by the developer should reside in the
container image. The container image comprises all the developer's source code to run
their application. The following example uses the application server image, and copies the
application code into the image.

```
`FROM nginx:1.20.1-alpine
COPY . /usr/share/nginx/html`
```

**Use source control and
tagging on all container images**

Maintain the Dockerfile for all container images in a source
control repository in the image hierarchy and ensure proper
tagging of container images. In addition, use a contentious
integration process to create a direct correlation between the
container's images in source control and the image tag. This
best practice is critical to determine what changed in the
container image from a prior release.

For example, tag `1.0` indicates that this tag will always point
to the latest patch release `1.0.1`, `1.0.2`, `1.0.3`, and so on.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/change-management.html*

---

# Failure management

CONTAINER_BUILD_REL_05: How do you monitor the health of a
container?

**Plan for health checks in
all containers builds and deployments**

It is common to initially develop container applications without thinking of the availability of the services in the container. When running container applications, there is no way of knowing whether the services running within a container are up or not. Adding a health check or probe to the container provides testing of the services in the container. Health check options are available in Docker using the `HEALTHCHECK` command, however, `containerd` does not have this option.

Examine the orchestrations systems health check and probing options. This could include liveness and readiness probes within Amazon EKS or health checks within a definition file within Amazon ECS.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/failure-management.html*

---

# Resources

This section provides companion material for the Container Build Lens with respect to
the reliability pillar.

**Blogs and documentation**

- [Create the
AppSpec file](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-create-appspec-file.html)
- [AppSpec File
example](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-example.html)
- [Task
definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)
- [Dockerfile reference: Healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck)
- [How
Amazon ECS manages CPU and memory resources](https://aws.amazon.com/blogs/containers/how-amazon-ecs-manages-cpu-and-memory-resources/)
- [Tutorial: Deploy an Amazon ECS service](https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-ecs-deployment.html)

**Whitepapers**

- [EKS
best practices (reliability)](https://aws.github.io/aws-eks-best-practices/reliability/docs/)
- [Amazon ECS best practices - Auto scaling and capacity
management](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity.html)

**Training materials**

[AWS containers immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/ed1a8610-c721-43be-b8e7-0f300f74684e/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/resources-2.html*

---
