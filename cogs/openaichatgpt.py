import discord
from discord.ext import commands
from settings import OPENAI_API_KEY
from openai import OpenAI, OpenAIError, AuthenticationError, RateLimitError, APIConnectionError

class OpenAIChatGPT(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = None
        if OPENAI_API_KEY is not None:
            try:
                self.client = OpenAI(api_key=OPENAI_API_KEY)
            except OpenAIError as e:
                print(f'OPENAI Exception occurred during OPENAI API KEY configuration: {e}')
            except Exception as e:
                print(f'Exception occurred during OPENAI API KEY configuration: {e}')

    @commands.hybrid_command(name='askchatgpt', description='Ask your queries to OpenAI ChatGPT')
    async def askchatgpt(self, ctx: commands.Context, message: str):
        await ctx.send(f"{ctx.author.mention} asked `{message}`")
        if self.client is None:
            await ctx.send("OpenAI ChatGPT API is not configured properly. Please contact an administrator.")
            return
        try:
            chat_completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant imitating Barney Stinson from How I Met Your Mother."},
                    {"role": "user", "content": message}
                    ]
            )
            response = chat_completion.choices[0].message.content
            if response:
                answer = response
                await ctx.send(answer)
            else:
                await ctx.send("Failed to get a valid response from OpenAI ChatGPT.")
        except AuthenticationError as e:
            print(f"AuthenticationError occurred: {e}")
            await ctx.send("Authentication failed. Please check the API key and try again.")
        except RateLimitError as e:
            print(f"RateLimitError occurred: {e}")
            await ctx.send("Rate limit exceeded. Please try again later.")
        except APIConnectionError as e:
            print(f"APIConnectionError occurred: {e}")
            await ctx.send("Failed to connect to the OpenAI API. Please try again later.")
        except OpenAIError as e:
            print(f"OpenAIError occurred: {e}")
            await ctx.send("An error occurred with the OpenAI API. Please try again later.")
        except Exception as e:
            print(f"Exception occurred while generating response: {e}")
            await ctx.send("An error occurred while processing your request. Please try again later.")

async def setup(bot):
    await bot.add_cog(OpenAIChatGPT(bot))
