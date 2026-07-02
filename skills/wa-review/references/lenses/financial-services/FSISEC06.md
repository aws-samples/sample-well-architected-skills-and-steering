**Pillar**: Security

# FSISEC06: How do you address emerging threats?

Security-focused enterprises are improving threat
identification and remediation with DevSecOps. This approach
accelerates application development and identifies threats
early, and security testing is performed at each step of the
software development lifecycle. Applying a DevSecOps framework
is critical for an FI's software development, meeting the
needs of a rapidly-changing product and a highly regulated
environment.

Emerging threats now include AI-specific concerns such as
prompt injection, model manipulation, harmful model responses,
and excessive agency risks from autonomous AI systems.
Integrate AI-specific vulnerability scanning into CI/CD
pipelines.

## FSISEC06-BP01 Automate remediation of common vulnerabilities and exposures (CVEs)

Scanning servers for common vulnerabilities is a
long-standing best practice. However, in the cloud, you
should not only automate the evaluation of operating
environments and applications, but also remediate known and
emerging security vulnerabilities automatically. For
example, you can use
[Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) service to automatically scan
servers in production, publish security findings to an Amazon Simple Notification Service (SNS) topic, run an AWS Lambda
function from those notifications to examine the findings, and
implement the appropriate remediation based on the type of
issue.

For generative AI systems, implement automated response
validation through multiple complementary patterns with
custom code validation using AWS Lambda with input and
output validation logic and AWS Step Functions for
orchestrated validation workflows. Consider LLM-as-a-judge
where a specialized model (like Amazon Nova Premier)
evaluates primary responses for safety and accuracy. Use
Amazon Bedrock Guardrails with built-in content filters,
prompt injection detection, and contextual grounding checks
that can be applied at both input and output stages.

## FSISEC06-BP02 Perform static analysis on all code deploys

As part of a DevSecOps strategy, you can secure your
application deployments by integrating preventive and
detective security controls within the pipeline. One of the
key benefits of static code analysis is that you can learn
about security vulnerabilities prior to provisioning AWS
resources, which can help reduce costs and risk.

## FSISEC06-BP03 Conduct regular penetration testing

Simulating security incidents inside the AWS environment helps
you have a better understanding of your security posture.
Financial services organizations perform penetration testing
of web applications most often when a new application is
launched or when it's first migrated to the cloud. Some may
even conduct penetration testing periodically every year. Run
penetration testing regularly after every major release that
involves significant re-architecture changes. Major releases
might introduce vulnerabilities that didn't exist earlier.

## FSISEC06-BP04 Deploy web application firewalls

[AWS WAF](https://aws.amazon.com/waf/) is an application firewall service for
HTTP applications that applies a set of rules to an HTTP
conversation. You can buy managed rule sets from the AWS Marketplace that protect against application vulnerabilities,
such as the Open Worldwide Application Security Project
([OWASP
Top 10](https://aws.amazon.com/marketplace/pp/prodview-p77unujkxrg7g)), bots, or emerging CVEs. Managed rules are
automatically updated by AWS Marketplace security sellers.

### Prescriptive guidance

- Automation is key to maintain continuous vulnerability
management and a remediation posture. For details, see
[Automate vulnerability management and remediation in
AWS](https://aws.amazon.com/blogs/mt/automate-vulnerability-management-and-remediation-in-aws-using-amazon-inspector-and-aws-systems-manager-part-1/).
- Application modernization leads to containerized
applications. You can deploy vulnerability management
into your CI/CD pipeline and scan container images. For
more details, see
[Use Amazon Inspector to manage your build and deploy pipelines for containerized applications](https://aws.amazon.com/blogs/security/use-amazon-inspector-to-manage-your-build-and-deploy-pipelines-for-containerized-applications/).
- From a shift left approach, apply vulnerability
management in your CI/CD pipeline. For more details, see
[Detect security vulnerabilities and automate code reviews](https://aws.amazon.com/blogs/devops/automating-detection-of-security-vulnerabilities-and-bugs-in-ci-cd-pipelines-using-amazon-codeguru-reviewer-cli/).

## Resources

**Related documents:**

- [Penetration
Testing at AWS](https://aws.amazon.com/security/penetration-testing/)
- [Detect Python and Java code security vulnerabilities with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/detect-python-and-java-code-security-vulnerabilities-with-codeguru-reviewer/)
- [Amazon Inspector FAQs](https://aws.amazon.com/inspector/faqs/)

**Related videos:**

- [AWS re:Invent 2022 - Detect vulnerabilities in AWS Lambda functions using Amazon Inspector](https://www.youtube.com/watch?v=gWoJqnRB3MA&ab_channel=AWSEvents)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisec06.html*
