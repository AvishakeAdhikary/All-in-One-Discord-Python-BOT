import os
from dotenv import load_dotenv

load_dotenv()

# Discord Environmental Variables
DISCORD_APPLICATION_TOKEN = os.getenv('DISCORD_APPLICATION_TOKEN')
DISCORD_APPLICATION_CLIENT_ID = os.getenv('DISCORD_APPLICATION_CLIENT_ID')
DISCORD_APPLICATION_CLIENT_SECRET = os.getenv('DISCORD_APPLICATION_CLIENT_SECRET')
DISCORD_APPLICATION_PUBLIC_KEY = os.getenv('DISCORD_APPLICATION_PUBLIC_KEY')
DISCORD_SERVER_ID = os.getenv('DISCORD_SERVER_ID')
DISCORD_SERVER_WELCOME_CHANNEL_ID = os.getenv('DISCORD_SERVER_WELCOME_CHANNEL_ID')
DISCORD_SERVER_AUDITLOGS_CHANNEL_ID = os.getenv('DISCORD_SERVER_AUDITLOGS_CHANNEL_ID')

# BOT Colors
DISCORD_BOT_COLOR_DARK = (26, 26, 26)
DISCORD_BOT_COLOR_LIGHT = (254, 225, 199)
DISCORD_BOT_COLOR_EXTRA_1 = (181, 168, 134)
DISCORD_BOT_COLOR_EXTRA_2 = (250, 126, 97)
DISCORD_BOT_COLOR_EXTRA_3 = (244, 65, 116)

# BOT Discord Status
DISCORD_STATUS = os.getenv('DISCORD_STATUS')

# Owner Information
OWNER_ID = os.getenv('OWNER_ID')

MONGO_DB_URI = os.getenv('MONGO_DB_URI')
MONGO_DB_DATABASE_NAME = os.getenv('MONGO_DB_DATABASE_NAME')
MONGO_DB_COLLECTION_CONFIG_NAME = os.getenv('MONGO_DB_COLLECTION_CONFIG_NAME')
MONGO_DB_COLLECTION_BIRTHDAYS = os.getenv('MONGO_DB_COLLECTION_BIRTHDAYS')

# AI Information
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Channel Logging Information
SYSTEM_LOGGING_WEBHOOK_ID = os.getenv('SYSTEM_LOGGING_WEBHOOK_ID')
SYSTEM_LOGGING_WEBHOOK_TOKEN = os.getenv('SYSTEM_LOGGING_WEBHOOK_TOKEN')

# Spotify Information
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')