# Utilise une image Python 3.11 de base.
FROM python:3.11

COPY src/ /src
COPY requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt 

CMD [ "python", "main.py"]
