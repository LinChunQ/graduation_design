from flask import request, jsonify, Blueprint
from app.services.sys_service import SystemService
from flask_jwt_extended import jwt_required, get_jwt_identity

sys_bp = Blueprint('sys', __name__, url_prefix='/sys')
@sys_bp.route('/addNotice', methods=['POST'])
@jwt_required()
def addNotice(): #添加公告
    user_id = get_jwt_identity()
    data=request.json
    result, status_code=SystemService.addNotice(data,user_id)
    return jsonify(result), status_code

@sys_bp.route('/getNotice',methods=['POST'])
def getNotice(): #获取公告
    data=request.json
    result, status_code = SystemService.getNotice(data)
    return jsonify(result), status_code

@sys_bp.route('/delNotice',methods=['POST'])
@jwt_required()
def delNotice(): #删除公告
    data = request.json
    result, status_code = SystemService.delNotice(data)
    return jsonify(result), status_code

@sys_bp.route('/addNoticeType', methods=['POST'])
@jwt_required()
def addNoticeType(): #添加公告类型
    data=request.json
    result, status_code=SystemService.addNoticeType(data)
    return jsonify(result), status_code

@sys_bp.route('/getNoticeType',methods=['POST'])
@jwt_required()
def getNoticeType(): #获取公告类型
    result, status_code = SystemService.getNoticeType()
    return jsonify(result), status_code

@sys_bp.route('/delNoticeType',methods=['POST'])
@jwt_required()
def delNoticeType(): #删除公告类型
    data = request.json
    result, status_code = SystemService.delNoticeType(data)
    return jsonify(result), status_code

@sys_bp.route('/addFeedBack', methods=['POST'])
@jwt_required()
def addFeedBack(): #添加反馈
    user_id=get_jwt_identity()
    data=request.json
    result, status_code=SystemService.addFeedBack(data,user_id)
    return jsonify(result), status_code

@sys_bp.route('/getFeedBack', methods=['POST'])
@jwt_required()
def getFeedBack(): #获取反馈根据反馈类型
    data=request.json
    result, status_code=SystemService.getFeedBack(data)
    return jsonify(result), status_code

@sys_bp.route('/replyFeedBack', methods=['POST'])
@jwt_required()
def replyFeedBack(): #回复反馈反馈
    data=request.json
    result, status_code=SystemService.replyFeedBack(data)
    return jsonify(result), status_code
