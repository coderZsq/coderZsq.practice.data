# coding:utf-8
import redis


class Config(object):
    SECRET_KEY = "degw,dhuebdnulhdgywg3g7gbdbcjh,7dltg3bamdg7favfbufgdal2fvh,gfdilwgd3kyfv3b"
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@172.16.23.91:3306/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    REDIS_HOST = '172.16.23.91'
    REDIS_PORT = 6379
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}