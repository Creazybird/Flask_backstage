from flask_script import Shell, Manager
from flask import Flask
app=Flask(__name__)
manager=Manager(app)


if __name__=='__main__':
    #app.run() 不在使用app.run()
    manager.run()
