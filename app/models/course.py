from app.extensions import db

class Course(db.Model):
    __tablename__ = 'course'  # 数据库表名

    course_id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer,db.ForeignKey('users.teacher_id') ,nullable=False) #教师id
    course_name = db.Column(db.String(256), nullable=False)  #课程名称也是试卷名称
    stu_count= db.Column(db.Integer, nullable=False) #课程学生人数
    submit_count = db.Column(db.Integer, nullable=False) #已批改人数
    isDelete = db.Column(db.Boolean, default=False)#判断是否删除
    teacher = db.relationship('User', backref='course')