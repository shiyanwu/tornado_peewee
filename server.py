# 引入httpServer模块

import tornado.httpserver

from config import options
from myapplication import MyApplication

# 启动多个进程
if __name__ == "__main__":
    app = MyApplication()
    httpServer = tornado.httpserver.HTTPServer(app)
    httpServer.bind(options["port"])
    httpServer.start(1)
    tornado.ioloop.IOLoop.current().start()
