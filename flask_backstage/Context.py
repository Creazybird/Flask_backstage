# Flask背后设计理念之一就是，代码在执行时会处于两种不同的状态（States）.当Flask对象被实例化
# 后在模块层次上应用会隐式处于应用配置状态。一直到第一个请求到达这种隐式才结束
# 应用上下文会在必要时被创建和销毁。它不会在线程间移动，并且也不会在不同的请求之间共享。
# 正因为如此，它是一个存储数据库链接信息回或是别的东西的最佳位。
from flask import Flask ,current_app,request
app=Flask(__name__)

@app.route('/')
def index():
    print(current_app.name) # 返回的就是当前包含app这个实体的.py文件的名字  Context
    return 'hello world'
if __name__=='__main__':
    app.run()