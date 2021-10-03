# photon-project
Programming the Photon Laser Tag game

# Architecture

*Dependencies*

* **pipenv**
You'll need pipenv installed on your system and probably in the $PATH for your system if you want to be able to easily use in the CLI. You can install pipenv with pip from Python. If you're on Windows you'll have to add it to your $PATH variable manually, on Linux when you run "sudo pip install pipenv" it should add it to your path. pipenv is basically an environment to put our python dependencies for this project in so that we don't have to have everything installed on the host machine. For instance, Flask, SQLAlchemy, etc... can all just be packaged with the project using pipenv instead of us needing to install it. 

* **Node.js** 
Go ahead and grab Node.js and NPM to install on your system as well if you will need to manage Angular. NPM is basically a package manager that we can use to install Angular and manage the additional components that are optional with the framework, like @Angular/Routing. 

* **Heroku**

* **PostgreSQL**

#

*Backend*

For the backend I went ahead and installed SQLAlchemy and the psycopg2 driver for PostgreSQL to be compatible with SQLAlchemy. You guys don't have to use that if you have a better method, though, it was just a recommended solution I found and went ahead and set up. 

#

*Frontend*

The frontend is using Angular. We also have @Angular/Routing for redirects within the webapp. 

# Running The Webapp

1) Navigate in your CLI to the backend folder of the project, then do...
  * set FLASK_APP=./src/main.py (This is an environment variable, so on linux it'll be "export FLASK_APP=./src/main.py",      on Windows it'll be "set FLASK_APP=./src/main.py"
  * Now you need to enter the virtual environment for the project so you have access to all of the dependencies. Just do      "pipenv shell"
  * Finally, you should be able to now do "flask run -h 0.0.0.0"
2) In a new terminal window, navigate to the frontend directory in the project, then do "ng serve"
3) You should now be able to navigate to http://localhost:4200 in your browser and see the test page!
