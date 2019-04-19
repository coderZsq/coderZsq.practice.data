# coding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
import redis

app = Flask(__name__)


class Config(object):
    DEBUG = True
    SECRET_KEY = "degw,dhuebdnulhdgywg3g7gbdbcjh,7dltg3bamdg7favfbufgdal2fvh,gfdilwgd3kyfv3b"
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@172.16.23.91:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = '172.16.23.91'
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400


app.config.from_object(Config)

db = SQLAlchemy(app)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

Session(app)

CSRFProtect(app)


@app.route('/index')
def index():

    return 'index page'


if __name__ == '__main__':
    app.run()