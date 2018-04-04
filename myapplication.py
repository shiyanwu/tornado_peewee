from tornado.web import Application
from views.main import MainHandler
from config import settings


class MyApplication(Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
        ]
        super(MyApplication, self).__init__(handlers, **settings)
