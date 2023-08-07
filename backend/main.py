# -*- coding: UTF-8 -*-
from flask import Flask


app = Flask(__name__)

#route()函数是一个装饰器，告诉应用程序那个url应该调用（rule,options)
#rule参数表示该函数的url绑定，options是要转发给基础rule对象的参数列表
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user')
def getUserInfor():
    return '<h1>user page</h1>'



if __name__ == '__main__':
    app.run(host="127.0.0.1",port="3333",debug=True)