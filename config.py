import os

#config database
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:18031997@localhost/python?charset=utf8"
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Secret key for signing cookies
# SECRET_KEY = os.urandom(16)
SECRET_KEY = 'SECRET_KEY'
APP_URL = 'http://127.0.0.1:5000'
MYSQL_DATABASE_CHARSET = 'utf8mb4'