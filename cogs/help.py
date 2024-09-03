import discord
from discord.ext import commands
from discord.ui import Select, View

class HelpDropdown(Select):
    def __init__(self, cogs):
        options = [discord.SelectOption(label=cog, value=cog) for cog in cogs]
        super().__init__(placeholder="Select a cog...", options=options)
        self.cogs = cogs

    async def callback(self, interaction: discord.Interaction):
        cog_name = self.values[0]
        commands = self.cogs.get(cog_name, [])
        embed = discord.Embed(title=f"Help for {cog_name} Cog", description="\n".join(commands), color=discord.Color.blue())
        await interaction.response.edit_message(embed=embed)

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cogs = self.load_cogs_help()
    
    def load_cogs_help(self):
        cogs_help = {}
        for cog in self.bot.cogs:
            commands_list = [f"**{command.name}**: {command.description or 'No description provided.'}" for command in self.bot.get_cog(cog).get_commands()]
            cogs_help[cog] = commands_list
        return cogs_help

    @commands.command(name='gethelp')
    async def gethelp(self, ctx):
        view = View()
        dropdown = HelpDropdown(self.cogs)
        view.add_item(dropdown)
        
        embed = discord.Embed(title="Help Menu", description="Select a cog from the dropdown to get help on its commands.", color=discord.Color.blue())
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Help(bot))
