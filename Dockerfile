FROM python:3
LABEL author=dagedan@gmail.com
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangocode
WORKDIR /djangocode
COPY requirements.txt /djangocode/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider
COPY . /djangocode/

