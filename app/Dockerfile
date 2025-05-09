FROM python:3

# 设置 pip 镜像源为阿里云镜像
ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/

# 设置镜像源不验证 SSL
ENV PIP_TRUSTED_HOST=mirrors.aliyun.com

# 设置工作目录为项目根目录
WORKDIR /app

# 设置Python模块搜索路径（关键！）
ENV PYTHONPATH=/app

# 先安装依赖（利用Docker缓存层）
COPY requirements.txt .
RUN pip install -r requirements.txt

# 复制所有代码
COPY . /app

# 使用flask命令更可靠
ENV FLASK_APP=run.py

CMD ["flask", "run", "--host=0.0.0.0"]
