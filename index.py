#!/usr/bin/env python3
#coding:utf-8

from bottle import route,default_app,install,run,request,static_file
from beaker.middleware import SessionMiddleware
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,Sequence,String
from sqlalchemy.ext.declarative import declarative_base
from beaker.middleware import SessionMiddleware
from App.Model.models import ShellDbConfig,User,WebShell
from bottle import jinja2_view as view
from bottle import redirect,static_file
from App.Common.utils import makePass,randSalt

#设置session参数
session_opts = {
    'session.type':'file',               # 以文件的方式保存session
    'session.cookei_expires':360,       # session过期时间为360秒
    'session.data_dir':r'/tmp/sessions/',  # session存放路径
    'sessioni.auto':True
    }

#连接数据库
engine=create_engine('mysql+pymysql://root:root@localhost:3306/guillotines?charset=utf8')

app=default_app()
app = SessionMiddleware(app, session_opts)

Base = declarative_base()

plugin = sqlalchemy.Plugin(
    engine, # SQLAlchemy engine created with create_engine function.
    Base.metadata, # SQLAlchemy metadata, required only if create=True.
    keyword='db', # Keyword used to inject session database in a route (default 'db').
    create=True, # If it is true, execute `metadata.create_all(engine)` when plugin is applied (default False).
    commit=True, # If it is true, plugin commit changes after route is executed (default True).
    use_kwargs=False # If it is true and keyword is not defined, plugin uses **kwargs argument to inject session database (default False).
)

#安装sqlalchemy插件
install(plugin)



#记录访客IP
@route('/')
def index():
    uinfo=list()
    ip=open("ip.txt","a")
    ip.write(request.remote_addr+'\n')
    ip.close()

    return "客观里面请~"

#登陆模板
@route('/Login')
@view('App/View/Login/index.tpl')
def Login():
    pass

#Main路由
@route('/Main')
@view('App/View/Main/index.tpl')
def Main():
    pass

#静态文件资源模板
@route('/Public/<filename:re:.*.[css|js||png|jpg|jpeg|gif|eot|svg|ttf|woff|woff2|otf]$>')
def Public(filename):
    return static_file(filename, root="Public")



run(app=app,host="127.0.0.1",debug="True",port="8088")
#run(app=app,host="127.0.0.1",server='gunicorn',port="8088")
