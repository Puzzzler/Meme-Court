# Reaction Jury

A Discord bot that lets the community vote on memes and delivers hilarious verdicts.

---

## Requirements

- Python 3.14
- Git

---

## First-Time Setup

Clone the repository.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Copy the example configuration:

```powershell
copy .env.example .env
```

Open `.env` and add your Discord bot token and the numeric ID of the meme channel:

```text
DISCORD_TOKEN=your_bot_token_here
MEME_CHANNEL_ID=123456789012345678
```

---

## Running the Bot

Start the bot:

```powershell
python bot.py
```

Stop the bot with:

```text
Ctrl+C
```

## Discord Configuration

In the Discord Developer Portal:

1. Open the bot application's **Bot** settings.
2. Enable **Message Content Intent**.
3. Invite the bot with the `bot` and `applications.commands` scopes.
4. Give the bot permission to:
   - View the meme channel
   - Read message history
   - Add reactions

## Sprint 1 Behavior

- Human image uploads in the configured meme channel receive thumbs-up and thumbs-down voting reactions.
- Text-only posts and GIF uploads do not receive voting reactions.
- Posts outside the configured meme channel do not receive voting reactions.
