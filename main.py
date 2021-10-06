from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/players')
def get_player_by_id():
    print('Does nothing')
    # This is where we will interact with the database

@app.route('/')
def home():
    return render_template('src/index.html')
