# -*- coding: utf-8 -*-
from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello/')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.baidu.com'
    }
    return '<html></html>', 301, headers

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])

