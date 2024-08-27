import discord
from discord.ext import commands, tasks
from settings import DISCORD_APPLICATION_TOKEN, DISCORD_STATUS
import os
import datetime

print("Starting with bot token:", DISCORD_APPLICATION_TOKEN)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents) 

@bot.event
async def on_ready():
    await load_cogs()
    print(f'Logged in as {bot.user}')
    update_presence.start()

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

async def load_cogs():
    # Load cogs (command modules)
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
        details = "Chilling",
        large_image = "legendary",
        large_text = "This is legendary",
        small_image = "legendary",
        small_text = "This is legendary",
        party_id = "barney_stinson",
        party_size = "1",
        party_max = "5",
        join_secret = "legendaddy",
        url="https://avishakeadhikary.github.io/",
        start=current_time
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)

async def run_bot():
    await bot.start(DISCORD_APPLICATION_TOKEN)