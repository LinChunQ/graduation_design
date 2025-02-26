class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:QQ1314520@localhost:3306/uga-flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    JWT_SECRET_KEY = 'uga12345678'
    JWT_HEADER_NAME = 'Token'
    JWT_HEADER_TYPE = ''

