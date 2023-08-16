FROM python:3.8

RUN apt update

ARG USERNAME
ARG 

ARG NAME

RUN echo ${USERNAME}

RUN apt install python3 python3-pip python3-venv -y

RUN mkdir /opt/main

COPY . /opt/main

WORKDIR /opt/main

RUN pip install flask

RUN pip install flask_sqlalchemy

RUN pip install sqlalchemy_utils

RUN pip install pymysql

RUN pip install flask_wtf

RUN python3 create.py

ENTRYPOINT ["python3", "app.py"]