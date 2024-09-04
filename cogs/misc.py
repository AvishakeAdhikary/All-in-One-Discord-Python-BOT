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

    @commands.hybrid_command(name='roast', description='Roasts a specified user or yourself if no user is specified.')
    async def roast(self, ctx: commands.Context, user: Optional[Union[discord.Member, discord.User]] = None):
        try:
            if user is None:
                user = ctx.author

            if not isinstance(user, (discord.Member, discord.User)):
                raise TypeError("Invalid user type provided")

            roasts = [
                "You're like a human thesaurus, but only for bad ideas.",
                "If you were a vegetable, you'd be a 'couch potato'.",
                "You bring everyone so much joy when you leave the room.",
                "I'd agree with you, but then we'd both be wrong.",
                "If brains were dynamite, you wouldn't have enough to blow your nose.",
                "You're proof that even the worst days can end.",
                "You're like a cloud. When you disappear, it's a beautiful day.",
                "I'd make a joke about your intelligence, but it's a bit too high-brow.",
                "Calling you an idiot would be an insult to idiots everywhere.",
                "You're the reason they put instructions on shampoo bottles.",
                "You're not stupid; you're just inexperienced.",
                "I'd explain it to you, but I left my patience at home.",
                "You have the unique talent of making everyone around you smarter.",
                "You're like a broken pencil: pointless.",
                "I'd tell you a joke, but you're too dense to get it.",
                "If you were any more dense, you'd collapse into a black hole.",
                "You're not the dumbest person in the world, but you better hope they don't come here.",
                "You have the charisma of a damp rag.",
                "You could use a little more polish on that personality of yours.",
                "Your secrets are always safe with me. I never even listen when you tell me them.",
                "I'm not saying you're dumb, but you could use a few more neurons.",
                "You have the social skills of a cactus.",
                "Your face would make a great scarecrow.",
                "You're like a sunburn: not wanted, and it only makes things worse.",
                "If your brain was dynamite, it wouldn't be enough to blow your hat off.",
                "You're like a sloth trying to win a race.",
                "Even my dog has more personality than you.",
                "You're the type of person who could get lost in a one-room apartment.",
                "If ignorance is bliss, you must be the happiest person alive.",
                "Your IQ is lower than your shoe size.",
                "I'm not saying you're forgettable, but I've forgotten you already.",
                "You're as useful as a screen door on a submarine.",
                "If you were any more clueless, you'd need a GPS to find your way to the bathroom.",
                "You're like an expired coupon: no value and just annoying.",
                "I could listen to you, but I have better things to do, like watching paint dry.",
                "If you were any more transparent, you'd be invisible.",
                "I'd tell you to have a nice day, but I'm afraid you'll just ruin it.",
                "You're proof that even the worst people can find friends.",
                "If laziness were an Olympic sport, you'd win gold.",
                "You're about as useful as a chocolate teapot.",
                "I'd call you a genius, but that's not even close to accurate.",
                "You're like a broken clock: even when you're right, it's by accident.",
                "You have the energy of a deflated balloon.",
                "You're a perfect example of why some animals eat their young.",
                "Your opinions are like bad movies: I can't take them seriously.",
                "I don't have the time or crayons to explain this to you."
            ]

            import random
            roast_message = random.choice(roasts)
            if user == ctx.author:
                roast_message = f"{ctx.author.mention}" + roast_message
            else:
                roast_message = f"{user.mention}, " + roast_message

            await ctx.send(roast_message)

        except TypeError as e:
            await ctx.send(str(e))
        except Exception as e:
            await ctx.send(f"An unexpected error occurred: {str(e)}")

async def setup(bot):
    await bot.add_cog(Miscellaneous(bot))
