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
    phone = data.get('phone')
    school = data.get('school')
    profession = data.get('profession')
    captcha=data.get('captcha')
    result, status_code = AuthService.register(username,email, phone, school, profession, password,captcha)
    return jsonify(result), status_code

#注册获取验证码
@auth_bp.route('/getCaptcha',methods=['POST'])
def getCaptcha():
    data=request.json
    email=data.get('email')
    result, status_code = AuthService.get_email_captcha(email)
    return jsonify(result), status_code

# 用户登录
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    result, status_code = AuthService.login(username, password,role)
    return result, status_code

# 获取用户信息（需要 JWT 令牌）
@auth_bp.route('/getUserInfo', methods=['POST'])
@jwt_required()  # JWT 认证保护
def getUserInfo():
    user_id = get_jwt_identity()
    role = request.json.get('role')
    result, status_code = AuthService.getUserInfo(user_id,role)
    return jsonify(result), status_code

#更新用户信息（需要 JWT 令牌）
@auth_bp.route('/updateUserInfo', methods=['POST'])
@jwt_required()
def updateUserInfo():
    user_id = get_jwt_identity()
    data=request.json
    userInfo = data.get('userInfo')
    role=data.get('role')
    result, status_code = AuthService.updateUserInfo(userInfo,user_id,role)
    return jsonify(result), status_code