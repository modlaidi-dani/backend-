FROM python:3.12-slim

WORKDIR /opt/project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
ENV CORESETTING_IN_DOCKER true

RUN set -xe \
    && apt-get update \
    && apt-get install -y build-essential \
    && pip install --upgrade pip poetry virtualenvwrapper   \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY ["pyproject.toml", "poetry.lock", "./"]



RUN poetry run pip install pip

RUN poetry install --no-root

COPY ["LICENSE", "README.rst", "Makefile","./"]
COPY erp erp
COPY local local
RUN poetry install

EXPOSE 8000
