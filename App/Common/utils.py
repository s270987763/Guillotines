#!/usr/bin/env python3
#coding:utf-8
from random import sample
import hashlib

#MD5加密
def makePass(pwd):
    m=hashlib.md5()
    m.update(pwd.encode('utf-8'))
    saltpass=m.hexdigest()
    return saltpass

#生成一个10位salt
def randSalt():
    list=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    salt=sample(list,10)
    #把生成的list转换为8位的字符串
    strlist=""
    strlist=strlist.join(salt)
    return str(strlist)