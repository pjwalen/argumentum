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

if 'RDS_HOSTNAME' in os.environ:
    application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOSTNAME}:{RDS_PORT}/{RDS_DB_NAME}'.format(**os.environ)

db = SQLAlchemy(application)

from argumentum.controllers import *
from argumentum.utils import create_demo_data


@application.before_first_request
def createdb():
    db.create_all()
    if Argument.query.count() == 0:
        create_demo_data()
