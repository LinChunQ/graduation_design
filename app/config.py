from datetime import timedelta
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:QQ1314520@114.55.218.3:3306/uga-flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = 'uga12345678'
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = ''
    JSON_AS_ASCII= False  # 确保 JSON 响应中非 ASCII 字符不被转义
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)