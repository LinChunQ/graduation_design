from flask import Flask
from app.extensions import db, jwt,mail
from app.blueprints.auth_routes import auth_bp
from app.blueprints.smart_routes import smart_bp
from app.blueprints.user_routes import user_bp
from app.config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app,
         resources={r"/*": {"origins": "http://localhost:5173"}},
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"])

    # 初始化扩展
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    # 注册蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(smart_bp)
    app.register_blueprint(user_bp)
    # # 🚀 打印所有路由
    # with app.app_context():
    #     print(app.url_map)
    return app
