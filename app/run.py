from flask import make_response

from app import create_app
from app.extensions import db

app = create_app()


# 创建数据库表
with app.app_context():
    db.create_all()



if __name__ == '__main__':
    #app.run(debug=True, use_debugger=False, use_reloader=False)  # 获得更清晰日志
    app.run(host='0.0.0.0', port=5000, debug=True) ##部署到服务器
