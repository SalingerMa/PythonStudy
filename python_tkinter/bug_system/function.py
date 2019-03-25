# -*- coding: utf-8 -*-
<<<<<<< HEAD
from bug_system.mysqler.mysqler import SQL

class Common:
    @classmethod
    def get_table_data(cls, table):
        data = SQL.select(table)
        table_data = {}
        for item in data:
            table_data[item[0]] = list(item[1:])
        return table_data

    @classmethod
    def get_table_column(cls, table):
        data = SQL.select_column(table)
        return [item[0] for item in data]




if __name__ == '__main__':
    a = Common.get_table_column('submit_bug_of_this_week')
    print(a)
=======
>>>>>>> 7d83a6a9b33b138d28fa022ac530527380262fc8
