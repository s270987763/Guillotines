#!/usr/bin/env python3
#coding:utf-8
from App.Common.utils import checkxss,checkemail
def checkLogin(db,data):
    try:
        data=json.loads(data)
        email=checkemail(data["email"])
        pwd=makePass(data["password"])
        
        user=db.query(User).filter(User.EMAIL==email).first()
        if user:
            salt=user.SALT
            md5pass=makePass(pwd+salt)
            if user.PWD==md5pass:
                return {"type":"success"}
            else:
                {"type":"error"}
        else:
            {"type":"error"}
    except Exception as e:
        return {"error":e}
