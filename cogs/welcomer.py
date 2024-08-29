import discord
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from discord import File
from settings import DISCORD_SERVER_WELCOME_CHANNEL_ID, DISCORD_BOT_COLOR_LIGHT, DISCORD_BOT_COLOR_EXTRA_2

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = DISCORD_SERVER_WELCOME_CHANNEL_ID
        channel = self.bot.get_channel(channel_id)
        if channel is None:
            try:
                channel = await self.bot.fetch_channel(channel_id)
            except discord.NotFound:
                print(f"Channel with ID {channel_id} not found.")
                return
            except discord.Forbidden:
                print(f"Bot does not have permission to access channel with ID {channel_id}.")
                return
            except discord.HTTPException as e:
                print(f"HTTP Exception occurred: {e}")
                return
        print(f'Welcome Channel Name: {channel.name}')
        message = f'Welcome to {member.guild.name}'
        background_image = Editor("static/himym-umbrella.jpg")
        user_profile_image = await load_image_async(str(member.avatar.url))
        circle_profile_image = Editor(user_profile_image).resize((150, 150)).circle_image()
        font = Font.montserrat(size=50, variant="bold")
        background_image.paste(circle_profile_image, (725, 100))
        background_image.ellipse((725, 100), width=150, height=150, outline="white", stroke_width=5)
        background_image.text((800, 400), f"{message}", color=DISCORD_BOT_COLOR_LIGHT, font=font, align="center")
        background_image.text((800, 500), f"@{member.name}", color=DISCORD_BOT_COLOR_EXTRA_2, font=font, align="center")
        file = File(fp=background_image.image_bytes, filename="welcome.jpg")
        await channel.send(f"Welcome, {member.mention}! SUIT UP!!!", file=file)
    
async def setup(bot):
    await bot.add_cog(Welcomer(bot))