FROM python:3
LABEL author=dagedan@gmail.com
ENV PYTHONUNBUFFERED 1
RUN mkdir /djangocode
WORKDIR /djangocode
COPY requirements.txt /djangocode/
RUN pip install -r requirements.txt
COPY . /djangocode/
