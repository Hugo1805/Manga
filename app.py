from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_dotenv import DotEnv
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
from database.db import  initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

import os


#APP
app = Flask(__name__)

app.config.from_envvar('ENV_FILE_LOCATION')

#DotEnv
# load_dotenv(find_dotenv())

#CORS
cors = CORS(app)

# API
api = Api(app,errors=errors)

#Bcrypt
bcrypt = Bcrypt(app)

#JWT
jwt = JWTManager(app)


#Database

app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/manga'
}

initialize_db(app)

# Restfull routes

initialize_routes(api)


if __name__ == "__main__":
    app.run()
