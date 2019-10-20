from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/list')
def list():
    return 'list'

@app.route('/detail')
def detail():
    return 'detail'

@app.route('/')
def admin_hone():
    return 'admin_home'

@app.route('/new')
def new():
    return 'new'

@app.route('/edit')
def edit():
    return 'edit'

@app.route('/publish')
def publish():
    return 'publish'

#问题：随着共能的增加，路由的不断增多，这个.py文件会变成的非常大，将来维护起来会非常麻烦
# 此时想到了模块化的处理方式，将admin相关的路由写道一个admin.py文件
# 在flask中提供了Blueprint类，来专门处理模块化开发

if __name__=='__main__':
    app.run()