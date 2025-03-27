from flask import request, jsonify, Blueprint
from app.services.auth_service import AuthService
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 用户注册
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    sex = data.get('sex')
    age = data.get('age')
    phone = data.get('phone')
    address = data.get('address')
    school = data.get('school')
    profession = data.get('profession')

    result, status_code = AuthService.register(username, sex, age, email, phone, address, school, profession, password)
    return jsonify(result), status_code

# 用户登录
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    result, status_code = AuthService.login(username, password)
    return result, status_code

# 受保护路由（需要 JWT 令牌）
@auth_bp.route('/getUserInfo', methods=['GET'])
@jwt_required()  # JWT 认证保护
def getUserInfo():
    user_id = get_jwt_identity()
    result, status_code = AuthService.getUserInfo(user_id)
    return jsonify(result), status_code
@auth_bp.route('/updateUserInfo', methods=['POST'])
@jwt_required()
def updateUserInfo():
    user_id = get_jwt_identity()
    userInfo = request.json
    result, status_code = AuthService.updateUserInfo(userInfo,user_id)
    return jsonify(result), status_code