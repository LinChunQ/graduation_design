from flask import request, jsonify, Blueprint
from app.services.smart_service import SmartService
from flask_jwt_extended import jwt_required, get_jwt_identity

smart_bp = Blueprint('smart', __name__, url_prefix='/smart')

#智能打分
@jwt_required()  # JWT 认证保护
@smart_bp.route('/grading', methods=['POST'])
def grading():
    result, status_code=SmartService.grading()
    return jsonify(result), status_code