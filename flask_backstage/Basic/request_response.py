# 理解 http 协议中的request和response对象
# 理解flask中的请求上下文
from flask import request,current_app,g
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    #程序员需要在这个函数里看到浏览器中发送过来的request,直接调用flask中的request 请求上下文
    user_aget=request.headers.get('User-Agent')
    host=request.headers.get('Host')
    re=request.headers
    current=current_app.name
    #return '<h1>请求上下文<h1> %s'%re
    return '<h1>应用上下文<h1>%s'%current

@app.route('/get')
def get():
    re=request.headers
    #不同视图函数中的请求函数是相互独立的， index和get中的request.XX是相互独立的
    # 是分别属于自己的请求
    # 额外补充：这里应该是flask中已经实现了的东西：
        # 在多线程服务器中，多个线程同时处理不同客户端发送的不同请求时，每个线程
        # 看到的request对象必然是不同。Flask使用上下文听特定的变量在一个线程中全局
        #  可访问，与此同时不会干扰其他线程

    return '<h1>比较不同视图函数中的请求体</h1>'+re

if __name__=='__main__':
    print(app.url_map)  #查看Flask应用程序中的url映射
    app.run(debug=True)

