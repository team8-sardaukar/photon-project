from flask import Flask, request, render_template, redirect
from flask.helpers import send_from_directory
from flask_cors import CORS
from urllib.parse import urlparse
import os

app = Flask(__name__)
CORS(app)
port = int(os.environ.get("PORT",5000))
app.run(host='0.0.0.0', port=port)

@app.route('/players')
def get_player_by_id():
    print('Does nothing')
    # This is where we will interact with the database

@app.route('/')
def home():
    o = urlparse(request.base_url)
    send = o.hostname + ':8080'
    return redirect(send)
