from database import DatabaseManager

class WelcomeManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.collection_name = "welcome_settings"

    def set_welcome_channel(self, guild_id, channel_id):
        query = {"guild_id": guild_id}
        update = {"welcome_channel_id": channel_id}
        self.db_manager.update_one(self.collection_name, query, update)

    def get_welcome_channel(self, guild_id):
        query = {"guild_id": guild_id}
        result = self.db_manager.find_one(self.collection_name, query)
        return result.get("welcome_channel_id") if result else None

    def set_welcome_message(self, guild_id, message):
        query = {"guild_id": guild_id}
        update = {"welcome_message": message}
        self.db_manager.update_one(self.collection_name, query, update)

    def get_welcome_message(self, guild_id):
        query = {"guild_id": guild_id}
        result = self.db_manager.find_one(self.collection_name, query)
        return result.get("welcome_message") if result else "Welcome to {servername}!"

# @commands.Cog.listener()
#     async def on_member_join(self, member: discord.Member):
#         guild_id = member.guild.id
#         welcome_channel_id = self.welcomemanager.get_welcome_channel(guild_id)
#         welcome_message = self.welcomemanager.get_welcome_message(guild_id)
        
#         if welcome_channel_id is not None:
#             channel = self.bot.get_channel(welcome_channel_id)
#             if channel is not None:
#                 message = welcome_message.format(servername=member.guild.name)
#                 background_image = Editor("static/himym-umbrella.jpg")
#                 user_profile_image = await load_image_async(str(member.avatar.url))
#                 circle_profile_image = Editor(user_profile_image).resize((150, 150)).circle_image()
#                 font = Font.montserrat(size=50, variant="light")

#                 background_image.paste(circle_profile_image, (725, 100))
#                 background_image.ellipse((725, 100), width=150, height=150, outline="white", stroke_width=5)
#                 background_image.text((800, 400), f"{message}", color="white", font=font, align="center")
#                 background_image.text((800, 500), f"{member.name}", color="white", font=font, align="center")
#                 file = File(fp=background_image.image_bytes, filename="welcome.jpg")
#                 await channel.send(f"Hello, {member.mention}! SUIT UP!!!", file=file)