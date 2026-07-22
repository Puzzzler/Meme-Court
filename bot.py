import os

import discord
from discord import app_commands
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Get our Discord bot token
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN was not found. Check that your .env file exists "
        "and contains DISCORD_TOKEN=your_token_here"
    )

# Tell Discord what information we want to receive
intents = discord.Intents.default()

# Create our bot client
client = discord.Client(intents=intents)

# Create a command tree for slash commands
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}!")


@tree.command(name="ping", description="Check whether the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong")

client.run(TOKEN)