from dotenv import load_dotenv
import os

from flask.json import dump 

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO')
WTF_CSRF_ENABLED=os.getenv('WTF_CSRF_ENABLED')