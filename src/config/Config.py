import configparser
import os
import random
import string
"""Flask config class."""
import os


class BaseConfig:
    """Base config vars."""
    SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@localhost/code"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #DEBUG = True
    