# GAMEPERF08 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GAMEPERF08-BP01 Inform and include the player in your process

Provide an option to display in game metrics like latency, frames
per second and dropped packets. Surface infrastructure issues and
maintenance downtime through player facing communication like
status pages. Celebrate new game locations with player comms
including dev blogs and set expectations for expected player
experience improvements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Include the player**

Provide a simple diagnostic submission process that collects
relevant files and attaches them to a player support ticket from
your game client. Enable a support forum where players can help
each other and become a part of improving the game experience

**Consider trade-offs versus player
expectations**

Moving backend systems for cost efficiency may not be noticeable
to players but moving game servers can change ping time. Be
consistent and fair to players with reasoning for expansion and
reduction of your game hosting locations.

Player communities and geographies will have their own
characteristics that may impact expectations of your game. For
example, South Korea has some of the fastest internet on the
planet and the expectation for gameplay is single digit latency
which drives highly competitive play. Casual gameplay on mobile
devices creates a different performance profile and use pattern in
comparison to console and PC session play.

Login and lobby are a part of the experience and should feel
responsive, even if the server is offline for maintenance. Raid
night planning or hanging out in the lobby is part of the player
experience and is important to consider when choosing focus areas
for performance efficiency. Players may leave your game client
open for months, sometimes they may just log in occasionally to
read the patch notes. A Live Ops game needs to keep the entire
player experience in mind as a part of engineering process and
culture.

### Implementation steps

- Provide in-game metrics such as latency, FPS, and packet
loss, and communicate infrastructure issues and maintenance
schedules via status pages and player-facing updates.
- Implement a diagnostic dump and submission feature in the
game client and create a support forum to foster
community-driven troubleshooting and improvement.
- Tailor performance optimizations to player community
expectations, such as low latency for competitive Regions or
responsive login/lobby experiences for casual and
long-session players.
- Design Live Ops workflows to account for the entire player
experience, from active gameplay to idle client behavior,
facilitating seamless engagement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf08-bp01.html*

---

# GAMEPERF08-BP02 Align solution selection with engineering team skills and expertise

Assess your team's skills and expertise in managing and optimizing
game server performance when choosing your hosting option.
Self-hosted solutions like EC2 and containers require more
knowledge of infrastructure management, performance tuning, and
scaling. If your team lacks these skills, a managed service like
GameLift may be more suitable, as it abstracts away many of the
complexities and allows your team to focus on game-specific
optimizations.

**Level of risk exposed if this best
practice is not established: High**

## Implementation guidance

By evaluating these factors and conducting performance tests
across different hosting options, you can select the most
appropriate solution that meets your game's specific requirements
while optimizing for performance efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gameperf08-bp02.html*

---
