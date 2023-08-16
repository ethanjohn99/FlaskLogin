import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

app = Flask(__name__)

username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
endpoint  = os.environ.get('ENDPOINT')
name     = os.environ.get('NAME')

#url = 'sqlite:///C:\\Users\\nathan.forester\\Documents\\movies.db' 
url = 'sqlite:////home/ubuntu/FlaskMovieDB2/movies.db' 
# url = f'mysql+pymysql://'
#url = 'mysql+pymysql://nathan:password@my-rds-27-09.cb9iyz332tc1.eu-west-2.rds.amazonaws.com:3306/Here'
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SECRET_KEY'] = '123456789'

db = SQLAlchemy(app)
app.app_context().push()

engine= create_engine(url, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
else:
    engine.connect()

import application.routes 