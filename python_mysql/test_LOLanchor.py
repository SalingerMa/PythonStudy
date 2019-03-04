# -*- coding: utf-8 -*-

import pymysql
from Spider.PandaTV_LOLrank import Spider
import re

# 连接数据库
def connect_mysql():
    db_host = "localhost"
    db_user = "root"
    db_pwd = "123456"
    db_data = "anchors"
    db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
    return db

# 获取时间
def get_sql_time():
    cursor.execute("select now();")
    data = cursor.fetchall()

    now_ = str(data[0][0]).split(" ")
    day_time = now_[0].split("-")
    hour_time = now_[1].split(":")
    now_time = "a%s%s%s%sa" % (day_time[1], day_time[2], hour_time[0], hour_time[1])

    return now_time

# 查询和创建主播信息
def search_create_anchor_(name):
    if name != "":
        sql_2 = "select * from lolanchor_room_data where name = '%s'" % name
        cursor.execute(sql_2)
        data_2 = cursor.fetchall()
        if data_2 == ():
            sql_1 = "insert into lolanchor_room_data(name) values('%s');" % name
            cursor.execute(sql_1)
            db.commit()

# 创建列名
def create_time_column(time):
    sql_3 = 'alter table lolanchor_room_data add %s char(20);' % time
    cursor.execute(sql_3)
    db.commit()

def update_anchor_data(time, number, name):
    sql_4 = "update lolanchor_room_data set %s = '%s' where name = '%s';" % (time, number, name)
    cursor.execute(sql_4)
    db.commit()

db = connect_mysql()
cursor = db.cursor()

time = get_sql_time()
create_time_column(time)

anchors_data = Spider().go()  # 获取数据
for i in anchors_data:
    rank = str(i["rank"])
    name = str(i["name"])
    str_number = str(i["number"])

    if '万' in str_number:
        int_number2 = float(str_number.replace("万", ""))
        int_number2 *= 10000
        int_number = int(int_number2)

    search_create_anchor_(name)
    update_anchor_data(time, int_number, name)

db.close()

