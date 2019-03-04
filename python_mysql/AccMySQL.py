# -*- coding: utf-8 -*-
import pymysql

db_host = "localhost"
db_user = "root"
db_pwd = "123456"
db_data = "company"
db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
cursor = db.cursor()
sql_1 = """create table cd(a int(2));"""
cursor.execute(sql_1)
db.commit()
sql_2 = "insert into cd(a) VALUES(1)"
cursor.execute(sql_2)
db.commit()
db.close()


