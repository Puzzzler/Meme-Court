# Reaction Jury

## Vision

What problem are we solving?

One or two paragraphs.

---

# Core Gameplay

Describe the experience from a user's perspective.

Example:

1. User posts meme.
2. Jury convenes.
3. Community votes.
4. Verdict reached.
5. Rewards or punishment issued.
6. Monthly Hall of Fame.

---

# Design Philosophy

Examples:

- Funny before serious.
- Simple to use.
- Community driven.
- No unnecessary admin work.
- Feels like a game.
- Courtroom theme everywhere.

---

# Features

## MVP

- Auto reactions
- Vote counting
- Threshold detection
- Meme Jail
- Certified Meme
- Monthly winners

---

## Future Features

Ideas that are NOT part of MVP.

Examples:

- Appeals
- Jury summons
- Daily challenges
- Streaks
- Leaderboards
- Web dashboard
- AI generated verdicts

---

# User Flow

Post meme
    ↓
Bot reacts
    ↓
People vote
    ↓
Threshold reached?
    ↓
No ────────────────┐
                   │
Yes                │
↓                  │
Verdict            │
↓                  │
Role/Jail          │
↓                  │
Monthly statistics

---

# Roles

## User

Can:
- Post memes
- Vote

Cannot:
- Vote twice

---

## Moderator

Can:
- Override verdict
- Release Meme Jail
- Configure thresholds

---

# Configuration

Channel IDs

Roles

Thresholds

Timers

---

# Commands

/user

/admin

/debug

---

# Database

Users

Messages

Votes

Awards

Punishments

Settings

---

# Edge Cases

Examples:

Delete meme after verdict.

Delete meme before verdict.

Bot restart.

Reaction removed.

Reaction changed.

Role already exists.

Moderator posts meme.

Bot lacks permissions.

---

# Roadmap

Sprint 0

Sprint 1

Sprint 2

Sprint 3

...

---

# Parking Lot

Ideas we like but aren't building yet.

Never delete ideas.

Move them into sprints later.

- Court stenographer messages

- Random jury quotes

- Appeal system

- Community pardon vote

- Anonymous jury mode

- Golden Gavel award

- Prosecutor vs Defense events

- Emoji animations

- AI writes the verdict

- Seasonal events

- Holiday themes
- Use monthly 'wall of fame' on other text channels (for example: the hobby text channel, it will post on the main discord text channel the highest reaction post so the discord can discover other text channels)
- A public leaderboard command.
- Meme streaks and achievements.
- A Judge or Jury Duty role.
- Anonymous monthly nominations.
- A web dashboard.
- Multiple meme channels or server support.
- Custom court-themed messages and random verdict lines.
- Ties are handled by the monthly meme king winner when a meme has both the same number of thumbs up and thumbs down. (Could be more exciting if the tie breaker is asked "even or odd" and says one and then the bot rolls a dice and if it matches what the tie breaker said the meme is saved, and if not the meme poster gets the punishment)
- Detect eligible meme posts and ignore ordinary conversation. (implemented into Sprint 1)
- Give users that post memes fake currenacy or a total score of 'thumbs up reactions - thumbs down reactions = total score' and that is one way we can handle the leaderboard.


---

# Questions

Things we haven't decided yet.

Examples:

Should downvotes expire?

Can punishments stack?

Can multiple verdicts exist?

Should admins be immune? - (no)
Bot stops looking at posts after an extended period of time so that it won't forever check posts
Positive threshold: __10____ 👍
Negative threshold: ___10___ 👎
Minimum votes for monthly awards: __10____
Voting window per meme: ______ hours/days
Deliberation delay: none / ______ minutes
Can one person hold both 👍 and 👎? no (if we allow them to have both we might have more ties on memes)
Positive reward role and duration: ____________________
Monthly report day and time: ____1st day of the month at 9am CST________________
Tie-break rule: most positive votes / earliest post / other: ____________________

---

# Decisions Log

Date

Decision

Reason

Example:

2026-07-21

Use Meme Jail instead of Discord timeout. (current theory is giving them a temporary role that can't post in meme court channel for 4 hours)

Reason:
Less disruptive and funnier.

Decision:
Sprint 1 meme eligibility is limited to uploaded image attachments.

Reason:
Prevents casual conversation from being judged and keeps the meme channel focused on actual meme posts.

# Not Yet

- Docker

- Web dashboard

- Database optimization

- Multiple servers

- Localization

- Metrics

- Unit tests

- CI/CD