from sqlalchemy import nullsfirst
import random
import string

from app.models.user import User
from app.models.admin import Admin
from app.common.request.response import ResponseHandler
from app.extensions import db,mail
from flask_jwt_extended import create_access_token
from app.utils.MyTool import model_to_dict
from flask_mail import Message
from flask import Flask, request
from app.models.email_captcha import EmailCaptchaModel

class AuthService:
    @staticmethod
    def register(username, sex, age, email, phone, address, school, profession, password): #注册用户
        if User.query.filter_by(username=username).first():
            return {"code": 400, "msg": "该用户名已存在!"}, 200

        new_user = User(username=username, email=email, sex=sex, age=age, phone=phone, address=address, school=school,
                        profession=profession)
        new_user.set_password(password)

        try:
            db.session.add(new_user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": f"注册失败: {str(e)}"}, 200

        return {"code": 200, "msg": "用户注册成功！"}, 200

    @staticmethod
    def get_email_captcha(email):
        # 6位，数字和字母的组成
        source = string.digits * 6
        captcha = random.sample(source, 6)
        # 列表变成字符串
        captcha = "".join(captcha)
        print(captcha)

        # I/O 操作
        message = Message(subject="高校教师助手", recipients=[email], body=f"您的验证码是:{captcha}")
        mail.send(message)

        # 使用数据库存储
        email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
        db.session.add(email_captcha)
        db.session.commit()
        return {"code": 200, "msg": "验证码已发送到邮箱!"},200

    @staticmethod
    def login(username, password,role):#登陆
        if role=='0':
            user = Admin.query.filter_by(username=username).first()
        elif role=='1':
            user = User.query.filter_by(username=username).first()

        if not user:
            return {"code": 400, "msg": "不存在该用户,请注册!"}, 200
        elif not user.check_password(password):
            return {"code": 400, "msg": "用户名或密码错误!"}, 200
        else:
            if role=='0':
                token = create_access_token(identity=str(user.admin_id))
            else:
                token = create_access_token(identity=str(user.teacher_id))
            return {"code": 200, "data": {"token": token}, "msg": "登录成功"}, 200


    @staticmethod
    def getUserInfo(user_id,role): #获取用户信息
        try:
            if role=='0':
                users= Admin.query.filter_by(admin_id=user_id).first()
            elif role=='1':
                users = User.query.filter_by(teacher_id=user_id).first()
            userinfo = model_to_dict(users)
            userinfo.pop('password_hash', None)
            if userinfo:
                return {"code": 200, "data": {"userInfo": userinfo}, "msg": ''}, 200
            return {"code": 404, "msg": "获取个人信息出错"}, 200
        except Exception as e:
            print(e)
            return {"code": 500, "msg": "服务器出错"}, 200
    @staticmethod
    def updateUserInfo(userInfo,user_id,role): #修改用户信息
        try:
            if role=='0':
                user = Admin.query.filter_by(admin_id=user_id).first()
            elif role=='1':
                user = User.query.filter_by(teacher_id=user_id).first()
            user.nickname = userInfo['nickname']
            user.sex = userInfo['sex']
            user.age = userInfo['age']
            user.phone = userInfo['phone']
            user.address = userInfo['address']
            user.school = userInfo['school']
            if role=='1':
                user.profession = userInfo['profession']
            db.session.commit()
            return {"code": 200, "msg": "修改成功"}, 200
        except Exception as e:
            print(e)
            return {"code": 500, "msg": "服务器出错"}, 200