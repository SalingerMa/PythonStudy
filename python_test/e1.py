# -*- coding: utf-8 -*-
from hello import app, mail
from flask_mail import Message
msg = Message('test subject', sender='2953095771@qq.com', recipients=['1725589965@qq.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)