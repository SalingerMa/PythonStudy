# -*- coding: utf-8 -*-
import pymysql

db_host = 'localhost'
db_user = 'root'
db_pwd = 'xls1208'
db_data = 'bug_system'

db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
cursor = db.cursor()

class SQL:

    @classmethod
    def insert_bookinfo(cls, xs_name, xs_author, bookid, category, status, updatetime):
        sql = "INSERT INTO ddbook(`xs_name`,`xs_author`, `bookid`, `category`, `status`, `updatetime`) VALUES(%(xs_name)s, %(xs_author)s, %(bookid)s, %(category)s , %(status)s, %(updatetime)s)"

        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'bookid': bookid,
            'category': category,
            'status': status,
            'updatetime': updatetime,
        }
        cursor.execute(sql, value)
        db.commit()

    @classmethod
    def select(cls, table, ):
        sql = "SELECT * FROM %s" % table
        cursor.execute(sql)
        return cursor.fetchall()


# a = SQL.select('up_table')
# print(a)
