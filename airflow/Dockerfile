FROM apache/airflow:2.0.1
USER root
RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && pip install --upgrade pip \
    && pip install -r requirements.txt