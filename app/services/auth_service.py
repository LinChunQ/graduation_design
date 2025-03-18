from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token
import json
from app.utils.MyTool import model_to_dict


class AuthService:
    @staticmethod
    def register(username, sex, age, email, phone, address, school, profession, password):
        if User.query.filter_by(username=username).first():
            return {"code": 400, "msg": "Username already exists"}, 200

        new_user = User(username=username, email=email, sex=sex, age=age, phone=phone, address=address, school=school,
                        profession=profession)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": f"Registration failed: {str(e)}"}, 200

        return {"code": 200, "msg": "User registered successfully"}, 200

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            token = create_access_token(identity=str(user.teacher_id))
            return {"code": 200, "data": {"token": token}, "msg": "登录成功"}, 200
        return {"code": 400, "msg": "用户名或密码错误!"}, 200

    @staticmethod
    def getUserInfo(user_id):
        try:
            users = User.query.filter_by(teacher_id=user_id).first()
            userinfo = model_to_dict(users)
            # 使用 pop 删除指定的键，pop 会返回删除的值，但我们这里不需要返回值
            userinfo.pop('teacher_id', None)  # 如果键不存在，返回 None 不会抛出异常
            userinfo.pop('password_hash', None)

            if userinfo:
                return {"code": 200, "data": {"userInfo": userinfo}, "msg": ''}, 200
            return {"code": 404, "msg": "获取个人信息出错"}, 200
        except Exception as e:
            print(e)
            return {"code": 500, "msg": "服务器出错"}, 200