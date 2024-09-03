import discord
from discord.ext import commands, tasks
from settings import DISCORD_APPLICATION_TOKEN, DISCORD_STATUS, MONGO_DB_COLLECTION_CONFIG_NAME
from databasemanager import DatabaseManager
import os
import datetime

print("Starting with bot token:", DISCORD_APPLICATION_TOKEN)

database_manage = DatabaseManager(collection_name=MONGO_DB_COLLECTION_CONFIG_NAME)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await load_cogs()
    print(f'Logged in as {bot.user}')
    update_presence.start()
    await sync_commands()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        print(f"Received a DM from {message.author}: {message.content}")
    else:
        print(f"Received a message in server '{message.guild.name}' from {message.author}: {message.content}")
    await bot.process_commands(message)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            cog = filename[:-3]
            try:
                await bot.load_extension(f'cogs.{cog}')
                print(f"Loaded cog: {cog}")
            except Exception as e:
                print(f"Failed to load cog {cog}: {e}")

async def sync_commands():
    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} commands.')
    except Exception as e:
        print(f"Exception occured during command sync {e}")

@tasks.loop(seconds=15)
async def update_presence():
    current_time = datetime.datetime.utcnow()
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name=DISCORD_STATUS,
        details = "In: The Lusty Leopard",
        assets = {
            "large_image": "legendary",
            "large_text": "Legendary",
            "small_image": "suitup",
            "small_text": "Suit-Up"
        },
        party = {
            "id": "barney_stinson",
            "size": [1, 5]
        },
        buttons = [
            {
                'label': 'Join Our Server',
                'url': 'https://discord.gg/sDtCr5gZuH'
            },
            {
                'label': 'Website',
                'url': 'https://avishakeadhikary.github.io/'
            }
        ],
        platform = "Windows",
        url="https://avishakeadhikary.github.io/",
        start=current_time
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)

async def run_bot():
    await bot.start(DISCORD_APPLICATION_TOKEN)