from flask import request, jsonify, Blueprint
from app.services.statis_service import StatisService
from flask_jwt_extended import jwt_required, get_jwt_identity

statis_bp = Blueprint('statis', __name__, url_prefix='/statis')
@statis_bp.route('/getStaById', methods=['POST'])
@jwt_required()
def getStaById(): # 创建课程
    user_id = get_jwt_identity()
    data=request.json
    result, status_code=StatisService.getStaById(data,user_id)
    return jsonify(result), status_code
