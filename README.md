## 高校阅卷助手 后端项目结构
app/
├── blueprints/* # 蓝图（路由层，类似 SpringBoot 的 controller 层）
├── common/*
├── config.py # 配置文件（数据库、Redis 等）
├── Dockerfile # Docker 构建配置
├── extensions.py # Flask 插件拓展（如 SQLAlchemy、Redis 初始化等）
├── init.py # Flask 应用初始化入口
├── models/* # 模型层（ORM 类）
├── README.md # 项目说明文档
├── requirements.txt # Python 依赖列表
├── run.py # 启动 Flask 应用的主脚本
├── services/* # 服务层（业务逻辑处理）
└── utils/* # 工具类

## 前端项目结构
src
├─apis/* # 对应后端接口
├─assets/* # 静态资源
├─components/* # 组件
├─router/* #路由配置
├─stores/* #pinia状态
├─utils/* #工具配置
│  ├─i18n
│  │  └─language
│  └─request
└─views #各个模块页面
    ├─About
    ├─DataCenter
    ├─FeedBack
    ├─Help
    ├─Home
    ├─Notice
    ├─SmartCorrections
    ├─Statistics
    └─User
