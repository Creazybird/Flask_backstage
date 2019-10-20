# -*- coding: UTF-8 -*-
# 链接数据库
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 链接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bird@127.0.0.1:3306/expertcommisson'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

DB = SQLAlchemy(app)


class Organization(DB.Model):
    __tablename__ = 'organization'
    OrganizationId = DB.Column(DB.Integer, primary_key=True)
    Name = DB.Column(DB.String(64))
    OrganizationTypeId = DB.Column(DB.Integer)
    Deleted = DB.Column(DB.Integer)

    def __repr__(self):
        return 'organization 内容：%s%s' % self.id % self.name


if __name__ == '__main__':
    TEST=Organization(OrganizationId=3,Name='你好ma',OrganizationTypeId=3,Deleted=1)
    DB.session.add(TEST)
    DB.session.commit()
    app.run()
