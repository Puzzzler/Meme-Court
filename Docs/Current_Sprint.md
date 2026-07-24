# Sprint 3: Persistent Case Files

## Goal

Store known meme submissions and each member's current vote in SQLite so Reaction Jury keeps its court record across restarts.

## Data Rules

- SQLite stores known eligible meme submissions.
- SQLite stores each human member's current vote.
- A member may have only one stored vote per meme.
- Switching votes updates the existing vote.
- Removing a vote deletes that user's stored vote.
- Discord reactions remain the source of truth for visible reactions.
- Sprint 3 does not need to recover reaction events that happened while the bot was offline.
- Reward and punishment state will be added when those features are implemented.
- created_at and updated_at are stored in UTC.


## Build Tasks

- [ ] Create the SQLite database automatically if it does not exist.
- [ ] Create a `memes` table.
- [ ] Store message ID, guild ID, channel ID, author ID, and created time.
- [ ] Create a `votes` table.
- [ ] Store message ID, user ID, current vote, and updated time.
- [ ] Enforce one vote row per user per meme.
- [ ] Save eligible meme submissions when they are posted.
- [ ] Save new votes.
- [ ] Update stored votes when members switch.
- [ ] Delete stored votes when members remove them.
- [ ] Preserve records across bot restarts.
- [ ] Log database errors clearly.

## Acceptance Checks

- [ ] Posting an eligible meme creates one meme record.
- [ ] Adding a vote creates one vote record.
- [ ] Switching votes updates the existing record instead of creating a second one.
- [ ] Removing a vote removes that vote record.
- [ ] Restarting Reaction Jury preserves known memes.
- [ ] Restarting Reaction Jury preserves known votes.
- [ ] Repeated events do not create duplicate meme records.
- [ ] A user cannot have two stored votes for the same meme.
- [ ] Database errors do not crash the bot without a useful log.

## Not Part of Sprint 3

- Recovering votes cast while Reaction Jury was offline.
- Reward/punishment tracking.
- Monthly reports.
- Vote history/audit trail.
- Multi-server database architecture.

## Codex Checkpoint

Ask Codex to propose the SQLite schema only.

Review and approve:
- tables
- columns
- data types
- primary keys
- foreign keys
- UNIQUE constraints
- indexes

Do not allow implementation until the schema is approved.

## Suggested Commit

Complete Sprint 3: Persistent Case Files

## Sprint 3 Data Decisions

- Keep meme and vote records indefinitely unless an admin intentionally purges them.
- Store individual current votes, not aggregate vote counts.
- Calculate meme score as thumbs-up minus thumbs-down when needed.
- Do not store derived score totals in the database.
- Meme authors may vote on their own submissions.
- Discord reactions remain the source of truth for visible current reactions.
- SQLite preserves the bot's known court record across restarts.
- Sprint 3 does not need to recover reactions that happened while the bot was offline.
- Monthly reports will query memes by their creation timestamps.
- Best and worst meme should be based on net score, not raw thumbs-up count.
- Monthly results should eventually become final once the month closes.
- A future `monthly_results` record can freeze those historical winners.
- Deleted Discord memes should eventually remain in the court record rather than disappearing from history.
- Meme persistence begins with submissions observed after Sprint 3 is deployed. Historical backfill is not required.

## Design Notes

- Store timestamps as UTC ISO-8601 text.
- Meme created_at comes from Discord's message timestamp.
- Enable SQLite foreign-key enforcement on every database connection.
- Existing pre-Sprint-3 test memes do not need to be imported.
- The runtime database file is not committed to Git.
- Query SQLite as needed; loading the entire database into memory at startup is not required.