from app import create_app
from app.extensions import db
from flask_cors import CORS
app = create_app()
CORS(app, origins="http://localhost:5173", supports_credentials=True)
# 创建数据库表
with app.app_context():
    db.create_all()


@app.after_request
def set_default_headers(response):
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


if __name__ == '__main__':
    app.run(debug=True)