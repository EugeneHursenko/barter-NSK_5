import os
basedir = os.path.abspath(os.path.dirname(__file__))

TIMEZONE='Asia/Novosibirsk'
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite'
SQLALCHEMY_ECHO = False
SECRET_KEY = '!!! Нужно перегрузить в instance/config.py'
