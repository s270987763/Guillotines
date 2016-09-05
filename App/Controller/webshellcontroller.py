#!/usr/bin/env python3
#coding:utf-8

from App.Model.models import WebShell
from sqlalchemy import func
from App.Common.utils import checkxss
from App.Conf.conf import showShellconfig

def getTotalShell(db):
    num=db.query(func.count(WebShell.ID)).first()
    return str(num[0])

def addOneShell(db,url,password,category):
    
    try:
        shell=WebShell(url,password,category)
        db.add(shell)
        return {"type":"success"}
    except Exception as e:
        return {"type":e}
    

def getShellLists(db,page):
    try:
        num=showShellconfig()
        start=(page-1)*num
        #分页查询
        #query=query.order_by(‘id’)
        #通常先order_by之后才能调用offset和limit
        #query=query.offset(0)  --设置开始位置
        #query=query.limit(10)  --设置返回多少条
        shells=db.query(WebShell).order_by('ID').offset(start).limit(num).all()
        return {"type":"success","info":str(shells)}
    except Exception as e:
        return {"type":e}