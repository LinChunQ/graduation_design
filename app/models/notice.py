from app.extensions import db
class Notice(db.Model):
    __tablename__ = 'notice'  # 数据库表名
    id = db.Column(db.Integer, primary_key=True)
    user_id=db.Column(db.String(255),nullable=False) #发布人id
    username = db.Column(db.String(64), nullable=False)  # 发布人用户名
    title = db.Column(db.String(255), nullable=True)  # 标题
    type = db.Column(db.Integer, nullable=False)  #公告类型
    content = db.Column(db.String(1024), nullable=False)  # 公告内容
    create_time=db.Column(db.String(128),nullable=False) #发布时间