# GAMESOPS04 — Health monitoring

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GAMESOPS04-BP01 Instrument the game to detect and monitor player-impacting issues

In addition to responding to social media and player reports of
issues, instrument your game with monitoring solutions to detect
and investigate player-impacting issues.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

No amount of testing can identify every issue in a game. Games are
usually launched with known issues that are planned to be
gradually fixed with the next release of the game. Known and
reproducible issues are straightforward to address and fix. To
assist with identifying such issues, game clients should implement
player activity tracking, app logging, and reporting in various
strategic places to assist the backend team identify client-side
issues. The ability to find such issues early assists the game
developers troubleshoot and fix the issue before it becomes
widespread. The data and logs reported by the tracking code should
never include personally identifiable information (PII), and they
should only contain game specific metadata that assist with
debugging.

Implement an observability solution for detecting and responding
to issues such as game crashes or bugs. You can
use [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to create canaries that can monitor
the health of your player-facing backend game services. You can
instrument your backend services with
[AWS X-Ray](https://aws.amazon.com/xray/) to
trace requests across distributed services, and send your custom
logs and metrics
to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/).

Third-party solutions, such as
[Backtrace.io](http://Backtrace.io/) and
[Sentry](https://sentry.io/welcome/), are
popular solutions for error reporting in games. Application
performance monitoring (APM) solutions from partners such
as [New Relic](https://newrelic.com/),
[Splunk](https://www.splunk.com/en_us/devops/application-performance-monitoring.html),
[Datadog](https://www.datadoghq.com/product/apm/),
and [Honeycomb.io](http://Honeycomb.io/)
are also popular.

The game's live operations team and community managers should also
monitor various social networks and channels to check for player
feedback, complaints, and bug reports in addition to the official
support channels. Review and attempt to reproduce every
game-specific complaint, or send them to the QA team for review.
If reproducible, escalate the issue to the game developers for
their troubleshooting and a fix before it impacts the larger
player base.

### Implementation steps

- **Implement monitoring
solutions:** Use monitoring tools to detect
player-impacting issues and respond quickly.
- **Track player activity and
logs:** Instrument game clients to log player
activity and report issues, and verify that no personally
identifiable information (PII) is included.
- **Use third-party and AWS
tools:** Use tools like CloudWatch, X-Ray, and
third-party solutions for error reporting and performance
monitoring, and monitor social media for player feedback and
bug reports.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesops04-bp01.html*

---
