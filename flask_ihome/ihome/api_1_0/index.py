# -*- coding: utf-8 -*-
# @Time    : 18-4-14 下午7:39
# @Author  : Mat

import logging
from . import api
from ihome import models

@api.route('/',methods=["GET","POST"])
def index():
    # session["name"] = "banzhang"

    logging.debug("调试信息")
    logging.info("详情信息")
    logging.warning("警告信息")
    logging.error("错误信息")

    return "helloworld"