#coding:utf-8


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ----------1.跟发件相关的参数------
smtpserver = "smtp.163.com"      # 发件服务器
port = 0                      # 端口
sender = "xxx"         # 账号
psw = "xxx"                         # 密码
receiver = "xxx"        # 接收人

# ----------2.编辑邮件的内容------
# # 读文件
# file_path = "./cc.html"
# with open(file_path, "rb") as fp:
#     mail_body = fp.read()

msg = MIMEMultipart()
msg["from"] = sender                             # 发件人
msg["to"] = receiver                               # 收件人
msg["subject"] = "这个我的主题"             # 主题

# 正文
mail_body = '<h1>Hi</h1><p>test</p>' # 设置邮件正文，这里是支持HTML的

body = MIMEText(mail_body, "html", "utf-8")
msg.attach(body)

# 附件
# att = MIMEText(mail_body, "base64", "utf-8")
# att["Content-Type"] = "application/octet-stream"
# att["Content-Disposition"] = 'attachment; filename="cc1.html"'
# msg.attach(att)

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open(r'stu.xlsx', 'rb').read(), 'base64', "utf-8")
att1["Content-Type"] ='application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="%s"' % os.path.basename(r'stu.xlsx').encode("utf-8")

msg.attach(att1)


# ----------3.发送邮件------
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)  # 连服务器
    smtp.login(sender, psw)   # 登录
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)  # 连服务器
    smtp.login(sender, psw)  # 登录
smtp.sendmail(sender, receiver, msg.as_string())  # 发送
smtp.quit()    # 关闭

