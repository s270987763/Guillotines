from sqlalchemy import create_engine

def dbconfig():
    engine=create_engine('mysql+pymysql://root:root@localhost:3306/guillotines?charset=utf8')
    return engine
