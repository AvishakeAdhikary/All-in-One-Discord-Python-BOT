import discord
from discord.ext import commands
from settings import GEMINI_API_KEY

class GoogleGemini(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.HybridCommand()
    async def askgemini(self, interaction: discord.Interaction, message):
        pass
    
async def setup(bot):
    await bot.add_cog(GoogleGemini(bot))