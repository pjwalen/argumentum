"""
    Argumentum

    Web application for moderating an argument.
    Written By: Patrick Walentiny and Matthew Byrne
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class default_settings(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


application = Flask(__name__)
application.secret_key = os.urandom(24)
application.config.from_object('argumentum.default_settings')
db = SQLAlchemy(application)


@application.before_first_request
def createdb():
    db.create_all()


from argumentum.views import *
