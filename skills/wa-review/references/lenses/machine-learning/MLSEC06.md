# MLSEC06 — Monitoring

**Pillar**: Security  
**Best Practices**: 2

---

# MLSEC06-BP01 Restrict access to intended legitimate consumers

Use least privilege permissions to invoke the deployed model
endpoint. For consumers who are external to the workload
environment, provide access using a secure API.

**Desired outcome:** You establish
secure inference API endpoints that allow only authorized parties to
access your ML models. You create a controlled environment where
model access is restricted based on legitimate business needs, while
maintaining monitoring capabilities to track interactions with your
models. Your ML endpoints are protected using the same security
principles applied to other HTTPS APIs, providing data protection in
transit and proper authentication.

**Common anti-patterns:**

- Allowing public access to model endpoints without proper
authentication.
- Using overly permissive IAM roles for model endpoint access.
- Failing to implement network controls for inference endpoints.
- Not monitoring or logging model inference activities.
- Using the same credentials for development and production model
access.

**Benefits of establishing this best
practice:**

- Reduced risk of unauthorized model access and potential data
exfiltration.
- Enhanced control over who can use your ML models and when.
- Improved monitoring and auditability of model usage.
- Protection of intellectual property embedded in models.
- Improves adherence to regulatory requirements for data security.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing your ML model endpoints is critical to protect both your
intellectual property and the data processed by these models. By
treating ML inference endpoints with the same security rigor as
other HTTPS APIs, you can maintain a strong security posture while
enabling legitimate business use. You need to implement proper
authentication, network controls, and monitoring to verify that
only authorized parties can access your models.

When deploying machine learning models in production, you should
consider the model as a valuable asset that requires protection.
This means implementing layers of security controls including
network isolation through VPC configuration, strong authentication
mechanisms, and continuous monitoring of inference activities. For
external consumers, create a dedicated API layer that enforces
security policies and controls access.

### Implementation steps

- **Plan your access control
strategy**. Define which users or applications need
access to your model endpoints and what specific permissions
they require. Follow the principle of least privilege,
granting only the minimum permissions necessary for each
consumer to perform their required tasks.
- **Set up secure inference API
endpoints**. Host your ML models so that consumers
can perform inference against them securely. Use
[Amazon SageMaker AI endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-manage.html) with proper authentication and
authorization controls. Use
[Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to automatically
benchmark and optimize your model deployments for the best
security-performance balance, and select optimal compute
instances and configurations while maintaining security
controls. This approach defines the relationship between the
model and its consumers, restricts access to the base model,
and provides monitoring capabilities for model interactions.
- **Implement network security
controls**. Configure your SageMaker AI inference
endpoints within a VPC to isolate network traffic. Use
security groups to define inbound and outbound traffic
rules, and consider using
[AWS PrivateLink](https://aws.amazon.com/privatelink/) for private connectivity to your
endpoints. Follow guidance from the
[AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) to implement proper
network controls, such as restricting access to specific IP
ranges and implementing bot protection.
- **Configure authentication and
authorization**. Sign HTTPS requests for API calls
so that requester identity can be verified. Use
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) to control who has access
to your SageMaker AI resources and what actions they can
perform. Consider using
[Amazon Cognito](https://aws.amazon.com/cognito/) for managing user identities if your API is
accessed by external users.
- **Deploy endpoints in a secure VPC
configuration**. Use
[VPC
endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) to privately connect your VPC to supported
AWS services without requiring an internet gateway. Follow
the guidance in
[Give
SageMaker AI Hosted Endpoints Access to Resources in Your
Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html) to configure your endpoint for VPC access.
- **Implement encryption for data in
transit and at rest**. Configure your endpoints to
use HTTPS for API calls. Encrypt model artifacts and data at
rest using
[AWS Key Management Service (KMS)](https://aws.amazon.com/kms/). Use client-side encryption
for sensitive data when appropriate.
- **Set up monitoring and
logging**. Configure
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor your endpoints and
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to log API calls. Implement
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to detect drift and data quality issues
in your production models.
- **Use model registry for
governance**. Implement
[SageMaker AI
MLflow Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to catalog and manage versions
of your models, control which model versions are deployed,
and maintain an audit trail of model approvals and
deployments.
- **Implement proper API design
patterns**. Design your inference API following
REST best practices. Include proper input validation, error
handling, and rate limiting to protect against abuse.
Consider implementing an
[API Gateway](https://aws.amazon.com/api-gateway/) in front of your SageMaker AI endpoint for
additional controls.
- **Conduct regular security
reviews**. Periodically review the security
configuration of your endpoints, check for over-permissive
policies, and validate that access logs show only expected
patterns of usage.
- **Implement guardrails for AI
models**. For AI endpoints, implement content
filtering and validation controls to provide responsible
outputs, stop harmful content generation, and maintain
appropriate use of the models.

## Resources

**Related documents:**

- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Real-time
Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
- [Give
SageMaker AI Hosted Endpoints Access to Resources in Your Amazon VPC](https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Integrating
machine learning models into your Java-based
microservices](https://aws.amazon.com/blogs/awsmarketplace/integrating-machine-learning-models-into-your-java-based-microservices/)
- [How
Financial Institutions can use AWS to Address Regulatory
Reporting](https://aws.amazon.com/blogs/architecture/how-banks-can-use-aws-to-meet-compliance/)
- [Secure
deployment of Amazon SageMaker AI resources](https://aws.amazon.com/blogs/security/secure-deployment-of-amazon-sagemaker-resources/)
- [Accelerating
Machine Learning Development with Data Science as a Service
from Change Healthcare](https://aws.amazon.com/blogs/apn/accelerating-machine-learning-development-with-data-science-as-a-service-from-change-healthcare/)

**Related videos:**

- [End-to-End
machine learning using Spark and Amazon SageMaker AI](https://www.youtube.com/watch?v=FKgivdwzO5g)

**Related examples:**

- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec06-bp01.html*

---

# MLSEC06-BP02 Monitor human interactions with data for anomalous activity

Implement comprehensive monitoring of data access events to detect
unauthorized or suspicious activities. By auditing user interactions
with data, you can identify potential security threats such as
unusual access patterns, abnormal locations, or activity that
exceeds normal baselines. Use specialized AWS services for anomaly
detection alongside data classification to assess risks and protect
your machine learning assets.

**Desired outcome:** You have
comprehensive visibility into human interactions with your data,
with logging enabled for create, read, update, and delete
operations. You can identify who accessed specific data elements,
what actions they took, and when those actions occurred. Your
monitoring system automatically flags anomalous activities based on
established baselines and alerts you to potential security threats.
Data classification is integrated with your monitoring approach to
prioritize security events based on data sensitivity.

**Common anti-patterns:**

- Implementing logging without monitoring or analysis
capabilities.
- Focusing only on system-level access without tracking specific
data interactions.
- Failing to establish user activity baselines for anomaly
detection.
- Not classifying data to differentiate between access to
sensitive and non-sensitive information.
- Monitoring access events without automated alerting mechanisms.

**Benefits of establishing this best
practice:**

- Early detection of potential data breaches or insider threats.
- Improved ability to investigate security incidents with
comprehensive audit trails.
- Improves adherence to data protection regulations and
requirements.
- Better visibility into how data is being used across your ML
systems.
- Reduced risk of unauthorized data access or exfiltration.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting your machine learning data requires visibility into who
is accessing it and how it's being used. By monitoring human
interactions with your data, you can identify potential security
threats before they lead to data breaches or misuse. This involves
implementing comprehensive logging for data access events,
classifying your data based on sensitivity, and using automated
tools to detect anomalous behavior.

Start by enabling logging for data interactions, particularly
focusing on human access rather than just system-to-system
communications. Your logs should capture details about who
accessed the data, what specific elements they accessed, what
actions they took, and when those interactions occurred. This
creates an audit trail that serves as the foundation for your
monitoring strategy.

Next, classify your data based on sensitivity and importance. By
knowing which datasets contain personally identifiable information
(PII), intellectual property, or other sensitive information, you
can prioritize monitoring efforts and apply appropriate security
controls. This classification details the potential impact of
unauthorized access to different datasets.

Finally, implement anomaly detection to identify unusual patterns
that might indicate security threats. These anomalies could
include access from unusual locations, outside normal working
hours, excessive access volume, or access to data that's not
typically needed for an employee's role. When anomalies are
detected, your system should generate alerts to prompt
investigation.

### Implementation steps

- **Enable data access
logging**. Verify that you have data access logging
for human CRUD (create, read, update, and delete)
operations, including the details of who accessed what
elements, what action they took, and at what time. Leverage
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to capture API calls and user activities
across your AWS environment. Configure CloudTrail to log
data events for
[Amazon S3](https://aws.amazon.com/s3/) buckets containing your training and inference
data. For SageMaker AI environments, use
[Amazon SageMaker AI Logging and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html) capabilities to
track access to ML models and datasets.
- **Classify your data**. Use
[Amazon Macie](https://aws.amazon.com/macie/) for protecting and classifying training and
inference data in
[Amazon S3](https://aws.amazon.com/s3/). Amazon Macie is a fully managed security service
that uses ML to automatically discover, classify, and
protect sensitive data in AWS. The service recognizes
sensitive data, such as personally identifiable information
(PII) or intellectual property. Configure Macie to perform
regular automated scans of your S3 buckets to identify and
tag sensitive data. Create custom data identifiers in Macie
to recognize organization-specific sensitive data patterns
beyond the standard patterns Macie detects.
- **Monitor and protect**. Use
[Amazon GuardDuty](https://aws.amazon.com/guardduty/) to monitor for malicious and unauthorized
activities. This will enable protecting AWS accounts,
workloads, and data stored in
[Amazon S3](https://aws.amazon.com/s3/). Configure GuardDuty to analyze CloudTrail logs,
VPC flow logs, and DNS logs to detect suspicious activities.
Pay special attention to the
[GuardDuty
S3 Finding Types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html) which can detect anomalous access
patterns to your S3-stored data.
- **Set up anomaly detection**.
Implement automated anomaly detection for data access
patterns using
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html). Create CloudWatch
metrics for access frequency, data volume transferred,
access times, and other relevant metrics. Configure
CloudWatch alarms to alert when anomalies are detected based
on these metrics.
- **Establish data access
baselines**. Create baseline profiles of normal
user access patterns using
[AWS CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor access trends over time. Set up
dashboards that visualize normal patterns of data access by
team, role, or time period. Use these baselines to fine-tune
anomaly detection thresholds and reduce false positives.
- **Implement alerting
mechanisms**. Configure
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) to trigger automated responses when
suspicious access events are detected. Route alerts to your
security team through notification channels like
[Amazon SNS](https://aws.amazon.com/sns/) for immediate response. Create different alerting
thresholds based on data classification and sensitivity.
- **Centralize logging and
monitoring**. Use
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) (formerly Amazon OpenSearch Service) to create a centralized repository for log analysis
and visualization. Build comprehensive dashboards to monitor
data access patterns across your organization. Implement log
retention policies that comply with your regulatory
requirements.
- **Control and audit data exploration
activities**. Implement
[AWS Lake Formation](https://aws.amazon.com/lake-formation/) with
[Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/) to provide fine-grained access
controls for data exploration. Configure Lake Formation
permissions to restrict data access based on user roles and
data classification. Use
[AWS IAM](https://aws.amazon.com/iam/) to enforce least-privilege access to sensitive
data.
- **Monitor access to AI training
data**. Implement specialized monitoring for
datasets used to train AI models, as these may contain
particularly sensitive information or be subject to greater
privacy concerns. Use
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/) to detect drift in model
behavior that might indicate data access issues. Implement
enterprise-ready security and privacy controls for
foundation models.

## Resources

**Related documents:**

- [CloudWatch Logs for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/logging-cloudwatch.html)
- [GuardDuty
S3 Protection finding types](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
- [Configure
security in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/security.html)
- [Building
a Self-Service, Secure, & Continually Compliant
Environment on AWS](https://aws.amazon.com/blogs/architecture/building-a-self-service-secure-continually-compliant-environment-on-aws/)
- [How
to Use New Advanced Security Features for Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-use-new-advanced-security-features-for-amazon-cognito-user-pools/)
- [Best
practices for setting up Amazon Macie with AWS Organizations](https://aws.amazon.com/blogs/security/best-practices-for-setting-up-amazon-macie-with-aws-organizations/)

**Related videos:**

- [Protect
Your Data in S3 with Amazon Macie and Amazon GuardDuty - AWS
Online Tech Talks](https://www.youtube.com/watch?v=lvPT71jAIXk)
- [Protecting
sensitive data with Amazon Macie and Amazon GuardDuty](https://www.youtube.com/watch?v=h7pq95RMuEQ)

**Related examples:**

- [AWS Security Hub CSPM automated response and remediation](https://github.com/aws-solutions/aws-security-hub-automated-response-and-remediation)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsec06-bp02.html*

---
