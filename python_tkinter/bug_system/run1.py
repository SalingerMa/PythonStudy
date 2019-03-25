# -*- coding: utf-8 -*-
from bug_system import *
from bug_system.table_col import table_col
root.title("BUG SYS")
columns = ("BUG" ,"AND", "IOS", "SER", "H5", "PRO")

BUG = ['Bloker', 'Critical', 'Major', 'Minior']
AND = ['1','3','0','4']
IOS = ['1','3','2','4']
SER = ['2','3','1','2']
H5 = ['1','3','0','2']
PRO = ['2','3','1','0']

up_frame = Frame(root)
rest_frame = Frame(root)


table_col(up_frame, columns, BUG, AND, IOS, SER, H5, PRO)
table_col(rest_frame, columns, BUG, AND, IOS, SER, H5, PRO)
up_frame.pack()
rest_frame.pack()
root.mainloop()  # 进入消息循环
