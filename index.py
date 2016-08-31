#!/usr/bin/env python3
#coding:utf-8

from Core.bottle import route,default_app,install,run,request,static_file
from beaker.middleware import SessionMiddleware
from Core.bottle.ext import sqlalchemy
from sqlalchemy import create_engine,Column,Integer,Sequence,String
from sqlalchemy.ext.declarative import declarative_base
from beaker.middleware import SessionMiddleware
from Core.bottle import jinja2_view as view
from Core.bottle import redirect,static_file
from App.Common.utils import makePass,randSalt,checkxss,checkuname,checktel,checkemail
import re,string,logging,json
from Core.bottle import request,template
from App.Controller.userscontroller import checkLogin
from App.Conf.conf import dbconfig


#设置session参数
session_opts = {
    'session.type':'file',               # 以文件的方式保存session
    'session.cookei_expires':360,       # session过期时间为360秒
    'session.data_dir':r'/tmp/sessions/',  # session存放路径
    'sessioni.auto':True
    }

#连接数据库
engine=dbconfig()

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
    s=request.environ.get('beaker.session')
    email=s.get('email',None)
    if not email:
        return redirect('/Login')
    else:
        redirect('/Main/index')

#icon图标
@route('/favicon.ico')
def icon():
    return static_file("favicon.ico",root="Public")


#登陆
@route('/Login')
@view('App/View/Login/index.tpl')
def Login():
    pass

#登陆验证
@route('/Api/checkLogin',method="POST")
def check(db):
    email=request.POST.get('email')
    pwd=request.POST.get('password')
    info=checkLogin(db,email,pwd)
    if info=="sucess":
        s=request.environ.get('beaker.session')
        s['email']=email
        s.save()
    info={"type":info}
    return info

#Main路由
@route('/Main/<path>')
def MainPath(path):
    s=request.environ.get('beaker.session')
    email=s.get('email',None)
    if not email:
        return redirect('/Login')
    return template('App/View/Main/'+path+'.tpl')


#静态文件资源模板
@route('/Public/<filename:re:.*.[css|js||png|jpg|jpeg|gif|eot|svg|ttf|woff|woff2|otf]$>')
def Public(filename):
    return static_file(filename, root="Public")



run(app=app,host="127.0.0.1",debug=True,reloader=True,port="8088")
#run(app=app,host="127.0.0.1",server='gunicorn',port="8088")
