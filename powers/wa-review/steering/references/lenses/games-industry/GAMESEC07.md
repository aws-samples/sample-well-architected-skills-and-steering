# GAMESEC07 — Incident response

**Pillar**: Security  
**Best Practices**: 2

---

# GAMESEC07-BP01 Implement an incident response plan to handle bad actors and abusive behavior

Create a plan of action for responding to bad actors and abusive
behavior in your game.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Consider factors such as when to
temporarily suspend or permanently ban players and how long to
disable credentials for temporarily suspended players.

**Customer example**

AnyCompany Games creates a tiered incident response system in
which minor infractions like inappropriate chat messages result in
automatic 24-hour account suspensions, while more severe
violations such as cheating or harassment trigger immediate 7-day
suspensions with mandatory review by human moderators.

Additionally, AnyCompany Games establishes escalation procedures
in which repeat offenders face progressively longer suspensions.
They create appeal processes that allow falsely flagged players to
contest automated actions while maintaining security through
identity verification requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec07-bp01.html*

---

# GAMESEC07-BP02 Ban accounts that are associated with bad actors

If left unmitigated, abusive behaviors in a game can continue to
have a negative impact on the gaming experience for others and
should be mitigated as soon as possible. Implement a process to
impose bans or other forms of restrictions on bad actors who are
confirmed to be in violation of your terms of service.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Typically, the rules and evaluation process for determining the
circumstances for imposing these types of restrictions will be
determined by personnel such as a player community team or trust
and safety team within your organization. After you've flagged bad
actors, run a pre-determined workflow to act on the identified
players.

For example,
[AWS Step Functions](https://aws.amazon.com/step-functions/) and
[AWS Lambda](https://aws.amazon.com/lambda/) functions can be used to run an automated workflow
that accepts a batch of player accounts as input. The workflow
then updates entries in an
[Amazon DynamoDB](https://aws.amazon.com/dynamodb) table called Bans, which can include details about
the player account, the ban reason, and duration.

Depending on the design of your game and account management system
and the type of abuse that you encounter from bad actors, maintain
a banning system of record that is separate from your account
management system. You may not want to turn off the player's
account from your account management system, opting instead to
simply turn off their ability to play your game. This can be useful
in situations where the player's account credentials are used to
access multiple games with different terms of service or policies.

### Implementation steps

- Define and enforce policies for responding to abusive
behaviors from bad actors.
- Use AWS services to automate your responses to bad actors.

### Resources

- [AWS Security Incident Response Technical Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html)
- [AWS Machine Learning Blog: Detect real and live users and deter
bad actors using Amazon Rekognition Face Liveness](https://aws.amazon.com/blogs/machine-learning/detect-real-and-live-users-and-deter-bad-actors-using-amazon-rekognition-face-liveness/)
- [AWS Solutions for Games: Community Health](https://aws.amazon.com/solutions/games/community-health/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec07-bp02.html*

---
