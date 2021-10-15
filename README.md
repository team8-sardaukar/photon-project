# photon-project
Programming the Photon Laser Tag game
## Setup
**Dependencies**
*These are only necessary for setting up a local dev environment*
1) Install pipenv to set up a virtual environment for the Python side of the webapp. Go to your photon-project
directory and run `pip install pipenv`
2) Create the virtual environment for the application on your machine: `pipenv --three` (still in photon-project)
3) Install packages for connecting to database: `pipenv install sqlalchemy psycopg2-binary`
4) Install packages for webserver: `pipenv install flask marshmallow flask-cors`
5) (ONLY FOR THOSE NOT RUNNING WINDOWS) Now you'll need to start the webserver as we actually use it, if you still have the flask instance from earlier running,
  you'll want to go ahead and stop that now, then continue. 
  * Install gunicorn in the pipenv: `pipenv install gunicorn`
  * Open the pipenv shell: `pipenv shell`
  * Do: `gunicorn main:app`
  * Assuming all went well, you should now be able to navigate to "localhost:8000" in your browser and see the webapp!
6) (DON'T DO THIS IF YOU DID NUMBER 9) You can just use Flask to host the webserver if you can't use guinicorn
  * Outside of virtual environment do `set FLASK_APP=main.py`
  * Then do: `pipenv shell`
  * Now do `flask run`
  * Now go to the IP address and port it gives you in your browser and it should work!
***
## Deploying to Heroku
*This assumes that you are already logged in to the Heroku CLI*
1) The webapp already has the git remote setup for Heroku, so you should start by committing and pushing your changes to
  the main branch of the github. (If you haven't tested your changes please don't just commit them to main and deploy)
2) Once you've run `git push origin main` and everything went through, you should be able to do 
  `git push heroku main` in the CLI where heroku is logged in
3) Heroku takes a bit to build the webapp, but you'll get a message when it is done. Then you should be able to navigate
  to the webapp at https://team-8-sardaukar.herokuapp.com/
