# -*- coding: utf-8 -*-
"""
本文用于发送带有附件的邮件

编写步骤：
1. 构造MIMEMultipart对象做为根容器
2. 构造MIMEText对象做为邮件显示内容并附加到根容器
3. 构造MIMEBase对象做为文件附件内容并附加到根容器
　　a. 读入文件内容并格式化
　　b. 设置附件头
4. 设置根容器属性
5. 得到格式化后的完整文本
6. 用smtp发送邮件
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email import utils
import mimetypes
import os.path

class SendEmial():

    def send_file_email(self, receiver, file_name):
        # 参数
        From = "xxx@163.com"
        smtpserver = "smtp.163.com"
        To = receiver  # 收件人
        file_name = file_name  # 文件路径
        server = smtplib.SMTP(smtpserver)
        server.login("xxx", "xxx")  # 仅smtp服务器需要验证时

        # 构造MIMEMultipart对象做为根容器
        main_msg = MIMEMultipart()

        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = MIMEText("Hi", _charset="utf-8")
        main_msg.attach(text_msg)

        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        data = open(file_name, 'rb')
        ctype, encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype,subtype = ctype.split('/', 1)
        file_msg = MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close()
        encoders.encode_base64(file_msg)  # 把附件编码

        ## 设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition',
                            'attachment', filename=basename)
        main_msg.attach(file_msg)

        # 设置根容器属性
        main_msg['From'] = From
        main_msg['To'] = To
        main_msg['Subject'] = "File"
        main_msg['Date'] = utils.formatdate()

        # 得到格式化后的完整文本
        fullText = main_msg.as_string()

        # 用smtp发送邮件
        try:
            server.sendmail(From, To, fullText)
        finally:
            server.quit()



