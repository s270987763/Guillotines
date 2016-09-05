#!/usr/bin/env python3
#coding:utf-8

from sqlalchemy import create_engine

def dbconfig():
    engine=create_engine('mysql+pymysql://root:741521@localhost:3306/gu?charset=utf8')
    return engine

def showShellconfig():
    #每页显示20个webshell
    return 20
