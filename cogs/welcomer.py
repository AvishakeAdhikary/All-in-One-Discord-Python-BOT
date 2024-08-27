import discord
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from discord import File
from settings import DISCORD_SERVER_WELCOME_CHANNEL_ID

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = DISCORD_SERVER_WELCOME_CHANNEL_ID
        if channel is not None:
            await channel.send(f'Welcome to {member.guild.name}, {member.mention}.')
    
async def setup(bot):
    await bot.add_cog(Welcomer(bot))