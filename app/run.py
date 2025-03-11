from app import create_app
from app.extensions import db
from flask_cors import CORS
app = create_app()
CORS(app)
# 创建数据库表
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)