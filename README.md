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

Open `.env` and replace the value with your Discord bot token:

```text
DISCORD_TOKEN=your_bot_token_here
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

