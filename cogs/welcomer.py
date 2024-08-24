import discord
from discord.ext import commands

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channel_id = None
        self.welcome_message = "Welcome to the server, {user}!"

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user.name}")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if self.welcome_channel_id is not None:
            channel = self.bot.get_channel(self.welcome_channel_id)
            if channel is not None:
                message = self.welcome_message.format(user=member.mention)
                await channel.send(message)

    @commands.group(invoke_without_command=True)
    async def welcome(self, ctx):
        await ctx.send("Welcome command. Use `!welcome setchannel <channel_id>` to set the welcome channel or `!welcome setmessage <message>` to set the welcome message.")

    @welcome.command(name="setchannel")
    @commands.has_permissions(administrator=True)
    async def setchannel(self, ctx, channel: discord.TextChannel):
        self.welcome_channel_id = channel.id
        await ctx.send(f"Welcome channel set to {channel.mention}.")

    @welcome.command(name="setmessage")
    @commands.has_permissions(administrator=True)
    async def setmessage(self, ctx, *, message):
        self.welcome_message = message
        await ctx.send("Welcome message updated!")

async def setup(bot):
    await bot.add_cog(Welcomer(bot))
