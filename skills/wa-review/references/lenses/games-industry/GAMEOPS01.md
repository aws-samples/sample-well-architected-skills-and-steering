# GAMEOPS01 — Live operations

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# GAMEOPS01-BP01 Use game objectives and business performance metrics to develop your live operations strategy

Consult business stakeholders, such as game producers and publishing
partners, to determine objectives and performance metrics for a
game. This can assist you develop plans for how you will manage the
game, including defining your maintenance windows, software and
infrastructure update schedules, and system reliability and
recoverability goals.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

These metrics can also assist you determine at which stage of your
game's lifecycle you should incorporate a live operation steam
(Live Ops) to monitor game health, collect direct game feedback,
and build streamlined and automated release processes. For
example, a new game might wait until a certain scale is achieved,
measured by active player count, revenue, or another set of
metrics, before setting up a dedicated live operations team. An
established game development studio might already have live
operations experience, perhaps for their other games, so they'd
only need to onboard the new game.

### Implementation steps

- You may define the targets for player concurrency (CCU) and
daily and monthly active users (DAU and MAU) that the game
infrastructure should be capable to effectively support,
your infrastructure budgets, financial targets, and other
performance goals, such as the frequency for release of
content and features to increase player engagement. These
objectives and metrics feed into decisions about the game
design, release management, observability, and support that
is needed for efficient operations.
- Your game might have an objective to release new content
updates at least once each month with no downtime during
release. This information assists you to define your release
deployment strategy and coordinate the scheduling of
required maintenance that may require downtime at other
times throughout the month and contribute towards your
availability SLA.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameops01-bp01.html*

---
