from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
# 初始化数据库和 JWT
db = SQLAlchemy()
jwt = JWTManager()
