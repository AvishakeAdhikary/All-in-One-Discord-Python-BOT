from quart import jsonify
from fragments import read_html_fragments

def register_routes(app):
    @app.route('/home', methods=['GET'])
    async def home():
        homeFragment = read_html_fragments(relativeFilePath='/templates/fragments', fileName="home.html")
        return jsonify({'html': homeFragment})

    @app.route('/ai', methods=['GET'])
    async def ai():
        aiFragment = read_html_fragments(relativeFilePath='/templates/fragments', fileName="ai.html")
        return jsonify({'html': aiFragment})

    @app.route('/welcomer', methods=['GET'])
    async def welcomer():
        welcomerFragment = read_html_fragments(relativeFilePath='/templates/fragments', fileName="welcomer.html")
        return jsonify({'html': welcomerFragment})

    @app.route('/invite', methods=['GET'])
    async def invite():
        return jsonify({'html': '<p>This is invite</p>'})

    @app.route('/database', methods=['GET'])
    async def database():
        databaseFragment = read_html_fragments(relativeFilePath='/templates/fragments', fileName="database.html")
        return jsonify({'html': databaseFragment})

    @app.route('/servers', methods=['GET'])
    async def servers():
        return jsonify({'html': '<p>This is servers</p>'})

    @app.route('/status', methods=['GET'])
    async def status():
        return jsonify({'html': '<p>This is status</p>'})

    @app.route('/activedevbadge', methods=['GET'])
    async def activedevbadge():
        return jsonify({'html': '<p>This is active dev badge</p>'})

    @app.route('/supportserver', methods=['GET'])
    async def supportserver():
        return jsonify({'html': '<p>This is support server</p>'})

    @app.route('/verification', methods=['GET'])
    async def verification():
        return jsonify({'html': '<p>This is verification</p>'})

    @app.route('/logging', methods=['GET'])
    async def logging():
        return jsonify({'html': '<p>This is logging</p>'})
    
    @app.route('/sendmessage', methods=['GET'])
    async def sendmessage():
        return jsonify({'html': '<p>This is send message</p>'})

    @app.route('/weather', methods=['GET'])
    async def weather():
        return jsonify({'html': '<p>This is weather</p>'})

    @app.route('/miscellaneous', methods=['GET'])
    async def miscellaneous():
        return jsonify({'html': '<p>This is miscellaneous</p>'})

    @app.route('/moderation', methods=['GET'])
    async def moderation():
        return jsonify({'html': '<p>This is moderation</p>'})

    @app.route('/level', methods=['GET'])
    async def level():
        return jsonify({'html': '<p>This is level</p>'})

    @app.route('/birthdays', methods=['GET'])
    async def birthdays():
        return jsonify({'html': '<p>This is birthdays</p>'})

    @app.route('/translate', methods=['GET'])
    async def translate():
        return jsonify({'html': '<p>This is translate</p>'})

    @app.route('/usage', methods=['GET'])
    async def usage():
        return jsonify({'html': '<p>This is usage</p>'})

    @app.route('/errorlogs', methods=['GET'])
    async def errorlogs():
        return jsonify({'html': '<p>This is error logs</p>'})

    @app.route('/games', methods=['GET'])
    async def games():
        return jsonify({'html': '<p>This is games</p>'})

    @app.route('/giveaways', methods=['GET'])
    async def giveaways():
        return jsonify({'html': '<p>This is giveaways</p>'})

    @app.route('/tickets', methods=['GET'])
    async def tickets():
        return jsonify({'html': '<p>This is tickets</p>'})

    @app.route('/tools', methods=['GET'])
    async def tools():
        return jsonify({'html': '<p>This is tools</p>'})

    @app.route('/about', methods=['GET'])
    async def about():
        return jsonify({'html': '<iframe class="rounded h-full w-full" src="https://avishakeadhikary.github.io" frameborder="0"></iframe>'})

