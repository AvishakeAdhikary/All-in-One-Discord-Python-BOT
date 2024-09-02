import discord
from discord.ext import commands
from typing import Optional, Union

class Miscellaneous(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.hybrid_command(name='showavatar', description='Shows the user avatar')
    async def showavatar(self, ctx: commands.Context, user: Optional[Union[discord.Member, discord.User]] = None):
        try:
            if user is None:
                user = ctx.author

            if not isinstance(user, (discord.Member, discord.User)):
                raise TypeError("Invalid user type provided")

            embed = discord.Embed(color=0x000000)
            embed.set_image(url=user.display_avatar.url)

            avatar_button = discord.ui.Button(label="Download", url=user.display_avatar.url, emoji='⬇️')
            view = discord.ui.View()
            view.add_item(avatar_button)

            await ctx.send(embed=embed, view=view)

        except discord.NotFound:
            await ctx.send("The user or their avatar was not found.")
        except discord.HTTPException:
            await ctx.send("An error occurred while fetching the avatar.")
        except TypeError as e:
            await ctx.send(str(e))
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))
