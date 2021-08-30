FROM python:3.8.3-slim

MAINTAINER Jose Morales Lira <jmmorales@uc.cl>

WORKDIR /app
COPY requirements.txt requirements-dev.txt .
RUN apt-get update && \
    apt-get install -yy libpq-dev build-essential && \
    pip install -r requirements.txt -r requirements-dev.txt

COPY . .
CMD uvicorn app.main:app --host=0.0.0.0