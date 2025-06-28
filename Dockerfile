FROM python:3.12.3-slim

RUN apt-get update && apt-get -y install libpq-dev gcc

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

ENTRYPOINT []