from app.extensions import db
from app.models.feedback import FeedBack
from app.models.notice import Notice
from app.models.admin import Admin
from app.models.user import User
from  app.models.notice_type import NoticeType
from datetime import datetime
from app.utils.MyTool import model_to_dict
from flask_mail import Message
from app.extensions import mail
class SystemService:
    @staticmethod
    def addNotice(data,user_id): #添加公告
        username=Admin.query.filter_by(admin_id=user_id).first().username
        # 获取当前时间
        now = datetime.now()
        # 格式化输出
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        notice=Notice(user_id=user_id,username=username,title=data['title'],type=data['type'],
                      content=data['content'],create_time=formatted_time)
        try:
            db.session.add(notice)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": f"添加失败: {str(e)}"}, 200
        return {"code": 200, "msg": "添加成功！"}, 200

    @staticmethod
    def addNoticeType(data): #添加公告类型
        notice_type=NoticeType(name=data['type'])
        notice_type_list=NoticeType.query.filter_by(name=notice_type.name).all()
        if len(notice_type_list)==0:
            try:
                db.session.add(notice_type)
                db.session.commit()
                return {"code": 200, "msg": "添加成功！"}, 200
            except Exception as e:
                db.session.rollback()
                return {"code": 500, "msg": f"添加失败: {str(e)}"}, 200
        else:
            return {"code": 400, "msg": "该类型已存在！"}, 200

    @staticmethod
    def getNotice(data): #获取公告列表
        currentPage = data.get('currentPage', 1)  # 当前页码，默认为1
        pageSize = data.get('pageSize', 10)  # 每页显示的记录数，默认为10
        if currentPage==0 and pageSize==0:
            try:
                noticeList=Notice.query.filter_by().all()
                return {"code": 200, "msg": "", "data": [model_to_dict(notice) for notice in noticeList]}, 200
            except Exception as e:
                return {"code": 500, "msg": "获取通知列表失败!"}, 200

        page = int(currentPage) if currentPage != 0 else 1
        per_page = int(pageSize) if pageSize != 0 else 10
        pagination = Notice.query.filter_by().paginate(page=page, per_page=per_page,error_out=False)
        noticeLists = pagination.items
        return {
            "code":200,
            "data":{
                "data":[model_to_dict(notice) for notice in noticeLists],
                "current_page": pagination.page,
                "per_page": pagination.per_page,
                "total_pages": pagination.pages,
                "total": pagination.total,
            }
        },200

    @staticmethod
    def getNoticeType():
        try:
            notice_type_list = NoticeType.query.filter_by().all()
        except Exception as e:
            return {"code": 500, "msg": "获取失败!"}, 200
        return{"code": 200, "msg": "","data":[model_to_dict(notice_type) for notice_type in notice_type_list]}, 200

    @staticmethod
    def delNotice(data):
        try:
            notice = Notice.query.get(data['id'])  # 先查询
            if notice:
                db.session.delete(notice)  # 再删除
                db.session.commit()
        except Exception as e:
                return {"code": 500, "msg": "删除失败!"}, 200
        return {"code": 200, "msg": "删除成功!"}, 200

    @staticmethod
    def delNoticeType(data):
        try:
            notice_type = NoticeType.query.get(data['id'])  # 先查询
            if notice_type:
                db.session.delete(notice_type)  # 再删除
                db.session.commit()
        except Exception as e:
            return {"code": 500, "msg": "删除失败!"}, 200
        return {"code": 200, "msg": "删除成功!"}, 200

    @staticmethod
    def addFeedBack(data,user_id):
        user=User.query.filter_by(teacher_id=user_id).first()
        # 获取当前时间
        now = datetime.now()
        # 格式化输出
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        feedback=FeedBack(user_id=user_id,username=user.nickname,user_email=user.email,
                          content=data['content'],type=data['type'],process=0,create_time=formatted_time)
        try:
            db.session.add(feedback)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "反馈失败!"}, 200
        return {"code": 200, "msg": "反馈成功，谢谢你的反馈！"}, 200

    @staticmethod
    def getFeedBack(data):  # 获取反馈列表
        currentPage = data.get('currentPage', 1)  # 当前页码，默认为1
        pageSize = data.get('pageSize', 10)  # 每页显示的记录数，默认为10
        if currentPage == 0 and pageSize == 0:
            try:
                feedbackList = FeedBack.query.filter_by().all()
                return {"code": 200, "msg": "", "data": [model_to_dict(fb) for fb in feedbackList]}, 200
            except Exception as e:
                return {"code": 500, "msg": "获取反馈列表失败!"}, 200

        page = int(currentPage) if currentPage != 0 else 1
        per_page = int(pageSize) if pageSize != 0 else 10
        pagination = FeedBack.query.filter_by().paginate(page=page, per_page=per_page, error_out=False)
        fbLists = pagination.items
        good=0 #好评
        bad=0   #差评
        suggest=0   #建议
        other=0 #其他
        for fb in fbLists:
            if fb.type==1:
                good+=1
            elif fb.type==2:
                bad+=1
            elif fb.type==3:
                suggest+=1
            elif fb.type==4:
                other+=1

        return {
            "code": 200,
            "data": {
                "data": [model_to_dict(fb) for fb in fbLists],
                "current_page": pagination.page,
                "per_page": pagination.per_page,
                "total_pages": pagination.pages,
                "total": pagination.total,
                "good":good,
                "bad":bad,
                "suggest":suggest,
                "other":other
            }
        }, 200

    @staticmethod
    def replyFeedBack(data):
        email=data['user_email']
        try:
            feedbackMsg=Message(subject='高校助手反馈回复',recipients=[email],body=f"反馈回复:{data['reply_content']}")
            mail.send(feedbackMsg)
        except  Exception as e:
            return {"code": 500, "msg": "发送邮件失败!"}, 200
        new_feedback = FeedBack.query.filter_by(id=data['id']).first()
        new_feedback.reply_content = data['reply_content']
        new_feedback.process = 1
        try:
            db.session.commit()
            return {"code": 200, "msg": "回复成功!"}, 200
        except Exception as e:
            db.session.rollback()
            return {"code": 500, "msg": "回复失败!"}, 200


