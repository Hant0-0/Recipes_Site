FROM python:3.10-alpine3.17

COPY requirements.txt /temp/requirements.txt
COPY recipes /recipes
WORKDIR /recipes
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password recipes-user

USER recipes-user