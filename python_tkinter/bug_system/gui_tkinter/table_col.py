# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

def table_col(frame, columns, BUG, AND, IOS, SER, H5, PRO):

    treeview = ttk.Treeview(frame, height=5, show="headings", columns=columns,)  # 表格
    for column in columns:
        treeview.column(column, width=60, anchor='center') # 表示列,不显示
        treeview.heading(column, text=column)  # 显示表头
        treeview.pack(side=LEFT, fill=BOTH)


    for i in range(len(BUG)):  # 写入数据
        treeview.insert('', i, values=(BUG[i], AND[i], IOS[i], SER[i], H5[i], PRO[i]))

    def set_cell_value(event):  # 双击进入编辑状态
        for item in treeview.selection():
            item_text = treeview.item(item, "values")
        # item_text = treeview.item(treeview.selection(), "values")
        column = treeview.identify_column(event.x)  # 列
        row = treeview.identify_row(event.y)  # 行
        cn = int(str(column).replace('#', ''))
        rn = int(str(row).replace('I', ''))
        entryedit = Text(frame, width=10, height=1)
        entryedit.place(x=(cn - 1) * 60, y=rn * 20)
        def saveedit():
            treeview.set(item, column=column, value=entryedit.get(0.0, "end"))
            entryedit.destroy()
            okb.destroy()
        okb = ttk.Button(frame, text='OK', width=4, command=saveedit)
        okb.place(x=cn * 60, y=rn * 20)

    treeview.bind('<Double-1>', set_cell_value)  # 双击左键进入编辑

