from tornado.web import *

from model.user import User


class MainHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        user = User.create(
            username="s13",
            password="12345678",
            email="shiyanwushuai@163.com",
            join_date=datetime.datetime.now())
        gen_log.info(user)
