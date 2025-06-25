## 高校阅卷助手 
## 后端项目结构(python+flask+mysql+redis)

app/
├── blueprints/           # 蓝图（路由层，类似 SpringBoot 的 controller 层）
├── common/               # 通用模块（如请求封装）
├── config.py             # 配置文件（数据库、Redis 等）
├── Dockerfile            # Docker 构建配置
├── extensions.py         # Flask 插件扩展（如 SQLAlchemy、Redis 初始化）
├── init.py               # Flask 应用初始化入口
├── models/               # 模型层（ORM 类）
├── README.md             # 项目说明文档
├── requirements.txt      # Python 依赖列表
├── run.py                # 启动 Flask 应用的主脚本
├── services/             # 服务层（业务逻辑处理）
└── utils/                # 工具类


## 前端项目结构(vue3+pinia+element-plus)
src/
├── apis/                 # 封装的 API 接口调用
├── assets/               # 静态资源（图片、样式等）
├── components/           # Vue 组件
├── router/               # Vue Router 配置
├── stores/               # 状态管理（Pinia）
├── utils/                # 工具配置
│   ├── i18n/             # 多语言支持
│   │   └── language/     # 多语言文件夹
│   └── request/          # Axios 请求封装
└── views/                # 各模块页面
    ├── About/            # 关于页面
    ├── DataCenter/       # 数据中心
    ├── FeedBack/         # 用户反馈
    ├── Help/             # 帮助中心
    ├── Home/             # 首页
    ├── Notice/           # 公告模块
    ├── SmartCorrections/ # 智能阅卷
    ├── Statistics/       # 数据统计
    └── User/             # 用户管理
    
作品展示地址：http://114.55.218.3:8080/
