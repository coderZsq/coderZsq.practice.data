# coding:utf-8
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from logging.handlers import RotatingFileHandler
from flask_.utils.commons import ReConverter
import redis
import logging


db = SQLAlchemy()
redis_store = None

logging.basicConfig(level=logging.WARNING)
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    app = Flask(__name__)
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    db.init_app(app)
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    Session(app)
    CSRFProtect(app)
    app.url_map.converters["re"] = ReConverter
    from flask_ import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")
    from flask_ import web_html
    app.register_blueprint(web_html.html)
    return app
