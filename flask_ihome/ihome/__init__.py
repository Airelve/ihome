# -*- coding: utf-8 -*-
# @Time    : 18-4-14 下午5:56
# @Author  : Mat

import logging
from logging.handlers import RotatingFileHandler

from flask import Flask,session
from flask_session import Session #用来指定session存储的位置
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config_dict

db = SQLAlchemy()

def create_app(config_name):
    log_file()

    app = Flask(__name__)
    config = config_dict.get(config_name)
    app.config.from_object(config)

    Session(app)
    # 数据库绑定app
    db.init_app(app)
    # 配置csrf
    CSRFProtect(app)
    from ihome.api_1_0 import api
    app.register_blueprint(api)

    return app


def log_file():

    # 设置日志的记录等级
    logging.basicConfig(level=logging.DEBUG)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1000, backupCount=10)
    # 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日记录器
    logging.getLogger().addHandler(file_log_handler)
