**Pillar**: Reliability

# FSIREL01: Have you planned for events that impact your software development infrastructure and challenge your recovery plans?

Financial services institutions are increasingly relying on continuous integration
(CI) and deployment (CD) pipelines to accelerate development and deployment. Often the
only way to change production systems is through the pipeline to ensure that quality
controls, security guard rails, and standards are maintained as part of the change
management process.

## FSIREL01-BP01 Treat your CI/CD tools as critical workload components for recovery

If key elements of an SDLC environment, such as the CI/CD
pipeline, are impacted, you might not be able to commit new
code, change configurations, pull containers, or upload
application artifacts, which can result in an outage of your
workload. Understand the entire dependencies of your SDLC and
plan for disruption of the critical components that the SDLC
relies on. Consider replicating your SDLC environment and
supporting services in another Region, which allows you to
continually replicate source code, application, and container
repositories. Based on the criticality of your workload, you
should understand how your components interact with both the
data plan and the control plan to understand what failures
would cause service disruptions to your workload.

## FSIREL01-BP02 Implement AI model versioning and rollback strategies

Financial services institutions must establish formal AI model
versioning and rollback capabilities to maintain operational
resilience. Implement immutable model registries that preserve
all model artifacts, training data characteristics,
hyperparameters, and performance metrics for each version.
Develop clear versioning conventions that include major and
minor designations based on the significance of model changes.
Establish automated deployment pipelines with built-in
validation gates and rollback triggers based on predefined
performance thresholds. Create comprehensive rollback
procedures that include not just technical reversion steps but
also business impact assessments, customer communication
templates, and regulatory notification processes where
required. Test rollback capabilities regularly as part of
disaster recovery exercises.

## FSIREL01-BP03 Add specialized AI system testing and validation to software testing methodology

Effective AI system testing and validation requires a
multi-layered approach beyond traditional software testing
methodologies. Establish separate development, testing, and
production environments with appropriate data separation and
access controls. Implement comprehensive testing regimes including
unit tests for individual components, integration tests for system
interactions, and holistic validation with representative data,
prompt and response testing, and human-in-the-loop evaluations
that provide qualitative checks for grounding, tone, and policy
compliance. For critical financial applications, conduct
adversarial testing to identify potential vulnerabilities and edge
cases. Validation should include fairness and bias assessments,
particularly for consumer-facing applications where regulatory
adherence is essential. Document all testing procedures, results,
and remediation actions to support audit requirements and
regulatory examinations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel01.html*
