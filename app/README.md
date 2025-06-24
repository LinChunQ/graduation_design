## pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple pymysql  //镜像源使用样例

## 高校阅卷助手 后端
app
├── blueprints              #蓝图(路由层相当于SpringBoot的controller层)
│   ├── auth_routes.py              
│   ├── smart_routes.py
│   ├── statis_routers.py
│   └── user_routes.py
├── common
│   └── request
│       └── response.py
├── config.py               #配置文件
├── Dockerfile              #docker的配置文件
├── extensions.py           #拓展
├── __init__.py             #初始化文件
├── models                  #模型(一些类)
│   ├── admin.py
│   ├── course.py
│   ├── email_captcha.py
│   ├── exam_images.py
│   ├── feedback.py
│   ├── notice.py
│   ├── statistics.py
│   ├── sub_sta.py
│   ├── test_paper.py
│   └── user.py
├── README.md               # 项目的说明文档
├── requirements.txt        # 项目依赖 
├── run.py                  # 启动Flask应用 
├── services                #服务层(具体业务实现)
│   ├── auth_service.py
│   ├── smart_service.py
│   ├── statis_service.py
│   └── user_service.py
└── utils                   #工具类
    └── MyTool.py



