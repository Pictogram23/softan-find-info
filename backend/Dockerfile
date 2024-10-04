FROM python:3.12.7-alpine3.20

WORKDIR /usr/src/app/backend

COPY /requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt