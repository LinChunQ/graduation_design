from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
import redis
# 初始化数据库和 JWT
db = SQLAlchemy()
jwt = JWTManager()
# 配置Redis
redis_client = redis.Redis(host='114.55.218.3', password='QQ1314520', port=6379, db=0,decode_responses=True )

#初始化邮箱
mail=Mail()