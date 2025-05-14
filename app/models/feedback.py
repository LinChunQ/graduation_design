from app.extensions import db

class FeedBack(db.Model):
    __tablename__='feedback'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(64), nullable=False)
    user_email=db.Column(db.String(128), nullable=False)
    content=db.Column(db.String(1024), nullable=True)
    reply_content = db.Column(db.String(1024), nullable=True)
    process=db.Column(db.Integer, nullable=False) #0:未回复 1已回复
    type=db.Column(db.Integer, nullable=False) #0:全部 1:好评 2:差评 3:建议 4:其它
    create_time=db.Column(db.String(64), nullable=False)