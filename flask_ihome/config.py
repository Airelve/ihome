# -*- coding: utf-8 -*-
# @Time    : 18-4-14 下午5:37
# @Author  : Mat
import redis


class BaseConfig:
    SECRET_KEY = "EZXRDCFVBHNJYYHRGFCX"

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@localhost:3306/flask_ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session配置
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host = REDIS_HOST,port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 24*3600*2

#     开发模式
class Developer(BaseConfig):
    DEBUG = True

    # 线上模式
class Production(BaseConfig):
    pass

config_dict = {
    'develop':Developer,
    'product':Production
}



























