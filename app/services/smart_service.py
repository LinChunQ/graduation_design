from app.models.test_paper import TestPaper
from app.extensions import db
import json
from app.utils.MyTool import model_to_dict
import base64
import requests
import sys
from flask import Flask, request

if sys.version_info.major == 2:
    from urllib import quote
else:
    from urllib.parse import quote

recognise_api_url = "https://aip.baidubce.com/rest/2.0/solution/v1/iocr/recognise"
access_token = "24.35a5c96a1f6d6cc1b8c9f81bbea80b44.2592000.1745477152.282335-118175815"
templateSign = "5f26f20073e43c27f7b5ffa526dbc194"

class SmartService:
    @staticmethod
    def grading(user_id):
        try:
            # 接收前端上传的文件对象
            uploaded_file = request.files.get('image')
            if not uploaded_file:
                return {"code": 400, "msg": "未接收到图片文件"}, 400

            # 直接读取文件内容
            image_data = uploaded_file.read()
            image_b64 = base64.b64encode(image_data).decode()
            headers = {
                'Content-Type': "application/x-www-form-urlencoded",
                'charset': "utf-8"
            }
            # 请求模板的bodys
            recognise_bodys = "access_token=" + access_token + "&templateSign=" + templateSign + \
                              "&image=" + quote(image_b64.encode("utf8"))
            # 请求模板识别
            response = requests.post(recognise_api_url, data=recognise_bodys, headers=headers)
            # JSON解析方式
            try:
                response_data = json.loads(response.text)  # 正确解析文本为JSON
            except json.JSONDecodeError as e:
                return {"code": 500, "msg": f"响应解析失败：{str(e)}", "data": None}, 500

            # 根据实际响应结构调整（关键修改点）
            if response_data.get("error_code") != 0:
                return {
                    "code": 500,
                    "msg": f"OCR识别失败：{response_data.get('error_msg', '未知错误')}",
                    "data": None
                }, 500

            # 正确获取数据层级（根据你提供的响应示例）
            actual_data = response_data.get("data", {})
            ret_list = actual_data.get("ret", [])

            # 构建word映射表
            word_mapping = {
                item["word_name"]: item.get("word", "")
                for item in ret_list
                if "word_name" in item  # 确保包含word_name字段
            }

            new_test = TestPaper(
                college=word_mapping["学院"], 
                teacher_id=user_id, 
                stu_class=word_mapping["班级"],
                stu_name=word_mapping["姓名"],
                stu_no=word_mapping["学号"],
                p1=int(word_mapping.get('一', '0')) if word_mapping.get('一', '0').isdigit() else 0,
                p2=int(word_mapping.get('二', '0')) if word_mapping.get('二', '0').isdigit() else 0,
                p3=int(word_mapping.get('三', '0')) if word_mapping.get('三', '0').isdigit() else 0,
                p4=int(word_mapping.get('四', '0')) if word_mapping.get('四', '0').isdigit() else 0,
                p5=int(word_mapping.get('五', '0')) if word_mapping.get('五', '0').isdigit() else 0,
                p6=int(word_mapping.get('六', '0')) if word_mapping.get('六', '0').isdigit() else 0,
                total=0  # 初始化为0，calctotal方法会计算总分
            )
            new_test.calctotal()
            try:
                db.session.add(new_test)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return {"code": 500, "msg": f"数据库插入失败：{str(e)}", "data": None}, 500

            # 重新查询以确保包含test_id
            new_test = TestPaper.query.filter_by(stu_no=new_test.stu_no).first()

            return {
                "code": 200,
                "msg": "识别成功",
                "data": model_to_dict(new_test)
            }, 200

        except Exception as e:
            return {"code": 500, "msg": f"系统异常：{str(e)}", "data": None}, 500