**Saga**: Development lifecycle
**Capability**: DL.EAC — Everything as code

---

# [DL.EAC.4] Implement continuous configuration for enhanced application management

**Category:** RECOMMENDED

*Configuration as code* is the practice of managing and tracking
configuration changes as code, providing an audit trail and reducing errors from manual
changes. [Continuous configuration](https://www.allthingsdistributed.com/2021/08/continuous-configuration-on-aws.html) uses configuration as code to enhance configuration
management by allowing configuration changes to be made independently of application code
deployments.

Configuration should be separated from application code to allow for independent
tracking and management. Use tools designed for managing configurations as code, such
as [AWS
AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/), to manage configuration externally from the application. Create fully
automated pipelines that perform continuous integration and continuous delivery (CI/CD)
based on changes to the configuration code. Just like with application deployment
pipelines, these configuration deployment pipelines should run quality assurance tests,
followed by deployment in a non-production environment before deploying to production.

It's important to distinguish between static and dynamic configuration types. Static
configurations do not change during the software's runtime and are specific to each
environment. Dynamic configurations can be adjusted at runtime without downtime. [Feature
flags](https://aws.amazon.com/systems-manager/features/appconfig#Feature_flags) are examples of dynamic configurations that can be used to control which
features are enabled per environment to decouple release from deployment. Operational
configurations, such as log level, throttling thresholds, connection/request limits,
alerts, and notifications, can be static or dynamic depending on the use case and need to
be managed. Application modes, which toggle the application to run as either
*development*, *test*, or
*production*, are typically considered to be static configuration
that is set at startup and do not change.

General use cases for continuous configuration include application integration
tuning, feature toggling, allowing access to premium content through allow lists, and
addressing operational issues and troubleshooting. To manage your configurations
effectively, establish a routine to prevent configuration bloat. While it can seem
tempting to externalize as many variables as possible, an excessively complex
configuration file can lead to confusion and errors. Carefully evaluate the necessity,
frequency of change, and runtime requirements of each value to decide if it should be
included as dynamic configuration.

For large-scale deployment of configuration as code, a [Dynamic Configuration Pipeline](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/dynamic-configuration-pipeline/index.html) is recommended. This allows centralized
management of the entire workload configuration and its components across all
environments. It ensures that all configurations are version-controlled, adhere to quality
assurance and code review processes, and is capable of progressively deploying
configuration changes and performing rollbacks as necessary to minimize system
disruptions.

Continuous configuration is beneficial in DevOps environments, as it improves
operational efficiency and scalability. However, not every system requires the complexity
associated with continuous configuration. Therefore, each workload should be evaluated
depending on architecture choice, team preferences, and service level objective
requirements.

**Related information:**

- [AWS Cloud Adoption Framework: Operations Perspective
- Configuration management](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-operations-perspective/configuration-management.html)
- [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Continuous configuration](https://www.allthingsdistributed.com/2021/08/continuous-configuration-on-aws.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.4-implement-continuous-configuration-for-enhanced-application-management.html*
