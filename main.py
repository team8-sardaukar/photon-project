from flask import Flask, request, render_template, jsonify
from flask_cors import CORS

#template_dir = os.path.abspath('/dist')
#absTest = '/home/ivris/Documents/photon-project/templates'
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/player-entry', methods=['GET'])
def playerEntry():
    return render_template('player-entry.html')

@app.route('/player-entry', methods=['POST'])
def get_player_by_id():
    global player
    return jsonify(player['data'])

if __name__ == '__main__':
    app.run()
    CORS(app)

player = {
    "data": [
        {
            "ID": "9982753",
            "username": "imverycool"
        },
    ]
}