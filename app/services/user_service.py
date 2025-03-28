from sqlalchemy.sql.dml import isdelete

from app.extensions import db
import json

from app.models.test_paper import TestPaper
from app.utils.MyTool import model_to_dict
from app.models.course import Course


class UserService:

    @staticmethod
    def createCourse(data, user_id):
        course = Course(course_name=data['course_name'], teacher_id=user_id,
                        stu_count=data['stu_count'], submit_count=data['submit_count'],
                        isDelete=False)
        try:
            db.session.add(course)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "创建课程失败!"}, 200
        return {"code": 200, "msg": "创建课程成功!"}, 200

    @staticmethod
    def getCourseById(user_id):  # 通过 teacher_id 获取该教师名下所有课程信息
        try:
            courses = Course.query.filter_by(teacher_id=user_id,isDelete=False).all()
        except Exception as e:
            return {"code": 500, "msg": "获取课程失败!"}, 200
        return{"code": 200, "msg": "","data":[model_to_dict(course) for course in courses]}, 200

    @staticmethod
    def deleteCourse(data): # 删除课程
        course = Course.query.filter_by(course_id=data['course_id']).first()
        if not course:
            return {"code": 404, "msg": "课程不存在!"}, 200
        try:
            course.isDelete = True
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "删除课程失败!"}, 200
        return {"code": 200, "msg": "删除课程成功!"}, 200

    @staticmethod
    def updateCourse(data):
        course = Course.query.filter_by(course_id=data['course_id']).first()
        if not course:
            return {"code": 404, "msg": "课程不存在!"}, 200
        try:
            course.course_name = data['course_name']
            course.stu_count = data['stu_count']
            course.submit_count = data['submit_count']
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "更新课程失败!"}, 200
        return {"code": 200, "msg": "更新课程成功!"}, 200

    @staticmethod
    @staticmethod
    def getTestByCourseId(data, user_id):  # 根据用户id和课程id获取所有试卷信息
        course_id = data.get('course_id')
        page = int(data.get('currentPage', 1))  # 当前页码，默认为1
        per_page = int(data.get('pageSize', 10))  # 每页显示的记录数，默认为10
        if course_id == 0:
            try:
                pagination = TestPaper.query.filter_by(teacher_id=user_id).paginate(page=page, per_page=per_page,
                                                                                    error_out=False)
                test_papers = pagination.items
                return {
                    "code": 200,
                    "msg": "",
                    "data":{
                        "data":[model_to_dict(test_paper) for test_paper in test_papers],
                        "current_page": pagination.page,
                        "per_page": pagination.per_page,
                        "total_pages": pagination.pages,
                        "total_items": pagination.total,
                    }
                }, 200
            except Exception as e:
                return {"code": 500, "msg": "获取试卷失败!"}, 200

        try:
            pagination = TestPaper.query.filter_by(course_id=course_id, isDelete=False).paginate(page=page,
                                                                                                 per_page=per_page,
                                                                                                 error_out=False)
            test_papers = pagination.items
            return {
                    "code": 200,
                    "msg": "",
                    "data":{
                        "data":[model_to_dict(test_paper) for test_paper in test_papers],
                        "current_page": pagination.page,
                        "per_page": pagination.per_page,
                        "total_pages": pagination.pages,
                        "total_items": pagination.total,
                    }
                }, 200
        except Exception as e:
            return {"code": 500, "msg": "获取试卷失败!"}, 200