import discord
from discord.ext import commands
from config.settings import DISCORD_APPLICATION_TOKEN
import os

print("Starting with bot token:", DISCORD_APPLICATION_TOKEN)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await load_cogs()
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    await bot.process_commands(message)

async def load_cogs():
    # Load cogs (command modules)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            cog = filename[:-3]
            await bot.load_extension(f'cogs.{cog}')

async def run_bot():
    await bot.start(DISCORD_APPLICATION_TOKEN)
