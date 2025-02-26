#高校阅卷助手 后端
##
univeristyGradingAssistant/
│
├── app/
│   ├── __init__.py              # 初始化Flask应用
│   ├── config.py                # 配置文件
│   ├── routes.py                # 统一路由文件，定义所有API接口
│   ├── models.py                # 数据库模型文件
│   ├── services/                # 存放服务类，处理业务逻辑
│   │   ├── user_service.py      # 处理与用户相关的服务（登录、信息等）
│   │   ├── grading_service.py   # 处理自动阅卷服务（图片识别、数据保存等）
│   │   └── display_service.py   # 处理数据展示的服务
│   ├── utils/                   # 工具类，存放通用功能
│   │   ├── image_utils.py       # 图像处理相关的工具类
│   │   └── file_utils.py        # 文件操作相关工具类
│   ├── auth/                    # 用户认证与权限管理相关
│   │   ├── __init__.py          # 初始化认证模块
│   │   ├── jwt_auth.py          # JWT认证相关功能
│   │   └── password_utils.py    # 密码加密与验证
│ 
│ 
│
│
├── requirements.txt             # 项目依赖
├── run.py                       # 启动Flask应用
├── migrations/                  # 数据库迁移（如果使用SQLAlchemy）
│
│
└── README.md                    # 项目的说明文档

#从0-1:
2025/2/5:搭建后端基本框架、实现用户登录模块
2025/2/6:改善框架，完成注册，登录模块