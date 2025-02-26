from flask import Flask
from app.extensions import db, jwt
from app.blueprints.auth.routes import auth_bp
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)

    # 注册蓝图
    app.register_blueprint(auth_bp)
    # 🚀 打印所有路由
    with app.app_context():
        print(app.url_map)
    return app
