from os import path

BASE_DIRS = path.dirname(__file__)

# 参数
options = {
    "port": 8088
}

# 数据库配置
mysql_msg = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "root",
    "dbName": "ssm",
    "port": 3306
}

# 配置
settings = {
    "static_path": path.join(BASE_DIRS, "static"),
    "template_path": path.join(BASE_DIRS, "templates"),
    "debug": True,
    # 关闭系统的转义
    # "autoescape": None
}
