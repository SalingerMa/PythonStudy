# -*- coding: utf-8 -*-
import pymysql
from Spider.PandaTV_LOLrank import Spider
# 连接数据库
def connect_sql():
    db_host = "localhost"
    db_user = "root"
    db_pwd = "123456"
    db_data = "company"
    db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
    return db

def get_sql_time():
    sql_1 = "select now();"
    cursor.execute(sql_1)
    data = cursor.fetchall()
    now_time = str(data[0][0]).split(" ")[1].replace(":", "")

    return now_time

db = connect_sql()
cursor = db.cursor()
sql_time = get_sql_time()

sql_2 = """CREATE TABLE `%s_rank` (
`rank`  CHAR(20),
`name`  CHAR(20),
`number`  CHAR(25)
)DEFAULT CHARACTER SET=utf8;""" % sql_time
cursor.execute(sql_2)
db.commit()
# 获取数据
anchors_data = Spider().go()
for i in anchors_data:
    rank = str(i["rank"])
    name = str(i["name"])
    number = str(i["number"])
    sql = """INSERT INTO %s_rank() VALUES('%s','%s','%s')"""% (sql_time,rank,name,number)
    cursor.execute(sql)
    db.commit()
db.close()

