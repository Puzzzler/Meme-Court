import os

import discord
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Get our Discord bot token
TOKEN = os.getenv("DISCORD_TOKEN")

# Tell Discord what information we want to receive
intents = discord.Intents.default()

# Create our bot client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}!")


client.run(TOKEN)