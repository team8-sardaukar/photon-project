from flask import Flask, request, render_template, jsonify, flash
from flask_cors import CORS
from entities.entity import Session, engine, Base
from entities.player import Player

#template_dir = os.path.abspath('/dist')
#absTest = '/home/ivris/Documents/photon-project/templates'
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

Base.metadata.create_all(engine)
session = Session()
players = session.query(Player).all()

playersList = [
    {
        'id':'01221',
        'codename':'TESTER'
    },
    {
        'id':'01222',
        'codename':'OTHER'
    }
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/player-entry', methods=['GET'])
def playerEntry():
    return render_template('player-entry.html')

@app.route('/player-entry', methods=['GET'])
def playerEntryScreen():
    # Still needs to submit to database
    return render_template('player-entry.html')

@app.route('/player-entry', methods=['POST'])
def getPlayerByID():
    greenId = request.form["GreenId0"]
    greenName = request.form["GreenName0"]
    greenEntry = [greenId, greenName]
    redId = request.form["RedID0"]
    redName = request.form["RedName0"]
    redEntry = [redId, redName]
    #global player
    #return jsonify(player['data'])
    if redId and redName and greenId and greenName:
        #submit the 
        return jsonify(greenEntry, redEntry)
    elif not redId and greenId:
        if not greenName:
            foundEntry = 0
            for player in players:
                if (int(greenId) == player.id):
                    newPlayerDict = {"id":greenId, "codename":player.codename}
                    playersList.append(newPlayerDict.copy())
                    foundEntry = 1
            if (foundEntry != 1):
                flash('NO PLAYER FOUND BY THAT ID! ENTER A NEW CODENAME FOR THAT PLAYER ID!')
            return render_template('player-entry.html', data=playersList)
        else:
            entry = Player(greenId, greenName)
            print(str(entry.id) + str(entry.codename))
            session.add(entry)
            session.commit()
            return render_template('player-entry.html', data=playersList)
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
