FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt

COPY interview /app


