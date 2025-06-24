from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
import redis
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()
server_ip = os.getenv("SERVER_IP")
redis_password = os.getenv("REDIS_PASSWORD")
# 初始化数据库和 JWT
db = SQLAlchemy()
jwt = JWTManager()
# 配置Redis
redis_client = redis.Redis(host=server_ip, password=redis_password, port=6379, db=0,decode_responses=True )

#初始化邮箱
mail=Mail()