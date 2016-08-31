#!/usr/bin/env python3
#coding:utf-8
from sqlalchemy import create_engine,Column,Integer,Sequence,String,DateTime,Float
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class ShellDbConfig(Base):
    __tablename__='gu_shelldbconf'
    ID=Column(Integer,Sequence('id_seq'), primary_key=True)
    HOST=Column(String(128))
    PORT=Column(String(5))
    PWD=Column(String(32))
    CREATE_TIME=Column(DateTime)
    
    def __init__(self,host,port,pwd):
        self.HOST=host
        self.PORT=port
        self.PWD=pwd
        
    def __repr__(self):
        return "<gu_shelldbconf('%s,%s,%s')>" % (self.HOST,self.PORT,self.PWD)
    
    
class User(Base):
    __tablename__='gu_users'
    ID=Column(Integer,Sequence('id_seq'), primary_key=True)
    NAME=Column(String(32))
    EMAIL=Column(String(100))
    PWD=Column(String(32))
    SALT=Column(String(10))
    UTYPE=Column(String(10))
    CREATE_TIME=Column(DateTime)
    
    def __init__(self,name,email,pwd,salt,utype):
        self.NAME=name
        self.EMAIL=email
        self.PWD=pwd
        self.SALT=salt
        self.UTYPE=utype
        
    
    def __repr__(self):
        return "<User('%s,%s,%s,%s,%s')>" % (self.NAME,self.EMAIL,self.PWD,self.SALT,self.UTYPE)
    

class WebShell(Base):
    __tablename__='gu_webshell'
    ID=Column(Integer,Sequence('id_seq'), primary_key=True)
    URL=Column(String(255),unique=True,index=True)
    PWD=Column(String(32))
    IP=Column(String(128))
    IP_ADDRESS=Column(String(255))
    CATEGORY=Column(String(6))
    CREATE_TIME=Column(DateTime)
    HTTPCODE=Column(String(3))
    BR=Column(Integer)
    PR=Column(Integer)
    
    def __init__(self,url,pwd,ip,address,category,httpcode,br,pr):
        self.URL=url
        self.PWD=pwd
        self.IP=ip
        self.IP_ADDRESS=address
        self.CATEGORY=category
        self.HTTPCODE=httpcode
        self.BR=br
        self.PR=pr
        
    def __repr__(self):
        return "<Webshell('%s,%s,%s,%s,%s,%s,%s,%s')>"  % (self.URL,self.PWD,self.IP,self.IP_ADDRESS,self.CATEGORY,self.HTTPCODE,self.BR,self.PR)
    
    
    
    
    
    
