from app.extensions import db
class NoticeType(db.Model):
    __tablename__ = 'notice_type'  # 数据库表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)  # 姓名