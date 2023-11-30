# Utilise une image Python 3.11 de base.
FROM python:3.11-slim

COPY src/ /src
COPY requirements.txt /src/requirements.txt

WORKDIR /src

RUN apk --no-cache add gcc musl-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD [ "python", "main.py"]
