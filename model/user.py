from peewee import CharField, DateTimeField
from peewee import Model
from db import db


class BaseModel(Model):
    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([User])


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()
