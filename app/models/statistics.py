from app.extensions import db

class DataSta(db.Model):
    __tablename__ = 'statistics'  # 数据库表名
    sta_id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, nullable=False)  # 教师id
    course_id = db.Column(db.Integer,nullable=False) #课程id
    course_name = db.Column(db.String(256), nullable=True)  #课程名称也是试卷名称
    median = db.Column(db.Numeric(5, 2), nullable=True) #该课程总分的中位数
    mean = db.Column(db.Numeric(5, 2), nullable=True) #该课程总分的平均数
    min = db.Column(db.Numeric(5, 2), nullable=True) #该课程总分的最小数
    max = db.Column(db.Numeric(5, 2), nullable=True) #该课程总分的最大数
    failure_cnt = db.Column(db.Integer,nullable=True) #不及格人数
    pass_cnt = db.Column(db.Integer,nullable=True) #及格人数
    good_cnt = db.Column(db.Integer,nullable=True) #良好人数
    excellent_cnt=db.Column(db.Integer,nullable=True) #优秀人数
    sum_cnt = db.Column(db.Integer, nullable=True)  # 该课程的总人数
    mean_p1 = db.Column(db.Numeric(5, 2), nullable=True)  # 该课程题目一的平均数
    mean_p2 = db.Column(db.Numeric(5, 2), nullable=True)  # 该课程题目二的平均数
    mean_p3 = db.Column(db.Numeric(5, 2), nullable=True)  # 该课程题目三的平均数
    mean_p4 = db.Column(db.Numeric(5, 2), nullable=True)  # 该课程题目四的平均数
    mean_p5 = db.Column(db.Numeric(5, 2), nullable=True)  # 该课程题目五的平均数
    mean_p6 = db.Column(db.Numeric(5, 2), nullable=True)  # 该课程题目六的平均数
    isNeedUpdate = db.Column(db.Boolean, default=True)#判断是否需要更新
    isDelete = db.Column(db.Boolean, default=False)#判断是否删除