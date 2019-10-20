# 进行数据迁移
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from Migrate_Flask.start import app
from Migrate_Flask.dbutil import db
from Migrate_Flask.Model import Author,Book  # 这行代码虽然在本文件没有使用，但是迁移数据库的时候会用到，如果不加，迁移的数据库为空
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('dbcommand',MigrateCommand)

if __name__=='__main__':
    manager.run()
