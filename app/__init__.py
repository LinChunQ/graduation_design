from flask import Flask,jsonify
from app.extensions import db, jwt
from app.blueprints.auth.routes import auth_bp
from app.blueprints.smart.routes import smart_bp
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

    # 注册蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(smart_bp)
    # 🚀 打印所有路由
    with app.app_context():
        print(app.url_map)
    return app
