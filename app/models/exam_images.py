from app.extensions import db
from datetime import datetime


class ExamImages(db.Model):
    __tablename__ = 'exam_images'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    templateSign = db.Column(db.String(64), nullable=False)
    templateName = db.Column(db.String(128), nullable=False)
    word_name = db.Column(db.String(64), nullable=False)  # 例如：姓名、学号
    word = db.Column(db.String(128), nullable=False)      # 识别出的值
    probability_average = db.Column(db.Float, nullable=True)
    probability_min = db.Column(db.Float, nullable=True)
    probability_variance = db.Column(db.Float, nullable=True)
    location_top = db.Column(db.Integer, nullable=True)
    location_left = db.Column(db.Integer, nullable=True)
    location_width = db.Column(db.Integer, nullable=True)
    location_height = db.Column(db.Integer, nullable=True)
    templateMatchDegree = db.Column(db.Float, nullable=True)
    clockwiseAngle = db.Column(db.Float, nullable=True)
    logId = db.Column(db.BigInteger, nullable=False)
    scores = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
