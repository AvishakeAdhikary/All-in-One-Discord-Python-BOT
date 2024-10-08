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
    try:
        asyncio.run(main())
    except:
        print("Something happened while trying to run the bot. Please debug the code or check your connection...")

# Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process