# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

from app.web import book

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

