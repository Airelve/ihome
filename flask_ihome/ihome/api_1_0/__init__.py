# -*- coding: utf-8 -*-
# @Time    : 18-4-14 下午7:37
# @Author  : Mat

from flask import Blueprint

#创建蓝图对象
api = Blueprint("api",__name__)


from . import  index
