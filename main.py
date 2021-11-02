from flask import Flask, request, render_template, jsonify, flash
from sqlalchemy.sql.expression import update
from flask_cors import CORS
from entities.entity import Session, engine, Base
from entities.player import Player
from time import sleep

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

Base.metadata.create_all(engine)
session = Session()
players = session.query(Player).all()

#Just an example of the player list dicts formatting
playersListEx = [ 
    {
        'id':'',
        'codename':''
    }
]

playersListGreen = []
playersListRed = []
redScore = 0
greenScore = 0

def updatePlayers(id, codename, team=0, score=0): #team 0 = green, 1 = red
    global players
    global playersListRed
    global playersListGreen
    for player in players:
        if (int(id) == player.id):
            newPlayerDict = {"id":id, "codename":codename, "score":score}
            if (team == 0):
                playersListGreen.append(newPlayerDict.copy())
            else:
                playersListRed.append(newPlayerDict.copy())
    
    #updatePlayerScore(1)

def updatePlayerScore(id):
    print("updating score!")
    global playersListGreen
    global playersListRed
    global redScore
    global greenScore

    for player in playersListGreen:
        if (int(player["id"]) == id):
            player["score"]+=10
            greenScore+=10
    
    for player in playersListRed:
        if (int(player["id"]) == id):
            player["score"]+=10
            redScore+=10

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/player-entry', methods=['GET'])
def playerEntryScreen():
    global playersListRed
    global playersListGreen
    playersListGreen = []
    playersListRed = []
    return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)

@app.route('/player-entry', methods=['POST'])
def getPlayerByID():
    global players
    global playersListGreen
    global playersListRed
    greenId = request.form["GreenId0"]
    greenName = request.form["GreenName0"]
    redId = request.form["RedID0"]
    redName = request.form["RedName0"]
    if redId and redName and greenId and greenName:
        entry = Player(greenId, greenName)
        session.add(entry)
        session.commit()
        entry = Player(redId, redName)
        session.add(entry)
        session.commit()
        players = session.query(Player).all()
        updatePlayers(redId, redName, 1)
        updatePlayers(greenId, greenName, 0)
        return render_template('player-entry.html', redList = playersListRed, greenList = playersListGreen)
    elif not redId and greenId:
        if not greenName:
            foundEntry = 0
            for player in players:
                if (int(greenId) == player.id):
                    updatePlayers(greenId, player.codename, 0)
                    foundEntry = 1
            if (foundEntry != 1):
                flash('NO PLAYER FOUND BY THAT ID! ENTER A NEW CODENAME FOR THAT PLAYER ID!')
            return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)
        else:
            entry = Player(greenId, greenName)
            session.add(entry)
            session.commit()
            players = session.query(Player).all()
            updatePlayers(greenId, greenName, 0)
            return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)
    elif not greenId and redId:
        if not redName:
            foundEntry = 0
            for player in players:
                if (int(redId) == player.id):
                    updatePlayers(redId, player.codename, 1)
                    foundEntry = 1
            if (foundEntry != 1):
                flash('NO PLAYER FOUND BY THAT ID! ENTER A NEW CODENAME FOR THAT PLAYER ID!')
            return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)
        else:
            entry = Player(redId, redName)
            session.add(entry)
            session.commit()
            players = session.query(Player).all()
            updatePlayers(redId, redName, 1)
            return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)
    elif greenId and redId:
        if (not greenName) and (not redName):
            foundEntry = 0
            for player in players:
                if (int(redId) == player.id):
                    updatePlayers(redId, player.codename, 1)
                    foundEntry = 1
            if (foundEntry != 1):
                flash('NO PLAYER FOUND BY THAT ID! ENTER A NEW CODENAME FOR THAT PLAYER ID!')
            foundEntry = 0
            for player in players:
                if (int(greenId) == player.id):
                    updatePlayers(greenId, player.codename, 0)
                    foundEntry = 1
            if (foundEntry != 1):
                flash('NO PLAYER FOUND BY THAT ID! ENTER A NEW CODENAME FOR THAT PLAYER ID!')
            return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)
    else:
        return render_template('player-entry.html', greenList = playersListGreen, redList = playersListRed)

@app.route('/play-action', methods=['GET'])
def playActionScreen():
    global playersListRed
    global playersListGreen
    return render_template('play-action.html', greenList = playersListGreen, redList = playersListRed, redScore = redScore, greenScore = greenScore)

if __name__ == '__main__':
    app.run()
    CORS(app)
