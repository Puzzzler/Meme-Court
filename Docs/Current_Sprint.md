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



## Codex Prompt for Sprint 2

Review the following Sprint 2 voting rules and generate test cases only.

Do not edit any files and do not write implementation code.

For each test case, provide:
1. Starting state
2. User action
3. Expected visible Discord reactions
4. Expected bot action
5. Expected terminal log
6. Any permissions, cache, reconnect, or race-condition risk

Rules:
- Only thumbs-up and thumbs-down are voting reactions.
- Only humans may vote.
- Meme authors may vote on their own submission.
- Every human member gets one vote per eligible meme.
- A member may hold only one vote per meme.
- Adding the opposite reaction switches the vote.
- Removing the current reaction clears the vote.
- Other emojis are ignored and left untouched.
- Rules apply only to eligible uploaded-image meme posts in the configured meme channel.
- GIF uploads and text-only posts are not eligible.
- Discord reactions are the source of current vote state.
- No persistence is required until Sprint 3.