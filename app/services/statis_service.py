from app.extensions import db
from app.models.test_paper import TestPaper
from app.models.statistics import DataSta
from app.utils.MyTool import model_to_dict
import numpy as np

class StatisService:
    @staticmethod
    def getStaById(data, user_id):
        course_id = data['course_id']
        try:
            test_paper_list=TestPaper.query.filter_by(course_id=course_id,isDelete=False).all()
            if test_paper_list:
                scores = [p.total for p in test_paper_list]
                DataSta.sum_cnt=len(scores)
                DataSta.median=float(np.median(scores))
                DataSta.mean=float(np.mean(scores))
                DataSta.max=float(np.max(scores))
                DataSta.min=float(np.min(scores))
                DataSta.teacher_id=user_id
                DataSta.course_id=course_id
                DataSta.course_name=TestPaper.query.filter_by(course_id=course_id,isDelete=False).first().course_name
                DataSta.isNeedUpdate=False
                DataSta.isDelete = False
                db.session.add(DataSta)
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "数据分析失败!"}, 200
        return {"code": 200, "msg": "数据分析成功!"}, 200



