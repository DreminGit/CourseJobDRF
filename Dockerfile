FROM python:3.12.3-slim

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .