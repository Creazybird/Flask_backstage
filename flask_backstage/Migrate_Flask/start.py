import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from flask import Flask
from Migrate_Flask.dbutil import db
import Migrate_Flask.config as config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def helloWorld():
    return 'hello World!!!!!!!!!!!!'


if __name__ == '__main__':
    app.run(debug=True)
