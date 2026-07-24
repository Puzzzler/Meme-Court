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

# Tracks reaction removals initiated by Reaction Jury itself.
# This prevents a vote switch from also being logged as a normal vote removal.
BOT_REMOVALS: set[tuple[int, int, str]] = set()


def is_supported_image_upload(attachment: discord.Attachment) -> bool:
    content_type = attachment.content_type or ""

    if content_type == "image/gif":
        return False

    if content_type.startswith("image/"):
        return True

    return attachment.filename.lower().endswith(SUPPORTED_IMAGE_EXTENSIONS)


def is_meme_submission(message: discord.Message) -> bool:
    return any(
        is_supported_image_upload(attachment)
        for attachment in message.attachments
    )


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


@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    # Always ignore Reaction Jury's own starter reactions.
    if client.user and payload.user_id == client.user.id:
        return

    # Ignore reactions from other bots when Discord gives us the member object.
    if payload.member and payload.member.bot:
        return

    if str(payload.emoji) not in VOTE_REACTIONS:
        return

    if payload.channel_id != MEME_CHANNEL_ID:
        return

    channel = client.get_channel(payload.channel_id)

    if channel is None:
        try:
            channel = await client.fetch_channel(payload.channel_id)
        except discord.NotFound:
            print(f"Channel not found: channel={payload.channel_id}")
            return
        except discord.Forbidden:
            print(f"Could not access channel: channel={payload.channel_id}")
            return
        except discord.HTTPException as error:
            print(f"Could not fetch channel: {error}")
            return

    if not isinstance(channel, discord.TextChannel):
        return

    try:
        message = await channel.fetch_message(payload.message_id)
    except discord.NotFound:
        print(f"Skipped reaction: message not found message={payload.message_id}")
        return
    except discord.Forbidden:
        print(
            f"Could not verify reaction: missing access "
            f"message={payload.message_id}"
        )
        return
    except discord.HTTPException as error:
        print(f"Could not fetch reaction message: {error}")
        return

    if not is_meme_submission(message):
        return

    current_vote = str(payload.emoji)

    if current_vote == VOTE_REACTIONS[0]:
        opposite_vote = VOTE_REACTIONS[1]
    else:
        opposite_vote = VOTE_REACTIONS[0]

    opposite_reaction = discord.utils.get(
        message.reactions,
        emoji=opposite_vote,
    )

    if opposite_reaction:
        try:
            async for user in opposite_reaction.users():
                if user.id == payload.user_id:
                    removal_key = (
                        payload.message_id,
                        payload.user_id,
                        opposite_vote,
                    )

                    BOT_REMOVALS.add(removal_key)

                    try:
                        await message.remove_reaction(opposite_vote, user)
                    except discord.Forbidden:
                        BOT_REMOVALS.discard(removal_key)
                        print(
                            f"Could not switch vote: missing permissions "
                            f"message={payload.message_id} user={payload.user_id}"
                        )
                        return
                    except discord.HTTPException as error:
                        BOT_REMOVALS.discard(removal_key)
                        print(f"Could not switch vote: {error}")
                        return

                    print(
                        f"Vote switched: user={payload.user_id} "
                        f"message={payload.message_id} "
                        f"from={opposite_vote} to={current_vote}"
                    )
                    return

        except discord.HTTPException as error:
            print(
                f"Could not check existing votes: "
                f"message={payload.message_id} error={error}"
            )
            return

    print(
        f"Vote added: user={payload.user_id} "
        f"message={payload.message_id} "
        f"vote={current_vote}"
    )


@client.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent):
    if str(payload.emoji) not in VOTE_REACTIONS:
        return

    if payload.channel_id != MEME_CHANNEL_ID:
        return

    removal_key = (
        payload.message_id,
        payload.user_id,
        str(payload.emoji),
    )

    # If Reaction Jury caused this removal during a vote switch,
    # don't log it as though the user manually removed their vote.
    if removal_key in BOT_REMOVALS:
        BOT_REMOVALS.discard(removal_key)
        return

    try:
        user = await client.fetch_user(payload.user_id)
    except discord.NotFound:
        return
    except discord.HTTPException as error:
        print(f"Could not identify reaction user: {error}")
        return

    if user.bot:
        return

    channel = client.get_channel(payload.channel_id)

    if channel is None:
        try:
            channel = await client.fetch_channel(payload.channel_id)
        except discord.NotFound:
            print(f"Channel not found: channel={payload.channel_id}")
            return
        except discord.Forbidden:
            print(f"Could not access channel: channel={payload.channel_id}")
            return
        except discord.HTTPException as error:
            print(f"Could not fetch channel: {error}")
            return

    if not isinstance(channel, discord.TextChannel):
        return

    try:
        message = await channel.fetch_message(payload.message_id)
    except discord.NotFound:
        print(
            f"Skipped reaction removal: message not found "
            f"message={payload.message_id}"
        )
        return
    except discord.Forbidden:
        print(
            f"Could not verify reaction removal: missing access "
            f"message={payload.message_id}"
        )
        return
    except discord.HTTPException as error:
        print(f"Could not fetch reaction removal message: {error}")
        return

    if not is_meme_submission(message):
        return

    print(
        f"Vote removed: user={payload.user_id} "
        f"message={payload.message_id} "
        f"vote={payload.emoji}"
    )


@tree.command(name="ping", description="Check whether the bot is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(PING_RESPONSE)


client.run(TOKEN)