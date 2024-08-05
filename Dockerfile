FROM python:3.11-alpine

WORKDIR /src

RUN apk add gcc
RUN apk add python3-dev

COPY requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY . /src







