# _*_ coding:utf-8 _*_
# Project Name: watchlist
# File Name: app
# Author： rockche
# Date:  2020/11/18  5:02 下午
# Description : 程序主页
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

