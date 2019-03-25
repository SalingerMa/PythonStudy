# -*- coding: utf-8 -*-
from common.mysqler import SQL

class Common:
    @classmethod
    def get_table_data(cls, table):
        """
        :param table:
        :return:{'Minor': [3, 0, 4, 1, 0], 'Bloker': [2, 10, 2, 1, 0], 'Major': [0, 15, 6, 0, 3], 'Critical': [3, 2, 1, 0, 3]}
        """
        data = SQL.select(table)
        table_data = {}
        for item in data:
            table_data[item[0]] = list(item[1:])
        return table_data

    @classmethod
    def get_table_column(cls, table):
        """
        :param table:
        :return: ['bug_id', 'AND', 'IOS', 'H5', 'SER', 'PRO']
        """
        data = SQL.select_column(table)
        return [item[0] for item in data]





if __name__ == '__main__':
    a = Common.get_table_data('up_table')
    print(a)
