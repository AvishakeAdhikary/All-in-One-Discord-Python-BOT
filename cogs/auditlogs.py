import discord
from discord.ext import commands
import logging
from settings import DISCORD_SERVER_AUDITLOGS_CHANNEL_ID

# Set up logging
logging.basicConfig(level=logging.INFO)

class AuditLogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channel_id = DISCORD_SERVER_AUDITLOGS_CHANNEL_ID
        self.logging_enabled = {
            "member_update": True,
            "channel_update": True,
            "role_update": True,
            "emoji_update": True,
            "member_ban_add": True,
            "member_ban_remove": True,
            "integration_create": True,
            "integration_update": True,
            "integration_delete": True,
            "voice_state_update": True
        }

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if self.logging_enabled["member_update"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Member updated: {before} -> {after}')

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if self.logging_enabled["channel_update"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Channel updated: {before} -> {after}')

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        if self.logging_enabled["role_update"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Role updated: {before} -> {after}')

    @commands.Cog.listener()
    async def on_guild_emoji_update(self, before, after):
        if self.logging_enabled["emoji_update"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Emoji updated: {before} -> {after}')

    @commands.Cog.listener()
    async def on_member_ban_add(self, guild, user):
        if self.logging_enabled["member_ban_add"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'User banned: {user}')

    @commands.Cog.listener()
    async def on_member_ban_remove(self, guild, user):
        if self.logging_enabled["member_ban_remove"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'User unbanned: {user}')

    @commands.Cog.listener()
    async def on_integration_create(self, integration):
        if self.logging_enabled["integration_create"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Integration created: {integration}')

    @commands.Cog.listener()
    async def on_integration_update(self, integration):
        if self.logging_enabled["integration_update"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Integration updated: {integration}')

    @commands.Cog.listener()
    async def on_integration_delete(self, integration):
        if self.logging_enabled["integration_delete"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                await channel.send(f'Integration deleted: {integration}')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.logging_enabled["voice_state_update"]:
            channel = self.bot.get_channel(self.log_channel_id)
            if channel:
                if before.channel is None and after.channel is not None:
                    # User joined a voice channel
                    await channel.send(f'{member} joined voice channel: {after.channel}')
                elif before.channel is not None and after.channel is None:
                    # User left a voice channel
                    await channel.send(f'{member} left voice channel: {before.channel}')
                elif before.channel != after.channel:
                    # User switched voice channels
                    await channel.send(f'{member} switched from {before.channel} to {after.channel}')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def toggle_logging(self, ctx, log_type: str, status: str):
        log_type = log_type.lower()
        status = status.lower()
        if log_type in self.logging_enabled and status in ["on", "off"]:
            self.logging_enabled[log_type] = (status == "on")
            await ctx.send(f'Logging for {log_type} has been turned {"on" if self.logging_enabled[log_type] else "off"}.')
        else:
            await ctx.send('Invalid log type or status. Use "on" or "off" for status.')

async def setup(bot):
    await bot.add_cog(AuditLogs(bot))
