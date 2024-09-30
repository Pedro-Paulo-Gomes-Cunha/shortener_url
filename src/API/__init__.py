

from src.config.Config import BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS   
import pymysql
import mysql.connector
from flask import Flask
from flask_migrate import Migrate
import os

app = Flask(__name__)

CORS(app)


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = BaseConfig.SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_DATABASE_URI'] =BaseConfig.SQLALCHEMY_DATABASE_URI
app.config['JWT_TOKEN_LOCATION'] = ['headers']


db = SQLAlchemy()


db.init_app(app)

migrate = Migrate(app, db)


from src.core.Domain.models import URL

from src.API import routes

if __name__ == 'main':
    
    app.run(host='0.0.0.0', port=5000)