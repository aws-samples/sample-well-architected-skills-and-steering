# Security

**Pages**: 7

---

# Identity and access management

SEC 1: How do you control access to your serverless API?

APIs are often targeted by attackers because of the operations that they can perform
and the valuable data they can obtain. There are various security best practices to
defend against these attacks.

From an authentication and authorization perspective, there are currently five
mechanisms to authorize an API call within API Gateway:

- AWS_IAM authorization
- Amazon Cognito user pools
- API Gateway Lambda authorizer
- Resource policies
- Mutual TLS authentication

It is important to understand if, and how, any of these mechanisms are implemented.
For consumers who are currently located within your AWS environment or have the means
to retrieve AWS Identity and Access Management (IAM) temporary credentials to access your environment, you can
use AWS_IAM authorization and add least-privileged permissions to the respective
IAM role to securely invoke your API.

The following diagram illustrates using AWS_IAM authorization in this
context:

*Figure 13: AWS_IAM authorization*

To add granularity into your IAM authorization you can implement tag-based access
control, which allows for better API-level control on the resources and actions.

If you have an existing Identity Provider (IdP), you can use an API Gateway Lambda
authorizer to invoke a Lambda function to authenticate or validate a given user against
your IdP. You can use a Lambda authorizer for custom validation logic based on identity
metadata.

A Lambda authorizer can send additional information derived from a bearer token or
request context values to your backend service. For example, the authorizer can return a
map containing user IDs, user names, and scope. By using Lambda authorizers, your backend
does not need to map authorization tokens to user-centric data, allowing you to limit
the exposure of such information to just the authorization function.

*Figure 14: API Gateway Lambda authorizer*

If you don’t have an IdP, you can leverage Amazon Cognito user pools to either provide built-in user
management or integrate with external identity providers, such as Facebook, Twitter,
Google+, and Amazon.

This is commonly seen in the mobile backend scenario, where users authenticate by
using existing accounts in social media platforms to register or sign in with their
email address or username. This approach also provides granular authorization through
[OAuth Scopes](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-enable-cognito-user-pool.html).

*Figure 15: Amazon Cognito user pools*

**

API Gateway API Keys is not a security mechanism and should not be used for authorization
unless it’s a public API. It should be used primarily to track a consumer’s usage across
your API and could be used in addition to the authorizers previously mentioned in this
section.

When using Lambda authorizers, we strictly advise against passing credentials or any
sort of sensitive data through query string parameters or headers, otherwise you may
open your system up to abuse.

Amazon API Gateway resource policies are JSON policy documents that can be attached to an API
to control whether a specified AWS Principal can invoke the API.

This mechanism allows you to restrict API invocations by:

- Users from a specified AWS account, or any AWS IAM identity.
- Specified source IP address ranges or CIDR blocks.
- Specified virtual private clouds (VPCs) or VPC endpoints (in any account).

With resource policies, you can restrict common scenarios, such as only
allowing requests coming from known clients with a specific IP range or from
another AWS account. If you plan to restrict requests coming from private IP
addresses, it’s recommended to use API Gateway private endpoints instead.

*Figure 16: Amazon API Gateway Resource Policy based on IP
CIDR*

With private endpoints, API Gateway will restrict access to services and resources inside
your VPC, or those connected through Direct Connect to your own data centers. To control
access to the VPC Endpoint you can add VPC endpoint policies so that you can grant or
deny the access to a particular APIs for the traffic going in your internal network.
Combining private endpoints, endpoint policies, and resource policies, an API can be
limited to specific resource invocations within a specific private IP range from a
specific VPC endpoint. This combination is mostly used on internal microservices where
they may be in the same account, or another account. If you are using API Gateway as a main
endpoint to your backend HTTP(s) services you can enable client-side SSL certificates so
that the backend services can authenticate and verify requests from API Gateway. When it comes
to large deployments and multiple AWS accounts, organizations can use cross-account
Lambda authorizers in API Gateway to reduce maintenance and centralize security practices. For
example, API Gateway has the ability to use Amazon Cognito user pools in a separate account. Lambda authorizers
can also be created and managed in a separate account and then re-used across multiple
APIs managed by API Gateway. Both scenarios are common for deployments with multiple
microservices that need to standardize authorization practices across APIs.

*Figure 17: API Gateway cross-account authorizers*

For cases like Internet of Things (IoT) or application-to-application authentication,
you can configure a mutual TLS (mTLS) authentication. In this scenario, the client
should present its certificate to verify its identity when accessing API Gateway endpoint. You
can also combine mTLS with Lambda authorizers for a more granular authorization
mechanism.

You can use AWS WAF to add protection of your APIs on the application network
layer. You can use managed rule groups to protect your APIs against well known attacks
like SQL injection and cross-site scripting (XSS), or if you have additional
requirements you can also create your own rule groups.

SEC 2: How are you managing the security boundaries of your
serverless application?

With Lambda functions, it’s recommended that you follow least-privileged access and
only allow the access needed to perform a given operation. Attaching a role with more
permissions than necessary can open up your systems for abuse.

With the security context, having smaller functions that perform scoped activities
contribute to a more well-architected serverless application. Regarding IAM roles,
sharing an IAM role within more than one Lambda function will likely violate
least-privileged access.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/identity-and-access-management.html*

---

# Detective controls

Log management is an important part of a well-architected design for reasons ranging
from security and forensics to regulatory or legal requirements.

It is equally important that you track vulnerabilities in application dependencies
because attackers can exploit known vulnerabilities found in dependencies regardless of
which programming language is used.

For application dependency vulnerability scans, there are several commercial and
open-source solutions, such as OWASP Dependency Check, that can integrate within your
CI/CD pipeline. It’s important to include all your dependencies, including AWS SDKs,
as part of your version control software repository.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/detective-controls.html*

---

# Infrastructure protection

For scenarios where your serverless application needs to interact with other
components deployed in a virtual private cloud (VPC) or applications residing
on-premises, it’s important to ensure that networking boundaries are considered.

Lambda functions can be configured to access resources within a VPC. Control traffic
at all layers as described in the AWS Well-Architected Framework. For workloads that
require outbound traffic filtering due to compliance reasons, proxies can be used in the
same manner that they are applied in non-serverless architectures.

Enforcing networking boundaries solely at the application code level and giving
instructions as to what resources one could access is not recommended due to separation
of concerns.

For service-to-service communication, favor dynamic authentication, such as temporary
credentials with AWS IAM over static keys. API Gateway and AWS AppSync both support IAM
Authorization that makes it ideal to protect communication to and from AWS
services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/infrastructure-protection.html*

---

# Data protection

Consider enabling [API Gateway Access Logs](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html)
and selectively choose only what you need, since the logs might contain sensitive data,
depending on your serverless application design. For this reason, we recommend that you
encrypt any sensitive data traversing your serverless application.

API Gateway and AWS AppSync employ TLS across all communications, clients, and integrations.
Although HTTP payloads are encrypted in-transit, request path and query strings that are
part of a URL might not be. Therefore, sensitive data can be accidentally exposed via
CloudWatch Logs if sent to standard output.

Additionally, malformed or intercepted input can be used as an attack vector—either
to gain access to a system or cause a malfunction. Sensitive data should be protected at
all times in all layers possible, as discussed in detail in the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html). The recommendations in that whitepaper
still apply here.

With regard to API Gateway, sensitive data should be either encrypted at the client-side
before making its way as part of an HTTP request, or sent as a payload as part of an
HTTP POST request. That also includes encrypting any headers that might contain
sensitive data prior to making a given request.

Concerning Lambda functions or any integrations that API Gateway may be configured with,
sensitive data should be encrypted before any processing or data manipulation. This will
prevent data leakage if such data gets exposed in persistent storage or by standard
output that is streamed and persisted by CloudWatch Logs.

In the scenarios described earlier in this document, Lambda functions would persist
encrypted data in either DynamoDB, OpenSearch Service, or Amazon S3 along with encryption at rest. We strictly
advise against sending, logging, and storing unencrypted sensitive data, either as part
of HTTP request path or query strings, or in the standard output of a Lambda function.

Enabling logging in API Gateway where sensitive data is unencrypted is also discouraged. As
mentioned in the [Detective controls](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/detective-controls.html) subsection, you should consult your compliance team
before enabling API Gateway logging in such cases.

SEC 3: How do you implement application security in your
workload?

Review security awareness documents authored by AWS Security bulletins and industry
threat intelligence as covered in the AWS Well-Architected Framework. OWASP guidelines
for application security still apply.

Validate and sanitize inbound events, and perform a security code review as you
normally would for non-serverless applications. For API Gateway, set up basic request
validation as a first step to ensure that the request adheres to the configured
JSON-schema request model as well as any required parameters in the URI, query string,
or headers. Application-specific deep validation should be implemented, whether that is
as a separate Lambda function, library, framework, or service.

To add protection for your code executing in Lambda runtime against any unintended and
unauthorised changes while it is moving in your CI/CD pipelines, you can add code
signature. Signing the code will confirm that it comes from a trusted source and is
unaltered. [AWS
Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) integrates with AWS Lambda to sign the code and enforce that only
trusted code is deployed into your runtime.

Store your secrets, such as database passwords or API keys, in a secrets manager that
allows for rotation, secure and audited access. Secrets Manager allows fine-grained policies
for secrets including auditing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/data-protection.html*

---

# Incident response

There are no security practices unique to serverless applications for this best
practice.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/incident-response.html*

---

# Key AWS services

Key AWS services for security are Amazon Cognito, IAM, Lambda, CloudWatch Logs, AWS CloudTrail,
AWS CodePipeline, Amazon S3, OpenSearch Service, DynamoDB, and Amazon Virtual Private Cloud (Amazon VPC).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/key-aws-services-1.html*

---

# Resources

Refer to the following resources to learn more about our best practices for security.

## Documentation and blogs

- [AWS Lambda permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html)
- [API Gateway Request Validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html)
- [API Gateway Lambda Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html)
- [Building fine-grained authorization using Amazon Cognito, API Gateway, and
IAM](https://aws.amazon.com/blogs/security/building-fine-grained-authorization-using-amazon-cognito-api-gateway-and-iam/)
- [Configuring VPC
Access for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/vpc.html)
- [Using AWS Secrets Manager with Lambda](https://aws.amazon.com/blogs/security/how-to-securely-provide-database-credentials-to-lambda-functions-by-using-aws-secrets-manager/)
- [Caching data and configuration settings with AWS Lambda extensions](https://aws.amazon.com/blogs/compute/caching-data-and-configuration-settings-with-aws-lambda-extensions/)
- [Auditing Secrets with
AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html)
- [OWASP Input validation cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [AWS Serverless Security Workshop](https://github.com/aws-samples/aws-serverless-security-workshop)
- [Code signing for Lambda](https://aws.amazon.com/blogs/aws/new-code-signing-a-trust-and-integrity-control-for-aws-lambda/)

## Whitepapers

- [Security Overview of AWS Lambda](https://docs.aws.amazon.com/whitepapers/latest/security-overview-aws-lambda/security-overview-aws-lambda.html)
- [OWASP Top Ten](https://owasp.org/www-project-top-ten/)
- [OWASP Secure Coding Best Practices](https://owasp.org/images/0/08/OWASP_SCP_Quick_Reference_Guide_v2.pdf)
- [Snyk – Commercial Vulnerability DB and Dependency
Check](https://snyk.io/)
- [Using
Hashicorp Vault with Lambda & API Gateway](https://learn.hashicorp.com/terraform/aws/lambda-api-gateway)

## Third-party tools

- [OWASP
Vulnerability Dependency Check](https://owasp.org/index.php/OWASP_Dependency_Check)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/resources-1.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
