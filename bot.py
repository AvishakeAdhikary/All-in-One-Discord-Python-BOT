import discord
from discord.ext import commands, tasks
from settings import DISCORD_APPLICATION_TOKEN, DISCORD_STATUS, MONGO_DB_COLLECTION_CONFIG_NAME
from databasemanager import DatabaseManager
import os
import datetime

print("Starting with bot token:", DISCORD_APPLICATION_TOKEN)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
    await load_cogs()
    print(f'Logged in as {bot.user}')
    update_presence.start()

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

@bot.command()
async def sync(ctx: commands.Context):
    load_cogs()

@tasks.loop(seconds=15)
async def update_presence():
    current_time = datetime.datetime.utcnow()
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name=DISCORD_STATUS,
        details = "In: The Lusty Leopard",
        large_image_url = "https://github.com/AvishakeAdhikary/All-in-One-Discord-Python-BOT/blob/main/static/legendary.jpg?raw=true",
        large_image_text = "This is legendary",
        small_image_url = "https://github.com/AvishakeAdhikary/All-in-One-Discord-Python-BOT/blob/main/static/legendary.jpg?raw=true",
        small_image_text = "This is legendary",
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