from app.extensions import db
import json
from app.utils.MyTool import model_to_dict
from app.models.course import Course


class UserService:

    @staticmethod
    def createCourse(data, teacher_id):
        course = Course(course_name=data['course_name'], teacher_id=teacher_id)
        try:
            db.session.add(course)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "创建课程失败!"}, 200
        return {"code": 200, "msg": "创建课程成功!"}, 200

    @staticmethod
    def getCourseById(teacher_id):  # 通过 teacher_id 获取该教师名下所有课程信息
        try:
            courses = Course.query.filter_by(teacher_id=teacher_id).all()
        except Exception as e:
            return {"code": 500, "msg": "获取课程失败!"}, 200
        return [model_to_dict(course) for course in courses], 200

    @staticmethod
    def deleteCourse(data): # 删除课程
        course = Course.query.filter_by(course_id=data['course_id']).first()
        if not course:
            return {"code": 404, "msg": "课程不存在!"}, 404
        try:
            db.session.delete(course)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "删除课程失败!"}, 500
        return {"code": 200, "msg": "删除课程成功!", "data": model_to_dict(course)}, 200

    @staticmethod
    def getTestByCourseId(data, user_id):#根据用户id和课程id获取所有试卷信息
        pass
