**Pillar**: Cost Optimization

# FSICOST13: Do you use cloud services to accommodate consulting or testing of projects?

Some financial services institutions hire contractors during specific months, or for a
project. Procuring a new machine, and ensuring that it is meeting the compliance standards
of a financial services institution can be resource intensive. Using a service like Amazon
WorkSpaces for end-user computing can help with cost-efficient utilization of resources.

## FSICOST13-BP01 Set up pay-as-you-go services when team expands for certain duration

Some financial services institutions hire contractors during specific months, or for
a project. These contractors can work on a project for a short duration, like 6 months to
a year. Procuring a new machine, and ensuring that it is meeting the compliance standards
of a financial services institution can be resource intensive. Using a service like [Amazon WorkSpaces](https://aws.amazon.com/workspaces/faqs/) for end-user computing can
help with cost-efficient utilization of resources. You can create workspaces per your
internal standards, and provision it for a new resource.

**Testing and consulting environments** Extend this
principle to generative AI experimentation by provisioning temporary, cost-capped
environments for proof of concept or consulting engagements. Use ephemeral inference
endpoints (for example, Amazon Bedrock provisioned throughput with automatic teardown) and
time-bounded SageMaker AI Studio domains for data scientists and contractors.

Establish guardrails that enforce token quotas, model tier limits, and usage budgets
per project, keeping generative AI testing compliant and cost-efficient. For partner or
consulting access, apply fine-grained IAM roles and service control policies (SCPs) to
segregate environments and avoid cross-account spend leakage.

Automate cleanup of idle notebooks, vector stores, and test embeddings using
AWS Lambda or Amazon EventBridge rules, verifying that sandbox environments incur zero residual cost
post-engagement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost13.html*
