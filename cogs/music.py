import discord
from discord.ext import commands
from settings import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
import wavelink

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lavalink_nodes = [
            {"host": "lavalink.oops.wtf", "port": 2000, "password": "www.freelavalink.ga"},
        ]

    @commands.hybrid_command(name='join', description="Make the bot join the channel.")
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("You are not connected to a voice channel.")
            return

        voice_channel = ctx.author.voice.channel

        if ctx.voice_client:
            if ctx.voice_client.channel == voice_channel:
                await ctx.send(f"Already connected to {voice_channel.name}.")
            else:
                try:
                    await ctx.voice_client.move_to(voice_channel)
                    await ctx.send(f"Moved to {voice_channel.name}.")
                except discord.ClientException:
                    await ctx.send("The bot is already in a voice channel.")
                except Exception as e:
                    await ctx.send(f"An error occurred: {e}")
        else:
            try:
                await voice_channel.connect()
                await ctx.send(f"Joined {voice_channel.name}.")
            except discord.ClientException:
                await ctx.send("The bot is already in a voice channel.")
            except discord.PrivilegedIntentsRequired as e:
                await ctx.send(f"Privileged intents required: {e}")
            except Exception as e:
                await ctx.send(f"An error occurred: {e}")

    @commands.hybrid_command(name='leave', description="Make the bot leave the channel.")
    async def leave(self, ctx):
        if ctx.voice_client is None:
            await ctx.send("I am not connected to any voice channel.")
            return

        try:
            await ctx.voice_client.disconnect()
            await ctx.send("Left the voice channel.")
        except discord.ClientException:
            await ctx.send("An error occurred while trying to disconnect.")
        except Exception as e:
            await ctx.send(f"An error occurred: {e}")

async def setup(bot):
    await bot.add_cog(Music(bot))
