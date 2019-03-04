# -*- coding: utf-8 -*-
from tkinter import *
from Spider.DownloadBook import *
root = Tk()
root.title("hello world")
root.geometry('400x300+500+300')
root.resizable(width=True, height=True)
var1 = IntVar()
var2 = StringVar()



def download():
    key = var1.get()
    code = code_text.get()
    if key == 1:
        bookname, n, key1 = MingYueBook().run(code)
        text.insert(INSERT, "下载"+bookname+":"+str(n)+"/"+str(key1))
    elif key == 2:
        YunZhongBook().run(code)

frm = Frame(root)
l = Label(frm, text="小说下载", font=("Arial", 15))
l.pack(side=TOP)
frm1 = Frame(frm)
Radiobutton(frm1, text="明月小说网", variable=var1, value=1).pack(side=LEFT)
Radiobutton(frm1, text="云中小说网", variable=var1, value=2).pack(side=RIGHT)
frm1.pack(side=TOP)

code_text = Entry(frm)
code_text.pack(side=TOP)

Button(frm, text="开始", command=download).pack()

text = Text(frm)
text.pack()

frm.pack()


root.mainloop()

