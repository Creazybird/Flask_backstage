# -*- coding: UTF-8 -*-
from flask import Flask, jsonify, abort, render_template
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def init():
    return 'hello world'


@app.route('/test')
def test():
    return 'This is a test'


# 使用jsonify,生成json数据响应体
@app.route('/response')
def demo():
    # 返回给前端的数据，设计成json数据格式
    # python中是字典数据类型
    data = {
        "user_id": 1,
        "name": 'guanguan',
    }
    return jsonify(data)


# 生成文本响应体 ,感觉用不到，网页的跳转还是交给vue 前端来做
@app.route('/response2')
def demo2():
    return redirect('http://www.baidu.com')


# 生成状态码
@app.route('/response3')
def demo3():
    return '状态码', 200


# 异常处理
# 1.abort 异常抛出
#   abort(code)  :主动抛出异常状态码

# 2.errorhandler  异常捕获  用来监听捕获异常，返回自定义的页面处理

@app.route('/game/<int:age>')
def play_game(age):
    abort(404)
    return 'helloworld'


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return "找不到服务器资源， I can not find "


# 请求钩子（很重要，设计到数据库的连接，权限的验证）
# 在在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：
#
# 在请求开始时，建立数据库连接；
# 在请求开始时，根据需求进行权限校验；
# 在请求结束时，指定数据的交互格式；
# 为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。


# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("在第一次请求之前调用")  # 第二次请求就不会调用此函数


# 在每次请求之前调用
@app.before_request
def before_request_test():
    print("我会在每次请求之前都会调用，哈哈哈哈哈哈")


# after_request 的视图函数会在每次请求执行完毕之后执行(前提：如果没有抛出错误)
# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入，
# 可以在次方法中对响应做最后一步统一处理 ，在这个函数将可以修改响应内容的格式
@app.after_request
def after(response):
    print('执行完响应后，我会被执行')
    response.headers['Content-Type'] = 'application/json'
    return response


# teardown_request:在每次请求后执行，（不管请求是否成功），
# 接收一个参数：用来接收错误信息

@app.teardown_request
def teardown_request_1(e):  # 视图函数的名字可以随便取 e代表错误参数
    print('我在每次请求之后执行，无论请求是否成功')
    print(e)

# 尝试写人生中第一个接口
@app.route('/gets')
def api_get():
    data={
        'name':'guanzhong',
        'job':'man',
        'women':'123123'
    }
    return  jsonify(data)

if __name__ == '__main__':
    app.run()
