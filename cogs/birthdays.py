import discord
from discord.ext import commands
import datetime
import pytz
from databasemanager import DatabaseManager
import traceback

class Birthdays(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DatabaseManager(collection_name='birthdays')
        self.settings_db = DatabaseManager(collection_name='settings')
        self.birthday_channel = self.settings_db.get_setting('birthday_channel')

    @commands.hybrid_command(name='setbirthdaychannel', description="Set the birthday channel in the server.")
    @commands.has_permissions(administrator=True)
    async def set_birthday_channel(self, ctx, channel: discord.TextChannel):
        """Sets the channel where birthday messages will be posted."""
        try:
            # Save the channel ID to the database
            self.settings_db.set_setting('birthday_channel', channel.id)
            self.birthday_channel = channel.id
            await ctx.send(f"Birthday messages will be posted in {channel.mention}")
        except Exception as e:
            await ctx.send("An error occurred while setting the birthday channel.")
            print(f"Error in set_birthday_channel: {e}")
            traceback.print_exc()

    @commands.hybrid_command(name='setbirthday', description="Set the birthday with optional year and timezone.")
    async def set_birthday(self, ctx, day: int, month: int, year: int = None, timezone: str = "UTC"):
        """Sets the birthday for the user with optional year and timezone."""
        try:
            user_id = ctx.author.id
            if not (1 <= day <= 31) or not (1 <= month <= 12):
                return await ctx.send("Invalid day or month. Please use valid dates.")

            if year:
                try:
                    birthday = datetime.datetime(year, month, day)
                except ValueError:
                    return await ctx.send("Invalid date provided.")
            else:
                today = datetime.date.today()
                birthday = datetime.date(today.year, month, day)

            self.db.update_one('birthdays', {'user_id': user_id}, {'$set': {'day': day, 'month': month, 'year': year, 'timezone': timezone}}, upsert=True)

            await ctx.send(f"Birthday set to {birthday.strftime('%d-%m-%Y') if year else birthday.strftime('%d-%m')}.")
        except Exception as e:
            await ctx.send("An error occurred while setting the birthday.")
            print(f"Error in set_birthday: {e}")
            traceback.print_exc()

    @commands.hybrid_command(name='listbirthday', description="List all saved birthdays.")
    async def list_birthdays(self, ctx):
        """Lists all saved birthdays."""
        try:
            birthdays = self.db.find_one('birthdays', {})
            if not birthdays:
                return await ctx.send("No birthdays set.")

            embed = discord.Embed(title="List of Birthdays", description="Here are the saved birthdays:")
            for entry in birthdays:
                user = self.bot.get_user(entry['user_id'])
                date = f"{entry['day']}-{entry['month']}-{entry['year'] if entry.get('year') else ''}"
                embed.add_field(name=user.name if user else "Unknown", value=date, inline=False)

            await ctx.send(embed=embed)
        except Exception as e:
            await ctx.send("An error occurred while listing the birthdays.")
            print(f"Error in list_birthdays: {e}")
            traceback.print_exc()

    async def send_birthday_message(self, user_id, birthday_date, timezone):
        """Sends a birthday message in the designated channel."""
        try:
            if self.birthday_channel is None:
                return
            
            channel = self.bot.get_channel(self.birthday_channel)
            user = self.bot.get_user(user_id)
            if not user:
                return

            timezone = pytz.timezone(timezone)
            current_time = datetime.datetime.now(timezone)

            embed = discord.Embed(
                title=f"🎉 Happy Birthday {user.name}! 🎉",
                description=f"Today is {user.name}'s birthday! 🥳",
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=user.avatar_url)
            embed.add_field(name="Date", value=birthday_date.strftime('%d-%m-%Y'))
            embed.add_field(name="Timezone", value=timezone.zone)
            embed.set_footer(text="Wishing you a wonderful year ahead!")

            await channel.send(embed=embed)
        except Exception as e:
            print(f"Error in send_birthday_message: {e}")
            traceback.print_exc()

async def setup(bot):
    await bot.add_cog(Birthdays(bot))
