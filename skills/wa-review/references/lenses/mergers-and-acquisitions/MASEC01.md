# MASEC01 — Security

**Pillar**: Security  
**Best Practices**: 5

---

## MASEC01-BP01 Use a centralized identity provider

At any given time, you can have only one directory or one SAML 2.0 identity provider connected to IAM Identity Center. But, you can change the identity source that is connected to a different one.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP02 Use a common authorization approach

Companies may have a very different approach to authorization. Companies need to use a common authorization platform and develop consistent authorization policies for the combined systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP03 Use AWS temporary credentials

You can use the AWS Security Token Service to create and provide trusted users with temporary security credentials that can control access to your AWS resources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP04 Store and use secrets securely

Use AWS Secrets Manager to replace hardcoded credentials in your code, including passwords, with an API call to Secrets Manager to retrieve the secret programmatically. The secret can't be compromised by someone examining your code because the secret no longer exists in the code.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

## MASEC01-BP05 Create a common policy for auditing and rotating credentials

Rotation is the process of periodically updating a secret. When you rotate a secret, you update the credentials in both the secret and the database or service. In Secrets Manager, you can set up automatic rotation for your secrets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/mergers-and-acquisitions-lens/masec-1.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
