#!/usr/bin/env python3
#coding:utf-8

from App.Model.models import WebShell
from sqlalchemy import func
from App.Common.utils import checkxss

def getTotalShell(db):
    num=db.query(func.count(WebShell.ID)).first()
    return str(num[0])

def addOneShell(db,url,password,category):
    
    try:
        shell=WebShell(url,password,category)
        db.add(shell)
    except Exception as e:
        return {"type":e}