import time
import datetime as dt

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado import gen
from tornado import httpclient
import requests

N = 3
URL = 'http://localhost:8888/sleep'
@gen.coroutine
def main():
    http_client = httpclient.AsyncHTTPClient()
    response = yield [
        http_client.fetch(URL) for i in range(N)
    ]

bg1 = time.time()
tornado.ioloop.IOLoop.current().run_sync(main)
print('async', time.time()-bg1)


# 同步请求方式
bg = time.time()
for i in range(N):
    requests.get(URL)

print('req', time.time()-bg)