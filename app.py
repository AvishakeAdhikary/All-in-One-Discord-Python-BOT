import asyncio
from quart import Quart, render_template
from endpoints import register_routes
import bot

app = Quart(__name__)

@app.route('/')
@app.route('/index')
async def index():
    return await render_template('index.html')

async def run_quart():
    register_routes(app)
    await app.run_task(host='0.0.0.0', port=5000, debug=True)

async def run_bot():
    await bot.run_bot()

async def main():
    # Start the Quart application and Discord bot
    await asyncio.gather(run_quart(), run_bot())

if __name__ == '__main__':
    asyncio.run(main())


# BOT Rich Presence
# static void UpdatePresence()
# {
#     DiscordRichPresence discordPresence;
#     memset(&discordPresence, 0, sizeof(discordPresence));
#     discordPresence.state = "Playing Solo";
#     discordPresence.details = "Competitive";
#     discordPresence.startTimestamp = 1507665886;
#     discordPresence.endTimestamp = 1507665886;
#     discordPresence.largeImageText = "Numbani";
#     discordPresence.smallImageText = "Rogue - Level 100";
#     discordPresence.partyId = "ae488379-351d-4a4f-ad32-2b9b01c91657";
#     discordPresence.partySize = 1;
#     discordPresence.partyMax = 5;
#     discordPresence.joinSecret = "MTI4NzM0OjFpMmhuZToxMjMxMjM= ";
#     Discord_UpdatePresence(&discordPresence);
# }

# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process