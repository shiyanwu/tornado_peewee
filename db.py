from peewee import MySQLDatabase

from config import mysql_msg

db = MySQLDatabase('ssm', user=mysql_msg["user"], password=mysql_msg["password"],
                         host=mysql_msg["host"], port=mysql_msg["port"])
