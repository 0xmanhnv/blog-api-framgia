import os

#config database
# SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:18031997@localhost/python?charset=utf8"
SQLALCHEMY_DATABASE_URI = "postgres://bhaywtwdwtfndd:2a23b212032d84a776e97e160c55421da81cc50b92ce712d712eda079527f408@ec2-54-243-150-10.compute-1.amazonaws.com:5432/d378ta5vd7qv2v"
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Secret key for signing cookies
# SECRET_KEY = os.urandom(16)
SECRET_KEY = 'SECRET_KEY'
APP_URL = 'http://127.0.0.1:5000'
MYSQL_DATABASE_CHARSET = 'utf8mb4'
CORS_HEADERS='Content-Type'