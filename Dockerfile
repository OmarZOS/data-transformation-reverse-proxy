FROM python:3.8-alpine

RUN python3 -m pip install flask

WORKDIR /code

COPY . /code


CMD ["flask","run"]