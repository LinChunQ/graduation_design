from flask import request, jsonify, Blueprint
from app.services.user_service import UserService
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint('user', __name__, url_prefix='/user')

#智能打分
@user_bp.route('/addCourse', methods=['POST'])
@jwt_required()  # JWT 认证保护
def createCourse(): # 创建课程
    user_id = get_jwt_identity()
    data=request.json
    result, status_code=UserService.createCourse(data,user_id)
    return jsonify(result), status_code

@user_bp.route('/getCourseById', methods=['GET'])
@jwt_required()  # JWT 认证保护
def getCourseById(): #通过id获取课程
    user_id = get_jwt_identity()
    result, status_code=UserService.getCourseById(user_id)
    return jsonify(result), status_code


@user_bp.route('/deleteCourse', methods=['POST'])
@jwt_required()  # JWT 认证保护
def deleteCourse(): #删除课程
    data=request.json
    result, status_code = UserService.deleteCourse(data)
    return jsonify(result), status_code

@user_bp.route('/updateCourse', methods=['POST'])
@jwt_required()
def updateCourse():
    data=request.json
    result, status_code = UserService.updateCourse(data)
    return jsonify(result), status_code

@user_bp.route('/getTestByCourseId', methods=['POST'])
@jwt_required()
def getTestByCourseId():#通过课程id获取试卷 若课程id为0则获取全部课程
    user_id = get_jwt_identity()
    data=request.json
    result, status_code = UserService.getTestByCourseId(data,user_id)
    return jsonify(result), status_code

