# -*- coding: utf-8 -*-
# @Time    : 18-4-14 下午3:46
# @Author  : Mat
from flask.ext.migrate import Migrate,MigrateCommand
from flask.ext.script import Manager
from ihome import db
from ihome import create_app

# 获取app
app = create_app("develop")
#数据库配置
#redis配置
#session配置
#创建应用程序管理对象
manager = Manager(app)
#关联app和db
Migrate(app,db)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()



