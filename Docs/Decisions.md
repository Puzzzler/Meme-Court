# Decisions We Won't Revisit

✅ Meme Jail instead of Discord timeout.

Reason:
Funnier, less disruptive.

---

✅ Courtroom theme.

Reason:
Makes the bot memorable.

---

✅ SQLite for MVP.

Reason:
Simple and reliable.


Decision:
Allow meme authors to vote on their own submissions.

Reason:
Reaction Jury is a fun community feature, not a strict election system. Allowing one self-vote keeps the rules simpler, encourages engagement, and removes unnecessary special-case logic.

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