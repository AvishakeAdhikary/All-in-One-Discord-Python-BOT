import discord
from discord.ext import commands
from settings import GEMINI_API_KEY
import google.generativeai as genai

class GoogleGemini(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.model = None
        if GEMINI_API_KEY is not None:
            try:
                genai.configure(api_key=GEMINI_API_KEY)
                self.model = genai.GenerativeModel("gemini-1.5-flash")
            except Exception as e:
                print(f'Exception occurred during GEMINI API KEY configuration: {e}')

    @commands.hybrid_command(name='askgemini', description='Ask your queries to Google Gemini')
    async def askgemini(self, ctx: commands.Context, message: str):
        await ctx.send(f"{ctx.author.mention} asked `{message}`")
        if self.model is None:
            await ctx.send("Google Gemini API is not configured properly. Please contact an administrator.")
            return
        try:
            response = await self.model.generate_content_async(message)
            
            if response and response.text:
                answer = response.text
                await ctx.send(answer)
            else:
                await ctx.send("Failed to get a valid response from Google Gemini.")
        except Exception as e:
            print(f"Exception occurred while generating response: {e}")
            await ctx.send("An error occurred while processing your request. Please try again later.")

async def setup(bot):
    await bot.add_cog(GoogleGemini(bot))
