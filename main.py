from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from entities.entity import Session, engine, Base
from entities.player import Player

#template_dir = os.path.abspath('/dist')
#absTest = '/home/ivris/Documents/photon-project/templates'
app = Flask(__name__)

Base.metadata.create_all(engine)
session = Session()
players = session.query(Player).all()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/player-entry', methods=['GET'])
def playerEntry():
    return render_template('player-entry.html')

@app.route('/player-entry', methods=['POST', 'GET'])
def get_player_by_id():
    # Still needs to submit to database
    greenId = request.form["GreenId0"]
    greenName = request.form["GreenName0"]
    greenEntry = [greenId, greenName]
    redId = request.form["RedID0"]
    redName = request.form["RedName0"]
    redEntry = [redId, redName]
    #global player
    #return jsonify(player['data'])
    if redId and redName and greenId and greenName:
        return jsonify(greenEntry, redEntry)
    elif not redId and greenId:
        if not greenName:
            return jsonify(greenId)
        else:
            return jsonify(greenEntry)
    elif not greenId and redId:
        if not redName:
            return jsonify(redId)
        else:
            return jsonify(redEntry)
    else:
        return render_template('player-entry.html')

if __name__ == '__main__':
    app.run()
    CORS(app)

print('PLAYERS: ')
for player in players:
    print(f'({player.id}) {player.codename}')
