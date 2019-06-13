import time
import datetime as dt

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.web

class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # time.sleep(3)
        yield tornado.gen.sleep(3)
        self.write(str(dt.datetime.now()))

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r'/sleep', SleepHandler),
        ],
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()