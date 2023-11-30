# Utilise une image Python 3.11 de base.
FROM python:3.11-slim

COPY src/ /src
COPY requirements.txt /src/requirements.txt

WORKDIR /src

RUN apk --no-cache add build-base && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base

CMD [ "python", "main.py"]
