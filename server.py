# 引入httpServer模块

from tornado import httpserver, ioloop, options
from config import m_options
from myapplication import MyApplication

# 启动多个进程
if __name__ == "__main__":
    app = MyApplication()
    options.parse_command_line()
    httpServer = httpserver.HTTPServer(app)
    httpServer.bind(m_options["port"])
    httpServer.start()
    ioloop.IOLoop.current().start()
