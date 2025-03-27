from app.extensions import db

from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'  # 数据库表名

    teacher_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)  # 用户名用来登陆
    nickname= db.Column(db.String(64), nullable=False) # 昵称
    sex = db.Column(db.String(2), nullable=True)  # 性别
    age = db.Column(db.Integer, nullable=True)  # 年龄
    email = db.Column(db.String(128),  nullable=False)  # 邮件
    phone = db.Column(db.String(32),  nullable=True)  # 手机号
    address = db.Column(db.String(128),  nullable=True)  # 地址
    school = db.Column(db.String(128),  nullable=True)  # 学校
    profession = db.Column(db.String(128),  nullable=True)  # 专业
    password_hash = db.Column(db.String(512), nullable=False)  # 加密密码
    test_papers = db.relationship('TestPaper', backref='user')

    # 设置密码（加密）
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # 验证密码
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
