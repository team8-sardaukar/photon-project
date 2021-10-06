from flask import Flask, request, render_template, redirect
from flask.helpers import send_from_directory
from flask_cors import CORS
import os

#template_dir = os.path.abspath('/dist')
#absTest = '/home/ivris/Documents/photon-project/templates'
app = Flask(__name__
#, template_folder=absTest
)

@app.route('/players')
def get_player_by_id():
    print('Does nothing')
    # This is where we will interact with the database

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    CORS(app)
