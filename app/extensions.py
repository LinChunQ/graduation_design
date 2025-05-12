from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail

# 初始化数据库和 JWT
db = SQLAlchemy()
jwt = JWTManager()

#初始化邮箱
mail=Mail()