# -*- coding: utf-8 -*-
import pymysql

db_host = 'localhost'
db_user = 'root'
db_pwd = '123456'
db_data = 'bug_system'

db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
cursor = db.cursor()

class SQL:

    @classmethod
    def insert_bookinfo(cls, xs_name, xs_author, bookid, category, status, updatetime):
<<<<<<< HEAD
        sql = ''
=======
        sql = "INSERT INTO ddbook(`xs_name`,`xs_author`, `bookid`, `category`, `status`, `updatetime`) VALUES(%(xs_name)s, %(xs_author)s, %(bookid)s, %(category)s , %(status)s, %(updatetime)s)"

>>>>>>> 7d83a6a9b33b138d28fa022ac530527380262fc8
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
<<<<<<< HEAD
    def select(cls, table):
        sql = "SELECT * FROM %s" % table
        cursor.execute(sql)
        return cursor.fetchall()
    @classmethod
    def select_column(cls, table):
        sql = "select COLUMN_NAME from information_schema.COLUMNS where table_name = %s"
        cursor.execute(sql, table)
        return cursor.fetchall()

# a = SQL.select_column('submit_bug_of_this_week')
=======
    def select(cls, table, ):
        sql = "SELECT * FROM %s" % table
        cursor.execute(sql)
        return cursor.fetchall()


# a = SQL.select('up_table')
>>>>>>> 7d83a6a9b33b138d28fa022ac530527380262fc8
# print(a)
