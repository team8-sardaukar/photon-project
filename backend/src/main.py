# coding=utf-8

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/players')
def get_players():
    # TODO: Get players from the database
    print("Remember to implement get_players!")

@app.route('/players', methods=['POST'])
def add_player():
    # TODO: Add new player to the database
    print("Remember to implement add_player!")
