# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
EXPOSE 80

WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt

COPY ./ /code/

CMD python3 -m flask run --host=0.0.0.0 --port=80