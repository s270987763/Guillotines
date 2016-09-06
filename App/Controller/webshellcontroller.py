#!/usr/bin/env python3
#coding:utf-8

from App.Model.models import WebShell
from sqlalchemy import func
from App.Common.utils import checkxss
from App.Conf.conf import showShellconfig
import json
from App.Common.commclass import WebShellAdmin

def getTotalShell(db):
    num=db.query(func.count(WebShell.ID)).first()
    return str(num[0])

def addOneShell(db,url,password,category):

    try:
        
        webshell=db.query(WebShell).filter(WebShell.URL==url).first()
        if webshell:
            return {"type":"error","info":"URL已存在"}
        else:
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
        #query=query.order_by('id')
        #通常先order_by之后才能调用offset和limit
        #query=query.offset(0)  --设置开始位置
        #query=query.limit(10)  --设置返回多少条
        shells=db.query(WebShell).order_by('ID').offset(start).limit(num).all()
        return '{"type":"success","info":%s}' %(shells)
    except Exception as e:
        return {"type":e}

#验证webshell是否可用    
def checkShell(db,url,pwd):
    try:
        webshell=WebShellAdmin(url,pwd,"echo 1;")
        mdata=webshell.doPost()
        if mdata=="1":
            return True
        else:
            return False
    except Exception as e:
        print(e)
        

