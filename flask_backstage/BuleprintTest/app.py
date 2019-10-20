from flask import Flask
from BuleprintTest.admin import admin
app = Flask(__name__)
app.register_blueprint(admin,url_prefix='/sb')

@app.route('/')
def index():
    return 'index'


@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

if __name__=='__main__':
    app.run()