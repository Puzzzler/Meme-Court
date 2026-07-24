A practical build plan for the meme courtroom Discord bot
Project vision: Members post memes in one dedicated channel. Reaction Jury adds 👍 and 👎, tracks voting, rewards successful memes, sends failed memers to a channel-only Meme Jail, and publishes monthly best-and-worst awards.
How to use this blueprint
•	Work on one sprint at a time. Do not begin the next sprint until the current sprint's acceptance checks pass.
•	Keep each change small enough to understand and test.
•	At the end of every sprint: test it, run git status, commit it, and write one sentence about what you learned.
•	Codex is a coding partner, not an autopilot. Ask it to explain plans and proposed changes before accepting them.
Definition of Done for Every Sprint
•	The feature works in the personal test server.
•	The bot handles the obvious failure case without crashing.
•	Secrets such as the Discord token are not committed.
•	Code is committed to Git with a meaningful message.
•	README notes are updated when setup or behavior changes.
Sprint 0: Foundation and Safety
Goal: Confirm the project is safe, reproducible, and ready for feature work.
Build tasks
☐ Confirm the bot still logs in and /ping works.
☐ Confirm .env and .venv are ignored by Git.
☐ Confirm requirements.txt contains discord.py and python-dotenv.
☐ Add a simple startup check that reports a missing token clearly instead of failing mysteriously.
☐ Create a short README section explaining how to activate the virtual environment and run the bot.
Acceptance checks
☐ A fresh terminal can activate .venv and run python bot.py.
☐ /ping replies successfully.
☐ git status does not show .env or .venv.
Codex checkpoint: First Codex practice: ask Codex to review the project structure only. Prompt it to identify risks and propose a plan without editing files.
Suggested commit: "Complete Sprint 0: Foundation and Safety"


Sprint 1: Open Meme Court
Goal: When a member posts in the meme channel, automatically add 👍 and 👎.
Build tasks
☐ Enable the Discord intents needed to receive new-message events.
☐ Store the meme channel ID in .env.
☐ Listen for new messages.
☐ Ignore messages outside the meme channel.
☐ Ignore messages created by bots.
☐ Add 👍 and 👎 reactions to eligible posts.
Acceptance checks
☐ A human post in the meme channel receives exactly the two jury reactions.
☐ A post in another channel receives nothing.
☐ The bot does not react to its own messages.
Codex checkpoint: Ask Codex to implement this sprint from a written acceptance checklist. Review its diff before applying it, then ask it to explain every changed line in plain English.
Suggested commit: "Complete Sprint 1: Open Meme Court"


# Sprint 2: Basic Voting Rules

## Goal

Treat thumbs-up and thumbs-down as valid votes while preventing obvious vote abuse.

## Voting Rules

- Only thumbs-up and thumbs-down are voting reactions.
- Only human reactions count.
- Meme authors may vote on their own submission.
- Every human member gets one vote per eligible meme.
- A member may hold only one vote per meme.
- Adding the opposite reaction switches the member's vote.
- Removing the current reaction clears the member's vote.
- Other emojis are left untouched.
- Rules apply only to eligible Sprint 1 meme submissions.
- Discord reactions are the source of current vote state.
- No database persistence is required until Sprint 3.

## Build Tasks

- [ ] Detect raw reaction additions.
- [ ] Detect raw reaction removals.
- [ ] Ignore reactions from bots.
- [ ] Ignore reactions other than thumbs-up and thumbs-down.
- [ ] Confirm the reacted message is an eligible meme submission.
- [ ] Remove the user's opposite vote when switching.
- [ ] Log useful vote activity during development.
- [ ] Handle deleted messages and missing permissions without crashing.

## Acceptance Checks

- [ ] The bot's starter reactions are not treated as votes.
- [ ] Other bots' reactions are ignored.
- [ ] A member cannot visibly hold both voting reactions.
- [ ] Adding the opposite reaction switches the vote.
- [ ] Removing the current reaction clears the vote.
- [ ] Unrelated emoji reactions remain untouched.
- [ ] The bot survives missing messages and permission errors.
- [ ] Restarting the bot does not remove existing Discord reactions.

## Codex Checkpoint

Give Codex the finalized voting rules and ask it to generate test cases and edge cases only. Do not allow file edits yet.

## Suggested Commit

Complete Sprint 2: Basic Voting Rules


Sprint 3: Persistent Case Files
Goal: Save meme and voting information so a restart does not erase the court record.
Build tasks
☐ Create a small SQLite database.
☐ Store message ID, author ID, channel ID, created time, and message link.
☐ Store each user's current vote.
☐ Store whether a reward or punishment has already happened.
☐ Load existing records after the bot restarts.
Acceptance checks
☐ Restarting the bot does not lose known memes or votes.
☐ A member cannot gain duplicate votes by reacting before and after a restart.
☐ Database errors are logged clearly.
Codex checkpoint: Ask Codex to propose the database schema first. Approve the tables and columns before allowing implementation.
Suggested commit: "Complete Sprint 3: Persistent Case Files"


Sprint 4: Verdicts and Thresholds
Goal: Trigger a verdict when a meme reaches configured positive or negative thresholds.
Build tasks
☐ Put thresholds in environment variables or a configuration section.
☐ Calculate 👍 count, 👎 count, and net score.
☐ Trigger each verdict only once per meme.
☐ Post a themed verdict message that links to the original meme.
☐ Add an optional 30-minute deliberation delay before the final verdict.
Acceptance checks
☐ The same meme cannot reward or punish its author twice.
☐ Changing votes during deliberation affects the final result.
☐ A tie or no-longer-met threshold produces no incorrect verdict.
Codex checkpoint: Have Codex write a small pure-Python verdict function and unit tests before connecting it to Discord events.
Suggested commit: "Complete Sprint 4: Verdicts and Thresholds"


Sprint 5: Rewards and Meme Jail
Goal: Give successful memers a reward and temporarily block failed memers from posting in the meme channel.
Build tasks
☐ Create or identify the reward role.
☐ Create or identify a Meme Jail role.
☐ Configure the meme channel so Meme Jail cannot send messages there.
☐ Award the positive role for a chosen duration.
☐ Apply Meme Jail for four hours.
☐ Automatically remove temporary roles when their time expires.
☐ Never punish administrators, moderators, or protected roles.
Acceptance checks
☐ The reward role is assigned and later removed.
☐ Meme Jail blocks only the meme channel, not the entire server.
☐ The jailed user regains access automatically after four hours.
☐ Protected users cannot be jailed.
Codex checkpoint: Ask Codex to review permission and role-order risks. Do not let it change server permissions automatically; use it to guide the manual Discord setup.
Suggested commit: "Complete Sprint 5: Rewards and Meme Jail"


Sprint 6: Admin Controls
Goal: Give trusted staff safe ways to inspect and correct the bot.
Build tasks
☐ Add /jury status for one meme.
☐ Add /jury config to display current thresholds and channel settings.
☐ Add /jury pardon to remove Meme Jail.
☐ Add /jury recalculate for recovery after mistakes.
☐ Restrict admin commands to approved roles or Discord permissions.
Acceptance checks
☐ Regular members cannot use staff commands.
☐ Admin actions create a visible audit message or terminal log.
☐ Invalid message links and missing records return friendly errors.
Codex checkpoint: Ask Codex to generate slash-command skeletons only, then fill in one command at a time together.
Suggested commit: "Complete Sprint 6: Admin Controls"


Sprint 7: Monthly Meme Court Report
Goal: Automatically announce the month's highest- and lowest-rated eligible memes.
Build tasks
☐ Define the reporting period and time zone.
☐ Require a minimum number of human votes to qualify.
☐ Rank by net score, with explicit tie-break rules.
☐ Post links to the best and worst meme.
☐ Assign temporary King of the Memes and Trash Memer roles.
☐ Remove the previous month's title roles.
☐ Prevent the report from posting twice.
Acceptance checks
☐ The selected memes come from the correct month.
☐ Deleted or inaccessible messages are handled gracefully.
☐ Tie-break behavior is consistent.
☐ Monthly roles move to the new winners correctly.
Codex checkpoint: Ask Codex to create sample meme data and verify the ranking logic before enabling the real monthly schedule.
Suggested commit: "Complete Sprint 7: Monthly Meme Court Report"


Sprint 8: Production Readiness
Goal: Prepare the bot for the larger Discord server and unattended operation.
Build tasks
☐ Move server-specific settings into configuration.
☐ Add structured logging and useful error messages.
☐ Add startup validation for channel IDs, role IDs, and permissions.
☐ Test missing roles, deleted messages, restarts, and Discord outages.
☐ Choose hosting and configure automatic restarts.
☐ Back up the SQLite database.
☐ Write an owner runbook: start, stop, update, restore, and troubleshoot.
Acceptance checks
☐ The bot restarts without losing data.
☐ A bad configuration fails clearly and safely.
☐ The larger server's moderators understand the rules and recovery steps.
Codex checkpoint: Use Codex as a release reviewer. Ask it to audit the repository for security, reliability, configuration, and missing documentation.
Suggested commit: "Complete Sprint 8: Production Readiness"



Initial Product Decisions to Make
☐ Positive threshold: __10____ 👍
☐ Negative threshold: ___10___ 👎
☐ Minimum votes for monthly awards: __10____
☐ Voting window per meme: ______ hours/days
☐ Deliberation delay: none / ______ minutes
☐ Can one person hold both 👍 and 👎? yes / no
☐ Positive reward role and duration: ____________________
☐ Monthly report day and time: ____________________
☐ Tie-break rule: most positive votes / earliest post / other: ____________________


Parking Lot: Later Ideas
☐ A public leaderboard command.
☐ Meme streaks and achievements.
☐ A Judge or Jury Duty role.
☐ Anonymous monthly nominations.
☐ A web dashboard.
☐ Multiple meme channels or server support.
☐ Custom court-themed messages and random verdict lines.
