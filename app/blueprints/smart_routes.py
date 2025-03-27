from flask import request, jsonify, Blueprint
from app.services.smart_service import SmartService
from flask_jwt_extended import jwt_required, get_jwt_identity

smart_bp = Blueprint('smart', __name__, url_prefix='/smart')

#智能打分
@smart_bp.route('/grading', methods=['POST'])
@jwt_required()  # JWT 认证保护
def grading():
    user_id = get_jwt_identity()
    result, status_code=SmartService.grading(user_id)
    return jsonify(result), status_code