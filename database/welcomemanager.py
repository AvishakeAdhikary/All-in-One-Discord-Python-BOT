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