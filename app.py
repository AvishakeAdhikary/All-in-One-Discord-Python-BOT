from quart import Quart, request, jsonify, render_template
import asyncio
import bot

app = Quart(__name__)

@app.route('/')
@app.route('/index')
async def index():
    return await render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return jsonify({'html': '<p>This is home</p>'})

@app.route('/ai')
def ai():
    return jsonify({'html': '<p>This is ai</p>'})

async def run_quart():
    await app.run_task(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(run_quart())
    loop.run_until_complete(bot.run_bot())

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