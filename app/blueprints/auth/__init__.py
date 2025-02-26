from flask import Blueprint

# 创建蓝图对象
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 导入路由（防止循环导入问题）
from . import routes
