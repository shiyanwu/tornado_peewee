from peewee import CharField, DateTimeField
from peewee import MySQLDatabase, Model
from config import mysql_msg

mysql_db = MySQLDatabase('ssm', user=mysql_msg["user"], password=mysql_msg["password"],
                         host=mysql_msg["host"], port=mysql_msg["port"])


class BaseModel(Model):
    class Meta:
        database = mysql_db


def create_tables():
    with mysql_db:
        mysql_db.create_tables([User])


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()
