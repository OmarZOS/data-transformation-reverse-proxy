FROM python:3.8-alpine

WORKDIR /code

COPY . /code

RUN pip3 install -r requirements.txt

CMD ["uvicorn","--host","0.0.0.0","server:app","--reload"]