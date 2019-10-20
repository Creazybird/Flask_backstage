# 为了防止csrf攻击 flask中有设计专门的机制来应对，生成token
# flask_wtf模块提供了csrf攻击的保护

# 请求中的post put dispatch delete 4种类型的请求保护，因为这些类型的请求
# 用于更改服务器的资源，对以上4种类型的请求，操作服务器资源的时候，会校验cookie中
# 的csrf_token ,表单中的csrf_token信息
# 只有哦上面二者的值相等的时候，那么校验则通过，可以操作服务器资源

# 在这个技术中要用到secret_key  本质上是一个加密盐

from flask import Flask, render_template
from flask_wtf import CSRFProtect

app = Flask(__name__)

# 设置盐值

app.config['SECRET_KEY'] = 'GZWINGSHI'

CSRFProtect(app)


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/add', methods=['POST'])
def add():
    return '登陆成功'


if __name__ == '__main__':
    app.run()
