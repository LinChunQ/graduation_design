from app.extensions import db

class TestPaper(db.Model):
    __tablename__ = 'test_paper'  # 数据库表名

    test_id = db.Column(db.Integer, primary_key=True)
    college = db.Column(db.String(256), nullable=False)  # 学院
    stu_class = db.Column(db.String(256), nullable=True)  # 班级
    stu_name = db.Column(db.String(64), nullable=True)  # 姓名
    stu_no = db.Column(db.String(128),  nullable=False)  # 学号
    p1 = db.Column(db.Integer,  nullable=True)  #题目一
    p2 = db.Column(db.Integer,  nullable=True)  #题目二
    p3 = db.Column(db.Integer, nullable=True)  # 题目三
    p4 = db.Column(db.Integer, nullable=True)  # 题目四
    p5 = db.Column(db.Integer,  nullable=True)  #题目五
    p6 = db.Column(db.Integer, nullable=True)  # 题目六
    total = db.Column(db.Integer, nullable=True)  #总分

    # 设置密码（加密）
    def calcgrading(self):
        self.total=self.p1+self.p2+self.p3+self.p4+self.p5+self.p6
