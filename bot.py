import os

import discord
from discord import app_commands
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Get configuration values
TOKEN = os.getenv("DISCORD_TOKEN")
meme_channel_id_text = os.getenv("MEME_CHANNEL_ID")

if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN was not found. Check that your .env file contains DISCORD_TOKEN."
    )

if not meme_channel_id_text:
    raise RuntimeError(
        "MEME_CHANNEL_ID was not found. Add the meme-court channel ID to your .env file."
    )

try:
    MEME_CHANNEL_ID = int(meme_channel_id_text)
except ValueError as error:
    raise RuntimeError("MEME_CHANNEL_ID must contain only numbers.") from error

# Tell Discord what information we want to receive
intents = discord.Intents.default()
intents.message_content = True

# Create our bot client
client = discord.Client(intents=intents)

# Create a command tree for slash commands
tree = app_commands.CommandTree(client)

VOTE_REACTIONS = ("\N{THUMBS UP SIGN}", "\N{THUMBS DOWN SIGN}")
PING_RESPONSE = "\N{TABLE TENNIS PADDLE AND BALL} Pong"
SUPPORTED_IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


def is_supported_image_upload(attachment: discord.Attachment) -> bool:
    content_type = attachment.content_type or ""

    if content_type == "image/gif":
        return False

    if content_type.startswith("image/"):
        return True

    return attachment.filename.lower().endswith(SUPPORTED_IMAGE_EXTENSIONS)


def is_meme_submission(message: discord.Message) -> bool:
    return any(is_supported_image_upload(attachment) for attachment in message.attachments)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}!")
    print(f"Watching meme channel: {MEME_CHANNEL_ID}")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.channel.id != MEME_CHANNEL_ID:
        return

    if not is_meme_submission(message):
        return

    try:
        for reaction in VOTE_REACTIONS:
            await message.add_reaction(reaction)
    except discord.Forbidden:
        print("Reaction Jury does not have permission to add reactions.")
    except discord.HTTPException as error:
        print(f"Discord could not add the reactions: {error}")


@tree.command(name="ping", description="Check whether the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(PING_RESPONSE)


client.run(TOKEN)
