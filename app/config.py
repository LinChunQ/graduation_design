from datetime import timedelta
from dotenv import load_dotenv
import os

# 加载 .env 文件
load_dotenv()
db_password = os.getenv("DB_PASSWORD")
server_ip = os.getenv("SERVER_IP")

class Config:
    # 数据库
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:{db_password}@{server_ip}:3306/uga-flask?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    #JWT
    JWT_SECRET_KEY = 'uga12345678'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = ''
    JSON_AS_ASCII= False  # 确保 JSON 响应中非 ASCII 字符不被转义
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    #QQ邮箱
    # 邮箱配置
    MAIL_SERVER = "smtp.qq.com"
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    #个人的邮箱
    MAIL_USERNAME = "497603213@qq.com"
    #获取到的授权码
    MAIL_PASSWORD = "bfrlhaeeujclcach"
    # 你的邮箱名字可以和MAIL_USERNAME一样
    MAIL_DEFAULT_SENDER = "497603213@qq.com"


