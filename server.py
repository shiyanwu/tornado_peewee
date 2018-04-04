# 引入httpServer模块

from tornado import httpserver, ioloop
from config import options
from myapplication import MyApplication

# 启动多个进程
if __name__ == "__main__":
    app = MyApplication()
    httpServer = httpserver.HTTPServer(app)
    httpServer.bind(options["port"])
    httpServer.start(1)
    ioloop.IOLoop.current().start()
