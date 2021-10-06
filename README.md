# photon-project
Programming the Photon Laser Tag game
## Setup
**Dependencies**
*These are only necessary for setting up a local dev environment*
1) Install pipenv to set up a virtual environment for the Python side of the webapp. Go to your photon-project
directory and run "pip install pipenv"
2) Next, make sure that you have Node.js and NPM installed. If not, download and install those for your OS
3) Install the angular CLI: "npm install -g @angular/cli"
3) Create the virtual environment for the application on your machine: "pipenv --three" (still in photon-project)
4) Install packages for connecting to database: "pipenv install sqlalchemy psycopg2-binary"
5) Install packages for webserver: "pipenv install flask marshmallow flask-cors"
6) Now you should try running the flask webserver, do the following:
  * set environment variable for flask app, on Windows do "set FLASK_APP=main.py", on Linux do "export FLASK_APP=./main.py"
  * Active the virtual environment. On Linux this is "source $(pipenv --venv)/bin/activate". On Windows you might be able 
  to do "pipenv shell"
  * Do "flask run" Theoretically the webserver should start
7) Now you'll need to build the Angular application, from outside the pipenv terminal but in the photon-project directory
  do the following:
  * You might need to run "npm update" here to ensure it can find the Angular devtools
  * run "ng build --build-optimizer --baseHref="/static/"" <-- NOTE THAT YOU NEED TO INCLUDE A QUOTATION MARK AT THE END AS WELL
  * Now you're going to need to copy the updated built Angular files in the static and templates, copy all of the files
  in /dist except for "index.html" to /static. On Linux you can do 
  "cp -r ./dist/* ./static && rm -rf ./static/index.html"
  * Then you need to copy index.html from /dist to /templates. On Linux you can do "cp -r ./dist/index.html ./templates/index.html"
8) (ONLY FOR THOSE NOT RUNNING WINDOWS) Now you'll need to start the webserver as we actually use it, if you still have the flask instance from earlier running,
  you'll want to go ahead and stop that now, then continue. 
  * Install gunicorn in the pipenv: "pipenv install gunicorn"
  * Open the pipenv shell: "pipenv shell"
  * Do: "gunicorn main:app"
  * Assuming all went well, you should now be able to navigate to "localhost:8000" in your browser and see the webapp!
8) (DON'T DO THIS IF YOU DID THE PREVIOUS NUMBER 8) You can just use Flask to host the webserver if you can't use guinicorn
  * Outside of virtual environment do "set FLASK_APP="main.py"
  * Then do: "pipenv shell"
  * Now do "flask run"
  * Now go to the IP address and port it gives you in your browser and it should work!
***
## Deploying to Heroku
*This assumes that you are already logged in to the Heroku CLI*
1) The webapp already has the git remote setup for Heroku, so you should start by committing and pushing your changes to
  the main branch of the github. (If you haven't tested your changes please don't just commit them to main and deploy)
2) Once you've run "git push origin main" and everything went through, you should be able to do 
  "git push heroku main" in the CLI where heroku is logged in
3) Heroku takes a bit to build the webapp, but you'll get a message when it is done. Then you should be able to navigate
  to the webapp at https://team-8-sardaukar.herokuapp.com/
