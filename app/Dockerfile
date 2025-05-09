FROM python:3

# 设置 pip 镜像源为阿里云镜像
ENV PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/

# 设置镜像源不验证 SSL
ENV PIP_TRUSTED_HOST=mirrors.aliyun.com

#工作目录
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# 设置 Flask 环境变量
ENV FLASK_APP=app.py

EXPOSE 9000

# 启动 Flask 应用
CMD ["python", "run.py", "--host=0.0.0.0"]

