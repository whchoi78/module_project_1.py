FROM apache/airflow:2.0.1
USER root
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && pip install --upgrade pip \
    && pip install bs4 \
    && pip install requests \
    && pip install pymysql
    #&& pip install -r requirements.txt