FROM python:3
LABEL author=dagedan@gmail.com
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangocode
WORKDIR /djangocode
ADD . /djangocode
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider
# Windows环境下编写的start.sh每行命令结尾有多余的\r字符，需移除。
RUN sed -i 's/\r//' ./start.sh

# 设置start.sh文件可执行权限
RUN chmod +x ./start.sh

